# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:43:23 IST` (`2026-10-30 04:13:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.38` | **Live Ask Quote**: `8.42` | **Mid Price**: `8.40`
- **Spread Points**: `4.00` | **Spread BPS**: `47.62 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.40` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.46` | Lower -3.00σ Band: `8.34`
  * Upper +2.51σ Band: `8.45` | Lower -2.51σ Band: `8.35`
  * Upper +2.01σ Band: `8.44` | Lower -2.01σ Band: `8.36`
  * Upper +2.00σ Band: `8.43` | Lower -2.00σ Band: `8.37`
  * Upper +1.28σ Band: `8.42` | Lower -1.28σ Band: `8.38`
  * Upper +1.00σ Band: `8.42` | Lower -1.00σ Band: `8.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.40` | EMA-20=`8.40` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.40` (Slope: `+0.0000`) | EMA-100=`8.40`
  * Institutional Anchors: EMA-144=`8.40` | EMA-200=`8.40` (Slope: `+0.0000`) | EMA-233=`8.40`
- **Range Boundaries**: 24H High=`8.48` | 24H Low=`8.32` | Weekly High=`8.57` | Weekly Low=`8.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.42` (Distance: `-0.28%`)
  * Point of Control (POC) = `8.32` (Distance: `+0.94%`)
  * Value Area Low (VAL) = `8.16` (Distance: `+3.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.73`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.43` | Low=`8.37`
  * New York Session (13:00-21:00 UTC): High=`8.45` | Low=`8.35`
  * Initial Balance (First Hour): IB High=`8.43` | IB Low=`8.37`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.37` - `8.43`
  * Optimal Trade Entry (OTE 0.705): `8.42`
  * Structural Invalidation Anchor (0.786): `8.47`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.41` | `8.44` | `8.40` | `8.43` | `56,352` | 474,219.41 USD | 10,205.07 USD | `+2.15%` | -5,106,219.12 USD | `-0.33` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `8.43` | `8.46` | `8.43` | `8.46` | `54,326` | 458,520.53 USD | 120,010.44 USD | `+26.17%` | -4,986,208.69 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.46` | `8.48` | `8.45` | `8.47` | `45,418` | 384,404.94 USD | 108,605.15 USD | `+28.25%` | -4,877,603.53 USD | `+0.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.33` | `8.39` | `8.33` | `8.38` | `205,673` | 1,720,663.97 USD | 698,930.79 USD | `+40.62%` | -5,316,140.31 USD | `+0.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.38` | `8.46` | `8.37` | `8.46` | `166,214` | 1,398,848.87 USD | 114,334.05 USD | `+8.17%` | -5,201,806.26 USD | `+0.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.46` | `8.48` | `8.45` | `8.47` | `45,418` | 384,404.94 USD | 108,605.15 USD | `+28.25%` | -5,093,201.11 USD | `+0.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.21` | `8.28` | `8.11` | `8.21` | `1,052,344` | 8,640,631.11 USD | 498,870.95 USD | `+5.77%` | -6,594,407.45 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.21` | `8.35` | `8.15` | `8.31` | `481,486` | 3,984,789.43 USD | 490,929.32 USD | `+12.32%` | -6,103,478.13 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.31` | `8.48` | `8.31` | `8.47` | `510,880` | 4,284,713.76 USD | 1,010,277.02 USD | `+23.58%` | -5,093,201.11 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.47` | `4,866,262` | 39,874,547.45 USD | 485,724.31 USD | `+1.22%` | -5,093,201.11 USD | `+0.89` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | 322,838.02 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | 269,016.05 USD | `-1.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,242,979.60 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,578,925.42 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.47` | `4,866,262` | 39,874,547.45 USD | 485,724.31 USD | `+1.22%` | -5,093,201.11 USD | `+0.89` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.40`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `8.41` | `112.4500` | 946.27 USD | 12,058.62 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.41` | `135.3100` | 1,138.59 USD | 11,112.35 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.41` | `112.4500` | 946.19 USD | 9,973.76 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.41` | `20.8000` | 175.01 USD | 9,027.57 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.41` | `112.5000` | 946.56 USD | 8,852.55 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.41` | `226.5400` | 1,905.95 USD | 7,905.99 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `8.41` | `713.1700` | 6,000.04 USD | 6,000.04 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.41` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.41` | `0.00%` | `-` |
| `BID` | `8.41` | `16.0000` | 134.58 USD | 134.58 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.41` | `150.1300` | 1,262.76 USD | 1,397.34 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.41` | `131.3000` | 1,104.29 USD | 2,501.62 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.41` | `2.9700` | 24.98 USD | 2,526.60 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.41` | `112.5100` | 946.21 USD | 3,472.81 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.41` | `18.6500` | 156.84 USD | 3,629.65 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.41` | `84.3300` | 709.19 USD | 4,338.84 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.41` | `126.0200` | 1,059.75 USD | 5,398.60 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.41` | `112.4500` | 945.59 USD | 6,344.19 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.41` | `5.5600` | 46.75 USD | 6,390.94 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.41` | `112.4500` | 945.51 USD | 7,336.45 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.41` | `137.5600` | 1,156.60 USD | 8,493.06 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.41` | `112.4500` | 945.43 USD | 9,438.49 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.41` | `5.8000` | 48.76 USD | 9,487.25 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.41` | `112.4500` | 945.36 USD | 10,432.61 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.41` | `237.7000` | 1,998.27 USD | 12,430.88 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.41` | `1410.6800` | 11,858.88 USD | 24,289.76 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.41` | `137.5600` | 1,156.36 USD | 25,446.12 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.41` | `112.4500` | 945.25 USD | 26,391.38 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.41` | `1915.5900` | 16,101.87 USD | 42,493.25 USD | `2 orders` | `-0.08%` | `-` |
| `ASK` | `8.42` | `112.8100` | 949.69 USD | 58,514.47 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.42` | `118.7900` | 1,000.00 USD | 57,564.78 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.42` | `200.0000` | 1,683.54 USD | 56,564.78 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.42` | `5.8000` | 48.82 USD | 54,881.24 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.42` | `1308.1000` | 11,010.80 USD | 54,832.42 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.42` | `467.8500` | 3,937.94 USD | 43,821.62 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.42` | `1783.5900` | 15,012.48 USD | 39,883.68 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.42` | `112.5000` | 946.90 USD | 24,871.20 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.42` | `112.4500` | 946.42 USD | 23,924.30 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.42` | `112.4500` | 946.39 USD | 22,977.87 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.42` | `950.6200` | 8,000.42 USD | 22,031.48 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.42` | `118.8200` | 999.97 USD | 14,031.06 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.42` | `115.5600` | 972.48 USD | 13,031.10 USD | `2 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1489` | `0x7737...bf66` | `SHORT` | 1,444,482.97 USD | `171,568.06` | `7.43` | `8.41` | `105.63` | -168,937.95 USD | `-11.70%` | `10X Cross` |
| `1577` | `0xeadc...9d55` | `LONG` | 1,347,682.07 USD | `160,070.56` | `8.11` | `8.41` | `0.000000` | 50,044.49 USD | `+3.71%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.89` | 5,999.48 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8930 USD [API] | `2026-10-29 01:10:17` |
| `ANNOUNCEMENT` | `INFO` | `8.91` | 5,999.75 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.9103 USD [API] | `2026-10-29 01:20:09` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.55` (Vol: 398,300.00 USD, Dist: `+1.32%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.54%`)
  * 48H Horizon: Short MP=`8.55` (Vol: 398,300.00 USD, Dist: `+1.28%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.57%`)
  * 3D Horizon: Short MP=`8.55` (Vol: 398,300.00 USD, Dist: `+1.28%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.57%`)
  * 7D Horizon: Short MP=`9.23` (Vol: 459,400.00 USD, Dist: `+9.36%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.57%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.69` | 793.33 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 221.37 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 595.77 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 218.85 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 1,350.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 257.03 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 903.69 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 265.08 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 583.75 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 164.85 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 275.43 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 126.65 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 128.76 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 3,920.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 340.97 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 574.72 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 161.46 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,150.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 107.06 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 23,310.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 25,570.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 582.41 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 1,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 133.53 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.87` | 15,390.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 686.37 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 198.27 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.42` | 2,940.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.58` | 426.94 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,930.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 2,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.79` | 2,390.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 17,380.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 10,380.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 2,530.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.07` | 506.50 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 651.75 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 915.43 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 1,220.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.20` | 480.07 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 121.68 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 6,210.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 162,780.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 512.43 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,760.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.62` | 2,810.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.66` | 132.67 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 231.68 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 147.33 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,970.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 902.40 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 2,150.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 145.88 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.88` | 375.17 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 957.69 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 105.61 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 2,420.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 2,450.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,410.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 7,090.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 1,460.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 257.99 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.51` | 651.50 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.66` | 373,080.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 747,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,570.00 USD | 746,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 729,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 2,900.00 USD | 723,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 720,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 21,580.00 USD | 713,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 6,270.00 USD | 692,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 685,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 684,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 410.80 USD | 677,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,710.00 USD | 676,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 672,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 671,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 670,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,980.00 USD | 667,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 663,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 659,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 659,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 297.49 USD | 530,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 746.58 USD | 530,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 21,670.00 USD | 529,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 507,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 354.23 USD | 506,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,600.00 USD | 505,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 7,420.00 USD | 482,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 644.88 USD | 474,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 474,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 472,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 443,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 443,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 442,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 422,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 2,890.00 USD | 419,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 29,180.00 USD | 416,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 387,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 386,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 386,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.28` | 1,460.00 USD | 364,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,840.00 USD | 363,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 326,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 324,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 3,590,000.00 USD | 3,590,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 320,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 317,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 3,580,000.00 USD | 3,580,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.41` | 13,230.00 USD | 316,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.42` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 303,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 303,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.44` | 3,230,000.00 USD | 3,230,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.44` | 3,570,000.00 USD | 3,570,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 300,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 300,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.46` | 3,210,000.00 USD | 3,210,000.00 USD | 7,860.00 USD | 0.00 USD | 52,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.46` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 289,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 285,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.48` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.48` | 3,540,000.00 USD | 3,540,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 2,010.00 USD | 284,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.50` | 3,130,000.00 USD | 3,130,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 282,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 281,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.52` | 3,110,000.00 USD | 3,110,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.52` | 3,520,000.00 USD | 3,520,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 280,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 278,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 415.52 USD | 274,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.56` | 3,030,000.00 USD | 3,030,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.56` | 3,480,000.00 USD | 3,480,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 273,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 248,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.58` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 26,280.00 USD | 248,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 3,010,000.00 USD | 3,010,000.00 USD | 405.20 USD | 3,770.00 USD | 194.10 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 1,140.00 USD | 222,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 221,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 3,010,000.00 USD | 3,010,000.00 USD | 583.80 USD | 0.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 220,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 219,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 2,990,000.00 USD | 2,990,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 3,450,000.00 USD | 3,450,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 219,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 219,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 219,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.68` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 214,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 3,250.00 USD | 213,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 2,970,000.00 USD | 2,970,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 2,950,000.00 USD | 2,950,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 2,930,000.00 USD | 2,930,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 3,390,000.00 USD | 3,390,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 210,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 2,920,000.00 USD | 2,920,000.00 USD | 1,660.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 3,390,000.00 USD | 3,390,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 210,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 8,670.00 USD | 209,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 2,910,000.00 USD | 2,910,000.00 USD | 44,950.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 3,380,000.00 USD | 3,380,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 2,470.00 USD | 200,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 198,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 2,850,000.00 USD | 2,850,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 3,310,000.00 USD | 3,310,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 193,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 2,070.00 USD | 187,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 2,800,000.00 USD | 2,800,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 3,280,000.00 USD | 3,280,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 2,270.00 USD | 185,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.84` | 2,780,000.00 USD | 2,780,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 3,270,000.00 USD | 3,270,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 183,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 2,760,000.00 USD | 2,760,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 3,210,000.00 USD | 3,210,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 160,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 160,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 2,720,000.00 USD | 2,720,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 3,160,000.00 USD | 3,160,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 1,430.00 USD | 159,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 2,650,000.00 USD | 2,650,000.00 USD | 14,350.00 USD | 7,630.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 3,060,000.00 USD | 3,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 158,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.92` | 2,620,000.00 USD | 2,620,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 3,000,000.00 USD | 3,000,000.00 USD | 55,490.00 USD | 8,420.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 157,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 153,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 2,580,000.00 USD | 2,580,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 2,920,000.00 USD | 2,920,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 137,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.96` | 245.57 USD | 9,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 2,510,000.00 USD | 2,510,000.00 USD | 20,670.00 USD | 11,220.00 USD | 149,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 2,830,000.00 USD | 2,830,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 9,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 2,330,000.00 USD | 2,330,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 2,710,000.00 USD | 2,710,000.00 USD | 56,660.00 USD | 26,790.00 USD | 146,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 6,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 2,270,000.00 USD | 2,270,000.00 USD | 1,500.00 USD | 22,850.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 2,480,000.00 USD | 2,480,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 2,180,000.00 USD | 2,180,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 2,400,000.00 USD | 2,400,000.00 USD | 20,910.00 USD | 46,670.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 2,010,000.00 USD | 2,010,000.00 USD | 33,700.00 USD | 17,810.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 2,280,000.00 USD | 2,280,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 1,940,000.00 USD | 1,940,000.00 USD | 76,840.00 USD | 22,300.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 1,980,000.00 USD | 1,980,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 1,820,000.00 USD | 1,820,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 1,760,000.00 USD | 1,760,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 1,770,000.00 USD | 1,770,000.00 USD | 30,110.00 USD | 14,390.00 USD | 96,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 1,720,000.00 USD | 1,720,000.00 USD | 61,500.00 USD | 19,700.00 USD | 15,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.12` | 1,620,000.00 USD | 1,620,000.00 USD | 110,990.00 USD | 12,270.00 USD | 319,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 1,620,000.00 USD | 1,620,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 1,180,000.00 USD | 1,180,000.00 USD | 12,410.00 USD | 0.00 USD | 58,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 1,440,000.00 USD | 1,440,000.00 USD | 72,460.00 USD | 25,370.00 USD | 192,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,110,000.00 USD | 1,110,000.00 USD | 44,830.00 USD | 42,030.00 USD | 159,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 1,150,000.00 USD | 1,150,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 864,670.00 USD | 864,670.00 USD | 133,120.00 USD | 19,620.00 USD | 175,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 1,080,000.00 USD | 1,080,000.00 USD | 39,830.00 USD | 43,260.00 USD | 176,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 535,970.00 USD | 535,970.00 USD | 33,560.00 USD | 32,530.00 USD | 17,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 817,140.00 USD | 817,140.00 USD | 92,320.00 USD | 58,100.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 6,270.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 452,680.00 USD | 452,680.00 USD | 32,330.00 USD | 39,650.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 658,310.00 USD | 658,310.00 USD | 117,230.00 USD | 21,570.00 USD | 10,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 345,380.00 USD | 345,380.00 USD | 163,080.00 USD | 10,300.00 USD | 69,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 508,550.00 USD | 508,550.00 USD | 39,950.00 USD | 3,480.00 USD | 107,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 102,620.00 USD | 102,620.00 USD | 15,150.00 USD | 15,590.00 USD | 16,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 357,410.00 USD | 357,410.00 USD | 30,490.00 USD | 5,750.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 55,260.00 USD | 55,260.00 USD | 0.00 USD | 0.00 USD | 57.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 319,300.00 USD | 319,300.00 USD | 122,850.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 195,270.00 USD | 195,270.00 USD | 152,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.31` | 3,720.00 USD | 3,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 55,210.00 USD | 55,210.00 USD | 55,190.00 USD | 0.00 USD | 16.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 42,900.00 USD | 42,900.00 USD | 42,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.34` | 122.98 USD | 122.98 USD | 0.00 USD | 0.00 USD | 122.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.34` | 245.96 USD | 245.96 USD | 0.00 USD | 0.00 USD | 122.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.36` | 263.76 USD | 263.76 USD | 0.00 USD | 0.00 USD | 17.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.36` | 14,290.00 USD | 14,290.00 USD | 0.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.38` | 1,020.00 USD | 1,020.00 USD | 691.75 USD | 0.00 USD | 64.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.38` | 73,260.00 USD | 73,260.00 USD | 0.00 USD | 0.00 USD | 58,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.40` | 108,990.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 35,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.42` | 1,810.00 USD | 1,810.00 USD | 788.46 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.42` | 128,030.00 USD | 128,030.00 USD | 16,070.00 USD | 0.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.44` | 91,790.00 USD | 91,790.00 USD | 0.00 USD | 0.00 USD | 89,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.44` | 138,510.00 USD | 138,510.00 USD | 10,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.46` | 419,730.00 USD | 419,730.00 USD | 35,680.00 USD | 4,700.00 USD | 287,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 623,300.00 USD | 623,300.00 USD | 365,050.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 517,470.00 USD | 517,470.00 USD | 0.00 USD | 39,180.00 USD | 58,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 825,140.00 USD | 825,140.00 USD | 0.00 USD | 49,360.00 USD | 152,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.50` | 805,570.00 USD | 805,570.00 USD | 66,120.00 USD | 101,350.00 USD | 120,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 925,210.00 USD | 925,210.00 USD | 0.00 USD | 100,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.52` | 2,150.00 USD | 5,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.52` | 1,240,000.00 USD | 1,240,000.00 USD | 203,080.00 USD | 69,980.00 USD | 164,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 1,150,000.00 USD | 1,150,000.00 USD | 2,990.00 USD | 135,400.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.54` | 190.93 USD | 6,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.54` | 1,350,000.00 USD | 1,350,000.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 1,360,000.00 USD | 1,360,000.00 USD | 71,540.00 USD | 136,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.55` | 3,220.00 USD | 9,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.56` | 1,570,000.00 USD | 1,570,000.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 2,180,000.00 USD | 2,180,000.00 USD | 691,140.00 USD | 122,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,990,000.00 USD | 1,990,000.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 2,940,000.00 USD | 2,940,000.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 3,060,000.00 USD | 3,060,000.00 USD | 75,040.00 USD | 39,160.00 USD | 388.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 2,510,000.00 USD | 2,510,000.00 USD | 83,560.00 USD | 57,150.00 USD | 201,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 43,670.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 2,660,000.00 USD | 2,660,000.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 2,870,000.00 USD | 2,870,000.00 USD | 78,620.00 USD | 21,010.00 USD | 108,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 16,520.00 USD | 281.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 3,150,000.00 USD | 3,150,000.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 3,880,000.00 USD | 3,880,000.00 USD | 207,090.00 USD | 43,100.00 USD | 334,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 9,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.70` | 3,250,000.00 USD | 3,250,000.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 3,990,000.00 USD | 3,990,000.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 3,320,000.00 USD | 3,320,000.00 USD | 18,250.00 USD | 0.00 USD | 50,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 3,410,000.00 USD | 3,410,000.00 USD | 49,310.00 USD | 28,810.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 4,070,000.00 USD | 4,070,000.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 3,540,000.00 USD | 3,540,000.00 USD | 112,960.00 USD | 2,530.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.78` | 105.04 USD | 9,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.78` | 3,690,000.00 USD | 3,690,000.00 USD | 108,350.00 USD | 11,500.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 4,160,000.00 USD | 4,160,000.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.79` | 423.22 USD | 10,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.80` | 3,890,000.00 USD | 3,890,000.00 USD | 125,120.00 USD | 22,330.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 4,250,000.00 USD | 4,250,000.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 3,910,000.00 USD | 3,910,000.00 USD | 19,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 4,350,000.00 USD | 4,350,000.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 16,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.84` | 4,030,000.00 USD | 4,030,000.00 USD | 40,640.00 USD | 8,820.00 USD | 73,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 4,060,000.00 USD | 4,060,000.00 USD | 13,620.00 USD | 2,250.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 4,470,000.00 USD | 4,470,000.00 USD | 29,310.00 USD | 0.00 USD | 81,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 4,070,000.00 USD | 4,070,000.00 USD | 1,320.00 USD | 8,950.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 4,230,000.00 USD | 4,230,000.00 USD | 31,860.00 USD | 8,140.00 USD | 122,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 4,610,000.00 USD | 4,610,000.00 USD | 2,440.00 USD | 0.00 USD | 115,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 4,300,000.00 USD | 4,300,000.00 USD | 40,710.00 USD | 7,360.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 4,630,000.00 USD | 4,630,000.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 4,370,000.00 USD | 4,370,000.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 4,690,000.00 USD | 4,690,000.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 4,370,000.00 USD | 4,370,000.00 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 4,690,000.00 USD | 4,690,000.00 USD | 1,930.00 USD | 0.00 USD | 432.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 4,420,000.00 USD | 4,420,000.00 USD | 25,040.00 USD | 5,550.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 4,550,000.00 USD | 4,550,000.00 USD | 85,360.00 USD | 30,520.00 USD | 11,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 5,030,000.00 USD | 5,030,000.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 4,650,000.00 USD | 4,650,000.00 USD | 40,920.00 USD | 43,160.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 5,120,000.00 USD | 5,120,000.00 USD | 34,650.00 USD | 56,120.00 USD | 425.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 4,820,000.00 USD | 4,820,000.00 USD | 87,540.00 USD | 43,590.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 5,300,000.00 USD | 5,300,000.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 4,950,000.00 USD | 4,950,000.00 USD | 35,620.00 USD | 33,420.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 5,380,000.00 USD | 5,380,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 5,080,000.00 USD | 5,080,000.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 5,400,000.00 USD | 5,400,000.00 USD | 197,760.00 USD | 43,240.00 USD | 81,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 6,650,000.00 USD | 6,650,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 5,730,000.00 USD | 5,730,000.00 USD | 167,130.00 USD | 47,350.00 USD | 108,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 7,670,000.00 USD | 7,670,000.00 USD | 490,020.00 USD | 24,170.00 USD | 503,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 5,950,000.00 USD | 5,950,000.00 USD | 118,520.00 USD | 23,510.00 USD | 79,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 8,730,000.00 USD | 8,730,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 6,180,000.00 USD | 6,180,000.00 USD | 121,810.00 USD | 44,640.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 9,320,000.00 USD | 9,320,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 6,500,000.00 USD | 6,500,000.00 USD | 174,230.00 USD | 44,900.00 USD | 105,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 10,340,000.00 USD | 10,340,000.00 USD | 565,140.00 USD | 162,460.00 USD | 291,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.19` | 1,590.00 USD | 17,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 6,740,000.00 USD | 6,740,000.00 USD | 141,410.00 USD | 43,540.00 USD | 51,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 11,270,000.00 USD | 11,270,000.00 USD | 549,250.00 USD | 134,550.00 USD | 238,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 1,870.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 6,850,000.00 USD | 6,850,000.00 USD | 86,390.00 USD | 10,580.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 12,410,000.00 USD | 12,410,000.00 USD | 585,170.00 USD | 144,840.00 USD | 417,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 6,910,000.00 USD | 6,910,000.00 USD | 47,010.00 USD | 4,270.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 12,980,000.00 USD | 12,980,000.00 USD | 335,740.00 USD | 56,410.00 USD | 173,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 6,960,000.00 USD | 6,960,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 13,410,000.00 USD | 13,410,000.00 USD | 273,920.00 USD | 96,980.00 USD | 61,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 7,020,000.00 USD | 7,020,000.00 USD | 44,530.00 USD | 10,920.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 14,110,000.00 USD | 14,110,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 7,120,000.00 USD | 7,120,000.00 USD | 59,470.00 USD | 13,560.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 14,670,000.00 USD | 14,670,000.00 USD | 199,810.00 USD | 97,780.00 USD | 263,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 7,180,000.00 USD | 7,180,000.00 USD | 37,200.00 USD | 4,250.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 15,340,000.00 USD | 15,340,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 7,250,000.00 USD | 7,250,000.00 USD | 40,730.00 USD | 9,520.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 15,670,000.00 USD | 15,670,000.00 USD | 204,260.00 USD | 53,150.00 USD | 69,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 7,340,000.00 USD | 7,340,000.00 USD | 52,470.00 USD | 10,420.00 USD | 33,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 16,090,000.00 USD | 16,090,000.00 USD | 247,120.00 USD | 73,430.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 128.44 USD | 19,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.38` | 7,390,000.00 USD | 7,390,000.00 USD | 29,420.00 USD | 7,320.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 16,620,000.00 USD | 16,620,000.00 USD | 383,530.00 USD | 55,400.00 USD | 93,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 7,430,000.00 USD | 7,430,000.00 USD | 31,880.00 USD | 0.00 USD | 25.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 17,020,000.00 USD | 17,020,000.00 USD | 234,760.00 USD | 42,520.00 USD | 124,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 20,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 7,450,000.00 USD | 7,450,000.00 USD | 10,810.00 USD | 2,390.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 17,290,000.00 USD | 17,290,000.00 USD | 176,920.00 USD | 19,780.00 USD | 71,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 7,480,000.00 USD | 7,480,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 17,410,000.00 USD | 17,410,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 17,520,000.00 USD | 17,520,000.00 USD | 60,020.00 USD | 29,830.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 138.85 USD | 20,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.48` | 17,580,000.00 USD | 17,580,000.00 USD | 12,180.00 USD | 27,840.00 USD | 26,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 17,750,000.00 USD | 17,750,000.00 USD | 89,460.00 USD | 33,210.00 USD | 45,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 17,940,000.00 USD | 17,940,000.00 USD | 102,150.00 USD | 29,320.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 18,150,000.00 USD | 18,150,000.00 USD | 192,090.00 USD | 25,090.00 USD | 378.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 18,260,000.00 USD | 18,260,000.00 USD | 88,510.00 USD | 5,260.00 USD | 13,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 18,340,000.00 USD | 18,340,000.00 USD | 35,340.00 USD | 14,530.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 18,400,000.00 USD | 18,400,000.00 USD | 38,740.00 USD | 5,460.00 USD | 20,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 18,480,000.00 USD | 18,480,000.00 USD | 70,470.00 USD | 1,540.00 USD | 10,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 20,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.64` | 18,560,000.00 USD | 18,560,000.00 USD | 35,210.00 USD | 17,650.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 22,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.66` | 18,630,000.00 USD | 18,630,000.00 USD | 37,340.00 USD | 21,280.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 18,740,000.00 USD | 18,740,000.00 USD | 68,230.00 USD | 20,310.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 18,860,000.00 USD | 18,860,000.00 USD | 77,860.00 USD | 12,990.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 18,960,000.00 USD | 18,960,000.00 USD | 70,300.00 USD | 6,920.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 22,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.74` | 19,010,000.00 USD | 19,010,000.00 USD | 21,230.00 USD | 7,200.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 19,110,000.00 USD | 19,110,000.00 USD | 35,520.00 USD | 12,480.00 USD | 51,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 19,190,000.00 USD | 19,190,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 19,250,000.00 USD | 19,250,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 19,490,000.00 USD | 19,490,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 19,520,000.00 USD | 19,520,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 19,650,000.00 USD | 19,650,000.00 USD | 58,130.00 USD | 2,210.00 USD | 71,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 19,690,000.00 USD | 19,690,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 19,780,000.00 USD | 19,780,000.00 USD | 55,970.00 USD | 19,700.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 19,830,000.00 USD | 19,830,000.00 USD | 27,710.00 USD | 10,810.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.94` | 19,960,000.00 USD | 19,960,000.00 USD | 69,320.00 USD | 11,150.00 USD | 51,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.96` | 298,660.00 USD | 321,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.96` | 20,000,000.00 USD | 20,000,000.00 USD | 29,800.00 USD | 1,360.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 20,030,000.00 USD | 20,030,000.00 USD | 840.10 USD | 4,150.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 20,080,000.00 USD | 20,080,000.00 USD | 16,100.00 USD | 3,650.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.04` | 20,090,000.00 USD | 20,090,000.00 USD | 1,080.00 USD | 3,590.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.06` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.08` | 20,130,000.00 USD | 20,130,000.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 323,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 324,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 107,050.00 USD | 431,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.89` | 100.13 USD | 431,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.97` | 54,880.00 USD | 486,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 493,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.10` | 415.06 USD | 493,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 505,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.29` | 270.63 USD | 505,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.34` | 319.08 USD | 505,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 518,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 814,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.80` | 114.27 USD | 814,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 815,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 816,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 818,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 818,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 906,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.28` | 60,470.00 USD | 967,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 970,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 971,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 971,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.34` | 282.83 USD | 971,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 972,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.04` | 246.72 USD | 972,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.18` | 544.63 USD | 973,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.22` | 4,230.00 USD | 977,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 977,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 978,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 998,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.39` | 6,130.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.72` | 167.79 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.39` | 23,920.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.41` | 266,050.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.46` | 23,290.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.82` | 2,260,000.00 USD | 0.00 USD | 209.88 USD | `-78.39%` | `115.00` |
| `Live` | `Long` | `1.88` | 2,260,000.00 USD | 0.00 USD | 131.25 USD | `-77.80%` | `70.00` |
| `Live` | `Long` | `1.96` | 2,260,000.00 USD | 0.00 USD | 216.63 USD | `-76.86%` | `110.81` |
| `Live` | `Long` | `1.98` | 2,260,000.00 USD | 0.00 USD | 375.23 USD | `-76.62%` | `189.99` |
| `Live` | `Long` | `2.00` | 2,260,000.00 USD | 0.00 USD | 160.40 USD | `-76.26%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,260,000.00 USD | 0.00 USD | 110.52 USD | `-75.91%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,260,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.55%` | `2,382.76` |
| `Live` | `Long` | `2.10` | 2,250,000.00 USD | 0.00 USD | 254.81 USD | `-75.20%` | `121.63` |
| `Live` | `Long` | `2.12` | 2,250,000.00 USD | 0.00 USD | 244.38 USD | `-74.84%` | `115.00` |
| `Live` | `Long` | `2.17` | 2,250,000.00 USD | 0.00 USD | 248.97 USD | `-74.37%` | `115.00` |
| `Live` | `Long` | `2.25` | 2,250,000.00 USD | 0.00 USD | 259.32 USD | `-73.30%` | `115.00` |
| `Live` | `Long` | `2.27` | 2,250,000.00 USD | 0.00 USD | 114.11 USD | `-73.07%` | `50.16` |
| `Live` | `Long` | `2.40` | 2,250,000.00 USD | 0.00 USD | 9,540.00 USD | `-71.65%` | `3,981.48` |
| `Live` | `Long` | `2.65` | 2,240,000.00 USD | 0.00 USD | 124.16 USD | `-68.69%` | `46.94` |
| `Live` | `Long` | `2.69` | 2,240,000.00 USD | 0.00 USD | 942.44 USD | `-68.21%` | `351.00` |
| `Live` | `Long` | `2.79` | 2,240,000.00 USD | 0.00 USD | 144.82 USD | `-67.03%` | `52.00` |
| `Live` | `Long` | `2.83` | 2,240,000.00 USD | 0.00 USD | 324.88 USD | `-66.56%` | `115.00` |
| `Live` | `Long` | `2.87` | 2,240,000.00 USD | 0.00 USD | 232.67 USD | `-66.08%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,240,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.25%` | `15,165.76` |
| `Live` | `Long` | `2.94` | 2,190,000.00 USD | 0.00 USD | 20,590.00 USD | `-65.14%` | `6,990.57` |
| `Live` | `Long` | `2.98` | 2,170,000.00 USD | 0.00 USD | 111.12 USD | `-64.78%` | `37.35` |
| `Live` | `Long` | `3.23` | 2,170,000.00 USD | 0.00 USD | 24,150.00 USD | `-61.70%` | `7,465.11` |
| `Live` | `Long` | `3.37` | 2,150,000.00 USD | 0.00 USD | 389.53 USD | `-60.16%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,150,000.00 USD | 0.00 USD | 151.88 USD | `-60.04%` | `45.00` |
| `Live` | `Long` | `3.48` | 2,150,000.00 USD | 0.00 USD | 1,320.00 USD | `-58.74%` | `377.71` |
| `Live` | `Long` | `3.54` | 2,150,000.00 USD | 0.00 USD | 392.22 USD | `-58.03%` | `110.64` |
| `Live` | `Long` | `3.67` | 2,150,000.00 USD | 0.00 USD | 109.95 USD | `-56.61%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,150,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.55%` | `400.00` |
| `Live` | `Long` | `3.77` | 2,150,000.00 USD | 0.00 USD | 613.09 USD | `-55.43%` | `162.84` |
| `Live` | `Long` | `3.90` | 2,150,000.00 USD | 0.00 USD | 131.73 USD | `-53.89%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,150,000.00 USD | 0.00 USD | 402.70 USD | `-52.35%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,140,000.00 USD | 0.00 USD | 152.29 USD | `-52.11%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,140,000.00 USD | 0.00 USD | 159.29 USD | `-50.93%` | `38.43` |
| `Live` | `Long` | `4.16` | 2,140,000.00 USD | 0.00 USD | 8,310.00 USD | `-50.81%` | `2,000.00` |
| `Live` | `Long` | `4.17` | 2,140,000.00 USD | 0.00 USD | 2,770.00 USD | `-50.69%` | `666.20` |
| `Live` | `Long` | `4.21` | 2,130,000.00 USD | 0.00 USD | 1,690.00 USD | `-50.10%` | `400.00` |
| `Live` | `Long` | `4.24` | 2,130,000.00 USD | 0.00 USD | 365.35 USD | `-49.86%` | `86.27` |
| `Live` | `Long` | `4.45` | 2,130,000.00 USD | 0.00 USD | 110.77 USD | `-47.38%` | `24.92` |
| `Live` | `Long` | `4.46` | 2,130,000.00 USD | 0.00 USD | 415.74 USD | `-47.26%` | `93.32` |
| `Live` | `Long` | `4.59` | 2,130,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.60%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,100,000.00 USD | 0.00 USD | 486.93 USD | `-45.36%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,100,000.00 USD | 0.00 USD | 2,930.00 USD | `-45.25%` | `634.06` |
| `Live` | `Long` | `4.66` | 2,100,000.00 USD | 0.00 USD | 105.11 USD | `-44.89%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,100,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.77%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,090,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.65%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,090,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.54%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,080,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.42%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,080,000.00 USD | 0.00 USD | 521.95 USD | `-43.83%` | `110.00` |
| `Live` | `Long` | `4.76` | 2,080,000.00 USD | 0.00 USD | 105.64 USD | `-43.59%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,080,000.00 USD | 0.00 USD | 207.81 USD | `-42.88%` | `43.07` |
| `Live` | `Long` | `4.83` | 2,080,000.00 USD | 0.00 USD | 467.01 USD | `-42.76%` | `96.59` |
| `Live` | `Long` | `4.84` | 2,070,000.00 USD | 0.00 USD | 308.87 USD | `-42.64%` | `63.75` |
| `Live` | `Long` | `4.91` | 2,070,000.00 USD | 0.00 USD | 20,000.00 USD | `-41.93%` | `4,076.61` |
| `Live` | `Long` | `4.92` | 2,050,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.81%` | `251.00` |
| `Live` | `Long` | `4.92` | 2,050,000.00 USD | 0.00 USD | 510.87 USD | `-41.69%` | `103.73` |
| `Live` | `Long` | `4.95` | 2,050,000.00 USD | 0.00 USD | 352.68 USD | `-41.46%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,050,000.00 USD | 0.00 USD | 945.36 USD | `-41.34%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,050,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.22%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,050,000.00 USD | 0.00 USD | 282.23 USD | `-41.10%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,050,000.00 USD | 0.00 USD | 269.53 USD | `-40.87%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,050,000.00 USD | 0.00 USD | 57,120.00 USD | `-40.63%` | `11,389.46` |
| `Live` | `Long` | `5.03` | 1,990,000.00 USD | 0.00 USD | 167.78 USD | `-40.51%` | `33.39` |
| `Live` | `Long` | `5.04` | 1,990,000.00 USD | 0.00 USD | 314.59 USD | `-40.39%` | `62.48` |
| `Live` | `Long` | `5.05` | 1,990,000.00 USD | 0.00 USD | 504.74 USD | `-40.16%` | `99.85` |
| `Live` | `Long` | `5.08` | 1,990,000.00 USD | 0.00 USD | 2,750.00 USD | `-39.92%` | `542.01` |
| `Live` | `Long` | `5.08` | 1,990,000.00 USD | 0.00 USD | 105.46 USD | `-39.80%` | `20.74` |
| `Live` | `Long` | `5.09` | 1,990,000.00 USD | 0.00 USD | 651.75 USD | `-39.68%` | `127.92` |
| `Live` | `Long` | `5.12` | 1,990,000.00 USD | 0.00 USD | 915.43 USD | `-39.45%` | `178.97` |
| `Live` | `Long` | `5.12` | 1,980,000.00 USD | 0.00 USD | 250.20 USD | `-39.33%` | `48.82` |
| `Live` | `Long` | `5.13` | 1,980,000.00 USD | 0.00 USD | 396.06 USD | `-39.21%` | `77.13` |
| `Live` | `Long` | `5.14` | 1,980,000.00 USD | 0.00 USD | 119.36 USD | `-39.09%` | `23.20` |
| `Live` | `Long` | `5.17` | 1,980,000.00 USD | 0.00 USD | 516.50 USD | `-38.85%` | `100.00` |
| `Live` | `Long` | `5.17` | 1,980,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.73%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,980,000.00 USD | 0.00 USD | 5,610.00 USD | `-38.62%` | `1,082.04` |
| `Live` | `Long` | `5.20` | 1,980,000.00 USD | 0.00 USD | 480.07 USD | `-38.50%` | `92.41` |
| `Live` | `Long` | `5.21` | 1,980,000.00 USD | 0.00 USD | 300.91 USD | `-38.26%` | `57.70` |
| `Live` | `Long` | `5.25` | 1,980,000.00 USD | 0.00 USD | 1,560.00 USD | `-37.79%` | `296.05` |
| `Live` | `Long` | `5.26` | 1,970,000.00 USD | 0.00 USD | 2,350.00 USD | `-37.67%` | `447.00` |
| `Live` | `Long` | `5.28` | 1,970,000.00 USD | 0.00 USD | 160,550.00 USD | `-37.55%` | `30,435.20` |
| `Live` | `Long` | `5.29` | 1,810,000.00 USD | 0.00 USD | 640.70 USD | `-37.43%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,810,000.00 USD | 0.00 USD | 448.69 USD | `-37.08%` | `84.42` |
| `Live` | `Long` | `5.33` | 1,810,000.00 USD | 0.00 USD | 716.11 USD | `-36.96%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,810,000.00 USD | 0.00 USD | 660.46 USD | `-36.13%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,810,000.00 USD | 0.00 USD | 20,160.00 USD | `-35.89%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,790,000.00 USD | 0.00 USD | 160,400.00 USD | `-35.78%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,630,000.00 USD | 0.00 USD | 1,360.00 USD | `-35.66%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,630,000.00 USD | 0.00 USD | 264.72 USD | `-35.30%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,630,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.18%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,620,000.00 USD | 0.00 USD | 354.06 USD | `-35.06%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,620,000.00 USD | 0.00 USD | 19,290.00 USD | `-34.95%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,610,000.00 USD | 0.00 USD | 367.41 USD | `-34.71%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,600,000.00 USD | 0.00 USD | 121.38 USD | `-34.47%` | `21.93` |
| `Live` | `Long` | `5.54` | 1,600,000.00 USD | 0.00 USD | 2,760.00 USD | `-34.35%` | `497.70` |
| `Live` | `Long` | `5.55` | 1,600,000.00 USD | 0.00 USD | 1,500.00 USD | `-34.24%` | `270.00` |
| `Live` | `Long` | `5.58` | 1,600,000.00 USD | 0.00 USD | 63,260.00 USD | `-34.00%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,540,000.00 USD | 0.00 USD | 34,430.00 USD | `-33.76%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,500,000.00 USD | 0.00 USD | 2,810.00 USD | `-33.53%` | `500.00` |
| `Live` | `Long` | `5.63` | 1,500,000.00 USD | 0.00 USD | 468.55 USD | `-33.29%` | `83.15` |
| `Live` | `Long` | `5.71` | 1,500,000.00 USD | 0.00 USD | 574.89 USD | `-32.46%` | `100.77` |
| `Live` | `Long` | `5.71` | 1,500,000.00 USD | 0.00 USD | 147.33 USD | `-32.34%` | `25.78` |
| `Live` | `Long` | `5.72` | 1,500,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.22%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,500,000.00 USD | 0.00 USD | 661.65 USD | `-32.11%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,500,000.00 USD | 0.00 USD | 125.70 USD | `-31.99%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,500,000.00 USD | 0.00 USD | 3,190.00 USD | `-31.87%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,490,000.00 USD | 0.00 USD | 11,130.00 USD | `-31.75%` | `1,931.12` |
| `Live` | `Long` | `5.78` | 1,480,000.00 USD | 0.00 USD | 801.40 USD | `-31.63%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,480,000.00 USD | 0.00 USD | 635.31 USD | `-31.39%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,480,000.00 USD | 0.00 USD | 580.50 USD | `-31.28%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,480,000.00 USD | 0.00 USD | 106.65 USD | `-31.16%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,480,000.00 USD | 0.00 USD | 145.88 USD | `-30.92%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,480,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.68%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,480,000.00 USD | 0.00 USD | 984.70 USD | `-30.21%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,480,000.00 USD | 0.00 USD | 399.18 USD | `-30.09%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,480,000.00 USD | 0.00 USD | 277.35 USD | `-29.97%` | `46.89` |
| `Live` | `Long` | `5.96` | 1,480,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.50%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,460,000.00 USD | 0.00 USD | 585.97 USD | `-29.26%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,460,000.00 USD | 0.00 USD | 341.56 USD | `-28.91%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,460,000.00 USD | 0.00 USD | 446.85 USD | `-28.79%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,460,000.00 USD | 0.00 USD | 331.68 USD | `-28.55%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,460,000.00 USD | 0.00 USD | 105.61 USD | `-28.44%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,460,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.32%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,460,000.00 USD | 0.00 USD | 265.10 USD | `-28.20%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,460,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.08%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,460,000.00 USD | 0.00 USD | 405.14 USD | `-27.96%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,460,000.00 USD | 0.00 USD | 3,130.00 USD | `-27.84%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,450,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.61%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,450,000.00 USD | 0.00 USD | 137.02 USD | `-27.49%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,450,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.37%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,450,000.00 USD | 0.00 USD | 1,670.00 USD | `-27.25%` | `272.43` |
| `Live` | `Long` | `6.16` | 1,450,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.13%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,440,000.00 USD | 0.00 USD | 104.36 USD | `-26.90%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,440,000.00 USD | 0.00 USD | 310.25 USD | `-26.54%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,440,000.00 USD | 0.00 USD | 972.65 USD | `-25.95%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,440,000.00 USD | 0.00 USD | 3,970.00 USD | `-25.71%` | `632.17` |
| `Live` | `Long` | `6.29` | 1,440,000.00 USD | 0.00 USD | 2,430.00 USD | `-25.48%` | `386.46` |
| `Live` | `Long` | `6.33` | 1,430,000.00 USD | 0.00 USD | 277.48 USD | `-25.12%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,430,000.00 USD | 0.00 USD | 4,470.00 USD | `-24.77%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,430,000.00 USD | 0.00 USD | 284,770.00 USD | `-24.65%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,140,000.00 USD | 0.00 USD | 6,410.00 USD | `-24.53%` | `1,006.23` |
| `Live` | `Long` | `6.39` | 1,140,000.00 USD | 0.00 USD | 1,440.00 USD | `-24.29%` | `225.14` |
| `Live` | `Long` | `6.42` | 1,140,000.00 USD | 0.00 USD | 306.32 USD | `-24.05%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,140,000.00 USD | 0.00 USD | 484.64 USD | `-23.94%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,140,000.00 USD | 0.00 USD | 6,780.00 USD | `-23.82%` | `1,052.89` |
| `Live` | `Long` | `6.45` | 1,130,000.00 USD | 0.00 USD | 361,300.00 USD | `-23.70%` | `56,059.40` |
| `Live` | `Long` | `6.46` | 767,880.00 USD | 0.00 USD | 1,050.00 USD | `-23.46%` | `162.75` |
| `Live` | `Long` | `6.50` | 766,830.00 USD | 0.00 USD | 257.99 USD | `-22.99%` | `39.66` |
| `Live` | `Long` | `6.51` | 766,570.00 USD | 0.00 USD | 651.50 USD | `-22.87%` | `100.00` |
| `Live` | `Long` | `6.54` | 765,920.00 USD | 0.00 USD | 852.03 USD | `-22.63%` | `130.38` |
| `Live` | `Long` | `6.54` | 765,070.00 USD | 0.00 USD | 8,970.00 USD | `-22.52%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 756,100.00 USD | 0.00 USD | 1,770.00 USD | `-22.04%` | `269.14` |
| `Live` | `Long` | `6.59` | 754,320.00 USD | 0.00 USD | 1,100.00 USD | `-21.92%` | `166.55` |
| `Live` | `Long` | `6.62` | 753,230.00 USD | 0.00 USD | 2,110.00 USD | `-21.69%` | `318.57` |
| `Live` | `Long` | `6.62` | 751,120.00 USD | 0.00 USD | 364.90 USD | `-21.57%` | `55.08` |
| `Live` | `Long` | `6.63` | 750,750.00 USD | 0.00 USD | 245.89 USD | `-21.45%` | `37.06` |
| `Live` | `Long` | `6.66` | 750,510.00 USD | 0.00 USD | 1,520.00 USD | `-21.21%` | `228.41` |
| `Live` | `Long` | `6.67` | 748,990.00 USD | 0.00 USD | 1,320.00 USD | `-20.98%` | `198.12` |
| `Live` | `Long` | `6.71` | 747,660.00 USD | 0.00 USD | 16,570.00 USD | `-20.62%` | `2,471.72` |
| `Live` | `Long` | `6.71` | 731,090.00 USD | 0.00 USD | 6,180.00 USD | `-20.50%` | `920.74` |
| `Live` | `Long` | `6.75` | 724,910.00 USD | 0.00 USD | 1,330.00 USD | `-20.15%` | `196.95` |
| `Live` | `Long` | `6.78` | 723,580.00 USD | 0.00 USD | 6,780.00 USD | `-19.79%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 716,810.00 USD | 0.00 USD | 21,580.00 USD | `-19.67%` | `3,180.66` |
| `Live` | `Long` | `6.79` | 695,220.00 USD | 0.00 USD | 4,720.00 USD | `-19.56%` | `694.73` |
| `Live` | `Long` | `6.80` | 690,500.00 USD | 0.00 USD | 1,500.00 USD | `-19.44%` | `220.95` |
| `Live` | `Long` | `6.82` | 689,000.00 USD | 0.00 USD | 7,230.00 USD | `-19.32%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 681,770.00 USD | 0.00 USD | 1,160.00 USD | `-19.20%` | `170.32` |
| `Live` | `Long` | `6.87` | 680,610.00 USD | 0.00 USD | 3,710.00 USD | `-18.73%` | `540.58` |
| `Live` | `Long` | `6.88` | 676,900.00 USD | 0.00 USD | 1,580.00 USD | `-18.49%` | `229.18` |
| `Live` | `Long` | `6.92` | 675,320.00 USD | 0.00 USD | 579.62 USD | `-18.02%` | `83.70` |
| `Live` | `Long` | `6.93` | 674,740.00 USD | 0.00 USD | 3,500.00 USD | `-17.90%` | `504.07` |
| `Live` | `Long` | `6.95` | 671,240.00 USD | 0.00 USD | 3,980.00 USD | `-17.78%` | `572.68` |
| `Live` | `Long` | `6.96` | 667,270.00 USD | 0.00 USD | 3,480.00 USD | `-17.66%` | `500.00` |
| `Live` | `Long` | `6.96` | 663,790.00 USD | 0.00 USD | 636.74 USD | `-17.54%` | `91.42` |
| `Live` | `Long` | `6.97` | 663,150.00 USD | 0.00 USD | 128,810.00 USD | `-17.43%` | `18,466.99` |
| `Live` | `Long` | `6.99` | 534,340.00 USD | 0.00 USD | 297.49 USD | `-17.31%` | `42.59` |
| `Live` | `Long` | `7.00` | 534,050.00 USD | 0.00 USD | 746.58 USD | `-17.19%` | `106.73` |
| `Live` | `Long` | `7.00` | 533,300.00 USD | 0.00 USD | 21,040.00 USD | `-17.07%` | `3,003.11` |
| `Live` | `Long` | `7.03` | 512,260.00 USD | 0.00 USD | 1,370.00 USD | `-16.83%` | `194.51` |
| `Live` | `Long` | `7.05` | 510,900.00 USD | 0.00 USD | 354.23 USD | `-16.48%` | `50.21` |
| `Live` | `Long` | `7.07` | 510,540.00 USD | 0.00 USD | 23,600.00 USD | `-16.36%` | `3,340.54` |
| `Live` | `Long` | `7.08` | 486,940.00 USD | 0.00 USD | 7,420.00 USD | `-16.24%` | `1,048.27` |
| `Live` | `Long` | `7.08` | 479,530.00 USD | 0.00 USD | 1,050.00 USD | `-16.12%` | `148.63` |
| `Live` | `Long` | `7.09` | 478,470.00 USD | 0.00 USD | 2,130.00 USD | `-16.00%` | `300.00` |
| `Live` | `Long` | `7.11` | 476,340.00 USD | 0.00 USD | 28,530.00 USD | `-15.89%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 447,810.00 USD | 0.00 USD | 379.66 USD | `-15.77%` | `53.36` |
| `Live` | `Long` | `7.13` | 447,430.00 USD | 0.00 USD | 777.50 USD | `-15.53%` | `108.97` |
| `Live` | `Long` | `7.14` | 446,660.00 USD | 0.00 USD | 20,270.00 USD | `-15.41%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 426,390.00 USD | 0.00 USD | 2,380.00 USD | `-15.06%` | `331.12` |
| `Live` | `Long` | `7.18` | 424,010.00 USD | 0.00 USD | 31,630.00 USD | `-14.94%` | `4,401.89` |
| `Live` | `Long` | `7.21` | 392,380.00 USD | 0.00 USD | 322.94 USD | `-14.58%` | `44.76` |
| `Live` | `Long` | `7.22` | 392,060.00 USD | 0.00 USD | 1,450.00 USD | `-14.47%` | `200.00` |
| `Live` | `Long` | `7.24` | 390,620.00 USD | 0.00 USD | 1,480.00 USD | `-14.35%` | `205.21` |
| `Live` | `Long` | `7.25` | 389,130.00 USD | 0.00 USD | 185.83 USD | `-14.23%` | `25.65` |
| `Live` | `Long` | `7.25` | 388,950.00 USD | 0.00 USD | 21,280.00 USD | `-14.11%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 367,670.00 USD | 0.00 USD | 36,420.00 USD | `-13.76%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 331,240.00 USD | 0.00 USD | 1,680.00 USD | `-13.64%` | `230.97` |
| `Live` | `Long` | `7.33` | 329,560.00 USD | 0.00 USD | 1,350.00 USD | `-13.16%` | `183.96` |
| `Live` | `Long` | `7.34` | 328,210.00 USD | 0.00 USD | 17,490.00 USD | `-13.05%` | `2,381.89` |
| `Live` | `Long` | `7.37` | 310,710.00 USD | 0.00 USD | 2,940.00 USD | `-12.81%` | `399.15` |
| `Live` | `Long` | `7.38` | 307,770.00 USD | 0.00 USD | 1,100.00 USD | `-12.69%` | `148.75` |
| `Live` | `Long` | `7.38` | 306,670.00 USD | 0.00 USD | 1,260.00 USD | `-12.57%` | `170.87` |
| `Live` | `Long` | `7.42` | 305,410.00 USD | 0.00 USD | 147.61 USD | `-12.10%` | `19.88` |
| `Live` | `Long` | `7.43` | 305,260.00 USD | 0.00 USD | 2,430.00 USD | `-11.98%` | `327.05` |
| `Live` | `Long` | `7.45` | 302,830.00 USD | 0.00 USD | 210.99 USD | `-11.86%` | `28.34` |
| `Live` | `Long` | `7.46` | 302,620.00 USD | 0.00 USD | 10,390.00 USD | `-11.74%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 292,230.00 USD | 0.00 USD | 4,590.00 USD | `-11.62%` | `614.36` |
| `Live` | `Long` | `7.47` | 287,650.00 USD | 0.00 USD | 1,120.00 USD | `-11.51%` | `149.52` |
| `Live` | `Long` | `7.50` | 286,530.00 USD | 0.00 USD | 962.81 USD | `-11.27%` | `128.46` |
| `Live` | `Long` | `7.50` | 285,570.00 USD | 0.00 USD | 421.78 USD | `-11.15%` | `56.20` |
| `Live` | `Long` | `7.51` | 285,140.00 USD | 0.00 USD | 1,710.00 USD | `-11.03%` | `228.21` |
| `Live` | `Long` | `7.53` | 283,430.00 USD | 0.00 USD | 1,570.00 USD | `-10.91%` | `208.52` |
| `Live` | `Long` | `7.54` | 281,860.00 USD | 0.00 USD | 4,210.00 USD | `-10.80%` | `559.01` |
| `Live` | `Long` | `7.55` | 277,650.00 USD | 0.00 USD | 415.52 USD | `-10.56%` | `55.00` |
| `Live` | `Long` | `7.57` | 277,230.00 USD | 0.00 USD | 26,570.00 USD | `-10.44%` | `3,512.23` |
| `Live` | `Long` | `7.58` | 250,660.00 USD | 0.00 USD | 118.25 USD | `-10.32%` | `15.61` |
| `Live` | `Long` | `7.59` | 250,540.00 USD | 0.00 USD | 24,760.00 USD | `-10.09%` | `3,260.14` |
| `Live` | `Long` | `7.61` | 225,780.00 USD | 0.00 USD | 1,140.00 USD | `-9.97%` | `149.34` |
| `Live` | `Long` | `7.62` | 224,650.00 USD | 0.00 USD | 754.04 USD | `-9.85%` | `99.02` |
| `Live` | `Long` | `7.62` | 223,890.00 USD | 0.00 USD | 787.51 USD | `-9.73%` | `103.28` |
| `Live` | `Long` | `7.63` | 223,110.00 USD | 0.00 USD | 378.93 USD | `-9.61%` | `49.63` |
| `Live` | `Long` | `7.66` | 222,730.00 USD | 0.00 USD | 135.42 USD | `-9.38%` | `17.69` |
| `Live` | `Long` | `7.67` | 222,590.00 USD | 0.00 USD | 6,110.00 USD | `-9.26%` | `797.08` |
| `Live` | `Long` | `7.67` | 216,480.00 USD | 0.00 USD | 4,480.00 USD | `-9.14%` | `583.63` |
| `Live` | `Long` | `7.68` | 212,000.00 USD | 0.00 USD | 739.30 USD | `-9.02%` | `96.20` |
| `Live` | `Long` | `7.70` | 211,260.00 USD | 0.00 USD | 6,690.00 USD | `-8.90%` | `869.22` |
| `Live` | `Long` | `7.75` | 204,580.00 USD | 0.00 USD | 500.12 USD | `-8.19%` | `64.49` |
| `Live` | `Long` | `7.76` | 204,080.00 USD | 0.00 USD | 455.73 USD | `-8.07%` | `58.69` |
| `Live` | `Long` | `7.78` | 203,620.00 USD | 0.00 USD | 8,670.00 USD | `-7.95%` | `1,115.74` |
| `Live` | `Long` | `7.79` | 194,940.00 USD | 0.00 USD | 2,470.00 USD | `-7.84%` | `317.11` |
| `Live` | `Long` | `7.79` | 192,480.00 USD | 0.00 USD | 4,480.00 USD | `-7.72%` | `574.50` |
| `Live` | `Long` | `7.80` | 188,000.00 USD | 0.00 USD | 6,380.00 USD | `-7.60%` | `817.06` |
| `Live` | `Long` | `7.83` | 181,620.00 USD | 0.00 USD | 2,270.00 USD | `-7.36%` | `290.31` |
| `Live` | `Long` | `7.84` | 179,350.00 USD | 0.00 USD | 22,560.00 USD | `-7.13%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 156,790.00 USD | 0.00 USD | 233.83 USD | `-6.89%` | `29.73` |
| `Live` | `Long` | `7.88` | 156,550.00 USD | 0.00 USD | 1,310.00 USD | `-6.77%` | `166.93` |
| `Live` | `Long` | `7.89` | 155,240.00 USD | 0.00 USD | 1,430.00 USD | `-6.53%` | `180.69` |
| `Live` | `Long` | `7.91` | 153,810.00 USD | 0.00 USD | 2,360.00 USD | `-6.42%` | `298.43` |
| `Live` | `Long` | `7.92` | 151,450.00 USD | 0.00 USD | 4,600.00 USD | `-6.18%` | `580.78` |
| `Live` | `Long` | `7.93` | 146,850.00 USD | 0.00 USD | 16,340.00 USD | `-6.06%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 130,510.00 USD | 0.00 USD | 127,110.00 USD | `-5.94%` | `15,999.24` |
| `Live` | `Long` | `7.97` | 3,390.00 USD | 0.00 USD | 1,580.00 USD | `-5.59%` | `198.26` |
| `Live` | `Long` | `7.99` | 1,810.00 USD | 0.00 USD | 1,600.00 USD | `-5.47%` | `200.68` |
| `Live` | `Long` | `8.00` | 210.99 USD | 0.00 USD | 210.99 USD | `-5.35%` | `26.39` |
| `Live` | `Short` | `8.52` | 1,480.00 USD | 1,480.00 USD | 0.00 USD | `+0.81%` | `173.74` |
| `Live` | `Short` | `8.55` | 4,700.00 USD | 3,220.00 USD | 0.00 USD | `+1.28%` | `376.02` |
| `Live` | `Short` | `8.69` | 4,910.00 USD | 209.31 USD | 0.00 USD | `+2.82%` | `24.10` |
| `Live` | `Short` | `8.72` | 5,050.00 USD | 145.62 USD | 0.00 USD | `+3.29%` | `16.69` |
| `Live` | `Short` | `8.79` | 5,470.00 USD | 423.22 USD | 0.00 USD | `+4.12%` | `48.12` |
| `Live` | `Short` | `8.82` | 11,480.00 USD | 6,000.00 USD | 0.00 USD | `+4.48%` | `680.16` |
| `Live` | `Short` | `8.91` | 15,690.00 USD | 4,210.00 USD | 0.00 USD | `+5.54%` | `472.28` |
| `Live` | `Short` | `9.19` | 17,280.00 USD | 1,590.00 USD | 0.00 USD | `+8.74%` | `173.30` |
| `Live` | `Short` | `9.21` | 19,150.00 USD | 1,870.00 USD | 0.00 USD | `+9.09%` | `202.76` |
| `Live` | `Short` | `9.30` | 437,880.00 USD | 418,730.00 USD | 0.00 USD | `+10.16%` | `45,000.94` |
| `Live` | `Short` | `9.38` | 438,010.00 USD | 128.44 USD | 0.00 USD | `+10.99%` | `13.70` |
| `Live` | `Short` | `9.41` | 438,450.00 USD | 440.06 USD | 0.00 USD | `+11.46%` | `46.74` |
| `Live` | `Short` | `9.46` | 438,590.00 USD | 138.85 USD | 0.00 USD | `+12.05%` | `14.67` |
| `Live` | `Short` | `9.62` | 438,730.00 USD | 138.98 USD | 0.00 USD | `+13.95%` | `14.44` |
| `Live` | `Short` | `9.64` | 440,660.00 USD | 1,930.00 USD | 0.00 USD | `+14.18%` | `200.61` |
| `Live` | `Short` | `9.73` | 440,860.00 USD | 192.95 USD | 0.00 USD | `+15.25%` | `19.82` |
| `Live` | `Short` | `10.35` | 443,510.00 USD | 2,650.00 USD | 0.00 USD | `+22.47%` | `256.58` |
| `Live` | `Short` | `10.38` | 547,360.00 USD | 103,850.00 USD | 0.00 USD | `+22.94%` | `10,000.00` |
| `Live` | `Short` | `10.56` | 547,880.00 USD | 523.81 USD | 0.00 USD | `+25.08%` | `49.58` |
| `Live` | `Short` | `10.71` | 548,140.00 USD | 256.49 USD | 0.00 USD | `+26.73%` | `23.96` |
| `Live` | `Short` | `10.74` | 548,440.00 USD | 302.47 USD | 0.00 USD | `+27.21%` | `28.15` |
| `Live` | `Short` | `10.89` | 548,540.00 USD | 100.13 USD | 0.00 USD | `+28.98%` | `9.19` |
| `Live` | `Short` | `11.01` | 555,510.00 USD | 6,970.00 USD | 0.00 USD | `+30.28%` | `633.00` |
| `Live` | `Short` | `11.02` | 610,580.00 USD | 55,080.00 USD | 0.00 USD | `+30.40%` | `5,000.00` |
| `Live` | `Short` | `11.27` | 622,250.00 USD | 11,670.00 USD | 0.00 USD | `+33.36%` | `1,035.87` |
| `Live` | `Short` | `11.62` | 634,390.00 USD | 12,140.00 USD | 0.00 USD | `+37.62%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 931,150.00 USD | 296,760.00 USD | 0.00 USD | `+38.33%` | `25,397.02` |
| `Live` | `Short` | `11.80` | 931,270.00 USD | 114.27 USD | 0.00 USD | `+39.76%` | `9.68` |
| `Live` | `Short` | `11.93` | 931,770.00 USD | 505.74 USD | 0.00 USD | `+41.18%` | `42.41` |
| `Live` | `Short` | `11.95` | 932,820.00 USD | 1,050.00 USD | 0.00 USD | `+41.41%` | `87.54` |
| `Live` | `Short` | `12.30` | 934,550.00 USD | 1,730.00 USD | 0.00 USD | `+45.67%` | `140.71` |
| `Live` | `Short` | `12.40` | 934,890.00 USD | 343.62 USD | 0.00 USD | `+46.86%` | `27.70` |
| `Live` | `Short` | `13.10` | 939,820.00 USD | 4,930.00 USD | 0.00 USD | `+55.03%` | `376.48` |
| `Live` | `Short` | `13.20` | 1,030,000.00 USD | 87,940.00 USD | 0.00 USD | `+56.21%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,030,000.00 USD | 3,810.00 USD | 0.00 USD | `+57.40%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,030,000.00 USD | 430.34 USD | 0.00 USD | `+59.41%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,030,000.00 USD | 172.29 USD | 0.00 USD | `+62.01%` | `12.59` |
| `Live` | `Short` | `13.74` | 1,090,000.00 USD | 62,610.00 USD | 0.00 USD | `+62.72%` | `4,555.14` |
| `Live` | `Short` | `14.23` | 1,100,000.00 USD | 280.86 USD | 0.00 USD | `+68.52%` | `19.73` |
| `Live` | `Short` | `14.66` | 1,100,000.00 USD | 823.29 USD | 0.00 USD | `+73.61%` | `56.14` |
| `Live` | `Short` | `14.70` | 1,100,000.00 USD | 527.40 USD | 0.00 USD | `+73.97%` | `35.89` |
| `Live` | `Short` | `15.13` | 1,100,000.00 USD | 4,200.00 USD | 0.00 USD | `+79.18%` | `277.54` |
| `Live` | `Short` | `15.20` | 1,100,000.00 USD | 249.35 USD | 0.00 USD | `+79.89%` | `16.41` |
| `Live` | `Short` | `15.29` | 1,100,000.00 USD | 229.43 USD | 0.00 USD | `+81.07%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,100,000.00 USD | 230.17 USD | 0.00 USD | `+81.66%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,120,000.00 USD | 20,000.00 USD | 0.00 USD | `+82.14%` | `1,300.00` |
| `Live` | `Short` | `15.52` | 1,120,000.00 USD | 334.35 USD | 0.00 USD | `+83.68%` | `21.55` |
| `Live` | `Short` | `15.72` | 1,120,000.00 USD | 167.79 USD | 0.00 USD | `+86.16%` | `10.67` |
| `Live` | `Short` | `15.77` | 1,120,000.00 USD | 185.55 USD | 0.00 USD | `+86.64%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,120,000.00 USD | 1,700.00 USD | 0.00 USD | `+87.35%` | `107.48` |
| `Live` | `Short` | `16.38` | 1,390,000.00 USD | 265,410.00 USD | 0.00 USD | `+93.86%` | `16,208.00` |
| `Live` | `Short` | `16.43` | 1,410,000.00 USD | 23,250.00 USD | 0.00 USD | `+94.57%` | `1,414.55` |
| `Live` | `Short` | `16.52` | 1,410,000.00 USD | 190.91 USD | 0.00 USD | `+95.52%` | `11.56` |
| `Live` | `Short` | `16.61` | 1,440,000.00 USD | 24,250.00 USD | 0.00 USD | `+96.70%` | `1,459.25` |
| `Live` | `Short` | `16.64` | 1,440,000.00 USD | 118.35 USD | 0.00 USD | `+97.05%` | `7.11` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 358,250.00 USD | 0.00 USD | 611.73 USD | `-72.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 357,630.00 USD | 0.00 USD | 793.75 USD | `-52.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 356,840.00 USD | 0.00 USD | 105.04 USD | `-46.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 356,740.00 USD | 0.00 USD | 67,970.00 USD | `-40.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 288,770.00 USD | 0.00 USD | 205.30 USD | `-37.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 288,560.00 USD | 0.00 USD | 465.42 USD | `-35.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 288,100.00 USD | 0.00 USD | 349.35 USD | `-34.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 287,750.00 USD | 0.00 USD | 1,020.00 USD | `-34.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 286,730.00 USD | 0.00 USD | 1,330.00 USD | `-31.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 285,400.00 USD | 0.00 USD | 493.50 USD | `-29.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 284,910.00 USD | 0.00 USD | 100.98 USD | `-29.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 284,810.00 USD | 0.00 USD | 500.70 USD | `-28.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 284,310.00 USD | 0.00 USD | 4,160.00 USD | `-27.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 280,150.00 USD | 0.00 USD | 6,500.00 USD | `-26.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 273,650.00 USD | 0.00 USD | 906.18 USD | `-26.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 272,750.00 USD | 0.00 USD | 127.35 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 272,620.00 USD | 0.00 USD | 864.38 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 271,750.00 USD | 0.00 USD | 130.10 USD | `-22.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 271,620.00 USD | 0.00 USD | 4,340.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 267,280.00 USD | 0.00 USD | 5,520.00 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 261,760.00 USD | 0.00 USD | 100.72 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 261,660.00 USD | 0.00 USD | 296.34 USD | `-20.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 261,360.00 USD | 0.00 USD | 921.19 USD | `-19.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 260,440.00 USD | 0.00 USD | 709.98 USD | `-18.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 259,730.00 USD | 0.00 USD | 1,380.00 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 258,350.00 USD | 0.00 USD | 262.44 USD | `-17.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 258,090.00 USD | 0.00 USD | 24,350.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 233,730.00 USD | 0.00 USD | 187.79 USD | `-15.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 233,550.00 USD | 0.00 USD | 6,790.00 USD | `-15.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 226,760.00 USD | 0.00 USD | 9,770.00 USD | `-15.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 216,990.00 USD | 0.00 USD | 7,210.00 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 209,790.00 USD | 0.00 USD | 282.74 USD | `-14.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 209,500.00 USD | 0.00 USD | 603.44 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,900.00 USD | 0.00 USD | 464.61 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 208,430.00 USD | 0.00 USD | 2,090.00 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 206,340.00 USD | 0.00 USD | 129.58 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 206,210.00 USD | 0.00 USD | 114.65 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 206,100.00 USD | 0.00 USD | 702.75 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 205,390.00 USD | 0.00 USD | 4,630.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 200,760.00 USD | 0.00 USD | 199.39 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 200,560.00 USD | 0.00 USD | 6,270.00 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 194,300.00 USD | 0.00 USD | 37,420.00 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 156,870.00 USD | 0.00 USD | 2,120.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 154,750.00 USD | 0.00 USD | 799.83 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 153,950.00 USD | 0.00 USD | 820.44 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 153,130.00 USD | 0.00 USD | 103.41 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 153,030.00 USD | 0.00 USD | 218.24 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 152,810.00 USD | 0.00 USD | 113.78 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 152,690.00 USD | 0.00 USD | 152.10 USD | `-9.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 152,540.00 USD | 0.00 USD | 297.59 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 152,240.00 USD | 0.00 USD | 528.88 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 151,720.00 USD | 0.00 USD | 360.13 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 151,360.00 USD | 0.00 USD | 578.04 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 150,780.00 USD | 0.00 USD | 424.05 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 150,350.00 USD | 0.00 USD | 23,790.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 126,570.00 USD | 0.00 USD | 3,940.00 USD | `-7.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 122,630.00 USD | 0.00 USD | 115.23 USD | `-7.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 122,510.00 USD | 0.00 USD | 183.33 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 122,330.00 USD | 0.00 USD | 1,890.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 120,440.00 USD | 0.00 USD | 6,520.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 113,920.00 USD | 0.00 USD | 5,710.00 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 108,210.00 USD | 0.00 USD | 1,590.00 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 106,630.00 USD | 0.00 USD | 898.42 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 105,730.00 USD | 0.00 USD | 7,960.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 97,770.00 USD | 0.00 USD | 9,160.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 88,610.00 USD | 0.00 USD | 3,430.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 85,180.00 USD | 0.00 USD | 123.58 USD | `-4.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 85,050.00 USD | 0.00 USD | 2,110.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 82,950.00 USD | 0.00 USD | 152.56 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 82,790.00 USD | 0.00 USD | 2,730.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 80,060.00 USD | 0.00 USD | 121.69 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 79,940.00 USD | 0.00 USD | 5,230.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 74,710.00 USD | 0.00 USD | 477.36 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 74,230.00 USD | 0.00 USD | 924.78 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 73,310.00 USD | 0.00 USD | 744.88 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 72,560.00 USD | 0.00 USD | 6,500.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 66,060.00 USD | 0.00 USD | 884.60 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 65,180.00 USD | 0.00 USD | 5,550.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 59,620.00 USD | 0.00 USD | 1,430.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 58,190.00 USD | 0.00 USD | 3,080.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 55,110.00 USD | 0.00 USD | 520.75 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 54,590.00 USD | 0.00 USD | 3,020.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 51,560.00 USD | 0.00 USD | 141.04 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 51,420.00 USD | 0.00 USD | 22,560.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 28,860.00 USD | 0.00 USD | 515.66 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 28,340.00 USD | 0.00 USD | 1,030.00 USD | `-2.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 27,320.00 USD | 0.00 USD | 197.96 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 27,120.00 USD | 0.00 USD | 9,110.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 18,000.00 USD | 0.00 USD | 397.71 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 17,610.00 USD | 0.00 USD | 408.78 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 17,200.00 USD | 0.00 USD | 201.49 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 17,000.00 USD | 0.00 USD | 4,150.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 12,850.00 USD | 0.00 USD | 242.42 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 12,610.00 USD | 0.00 USD | 2,920.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 9,690.00 USD | 0.00 USD | 1,690.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 8,000.00 USD | 0.00 USD | 408.58 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 7,590.00 USD | 0.00 USD | 756.06 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 6,830.00 USD | 0.00 USD | 970.35 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 5,860.00 USD | 0.00 USD | 503.59 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 5,360.00 USD | 0.00 USD | 419.25 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 4,940.00 USD | 0.00 USD | 1,970.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 2,970.00 USD | 0.00 USD | 328.55 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 2,640.00 USD | 0.00 USD | 314.81 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 2,330.00 USD | 0.00 USD | 1,880.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 445.78 USD | 0.00 USD | 307.54 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 138.24 USD | 0.00 USD | 138.24 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 710.81 USD | 710.81 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 1,480.00 USD | 769.61 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 1,630.00 USD | 146.79 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 2,040.00 USD | 408.78 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 19,050.00 USD | 17,010.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 19,450.00 USD | 408.55 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 20,580.00 USD | 1,130.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 20,870.00 USD | 290.10 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 25,280.00 USD | 4,400.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 25,520.00 USD | 243.82 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 27,120.00 USD | 1,600.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 28,540.00 USD | 1,420.00 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 29,670.00 USD | 1,130.00 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 30,420.00 USD | 751.56 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 31,920.00 USD | 1,490.00 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 36,200.00 USD | 4,290.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 36,410.00 USD | 201.97 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 36,510.00 USD | 103.31 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 36,620.00 USD | 107.84 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 36,730.00 USD | 107.97 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 36,900.00 USD | 176.62 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 37,890.00 USD | 990.09 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 42,900.00 USD | 5,010.00 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 43,480.00 USD | 575.14 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 43,880.00 USD | 399.67 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 44,700.00 USD | 819.28 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 45,030.00 USD | 333.07 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 49,400.00 USD | 4,370.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 51,180.00 USD | 1,780.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 90,990.00 USD | 39,810.00 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 91,200.00 USD | 215.16 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 91,590.00 USD | 388.12 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 92,300.00 USD | 711.78 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 92,870.00 USD | 563.87 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 94,900.00 USD | 2,030.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 95,140.00 USD | 243.40 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 100,910.00 USD | 5,760.00 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 101,140.00 USD | 234.04 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 101,310.00 USD | 163.91 USD | 0.00 USD | `+4.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 101,420.00 USD | 110.58 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 102,520.00 USD | 1,100.00 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 104,450.00 USD | 1,930.00 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 105,240.00 USD | 788.72 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 107,050.00 USD | 1,800.00 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 107,210.00 USD | 163.33 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 136,730.00 USD | 29,520.00 USD | 0.00 USD | `+5.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 136,960.00 USD | 223.62 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 137,140.00 USD | 180.53 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 137,540.00 USD | 401.63 USD | 0.00 USD | `+6.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 452,690.00 USD | 315,150.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 452,800.00 USD | 104.59 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 453,060.00 USD | 262.56 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 453,190.00 USD | 130.03 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 454,570.00 USD | 1,380.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 455,650.00 USD | 1,090.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 456,270.00 USD | 616.37 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 456,370.00 USD | 102.03 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 456,820.00 USD | 453.84 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 456,990.00 USD | 160.99 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 457,400.00 USD | 415.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 458,910.00 USD | 1,510.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 459,520.00 USD | 606.18 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 732,680.00 USD | 273,160.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 737,230.00 USD | 4,560.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 737,400.00 USD | 166.53 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 739,400.00 USD | 2,000.00 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,130,000.00 USD | 394,210.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,130,000.00 USD | 119.24 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,140,000.00 USD | 2,660.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,140,000.00 USD | 131.87 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,140,000.00 USD | 149.17 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,140,000.00 USD | 2,220.00 USD | 0.00 USD | `+9.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,370,000.00 USD | 231,380.00 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,370,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,370,000.00 USD | 434.45 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,390,000.00 USD | 18,610.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,390,000.00 USD | 166.83 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,390,000.00 USD | 150.79 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,390,000.00 USD | 101.58 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,390,000.00 USD | 109.36 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,390,000.00 USD | 116.69 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,390,000.00 USD | 163.41 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,390,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,390,000.00 USD | 660.84 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,390,000.00 USD | 714.59 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,400,000.00 USD | 928.13 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,400,000.00 USD | 102.45 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,400,000.00 USD | 219.84 USD | 0.00 USD | `+11.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,400,000.00 USD | 1,890.00 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,400,000.00 USD | 1,130.00 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,400,000.00 USD | 288.46 USD | 0.00 USD | `+12.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,400,000.00 USD | 119.92 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,400,000.00 USD | 231.00 USD | 0.00 USD | `+13.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,400,000.00 USD | 221.07 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,400,000.00 USD | 992.00 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,400,000.00 USD | 148.48 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,400,000.00 USD | 191.36 USD | 0.00 USD | `+14.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,410,000.00 USD | 4,440.00 USD | 0.00 USD | `+14.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,410,000.00 USD | 108.21 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,410,000.00 USD | 169.68 USD | 0.00 USD | `+15.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,410,000.00 USD | 574.66 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,410,000.00 USD | 121.87 USD | 0.00 USD | `+15.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,410,000.00 USD | 115.88 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,410,000.00 USD | 340.05 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,410,000.00 USD | 742.12 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,410,000.00 USD | 899.47 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,480,000.00 USD | 70,020.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,480,000.00 USD | 373.97 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,480,000.00 USD | 5,050.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,490,000.00 USD | 6,370.00 USD | 0.00 USD | `+19.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,490,000.00 USD | 404.20 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,700,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,700,000.00 USD | 1,150.00 USD | 0.00 USD | `+19.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,700,000.00 USD | 172.16 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,700,000.00 USD | 922.87 USD | 0.00 USD | `+21.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,700,000.00 USD | 489.40 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,710,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,710,000.00 USD | 118.01 USD | 0.00 USD | `+23.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,710,000.00 USD | 818.31 USD | 0.00 USD | `+24.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,710,000.00 USD | 312.31 USD | 0.00 USD | `+24.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,710,000.00 USD | 2,290.00 USD | 0.00 USD | `+24.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,710,000.00 USD | 178.46 USD | 0.00 USD | `+25.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,710,000.00 USD | 173.42 USD | 0.00 USD | `+26.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,710,000.00 USD | 184.75 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,710,000.00 USD | 135.78 USD | 0.00 USD | `+27.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,710,000.00 USD | 127.96 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,710,000.00 USD | 476.43 USD | 0.00 USD | `+28.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,710,000.00 USD | 869.35 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,710,000.00 USD | 118.97 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,710,000.00 USD | 251.06 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,710,000.00 USD | 552.44 USD | 0.00 USD | `+29.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,710,000.00 USD | 537.26 USD | 0.00 USD | `+30.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,710,000.00 USD | 320.29 USD | 0.00 USD | `+31.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,710,000.00 USD | 1,100.00 USD | 0.00 USD | `+32.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,720,000.00 USD | 2,270.00 USD | 0.00 USD | `+32.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,720,000.00 USD | 1,270.00 USD | 0.00 USD | `+33.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,720,000.00 USD | 1,380.00 USD | 0.00 USD | `+34.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,720,000.00 USD | 2,410.00 USD | 0.00 USD | `+35.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,730,000.00 USD | 9,520.00 USD | 0.00 USD | `+35.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,730,000.00 USD | 2,050.00 USD | 0.00 USD | `+35.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,730,000.00 USD | 529.11 USD | 0.00 USD | `+36.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,740,000.00 USD | 7,700.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,740,000.00 USD | 906.03 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,740,000.00 USD | 434.61 USD | 0.00 USD | `+40.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,740,000.00 USD | 163.52 USD | 0.00 USD | `+40.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,750,000.00 USD | 10,370.00 USD | 0.00 USD | `+42.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,760,000.00 USD | 5,270.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,760,000.00 USD | 115.02 USD | 0.00 USD | `+45.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,760,000.00 USD | 3,350.00 USD | 0.00 USD | `+50.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,760,000.00 USD | 197.97 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,770,000.00 USD | 3,200.00 USD | 0.00 USD | `+52.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,770,000.00 USD | 179.58 USD | 0.00 USD | `+53.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,770,000.00 USD | 568.45 USD | 0.00 USD | `+53.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,770,000.00 USD | 169.57 USD | 0.00 USD | `+55.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,770,000.00 USD | 446.52 USD | 0.00 USD | `+58.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,770,000.00 USD | 5,320.00 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 1,980,000.00 USD | 210,750.00 USD | 0.00 USD | `+59.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 1,980,000.00 USD | 407.95 USD | 0.00 USD | `+62.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 1,980,000.00 USD | 174.91 USD | 0.00 USD | `+63.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 1,990,000.00 USD | 4,650.00 USD | 0.00 USD | `+65.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 1,990,000.00 USD | 960.26 USD | 0.00 USD | `+68.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 1,990,000.00 USD | 2,710.00 USD | 0.00 USD | `+69.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 1,990,000.00 USD | 805.90 USD | 0.00 USD | `+71.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 1,990,000.00 USD | 655.55 USD | 0.00 USD | `+74.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,000,000.00 USD | 4,890.00 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,000,000.00 USD | 471.09 USD | 0.00 USD | `+76.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,000,000.00 USD | 383.85 USD | 0.00 USD | `+77.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,650,000.00 USD | 653,420.00 USD | 0.00 USD | `+77.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,660,000.00 USD | 3,010.00 USD | 0.00 USD | `+78.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,660,000.00 USD | 111.87 USD | 0.00 USD | `+87.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,660,000.00 USD | 219.91 USD | 0.00 USD | `+89.48%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.36` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD |
| `7D` | `7.40` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 6,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.42` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 48.44 USD |
| `1D` | `7.44` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 196.00 USD | 0.00 USD | 18,000.00 USD |
| `7D` | `7.44` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `7.46` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 7,860.00 USD | 0.00 USD | 52,720.00 USD |
| `7D` | `7.46` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 0.00 USD | 1,410.00 USD | 24,000.00 USD |
| `1D` | `7.48` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 11,780.00 USD |
| `7D` | `7.48` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 9,120.00 USD | 0.00 USD | 20,570.00 USD |
| `1D` | `7.50` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 717.40 USD | 4,920.00 USD | 24,120.00 USD |
| `1D` | `7.52` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 26,110.00 USD | 9,580.00 USD | 36,310.00 USD |
| `7D` | `7.52` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,150.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD |
| `1D` | `7.56` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 15,020.00 USD | 4,270.00 USD | 3,020.00 USD |
| `7D` | `7.56` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 19,530.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.58` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.02 USD |
| `1D` | `7.60` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 405.20 USD | 3,770.00 USD | 194.10 USD |
| `1D` | `7.62` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 583.80 USD | 0.00 USD | 11,670.00 USD |
| `1D` | `7.64` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 17,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.64` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 812.40 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.66` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 9,430.00 USD |
| `7D` | `7.66` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 23,280.00 USD |
| `7D` | `7.68` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD |
| `1D` | `7.70` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 321.75 USD | 2,390.00 USD | 14,120.00 USD |
| `1D` | `7.72` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 4,600.00 USD | 1,630.00 USD | 12,390.00 USD |
| `7D` | `7.72` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD |
| `1D` | `7.74` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 3,340.00 USD | 4,580.00 USD | 2,590.00 USD |
| `7D` | `7.74` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.76` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 1,660.00 USD | 1,100.00 USD | 5,380.00 USD |
| `7D` | `7.76` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `1D` | `7.78` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 44,950.00 USD | 3,730.00 USD | 8,950.00 USD |
| `7D` | `7.78` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,580.00 USD |
| `1D` | `7.80` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 39,070.00 USD | 10,860.00 USD | 8,320.00 USD |
| `7D` | `7.80` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 14,770.00 USD | 12,980.00 USD | 0.00 USD |
| `1D` | `7.82` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD |
| `7D` | `7.82` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,330.00 USD |
| `1D` | `7.84` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,680.00 USD | 4,910.00 USD | 12,620.00 USD |
| `7D` | `7.84` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 30,950.00 USD | 2,380.00 USD | 25,490.00 USD |
| `1D` | `7.86` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 15,790.00 USD | 1,680.00 USD | 16,520.00 USD |
| `7D` | `7.86` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.88` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 46,100.00 USD | 9,570.00 USD | 22,860.00 USD |
| `7D` | `7.88` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,720.00 USD |
| `1D` | `7.90` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 14,350.00 USD | 7,630.00 USD | 7,820.00 USD |
| `7D` | `7.90` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 17,500.00 USD |
| `1D` | `7.92` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 24,660.00 USD | 2,950.00 USD | 6,190.00 USD |
| `7D` | `7.92` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 55,490.00 USD | 8,420.00 USD | 15,500.00 USD |
| `1D` | `7.94` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 20,330.00 USD | 6,860.00 USD | 48,360.00 USD |
| `7D` | `7.94` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,780.00 USD |
| `1D` | `7.96` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 20,670.00 USD | 11,220.00 USD | 149,000.00 USD |
| `7D` | `7.96` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 21,840.00 USD | 6,920.00 USD | 86,150.00 USD |
| `1D` | `7.98` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 17,030.00 USD | 3,300.00 USD | 37,760.00 USD |
| `7D` | `7.98` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 56,660.00 USD | 26,790.00 USD | 146,520.00 USD |
| `1D` | `8.00` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,500.00 USD | 22,850.00 USD | 62,450.00 USD |
| `7D` | `8.00` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,470.00 USD |
| `1D` | `8.02` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 81,330.00 USD | 10,580.00 USD | 82,920.00 USD |
| `7D` | `8.02` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 20,910.00 USD | 46,670.00 USD | 56,400.00 USD |
| `1D` | `8.04` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 33,700.00 USD | 17,810.00 USD | 15,050.00 USD |
| `7D` | `8.04` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 152,340.00 USD | 56,910.00 USD | 86,510.00 USD |
| `1D` | `8.06` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 76,840.00 USD | 22,300.00 USD | 19,110.00 USD |
| `7D` | `8.06` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 122,100.00 USD | 20,850.00 USD | 86,210.00 USD |
| `1D` | `8.08` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 36,720.00 USD | 6,070.00 USD | 13,010.00 USD |
| `7D` | `8.08` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD |
| `1D` | `8.10` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 30,110.00 USD | 14,390.00 USD | 96,600.00 USD |
| `7D` | `8.10` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 61,500.00 USD | 19,700.00 USD | 15,580.00 USD |
| `1D` | `8.12` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 110,990.00 USD | 12,270.00 USD | 319,110.00 USD |
| `7D` | `8.12` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 27,520.00 USD | 10,810.00 USD | 142,650.00 USD |
| `1D` | `8.14` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 12,410.00 USD | 0.00 USD | 58,600.00 USD |
| `7D` | `8.14` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 72,460.00 USD | 25,370.00 USD | 192,000.00 USD |
| `1D` | `8.16` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 44,830.00 USD | 42,030.00 USD | 159,250.00 USD |
| `7D` | `8.16` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 38,430.00 USD | 5,510.00 USD | 30,350.00 USD |
| `1D` | `8.18` | 864,670.00 USD | 0.00 USD | 864,670.00 USD | 133,120.00 USD | 19,620.00 USD | 175,960.00 USD |
| `7D` | `8.18` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 39,830.00 USD | 43,260.00 USD | 176,600.00 USD |
| `1D` | `8.20` | 535,970.00 USD | 0.00 USD | 535,970.00 USD | 33,560.00 USD | 32,530.00 USD | 17,200.00 USD |
| `7D` | `8.20` | 817,140.00 USD | 0.00 USD | 817,140.00 USD | 92,320.00 USD | 58,100.00 USD | 8,420.00 USD |
| `1D` | `8.22` | 452,680.00 USD | 0.00 USD | 452,680.00 USD | 32,330.00 USD | 39,650.00 USD | 35,310.00 USD |
| `7D` | `8.22` | 658,310.00 USD | 0.00 USD | 658,310.00 USD | 117,230.00 USD | 21,570.00 USD | 10,950.00 USD |
| `1D` | `8.24` | 345,380.00 USD | 0.00 USD | 345,380.00 USD | 163,080.00 USD | 10,300.00 USD | 69,390.00 USD |
| `7D` | `8.24` | 508,550.00 USD | 0.00 USD | 508,550.00 USD | 39,950.00 USD | 3,480.00 USD | 107,710.00 USD |
| `1D` | `8.26` | 102,620.00 USD | 0.00 USD | 102,620.00 USD | 15,150.00 USD | 15,590.00 USD | 16,620.00 USD |
| `7D` | `8.26` | 357,410.00 USD | 0.00 USD | 357,410.00 USD | 30,490.00 USD | 5,750.00 USD | 1,870.00 USD |
| `1D` | `8.28` | 55,260.00 USD | 0.00 USD | 55,260.00 USD | 0.00 USD | 0.00 USD | 57.32 USD |
| `7D` | `8.28` | 319,300.00 USD | 0.00 USD | 319,300.00 USD | 122,850.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `8.30` | 195,270.00 USD | 0.00 USD | 195,270.00 USD | 152,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.32` | 55,210.00 USD | 0.00 USD | 55,210.00 USD | 55,190.00 USD | 0.00 USD | 16.44 USD |
| `7D` | `8.32` | 42,900.00 USD | 0.00 USD | 42,900.00 USD | 42,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.34` | 122.98 USD | 122.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.98 USD |
| `1D` | `8.34` | 245.96 USD | 245.96 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.98 USD |
| `7D` | `8.34` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.36` | 263.76 USD | 263.76 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17.80 USD |
| `7D` | `8.36` | 14,290.00 USD | 14,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `8.38` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | 691.75 USD | 0.00 USD | 64.64 USD |
| `7D` | `8.38` | 73,260.00 USD | 73,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 58,970.00 USD |
| `7D` | `8.40` | 108,990.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35,730.00 USD |
| `1D` | `8.42` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 788.46 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.42` | 128,030.00 USD | 128,030.00 USD | 0.00 USD | 16,070.00 USD | 0.00 USD | 2,970.00 USD |
| `1D` | `8.44` | 91,790.00 USD | 91,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 89,980.00 USD |
| `7D` | `8.44` | 138,510.00 USD | 138,510.00 USD | 0.00 USD | 10,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.46` | 419,730.00 USD | 419,730.00 USD | 0.00 USD | 35,680.00 USD | 4,700.00 USD | 287,550.00 USD |
| `7D` | `8.46` | 623,300.00 USD | 623,300.00 USD | 0.00 USD | 365,050.00 USD | 0.00 USD | 119,740.00 USD |
| `1D` | `8.48` | 517,470.00 USD | 517,470.00 USD | 0.00 USD | 0.00 USD | 39,180.00 USD | 58,560.00 USD |
| `7D` | `8.48` | 825,140.00 USD | 825,140.00 USD | 0.00 USD | 0.00 USD | 49,360.00 USD | 152,480.00 USD |
| `1D` | `8.50` | 805,570.00 USD | 805,570.00 USD | 0.00 USD | 66,120.00 USD | 101,350.00 USD | 120,630.00 USD |
| `7D` | `8.50` | 925,210.00 USD | 925,210.00 USD | 0.00 USD | 0.00 USD | 100,070.00 USD | 0.00 USD |
| `1D` | `8.52` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 203,080.00 USD | 69,980.00 USD | 164,800.00 USD |
| `7D` | `8.52` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 2,990.00 USD | 135,400.00 USD | 91,380.00 USD |
| `1D` | `8.54` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 61,500.00 USD | 32,530.00 USD | 16,750.00 USD |
| `7D` | `8.54` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 71,540.00 USD | 136,470.00 USD | 0.00 USD |
| `1D` | `8.56` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 183,280.00 USD | 33,670.00 USD | 0.00 USD |
| `7D` | `8.56` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 691,140.00 USD | 122,650.00 USD | 0.00 USD |
| `1D` | `8.58` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 234,090.00 USD | 5,060.00 USD | 179,360.00 USD |
| `7D` | `8.58` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 57,190.00 USD | 120,500.00 USD |
| `7D` | `8.60` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 75,040.00 USD | 39,160.00 USD | 388.58 USD |
| `1D` | `8.62` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 83,560.00 USD | 57,150.00 USD | 201,890.00 USD |
| `7D` | `8.62` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 43,670.00 USD | 87,180.00 USD |
| `1D` | `8.64` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 89,460.00 USD | 30,330.00 USD | 29,280.00 USD |
| `7D` | `8.64` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 12,800.00 USD | 76,240.00 USD |
| `1D` | `8.66` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 78,620.00 USD | 21,010.00 USD | 108,320.00 USD |
| `7D` | `8.66` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | 281.77 USD |
| `1D` | `8.68` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 65,090.00 USD | 9,810.00 USD | 212,540.00 USD |
| `7D` | `8.68` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 207,090.00 USD | 43,100.00 USD | 334,680.00 USD |
| `1D` | `8.70` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 50,130.00 USD | 16,260.00 USD | 30,560.00 USD |
| `7D` | `8.70` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 29,260.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.72` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 18,250.00 USD | 0.00 USD | 50,740.00 USD |
| `1D` | `8.74` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 49,310.00 USD | 28,810.00 USD | 12,900.00 USD |
| `7D` | `8.74` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 48,810.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.76` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 112,960.00 USD | 2,530.00 USD | 9,800.00 USD |
| `7D` | `8.76` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,980.00 USD |
| `1D` | `8.78` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 108,350.00 USD | 11,500.00 USD | 35,600.00 USD |
| `7D` | `8.78` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.80` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 125,120.00 USD | 22,330.00 USD | 52,850.00 USD |
| `7D` | `8.80` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 31,560.00 USD |
| `1D` | `8.82` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 19,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.82` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 103,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 40,640.00 USD | 8,820.00 USD | 73,730.00 USD |
| `1D` | `8.86` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 13,620.00 USD | 2,250.00 USD | 11,350.00 USD |
| `7D` | `8.86` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 81,960.00 USD |
| `1D` | `8.88` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 1,320.00 USD | 8,950.00 USD | 186.36 USD |
| `7D` | `8.88` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.90` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 31,860.00 USD | 8,140.00 USD | 122,600.00 USD |
| `7D` | `8.90` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 115,910.00 USD |
| `1D` | `8.92` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 40,710.00 USD | 7,360.00 USD | 17,020.00 USD |
| `7D` | `8.92` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 1,730.00 USD | 0.00 USD | 17,620.00 USD |
| `1D` | `8.94` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD |
| `7D` | `8.94` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.96` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 2,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.96` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 432.56 USD |
| `1D` | `8.98` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 25,040.00 USD | 5,550.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `9.00` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 85,360.00 USD | 30,520.00 USD | 11,400.00 USD |
| `7D` | `9.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD |
| `1D` | `9.02` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 40,920.00 USD | 43,160.00 USD | 18,840.00 USD |
| `7D` | `9.02` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 34,650.00 USD | 56,120.00 USD | 425.46 USD |
| `1D` | `9.04` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 87,540.00 USD | 43,590.00 USD | 38,730.00 USD |
| `7D` | `9.04` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 90,520.00 USD | 74,750.00 USD | 15,140.00 USD |
| `1D` | `9.06` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 35,620.00 USD | 33,420.00 USD | 60,040.00 USD |
| `7D` | `9.06` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.08` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD |
| `7D` | `9.08` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.10` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 197,760.00 USD | 43,240.00 USD | 81,020.00 USD |
| `7D` | `9.10` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD |
| `1D` | `9.12` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 167,130.00 USD | 47,350.00 USD | 108,750.00 USD |
| `7D` | `9.12` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 503,470.00 USD |
| `1D` | `9.14` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 118,520.00 USD | 23,510.00 USD | 79,110.00 USD |
| `7D` | `9.14` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,920.00 USD |
| `1D` | `9.16` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 121,810.00 USD | 44,640.00 USD | 63,950.00 USD |
| `7D` | `9.16` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,690.00 USD |
| `1D` | `9.18` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 174,230.00 USD | 44,900.00 USD | 105,630.00 USD |
| `7D` | `9.18` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 565,140.00 USD | 162,460.00 USD | 291,400.00 USD |
| `1D` | `9.20` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 141,410.00 USD | 43,540.00 USD | 51,090.00 USD |
| `7D` | `9.20` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 549,250.00 USD | 134,550.00 USD | 238,560.00 USD |
| `1D` | `9.22` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 86,390.00 USD | 10,580.00 USD | 13,790.00 USD |
| `7D` | `9.22` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 585,170.00 USD | 144,840.00 USD | 417,600.00 USD |
| `1D` | `9.24` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 47,010.00 USD | 4,270.00 USD | 3,040.00 USD |
| `7D` | `9.24` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 335,740.00 USD | 56,410.00 USD | 173,010.00 USD |
| `1D` | `9.26` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 35,150.00 USD | 8,290.00 USD | 9,710.00 USD |
| `7D` | `9.26` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 61,560.00 USD |
| `1D` | `9.28` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 44,530.00 USD | 10,920.00 USD | 2,780.00 USD |
| `7D` | `9.28` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,240.00 USD |
| `1D` | `9.30` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 59,470.00 USD | 13,560.00 USD | 29,560.00 USD |
| `7D` | `9.30` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 263,720.00 USD |
| `1D` | `9.32` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 37,200.00 USD | 4,250.00 USD | 23,760.00 USD |
| `7D` | `9.32` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,810.00 USD |
| `1D` | `9.34` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 40,730.00 USD | 9,520.00 USD | 11,500.00 USD |
| `7D` | `9.34` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 204,260.00 USD | 53,150.00 USD | 69,970.00 USD |
| `1D` | `9.36` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 52,470.00 USD | 10,420.00 USD | 33,220.00 USD |
| `7D` | `9.36` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 247,120.00 USD | 73,430.00 USD | 98,250.00 USD |
| `1D` | `9.38` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 29,420.00 USD | 7,320.00 USD | 14,510.00 USD |
| `7D` | `9.38` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 93,430.00 USD |
| `1D` | `9.40` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD | 25.34 USD |
| `7D` | `9.40` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 124,420.00 USD |
| `1D` | `9.42` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 10,810.00 USD | 2,390.00 USD | 14,160.00 USD |
| `7D` | `9.42` | 17,290,000.00 USD | 17,290,000.00 USD | 0.00 USD | 176,920.00 USD | 19,780.00 USD | 71,300.00 USD |
| `1D` | `9.44` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD |
| `7D` | `9.44` | 17,410,000.00 USD | 17,410,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,590.00 USD |
| `1D` | `9.46` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `9.46` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 60,020.00 USD | 29,830.00 USD | 19,240.00 USD |
| `7D` | `9.48` | 17,580,000.00 USD | 17,580,000.00 USD | 0.00 USD | 12,180.00 USD | 27,840.00 USD | 26,460.00 USD |
| `7D` | `9.50` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 89,460.00 USD | 33,210.00 USD | 45,830.00 USD |
| `7D` | `9.52` | 17,940,000.00 USD | 17,940,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 50,930.00 USD |
| `7D` | `9.54` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 192,090.00 USD | 25,090.00 USD | 378.07 USD |
| `7D` | `9.56` | 18,260,000.00 USD | 18,260,000.00 USD | 0.00 USD | 88,510.00 USD | 5,260.00 USD | 13,410.00 USD |
| `7D` | `9.58` | 18,340,000.00 USD | 18,340,000.00 USD | 0.00 USD | 35,340.00 USD | 14,530.00 USD | 26,840.00 USD |
| `7D` | `9.60` | 18,400,000.00 USD | 18,400,000.00 USD | 0.00 USD | 38,740.00 USD | 5,460.00 USD | 20,730.00 USD |
| `7D` | `9.62` | 18,480,000.00 USD | 18,480,000.00 USD | 0.00 USD | 70,470.00 USD | 1,540.00 USD | 10,380.00 USD |
| `7D` | `9.64` | 18,560,000.00 USD | 18,560,000.00 USD | 0.00 USD | 35,210.00 USD | 17,650.00 USD | 20,030.00 USD |
| `7D` | `9.66` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 17,790.00 USD |
| `7D` | `9.68` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 15,370.00 USD |
| `7D` | `9.70` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 77,860.00 USD | 12,990.00 USD | 31,780.00 USD |
| `7D` | `9.72` | 18,960,000.00 USD | 18,960,000.00 USD | 0.00 USD | 70,300.00 USD | 6,920.00 USD | 26,080.00 USD |
| `7D` | `9.74` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 21,230.00 USD | 7,200.00 USD | 20,230.00 USD |
| `7D` | `9.76` | 19,110,000.00 USD | 19,110,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 51,830.00 USD |
| `7D` | `9.78` | 19,190,000.00 USD | 19,190,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,470.00 USD |
| `7D` | `9.80` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,400.00 USD |
| `7D` | `9.82` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,510.00 USD |
| `7D` | `9.84` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,130.00 USD |
| `7D` | `9.86` | 19,650,000.00 USD | 19,650,000.00 USD | 0.00 USD | 58,130.00 USD | 2,210.00 USD | 71,810.00 USD |
| `7D` | `9.88` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 7,170.00 USD | 8,710.00 USD | 20,570.00 USD |
| `7D` | `9.90` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 15,360.00 USD |
| `7D` | `9.92` | 19,830,000.00 USD | 19,830,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 8,990.00 USD |
| `7D` | `9.94` | 19,960,000.00 USD | 19,960,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 51,560.00 USD |
| `7D` | `9.96` | 20,000,000.00 USD | 20,000,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 11,080.00 USD |
| `7D` | `9.98` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 29,460.00 USD |
| `7D` | `10.00` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 16,100.00 USD | 3,650.00 USD | 15,030.00 USD |
| `7D` | `10.04` | 20,090,000.00 USD | 20,090,000.00 USD | 0.00 USD | 1,080.00 USD | 3,590.00 USD | 9,540.00 USD |
| `7D` | `10.06` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD |
| `7D` | `10.08` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `350.88M` | Total OI Tokens: `41,744,583.1 AVAX`
  * 1h OI Change: `+0.95%` | 4h OI Change: `+0.33%` | 24h OI Change: `-7.71%`
  * Exchange Breakdown: Binance=`80.57M` | Bybit=`57.25M` | OKX=`11.61M` | Hyperliquid=`16.40M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-9.63K` | Last 24h: `18.18K` | Last 3d: `59.53K` | Last 7d: `106.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0074%` | **USDT OKX** | `0.0098%` |
| **USDT Bybit** | `-0.0308%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0073%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `0.0010%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `41.64%` | `58.36%` | `0.71` | 7,130,000.00 USD |
| `15M` | `Binance` | `40.92%` | `59.08%` | `0.69` | 2,710,000.00 USD |
| `15M` | `OKX` | `41.34%` | `58.66%` | `0.70` | 1,410,000.00 USD |
| `15M` | `Bybit` | `38.19%` | `61.81%` | `0.62` | 516,410.00 USD |
| `15M` | `KuCoin` | `32.84%` | `67.16%` | `0.49` | 33,320.00 USD |
| `15M` | `Gate` | `30.57%` | `69.43%` | `0.44` | 94,790.00 USD |
| `15M` | `Bitget` | `28.85%` | `71.15%` | `0.41` | 220,190.00 USD |
| `15M` | `BingX` | `46.43%` | `53.57%` | `0.87` | 103,080.00 USD |
| `15M` | `MEXC` | `49.09%` | `50.91%` | `0.96` | 1,480,000.00 USD |
| `15M` | `Bitunix` | `32.05%` | `67.95%` | `0.47` | 224,330.00 USD |
| `15M` | `Hyperliquid` | `25.46%` | `74.54%` | `0.34` | 126,270.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.05%` | `52.95%` | `0.89` | 156,680.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `89.96%` | `10.04%` | `8.96` | 14,800.00 USD |
| `15M` | `HTX` | `42.7%` | `57.3%` | `0.75` | 2,320.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `13.13%` | `86.87%` | `0.15` | 24,610.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.73%` | `47.27%` | `1.12` | 7,130.00 USD |
| `15M` | `Whale Positions` | `40.92%` | `59.08%` | `0.69` | 2,710,000.00 USD |
| `15M` | `Global Accounts` | `41.64%` | `58.36%` | `0.71` | 7,130,000.00 USD |
| `1H` | `AVAX` | `48.04%` | `51.96%` | `0.92` | 21,460,000.00 USD |
| `1H` | `Binance` | `50.1%` | `49.9%` | `1.00` | 8,030,000.00 USD |
| `1H` | `OKX` | `50.5%` | `49.5%` | `1.02` | 2,160,000.00 USD |
| `1H` | `Bybit` | `47.26%` | `52.74%` | `0.90` | 2,390,000.00 USD |
| `1H` | `KuCoin` | `51.71%` | `48.29%` | `1.07` | 154,730.00 USD |
| `1H` | `Gate` | `50.97%` | `49.03%` | `1.04` | 379,710.00 USD |
| `1H` | `Bitget` | `54.61%` | `45.39%` | `1.20` | 1,040,000.00 USD |
| `1H` | `BingX` | `49.22%` | `50.78%` | `0.97` | 1,000,000.00 USD |
| `1H` | `MEXC` | `33.97%` | `66.03%` | `0.51` | 1,040,000.00 USD |
| `1H` | `Bitunix` | `43.57%` | `56.43%` | `0.77` | 593,580.00 USD |
| `1H` | `Hyperliquid` | `65.8%` | `34.2%` | `1.92` | 128,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.2%` | `50.8%` | `0.97` | 3,960,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.62%` | `94.38%` | `0.06` | 175,720.00 USD |
| `1H` | `HTX` | `36.89%` | `63.11%` | `0.58` | 147,390.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.12%` | `99.88%` | `0.00` | 300.32 USD |
| `1H` | `Aster` | `9.28%` | `90.72%` | `0.10` | 225,730.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `15.54%` | `84.46%` | `0.18` | 48,860.00 USD |
| `1H` | `Whale Positions` | `50.1%` | `49.9%` | `1.00` | 8,030,000.00 USD |
| `1H` | `Global Accounts` | `48.04%` | `51.96%` | `0.92` | 21,460,000.00 USD |
| `4H` | `AVAX` | `47.46%` | `52.54%` | `0.90` | 477,020,000.00 USD |
| `4H` | `Binance` | `47.72%` | `52.28%` | `0.91` | 177,620,000.00 USD |
| `4H` | `OKX` | `47.6%` | `52.4%` | `0.91` | 112,330,000.00 USD |
| `4H` | `Bybit` | `49.19%` | `50.81%` | `0.97` | 47,350,000.00 USD |
| `4H` | `KuCoin` | `53.27%` | `46.73%` | `1.14` | 4,310,000.00 USD |
| `4H` | `Gate` | `50.62%` | `49.38%` | `1.03` | 40,100,000.00 USD |
| `4H` | `Bitget` | `43.4%` | `56.6%` | `0.77` | 16,010,000.00 USD |
| `4H` | `BingX` | `26.14%` | `73.86%` | `0.35` | 7,740,000.00 USD |
| `4H` | `MEXC` | `43.43%` | `56.57%` | `0.77` | 22,930,000.00 USD |
| `4H` | `Bitunix` | `47.54%` | `52.46%` | `0.91` | 17,480,000.00 USD |
| `4H` | `Hyperliquid` | `49.25%` | `50.75%` | `0.97` | 6,330,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.3%` | `42.7%` | `1.34` | 1,460,000.00 USD |
| `4H` | `Crypto.com` | `43.59%` | `56.41%` | `0.77` | 588,330.00 USD |
| `4H` | `WhiteBIT` | `20.64%` | `79.36%` | `0.26` | 3,940,000.00 USD |
| `4H` | `HTX` | `52.7%` | `47.3%` | `1.11` | 12,620,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.59%` | `51.41%` | `0.95` | 1,120,000.00 USD |
| `4H` | `Aster` | `56.05%` | `43.95%` | `1.28` | 4,840,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.81%` | `58.19%` | `0.72` | 232,720.00 USD |
| `4H` | `Whale Positions` | `47.72%` | `52.28%` | `0.91` | 177,620,000.00 USD |
| `4H` | `Global Accounts` | `47.46%` | `52.54%` | `0.90` | 477,020,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.21` | `8.19` | `8.21` | `8.22` | `8.16` | 1,163,864.40 USD | 663,189.73 USD | 500,674.67 USD | 162,515.06 USD | `+13.96%` | `9B / 6S` |
| `0:00 UTC` | `8.17` | `8.20` | `8.17` | `8.25` | `8.15` | 1,223,062.19 USD | 718,965.78 USD | 504,096.41 USD | 214,869.37 USD | `+17.57%` | `26B / 17S` |
| `5:00 UTC` | `8.30` | `8.29` | `8.30` | `8.33` | `8.24` | 1,042,239.86 USD | 674,984.50 USD | 367,255.36 USD | 307,729.14 USD | `+29.53%` | `28B / 5S` |
| `0:00 UTC` | `8.34` | `8.33` | `8.34` | `8.35` | `8.30` | 876,108.07 USD | 469,253.46 USD | 406,854.61 USD | 62,398.85 USD | `+7.12%` | `5B / 6S` |
| `5:00 UTC` | `8.33` | `8.32` | `8.33` | `8.35` | `8.30` | 843,379.31 USD | 374,655.63 USD | 468,723.68 USD | -94,068.04 USD | `-11.15%` | `5B / 8S` |
| `0:00 UTC` | `8.35` | `8.34` | `8.35` | `8.36` | `8.31` | 780,795.97 USD | 434,601.51 USD | 346,194.47 USD | 88,407.04 USD | `+11.32%` | `13B / 6S` |
| `5:00 UTC` | `8.38` | `8.37` | `8.38` | `8.39` | `8.33` | 1,720,663.97 USD | 1,209,797.38 USD | 510,866.59 USD | 698,930.78 USD | `+40.62%` | `15B / 2S` |
| `0:00 UTC` | `8.44` | `8.42` | `8.44` | `8.46` | `8.37` | 1,398,848.87 USD | 756,591.46 USD | 642,257.41 USD | 114,334.05 USD | `+8.17%` | `18B / 13S` |
| `5:00 UTC` | `8.43` | `8.45` | `8.43` | `8.48` | `8.43` | 1,888,943.37 USD | 611,021.12 USD | 1,277,922.26 USD | -666,901.14 USD | `-35.31%` | `4B / 11S` |
| `0:00 UTC` | `8.45` | `8.45` | `8.45` | `8.45` | `8.44` | 11,513.06 USD | 2,821.55 USD | 8,691.51 USD | -5,869.97 USD | `-50.99%` | `1B / 3S` |

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
| `5m` | -38,370.00 USD | -55,880.00 USD | **`DISTRIBUTION`** |
| `15m` | -76,750.00 USD | -801,430.00 USD | **`DISTRIBUTION`** |
| `30m` | -46,970.00 USD | -464,590.00 USD | **`DISTRIBUTION`** |
| `1h` | -67,910.00 USD | 398,540.00 USD | **`ACCUMULATION`** |
| `2h` | 111,410.00 USD | 1,410,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,400,000.00 USD | -1,170,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -653,950.00 USD | -2,130,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,560,000.00 USD | -7,720,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,930,000.00 USD | -12,250,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,550,000.00 USD | -10,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,760,000.00 USD | -54,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,040,000.00 USD | -270,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-38.37K` | 15m=`-76.75K` | 1h=`-67.91K` | 24h=`-2.55M`
* Futures Capital Netflows: 5m=`-55.88K` | 15m=`-801.43K` | 1h=`+398.54K` | 24h=`-10.79M`
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
  * Execution Entry: `8.16` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.90` (Risk Distance: `1.26` pts)
  * +2.5R Take Profit: `11.31`
  * Mathematical Lot Sizing: **`7.93 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.42` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.68` (Risk Distance: `1.26` pts)
  * +2.5R Take Profit: `5.27`
  * Mathematical Lot Sizing: **`7.93 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
