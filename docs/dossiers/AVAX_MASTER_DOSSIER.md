# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:36:03 IST` (`2026-10-29 20:06:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.77` | **Live Ask Quote**: `8.80` | **Mid Price**: `8.79`
- **Spread Points**: `3.00` | **Spread BPS**: `34.15 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `8.90` (Distance: `-1.27%`)
  * Point of Control (POC) = `8.78` (Distance: `+0.12%`)
  * Value Area Low (VAL) = `8.58` (Distance: `+2.43%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `8.75` - `8.82`
  * Optimal Trade Entry (OTE 0.705): `8.80`
  * Structural Invalidation Anchor (0.786): `8.86`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.85` | `8.87` | `8.85` | `8.85` | `13,237` | 117,232.22 USD | 16,614.28 USD | `+14.17%` | -4,743,510.56 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.85` | `8.85` | `8.84` | `8.85` | `20,878` | 184,681.04 USD | -62,492.08 USD | `-33.84%` | -4,806,002.64 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.85` | `8.86` | `8.78` | `8.79` | `121,419` | 1,070,268.64 USD | -131,556.01 USD | `-12.29%` | -4,937,558.65 USD | `-1.83` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `8.83` | `8.87` | `8.83` | `8.85` | `66,310` | 587,148.06 USD | 200,256.54 USD | `+34.11%` | -4,233,883.87 USD | `+0.99` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.85` | `8.87` | `8.84` | `8.85` | `48,790` | 431,773.06 USD | -50,732.69 USD | `-11.75%` | -4,284,616.56 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.85` | `8.86` | `8.78` | `8.79` | `121,610` | 1,071,947.91 USD | -133,147.36 USD | `-12.42%` | -4,417,763.92 USD | `-0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `8.87` | `8.89` | `8.79` | `8.84` | `435,467` | 3,847,058.68 USD | -67,411.45 USD | `-1.75%` | -4,291,060.73 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.84` | `8.87` | `8.80` | `8.85` | `249,668` | 2,205,666.85 USD | 221,936.79 USD | `+10.06%` | -4,069,123.94 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.85` | `8.86` | `8.78` | `8.79` | `121,419` | 1,070,268.64 USD | -131,556.01 USD | `-12.29%` | -4,200,679.95 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.78` | `8.79` | `121,419` | 1,070,268.64 USD | -131,556.01 USD | `-12.29%` | -4,797,566.98 USD | `+0.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.78` | `8.79` | `121,419` | 1,070,268.64 USD | -131,556.01 USD | `-12.29%` | -4,797,566.98 USD | `+0.56` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.79`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `8.85` | `146.6000` | 1,298.11 USD | 9,028.10 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.85` | `120.0800` | 1,063.27 USD | 7,729.98 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.85` | `677.6700` | 6,000.50 USD | 6,666.71 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `8.85` | `75.2400` | 666.21 USD | 666.21 USD | `2 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.85` | `0.00%` | `-` |
