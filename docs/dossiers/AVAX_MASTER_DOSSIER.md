# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:51:14 IST` (`2026-10-29 20:21:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.70` | **Live Ask Quote**: `8.74` | **Mid Price**: `8.72`
- **Spread Points**: `4.00` | **Spread BPS**: `45.87 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.76` | VWAP Z-Score: `+0.55` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0499` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `49.17` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.13` | Lower -3.00σ Band: `8.40`
  * Upper +2.51σ Band: `9.07` | Lower -2.51σ Band: `8.46`
  * Upper +2.01σ Band: `9.01` | Lower -2.01σ Band: `8.52`
  * Upper +2.00σ Band: `9.01` | Lower -2.00σ Band: `8.52`
  * Upper +1.28σ Band: `8.92` | Lower -1.28σ Band: `8.61`
  * Upper +1.00σ Band: `8.89` | Lower -1.00σ Band: `8.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.83` | EMA-20=`8.84` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.82` (Slope: `+0.0000`) | EMA-100=`8.81`
  * Institutional Anchors: EMA-144=`8.82` | EMA-200=`8.82` (Slope: `+0.0121`) | EMA-233=`8.83`
- **Range Boundaries**: 24H High=`9.14` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.90` (Distance: `-2.01%`)
  * Point of Control (POC) = `8.74` (Distance: `-0.23%`)
  * Value Area Low (VAL) = `8.58` (Distance: `+1.62%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `8.69` - `8.75`
  * Optimal Trade Entry (OTE 0.705): `8.74`
  * Structural Invalidation Anchor (0.786): `8.79`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.85` | `8.86` | `8.70` | `8.70` | `317,287` | 2,781,950.83 USD | -851,934.67 USD | `-30.62%` | -5,136,551.23 USD | `-4.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.70` | `8.74` | `8.65` | `8.71` | `234,662` | 2,039,581.77 USD | 326,257.17 USD | `+16.00%` | -4,810,294.06 USD | `+1.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.71` | `8.74` | `8.68` | `8.72` | `78,861` | 687,335.62 USD | 98,346.50 USD | `+14.31%` | -4,711,947.56 USD | `+0.50` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.83` | `8.87` | `8.83` | `8.85` | `66,310` | 587,148.06 USD | 200,256.54 USD | `+34.11%` | -4,233,883.87 USD | `+0.99` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.85` | `8.87` | `8.84` | `8.85` | `48,790` | 431,773.06 USD | -50,732.69 USD | `-11.75%` | -4,284,616.56 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.85` | `8.86` | `8.65` | `8.72` | `630,853` | 5,509,243.40 USD | -427,706.18 USD | `-7.76%` | -4,712,322.74 USD | `-0.85` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.87` | `8.89` | `8.79` | `8.84` | `435,467` | 3,847,058.68 USD | -67,411.45 USD | `-1.75%` | -4,291,060.73 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.84` | `8.87` | `8.80` | `8.85` | `249,668` | 2,205,666.85 USD | 221,936.79 USD | `+10.06%` | -4,069,123.94 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.85` | `8.86` | `8.65` | `8.72` | `630,810` | 5,508,868.22 USD | -427,331.00 USD | `-7.76%` | -4,496,454.94 USD | `-0.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.65` | `8.72` | `630,810` | 5,508,868.22 USD | -427,331.00 USD | `-7.76%` | -5,093,341.98 USD | `+0.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.65` | `8.72` | `630,810` | 5,508,868.22 USD | -427,331.00 USD | `-7.76%` | -5,093,341.98 USD | `+0.36` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.72`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.72` | `48.1600` | 420.18 USD | 2,019.83 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.72` | `48.1600` | 420.16 USD | 2,439.99 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.72` | `96.2900` | 840.00 USD | 3,279.98 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `8.72` | `20.5800` | 179.53 USD | 3,459.51 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.72` | `48.1600` | 420.09 USD | 3,879.61 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.72` | `48.1600` | 420.07 USD | 4,299.67 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.72` | `433.8300` | 3,783.78 USD | 8,083.45 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.72` | `48.1700` | 420.12 USD | 8,503.58 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.72` | `1380.2000` | 12,037.41 USD | 20,540.99 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.72` | `158.9500` | 1,386.25 USD | 21,927.24 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.72` | `48.1500` | 419.91 USD | 22,347.15 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.72` | `107.5000` | 937.49 USD | 23,284.64 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.72` | `53.5300` | 466.80 USD | 23,751.44 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `8.72` | `57.3100` | 499.76 USD | 24,251.20 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.72` | `114.6700` | 999.92 USD | 25,251.12 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.72` | `492.3200` | 4,292.98 USD | 29,544.11 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `8.72` | `48.1700` | 420.03 USD | 29,964.13 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.72` | `28.6500` | 249.81 USD | 30,213.94 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.72` | `48.1600` | 419.92 USD | 30,633.87 USD | `1 orders` | `-0.09%` | `-` |
| `ASK` | `8.73` | `78.6200` | 686.53 USD | 57,332.41 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.73` | `1380.2000` | 12,052.18 USD | 56,645.87 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.73` | `520.8500` | 4,548.11 USD | 44,593.69 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `8.73` | `1145.2400` | 10,000.24 USD | 40,045.58 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.73` | `56.5800` | 494.05 USD | 30,045.34 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.73` | `48.1600` | 420.52 USD | 29,551.30 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.73` | `137.5600` | 1,201.06 USD | 29,130.78 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.73` | `244.8400` | 2,137.72 USD | 27,929.71 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `8.73` | `48.1600` | 420.48 USD | 25,791.99 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.73` | `28.7200` | 250.74 USD | 25,371.51 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.73` | `119.9000` | 1,046.77 USD | 25,120.77 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.73` | `65.5400` | 572.17 USD | 24,073.99 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.73` | `1116.3800` | 9,746.00 USD | 23,501.82 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.73` | `48.1600` | 420.43 USD | 13,755.82 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.73` | `23.0400` | 201.13 USD | 13,335.39 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.73` | `733.0300` | 6,398.84 USD | 13,134.26 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `8.73` | `103.8600` | 906.61 USD | 6,735.42 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `8.73` | `120.0800` | 1,048.19 USD | 5,828.81 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.73` | `526.8900` | 4,599.06 USD | 4,780.62 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.73` | `20.8000` | 181.55 USD | 181.55 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.73` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.73` | `0.00%` | `-` |
| `BID` | `8.73` | `183.3200` | 1,599.65 USD | 1,599.65 USD | `1 orders` | `-0.01%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1505` | `0x7737...bf66` | `SHORT` | 1,498,235.24 USD | `171,568.06` | `7.43` | `8.76` | `109.67` | -222,690.22 USD | `-14.86%` | `10X Cross` |
| `1589` | `0xeadc...9d55` | `LONG` | 1,397,383.97 USD | `160,070.56` | `8.11` | `8.76` | `0.000000` | 99,746.40 USD | `+7.14%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.22` (Vol: 293,800.00 USD, Dist: `+5.46%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`9.22` (Vol: 221,300.00 USD, Dist: `+5.49%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--3.26%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 264,100.00 USD, Dist: `+5.49%`) | Long MP=`8.55` (Vol: 152,200.00 USD, Dist: `--2.20%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 419,200.00 USD, Dist: `+6.17%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--2.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.85` | 204.05 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 102.18 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 1,910.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 262.35 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 391.63 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 918.27 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 17,160.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 282.66 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 270.19 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 627.44 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 140.18 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 1,230.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 1,520.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 404.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 109.42 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 712.82 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 297.24 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 325.98 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.96` | 8,990.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 371.88 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.01` | 401.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.08` | 2,320.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 1,130.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.22` | 171.58 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.26` | 106.63 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 115.97 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.42` | 2,230.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.64` | 223.98 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 9,060.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 240.48 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.79` | 5,050.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.82` | 17,120.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 113.33 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 146.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 329.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 805.91 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 4,200.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.14` | 156,590.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 2,650.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 22,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.66` | 4,160.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 406.45 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 869.71 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 327,670.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 640.67 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 336.30 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 12,120.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 3,060.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,550.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 3,200.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 2,500.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 4,150.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 147.51 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 1,740.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 894,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 889,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 1,700.00 USD | 889,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 887,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 881,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 880,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 876,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 867,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.61` | 409.51 USD | 866,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 865,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,190.00 USD | 863,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 861,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 861,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 844,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 843,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 836,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 819,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 815,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 813,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 811,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,410.00 USD | 810,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 18,930.00 USD | 806,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 787,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,380.00 USD | 784,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 782,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 777,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 27,700.00 USD | 777,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 749,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 745,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 742,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 741,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 20,860.00 USD | 740,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 1,530.00 USD | 720,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 3,390.00 USD | 718,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 715,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 711,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 704,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 29,850.00 USD | 702,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 672,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 672,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 670,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 649,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 581.02 USD | 647,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.22` | 833.26 USD | 647,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 646,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 646,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 646,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 19,790.00 USD | 609,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 168.76 USD | 589,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 5,050.00 USD | 589,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 584,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 582,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 577,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 572,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 568,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 2,590.00 USD | 550,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 500.00 USD | 547,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 1,490.00 USD | 547,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 545,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 545,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 9,160.00 USD | 544,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 535,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 531,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 530,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 529,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 528,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 523,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 4,380.00 USD | 523,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 519,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 494,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 493,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 493,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 492,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 492,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 490,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 489,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,760.00 USD | 488,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 468,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 465,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 465,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.77` | 9,420,000.00 USD | 9,420,000.00 USD | 18,150.00 USD | 10,660.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 464,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 463,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,760,000.00 USD | 4,760,000.00 USD | 65,890.00 USD | 11,370.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.79` | 9,380,000.00 USD | 9,380,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 459,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 458,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,670,000.00 USD | 4,670,000.00 USD | 6,130.00 USD | 7,800.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.81` | 9,340,000.00 USD | 9,340,000.00 USD | 2,240.00 USD | 11,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 457,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,650,000.00 USD | 4,650,000.00 USD | 4,150.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 9,330,000.00 USD | 9,330,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 452,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,630,000.00 USD | 4,630,000.00 USD | 4,570.00 USD | 1,820.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 9,270,000.00 USD | 9,270,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 441,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 439,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,620,000.00 USD | 4,620,000.00 USD | 23,470.00 USD | 3,090.00 USD | 22,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 9,240,000.00 USD | 9,240,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 438,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,570,000.00 USD | 4,570,000.00 USD | 21,240.00 USD | 9,580.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 9,180,000.00 USD | 9,180,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 438,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,530,000.00 USD | 4,530,000.00 USD | 11,920.00 USD | 3,480.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 9,110,000.00 USD | 9,110,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,510,000.00 USD | 4,510,000.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 9,060,000.00 USD | 9,060,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 437,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 436,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,480,000.00 USD | 4,480,000.00 USD | 11,610.00 USD | 9,310.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 8,960,000.00 USD | 8,960,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 308,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,450,000.00 USD | 4,450,000.00 USD | 13,510.00 USD | 5,620.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 8,860,000.00 USD | 8,860,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 308,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,430,000.00 USD | 4,430,000.00 USD | 4,090.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 8,770,000.00 USD | 8,770,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 306,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,420,000.00 USD | 4,420,000.00 USD | 6,600.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 8,670,000.00 USD | 8,670,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 306,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,410,000.00 USD | 4,410,000.00 USD | 17,700.00 USD | 2,310.00 USD | 297.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 8,600,000.00 USD | 8,600,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 305,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 216,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,380,000.00 USD | 4,380,000.00 USD | 24,220.00 USD | 3,770.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 8,420,000.00 USD | 8,420,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 210,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 206,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 4,350,000.00 USD | 4,350,000.00 USD | 13,130.00 USD | 4,100.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 8,290,000.00 USD | 8,290,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 168,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 4,330,000.00 USD | 4,330,000.00 USD | 14,060.00 USD | 2,630.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 8,140,000.00 USD | 8,140,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 11,700.00 USD | 168,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,300,000.00 USD | 4,300,000.00 USD | 13,850.00 USD | 6,970.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 8,060,000.00 USD | 8,060,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 156,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,270,000.00 USD | 4,270,000.00 USD | 10,810.00 USD | 0.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 8,010,000.00 USD | 8,010,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,250,000.00 USD | 4,250,000.00 USD | 28,020.00 USD | 662.47 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 7,940,000.00 USD | 7,940,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 156,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,220,000.00 USD | 4,220,000.00 USD | 3,360.00 USD | 0.00 USD | 59.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 7,800,000.00 USD | 7,800,000.00 USD | 6,560.00 USD | 7,770.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.18` | 235.36 USD | 155,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,220,000.00 USD | 4,220,000.00 USD | 5,590.00 USD | 0.00 USD | 469.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 7,780,000.00 USD | 7,780,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,050.00 USD | 155,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,210,000.00 USD | 4,210,000.00 USD | 3,540.00 USD | 0.00 USD | 445.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 7,740,000.00 USD | 7,740,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 152,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 152,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,210,000.00 USD | 4,210,000.00 USD | 26,390.00 USD | 4,080.00 USD | 41,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 7,710,000.00 USD | 7,710,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 149,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 148,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,140,000.00 USD | 4,140,000.00 USD | 18,270.00 USD | 1,150.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 7,580,000.00 USD | 7,580,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 147,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,110,000.00 USD | 4,110,000.00 USD | 11,530.00 USD | 14,210.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 7,510,000.00 USD | 7,510,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,740.00 USD | 133,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 123,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,080,000.00 USD | 4,080,000.00 USD | 109,350.00 USD | 16,540.00 USD | 45,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 7,430,000.00 USD | 7,430,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 123,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 104,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 3,910,000.00 USD | 3,910,000.00 USD | 109,200.00 USD | 24,540.00 USD | 20,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 7,240,000.00 USD | 7,240,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 71,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.33` | 3,760,000.00 USD | 3,760,000.00 USD | 27,740.00 USD | 27,890.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 7,140,000.00 USD | 7,140,000.00 USD | 58,510.00 USD | 36,210.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,760.00 USD | 66,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.35` | 3,680,000.00 USD | 3,680,000.00 USD | 21,290.00 USD | 16,080.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 7,020,000.00 USD | 7,020,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 61,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,390.00 USD | 58,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 3,620,000.00 USD | 3,620,000.00 USD | 26,050.00 USD | 11,480.00 USD | 30,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 6,840,000.00 USD | 6,840,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 4,620.00 USD | 51,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 3,560,000.00 USD | 3,560,000.00 USD | 99,370.00 USD | 14,620.00 USD | 90,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 6,690,000.00 USD | 6,690,000.00 USD | 197,900.00 USD | 8,930.00 USD | 68,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 46,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.40` | 1,380.00 USD | 44,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 3,350,000.00 USD | 3,350,000.00 USD | 100,580.00 USD | 29,160.00 USD | 88,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 6,410,000.00 USD | 6,410,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.41` | 681.03 USD | 43,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.43` | 3,130,000.00 USD | 3,130,000.00 USD | 63,260.00 USD | 47,320.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 6,010,000.00 USD | 6,010,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 42,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 42,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 2,990,000.00 USD | 2,990,000.00 USD | 108,590.00 USD | 25,950.00 USD | 54,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 5,700,000.00 USD | 5,700,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 422.16 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,860.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 2,800,000.00 USD | 2,800,000.00 USD | 274,020.00 USD | 47,840.00 USD | 68,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 5,340,000.00 USD | 5,340,000.00 USD | 426,960.00 USD | 70,760.00 USD | 200,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 27,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 2,410,000.00 USD | 2,410,000.00 USD | 267,220.00 USD | 76,720.00 USD | 60,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 4,640,000.00 USD | 4,640,000.00 USD | 283,720.00 USD | 54,550.00 USD | 118,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 26,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,000,000.00 USD | 2,000,000.00 USD | 96,210.00 USD | 63,330.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 4,180,000.00 USD | 4,180,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.53` | 1,790,000.00 USD | 1,790,000.00 USD | 66,040.00 USD | 46,880.00 USD | 65,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 3,690,000.00 USD | 3,690,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 1,620,000.00 USD | 1,620,000.00 USD | 83,340.00 USD | 27,440.00 USD | 62,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 2,870,000.00 USD | 2,870,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.57` | 1,440,000.00 USD | 1,440,000.00 USD | 142,880.00 USD | 23,160.00 USD | 141,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 2,440,000.00 USD | 2,440,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,140,000.00 USD | 1,140,000.00 USD | 158,140.00 USD | 56,580.00 USD | 65,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 1,560,000.00 USD | 1,560,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 855,060.00 USD | 855,060.00 USD | 103,430.00 USD | 36,000.00 USD | 55,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.61` | 1,070,000.00 USD | 1,070,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 660,310.00 USD | 660,310.00 USD | 180,480.00 USD | 44,210.00 USD | 42,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.63` | 721,200.00 USD | 721,200.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 392,660.00 USD | 392,660.00 USD | 156,430.00 USD | 43,300.00 USD | 52,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.65` | 620,650.00 USD | 620,650.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 140,730.00 USD | 140,730.00 USD | 0.00 USD | 0.00 USD | 42,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.67` | 382,600.00 USD | 382,600.00 USD | 77,920.00 USD | 24,870.00 USD | 173,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.69` | 98,300.00 USD | 98,300.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.69` | 105,900.00 USD | 105,900.00 USD | 70,550.00 USD | 12,790.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.71` | 71,600.00 USD | 71,600.00 USD | 52,630.00 USD | 0.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 50,120.00 USD | 50,120.00 USD | 44,990.00 USD | 0.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 100,230.00 USD | 100,230.00 USD | 44,990.00 USD | 0.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 168,140.00 USD | 168,140.00 USD | 32,080.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 220,950.00 USD | 220,950.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 326,690.00 USD | 326,690.00 USD | 132,830.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.77` | 329,000.00 USD | 329,000.00 USD | 26,810.00 USD | 0.00 USD | 81,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 380,810.00 USD | 380,810.00 USD | 32,240.00 USD | 12,000.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.79` | 381,660.00 USD | 381,660.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 386,500.00 USD | 386,500.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.81` | 390,110.00 USD | 390,110.00 USD | 0.00 USD | 8,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 464,430.00 USD | 464,430.00 USD | 10,770.00 USD | 2,250.00 USD | 64,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 466,580.00 USD | 466,580.00 USD | 0.00 USD | 2,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 434,590.00 USD | 434,590.00 USD | 0.00 USD | 0.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 544,350.00 USD | 544,350.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 505,590.00 USD | 505,590.00 USD | 0.00 USD | 0.00 USD | 71,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 555,910.00 USD | 555,910.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 561,220.00 USD | 561,220.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 648,270.00 USD | 648,270.00 USD | 40,450.00 USD | 36,070.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 599,820.00 USD | 599,820.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 713,420.00 USD | 713,420.00 USD | 38,030.00 USD | 5,120.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 842,050.00 USD | 842,050.00 USD | 185,270.00 USD | 36,180.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 918,810.00 USD | 918,810.00 USD | 106,640.00 USD | 66,510.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 1,020,000.00 USD | 1,020,000.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 1,030,000.00 USD | 1,030,000.00 USD | 22,480.00 USD | 37,250.00 USD | 49,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 1,110,000.00 USD | 1,110,000.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 1,140,000.00 USD | 1,140,000.00 USD | 41,700.00 USD | 25,630.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 1,150,000.00 USD | 1,150,000.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 1,340,000.00 USD | 1,340,000.00 USD | 101,210.00 USD | 23,610.00 USD | 75,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 1,440,000.00 USD | 1,440,000.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 1,550,000.00 USD | 1,550,000.00 USD | 118,620.00 USD | 34,700.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 2,880,000.00 USD | 2,880,000.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 1,840,000.00 USD | 1,840,000.00 USD | 190,770.00 USD | 51,740.00 USD | 46,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 4,080,000.00 USD | 4,080,000.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 2,010,000.00 USD | 2,010,000.00 USD | 91,780.00 USD | 30,600.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 4,720,000.00 USD | 4,720,000.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 2,300,000.00 USD | 2,300,000.00 USD | 170,750.00 USD | 37,660.00 USD | 80,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 5,550,000.00 USD | 5,550,000.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,630,000.00 USD | 2,630,000.00 USD | 178,200.00 USD | 76,590.00 USD | 73,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 6,350,000.00 USD | 6,350,000.00 USD | 503,250.00 USD | 101,150.00 USD | 193,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,860,000.00 USD | 2,860,000.00 USD | 141,440.00 USD | 15,610.00 USD | 66,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 7,310,000.00 USD | 7,310,000.00 USD | 554,780.00 USD | 132,850.00 USD | 277,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 3,810.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.23` | 3,050,000.00 USD | 3,050,000.00 USD | 134,640.00 USD | 13,360.00 USD | 45,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 8,330,000.00 USD | 8,330,000.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 3,120,000.00 USD | 3,120,000.00 USD | 49,760.00 USD | 8,330.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 8,830,000.00 USD | 8,830,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 3,160,000.00 USD | 3,160,000.00 USD | 39,300.00 USD | 4,490.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 9,160,000.00 USD | 9,160,000.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 3,220,000.00 USD | 3,220,000.00 USD | 36,690.00 USD | 8,000.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 10,020,000.00 USD | 10,020,000.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,320,000.00 USD | 3,320,000.00 USD | 70,040.00 USD | 13,670.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 10,650,000.00 USD | 10,650,000.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 3,360,000.00 USD | 3,360,000.00 USD | 16,620.00 USD | 8,530.00 USD | 15,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 11,020,000.00 USD | 11,020,000.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,450,000.00 USD | 3,450,000.00 USD | 44,830.00 USD | 8,000.00 USD | 33,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 11,500,000.00 USD | 11,500,000.00 USD | 289,480.00 USD | 88,340.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,570,000.00 USD | 3,570,000.00 USD | 67,060.00 USD | 24,480.00 USD | 26,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 11,970,000.00 USD | 11,970,000.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,640,000.00 USD | 3,640,000.00 USD | 48,890.00 USD | 4,040.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 12,330,000.00 USD | 12,330,000.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,730,000.00 USD | 3,730,000.00 USD | 65,590.00 USD | 2,860.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 12,780,000.00 USD | 12,780,000.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,770,000.00 USD | 3,770,000.00 USD | 20,770.00 USD | 2,260.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 13,020,000.00 USD | 13,020,000.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,770,000.00 USD | 3,770,000.00 USD | 2,220.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 13,160,000.00 USD | 13,160,000.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,780,000.00 USD | 3,780,000.00 USD | 3,280.00 USD | 5,690.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 13,260,000.00 USD | 13,260,000.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,820,000.00 USD | 3,820,000.00 USD | 22,170.00 USD | 572.85 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 13,340,000.00 USD | 13,340,000.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.49` | 428.79 USD | 415,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,830,000.00 USD | 3,830,000.00 USD | 12,280.00 USD | 3,160.00 USD | 124.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 13,640,000.00 USD | 13,640,000.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,880,000.00 USD | 3,880,000.00 USD | 35,960.00 USD | 7,630.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 13,850,000.00 USD | 13,850,000.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,900,000.00 USD | 3,900,000.00 USD | 8,810.00 USD | 7,800.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 13,900,000.00 USD | 13,900,000.00 USD | 28,850.00 USD | 17,400.00 USD | 880.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,920,000.00 USD | 3,920,000.00 USD | 6,120.00 USD | 4,390.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 14,060,000.00 USD | 14,060,000.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,940,000.00 USD | 3,940,000.00 USD | 5,940.00 USD | 1,820.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 14,120,000.00 USD | 14,120,000.00 USD | 26,920.00 USD | 15,650.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 3,990,000.00 USD | 3,990,000.00 USD | 24,220.00 USD | 3,090.00 USD | 22,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 14,250,000.00 USD | 14,250,000.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 4,010,000.00 USD | 4,010,000.00 USD | 11,660.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.63` | 14,300,000.00 USD | 14,300,000.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 4,030,000.00 USD | 4,030,000.00 USD | 11,480.00 USD | 5,210.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.65` | 14,370,000.00 USD | 14,370,000.00 USD | 33,020.00 USD | 20,230.00 USD | 18,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 4,050,000.00 USD | 4,050,000.00 USD | 11,920.00 USD | 3,480.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 14,450,000.00 USD | 14,450,000.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.69` | 4,080,000.00 USD | 4,080,000.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 14,620,000.00 USD | 14,620,000.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 4,110,000.00 USD | 4,110,000.00 USD | 11,610.00 USD | 9,310.00 USD | 8,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 14,770,000.00 USD | 14,770,000.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.73` | 4,120,000.00 USD | 4,120,000.00 USD | 2,760.00 USD | 3,700.00 USD | 13.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 14,780,000.00 USD | 14,780,000.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 415,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.75` | 4,130,000.00 USD | 4,130,000.00 USD | 10,750.00 USD | 1,920.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.75` | 14,860,000.00 USD | 14,860,000.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.76` | 549.11 USD | 415,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.77` | 4,140,000.00 USD | 4,140,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 14,970,000.00 USD | 14,970,000.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.78` | 470.18 USD | 416,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.79` | 4,150,000.00 USD | 4,150,000.00 USD | 5,640.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.79` | 15,040,000.00 USD | 15,040,000.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.80` | 4,160,000.00 USD | 4,160,000.00 USD | 6,680.00 USD | 770.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.81` | 15,210,000.00 USD | 15,210,000.00 USD | 103,830.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.83` | 15,340,000.00 USD | 15,340,000.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.85` | 15,440,000.00 USD | 15,440,000.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.87` | 15,490,000.00 USD | 15,490,000.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.89` | 15,570,000.00 USD | 15,570,000.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.91` | 15,620,000.00 USD | 15,620,000.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.93` | 15,680,000.00 USD | 15,680,000.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.95` | 15,770,000.00 USD | 15,770,000.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.97` | 15,820,000.00 USD | 15,820,000.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.99` | 15,840,000.00 USD | 15,840,000.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.01` | 15,860,000.00 USD | 15,860,000.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.03` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.09` | 113.76 USD | 416,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.15` | 6,890.00 USD | 423,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 7,330.00 USD | 430,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.23` | 114.12 USD | 430,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 434,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 434,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 434,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.74` | 37,210.00 USD | 472,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 474,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 481,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,810.00 USD | 492,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 504,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.65` | 776.22 USD | 505,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.78` | 58,870.00 USD | 564,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.96` | 1,360.00 USD | 566,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.12` | 620.17 USD | 566,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 568,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 568,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.63` | 430.85 USD | 569,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 570,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 36,850.00 USD | 606,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.95` | 14,500.00 USD | 621,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 102.68 USD | 621,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 709,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 234,840.00 USD | 944,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 948,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 948,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 948,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.73` | 160.01 USD | 948,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.10` | 3,910.00 USD | 952,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 953,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.71` | 241.31 USD | 953,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.81` | 292.30 USD | 954,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.84` | 2,460.00 USD | 956,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.86` | 320.13 USD | 956,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 957,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 957,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 977,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.45` | 154,450.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.70` | 111.59 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.29` | 263,950.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.48` | 22,650.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.70` | 84,150.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 162.26 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.77` | 340.87 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 4,930.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.66` | 2,660.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.70` | 108.89 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.85` | 2,320,000.00 USD | 0.00 USD | 204.05 USD | `-79.04%` | `110.00` |
| `Live` | `Long` | `1.97` | 2,320,000.00 USD | 0.00 USD | 102.18 USD | `-77.80%` | `52.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 159.60 USD | `-77.46%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,320,000.00 USD | 0.00 USD | 110.52 USD | `-77.01%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,320,000.00 USD | 0.00 USD | 1,910.00 USD | `-76.78%` | `929.47` |
| `Live` | `Long` | `2.06` | 2,310,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.67%` | `2,382.76` |
| `Live` | `Long` | `2.38` | 2,310,000.00 USD | 0.00 USD | 262.35 USD | `-73.05%` | `110.00` |
| `Live` | `Long` | `2.40` | 2,310,000.00 USD | 0.00 USD | 391.63 USD | `-72.83%` | `162.84` |
| `Live` | `Long` | `2.42` | 2,310,000.00 USD | 0.00 USD | 918.27 USD | `-72.60%` | `378.67` |
| `Live` | `Long` | `2.46` | 2,310,000.00 USD | 0.00 USD | 17,160.00 USD | `-72.26%` | `6,990.57` |
| `Live` | `Long` | `2.73` | 2,290,000.00 USD | 0.00 USD | 282.66 USD | `-69.21%` | `103.73` |
| `Live` | `Long` | `2.75` | 2,290,000.00 USD | 0.00 USD | 270.19 USD | `-68.99%` | `98.43` |
| `Live` | `Long` | `2.81` | 2,290,000.00 USD | 0.00 USD | 627.44 USD | `-68.19%` | `222.89` |
| `Live` | `Long` | `2.83` | 2,290,000.00 USD | 0.00 USD | 140.18 USD | `-68.08%` | `49.62` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 232.67 USD | `-67.63%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 44,510.00 USD | `-66.84%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.39%` | `415.06` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 1,520.00 USD | `-63.56%` | `470.82` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 404.38 USD | `-63.45%` | `125.00` |
| `Live` | `Long` | `3.25` | 2,240,000.00 USD | 0.00 USD | 109.42 USD | `-63.34%` | `33.72` |
| `Live` | `Long` | `3.31` | 2,240,000.00 USD | 0.00 USD | 712.82 USD | `-62.55%` | `215.03` |
| `Live` | `Long` | `3.37` | 2,240,000.00 USD | 0.00 USD | 389.53 USD | `-61.98%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,240,000.00 USD | 0.00 USD | 297.24 USD | `-61.87%` | `88.07` |
| `Live` | `Long` | `3.67` | 2,240,000.00 USD | 0.00 USD | 109.95 USD | `-58.59%` | `30.00` |
| `Live` | `Long` | `3.69` | 2,240,000.00 USD | 0.00 USD | 325.98 USD | `-58.37%` | `88.46` |
| `Live` | `Long` | `3.75` | 2,240,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.57%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,240,000.00 USD | 0.00 USD | 131.73 USD | `-55.99%` | `33.82` |
| `Live` | `Long` | `3.96` | 2,240,000.00 USD | 0.00 USD | 8,990.00 USD | `-55.31%` | `2,273.34` |
| `Live` | `Long` | `3.98` | 2,230,000.00 USD | 0.00 USD | 371.88 USD | `-54.98%` | `93.32` |
| `Live` | `Long` | `4.01` | 2,230,000.00 USD | 0.00 USD | 401.50 USD | `-54.64%` | `100.00` |
| `Live` | `Long` | `4.03` | 2,230,000.00 USD | 0.00 USD | 402.70 USD | `-54.52%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,230,000.00 USD | 0.00 USD | 152.29 USD | `-54.30%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,230,000.00 USD | 0.00 USD | 2,320.00 USD | `-53.85%` | `568.43` |
| `Live` | `Long` | `4.14` | 2,230,000.00 USD | 0.00 USD | 1,130.00 USD | `-53.17%` | `272.03` |
| `Live` | `Long` | `4.18` | 2,220,000.00 USD | 0.00 USD | 174.89 USD | `-52.72%` | `41.79` |
| `Live` | `Long` | `4.22` | 2,220,000.00 USD | 0.00 USD | 171.58 USD | `-52.26%` | `40.61` |
| `Live` | `Long` | `4.24` | 2,220,000.00 USD | 0.00 USD | 169.40 USD | `-52.15%` | `40.00` |
| `Live` | `Long` | `4.26` | 2,220,000.00 USD | 0.00 USD | 106.63 USD | `-51.81%` | `25.00` |
| `Live` | `Long` | `4.29` | 2,220,000.00 USD | 0.00 USD | 115.97 USD | `-51.47%` | `27.00` |
| `Live` | `Long` | `4.32` | 2,220,000.00 USD | 0.00 USD | 852.47 USD | `-51.25%` | `197.56` |
| `Live` | `Long` | `4.42` | 2,220,000.00 USD | 0.00 USD | 2,230.00 USD | `-50.00%` | `504.56` |
| `Live` | `Long` | `4.59` | 2,220,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.08%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 486.93 USD | `-47.86%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.74%` | `579.06` |
| `Live` | `Long` | `4.64` | 2,190,000.00 USD | 0.00 USD | 223.98 USD | `-47.52%` | `48.22` |
| `Live` | `Long` | `4.66` | 2,190,000.00 USD | 0.00 USD | 105.11 USD | `-47.41%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.29%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,180,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.18%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,180,000.00 USD | 0.00 USD | 9,060.00 USD | `-47.07%` | `1,933.95` |
| `Live` | `Long` | `4.70` | 2,170,000.00 USD | 0.00 USD | 7,040.00 USD | `-46.95%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,170,000.00 USD | 0.00 USD | 240.48 USD | `-46.39%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,170,000.00 USD | 0.00 USD | 105.64 USD | `-46.16%` | `22.17` |
| `Live` | `Long` | `4.79` | 2,170,000.00 USD | 0.00 USD | 5,050.00 USD | `-45.82%` | `1,053.00` |
| `Live` | `Long` | `4.82` | 2,160,000.00 USD | 0.00 USD | 17,120.00 USD | `-45.60%` | `3,556.00` |
| `Live` | `Long` | `4.83` | 2,140,000.00 USD | 0.00 USD | 467.01 USD | `-45.37%` | `96.59` |
| `Live` | `Long` | `4.88` | 2,140,000.00 USD | 0.00 USD | 113.33 USD | `-44.81%` | `23.20` |
| `Live` | `Long` | `4.89` | 2,140,000.00 USD | 0.00 USD | 146.85 USD | `-44.69%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,140,000.00 USD | 0.00 USD | 527.19 USD | `-44.58%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,140,000.00 USD | 0.00 USD | 1,230.00 USD | `-44.47%` | `251.00` |
| `Live` | `Long` | `4.96` | 2,140,000.00 USD | 0.00 USD | 945.36 USD | `-44.02%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 282.23 USD | `-43.79%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,140,000.00 USD | 0.00 USD | 329.11 USD | `-43.68%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.34%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,080,000.00 USD | 0.00 USD | 167.78 USD | `-43.23%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,080,000.00 USD | 0.00 USD | 314.59 USD | `-43.11%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,080,000.00 USD | 0.00 USD | 504.74 USD | `-42.89%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,080,000.00 USD | 0.00 USD | 805.91 USD | `-42.66%` | `158.80` |
| `Live` | `Long` | `5.09` | 2,080,000.00 USD | 0.00 USD | 4,200.00 USD | `-42.43%` | `824.62` |
| `Live` | `Long` | `5.12` | 2,080,000.00 USD | 0.00 USD | 250.20 USD | `-42.10%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,080,000.00 USD | 0.00 USD | 396.06 USD | `-41.98%` | `77.13` |
| `Live` | `Long` | `5.14` | 2,080,000.00 USD | 0.00 USD | 156,590.00 USD | `-41.87%` | `30,435.20` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.64%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.53%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,920,000.00 USD | 0.00 USD | 150.57 USD | `-41.42%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,920,000.00 USD | 0.00 USD | 300.91 USD | `-41.08%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,910,000.00 USD | 0.00 USD | 640.70 USD | `-40.29%` | `121.23` |
| `Live` | `Long` | `5.29` | 1,910,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.17%` | `500.00` |
| `Live` | `Long` | `5.32` | 1,910,000.00 USD | 0.00 USD | 232.85 USD | `-39.95%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,910,000.00 USD | 0.00 USD | 716.11 USD | `-39.84%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,910,000.00 USD | 0.00 USD | 660.46 USD | `-39.05%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.82%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 160,400.00 USD | `-38.71%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,730,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.59%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,730,000.00 USD | 0.00 USD | 264.72 USD | `-38.25%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,730,000.00 USD | 0.00 USD | 1,320.00 USD | `-38.14%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,730,000.00 USD | 0.00 USD | 354.06 USD | `-38.03%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,730,000.00 USD | 0.00 USD | 19,290.00 USD | `-37.92%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,710,000.00 USD | 0.00 USD | 367.41 USD | `-37.69%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 121.38 USD | `-37.46%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,710,000.00 USD | 0.00 USD | 967.98 USD | `-37.12%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,700,000.00 USD | 0.00 USD | 63,260.00 USD | `-37.01%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,640,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.79%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,610,000.00 USD | 0.00 USD | 22,270.00 USD | `-36.33%` | `3,952.96` |
| `Live` | `Long` | `5.66` | 1,580,000.00 USD | 0.00 USD | 4,160.00 USD | `-36.11%` | `734.88` |
| `Live` | `Long` | `5.71` | 1,580,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.54%` | `409.39` |
| `Live` | `Long` | `5.71` | 1,580,000.00 USD | 0.00 USD | 406.45 USD | `-35.43%` | `71.12` |
| `Live` | `Long` | `5.74` | 1,580,000.00 USD | 0.00 USD | 869.71 USD | `-35.20%` | `151.65` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 125.70 USD | `-35.09%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 3,190.00 USD | `-34.98%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,570,000.00 USD | 0.00 USD | 10,850.00 USD | `-34.86%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,560,000.00 USD | 0.00 USD | 801.40 USD | `-34.75%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.64%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 736.72 USD | `-34.53%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,560,000.00 USD | 0.00 USD | 580.50 USD | `-34.41%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,560,000.00 USD | 0.00 USD | 106.65 USD | `-34.30%` | `18.34` |
| `Live` | `Long` | `5.84` | 1,560,000.00 USD | 0.00 USD | 327,670.00 USD | `-33.96%` | `56,059.40` |
| `Live` | `Long` | `5.89` | 1,230,000.00 USD | 0.00 USD | 640.67 USD | `-33.40%` | `108.68` |
| `Live` | `Long` | `5.91` | 1,230,000.00 USD | 0.00 USD | 399.18 USD | `-33.28%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,230,000.00 USD | 0.00 USD | 336.30 USD | `-33.06%` | `56.76` |
| `Live` | `Long` | `5.96` | 1,230,000.00 USD | 0.00 USD | 12,120.00 USD | `-32.72%` | `2,035.32` |
| `Live` | `Long` | `5.97` | 1,220,000.00 USD | 0.00 USD | 585.97 USD | `-32.49%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,220,000.00 USD | 0.00 USD | 447.98 USD | `-32.38%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,220,000.00 USD | 0.00 USD | 341.56 USD | `-32.15%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,210,000.00 USD | 0.00 USD | 446.85 USD | `-32.04%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 331.68 USD | `-31.81%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 105.61 USD | `-31.70%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.59%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,210,000.00 USD | 0.00 USD | 265.10 USD | `-31.48%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 3,060.00 USD | `-31.36%` | `504.08` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 405.14 USD | `-31.25%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,210,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.14%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,210,000.00 USD | 0.00 USD | 3,200.00 USD | `-31.02%` | `524.73` |
| `Live` | `Long` | `6.12` | 1,200,000.00 USD | 0.00 USD | 2,500.00 USD | `-30.80%` | `408.83` |
| `Live` | `Long` | `6.14` | 1,200,000.00 USD | 0.00 USD | 238.61 USD | `-30.57%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,200,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.46%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 187.29 USD | `-30.35%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,190,000.00 USD | 0.00 USD | 104.36 USD | `-30.23%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 310.25 USD | `-29.89%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 4,150.00 USD | `-29.78%` | `667.50` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-29.67%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 972.65 USD | `-29.33%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,190,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.10%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,190,000.00 USD | 0.00 USD | 147.51 USD | `-28.99%` | `23.47` |
| `Live` | `Long` | `6.32` | 1,190,000.00 USD | 0.00 USD | 1,740.00 USD | `-28.65%` | `276.04` |
| `Live` | `Long` | `6.33` | 1,180,000.00 USD | 0.00 USD | 105.25 USD | `-28.54%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,180,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.20%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,180,000.00 USD | 0.00 USD | 284,770.00 USD | `-28.09%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 894,990.00 USD | 0.00 USD | 5,110.00 USD | `-27.97%` | `801.31` |
| `Live` | `Long` | `6.42` | 889,880.00 USD | 0.00 USD | 306.32 USD | `-27.52%` | `47.75` |
| `Live` | `Long` | `6.42` | 889,580.00 USD | 0.00 USD | 1,700.00 USD | `-27.41%` | `265.15` |
| `Live` | `Long` | `6.43` | 887,870.00 USD | 0.00 USD | 6,780.00 USD | `-27.29%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 881,100.00 USD | 0.00 USD | 1,050.00 USD | `-26.96%` | `162.75` |
| `Live` | `Long` | `6.54` | 880,040.00 USD | 0.00 USD | 3,620.00 USD | `-26.16%` | `554.55` |
| `Live` | `Long` | `6.54` | 876,420.00 USD | 0.00 USD | 8,970.00 USD | `-26.05%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 867,450.00 USD | 0.00 USD | 1,100.00 USD | `-25.60%` | `166.55` |
| `Live` | `Long` | `6.61` | 866,350.00 USD | 0.00 USD | 409.51 USD | `-25.37%` | `62.00` |
| `Live` | `Long` | `6.62` | 865,940.00 USD | 0.00 USD | 2,110.00 USD | `-25.26%` | `318.57` |
| `Live` | `Long` | `6.62` | 863,830.00 USD | 0.00 USD | 2,190.00 USD | `-25.15%` | `330.00` |
| `Live` | `Long` | `6.70` | 861,650.00 USD | 0.00 USD | 506.54 USD | `-24.36%` | `75.66` |
| `Live` | `Long` | `6.71` | 861,140.00 USD | 0.00 USD | 16,610.00 USD | `-24.24%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 844,530.00 USD | 0.00 USD | 1,330.00 USD | `-23.79%` | `196.95` |
| `Live` | `Long` | `6.78` | 843,200.00 USD | 0.00 USD | 6,780.00 USD | `-23.45%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 836,420.00 USD | 0.00 USD | 16,960.00 USD | `-23.34%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 819,460.00 USD | 0.00 USD | 4,260.00 USD | `-23.23%` | `626.24` |
| `Live` | `Long` | `6.80` | 815,210.00 USD | 0.00 USD | 1,500.00 USD | `-23.11%` | `220.95` |
| `Live` | `Long` | `6.82` | 813,700.00 USD | 0.00 USD | 2,670.00 USD | `-23.00%` | `391.11` |
| `Live` | `Long` | `6.83` | 811,040.00 USD | 0.00 USD | 158.14 USD | `-22.89%` | `23.17` |
| `Live` | `Long` | `6.83` | 810,880.00 USD | 0.00 USD | 4,410.00 USD | `-22.78%` | `644.73` |
| `Live` | `Long` | `6.86` | 806,470.00 USD | 0.00 USD | 18,930.00 USD | `-22.55%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 787,540.00 USD | 0.00 USD | 3,340.00 USD | `-22.44%` | `486.46` |
| `Live` | `Long` | `6.88` | 784,200.00 USD | 0.00 USD | 1,380.00 USD | `-22.32%` | `200.00` |
| `Live` | `Long` | `6.89` | 782,830.00 USD | 0.00 USD | 5,250.00 USD | `-22.10%` | `761.63` |
| `Live` | `Long` | `6.91` | 777,580.00 USD | 0.00 USD | 269.30 USD | `-21.98%` | `39.00` |
| `Live` | `Long` | `6.92` | 777,310.00 USD | 0.00 USD | 27,700.00 USD | `-21.76%` | `4,000.00` |
| `Live` | `Long` | `6.95` | 749,610.00 USD | 0.00 USD | 3,760.00 USD | `-21.53%` | `541.68` |
| `Live` | `Long` | `6.96` | 745,840.00 USD | 0.00 USD | 3,480.00 USD | `-21.42%` | `500.00` |
| `Live` | `Long` | `6.96` | 742,370.00 USD | 0.00 USD | 636.74 USD | `-21.31%` | `91.42` |
| `Live` | `Long` | `7.00` | 741,730.00 USD | 0.00 USD | 746.58 USD | `-20.97%` | `106.73` |
| `Live` | `Long` | `7.00` | 740,980.00 USD | 0.00 USD | 20,860.00 USD | `-20.85%` | `2,978.11` |
| `Live` | `Long` | `7.01` | 720,120.00 USD | 0.00 USD | 1,530.00 USD | `-20.74%` | `217.70` |
| `Live` | `Long` | `7.03` | 718,590.00 USD | 0.00 USD | 3,390.00 USD | `-20.63%` | `482.43` |
| `Live` | `Long` | `7.04` | 715,210.00 USD | 0.00 USD | 4,100.00 USD | `-20.40%` | `581.44` |
| `Live` | `Long` | `7.08` | 711,110.00 USD | 0.00 USD | 6,700.00 USD | `-20.06%` | `947.44` |
| `Live` | `Long` | `7.08` | 704,410.00 USD | 0.00 USD | 1,670.00 USD | `-19.95%` | `236.20` |
| `Live` | `Long` | `7.11` | 702,730.00 USD | 0.00 USD | 29,850.00 USD | `-19.72%` | `4,201.02` |
| `Live` | `Long` | `7.12` | 672,880.00 USD | 0.00 USD | 379.66 USD | `-19.61%` | `53.36` |
| `Live` | `Long` | `7.13` | 672,500.00 USD | 0.00 USD | 2,300.00 USD | `-19.39%` | `322.72` |
| `Live` | `Long` | `7.14` | 670,200.00 USD | 0.00 USD | 20,950.00 USD | `-19.27%` | `2,931.56` |
| `Live` | `Long` | `7.18` | 649,260.00 USD | 0.00 USD | 1,440.00 USD | `-18.82%` | `200.00` |
| `Live` | `Long` | `7.21` | 647,820.00 USD | 0.00 USD | 581.02 USD | `-18.48%` | `80.53` |
| `Live` | `Long` | `7.22` | 647,240.00 USD | 0.00 USD | 833.26 USD | `-18.37%` | `115.33` |
| `Live` | `Long` | `7.24` | 646,400.00 USD | 0.00 USD | 179.65 USD | `-18.26%` | `24.83` |
| `Live` | `Long` | `7.25` | 646,230.00 USD | 0.00 USD | 185.83 USD | `-18.14%` | `25.65` |
| `Live` | `Long` | `7.29` | 646,040.00 USD | 0.00 USD | 36,420.00 USD | `-17.69%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 609,610.00 USD | 0.00 USD | 19,790.00 USD | `-17.58%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 589,830.00 USD | 0.00 USD | 168.76 USD | `-17.35%` | `23.07` |
| `Live` | `Long` | `7.33` | 589,660.00 USD | 0.00 USD | 5,050.00 USD | `-17.24%` | `688.93` |
| `Live` | `Long` | `7.33` | 584,610.00 USD | 0.00 USD | 2,450.00 USD | `-17.13%` | `333.54` |
| `Live` | `Long` | `7.34` | 582,160.00 USD | 0.00 USD | 4,370.00 USD | `-17.01%` | `594.84` |
| `Live` | `Long` | `7.37` | 577,790.00 USD | 0.00 USD | 5,720.00 USD | `-16.79%` | `776.95` |
| `Live` | `Long` | `7.38` | 572,070.00 USD | 0.00 USD | 3,920.00 USD | `-16.67%` | `531.65` |
| `Live` | `Long` | `7.38` | 568,150.00 USD | 0.00 USD | 17,770.00 USD | `-16.56%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 550,380.00 USD | 0.00 USD | 2,590.00 USD | `-16.45%` | `350.17` |
| `Live` | `Long` | `7.42` | 547,790.00 USD | 0.00 USD | 500.00 USD | `-16.11%` | `67.34` |
| `Live` | `Long` | `7.43` | 547,290.00 USD | 0.00 USD | 1,490.00 USD | `-16.00%` | `200.00` |
| `Live` | `Long` | `7.45` | 545,810.00 USD | 0.00 USD | 210.99 USD | `-15.88%` | `28.34` |
| `Live` | `Long` | `7.46` | 545,590.00 USD | 0.00 USD | 1,370.00 USD | `-15.77%` | `183.84` |
| `Live` | `Long` | `7.46` | 544,220.00 USD | 0.00 USD | 9,160.00 USD | `-15.66%` | `1,227.40` |
| `Live` | `Long` | `7.47` | 535,060.00 USD | 0.00 USD | 3,210.00 USD | `-15.54%` | `430.09` |
| `Live` | `Long` | `7.50` | 531,850.00 USD | 0.00 USD | 1,580.00 USD | `-15.32%` | `211.22` |
| `Live` | `Long` | `7.50` | 530,260.00 USD | 0.00 USD | 1,080.00 USD | `-15.21%` | `143.74` |
| `Live` | `Long` | `7.53` | 529,190.00 USD | 0.00 USD | 995.86 USD | `-14.98%` | `132.34` |
| `Live` | `Long` | `7.54` | 528,190.00 USD | 0.00 USD | 4,210.00 USD | `-14.87%` | `559.01` |
| `Live` | `Long` | `7.55` | 523,980.00 USD | 0.00 USD | 157.14 USD | `-14.64%` | `20.80` |
| `Live` | `Long` | `7.58` | 523,820.00 USD | 0.00 USD | 4,380.00 USD | `-14.41%` | `578.50` |
| `Live` | `Long` | `7.59` | 519,440.00 USD | 0.00 USD | 25,140.00 USD | `-14.19%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 494,300.00 USD | 0.00 USD | 312.22 USD | `-13.96%` | `41.00` |
| `Live` | `Long` | `7.62` | 493,990.00 USD | 0.00 USD | 787.51 USD | `-13.85%` | `103.28` |
| `Live` | `Long` | `7.63` | 493,200.00 USD | 0.00 USD | 514.52 USD | `-13.74%` | `67.39` |
| `Live` | `Long` | `7.66` | 492,680.00 USD | 0.00 USD | 135.42 USD | `-13.51%` | `17.69` |
| `Live` | `Long` | `7.67` | 492,550.00 USD | 0.00 USD | 1,740.00 USD | `-13.40%` | `226.45` |
| `Live` | `Long` | `7.68` | 490,810.00 USD | 0.00 USD | 1,120.00 USD | `-13.17%` | `145.25` |
| `Live` | `Long` | `7.70` | 489,700.00 USD | 0.00 USD | 1,460.00 USD | `-13.06%` | `190.36` |
| `Live` | `Long` | `7.71` | 488,230.00 USD | 0.00 USD | 19,760.00 USD | `-12.95%` | `2,564.20` |
| `Live` | `Long` | `7.72` | 468,470.00 USD | 0.00 USD | 2,550.00 USD | `-12.72%` | `330.65` |
| `Live` | `Long` | `7.75` | 465,920.00 USD | 0.00 USD | 893.76 USD | `-12.38%` | `115.25` |
| `Live` | `Long` | `7.76` | 465,030.00 USD | 0.00 USD | 455.73 USD | `-12.27%` | `58.69` |
| `Live` | `Long` | `7.78` | 464,570.00 USD | 0.00 USD | 695.32 USD | `-12.15%` | `89.43` |
| `Live` | `Long` | `7.79` | 463,870.00 USD | 0.00 USD | 3,900.00 USD | `-12.04%` | `500.57` |
| `Live` | `Long` | `7.79` | 459,980.00 USD | 0.00 USD | 1,940.00 USD | `-11.93%` | `248.84` |
| `Live` | `Long` | `7.80` | 458,040.00 USD | 0.00 USD | 633.77 USD | `-11.82%` | `81.20` |
| `Live` | `Long` | `7.82` | 457,400.00 USD | 0.00 USD | 5,280.00 USD | `-11.70%` | `675.43` |
| `Live` | `Long` | `7.84` | 452,130.00 USD | 0.00 USD | 10,930.00 USD | `-11.36%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 441,190.00 USD | 0.00 USD | 2,110.00 USD | `-11.25%` | `269.14` |
| `Live` | `Long` | `7.87` | 439,080.00 USD | 0.00 USD | 176.18 USD | `-11.14%` | `22.40` |
| `Live` | `Long` | `7.88` | 438,900.00 USD | 0.00 USD | 555.19 USD | `-11.02%` | `70.50` |
| `Live` | `Long` | `7.91` | 438,350.00 USD | 0.00 USD | 505.13 USD | `-10.69%` | `63.90` |
| `Live` | `Long` | `7.93` | 437,840.00 USD | 0.00 USD | 1,820.00 USD | `-10.35%` | `228.88` |
| `Live` | `Long` | `7.95` | 436,030.00 USD | 0.00 USD | 127,110.00 USD | `-10.23%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 308,910.00 USD | 0.00 USD | 843.15 USD | `-10.12%` | `105.99` |
| `Live` | `Long` | `7.99` | 308,070.00 USD | 0.00 USD | 1,600.00 USD | `-9.78%` | `200.68` |
| `Live` | `Long` | `8.00` | 306,470.00 USD | 0.00 USD | 210.99 USD | `-9.67%` | `26.39` |
| `Live` | `Long` | `8.03` | 306,260.00 USD | 0.00 USD | 957.70 USD | `-9.33%` | `119.34` |
| `Live` | `Long` | `8.04` | 305,300.00 USD | 0.00 USD | 88,380.00 USD | `-9.22%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 216,920.00 USD | 0.00 USD | 6,890.00 USD | `-9.10%` | `856.44` |
| `Live` | `Long` | `8.05` | 210,030.00 USD | 0.00 USD | 3,340.00 USD | `-8.99%` | `414.27` |
| `Live` | `Long` | `8.06` | 206,690.00 USD | 0.00 USD | 37,830.00 USD | `-8.88%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 168,860.00 USD | 0.00 USD | 617.61 USD | `-8.65%` | `76.39` |
| `Live` | `Long` | `8.10` | 168,240.00 USD | 0.00 USD | 11,700.00 USD | `-8.54%` | `1,445.70` |
| `Live` | `Long` | `8.12` | 156,540.00 USD | 0.00 USD | 241.26 USD | `-8.31%` | `29.73` |
| `Live` | `Long` | `8.16` | 156,300.00 USD | 0.00 USD | 871.61 USD | `-7.75%` | `106.75` |
| `Live` | `Long` | `8.18` | 155,430.00 USD | 0.00 USD | 235.36 USD | `-7.64%` | `28.79` |
| `Live` | `Long` | `8.20` | 155,190.00 USD | 0.00 USD | 1,050.00 USD | `-7.41%` | `128.30` |
| `Live` | `Long` | `8.21` | 154,140.00 USD | 0.00 USD | 1,910.00 USD | `-7.30%` | `232.19` |
| `Live` | `Long` | `8.21` | 152,230.00 USD | 0.00 USD | 147.87 USD | `-7.18%` | `18.00` |
| `Live` | `Long` | `8.22` | 152,090.00 USD | 0.00 USD | 2,100.00 USD | `-7.07%` | `255.16` |
| `Live` | `Long` | `8.23` | 149,990.00 USD | 0.00 USD | 1,160.00 USD | `-6.96%` | `140.81` |
| `Live` | `Long` | `8.24` | 148,830.00 USD | 0.00 USD | 1,300.00 USD | `-6.84%` | `158.06` |
| `Live` | `Long` | `8.26` | 147,530.00 USD | 0.00 USD | 13,810.00 USD | `-6.73%` | `1,673.14` |
| `Live` | `Long` | `8.28` | 133,710.00 USD | 0.00 USD | 9,740.00 USD | `-6.51%` | `1,176.86` |
| `Live` | `Long` | `8.29` | 123,980.00 USD | 0.00 USD | 498.26 USD | `-6.39%` | `60.14` |
| `Live` | `Long` | `8.29` | 123,480.00 USD | 0.00 USD | 18,970.00 USD | `-6.28%` | `2,286.62` |
| `Live` | `Long` | `8.30` | 104,510.00 USD | 0.00 USD | 33,500.00 USD | `-6.17%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 71,010.00 USD | 0.00 USD | 4,550.00 USD | `-6.05%` | `547.70` |
| `Live` | `Long` | `8.34` | 66,460.00 USD | 0.00 USD | 4,760.00 USD | `-5.83%` | `571.65` |
| `Live` | `Long` | `8.36` | 61,690.00 USD | 0.00 USD | 3,180.00 USD | `-5.60%` | `380.92` |
| `Live` | `Long` | `8.37` | 58,510.00 USD | 0.00 USD | 7,390.00 USD | `-5.49%` | `883.19` |
| `Live` | `Long` | `8.38` | 51,120.00 USD | 0.00 USD | 4,620.00 USD | `-5.26%` | `550.46` |
| `Live` | `Long` | `8.39` | 46,510.00 USD | 0.00 USD | 1,680.00 USD | `-5.15%` | `200.00` |
| `Live` | `Long` | `8.40` | 44,830.00 USD | 0.00 USD | 1,380.00 USD | `-5.04%` | `164.50` |
| `Live` | `Long` | `8.41` | 43,440.00 USD | 0.00 USD | 681.03 USD | `-4.92%` | `80.93` |
| `Live` | `Long` | `8.44` | 42,760.00 USD | 0.00 USD | 188.61 USD | `-4.70%` | `22.36` |
| `Live` | `Long` | `8.45` | 42,570.00 USD | 0.00 USD | 588.70 USD | `-4.58%` | `69.71` |
| `Live` | `Long` | `8.46` | 41,990.00 USD | 0.00 USD | 422.16 USD | `-4.47%` | `49.93` |
| `Live` | `Long` | `8.46` | 41,560.00 USD | 0.00 USD | 1,860.00 USD | `-4.36%` | `220.00` |
| `Live` | `Long` | `8.47` | 39,700.00 USD | 0.00 USD | 12,430.00 USD | `-4.25%` | `1,466.22` |
| `Live` | `Long` | `8.48` | 27,280.00 USD | 0.00 USD | 1,160.00 USD | `-4.13%` | `136.39` |
| `Live` | `Long` | `8.49` | 26,120.00 USD | 0.00 USD | 403.51 USD | `-4.02%` | `47.50` |
| `Live` | `Long` | `8.51` | 25,710.00 USD | 0.00 USD | 6,380.00 USD | `-3.91%` | `750.34` |
| `Live` | `Long` | `8.52` | 19,330.00 USD | 0.00 USD | 7,770.00 USD | `-3.79%` | `912.98` |
| `Live` | `Long` | `8.54` | 11,560.00 USD | 0.00 USD | 6,350.00 USD | `-3.57%` | `743.78` |
| `Live` | `Long` | `8.54` | 5,210.00 USD | 0.00 USD | 1,550.00 USD | `-3.46%` | `180.95` |
| `Live` | `Long` | `8.55` | 3,660.00 USD | 0.00 USD | 684.40 USD | `-3.34%` | `80.00` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-2.78%` | `346.30` |
| `Live` | `Short` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | `+3.21%` | `34.41` |
| `Live` | `Short` | `9.21` | 4,130.00 USD | 3,810.00 USD | 0.00 USD | `+4.11%` | `413.79` |
| `Live` | `Short` | `9.29` | 4,230.00 USD | 100.93 USD | 0.00 USD | `+4.91%` | `10.87` |
| `Live` | `Short` | `9.35` | 8,150.00 USD | 3,930.00 USD | 0.00 USD | `+5.58%` | `420.07` |
| `Live` | `Short` | `9.38` | 412,270.00 USD | 404,120.00 USD | 0.00 USD | `+6.04%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 414,740.00 USD | 2,470.00 USD | 0.00 USD | `+6.37%` | `262.71` |
| `Live` | `Short` | `9.49` | 415,170.00 USD | 428.79 USD | 0.00 USD | `+7.28%` | `45.16` |
| `Live` | `Short` | `9.73` | 415,370.00 USD | 192.95 USD | 0.00 USD | `+9.99%` | `19.82` |
| `Live` | `Short` | `9.76` | 415,920.00 USD | 549.11 USD | 0.00 USD | `+10.22%` | `56.29` |
| `Live` | `Short` | `9.78` | 416,390.00 USD | 470.18 USD | 0.00 USD | `+10.44%` | `48.10` |
| `Live` | `Short` | `10.09` | 416,500.00 USD | 113.76 USD | 0.00 USD | `+13.94%` | `11.28` |
| `Live` | `Short` | `10.15` | 423,390.00 USD | 6,890.00 USD | 0.00 USD | `+14.74%` | `678.64` |
| `Live` | `Short` | `10.21` | 430,720.00 USD | 7,330.00 USD | 0.00 USD | `+15.41%` | `717.30` |
| `Live` | `Short` | `10.23` | 430,830.00 USD | 114.12 USD | 0.00 USD | `+15.64%` | `11.15` |
| `Live` | `Short` | `10.35` | 434,210.00 USD | 3,380.00 USD | 0.00 USD | `+16.88%` | `326.92` |
| `Live` | `Short` | `10.56` | 434,740.00 USD | 523.81 USD | 0.00 USD | `+19.37%` | `49.58` |
| `Live` | `Short` | `10.71` | 434,960.00 USD | 218.91 USD | 0.00 USD | `+21.06%` | `20.43` |
| `Live` | `Short` | `10.74` | 472,160.00 USD | 37,210.00 USD | 0.00 USD | `+21.40%` | `3,462.73` |
| `Live` | `Short` | `10.96` | 474,080.00 USD | 1,920.00 USD | 0.00 USD | `+23.89%` | `174.67` |
| `Live` | `Short` | `11.01` | 481,050.00 USD | 6,970.00 USD | 0.00 USD | `+24.34%` | `633.00` |
| `Live` | `Short` | `11.27` | 492,850.00 USD | 11,810.00 USD | 0.00 USD | `+27.28%` | `1,048.25` |
| `Live` | `Short` | `11.62` | 504,990.00 USD | 12,140.00 USD | 0.00 USD | `+31.34%` | `1,043.90` |
| `Live` | `Short` | `11.65` | 505,770.00 USD | 776.22 USD | 0.00 USD | `+31.68%` | `66.60` |
| `Live` | `Short` | `11.78` | 564,640.00 USD | 58,870.00 USD | 0.00 USD | `+33.04%` | `5,000.00` |
| `Live` | `Short` | `11.96` | 566,000.00 USD | 1,360.00 USD | 0.00 USD | `+35.19%` | `113.77` |
| `Live` | `Short` | `12.12` | 566,620.00 USD | 620.17 USD | 0.00 USD | `+36.88%` | `51.19` |
| `Live` | `Short` | `12.30` | 568,350.00 USD | 1,730.00 USD | 0.00 USD | `+39.03%` | `140.71` |
| `Live` | `Short` | `12.40` | 568,700.00 USD | 343.62 USD | 0.00 USD | `+40.16%` | `27.70` |
| `Live` | `Short` | `12.63` | 569,130.00 USD | 430.85 USD | 0.00 USD | `+42.76%` | `34.10` |
| `Live` | `Short` | `12.79` | 570,080.00 USD | 953.38 USD | 0.00 USD | `+44.45%` | `74.57` |
| `Live` | `Short` | `12.79` | 606,930.00 USD | 36,850.00 USD | 0.00 USD | `+44.56%` | `2,879.71` |
| `Live` | `Short` | `12.95` | 621,430.00 USD | 14,500.00 USD | 0.00 USD | `+46.26%` | `1,120.14` |
| `Live` | `Short` | `12.96` | 621,530.00 USD | 102.68 USD | 0.00 USD | `+46.48%` | `7.92` |
| `Live` | `Short` | `13.20` | 709,470.00 USD | 87,940.00 USD | 0.00 USD | `+49.08%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 944,310.00 USD | 234,840.00 USD | 0.00 USD | `+50.10%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 948,120.00 USD | 3,810.00 USD | 0.00 USD | `+50.21%` | `286.56` |
| `Live` | `Short` | `13.46` | 948,550.00 USD | 430.34 USD | 0.00 USD | `+52.13%` | `31.96` |
| `Live` | `Short` | `13.69` | 948,730.00 USD | 172.29 USD | 0.00 USD | `+54.62%` | `12.59` |
| `Live` | `Short` | `13.73` | 948,890.00 USD | 160.01 USD | 0.00 USD | `+55.18%` | `11.65` |
| `Live` | `Short` | `14.10` | 952,800.00 USD | 3,910.00 USD | 0.00 USD | `+59.25%` | `277.54` |
| `Live` | `Short` | `14.66` | 953,620.00 USD | 823.29 USD | 0.00 USD | `+65.69%` | `56.14` |
| `Live` | `Short` | `14.71` | 953,860.00 USD | 241.31 USD | 0.00 USD | `+66.14%` | `16.41` |
| `Live` | `Short` | `14.81` | 954,160.00 USD | 292.30 USD | 0.00 USD | `+67.39%` | `19.73` |
| `Live` | `Short` | `14.84` | 956,620.00 USD | 2,460.00 USD | 0.00 USD | `+67.61%` | `166.16` |
| `Live` | `Short` | `14.86` | 956,940.00 USD | 320.13 USD | 0.00 USD | `+67.84%` | `21.55` |
| `Live` | `Short` | `15.29` | 957,170.00 USD | 229.43 USD | 0.00 USD | `+72.81%` | `15.00` |
| `Live` | `Short` | `15.35` | 957,400.00 USD | 230.17 USD | 0.00 USD | `+73.37%` | `15.00` |
| `Live` | `Short` | `15.38` | 977,400.00 USD | 20,000.00 USD | 0.00 USD | `+73.83%` | `1,300.00` |
| `Live` | `Short` | `15.45` | 1,130,000.00 USD | 154,450.00 USD | 0.00 USD | `+74.50%` | `10,000.00` |
| `Live` | `Short` | `15.70` | 1,130,000.00 USD | 111.59 USD | 0.00 USD | `+77.33%` | `7.11` |
| `Live` | `Short` | `16.29` | 1,400,000.00 USD | 263,950.00 USD | 0.00 USD | `+83.99%` | `16,208.00` |
| `Live` | `Short` | `16.48` | 1,420,000.00 USD | 22,650.00 USD | 0.00 USD | `+86.25%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,420,000.00 USD | 190.91 USD | 0.00 USD | `+86.59%` | `11.56` |
| `Live` | `Short` | `16.70` | 1,500,000.00 USD | 84,150.00 USD | 0.00 USD | `+88.74%` | `5,037.66` |
| `Live` | `Short` | `16.75` | 1,500,000.00 USD | 162.26 USD | 0.00 USD | `+89.19%` | `9.69` |
| `Live` | `Short` | `16.77` | 1,500,000.00 USD | 340.87 USD | 0.00 USD | `+89.53%` | `20.32` |
| `Live` | `Short` | `17.02` | 1,500,000.00 USD | 191.87 USD | 0.00 USD | `+92.36%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,510,000.00 USD | 1,710.00 USD | 0.00 USD | `+93.60%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,510,000.00 USD | 101.47 USD | 0.00 USD | `+97.33%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,510,000.00 USD | 4,120.00 USD | 0.00 USD | `+99.13%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,510,000.00 USD | 4,930.00 USD | 0.00 USD | `+99.36%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,520,000.00 USD | 2,660.00 USD | 0.00 USD | `+99.59%` | `150.82` |
| `Live` | `Short` | `17.70` | 1,520,000.00 USD | 108.89 USD | 0.00 USD | `+100.04%` | `6.15` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 327,240.00 USD | 0.00 USD | 611.73 USD | `-73.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 326,630.00 USD | 0.00 USD | 793.75 USD | `-54.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 325,840.00 USD | 0.00 USD | 105.04 USD | `-49.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 325,730.00 USD | 0.00 USD | 67,970.00 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 257,760.00 USD | 0.00 USD | 205.30 USD | `-40.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 257,560.00 USD | 0.00 USD | 465.42 USD | `-38.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 257,090.00 USD | 0.00 USD | 349.35 USD | `-37.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 256,740.00 USD | 0.00 USD | 1,330.00 USD | `-34.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 255,420.00 USD | 0.00 USD | 493.50 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 254,920.00 USD | 0.00 USD | 100.98 USD | `-32.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 254,820.00 USD | 0.00 USD | 620.80 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 254,200.00 USD | 0.00 USD | 4,160.00 USD | `-31.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 250,050.00 USD | 0.00 USD | 6,500.00 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 243,540.00 USD | 0.00 USD | 864.38 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 242,680.00 USD | 0.00 USD | 1,430.00 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 241,250.00 USD | 0.00 USD | 4,340.00 USD | `-26.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 236,910.00 USD | 0.00 USD | 5,520.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 231,380.00 USD | 0.00 USD | 100.72 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 231,280.00 USD | 0.00 USD | 296.34 USD | `-23.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 230,990.00 USD | 0.00 USD | 921.19 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 230,070.00 USD | 0.00 USD | 709.98 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 229,360.00 USD | 0.00 USD | 262.44 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 229,090.00 USD | 0.00 USD | 3,610.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 225,480.00 USD | 0.00 USD | 6,790.00 USD | `-19.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 218,690.00 USD | 0.00 USD | 9,770.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 208,920.00 USD | 0.00 USD | 103.46 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,820.00 USD | 0.00 USD | 603.44 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,220.00 USD | 0.00 USD | 891.57 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 207,320.00 USD | 0.00 USD | 2,300.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 205,020.00 USD | 0.00 USD | 129.58 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 204,890.00 USD | 0.00 USD | 236.19 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 204,650.00 USD | 0.00 USD | 199.39 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 204,460.00 USD | 0.00 USD | 4,730.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 199,720.00 USD | 0.00 USD | 37,420.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 162,300.00 USD | 0.00 USD | 778.49 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 161,520.00 USD | 0.00 USD | 799.83 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 160,720.00 USD | 0.00 USD | 103.41 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 160,620.00 USD | 0.00 USD | 1,370.00 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 159,240.00 USD | 0.00 USD | 360.13 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 158,880.00 USD | 0.00 USD | 578.04 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 158,300.00 USD | 0.00 USD | 175.42 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 158,130.00 USD | 0.00 USD | 2,990.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 155,130.00 USD | 0.00 USD | 143.51 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 154,990.00 USD | 0.00 USD | 183.33 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 154,810.00 USD | 0.00 USD | 194.52 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 154,610.00 USD | 0.00 USD | 394.75 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 154,220.00 USD | 0.00 USD | 1,350.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 152,870.00 USD | 0.00 USD | 1,590.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 151,290.00 USD | 0.00 USD | 898.42 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 150,390.00 USD | 0.00 USD | 1,350.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 149,040.00 USD | 0.00 USD | 7,400.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 141,640.00 USD | 0.00 USD | 123.58 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 141,520.00 USD | 0.00 USD | 2,110.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 139,410.00 USD | 0.00 USD | 563.85 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 138,850.00 USD | 0.00 USD | 105.14 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 138,740.00 USD | 0.00 USD | 367.76 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 138,370.00 USD | 0.00 USD | 2,330.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 136,040.00 USD | 0.00 USD | 184.13 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 135,860.00 USD | 0.00 USD | 6,920.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 128,940.00 USD | 0.00 USD | 462.15 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 128,480.00 USD | 0.00 USD | 654.53 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 127,820.00 USD | 0.00 USD | 367.91 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 127,450.00 USD | 0.00 USD | 520.75 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 126,930.00 USD | 0.00 USD | 2,900.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 124,030.00 USD | 0.00 USD | 141.04 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 123,890.00 USD | 0.00 USD | 1,780.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 122,100.00 USD | 0.00 USD | 515.66 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 121,590.00 USD | 0.00 USD | 143.54 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 121,450.00 USD | 0.00 USD | 168.64 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 121,280.00 USD | 0.00 USD | 201.49 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 121,080.00 USD | 0.00 USD | 6,530.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 114,550.00 USD | 0.00 USD | 1,140.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 113,400.00 USD | 0.00 USD | 2,000.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 111,400.00 USD | 0.00 USD | 756.06 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 110,640.00 USD | 0.00 USD | 970.35 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 109,670.00 USD | 0.00 USD | 5,470.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 104,210.00 USD | 0.00 USD | 1,970.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 102,240.00 USD | 0.00 USD | 3,290.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 98,960.00 USD | 0.00 USD | 358.56 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 98,600.00 USD | 0.00 USD | 1,880.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 96,710.00 USD | 0.00 USD | 140.36 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 96,570.00 USD | 0.00 USD | 138.24 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 96,440.00 USD | 0.00 USD | 954.23 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 95,480.00 USD | 0.00 USD | 769.61 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 94,710.00 USD | 0.00 USD | 489.58 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 94,220.00 USD | 0.00 USD | 1,440.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 92,780.00 USD | 0.00 USD | 198.74 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 92,580.00 USD | 0.00 USD | 1,130.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 91,450.00 USD | 0.00 USD | 4,400.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 87,050.00 USD | 0.00 USD | 243.82 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 86,800.00 USD | 0.00 USD | 428.58 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 86,370.00 USD | 0.00 USD | 2,500.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 83,870.00 USD | 0.00 USD | 435.59 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 83,440.00 USD | 0.00 USD | 1,080.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 82,360.00 USD | 0.00 USD | 1,980.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 80,380.00 USD | 0.00 USD | 2,740.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 77,640.00 USD | 0.00 USD | 103.19 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 77,540.00 USD | 0.00 USD | 103.31 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 77,430.00 USD | 0.00 USD | 1,900.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 75,530.00 USD | 0.00 USD | 196.87 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 75,330.00 USD | 0.00 USD | 223.82 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 75,110.00 USD | 0.00 USD | 990.09 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 74,120.00 USD | 0.00 USD | 5,010.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 69,110.00 USD | 0.00 USD | 6,880.00 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 62,220.00 USD | 0.00 USD | 134.30 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 62,090.00 USD | 0.00 USD | 390.88 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 61,700.00 USD | 0.00 USD | 1,390.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 60,310.00 USD | 0.00 USD | 933.70 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 59,370.00 USD | 0.00 USD | 6,300.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 53,080.00 USD | 0.00 USD | 39,810.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 13,270.00 USD | 0.00 USD | 114.25 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 13,150.00 USD | 0.00 USD | 1,930.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 11,220.00 USD | 0.00 USD | 711.78 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 10,510.00 USD | 0.00 USD | 1,760.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 8,750.00 USD | 0.00 USD | 705.20 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 8,040.00 USD | 0.00 USD | 2,030.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 6,010.00 USD | 0.00 USD | 243.40 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 5,760.00 USD | 0.00 USD | 5,760.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 192.86 USD | 192.86 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 807.74 USD | 614.88 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 6,830.00 USD | 6,020.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 7,930.00 USD | 1,100.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 8,120.00 USD | 188.66 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 8,910.00 USD | 788.72 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 12,270.00 USD | 3,360.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 12,380.00 USD | 110.58 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 13,400.00 USD | 1,020.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 13,620.00 USD | 223.62 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 13,760.00 USD | 137.73 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 14,160.00 USD | 401.63 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 329,310.00 USD | 315,150.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 329,420.00 USD | 104.59 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 330,200.00 USD | 776.54 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 330,730.00 USD | 531.20 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 332,100.00 USD | 1,380.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 333,190.00 USD | 1,090.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 333,810.00 USD | 616.37 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 333,910.00 USD | 102.03 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 334,360.00 USD | 453.84 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 334,520.00 USD | 160.99 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 334,940.00 USD | 415.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 336,450.00 USD | 1,510.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 338,490.00 USD | 2,040.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 566,120.00 USD | 227,630.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 569,160.00 USD | 3,030.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 571,160.00 USD | 2,000.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 965,370.00 USD | 394,210.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,000,000.00 USD | 39,240.00 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,010,000.00 USD | 1,590.00 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 3,320.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,010,000.00 USD | 687.91 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,010,000.00 USD | 954.71 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,410,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,410,000.00 USD | 205.87 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,410,000.00 USD | 1,960.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,410,000.00 USD | 434.45 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,430,000.00 USD | 18,610.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,430,000.00 USD | 354.81 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,430,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,430,000.00 USD | 579.86 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,760,000.00 USD | 327,430.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,760,000.00 USD | 233.38 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 163.41 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 1,150.00 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,760,000.00 USD | 660.84 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,760,000.00 USD | 833.66 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,010.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,770,000.00 USD | 102.45 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 219.84 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,770,000.00 USD | 1,780.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,770,000.00 USD | 2,210.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,770,000.00 USD | 288.46 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,770,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,770,000.00 USD | 103.54 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,770,000.00 USD | 535.35 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,770,000.00 USD | 231.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,770,000.00 USD | 221.07 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,780,000.00 USD | 446.58 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,780,000.00 USD | 108.21 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,780,000.00 USD | 169.68 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,780,000.00 USD | 121.87 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,780,000.00 USD | 619.28 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,780,000.00 USD | 5,030.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,780,000.00 USD | 340.05 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,780,000.00 USD | 742.12 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,860,000.00 USD | 7,500.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,870,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,870,000.00 USD | 202.10 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 210,980.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,080,000.00 USD | 172.16 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,080,000.00 USD | 868.36 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,080,000.00 USD | 489.40 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,080,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,080,000.00 USD | 118.01 USD | 0.00 USD | `+17.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,090,000.00 USD | 312.31 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 2,290.00 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,090,000.00 USD | 118.97 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,090,000.00 USD | 251.06 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,090,000.00 USD | 552.44 USD | 0.00 USD | `+23.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,090,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,090,000.00 USD | 320.29 USD | 0.00 USD | `+25.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,090,000.00 USD | 1,100.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,100,000.00 USD | 2,410.00 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,110,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,120,000.00 USD | 3,530.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,120,000.00 USD | 7,700.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,120,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,120,000.00 USD | 434.61 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,120,000.00 USD | 163.52 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,250,000.00 USD | 2,770.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,260,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,260,000.00 USD | 197.97 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,260,000.00 USD | 504.17 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,260,000.00 USD | 169.57 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,260,000.00 USD | 159.66 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,260,000.00 USD | 446.52 USD | 0.00 USD | `+51.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,260,000.00 USD | 1,710.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+52.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,480,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,480,000.00 USD | 407.95 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,480,000.00 USD | 174.91 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,490,000.00 USD | 9,230.00 USD | 0.00 USD | `+58.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,490,000.00 USD | 960.26 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+62.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,490,000.00 USD | 805.90 USD | 0.00 USD | `+63.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,490,000.00 USD | 655.55 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,500,000.00 USD | 4,890.00 USD | 0.00 USD | `+67.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,500,000.00 USD | 471.09 USD | 0.00 USD | `+68.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,500,000.00 USD | 383.85 USD | 0.00 USD | `+69.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+80.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+91.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,150,000.00 USD | 4,500.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,270,000.00 USD | 120,270.00 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,270,000.00 USD | 122.39 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,270,000.00 USD | 586.59 USD | 0.00 USD | `+97.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,280,000.00 USD | 580.97 USD | 0.00 USD | `+98.91%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.77` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 18,150.00 USD | 10,660.00 USD | 4,850.00 USD |
| `1D` | `7.79` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 65,890.00 USD | 11,370.00 USD | 16,150.00 USD |
| `7D` | `7.79` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 19,090.00 USD | 4,540.00 USD | 15,300.00 USD |
| `1D` | `7.81` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 6,130.00 USD | 7,800.00 USD | 6,020.00 USD |
| `7D` | `7.81` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 2,240.00 USD | 11,570.00 USD | 0.00 USD |
| `1D` | `7.83` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 4,450.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `7.83` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD |
| `1D` | `7.85` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 4,570.00 USD | 3,060.00 USD | 10,340.00 USD |
| `7D` | `7.85` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 15,410.00 USD | 7,840.00 USD | 12,270.00 USD |
| `1D` | `7.87` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 29,410.00 USD | 4,570.00 USD | 25,310.00 USD |
| `7D` | `7.87` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 50,960.00 USD | 1,540.00 USD | 21,140.00 USD |
| `1D` | `7.89` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 21,240.00 USD | 9,580.00 USD | 6,270.00 USD |
| `7D` | `7.89` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,270.00 USD |
| `1D` | `7.91` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 11,920.00 USD | 3,480.00 USD | 7,980.00 USD |
| `7D` | `7.91` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD |
| `1D` | `7.93` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD |
| `7D` | `7.93` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.95` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 11,610.00 USD | 9,310.00 USD | 8,590.00 USD |
| `7D` | `7.95` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD |
| `1D` | `7.97` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 13,510.00 USD | 5,620.00 USD | 4,050.00 USD |
| `7D` | `7.97` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD |
| `1D` | `7.99` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 4,090.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `7.99` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD |
| `1D` | `8.01` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 6,600.00 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `8.01` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD |
| `1D` | `8.03` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 17,700.00 USD | 2,310.00 USD | 297.55 USD |
| `7D` | `8.03` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD |
| `1D` | `8.05` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 24,220.00 USD | 3,770.00 USD | 6,520.00 USD |
| `7D` | `8.05` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD |
| `1D` | `8.07` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 13,130.00 USD | 4,100.00 USD | 7,410.00 USD |
| `7D` | `8.07` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD |
| `1D` | `8.09` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 14,060.00 USD | 2,630.00 USD | 7,810.00 USD |
| `7D` | `8.09` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD |
| `1D` | `8.11` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 13,850.00 USD | 6,970.00 USD | 4,610.00 USD |
| `7D` | `8.11` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD |
| `1D` | `8.13` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 10,930.00 USD | 0.00 USD | 7,260.00 USD |
| `7D` | `8.13` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD |
| `1D` | `8.15` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 28,020.00 USD | 662.47 USD | 5,070.00 USD |
| `7D` | `8.15` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,850.00 USD |
| `1D` | `8.17` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,360.00 USD | 0.00 USD | 59.50 USD |
| `7D` | `8.17` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 6,560.00 USD | 7,770.00 USD | 10,030.00 USD |
| `1D` | `8.19` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 5,590.00 USD | 0.00 USD | 469.45 USD |
| `7D` | `8.19` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD |
| `1D` | `8.21` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 3,540.00 USD | 0.00 USD | 445.22 USD |
| `7D` | `8.21` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD |
| `1D` | `8.23` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 26,390.00 USD | 4,080.00 USD | 41,050.00 USD |
| `7D` | `8.23` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD |
| `1D` | `8.25` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 18,270.00 USD | 1,150.00 USD | 9,610.00 USD |
| `7D` | `8.25` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD |
| `1D` | `8.27` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 12,140.00 USD | 14,210.00 USD | 21.52 USD |
| `7D` | `8.27` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,190.00 USD |
| `1D` | `8.29` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 109,350.00 USD | 16,540.00 USD | 45,430.00 USD |
| `7D` | `8.29` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD |
| `1D` | `8.31` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 109,200.00 USD | 24,540.00 USD | 20,640.00 USD |
| `7D` | `8.31` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 80,550.00 USD | 13,500.00 USD | 11,000.00 USD |
| `1D` | `8.33` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 27,740.00 USD | 27,890.00 USD | 17,260.00 USD |
| `7D` | `8.33` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 58,510.00 USD | 36,210.00 USD | 20,080.00 USD |
| `1D` | `8.35` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 21,290.00 USD | 16,080.00 USD | 22,350.00 USD |
| `7D` | `8.35` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD |
| `1D` | `8.37` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 26,050.00 USD | 15,950.00 USD | 33,810.00 USD |
| `7D` | `8.37` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 92,990.00 USD | 31,220.00 USD | 38,480.00 USD |
| `1D` | `8.39` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 119,840.00 USD | 18,300.00 USD | 96,440.00 USD |
| `7D` | `8.39` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 226,860.00 USD | 8,930.00 USD | 77,780.00 USD |
| `1D` | `8.41` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 100,070.00 USD | 29,160.00 USD | 88,930.00 USD |
| `7D` | `8.41` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,940.00 USD |
| `1D` | `8.43` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 62,760.00 USD | 47,320.00 USD | 32,810.00 USD |
| `7D` | `8.43` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD |
| `1D` | `8.45` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 108,590.00 USD | 25,950.00 USD | 54,950.00 USD |
| `7D` | `8.45` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD |
| `1D` | `8.47` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 274,020.00 USD | 47,840.00 USD | 68,540.00 USD |
| `7D` | `8.47` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 426,960.00 USD | 70,760.00 USD | 200,480.00 USD |
| `1D` | `8.49` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 267,220.00 USD | 76,720.00 USD | 60,910.00 USD |
| `7D` | `8.49` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 283,720.00 USD | 54,550.00 USD | 118,450.00 USD |
| `1D` | `8.51` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 96,210.00 USD | 63,330.00 USD | 50,250.00 USD |
| `7D` | `8.51` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD |
| `1D` | `8.53` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 66,040.00 USD | 46,880.00 USD | 65,220.00 USD |
| `7D` | `8.53` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD |
| `1D` | `8.55` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 82,660.00 USD | 36,390.00 USD | 70,150.00 USD |
| `7D` | `8.55` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 279,560.00 USD | 136,440.00 USD | 45,090.00 USD |
| `1D` | `8.57` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 183,160.00 USD | 30,520.00 USD | 153,500.00 USD |
| `7D` | `8.57` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 767,620.00 USD | 94,290.00 USD | 93,950.00 USD |
| `1D` | `8.59` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 158,140.00 USD | 56,580.00 USD | 65,290.00 USD |
| `7D` | `8.59` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD |
| `1D` | `8.61` | 836,080.00 USD | 0.00 USD | 836,080.00 USD | 103,430.00 USD | 36,000.00 USD | 55,320.00 USD |
| `7D` | `8.61` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD |
| `1D` | `8.63` | 641,340.00 USD | 0.00 USD | 641,340.00 USD | 180,480.00 USD | 44,210.00 USD | 42,960.00 USD |
| `7D` | `8.63` | 698,910.00 USD | 0.00 USD | 698,910.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD |
| `1D` | `8.65` | 373,680.00 USD | 0.00 USD | 373,680.00 USD | 156,430.00 USD | 43,300.00 USD | 52,200.00 USD |
| `7D` | `8.65` | 598,360.00 USD | 0.00 USD | 598,360.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD |
| `1D` | `8.67` | 121,760.00 USD | 0.00 USD | 121,760.00 USD | 0.00 USD | 0.00 USD | 42,430.00 USD |
| `7D` | `8.67` | 360,310.00 USD | 0.00 USD | 360,310.00 USD | 77,920.00 USD | 24,870.00 USD | 173,920.00 USD |
| `1D` | `8.69` | 79,330.00 USD | 0.00 USD | 79,330.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD |
| `7D` | `8.69` | 83,610.00 USD | 0.00 USD | 83,610.00 USD | 70,550.00 USD | 12,790.00 USD | 270.26 USD |
| `1D` | `8.71` | 52,630.00 USD | 0.00 USD | 52,630.00 USD | 52,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.75` | 67,910.00 USD | 67,910.00 USD | 0.00 USD | 32,080.00 USD | 0.00 USD | 35,830.00 USD |
| `1D` | `8.75` | 135,820.00 USD | 135,820.00 USD | 0.00 USD | 32,080.00 USD | 0.00 USD | 35,830.00 USD |
| `7D` | `8.75` | 19,690.00 USD | 19,690.00 USD | 0.00 USD | 0.00 USD | 19,690.00 USD | 0.00 USD |
| `7D` | `8.75` | 39,370.00 USD | 39,370.00 USD | 0.00 USD | 0.00 USD | 19,690.00 USD | 0.00 USD |
| `1D` | `8.77` | 294,360.00 USD | 294,360.00 USD | 0.00 USD | 132,830.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `8.77` | 120,610.00 USD | 120,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 81,240.00 USD |
| `1D` | `8.79` | 348,480.00 USD | 348,480.00 USD | 0.00 USD | 32,240.00 USD | 12,000.00 USD | 9,880.00 USD |
| `7D` | `8.79` | 173,270.00 USD | 173,270.00 USD | 0.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD |
| `1D` | `8.81` | 354,180.00 USD | 354,180.00 USD | 0.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `8.81` | 181,720.00 USD | 181,720.00 USD | 0.00 USD | 0.00 USD | 8,450.00 USD | 0.00 USD |
| `1D` | `8.85` | 432,100.00 USD | 432,100.00 USD | 0.00 USD | 10,770.00 USD | 2,250.00 USD | 64,900.00 USD |
| `1D` | `8.89` | 450,570.00 USD | 450,570.00 USD | 0.00 USD | 0.00 USD | 11,100.00 USD | 7,370.00 USD |
| `7D` | `8.89` | 254,770.00 USD | 254,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 73,050.00 USD |
| `1D` | `8.91` | 588,840.00 USD | 588,840.00 USD | 0.00 USD | 40,950.00 USD | 7,360.00 USD | 89,960.00 USD |
| `7D` | `8.91` | 401,370.00 USD | 401,370.00 USD | 0.00 USD | 57,910.00 USD | 0.00 USD | 88,700.00 USD |
| `1D` | `8.93` | 600,410.00 USD | 600,410.00 USD | 0.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD |
| `1D` | `8.95` | 605,710.00 USD | 605,710.00 USD | 0.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD |
| `1D` | `8.99` | 692,760.00 USD | 692,760.00 USD | 0.00 USD | 40,450.00 USD | 36,070.00 USD | 10,530.00 USD |
| `7D` | `8.99` | 495,610.00 USD | 495,610.00 USD | 0.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.01` | 757,920.00 USD | 757,920.00 USD | 0.00 USD | 38,030.00 USD | 5,120.00 USD | 22,000.00 USD |
| `7D` | `9.01` | 737,830.00 USD | 737,830.00 USD | 0.00 USD | 185,270.00 USD | 36,180.00 USD | 20,780.00 USD |
| `1D` | `9.03` | 963,300.00 USD | 963,300.00 USD | 0.00 USD | 106,640.00 USD | 66,510.00 USD | 32,240.00 USD |
| `7D` | `9.03` | 912,880.00 USD | 912,880.00 USD | 0.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD |
| `1D` | `9.05` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 22,480.00 USD | 37,250.00 USD | 49,400.00 USD |
| `7D` | `9.05` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD |
| `1D` | `9.07` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 41,700.00 USD | 30,110.00 USD | 52,770.00 USD |
| `7D` | `9.07` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD |
| `1D` | `9.09` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 121,690.00 USD | 27,290.00 USD | 81,450.00 USD |
| `7D` | `9.09` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 179,590.00 USD | 8,680.00 USD | 143,810.00 USD |
| `1D` | `9.11` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 118,620.00 USD | 34,700.00 USD | 55,780.00 USD |
| `7D` | `9.11` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD |
| `1D` | `9.13` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 190,770.00 USD | 51,740.00 USD | 46,370.00 USD |
| `7D` | `9.13` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.15` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 92,380.00 USD | 30,600.00 USD | 49,860.00 USD |
| `7D` | `9.15` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD |
| `1D` | `9.17` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 170,750.00 USD | 37,660.00 USD | 80,240.00 USD |
| `7D` | `9.17` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD |
| `1D` | `9.19` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 178,200.00 USD | 76,590.00 USD | 58,100.00 USD |
| `7D` | `9.19` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 503,250.00 USD | 101,150.00 USD | 193,800.00 USD |
| `1D` | `9.21` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 121,150.00 USD | 15,610.00 USD | 66,720.00 USD |
| `7D` | `9.21` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 554,780.00 USD | 132,850.00 USD | 277,570.00 USD |
| `1D` | `9.23` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 134,640.00 USD | 13,360.00 USD | 39,000.00 USD |
| `7D` | `9.23` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD |
| `1D` | `9.25` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 49,760.00 USD | 8,330.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD |
| `1D` | `9.27` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 39,300.00 USD | 4,490.00 USD | 2,610.00 USD |
| `7D` | `9.27` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD |
| `1D` | `9.29` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 37,140.00 USD | 8,000.00 USD | 17,960.00 USD |
| `7D` | `9.29` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD |
| `1D` | `9.31` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 70,040.00 USD | 13,670.00 USD | 12,890.00 USD |
| `7D` | `9.31` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD |
| `1D` | `9.33` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 16,620.00 USD | 8,530.00 USD | 15,350.00 USD |
| `7D` | `9.33` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 124,660.00 USD | 64,710.00 USD | 179,090.00 USD |
| `1D` | `9.35` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 44,830.00 USD | 8,000.00 USD | 33,470.00 USD |
| `7D` | `9.35` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 289,480.00 USD | 88,340.00 USD | 96,310.00 USD |
| `1D` | `9.37` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 67,060.00 USD | 24,480.00 USD | 19,020.00 USD |
| `7D` | `9.37` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD |
| `1D` | `9.39` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 38,740.00 USD | 4,040.00 USD | 25,180.00 USD |
| `7D` | `9.39` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 206,980.00 USD | 57,260.00 USD | 87,830.00 USD |
| `1D` | `9.41` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 65,590.00 USD | 2,860.00 USD | 13,990.00 USD |
| `7D` | `9.41` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD |
| `1D` | `9.43` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 20,770.00 USD | 2,260.00 USD | 16,420.00 USD |
| `7D` | `9.43` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD |
| `1D` | `9.45` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `9.45` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD |
| `1D` | `9.47` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 2,610.00 USD | 5,690.00 USD | 192.20 USD |
| `7D` | `9.47` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD |
| `1D` | `9.49` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 22,170.00 USD | 572.85 USD | 10,750.00 USD |
| `7D` | `9.49` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD |
| `1D` | `9.51` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 12,280.00 USD | 3,160.00 USD | 124.70 USD |
| `7D` | `9.51` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD |
| `1D` | `9.53` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 35,960.00 USD | 7,630.00 USD | 5,400.00 USD |
| `7D` | `9.53` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD |
| `1D` | `9.55` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 8,810.00 USD | 7,800.00 USD | 6,030.00 USD |
| `7D` | `9.55` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 28,850.00 USD | 17,400.00 USD | 880.26 USD |
| `1D` | `9.57` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 6,420.00 USD | 4,390.00 USD | 7,390.00 USD |
| `7D` | `9.57` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD |
| `1D` | `9.59` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 5,940.00 USD | 3,060.00 USD | 10,340.00 USD |
| `7D` | `9.59` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 26,920.00 USD | 13,200.00 USD | 28,860.00 USD |
| `1D` | `9.61` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 29,640.00 USD | 4,570.00 USD | 25,310.00 USD |
| `7D` | `9.61` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 93,670.00 USD | 13,850.00 USD | 29,040.00 USD |
| `1D` | `9.63` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 11,160.00 USD | 4,370.00 USD | 1,150.00 USD |
| `7D` | `9.63` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD |
| `1D` | `9.65` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 11,480.00 USD | 5,210.00 USD | 5,130.00 USD |
| `7D` | `9.65` | 14,330,000.00 USD | 14,330,000.00 USD | 0.00 USD | 33,020.00 USD | 20,230.00 USD | 18,240.00 USD |
| `1D` | `9.67` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 11,920.00 USD | 3,480.00 USD | 8,060.00 USD |
| `7D` | `9.67` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD |
| `1D` | `9.69` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 21,130.00 USD | 5,660.00 USD | 3,970.00 USD |
| `7D` | `9.69` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD |
| `1D` | `9.71` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 11,610.00 USD | 9,310.00 USD | 8,590.00 USD |
| `7D` | `9.71` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD |
| `1D` | `9.73` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 2,760.00 USD | 3,700.00 USD | 13.70 USD |
| `7D` | `9.73` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD |
| `1D` | `9.75` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 10,750.00 USD | 1,920.00 USD | 4,040.00 USD |
| `7D` | `9.75` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD |
| `1D` | `9.77` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `9.77` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD |
| `1D` | `9.79` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 5,640.00 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `9.79` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD |
| `1D` | `9.80` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 6,680.00 USD | 770.83 USD | 0.00 USD |
| `7D` | `9.81` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 103,830.00 USD | 23,930.00 USD | 48,290.00 USD |
| `7D` | `9.83` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD |
| `7D` | `9.85` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD |
| `7D` | `9.87` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD |
| `7D` | `9.89` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD |
| `7D` | `9.91` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD |
| `7D` | `9.93` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD |
| `7D` | `9.95` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD |
| `7D` | `9.97` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD |
| `7D` | `9.99` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD |
| `7D` | `10.01` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD |
| `7D` | `10.03` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `375.46M` | Total OI Tokens: `42,920,950.3 AVAX`
  * 1h OI Change: `-1.15%` | 4h OI Change: `-2.83%` | 24h OI Change: `-5.39%`
  * Exchange Breakdown: Binance=`88.09M` | Bybit=`58.71M` | OKX=`12.56M` | Hyperliquid=`17.32M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.85K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0042%` | **USDT KuCoin** | `0.0092%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0052%` | **USDT Bitget** | `0.0086%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `44.03%` | `55.97%` | `0.79` | 24,580,000.00 USD |
| `15M` | `Binance` | `47.6%` | `52.4%` | `0.91` | 8,010,000.00 USD |
| `15M` | `OKX` | `34.64%` | `65.36%` | `0.53` | 2,920,000.00 USD |
| `15M` | `Bybit` | `46.57%` | `53.43%` | `0.87` | 2,790,000.00 USD |
| `15M` | `KuCoin` | `46.44%` | `53.56%` | `0.87` | 220,790.00 USD |
| `15M` | `Gate` | `48.4%` | `51.6%` | `0.94` | 406,280.00 USD |
| `15M` | `Bitget` | `47.62%` | `52.38%` | `0.91` | 1,070,000.00 USD |
| `15M` | `BingX` | `26.11%` | `73.89%` | `0.35` | 609,540.00 USD |
| `15M` | `MEXC` | `49.45%` | `50.55%` | `0.98` | 5,340,000.00 USD |
| `15M` | `Bitunix` | `53.77%` | `46.23%` | `1.16` | 1,240,000.00 USD |
| `15M` | `Hyperliquid` | `14.21%` | `85.79%` | `0.17` | 815,130.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.21%` | `51.79%` | `0.93` | 275,340.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `23.67%` | `76.33%` | `0.31` | 401,250.00 USD |
| `15M` | `HTX` | `51.07%` | `48.93%` | `1.04` | 7,970.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `27.67%` | `72.33%` | `0.38` | 214,580.00 USD |
| `15M` | `Aster` | `2.62%` | `97.38%` | `0.03` | 201,190.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `13.93%` | `86.07%` | `0.16` | 46,750.00 USD |
| `15M` | `Whale Positions` | `47.6%` | `52.4%` | `0.91` | 8,010,000.00 USD |
| `15M` | `Global Accounts` | `44.03%` | `55.97%` | `0.79` | 24,580,000.00 USD |
| `1H` | `AVAX` | `47.29%` | `52.71%` | `0.90` | 36,410,000.00 USD |
| `1H` | `Binance` | `49.45%` | `50.55%` | `0.98` | 10,600,000.00 USD |
| `1H` | `OKX` | `48.24%` | `51.76%` | `0.93` | 4,320,000.00 USD |
| `1H` | `Bybit` | `50.23%` | `49.77%` | `1.01` | 3,210,000.00 USD |
| `1H` | `KuCoin` | `48.78%` | `51.22%` | `0.95` | 250,920.00 USD |
| `1H` | `Gate` | `46.89%` | `53.11%` | `0.88` | 578,700.00 USD |
| `1H` | `Bitget` | `51.07%` | `48.93%` | `1.04` | 1,450,000.00 USD |
| `1H` | `BingX` | `35.18%` | `64.82%` | `0.54` | 964,020.00 USD |
| `1H` | `MEXC` | `49.51%` | `50.49%` | `0.98` | 10,570,000.00 USD |
| `1H` | `Bitunix` | `54.95%` | `45.05%` | `1.22` | 1,470,000.00 USD |
| `1H` | `Hyperliquid` | `21.48%` | `78.52%` | `0.27` | 1,030,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.65%` | `50.35%` | `0.99` | 564,400.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `11.08%` | `88.92%` | `0.12` | 834,510.00 USD |
| `1H` | `HTX` | `57.52%` | `42.48%` | `1.35` | 15,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `40.88%` | `59.12%` | `0.69` | 267,480.00 USD |
| `1H` | `Aster` | `7.95%` | `92.05%` | `0.09` | 198,020.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.44%` | `53.56%` | `0.87` | 81,250.00 USD |
| `1H` | `Whale Positions` | `49.45%` | `50.55%` | `0.98` | 10,600,000.00 USD |
| `1H` | `Global Accounts` | `47.29%` | `52.71%` | `0.90` | 36,410,000.00 USD |
| `4H` | `AVAX` | `41.95%` | `58.05%` | `0.72` | 108,640,000.00 USD |
| `4H` | `Binance` | `43.04%` | `56.96%` | `0.76` | 30,740,000.00 USD |
| `4H` | `OKX` | `42.28%` | `57.72%` | `0.73` | 10,240,000.00 USD |
| `4H` | `Bybit` | `45.21%` | `54.79%` | `0.83` | 8,430,000.00 USD |
| `4H` | `KuCoin` | `44.88%` | `55.12%` | `0.81` | 846,230.00 USD |
| `4H` | `Gate` | `49.84%` | `50.16%` | `0.99` | 1,390,000.00 USD |
| `4H` | `Bitget` | `39.08%` | `60.92%` | `0.64` | 3,360,000.00 USD |
| `4H` | `BingX` | `44.61%` | `55.39%` | `0.81` | 3,810,000.00 USD |
| `4H` | `MEXC` | `49.13%` | `50.87%` | `0.97` | 37,100,000.00 USD |
| `4H` | `Bitunix` | `48.36%` | `51.64%` | `0.94` | 3,670,000.00 USD |
| `4H` | `Hyperliquid` | `34.83%` | `65.17%` | `0.53` | 2,910,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.25%` | `50.75%` | `0.97` | 2,110,000.00 USD |
| `4H` | `Crypto.com` | `81.82%` | `18.18%` | `4.50` | 0.00 USD |
| `4H` | `WhiteBIT` | `0.07%` | `99.93%` | `0.00` | 2,790,000.00 USD |
| `4H` | `HTX` | `40.02%` | `59.98%` | `0.67` | 42,780.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.07%` | `50.93%` | `0.96` | 664,890.00 USD |
| `4H` | `Aster` | `44.15%` | `55.85%` | `0.79` | 402,440.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.49%` | `72.51%` | `0.38` | 149,330.00 USD |
| `4H` | `Whale Positions` | `43.04%` | `56.96%` | `0.76` | 30,740,000.00 USD |
| `4H` | `Global Accounts` | `41.95%` | `58.05%` | `0.72` | 108,640,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.82` | 1,418,137.84 USD | 651,843.02 USD | 766,294.83 USD | -114,451.81 USD | `-8.07%` | `11B / 12S` |
| `0:00 UTC` | `8.87` | `8.87` | `8.87` | `8.88` | `8.86` | 651,856.32 USD | 369,195.26 USD | 282,661.06 USD | 86,534.20 USD | `+13.28%` | `5B / 4S` |
| `5:00 UTC` | `8.84` | `8.86` | `8.84` | `8.89` | `8.84` | 682,076.12 USD | 288,770.26 USD | 393,305.86 USD | -104,535.61 USD | `-15.33%` | `9B / 13S` |
| `0:00 UTC` | `8.81` | `8.81` | `8.81` | `8.84` | `8.80` | 1,762,248.06 USD | 773,632.57 USD | 988,615.48 USD | -214,982.91 USD | `-12.20%` | `7B / 6S` |
| `5:00 UTC` | `8.84` | `8.83` | `8.84` | `8.86` | `8.79` | 750,878.19 USD | 458,225.53 USD | 292,652.66 USD | 165,572.87 USD | `+22.05%` | `19B / 3S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 637,816.13 USD | 328,825.06 USD | 308,991.07 USD | 19,833.99 USD | `+3.11%` | `4B / 4S` |
| `5:00 UTC` | `8.81` | `8.82` | `8.81` | `8.84` | `8.80` | 548,929.60 USD | 300,754.28 USD | 248,175.32 USD | 52,578.96 USD | `+9.58%` | `18B / 4S` |
| `0:00 UTC` | `8.86` | `8.86` | `8.86` | `8.87` | `8.83` | 587,148.06 USD | 393,702.30 USD | 193,445.76 USD | 200,256.54 USD | `+34.11%` | `5B / 1S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.84` | 431,773.06 USD | 190,520.19 USD | 241,252.88 USD | -50,732.69 USD | `-11.75%` | `8B / 6S` |
| `0:00 UTC` | `8.69` | `8.73` | `8.69` | `8.86` | `8.66` | 5,081,590.75 USD | 2,287,066.92 USD | 2,794,523.83 USD | -507,456.90 USD | `-9.99%` | `5B / 26S` |

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
| `5m` | -77,360.00 USD | 256,490.00 USD | **`ACCUMULATION`** |
| `15m` | -232,310.00 USD | -968,260.00 USD | **`DISTRIBUTION`** |
| `30m` | -256,080.00 USD | -1,050,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -352,430.00 USD | -567,180.00 USD | **`DISTRIBUTION`** |
| `2h` | -273,750.00 USD | -650,170.00 USD | **`DISTRIBUTION`** |
| `4h` | -558,700.00 USD | -5,020,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -26,970.00 USD | -3,750,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -272,040.00 USD | -4,050,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -430,440.00 USD | -3,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -185,570.00 USD | -7,470,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,140,000.00 USD | -43,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -54,090,000.00 USD | -273,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-77.36K` | 15m=`-232.31K` | 1h=`-352.43K` | 24h=`-185.57K`
* Futures Capital Netflows: 5m=`+256.49K` | 15m=`-968.26K` | 1h=`-567.18K` | 24h=`-7.47M`
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
  * Execution Entry: `8.58` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.46` (Risk Distance: `0.1199` pts)
  * +2.5R Take Profit: `8.88`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.90` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.02` (Risk Distance: `0.1199` pts)
  * +2.5R Take Profit: `8.60`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