| `BID` | `8.85` | `40.8300` | 361.44 USD | 361.44 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.85` | `54.4500` | 482.00 USD | 843.44 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `195.6800` | 1,732.06 USD | 2,575.50 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `54.4500` | 481.96 USD | 3,057.46 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `50.0000` | 442.56 USD | 3,500.02 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `66.0000` | 584.17 USD | 4,084.19 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `50.0000` | 442.55 USD | 4,526.74 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `42.5600` | 376.69 USD | 4,903.44 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `50.0000` | 442.53 USD | 5,345.96 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `40.8300` | 361.36 USD | 5,707.32 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `54.5100` | 482.41 USD | 6,189.74 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.85` | `538.0900` | 4,762.04 USD | 10,951.78 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `8.85` | `121.9900` | 1,079.54 USD | 12,031.32 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `70.8000` | 626.53 USD | 12,657.85 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `54.4300` | 481.66 USD | 13,139.51 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `164.0700` | 1,451.81 USD | 14,591.32 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `732.5200` | 6,481.70 USD | 21,073.02 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.85` | `80.1000` | 708.76 USD | 21,781.78 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.85` | `223.1100` | 1,974.14 USD | 23,755.92 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.69 USD | 24,237.61 USD | `1 orders` | `-0.06%` | `-` |
| `ASK` | `8.86` | `121.9300` | 1,080.03 USD | 48,075.48 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `1669.7600` | 14,789.73 USD | 46,995.45 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `167.3400` | 1,482.18 USD | 32,205.72 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `85.2600` | 755.16 USD | 30,723.54 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `413.1600` | 3,659.32 USD | 29,968.38 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `139.1300` | 1,232.25 USD | 26,309.06 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `57.3100` | 507.58 USD | 25,076.82 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `54.4400` | 482.15 USD | 24,569.24 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `2.9000` | 25.68 USD | 24,087.09 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `1016.2200` | 8,999.95 USD | 24,061.41 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `54.4400` | 482.13 USD | 15,061.46 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `200.0000` | 1,771.20 USD | 14,579.33 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `28.4700` | 252.13 USD | 12,808.13 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `46.3500` | 410.46 USD | 12,556.01 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.86` | `54.4400` | 482.09 USD | 12,145.55 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.86` | `297.6100` | 2,635.37 USD | 11,663.46 USD | `2 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1493` | `0x7737...bf66` | `SHORT` | 1,518,428.80 USD | `171,568.06` | `7.43` | `8.85` | `110.50` | -242,883.78 USD | `-16.00%` | `10X Cross` |
| `1571` | `0xeadc...9d55` | `LONG` | 1,416,752.51 USD | `160,070.56` | `8.11` | `8.85` | `0.000000` | 119,114.94 USD | `+8.41%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`9.22` (Vol: 276,800.00 USD, Dist: `+4.22%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.42%`)
  * 48H Horizon: Short MP=`9.22` (Vol: 221,300.00 USD, Dist: `+4.22%`) | Long MP=`8.46` (Vol: 190,100.00 USD, Dist: `--4.42%`)
  * 3D Horizon: Short MP=`9.22` (Vol: 264,100.00 USD, Dist: `+4.22%`) | Long MP=`8.75` (Vol: 159,700.00 USD, Dist: `--1.09%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 419,200.00 USD, Dist: `+4.90%`) | Long MP=`8.54` (Vol: 343,100.00 USD, Dist: `--3.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.85` | 204.05 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 481.25 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 159.60 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 104.26 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 375.35 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,170.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 290.37 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 265.65 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 814.80 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 17,370.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 109.88 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 133.73 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 45,470.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 1,130.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 1,460.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 404.38 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 114.82 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 152.25 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 775.18 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 341.01 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 371.88 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.08` | 9,290.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 1,130.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 174.89 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.20` | 419.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.29` | 2,440.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 174.83 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.32` | 852.47 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.33` | 2,190.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.37` | 117.86 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.51` | 217.71 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,680.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,490.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,730.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 240.48 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.80` | 15,790.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 6,380.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 146.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 527.19 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,350.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.99` | 329.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 318.46 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 4,690.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.16` | 156,890.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 2,300.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 21,080.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 163,110.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 367.41 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 121.38 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.57` | 967.98 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.59` | 34,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 22,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.66` | 4,160.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.70` | 405.03 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 2,340.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 238.86 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 2,890.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 736.72 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.88` | 329,350.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 640.67 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 12,380.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 447.98 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.03` | 404.46 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 331.68 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 448.72 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 1,630.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,550.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.11` | 3,200.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,370.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 4,390.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 187.29 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 2,560.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 715.31 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 1,610.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.32` | 277.04 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 105.25 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,110.00 USD | 896,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.41` | 1,640.00 USD | 891,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 890,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 889,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 883,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 1,720.00 USD | 882,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 3,620.00 USD | 880,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 876,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 2,170.00 USD | 867,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,100.00 USD | 865,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 864,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 506.54 USD | 862,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,610.00 USD | 861,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 845,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 6,780.00 USD | 843,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 16,960.00 USD | 837,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 4,260.00 USD | 820,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 815,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 2,670.00 USD | 814,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 811,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 4,830.00 USD | 811,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.86` | 18,930.00 USD | 806,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 787,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.89` | 5,250.00 USD | 784,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.91` | 269.30 USD | 779,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 1,510.00 USD | 778,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,760.00 USD | 777,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 3,480.00 USD | 773,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 28,500.00 USD | 770,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.99` | 1,400.00 USD | 741,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,550.00 USD | 740,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 24,240.00 USD | 738,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.04` | 4,100.00 USD | 714,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 710,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,670.00 USD | 703,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,230.00 USD | 702,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 673,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 2,300.00 USD | 673,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,950.00 USD | 671,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.16` | 1,630.00 USD | 650,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 648,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 581.02 USD | 647,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 179.65 USD | 646,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 646,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,560.00 USD | 646,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 19,790.00 USD | 609,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.32` | 168.76 USD | 589,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 4,910.00 USD | 589,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 2,450.00 USD | 584,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 4,370.00 USD | 582,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 577,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 572,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 568,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 1,550.00 USD | 550,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.42` | 1,540.00 USD | 548,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 1,700.00 USD | 547,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 545,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 5,430.00 USD | 544,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 538,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 535,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 534,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 533,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 532,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 527,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 118.09 USD | 527,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 4,260.00 USD | 527,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 523,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 498,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 497,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 497,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 496,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 496,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 494,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 493,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,410.00 USD | 492,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 472,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 470,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 469,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 468,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 468,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 464,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 462,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.81` | 9,750,000.00 USD | 9,750,000.00 USD | 16,260.00 USD | 16,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 461,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.83` | 9,720,000.00 USD | 9,720,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 456,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.85` | 9,660,000.00 USD | 9,660,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 445,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 443,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.87` | 9,630,000.00 USD | 9,630,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 443,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.89` | 9,570,000.00 USD | 9,570,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,410.00 USD | 442,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.91` | 9,500,000.00 USD | 9,500,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 5,210,000.00 USD | 5,210,000.00 USD | 16,360.00 USD | 2,950.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 440,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,180,000.00 USD | 5,180,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 9,450,000.00 USD | 9,450,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 439,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,170,000.00 USD | 5,170,000.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 437,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 5,150,000.00 USD | 5,150,000.00 USD | 74.90 USD | 5,170.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 9,350,000.00 USD | 9,350,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 310,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 5,140,000.00 USD | 5,140,000.00 USD | 2,760.00 USD | 3,170.00 USD | 13.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 5,130,000.00 USD | 5,130,000.00 USD | 9,050.00 USD | 1,920.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 9,250,000.00 USD | 9,250,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 5,110,000.00 USD | 5,110,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 309,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 5,110,000.00 USD | 5,110,000.00 USD | 482.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 9,160,000.00 USD | 9,160,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 307,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 5,100,000.00 USD | 5,100,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 5,100,000.00 USD | 5,100,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 9,060,000.00 USD | 9,060,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 5,090,000.00 USD | 5,090,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 307,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 5,080,000.00 USD | 5,080,000.00 USD | 8,600.00 USD | 1,540.00 USD | 288.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 8,990,000.00 USD | 8,990,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 306,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 5,070,000.00 USD | 5,070,000.00 USD | 9,860.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 218,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 5,060,000.00 USD | 5,060,000.00 USD | 14,360.00 USD | 3,770.00 USD | 330.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 8,810,000.00 USD | 8,810,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 211,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 5,040,000.00 USD | 5,040,000.00 USD | 12,030.00 USD | 1,700.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 208,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 5,020,000.00 USD | 5,020,000.00 USD | 1,100.00 USD | 2,400.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 8,680,000.00 USD | 8,680,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 5,020,000.00 USD | 5,020,000.00 USD | 4,580.00 USD | 1,410.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 170,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 5,010,000.00 USD | 5,010,000.00 USD | 9,480.00 USD | 1,220.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 8,530,000.00 USD | 8,530,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 165.46 USD | 169,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 4,990,000.00 USD | 4,990,000.00 USD | 9,530.00 USD | 2,720.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.11` | 11,550.00 USD | 169,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,970,000.00 USD | 4,970,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 8,450,000.00 USD | 8,450,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 157,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 4,960,000.00 USD | 4,960,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,940,000.00 USD | 4,940,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 8,400,000.00 USD | 8,400,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 4,940,000.00 USD | 4,940,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,920,000.00 USD | 4,920,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 8,330,000.00 USD | 8,330,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 4,900,000.00 USD | 4,900,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 157,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,900,000.00 USD | 4,900,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 8,190,000.00 USD | 8,190,000.00 USD | 6,560.00 USD | 7,770.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 4,890,000.00 USD | 4,890,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,890,000.00 USD | 4,890,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 8,170,000.00 USD | 8,170,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,290.00 USD | 156,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 4,890,000.00 USD | 4,890,000.00 USD | 7,720.00 USD | 2,310.00 USD | 445.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 155,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,870,000.00 USD | 4,870,000.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 8,130,000.00 USD | 8,130,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 153,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 4,870,000.00 USD | 4,870,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 153,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,850,000.00 USD | 4,850,000.00 USD | 20,920.00 USD | 4,080.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 8,100,000.00 USD | 8,100,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 151,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 4,800,000.00 USD | 4,800,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 150,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,780,000.00 USD | 4,780,000.00 USD | 8,080.00 USD | 0.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 7,970,000.00 USD | 7,970,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 148,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 4,770,000.00 USD | 4,770,000.00 USD | 215.69 USD | 11,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,760,000.00 USD | 4,760,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 7,900,000.00 USD | 7,900,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,860.00 USD | 135,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 4,740,000.00 USD | 4,740,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 125,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,620,000.00 USD | 4,620,000.00 USD | 34,850.00 USD | 9,470.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 7,820,000.00 USD | 7,820,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 124,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 4,570,000.00 USD | 4,570,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 105,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 4,490,000.00 USD | 4,490,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 7,630,000.00 USD | 7,630,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 72,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 4,420,000.00 USD | 4,420,000.00 USD | 19,380.00 USD | 4,190.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 4,390,000.00 USD | 4,390,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 7,530,000.00 USD | 7,530,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,630.00 USD | 67,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 4,350,000.00 USD | 4,350,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 4,330,000.00 USD | 4,330,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 7,410,000.00 USD | 7,410,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,410.00 USD | 63,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 4,290,000.00 USD | 4,290,000.00 USD | 4,090.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,160.00 USD | 59,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 4,260,000.00 USD | 4,260,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 7,230,000.00 USD | 7,230,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 3,410.00 USD | 52,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.38` | 4,230,000.00 USD | 4,230,000.00 USD | 35,960.00 USD | 4,080.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 1,870.00 USD | 49,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 4,150,000.00 USD | 4,150,000.00 USD | 63,220.00 USD | 10,540.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 7,080,000.00 USD | 7,080,000.00 USD | 197,900.00 USD | 8,930.00 USD | 68,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 47,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.40` | 4,020,000.00 USD | 4,020,000.00 USD | 67,650.00 USD | 22,890.00 USD | 68,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 710.22 USD | 45,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.41` | 3,860,000.00 USD | 3,860,000.00 USD | 33,220.00 USD | 3,620.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 6,800,000.00 USD | 6,800,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.41` | 681.03 USD | 44,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.42` | 3,800,000.00 USD | 3,800,000.00 USD | 33,600.00 USD | 12,790.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.43` | 674.00 USD | 44,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.43` | 3,740,000.00 USD | 3,740,000.00 USD | 29,980.00 USD | 34,530.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 6,400,000.00 USD | 6,400,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 43,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.44` | 3,660,000.00 USD | 3,660,000.00 USD | 35,570.00 USD | 8,900.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 1,470.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.45` | 3,610,000.00 USD | 3,610,000.00 USD | 73,020.00 USD | 17,050.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 6,090,000.00 USD | 6,090,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 226.93 USD | 41,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.46` | 3,470,000.00 USD | 3,470,000.00 USD | 153,340.00 USD | 17,770.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,860.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.47` | 3,250,000.00 USD | 3,250,000.00 USD | 120,680.00 USD | 30,070.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 5,730,000.00 USD | 5,730,000.00 USD | 426,960.00 USD | 70,760.00 USD | 200,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.48` | 3,080,000.00 USD | 3,080,000.00 USD | 126,360.00 USD | 39,180.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 27,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.49` | 2,860,000.00 USD | 2,860,000.00 USD | 140,860.00 USD | 36,190.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 5,030,000.00 USD | 5,030,000.00 USD | 283,720.00 USD | 54,550.00 USD | 118,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 26,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.50` | 2,680,000.00 USD | 2,680,000.00 USD | 64,670.00 USD | 12,970.00 USD | 28,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,570,000.00 USD | 2,570,000.00 USD | 16,530.00 USD | 48,100.00 USD | 21,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 4,570,000.00 USD | 4,570,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.52` | 2,490,000.00 USD | 2,490,000.00 USD | 48,940.00 USD | 17,250.00 USD | 23,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 2,400,000.00 USD | 2,400,000.00 USD | 17,100.00 USD | 29,630.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 4,080,000.00 USD | 4,080,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.54` | 2,310,000.00 USD | 2,310,000.00 USD | 19,100.00 USD | 6,040.00 USD | 43,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 2,240,000.00 USD | 2,240,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 3,260,000.00 USD | 3,260,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 2,140,000.00 USD | 2,140,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 1,990,000.00 USD | 1,990,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 2,830,000.00 USD | 2,830,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 1,830,000.00 USD | 1,830,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,680,000.00 USD | 1,680,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 1,950,000.00 USD | 1,950,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 1,550,000.00 USD | 1,550,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 1,420,000.00 USD | 1,420,000.00 USD | 35,340.00 USD | 12,770.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.61` | 1,470,000.00 USD | 1,470,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.62` | 1,360,000.00 USD | 1,360,000.00 USD | 102,610.00 USD | 23,160.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 1,200,000.00 USD | 1,200,000.00 USD | 77,860.00 USD | 21,050.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.63` | 1,110,000.00 USD | 1,110,000.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.64` | 1,090,000.00 USD | 1,090,000.00 USD | 105,620.00 USD | 11,790.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 954,100.00 USD | 954,100.00 USD | 50,810.00 USD | 31,510.00 USD | 33,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.65` | 1,010,000.00 USD | 1,010,000.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.66` | 838,680.00 USD | 838,680.00 USD | 74,110.00 USD | 26,760.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 722,810.00 USD | 722,810.00 USD | 59,230.00 USD | 9,170.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.67` | 772,830.00 USD | 772,830.00 USD | 77,920.00 USD | 24,870.00 USD | 173,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.68` | 626,980.00 USD | 626,980.00 USD | 39,990.00 USD | 5,900.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.69` | 576,510.00 USD | 576,510.00 USD | 18,040.00 USD | 5,700.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.69` | 496,130.00 USD | 496,130.00 USD | 70,550.00 USD | 12,790.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.70` | 530,590.00 USD | 530,590.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.71` | 496,220.00 USD | 496,220.00 USD | 18,250.00 USD | 11,690.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.73` | 447,300.00 USD | 447,300.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.74` | 394,470.00 USD | 394,470.00 USD | 0.00 USD | 7,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.75` | 386,750.00 USD | 386,750.00 USD | 32,080.00 USD | 8,290.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.75` | 390,230.00 USD | 390,230.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.76` | 310,550.00 USD | 310,550.00 USD | 78,530.00 USD | 15,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.77` | 216,980.00 USD | 216,980.00 USD | 54,300.00 USD | 8,510.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.77` | 169,270.00 USD | 169,270.00 USD | 26,810.00 USD | 0.00 USD | 81,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.78` | 128,450.00 USD | 128,450.00 USD | 19,230.00 USD | 0.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.79` | 99,340.00 USD | 99,340.00 USD | 13,010.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.79` | 61,220.00 USD | 61,220.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.80` | 74,330.00 USD | 74,330.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.81` | 8,570.00 USD | 8,570.00 USD | 0.00 USD | 8,450.00 USD | 118.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.84` | 68,640.00 USD | 68,640.00 USD | 0.00 USD | 0.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 44,480.00 USD | 44,480.00 USD | 0.00 USD | 0.00 USD | 44,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 77,770.00 USD | 77,770.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 115,480.00 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 71,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 89,330.00 USD | 89,330.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 102,370.00 USD | 102,370.00 USD | 0.00 USD | 5,550.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 176,380.00 USD | 176,380.00 USD | 40,450.00 USD | 30,520.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 209,720.00 USD | 209,720.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 221,430.00 USD | 221,430.00 USD | 36,960.00 USD | 0.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 241,530.00 USD | 241,530.00 USD | 1,080.00 USD | 5,120.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 451,940.00 USD | 451,940.00 USD | 185,270.00 USD | 36,180.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 315,350.00 USD | 315,350.00 USD | 38,060.00 USD | 30,950.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 429,270.00 USD | 429,270.00 USD | 54,730.00 USD | 31,750.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 626,990.00 USD | 626,990.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 470,090.00 USD | 470,090.00 USD | 18,960.00 USD | 10,710.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 538,390.00 USD | 538,390.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 719,540.00 USD | 719,540.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 589,720.00 USD | 589,720.00 USD | 27,120.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 653,730.00 USD | 653,730.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 759,900.00 USD | 759,900.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 695,350.00 USD | 695,350.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 853,910.00 USD | 853,910.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 1,050,000.00 USD | 1,050,000.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 949,220.00 USD | 949,220.00 USD | 66,840.00 USD | 22,440.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 1,060,000.00 USD | 1,060,000.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 2,490,000.00 USD | 2,490,000.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 1,200,000.00 USD | 1,200,000.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 1,350,000.00 USD | 1,350,000.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 3,690,000.00 USD | 3,690,000.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 1,420,000.00 USD | 1,420,000.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 1,520,000.00 USD | 1,520,000.00 USD | 57,880.00 USD | 22,150.00 USD | 22,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 4,330,000.00 USD | 4,330,000.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 1,630,000.00 USD | 1,630,000.00 USD | 63,210.00 USD | 18,910.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 1,810,000.00 USD | 1,810,000.00 USD | 107,540.00 USD | 18,740.00 USD | 50,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 5,160,000.00 USD | 5,160,000.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 1,980,000.00 USD | 1,980,000.00 USD | 80,310.00 USD | 35,050.00 USD | 56,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,140,000.00 USD | 2,140,000.00 USD | 97,890.00 USD | 40,200.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 5,960,000.00 USD | 5,960,000.00 USD | 503,250.00 USD | 101,150.00 USD | 193,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.20` | 3,800.00 USD | 4,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 2,340,000.00 USD | 2,340,000.00 USD | 119,740.00 USD | 12,660.00 USD | 67,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,400,000.00 USD | 2,400,000.00 USD | 48,600.00 USD | 6,420.00 USD | 9,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 6,920,000.00 USD | 6,920,000.00 USD | 554,780.00 USD | 132,850.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 2,520,000.00 USD | 2,520,000.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 2,610,000.00 USD | 2,610,000.00 USD | 57,020.00 USD | 3,310.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 7,940,000.00 USD | 7,940,000.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 2,640,000.00 USD | 2,640,000.00 USD | 31,050.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 2,690,000.00 USD | 2,690,000.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 8,440,000.00 USD | 8,440,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 2,710,000.00 USD | 2,710,000.00 USD | 16,250.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 2,740,000.00 USD | 2,740,000.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 8,770,000.00 USD | 8,770,000.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 2,770,000.00 USD | 2,770,000.00 USD | 20,250.00 USD | 3,860.00 USD | 27.40 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 2,850,000.00 USD | 2,850,000.00 USD | 48,970.00 USD | 15,680.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 9,620,000.00 USD | 9,620,000.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 2,900,000.00 USD | 2,900,000.00 USD | 42,450.00 USD | 9,410.00 USD | 26.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 2,960,000.00 USD | 2,960,000.00 USD | 27,590.00 USD | 4,250.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 10,260,000.00 USD | 10,260,000.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 2,980,000.00 USD | 2,980,000.00 USD | 9,610.00 USD | 2,530.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 3,000,000.00 USD | 3,000,000.00 USD | 7,010.00 USD | 6,000.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 10,630,000.00 USD | 10,630,000.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 3,030,000.00 USD | 3,030,000.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,090,000.00 USD | 3,090,000.00 USD | 28,980.00 USD | 3,810.00 USD | 20,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 11,110,000.00 USD | 11,110,000.00 USD | 289,480.00 USD | 88,340.00 USD | 96,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 3,150,000.00 USD | 3,150,000.00 USD | 30,450.00 USD | 11,070.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,210,000.00 USD | 3,210,000.00 USD | 36,610.00 USD | 13,410.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 11,580,000.00 USD | 11,580,000.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 3,280,000.00 USD | 3,280,000.00 USD | 47,540.00 USD | 4,040.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,310,000.00 USD | 3,310,000.00 USD | 16,910.00 USD | 1,730.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 11,940,000.00 USD | 11,940,000.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 3,350,000.00 USD | 3,350,000.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,400,000.00 USD | 3,400,000.00 USD | 29,300.00 USD | 1,660.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 12,390,000.00 USD | 12,390,000.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 3,410,000.00 USD | 3,410,000.00 USD | 10,620.00 USD | 622.99 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,440,000.00 USD | 3,440,000.00 USD | 10,160.00 USD | 6,940.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 12,630,000.00 USD | 12,630,000.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 3,450,000.00 USD | 3,450,000.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,450,000.00 USD | 3,450,000.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 12,770,000.00 USD | 12,770,000.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 3,010.00 USD | 417,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.46` | 3,460,000.00 USD | 3,460,000.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,490,000.00 USD | 3,490,000.00 USD | 18,220.00 USD | 6,870.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 12,870,000.00 USD | 12,870,000.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 3,490,000.00 USD | 3,490,000.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,520,000.00 USD | 3,520,000.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 12,950,000.00 USD | 12,950,000.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 3,540,000.00 USD | 3,540,000.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,540,000.00 USD | 3,540,000.00 USD | 295.05 USD | 0.00 USD | 124.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 13,250,000.00 USD | 13,250,000.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 3,570,000.00 USD | 3,570,000.00 USD | 17,180.00 USD | 3,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,590,000.00 USD | 3,590,000.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 13,460,000.00 USD | 13,460,000.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 3,600,000.00 USD | 3,600,000.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,610,000.00 USD | 3,610,000.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 13,510,000.00 USD | 13,510,000.00 USD | 28,850.00 USD | 17,400.00 USD | 880.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 3,620,000.00 USD | 3,620,000.00 USD | 4,750.00 USD | 1,280.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,630,000.00 USD | 3,630,000.00 USD | 1,370.00 USD | 3,100.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 13,670,000.00 USD | 13,670,000.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 3,640,000.00 USD | 3,640,000.00 USD | 1,110.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,650,000.00 USD | 3,650,000.00 USD | 4,830.00 USD | 1,250.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 13,730,000.00 USD | 13,730,000.00 USD | 26,920.00 USD | 15,650.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 3,670,000.00 USD | 3,670,000.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 3,700,000.00 USD | 3,700,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 13,860,000.00 USD | 13,860,000.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 3,700,000.00 USD | 3,700,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 3,720,000.00 USD | 3,720,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.63` | 13,910,000.00 USD | 13,910,000.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 3,720,000.00 USD | 3,720,000.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 3,740,000.00 USD | 3,740,000.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.65` | 13,980,000.00 USD | 13,980,000.00 USD | 33,020.00 USD | 20,230.00 USD | 18,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 3,750,000.00 USD | 3,750,000.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 3,760,000.00 USD | 3,760,000.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 14,060,000.00 USD | 14,060,000.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 3,780,000.00 USD | 3,780,000.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.69` | 3,790,000.00 USD | 3,790,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 14,230,000.00 USD | 14,230,000.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 3,810,000.00 USD | 3,810,000.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 3,820,000.00 USD | 3,820,000.00 USD | 74.90 USD | 5,170.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 14,370,000.00 USD | 14,370,000.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 3,830,000.00 USD | 3,830,000.00 USD | 2,760.00 USD | 3,170.00 USD | 57.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 14,390,000.00 USD | 14,390,000.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 417,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 3,830,000.00 USD | 3,830,000.00 USD | 5,260.00 USD | 738.05 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.75` | 3,840,000.00 USD | 3,840,000.00 USD | 3,790.00 USD | 1,180.00 USD | 946.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.75` | 14,470,000.00 USD | 14,470,000.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.76` | 3,850,000.00 USD | 3,850,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 14,580,000.00 USD | 14,580,000.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.78` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.79` | 3,860,000.00 USD | 3,860,000.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.79` | 14,650,000.00 USD | 14,650,000.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.79` | 551.36 USD | 418,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.81` | 14,820,000.00 USD | 14,820,000.00 USD | 103,830.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.81` | 472.10 USD | 418,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.83` | 14,950,000.00 USD | 14,950,000.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.85` | 15,050,000.00 USD | 15,050,000.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.87` | 15,100,000.00 USD | 15,100,000.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.89` | 15,180,000.00 USD | 15,180,000.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.91` | 15,230,000.00 USD | 15,230,000.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.93` | 15,290,000.00 USD | 15,290,000.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.95` | 15,380,000.00 USD | 15,380,000.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.97` | 15,430,000.00 USD | 15,430,000.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.99` | 15,450,000.00 USD | 15,450,000.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.01` | 15,460,000.00 USD | 15,460,000.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.03` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.09` | 113.76 USD | 419,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.15` | 22,320.00 USD | 441,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.21` | 7,330.00 USD | 448,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.23` | 114.12 USD | 448,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 3,380.00 USD | 452,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 452,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.70` | 37,030.00 USD | 489,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.71` | 218.91 USD | 489,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.96` | 1,920.00 USD | 491,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 498,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,810.00 USD | 510,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.47` | 720.29 USD | 511,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 523,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.70` | 778.89 USD | 524,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.81` | 59,080.00 USD | 583,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.04` | 1,370.00 USD | 584,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 586,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 586,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.68` | 432.22 USD | 587,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.76` | 36,730.00 USD | 624,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.79` | 953.38 USD | 624,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 102.68 USD | 625,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.97` | 14,530.00 USD | 639,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 727,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 234,840.00 USD | 962,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 966,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 966,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 966,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.14` | 164.79 USD | 966,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.43` | 4,000.00 USD | 970,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.62` | 288.35 USD | 971,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 972,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.84` | 243.44 USD | 972,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.86` | 2,470.00 USD | 974,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 322.06 USD | 975,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 975,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 975,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 995,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.49` | 154,950.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.74` | 111.95 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.29` | 263,950.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.46` | 22,620.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 84,520.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.77` | 340.87 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,710.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.46` | 101.47 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.62` | 4,120.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.64` | 4,930.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.66` | 2,660.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `2.33` | 326,540.00 USD | 0.00 USD | 611.73 USD | `-73.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 325,930.00 USD | 0.00 USD | 793.75 USD | `-54.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 325,130.00 USD | 0.00 USD | 105.04 USD | `-49.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 325,030.00 USD | 0.00 USD | 67,970.00 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 257,060.00 USD | 0.00 USD | 205.30 USD | `-40.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 256,860.00 USD | 0.00 USD | 465.42 USD | `-38.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 256,390.00 USD | 0.00 USD | 349.35 USD | `-37.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 256,040.00 USD | 0.00 USD | 1,330.00 USD | `-34.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 254,710.00 USD | 0.00 USD | 493.50 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 254,220.00 USD | 0.00 USD | 100.98 USD | `-32.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 254,120.00 USD | 0.00 USD | 620.80 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 253,500.00 USD | 0.00 USD | 4,160.00 USD | `-31.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 249,340.00 USD | 0.00 USD | 6,500.00 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 242,840.00 USD | 0.00 USD | 864.38 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 241,980.00 USD | 0.00 USD | 1,430.00 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 240,540.00 USD | 0.00 USD | 4,340.00 USD | `-26.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 236,200.00 USD | 0.00 USD | 5,520.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 230,680.00 USD | 0.00 USD | 100.72 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 230,580.00 USD | 0.00 USD | 296.34 USD | `-23.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 230,280.00 USD | 0.00 USD | 921.19 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 229,360.00 USD | 0.00 USD | 709.98 USD | `-22.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 228,650.00 USD | 0.00 USD | 262.44 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 228,390.00 USD | 0.00 USD | 3,610.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 224,780.00 USD | 0.00 USD | 6,790.00 USD | `-19.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 217,990.00 USD | 0.00 USD | 9,770.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 208,220.00 USD | 0.00 USD | 103.46 USD | `-18.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 208,120.00 USD | 0.00 USD | 603.44 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 207,510.00 USD | 0.00 USD | 891.57 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 206,620.00 USD | 0.00 USD | 2,300.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 204,320.00 USD | 0.00 USD | 129.58 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 204,190.00 USD | 0.00 USD | 236.19 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 203,950.00 USD | 0.00 USD | 199.39 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 203,750.00 USD | 0.00 USD | 4,730.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 199,020.00 USD | 0.00 USD | 37,420.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 161,600.00 USD | 0.00 USD | 778.49 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 160,820.00 USD | 0.00 USD | 799.83 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 160,020.00 USD | 0.00 USD | 103.41 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 159,910.00 USD | 0.00 USD | 1,370.00 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 158,540.00 USD | 0.00 USD | 360.13 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 158,180.00 USD | 0.00 USD | 578.04 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 157,600.00 USD | 0.00 USD | 175.42 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 157,430.00 USD | 0.00 USD | 2,990.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 154,430.00 USD | 0.00 USD | 143.51 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 154,290.00 USD | 0.00 USD | 183.33 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 154,100.00 USD | 0.00 USD | 194.52 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 153,910.00 USD | 0.00 USD | 394.75 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 153,520.00 USD | 0.00 USD | 1,350.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 152,170.00 USD | 0.00 USD | 1,590.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 150,580.00 USD | 0.00 USD | 898.42 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 149,690.00 USD | 0.00 USD | 1,350.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 148,340.00 USD | 0.00 USD | 7,400.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 140,940.00 USD | 0.00 USD | 123.58 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 140,820.00 USD | 0.00 USD | 2,110.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 138,710.00 USD | 0.00 USD | 563.85 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 138,140.00 USD | 0.00 USD | 105.14 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 138,040.00 USD | 0.00 USD | 367.76 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 137,670.00 USD | 0.00 USD | 2,330.00 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 135,340.00 USD | 0.00 USD | 184.13 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 135,150.00 USD | 0.00 USD | 6,500.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 128,650.00 USD | 0.00 USD | 462.15 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 128,190.00 USD | 0.00 USD | 654.53 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 127,530.00 USD | 0.00 USD | 367.91 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 127,170.00 USD | 0.00 USD | 520.75 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 126,650.00 USD | 0.00 USD | 2,900.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 123,740.00 USD | 0.00 USD | 141.04 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 123,600.00 USD | 0.00 USD | 1,780.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 121,820.00 USD | 0.00 USD | 515.66 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 121,300.00 USD | 0.00 USD | 143.54 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 121,160.00 USD | 0.00 USD | 168.64 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 120,990.00 USD | 0.00 USD | 201.49 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 120,790.00 USD | 0.00 USD | 6,530.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 114,260.00 USD | 0.00 USD | 1,140.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 113,120.00 USD | 0.00 USD | 2,000.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 111,110.00 USD | 0.00 USD | 756.06 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 110,360.00 USD | 0.00 USD | 970.35 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 109,390.00 USD | 0.00 USD | 5,470.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 103,920.00 USD | 0.00 USD | 1,970.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 101,950.00 USD | 0.00 USD | 3,290.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 98,670.00 USD | 0.00 USD | 358.56 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 98,310.00 USD | 0.00 USD | 1,880.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 96,430.00 USD | 0.00 USD | 140.36 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 96,290.00 USD | 0.00 USD | 138.24 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 96,150.00 USD | 0.00 USD | 954.23 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 95,190.00 USD | 0.00 USD | 769.61 USD | `-4.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 94,420.00 USD | 0.00 USD | 489.58 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 93,930.00 USD | 0.00 USD | 1,440.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 92,490.00 USD | 0.00 USD | 198.74 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 92,290.00 USD | 0.00 USD | 1,130.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 91,170.00 USD | 0.00 USD | 132.45 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 91,030.00 USD | 0.00 USD | 428.58 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 90,600.00 USD | 0.00 USD | 2,500.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 88,100.00 USD | 0.00 USD | 435.59 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 87,670.00 USD | 0.00 USD | 1,080.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 86,590.00 USD | 0.00 USD | 1,980.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 84,610.00 USD | 0.00 USD | 2,740.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 81,870.00 USD | 0.00 USD | 103.19 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 81,760.00 USD | 0.00 USD | 103.31 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 81,660.00 USD | 0.00 USD | 1,900.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 79,760.00 USD | 0.00 USD | 196.87 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 79,560.00 USD | 0.00 USD | 223.82 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 79,340.00 USD | 0.00 USD | 990.09 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 78,350.00 USD | 0.00 USD | 5,010.00 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 73,330.00 USD | 0.00 USD | 6,880.00 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 66,450.00 USD | 0.00 USD | 134.30 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 66,320.00 USD | 0.00 USD | 390.88 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 65,930.00 USD | 0.00 USD | 1,390.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 64,540.00 USD | 0.00 USD | 933.70 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 63,600.00 USD | 0.00 USD | 6,300.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 57,300.00 USD | 0.00 USD | 39,810.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 17,490.00 USD | 0.00 USD | 114.25 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 17,380.00 USD | 0.00 USD | 4,230.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 13,150.00 USD | 0.00 USD | 2,650.00 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 10,510.00 USD | 0.00 USD | 1,760.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 8,750.00 USD | 0.00 USD | 705.20 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 8,040.00 USD | 0.00 USD | 2,030.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 6,010.00 USD | 0.00 USD | 243.40 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 5,760.00 USD | 0.00 USD | 5,760.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 192.86 USD | 192.86 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 807.74 USD | 614.88 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 1,350.00 USD | 543.33 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 2,460.00 USD | 1,100.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 2,640.00 USD | 188.66 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 3,430.00 USD | 788.72 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 6,790.00 USD | 3,360.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 6,900.00 USD | 110.58 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 7,920.00 USD | 1,020.00 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 8,140.00 USD | 223.62 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 8,280.00 USD | 137.73 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 8,680.00 USD | 401.63 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 323,830.00 USD | 315,150.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 323,940.00 USD | 104.59 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 324,720.00 USD | 776.54 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 325,250.00 USD | 531.20 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 326,620.00 USD | 1,380.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 327,710.00 USD | 1,090.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 328,330.00 USD | 616.37 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 328,430.00 USD | 102.03 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 328,880.00 USD | 453.84 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 329,040.00 USD | 160.99 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 329,460.00 USD | 415.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 330,970.00 USD | 1,510.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 333,010.00 USD | 2,040.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 560,640.00 USD | 227,630.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 563,680.00 USD | 3,030.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 565,680.00 USD | 2,000.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 959,890.00 USD | 394,210.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 999,020.00 USD | 39,130.00 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,000,000.00 USD | 1,590.00 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,000,000.00 USD | 3,320.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,000,000.00 USD | 131.87 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,000,000.00 USD | 687.91 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,010,000.00 USD | 954.71 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,400,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,400,000.00 USD | 205.87 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `9.40` | 1,760,000.00 USD | 2,480.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,760,000.00 USD | 1,110.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,760,000.00 USD | 219.84 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,760,000.00 USD | 140.35 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,760,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,770,000.00 USD | 1,780.00 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,770,000.00 USD | 2,210.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,770,000.00 USD | 288.46 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,770,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,770,000.00 USD | 103.54 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,770,000.00 USD | 535.35 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,770,000.00 USD | 231.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,770,000.00 USD | 221.07 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,770,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,770,000.00 USD | 148.48 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,770,000.00 USD | 329.43 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,770,000.00 USD | 446.58 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,770,000.00 USD | 108.21 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,770,000.00 USD | 169.68 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,770,000.00 USD | 121.87 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,770,000.00 USD | 619.28 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,780,000.00 USD | 5,030.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,780,000.00 USD | 340.05 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,780,000.00 USD | 742.12 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,780,000.00 USD | 899.47 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,850,000.00 USD | 70,020.00 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,850,000.00 USD | 373.97 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `10.51` | 2,080,000.00 USD | 312.31 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,080,000.00 USD | 1,530.00 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,080,000.00 USD | 178.46 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,080,000.00 USD | 153.11 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,080,000.00 USD | 173.42 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,080,000.00 USD | 184.75 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,080,000.00 USD | 135.78 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,080,000.00 USD | 127.96 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,080,000.00 USD | 476.43 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,090,000.00 USD | 118.97 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,090,000.00 USD | 251.06 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,090,000.00 USD | 552.44 USD | 0.00 USD | `+23.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,090,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,090,000.00 USD | 320.29 USD | 0.00 USD | `+25.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,090,000.00 USD | 1,100.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,090,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,090,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,100,000.00 USD | 2,410.00 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,110,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,110,000.00 USD | 3,530.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,120,000.00 USD | 7,700.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,120,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,120,000.00 USD | 434.61 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,120,000.00 USD | 163.52 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,240,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,250,000.00 USD | 2,770.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,250,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,250,000.00 USD | 197.97 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,250,000.00 USD | 3,200.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,250,000.00 USD | 179.58 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,250,000.00 USD | 720.74 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,260,000.00 USD | 504.17 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,260,000.00 USD | 169.57 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,260,000.00 USD | 159.66 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,260,000.00 USD | 446.52 USD | 0.00 USD | `+51.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,260,000.00 USD | 1,710.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,260,000.00 USD | 5,320.00 USD | 0.00 USD | `+52.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,470,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,470,000.00 USD | 407.95 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,470,000.00 USD | 174.91 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,480,000.00 USD | 9,230.00 USD | 0.00 USD | `+58.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,480,000.00 USD | 960.26 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,480,000.00 USD | 2,710.00 USD | 0.00 USD | `+62.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,490,000.00 USD | 805.90 USD | 0.00 USD | `+63.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,490,000.00 USD | 655.55 USD | 0.00 USD | `+66.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,490,000.00 USD | 4,890.00 USD | 0.00 USD | `+67.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,490,000.00 USD | 471.09 USD | 0.00 USD | `+68.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,490,000.00 USD | 383.85 USD | 0.00 USD | `+69.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,140,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,140,000.00 USD | 111.87 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,140,000.00 USD | 219.91 USD | 0.00 USD | `+80.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,140,000.00 USD | 121.74 USD | 0.00 USD | `+91.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,140,000.00 USD | 297.59 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,150,000.00 USD | 4,500.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,270,000.00 USD | 120,270.00 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,270,000.00 USD | 122.39 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,270,000.00 USD | 586.59 USD | 0.00 USD | `+97.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,270,000.00 USD | 580.97 USD | 0.00 USD | `+98.91%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.81` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 16,260.00 USD | 16,110.00 USD | 0.00 USD |
| `7D` | `7.83` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD |
| `7D` | `7.85` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD |
| `7D` | `7.87` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD |
| `7D` | `7.89` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,180.00 USD |
| `7D` | `7.91` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD |
| `1D` | `7.92` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 16,360.00 USD | 2,950.00 USD | 11,950.00 USD |
| `1D` | `7.93` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD |
| `7D` | `7.93` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.94` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD |
| `1D` | `7.95` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 74.90 USD | 5,170.00 USD | 5,220.00 USD |
| `7D` | `7.95` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD |
| `1D` | `7.96` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 2,760.00 USD | 3,170.00 USD | 13.70 USD |
| `1D` | `7.97` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 9,050.00 USD | 1,920.00 USD | 4,040.00 USD |
| `7D` | `7.97` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD |
| `1D` | `7.98` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `1D` | `7.99` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 482.38 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.99` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD |
| `1D` | `8.00` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `1D` | `8.01` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.01` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD |
| `1D` | `8.02` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD |
| `1D` | `8.03` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 8,600.00 USD | 1,540.00 USD | 288.16 USD |
| `7D` | `8.03` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD |
| `1D` | `8.04` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 9,860.00 USD | 0.00 USD | 6,190.00 USD |
| `1D` | `8.05` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 14,360.00 USD | 3,770.00 USD | 330.10 USD |
| `7D` | `8.05` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD |
| `1D` | `8.06` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 12,030.00 USD | 1,700.00 USD | 5,880.00 USD |
| `1D` | `8.07` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 1,100.00 USD | 2,400.00 USD | 1,530.00 USD |
| `7D` | `8.07` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD |
| `1D` | `8.08` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 4,580.00 USD | 1,410.00 USD | 3,220.00 USD |
| `1D` | `8.09` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 9,480.00 USD | 1,220.00 USD | 4,600.00 USD |
| `7D` | `8.09` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD |
| `1D` | `8.10` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 9,530.00 USD | 2,720.00 USD | 6,270.00 USD |
| `1D` | `8.11` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD |
| `7D` | `8.11` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD |
| `1D` | `8.12` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD |
| `1D` | `8.13` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD |
| `7D` | `8.13` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD |
| `1D` | `8.14` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD |
| `1D` | `8.15` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD |
| `7D` | `8.15` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD |
| `1D` | `8.16` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD |
| `1D` | `8.17` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD |
| `7D` | `8.17` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 6,560.00 USD | 7,770.00 USD | 9,880.00 USD |
| `1D` | `8.18` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD |
| `1D` | `8.19` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD |
| `7D` | `8.19` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD |
| `1D` | `8.20` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 7,720.00 USD | 2,310.00 USD | 445.22 USD |
| `1D` | `8.21` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.21` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD |
| `1D` | `8.22` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD |
| `1D` | `8.23` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 20,920.00 USD | 4,080.00 USD | 31,000.00 USD |
| `7D` | `8.23` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD |
| `1D` | `8.24` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD |
| `1D` | `8.25` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 8,080.00 USD | 0.00 USD | 6,100.00 USD |
| `7D` | `8.25` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD |
| `1D` | `8.26` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 215.69 USD | 11,460.00 USD | 0.00 USD |
| `1D` | `8.27` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD |
| `7D` | `8.27` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,190.00 USD |
| `1D` | `8.28` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD |
| `1D` | `8.29` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 34,850.00 USD | 9,470.00 USD | 4,640.00 USD |
| `7D` | `8.29` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD |
| `1D` | `8.30` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD |
| `1D` | `8.31` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD |
| `7D` | `8.31` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD |
| `1D` | `8.32` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 19,380.00 USD | 4,190.00 USD | 7,320.00 USD |
| `1D` | `8.33` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD |
| `7D` | `8.33` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD |
| `1D` | `8.34` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD |
| `1D` | `8.35` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,090.00 USD |
| `7D` | `8.35` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD |
| `1D` | `8.36` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 4,090.00 USD | 2,420.00 USD | 21,790.00 USD |
| `1D` | `8.37` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,330.00 USD |
| `7D` | `8.37` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD |
| `1D` | `8.38` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 35,960.00 USD | 4,080.00 USD | 33,870.00 USD |
| `1D` | `8.39` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 63,220.00 USD | 10,540.00 USD | 56,430.00 USD |
| `7D` | `8.39` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 197,900.00 USD | 8,930.00 USD | 68,930.00 USD |
| `1D` | `8.40` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 67,650.00 USD | 22,890.00 USD | 68,000.00 USD |
| `1D` | `8.41` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 33,220.00 USD | 3,620.00 USD | 20,930.00 USD |
| `7D` | `8.41` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 122,320.00 USD | 32,690.00 USD | 244,940.00 USD |
| `1D` | `8.42` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 33,600.00 USD | 12,790.00 USD | 18,430.00 USD |
| `1D` | `8.43` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 29,980.00 USD | 34,530.00 USD | 14,410.00 USD |
| `7D` | `8.43` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 179,770.00 USD | 62,350.00 USD | 73,050.00 USD |
| `1D` | `8.44` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 35,570.00 USD | 8,900.00 USD | 5,560.00 USD |
| `1D` | `8.45` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 73,020.00 USD | 17,050.00 USD | 49,380.00 USD |
| `7D` | `8.45` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 210,670.00 USD | 59,180.00 USD | 89,430.00 USD |
| `1D` | `8.46` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 153,340.00 USD | 17,770.00 USD | 49,320.00 USD |
| `1D` | `8.47` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 120,680.00 USD | 30,070.00 USD | 19,220.00 USD |
| `7D` | `8.47` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 426,960.00 USD | 70,760.00 USD | 200,480.00 USD |
| `1D` | `8.48` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 126,360.00 USD | 39,180.00 USD | 53,230.00 USD |
| `1D` | `8.49` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 140,860.00 USD | 36,190.00 USD | 7,700.00 USD |
| `7D` | `8.49` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 283,720.00 USD | 54,550.00 USD | 118,450.00 USD |
| `1D` | `8.50` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 64,670.00 USD | 12,970.00 USD | 28,360.00 USD |
| `1D` | `8.51` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 16,530.00 USD | 48,100.00 USD | 21,930.00 USD |
| `7D` | `8.51` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD |
| `1D` | `8.52` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 48,940.00 USD | 17,250.00 USD | 23,600.00 USD |
| `1D` | `8.53` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 17,100.00 USD | 29,630.00 USD | 41,670.00 USD |
| `7D` | `8.53` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD |
| `1D` | `8.54` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 19,100.00 USD | 6,040.00 USD | 43,590.00 USD |
| `1D` | `8.55` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD |
| `7D` | `8.55` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD |
| `1D` | `8.56` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD |
| `1D` | `8.57` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD |
| `7D` | `8.57` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,250.00 USD |
| `1D` | `8.58` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD |
| `1D` | `8.59` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD |
| `7D` | `8.59` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD |
| `1D` | `8.60` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD |
| `1D` | `8.61` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 35,340.00 USD | 12,770.00 USD | 15,710.00 USD |
| `7D` | `8.61` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD |
| `1D` | `8.62` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 102,610.00 USD | 23,160.00 USD | 30,620.00 USD |
| `1D` | `8.63` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 77,860.00 USD | 21,050.00 USD | 12,350.00 USD |
| `7D` | `8.63` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD |
| `1D` | `8.64` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 105,620.00 USD | 11,790.00 USD | 19,190.00 USD |
| `1D` | `8.65` | 954,100.00 USD | 0.00 USD | 954,100.00 USD | 50,810.00 USD | 31,510.00 USD | 33,100.00 USD |
| `7D` | `8.65` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD |
| `1D` | `8.66` | 838,680.00 USD | 0.00 USD | 838,680.00 USD | 74,110.00 USD | 26,760.00 USD | 15,000.00 USD |
| `1D` | `8.67` | 722,810.00 USD | 0.00 USD | 722,810.00 USD | 59,230.00 USD | 9,170.00 USD | 27,430.00 USD |
| `7D` | `8.67` | 772,830.00 USD | 0.00 USD | 772,830.00 USD | 77,920.00 USD | 24,870.00 USD | 173,920.00 USD |
| `1D` | `8.68` | 626,980.00 USD | 0.00 USD | 626,980.00 USD | 39,990.00 USD | 5,900.00 USD | 4,570.00 USD |
| `1D` | `8.69` | 576,510.00 USD | 0.00 USD | 576,510.00 USD | 18,040.00 USD | 5,700.00 USD | 22,180.00 USD |
| `7D` | `8.69` | 496,130.00 USD | 0.00 USD | 496,130.00 USD | 70,550.00 USD | 12,790.00 USD | 22,560.00 USD |
| `1D` | `8.70` | 530,590.00 USD | 0.00 USD | 530,590.00 USD | 34,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.71` | 496,220.00 USD | 0.00 USD | 496,220.00 USD | 18,250.00 USD | 11,690.00 USD | 18,980.00 USD |
| `1D` | `8.73` | 447,300.00 USD | 0.00 USD | 447,300.00 USD | 44,990.00 USD | 2,720.00 USD | 5,120.00 USD |
| `1D` | `8.74` | 394,470.00 USD | 0.00 USD | 394,470.00 USD | 0.00 USD | 7,720.00 USD | 0.00 USD |
| `1D` | `8.75` | 386,750.00 USD | 0.00 USD | 386,750.00 USD | 32,080.00 USD | 8,290.00 USD | 35,830.00 USD |
| `7D` | `8.75` | 390,230.00 USD | 0.00 USD | 390,230.00 USD | 144,660.00 USD | 19,690.00 USD | 56,610.00 USD |
| `1D` | `8.76` | 310,550.00 USD | 0.00 USD | 310,550.00 USD | 78,530.00 USD | 15,050.00 USD | 0.00 USD |
| `1D` | `8.77` | 216,980.00 USD | 0.00 USD | 216,980.00 USD | 54,300.00 USD | 8,510.00 USD | 25,720.00 USD |
| `7D` | `8.77` | 169,270.00 USD | 0.00 USD | 169,270.00 USD | 26,810.00 USD | 0.00 USD | 81,240.00 USD |
| `1D` | `8.78` | 128,450.00 USD | 0.00 USD | 128,450.00 USD | 19,230.00 USD | 0.00 USD | 9,880.00 USD |
| `1D` | `8.79` | 99,340.00 USD | 0.00 USD | 99,340.00 USD | 13,010.00 USD | 12,000.00 USD | 0.00 USD |
| `7D` | `8.79` | 61,220.00 USD | 0.00 USD | 61,220.00 USD | 27,360.00 USD | 25,300.00 USD | 0.00 USD |
| `1D` | `8.80` | 74,330.00 USD | 0.00 USD | 74,330.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `8.81` | 8,570.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | 8,450.00 USD | 118.36 USD |
| `1D` | `8.84` | 68,640.00 USD | 0.00 USD | 68,640.00 USD | 0.00 USD | 0.00 USD | 68,640.00 USD |
| `1D` | `8.85` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.85` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.89` | 44,480.00 USD | 44,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,480.00 USD |
| `1D` | `8.90` | 77,770.00 USD | 77,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,770.00 USD |
| `7D` | `8.91` | 115,480.00 USD | 115,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 71,000.00 USD |
| `1D` | `8.92` | 89,330.00 USD | 89,330.00 USD | 0.00 USD | 8,060.00 USD | 0.00 USD | 3,500.00 USD |
| `1D` | `8.98` | 102,370.00 USD | 102,370.00 USD | 0.00 USD | 0.00 USD | 5,550.00 USD | 7,490.00 USD |
| `1D` | `8.99` | 176,380.00 USD | 176,380.00 USD | 0.00 USD | 40,450.00 USD | 30,520.00 USD | 3,040.00 USD |
| `7D` | `8.99` | 209,720.00 USD | 209,720.00 USD | 0.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.00` | 221,430.00 USD | 221,430.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 8,090.00 USD |
| `1D` | `9.01` | 241,530.00 USD | 241,530.00 USD | 0.00 USD | 1,080.00 USD | 5,120.00 USD | 13,910.00 USD |
| `7D` | `9.01` | 451,940.00 USD | 451,940.00 USD | 0.00 USD | 185,270.00 USD | 36,180.00 USD | 20,780.00 USD |
| `1D` | `9.02` | 315,350.00 USD | 315,350.00 USD | 0.00 USD | 38,060.00 USD | 30,950.00 USD | 4,810.00 USD |
| `1D` | `9.03` | 429,270.00 USD | 429,270.00 USD | 0.00 USD | 54,730.00 USD | 31,750.00 USD | 27,430.00 USD |
| `7D` | `9.03` | 626,990.00 USD | 626,990.00 USD | 0.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD |
| `1D` | `9.04` | 470,090.00 USD | 470,090.00 USD | 0.00 USD | 18,960.00 USD | 10,710.00 USD | 11,160.00 USD |
| `1D` | `9.05` | 538,390.00 USD | 538,390.00 USD | 0.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD |
| `7D` | `9.05` | 719,540.00 USD | 719,540.00 USD | 0.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD |
| `1D` | `9.06` | 589,720.00 USD | 589,720.00 USD | 0.00 USD | 27,120.00 USD | 2,420.00 USD | 21,790.00 USD |
| `1D` | `9.07` | 653,730.00 USD | 653,730.00 USD | 0.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD |
| `7D` | `9.07` | 759,900.00 USD | 759,900.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD |
| `1D` | `9.08` | 695,350.00 USD | 695,350.00 USD | 0.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD |
| `1D` | `9.09` | 853,910.00 USD | 853,910.00 USD | 0.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD |
| `7D` | `9.09` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD |
| `1D` | `9.10` | 949,220.00 USD | 949,220.00 USD | 0.00 USD | 66,840.00 USD | 22,440.00 USD | 6,030.00 USD |
| `1D` | `9.11` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD |
| `7D` | `9.11` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD |
| `1D` | `9.12` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD |
| `1D` | `9.13` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD |
| `7D` | `9.13` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.14` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD |
| `1D` | `9.15` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 57,880.00 USD | 22,150.00 USD | 22,630.00 USD |
| `7D` | `9.15` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD |
| `1D` | `9.16` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 63,210.00 USD | 18,910.00 USD | 29,260.00 USD |
| `1D` | `9.17` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 107,540.00 USD | 18,740.00 USD | 50,980.00 USD |
| `7D` | `9.17` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD |
| `1D` | `9.18` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 80,310.00 USD | 35,050.00 USD | 56,150.00 USD |
| `1D` | `9.19` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 97,890.00 USD | 40,200.00 USD | 17,030.00 USD |
| `7D` | `9.19` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 503,250.00 USD | 101,150.00 USD | 193,560.00 USD |
| `1D` | `9.20` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 119,740.00 USD | 12,660.00 USD | 67,770.00 USD |
| `1D` | `9.21` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 48,600.00 USD | 6,420.00 USD | 9,160.00 USD |
| `7D` | `9.21` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 554,780.00 USD | 132,850.00 USD | 277,380.00 USD |
| `1D` | `9.22` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD |
| `1D` | `9.23` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 57,020.00 USD | 3,310.00 USD | 33,950.00 USD |
| `7D` | `9.23` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD |
| `1D` | `9.24` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 31,050.00 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `9.25` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD |
| `1D` | `9.26` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 16,250.00 USD | 1,210.00 USD | 0.00 USD |
| `1D` | `9.27` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD |
| `7D` | `9.27` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD |
| `1D` | `9.28` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 20,250.00 USD | 3,860.00 USD | 27.40 USD |
| `1D` | `9.29` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 48,970.00 USD | 15,680.00 USD | 17,930.00 USD |
| `7D` | `9.29` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD |
| `1D` | `9.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 42,450.00 USD | 9,410.00 USD | 26.83 USD |
| `1D` | `9.31` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 27,590.00 USD | 4,250.00 USD | 25,510.00 USD |
| `7D` | `9.31` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD |
| `1D` | `9.32` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 9,610.00 USD | 2,530.00 USD | 10,830.00 USD |
| `1D` | `9.33` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 7,010.00 USD | 6,000.00 USD | 4,480.00 USD |
| `7D` | `9.33` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD |
| `1D` | `9.34` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD |
| `1D` | `9.35` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 28,980.00 USD | 3,810.00 USD | 20,530.00 USD |
| `7D` | `9.35` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 289,480.00 USD | 88,340.00 USD | 96,160.00 USD |
| `1D` | `9.36` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 30,450.00 USD | 11,070.00 USD | 20,570.00 USD |
| `1D` | `9.37` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 36,610.00 USD | 13,410.00 USD | 6,010.00 USD |
| `7D` | `9.37` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD |
| `1D` | `9.38` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 47,540.00 USD | 4,040.00 USD | 27,030.00 USD |
| `1D` | `9.39` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 16,910.00 USD | 1,730.00 USD | 3,240.00 USD |
| `7D` | `9.39` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD |
| `1D` | `9.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD |
| `1D` | `9.41` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 29,300.00 USD | 1,660.00 USD | 16,970.00 USD |
| `7D` | `9.41` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD |
| `1D` | `9.42` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 10,620.00 USD | 622.99 USD | 4,010.00 USD |
| `1D` | `9.43` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 10,160.00 USD | 6,940.00 USD | 12,410.00 USD |
| `7D` | `9.43` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD |
| `1D` | `9.44` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.45` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD |
| `7D` | `9.45` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD |
| `1D` | `9.46` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD |
| `1D` | `9.47` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 18,220.00 USD | 6,870.00 USD | 192.20 USD |
| `7D` | `9.47` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD |
| `1D` | `9.48` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD |
| `1D` | `9.49` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD |
| `7D` | `9.49` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD |
| `1D` | `9.50` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD |
| `1D` | `9.51` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 295.05 USD | 0.00 USD | 124.70 USD |
| `7D` | `9.51` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD |
| `1D` | `9.52` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 17,180.00 USD | 3,070.00 USD | 5,400.00 USD |
| `1D` | `9.53` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD |
| `7D` | `9.53` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD |
| `1D` | `9.54` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD |
| `1D` | `9.55` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD |
| `7D` | `9.55` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 28,850.00 USD | 17,400.00 USD | 880.26 USD |
| `1D` | `9.56` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 4,750.00 USD | 1,280.00 USD | 2,530.00 USD |
| `1D` | `9.57` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 1,370.00 USD | 3,100.00 USD | 4,950.00 USD |
| `7D` | `9.57` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD |
| `1D` | `9.58` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 1,110.00 USD | 563.17 USD | 7,730.00 USD |
| `1D` | `9.59` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 4,830.00 USD | 1,250.00 USD | 1,140.00 USD |
| `7D` | `9.59` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 26,920.00 USD | 15,650.00 USD | 23,150.00 USD |
| `1D` | `9.60` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD |
| `1D` | `9.61` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `7D` | `9.61` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD |
| `1D` | `9.62` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.63` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD |
| `7D` | `9.63` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD |
| `1D` | `9.64` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD |
| `1D` | `9.65` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD |
| `7D` | `9.65` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 33,020.00 USD | 20,230.00 USD | 18,150.00 USD |
| `1D` | `9.66` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD |
| `1D` | `9.67` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `9.67` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD |
| `1D` | `9.68` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD |
| `1D` | `9.69` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD |
| `7D` | `9.69` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD |
| `1D` | `9.70` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD |
| `1D` | `9.71` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 74.90 USD | 5,170.00 USD | 5,250.00 USD |
| `7D` | `9.71` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD |
| `1D` | `9.72` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 2,760.00 USD | 3,170.00 USD | 57.27 USD |
| `7D` | `9.73` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD |
| `1D` | `9.74` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 5,260.00 USD | 738.05 USD | 3,140.00 USD |
| `1D` | `9.75` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 3,790.00 USD | 1,180.00 USD | 946.22 USD |
| `7D` | `9.75` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD |
| `1D` | `9.76` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `9.77` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD |
| `1D` | `9.78` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 1,840.00 USD | 1,790.00 USD |
| `1D` | `9.79` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.79` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD |
| `7D` | `9.81` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 103,830.00 USD | 23,930.00 USD | 48,290.00 USD |
| `7D` | `9.83` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD |
| `7D` | `9.85` | 15,050,000.00 USD | 15,050,000.00 USD | 0.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD |
| `7D` | `9.87` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD |
| `7D` | `9.89` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD |
| `7D` | `9.91` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD |
| `7D` | `9.93` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD |
| `7D` | `9.95` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD |
| `7D` | `9.97` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD |
| `7D` | `9.99` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD |
| `7D` | `10.01` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD |
| `7D` | `10.03` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `382.49M` | Total OI Tokens: `43,225,852.1 AVAX`
  * 1h OI Change: `+0.03%` | 4h OI Change: `-1.04%` | 24h OI Change: `-2.95%`
  * Exchange Breakdown: Binance=`89.71M` | Bybit=`59.52M` | OKX=`12.73M` | Hyperliquid=`17.60M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.52K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0045%` | **USDT KuCoin** | `0.0099%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0041%` | **USDT Bitget** | `0.0098%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `38.51%` | `61.49%` | `0.63` | 563,030.00 USD |
| `15M` | `Binance` | `33.66%` | `66.34%` | `0.51` | 230,670.00 USD |
| `15M` | `OKX` | `32.67%` | `67.33%` | `0.49` | 47,910.00 USD |
| `15M` | `Bybit` | `96.13%` | `3.87%` | `24.84` | 39,550.00 USD |
| `15M` | `KuCoin` | `41.07%` | `58.93%` | `0.70` | 12,430.00 USD |
| `15M` | `Gate` | `62.95%` | `37.05%` | `1.70` | 39,540.00 USD |
| `15M` | `Bitget` | `68.03%` | `31.97%` | `2.13` | 844.99 USD |
| `15M` | `BingX` | `52%` | `48%` | `1.08` | 34,300.00 USD |
| `15M` | `MEXC` | `57.76%` | `42.24%` | `1.37` | 4,020.00 USD |
| `15M` | `Bitunix` | `35.24%` | `64.76%` | `0.54` | 6,580.00 USD |
| `15M` | `Hyperliquid` | `18.01%` | `81.99%` | `0.22` | 1,870.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41.28%` | `58.72%` | `0.70` | 37,950.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `5.13%` | `94.87%` | `0.05` | 73,180.00 USD |
| `15M` | `HTX` | `57.22%` | `42.78%` | `1.34` | 12,500.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `42.92%` | `57.08%` | `0.75` | 2,020.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 17.90 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.7%` | `76.3%` | `0.31` | 19,660.00 USD |
| `15M` | `Whale Positions` | `33.66%` | `66.34%` | `0.51` | 230,670.00 USD |
| `15M` | `Global Accounts` | `38.51%` | `61.49%` | `0.63` | 563,030.00 USD |
| `1H` | `AVAX` | `46.18%` | `53.82%` | `0.86` | 2,440,000.00 USD |
| `1H` | `Binance` | `56.69%` | `43.31%` | `1.31` | 723,050.00 USD |
| `1H` | `OKX` | `67.57%` | `32.43%` | `2.08` | 158,890.00 USD |
| `1H` | `Bybit` | `60.77%` | `39.23%` | `1.55` | 133,180.00 USD |
| `1H` | `KuCoin` | `66.07%` | `33.93%` | `1.95` | 60,990.00 USD |
| `1H` | `Gate` | `59.47%` | `40.53%` | `1.47` | 86,980.00 USD |
| `1H` | `Bitget` | `70.66%` | `29.34%` | `2.41` | 11,410.00 USD |
| `1H` | `BingX` | `42.22%` | `57.78%` | `0.73` | 324,410.00 USD |
| `1H` | `MEXC` | `49.41%` | `50.59%` | `0.98` | 15,800.00 USD |
| `1H` | `Bitunix` | `60.04%` | `39.96%` | `1.50` | 19,980.00 USD |
| `1H` | `Hyperliquid` | `64.78%` | `35.22%` | `1.84` | 15,050.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.8%` | `50.2%` | `0.99` | 389,690.00 USD |
| `1H` | `Crypto.com` | `99.57%` | `0.43%` | `231.56` | 0.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 395,920.00 USD |
| `1H` | `HTX` | `46.05%` | `53.95%` | `0.85` | 50,150.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `90.16%` | `9.84%` | `9.16` | 6,610.00 USD |
| `1H` | `Aster` | `97.35%` | `2.65%` | `36.74` | 607.64 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.86%` | `52.14%` | `0.92` | 49,790.00 USD |
| `1H` | `Whale Positions` | `56.69%` | `43.31%` | `1.31` | 723,050.00 USD |
| `1H` | `Global Accounts` | `46.18%` | `53.82%` | `0.86` | 2,440,000.00 USD |
| `4H` | `AVAX` | `43.24%` | `56.76%` | `0.76` | 73,410,000.00 USD |
| `4H` | `Binance` | `44.66%` | `55.34%` | `0.81` | 22,440,000.00 USD |
| `4H` | `OKX` | `43.09%` | `56.91%` | `0.76` | 5,120,000.00 USD |
| `4H` | `Bybit` | `49.2%` | `50.8%` | `0.97` | 3,880,000.00 USD |
| `4H` | `KuCoin` | `46.56%` | `53.44%` | `0.87` | 584,120.00 USD |
| `4H` | `Gate` | `50.63%` | `49.37%` | `1.03` | 1,350,000.00 USD |
| `4H` | `Bitget` | `43.68%` | `56.32%` | `0.78` | 1,330,000.00 USD |
| `4H` | `BingX` | `44.89%` | `55.11%` | `0.81` | 14,710,000.00 USD |
| `4H` | `MEXC` | `51.8%` | `48.2%` | `1.07` | 4,110,000.00 USD |
| `4H` | `Bitunix` | `50.94%` | `49.06%` | `1.04` | 2,790,000.00 USD |
| `4H` | `Hyperliquid` | `35.61%` | `64.39%` | `0.55` | 431,970.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.58%` | `49.42%` | `1.02` | 10,900,000.00 USD |
| `4H` | `Crypto.com` | `85.5%` | `14.5%` | `5.90` | 15,650.00 USD |
| `4H` | `WhiteBIT` | `0.06%` | `99.94%` | `0.00` | 5,280,000.00 USD |
| `4H` | `HTX` | `26.27%` | `73.73%` | `0.36` | 22,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.34%` | `48.66%` | `1.06` | 234,390.00 USD |
| `4H` | `Aster` | `52.05%` | `47.95%` | `1.09` | 124,850.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.3%` | `46.7%` | `1.14` | 63,660.00 USD |
| `4H` | `Whale Positions` | `44.66%` | `55.34%` | `0.81` | 22,440,000.00 USD |
| `4H` | `Global Accounts` | `43.24%` | `56.76%` | `0.76` | 73,410,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.94` | `8.90` | `8.94` | `8.94` | `8.85` | 1,871,719.04 USD | 766,811.36 USD | 1,104,907.68 USD | -338,096.31 USD | `-18.06%` | `8B / 28S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.82` | 1,418,137.84 USD | 651,843.02 USD | 766,294.83 USD | -114,451.81 USD | `-8.07%` | `11B / 12S` |
| `0:00 UTC` | `8.87` | `8.87` | `8.87` | `8.88` | `8.86` | 651,856.32 USD | 369,195.26 USD | 282,661.06 USD | 86,534.20 USD | `+13.28%` | `5B / 4S` |
| `5:00 UTC` | `8.84` | `8.86` | `8.84` | `8.89` | `8.84` | 682,076.12 USD | 288,770.26 USD | 393,305.86 USD | -104,535.61 USD | `-15.33%` | `9B / 13S` |
| `0:00 UTC` | `8.81` | `8.81` | `8.81` | `8.84` | `8.80` | 1,762,248.06 USD | 773,632.57 USD | 988,615.48 USD | -214,982.91 USD | `-12.20%` | `7B / 6S` |
| `5:00 UTC` | `8.84` | `8.83` | `8.84` | `8.86` | `8.79` | 750,878.19 USD | 458,225.53 USD | 292,652.66 USD | 165,572.87 USD | `+22.05%` | `19B / 3S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 637,816.13 USD | 328,825.06 USD | 308,991.07 USD | 19,833.99 USD | `+3.11%` | `4B / 4S` |
| `5:00 UTC` | `8.81` | `8.82` | `8.81` | `8.84` | `8.80` | 548,929.60 USD | 300,754.28 USD | 248,175.32 USD | 52,578.96 USD | `+9.58%` | `18B / 4S` |
| `0:00 UTC` | `8.86` | `8.86` | `8.86` | `8.87` | `8.83` | 587,148.06 USD | 393,702.30 USD | 193,445.76 USD | 200,256.54 USD | `+34.11%` | `5B / 1S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.84` | 429,446.19 USD | 188,441.02 USD | 241,005.17 USD | -52,564.14 USD | `-12.24%` | `8B / 6S` |

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
| `5m` | -102,370.00 USD | -620,030.00 USD | **`DISTRIBUTION`** |
| `15m` | -133,080.00 USD | -676,310.00 USD | **`DISTRIBUTION`** |
| `30m` | -148,900.00 USD | -594,240.00 USD | **`DISTRIBUTION`** |
| `1h` | -185,930.00 USD | -182,080.00 USD | **`DISTRIBUTION`** |
| `2h` | -130,570.00 USD | -119,340.00 USD | **`DISTRIBUTION`** |
| `4h` | -378,960.00 USD | -4,340,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 79,120.00 USD | -3,420,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -153,040.00 USD | -3,220,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -289,820.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -594,230.00 USD | -8,330,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,120,000.00 USD | -43,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -53,430,000.00 USD | -273,840,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-102.37K` | 15m=`-133.08K` | 1h=`-185.93K` | 24h=`-594.23K`
* Futures Capital Netflows: 5m=`-620.03K` | 15m=`-676.31K` | 1h=`-182.08K` | 24h=`-8.33M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `8.48` (Risk Distance: `0.1049` pts)
  * +2.5R Take Profit: `8.84`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.90` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.00` (Risk Distance: `0.1049` pts)
  * +2.5R Take Profit: `8.64`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.86`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
