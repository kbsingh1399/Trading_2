# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:20:51 IST` (`2026-10-29 19:50:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.83` | **Live Ask Quote**: `8.86` | **Mid Price**: `8.84`
- **Spread Points**: `3.00` | **Spread BPS**: `33.92 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.76` | VWAP Z-Score: `+0.39` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0531` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.49` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.13` | Lower -3.00σ Band: `8.39`
  * Upper +2.51σ Band: `9.07` | Lower -2.51σ Band: `8.45`
  * Upper +2.01σ Band: `9.01` | Lower -2.01σ Band: `8.52`
  * Upper +2.00σ Band: `9.01` | Lower -2.00σ Band: `8.52`
  * Upper +1.28σ Band: `8.92` | Lower -1.28σ Band: `8.61`
  * Upper +1.00σ Band: `8.88` | Lower -1.00σ Band: `8.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.83` | EMA-20=`8.84` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.82` (Slope: `+0.0000`) | EMA-100=`8.81`
  * Institutional Anchors: EMA-144=`8.82` | EMA-200=`8.82` (Slope: `+0.0349`) | EMA-233=`8.83`
- **Range Boundaries**: 24H High=`9.14` | 24H Low=`8.53` | Weekly High=`9.14` | Weekly Low=`8.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.91` (Distance: `-0.69%`)
  * Point of Control (POC) = `8.74` (Distance: `+1.20%`)
  * Value Area Low (VAL) = `8.58` (Distance: `+3.07%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `8.81` - `8.88`
  * Optimal Trade Entry (OTE 0.705): `8.86`
  * Structural Invalidation Anchor (0.786): `8.92`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.83` | `8.87` | `8.83` | `8.86` | `35,013` | 310,053.83 USD | 200,654.27 USD | `+64.72%` | -2,754,264.64 USD | `+2.84` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.86` | `8.86` | `8.85` | `8.85` | `19,114` | 169,216.74 USD | -57,006.76 USD | `-33.69%` | -2,811,271.39 USD | `-0.98` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.85` | `8.86` | `8.85` | `8.85` | `9,651` | 85,462.90 USD | 54,624.92 USD | `+63.92%` | -2,756,646.47 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.84` | `8.84` | `8.80` | `8.80` | `72,332` | 637,816.13 USD | 19,833.98 USD | `+3.11%` | -3,007,497.87 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.80` | `8.84` | `8.80` | `8.83` | `62,236` | 548,929.60 USD | 52,578.96 USD | `+9.58%` | -2,954,918.91 USD | `+0.49` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.83` | `8.87` | `8.83` | `8.85` | `63,778` | 564,733.47 USD | 198,272.44 USD | `+35.11%` | -2,756,646.47 USD | `+0.99` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.96` | `8.96` | `8.82` | `8.87` | `732,279` | 6,517,786.37 USD | -1,600,470.16 USD | `-24.56%` | -3,146,829.78 USD | `-2.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.87` | `8.89` | `8.79` | `8.84` | `435,467` | 3,847,058.68 USD | -67,411.45 USD | `-1.75%` | -3,214,241.23 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.84` | `8.87` | `8.80` | `8.85` | `198,340` | 1,751,426.09 USD | 270,738.50 USD | `+15.46%` | -2,943,502.73 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,206,528` | 19,674,606.03 USD | -2,463,247.05 USD | `-12.52%` | -2,943,555.84 USD | `-1.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `9.00` | `9.02` | `8.55` | `8.59` | `3,515,330` | 30,612,875.98 USD | -2,423,031.38 USD | `-7.92%` | -749,324.84 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -690,744.30 USD | `+0.17` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -426,486.82 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -480,308.79 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,206,528` | 19,674,606.03 USD | -2,463,247.05 USD | `-12.52%` | -2,943,555.84 USD | `-1.32` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.84`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID_SPREAD` | `8.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.85` | `0.00%` | `-` |
| `BID` | `8.85` | `26.2800` | 232.65 USD | 232.65 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.94 USD | 714.59 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `140.5300` | 1,244.06 USD | 1,958.65 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.93 USD | 2,440.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `16.0000` | 141.64 USD | 2,582.22 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.85` | `46.9400` | 415.50 USD | 2,997.71 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.88 USD | 3,479.60 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `50.0000` | 442.57 USD | 3,922.17 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `453.9300` | 4,017.92 USD | 7,940.09 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.85` | `455.2500` | 4,029.46 USD | 11,969.55 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.84 USD | 12,451.39 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.85` | `677.8800` | 5,999.71 USD | 18,451.10 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.85` | `136.6400` | 1,209.35 USD | 19,660.45 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.85` | `50.0000` | 442.50 USD | 20,102.95 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.79 USD | 20,584.73 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `50.0000` | 442.49 USD | 21,027.22 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `54.4400` | 481.78 USD | 21,509.00 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `35.2000` | 311.50 USD | 21,820.50 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.85` | `166.4900` | 1,473.32 USD | 23,293.82 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.85` | `904.0400` | 7,999.94 USD | 31,293.76 USD | `1 orders` | `-0.06%` | `-` |
| `ASK` | `8.86` | `214.5300` | 1,900.61 USD | 19,084.74 USD | `3 orders` | `+0.06%` | `-` |
| `ASK` | `8.86` | `92.4300` | 818.85 USD | 17,184.13 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `28.2400` | 250.18 USD | 16,365.29 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `211.2000` | 1,870.98 USD | 16,115.11 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `112.8800` | 999.96 USD | 14,244.13 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `46.0000` | 407.49 USD | 13,244.17 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `54.4500` | 482.33 USD | 12,836.68 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.86` | `213.1300` | 1,887.95 USD | 12,354.35 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `137.5600` | 1,218.49 USD | 10,466.40 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `91.7000` | 812.25 USD | 9,247.91 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `5.2800` | 46.77 USD | 8,435.66 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.86` | `167.3400` | 1,482.18 USD | 8,388.89 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `54.4300` | 482.10 USD | 6,906.71 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `246.0300` | 2,179.06 USD | 6,424.61 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `4.5100` | 39.94 USD | 4,245.55 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `102.7700` | 910.18 USD | 4,205.60 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `8.86` | `40.8200` | 361.51 USD | 3,295.42 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.86` | `20.8000` | 184.20 USD | 2,933.91 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.86` | `142.3800` | 1,260.89 USD | 2,749.71 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `8.86` | `168.1200` | 1,488.82 USD | 1,488.82 USD | `2 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1495` | `0x7737...bf66` | `SHORT` | 1,518,600.37 USD | `171,568.06` | `7.43` | `8.85` | `110.16` | -243,055.35 USD | `-16.01%` | `10X Cross` |
| `1570` | `0xeadc...9d55` | `LONG` | 1,417,088.66 USD | `160,070.56` | `8.11` | `8.85` | `0.000000` | 119,451.09 USD | `+8.43%` | `10X Cross` |

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
| `1D` | `Long Liquidation` | `7.92` | 5,220,000.00 USD | 5,220,000.00 USD | 16,360.00 USD | 2,950.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 923.42 USD | 440,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,190,000.00 USD | 5,190,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 9,450,000.00 USD | 9,450,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 439,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,180,000.00 USD | 5,180,000.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 437,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 5,160,000.00 USD | 5,160,000.00 USD | 74.90 USD | 5,170.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 9,350,000.00 USD | 9,350,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 310,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 5,150,000.00 USD | 5,150,000.00 USD | 2,760.00 USD | 3,170.00 USD | 13.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 5,140,000.00 USD | 5,140,000.00 USD | 9,050.00 USD | 1,180.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 9,250,000.00 USD | 9,250,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 5,130,000.00 USD | 5,130,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 309,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 5,120,000.00 USD | 5,120,000.00 USD | 482.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 9,160,000.00 USD | 9,160,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 307,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 5,120,000.00 USD | 5,120,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 5,120,000.00 USD | 5,120,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 9,060,000.00 USD | 9,060,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 5,110,000.00 USD | 5,110,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 307,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 5,100,000.00 USD | 5,100,000.00 USD | 8,600.00 USD | 1,540.00 USD | 288.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 8,990,000.00 USD | 8,990,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 306,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 5,090,000.00 USD | 5,090,000.00 USD | 9,860.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 218,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 5,070,000.00 USD | 5,070,000.00 USD | 14,360.00 USD | 3,770.00 USD | 330.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 8,810,000.00 USD | 8,810,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 211,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 5,050,000.00 USD | 5,050,000.00 USD | 12,030.00 USD | 1,700.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 208,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 5,030,000.00 USD | 5,030,000.00 USD | 1,100.00 USD | 2,400.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 8,680,000.00 USD | 8,680,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.08` | 5,030,000.00 USD | 5,030,000.00 USD | 4,700.00 USD | 1,410.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 170,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 5,020,000.00 USD | 5,020,000.00 USD | 9,630.00 USD | 1,220.00 USD | 6,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 8,530,000.00 USD | 8,530,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.10` | 165.46 USD | 169,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 5,000,000.00 USD | 5,000,000.00 USD | 23,830.00 USD | 3,750.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.11` | 11,550.00 USD | 169,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.11` | 4,970,000.00 USD | 4,970,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 8,450,000.00 USD | 8,450,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 157,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 4,960,000.00 USD | 4,960,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 4,940,000.00 USD | 4,940,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 8,400,000.00 USD | 8,400,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 4,930,000.00 USD | 4,930,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 4,910,000.00 USD | 4,910,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 8,330,000.00 USD | 8,330,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 4,890,000.00 USD | 4,890,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 157,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.17` | 4,890,000.00 USD | 4,890,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 8,190,000.00 USD | 8,190,000.00 USD | 6,560.00 USD | 7,770.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 4,890,000.00 USD | 4,890,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 4,890,000.00 USD | 4,890,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 8,170,000.00 USD | 8,170,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,290.00 USD | 156,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 4,880,000.00 USD | 4,880,000.00 USD | 7,720.00 USD | 2,310.00 USD | 445.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 155,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.21` | 4,870,000.00 USD | 4,870,000.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 8,130,000.00 USD | 8,130,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 153,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 4,870,000.00 USD | 4,870,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 153,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.23` | 4,850,000.00 USD | 4,850,000.00 USD | 20,920.00 USD | 4,080.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 8,100,000.00 USD | 8,100,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 151,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 4,790,000.00 USD | 4,790,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 150,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.25` | 4,780,000.00 USD | 4,780,000.00 USD | 8,080.00 USD | 0.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 7,970,000.00 USD | 7,970,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 148,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 4,760,000.00 USD | 4,760,000.00 USD | 215.69 USD | 11,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 4,750,000.00 USD | 4,750,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 7,900,000.00 USD | 7,900,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,860.00 USD | 135,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 4,740,000.00 USD | 4,740,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 125,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.29` | 4,620,000.00 USD | 4,620,000.00 USD | 34,850.00 USD | 9,470.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 7,820,000.00 USD | 7,820,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 124,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 4,570,000.00 USD | 4,570,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 105,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.31` | 4,480,000.00 USD | 4,480,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 7,630,000.00 USD | 7,630,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 72,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 4,410,000.00 USD | 4,410,000.00 USD | 19,380.00 USD | 4,190.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 4,380,000.00 USD | 4,380,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 7,530,000.00 USD | 7,530,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,630.00 USD | 67,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 4,350,000.00 USD | 4,350,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 4,320,000.00 USD | 4,320,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 7,410,000.00 USD | 7,410,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,410.00 USD | 63,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.36` | 4,290,000.00 USD | 4,290,000.00 USD | 4,090.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,160.00 USD | 59,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.37` | 4,260,000.00 USD | 4,260,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 7,230,000.00 USD | 7,230,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 3,410.00 USD | 52,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.38` | 4,220,000.00 USD | 4,220,000.00 USD | 36,140.00 USD | 4,080.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 1,870.00 USD | 49,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.39` | 4,150,000.00 USD | 4,150,000.00 USD | 63,440.00 USD | 10,540.00 USD | 56,460.00 USD | `Tier 1 CEX` |
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
| `1D` | `Long Liquidation` | `8.50` | 2,670,000.00 USD | 2,670,000.00 USD | 64,670.00 USD | 11,120.00 USD | 28,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.51` | 2,570,000.00 USD | 2,570,000.00 USD | 16,530.00 USD | 48,100.00 USD | 21,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 4,570,000.00 USD | 4,570,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.52` | 2,480,000.00 USD | 2,480,000.00 USD | 48,940.00 USD | 17,250.00 USD | 23,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 2,390,000.00 USD | 2,390,000.00 USD | 17,330.00 USD | 29,630.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 4,080,000.00 USD | 4,080,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.54` | 2,300,000.00 USD | 2,300,000.00 USD | 19,400.00 USD | 6,040.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.55` | 2,230,000.00 USD | 2,230,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 3,260,000.00 USD | 3,260,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.56` | 2,130,000.00 USD | 2,130,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 1,980,000.00 USD | 1,980,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.57` | 2,830,000.00 USD | 2,830,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.58` | 1,820,000.00 USD | 1,820,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.59` | 1,680,000.00 USD | 1,680,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.59` | 1,950,000.00 USD | 1,950,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.60` | 1,550,000.00 USD | 1,550,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.61` | 1,420,000.00 USD | 1,420,000.00 USD | 35,340.00 USD | 12,770.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.61` | 1,470,000.00 USD | 1,470,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.62` | 1,350,000.00 USD | 1,350,000.00 USD | 102,610.00 USD | 23,160.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.63` | 1,200,000.00 USD | 1,200,000.00 USD | 77,860.00 USD | 21,050.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.63` | 1,110,000.00 USD | 1,110,000.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.64` | 1,090,000.00 USD | 1,090,000.00 USD | 105,620.00 USD | 11,790.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.65` | 950,410.00 USD | 950,410.00 USD | 50,810.00 USD | 31,510.00 USD | 33,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.65` | 1,010,000.00 USD | 1,010,000.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.66` | 834,990.00 USD | 834,990.00 USD | 74,110.00 USD | 26,760.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.67` | 719,120.00 USD | 719,120.00 USD | 59,230.00 USD | 5,480.00 USD | 27,430.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `9.03` | 425,580.00 USD | 425,580.00 USD | 54,730.00 USD | 28,060.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 626,990.00 USD | 626,990.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 466,400.00 USD | 466,400.00 USD | 18,960.00 USD | 10,710.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 534,700.00 USD | 534,700.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 719,540.00 USD | 719,540.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 586,030.00 USD | 586,030.00 USD | 27,120.00 USD | 2,420.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 650,040.00 USD | 650,040.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 759,900.00 USD | 759,900.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 691,660.00 USD | 691,660.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 850,220.00 USD | 850,220.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 1,050,000.00 USD | 1,050,000.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 945,530.00 USD | 945,530.00 USD | 66,840.00 USD | 22,440.00 USD | 6,030.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `9.17` | 1,820,000.00 USD | 1,820,000.00 USD | 107,540.00 USD | 18,740.00 USD | 59,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 5,160,000.00 USD | 5,160,000.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 2,070,000.00 USD | 2,070,000.00 USD | 151,850.00 USD | 40,170.00 USD | 65,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 2,230,000.00 USD | 2,230,000.00 USD | 97,890.00 USD | 40,200.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 5,960,000.00 USD | 5,960,000.00 USD | 503,250.00 USD | 101,150.00 USD | 193,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.20` | 3,800.00 USD | 4,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.20` | 2,430,000.00 USD | 2,430,000.00 USD | 119,740.00 USD | 10,810.00 USD | 67,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 2,490,000.00 USD | 2,490,000.00 USD | 48,600.00 USD | 6,420.00 USD | 9,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 6,920,000.00 USD | 6,920,000.00 USD | 554,780.00 USD | 132,850.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 2,600,000.00 USD | 2,600,000.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 2,700,000.00 USD | 2,700,000.00 USD | 57,020.00 USD | 3,310.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 7,940,000.00 USD | 7,940,000.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 2,730,000.00 USD | 2,730,000.00 USD | 31,050.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 2,780,000.00 USD | 2,780,000.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 8,440,000.00 USD | 8,440,000.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 2,790,000.00 USD | 2,790,000.00 USD | 16,250.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 2,830,000.00 USD | 2,830,000.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 8,770,000.00 USD | 8,770,000.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 2,860,000.00 USD | 2,860,000.00 USD | 20,250.00 USD | 3,860.00 USD | 27.40 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 2,940,000.00 USD | 2,940,000.00 USD | 48,970.00 USD | 15,680.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 9,620,000.00 USD | 9,620,000.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.30` | 2,990,000.00 USD | 2,990,000.00 USD | 42,450.00 USD | 9,410.00 USD | 26.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 3,050,000.00 USD | 3,050,000.00 USD | 27,590.00 USD | 4,250.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 10,260,000.00 USD | 10,260,000.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 3,070,000.00 USD | 3,070,000.00 USD | 9,610.00 USD | 2,530.00 USD | 10,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 3,090,000.00 USD | 3,090,000.00 USD | 7,010.00 USD | 6,000.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 10,630,000.00 USD | 10,630,000.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 3,120,000.00 USD | 3,120,000.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.35` | 3,180,000.00 USD | 3,180,000.00 USD | 28,980.00 USD | 3,810.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 11,110,000.00 USD | 11,110,000.00 USD | 289,480.00 USD | 93,460.00 USD | 96,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 3,290,000.00 USD | 3,290,000.00 USD | 66,220.00 USD | 13,630.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 3,340,000.00 USD | 3,340,000.00 USD | 36,610.00 USD | 13,410.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 11,580,000.00 USD | 11,580,000.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 3,420,000.00 USD | 3,420,000.00 USD | 47,540.00 USD | 4,040.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.39` | 3,440,000.00 USD | 3,440,000.00 USD | 16,910.00 USD | 1,730.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 11,940,000.00 USD | 11,940,000.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 3,490,000.00 USD | 3,490,000.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 3,540,000.00 USD | 3,540,000.00 USD | 29,300.00 USD | 1,660.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 12,400,000.00 USD | 12,400,000.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 3,550,000.00 USD | 3,550,000.00 USD | 10,620.00 USD | 622.99 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 3,580,000.00 USD | 3,580,000.00 USD | 10,390.00 USD | 6,940.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 12,640,000.00 USD | 12,640,000.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 3,580,000.00 USD | 3,580,000.00 USD | 1,530.00 USD | 0.00 USD | 48.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 3,590,000.00 USD | 3,590,000.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 12,770,000.00 USD | 12,770,000.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.46` | 3,010.00 USD | 417,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.46` | 3,600,000.00 USD | 3,600,000.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 3,620,000.00 USD | 3,620,000.00 USD | 18,220.00 USD | 6,870.00 USD | 192.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 12,880,000.00 USD | 12,880,000.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 3,630,000.00 USD | 3,630,000.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 3,660,000.00 USD | 3,660,000.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 12,960,000.00 USD | 12,960,000.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 3,680,000.00 USD | 3,680,000.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 3,680,000.00 USD | 3,680,000.00 USD | 295.05 USD | 0.00 USD | 124.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.51` | 13,250,000.00 USD | 13,250,000.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 3,700,000.00 USD | 3,700,000.00 USD | 17,180.00 USD | 3,070.00 USD | 5,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 3,730,000.00 USD | 3,730,000.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 13,460,000.00 USD | 13,460,000.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 3,740,000.00 USD | 3,740,000.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.55` | 3,750,000.00 USD | 3,750,000.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 13,510,000.00 USD | 13,510,000.00 USD | 28,850.00 USD | 19,960.00 USD | 880.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 3,760,000.00 USD | 3,760,000.00 USD | 4,750.00 USD | 1,280.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.57` | 3,770,000.00 USD | 3,770,000.00 USD | 1,370.00 USD | 3,100.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 13,680,000.00 USD | 13,680,000.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 3,780,000.00 USD | 3,780,000.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.59` | 3,780,000.00 USD | 3,780,000.00 USD | 5,050.00 USD | 1,250.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 13,740,000.00 USD | 13,740,000.00 USD | 26,920.00 USD | 15,650.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 3,810,000.00 USD | 3,810,000.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.61` | 3,840,000.00 USD | 3,840,000.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 13,870,000.00 USD | 13,870,000.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 3,840,000.00 USD | 3,840,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.63` | 3,850,000.00 USD | 3,850,000.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.63` | 13,920,000.00 USD | 13,920,000.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 3,860,000.00 USD | 3,860,000.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.65` | 3,870,000.00 USD | 3,870,000.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.65` | 13,990,000.00 USD | 13,990,000.00 USD | 33,020.00 USD | 20,230.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 3,890,000.00 USD | 3,890,000.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.67` | 3,900,000.00 USD | 3,900,000.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.67` | 14,070,000.00 USD | 14,070,000.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 3,920,000.00 USD | 3,920,000.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.69` | 3,930,000.00 USD | 3,930,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.69` | 14,240,000.00 USD | 14,240,000.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 3,950,000.00 USD | 3,950,000.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.71` | 3,960,000.00 USD | 3,960,000.00 USD | 74.90 USD | 5,170.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.71` | 14,380,000.00 USD | 14,380,000.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 3,960,000.00 USD | 3,960,000.00 USD | 2,760.00 USD | 3,170.00 USD | 57.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.73` | 14,400,000.00 USD | 14,400,000.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 417,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 3,970,000.00 USD | 3,970,000.00 USD | 5,260.00 USD | 0.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.75` | 3,980,000.00 USD | 3,980,000.00 USD | 3,790.00 USD | 1,180.00 USD | 946.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.75` | 14,480,000.00 USD | 14,480,000.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.76` | 3,990,000.00 USD | 3,990,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.77` | 14,590,000.00 USD | 14,590,000.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.78` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.79` | 4,000,000.00 USD | 4,000,000.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.79` | 14,650,000.00 USD | 14,650,000.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.79` | 551.36 USD | 418,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.81` | 14,830,000.00 USD | 14,830,000.00 USD | 103,830.00 USD | 23,930.00 USD | 48,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.81` | 472.10 USD | 418,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.83` | 14,950,000.00 USD | 14,950,000.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.85` | 15,060,000.00 USD | 15,060,000.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.87` | 15,110,000.00 USD | 15,110,000.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.89` | 15,190,000.00 USD | 15,190,000.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.91` | 15,240,000.00 USD | 15,240,000.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.93` | 15,300,000.00 USD | 15,300,000.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.95` | 15,380,000.00 USD | 15,380,000.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.97` | 15,440,000.00 USD | 15,440,000.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.99` | 15,450,000.00 USD | 15,450,000.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.01` | 15,470,000.00 USD | 15,470,000.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.03` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `1.85` | 2,320,000.00 USD | 0.00 USD | 204.05 USD | `-79.01%` | `110.00` |
| `Live` | `Long` | `1.93` | 2,320,000.00 USD | 0.00 USD | 481.25 USD | `-78.22%` | `250.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 159.60 USD | `-77.43%` | `80.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 104.26 USD | `-77.31%` | `52.00` |
| `Live` | `Long` | `2.04` | 2,320,000.00 USD | 0.00 USD | 110.52 USD | `-76.97%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,320,000.00 USD | 0.00 USD | 4,920.00 USD | `-76.64%` | `2,382.76` |
| `Live` | `Long` | `2.31` | 2,310,000.00 USD | 0.00 USD | 375.35 USD | `-73.92%` | `162.84` |
| `Live` | `Long` | `2.33` | 2,310,000.00 USD | 0.00 USD | 2,170.00 USD | `-73.58%` | `929.47` |
| `Live` | `Long` | `2.38` | 2,310,000.00 USD | 0.00 USD | 290.37 USD | `-73.01%` | `121.75` |
| `Live` | `Long` | `2.42` | 2,310,000.00 USD | 0.00 USD | 265.65 USD | `-72.68%` | `110.00` |
| `Live` | `Long` | `2.42` | 2,310,000.00 USD | 0.00 USD | 814.80 USD | `-72.56%` | `336.00` |
| `Live` | `Long` | `2.48` | 2,310,000.00 USD | 0.00 USD | 17,370.00 USD | `-71.88%` | `6,990.57` |
| `Live` | `Long` | `2.58` | 2,290,000.00 USD | 0.00 USD | 109.88 USD | `-70.87%` | `42.67` |
| `Live` | `Long` | `2.69` | 2,290,000.00 USD | 0.00 USD | 133.73 USD | `-69.51%` | `49.62` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 232.67 USD | `-67.58%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 45,470.00 USD | `-66.79%` | `15,492.38` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 111.12 USD | `-66.34%` | `37.35` |
| `Live` | `Long` | `2.98` | 2,250,000.00 USD | 0.00 USD | 1,130.00 USD | `-66.23%` | `377.71` |
| `Live` | `Long` | `3.10` | 2,250,000.00 USD | 0.00 USD | 1,460.00 USD | `-64.98%` | `470.82` |
| `Live` | `Long` | `3.23` | 2,240,000.00 USD | 0.00 USD | 404.38 USD | `-63.40%` | `125.00` |
| `Live` | `Long` | `3.37` | 2,240,000.00 USD | 0.00 USD | 389.53 USD | `-61.93%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,240,000.00 USD | 0.00 USD | 151.88 USD | `-61.81%` | `45.00` |
| `Live` | `Long` | `3.40` | 2,240,000.00 USD | 0.00 USD | 114.82 USD | `-61.47%` | `33.72` |
| `Live` | `Long` | `3.54` | 2,240,000.00 USD | 0.00 USD | 152.25 USD | `-60.00%` | `43.07` |
| `Live` | `Long` | `3.60` | 2,240,000.00 USD | 0.00 USD | 775.18 USD | `-59.21%` | `215.03` |
| `Live` | `Long` | `3.67` | 2,240,000.00 USD | 0.00 USD | 109.95 USD | `-58.53%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,240,000.00 USD | 0.00 USD | 1,500.00 USD | `-57.51%` | `400.00` |
| `Live` | `Long` | `3.85` | 2,240,000.00 USD | 0.00 USD | 341.01 USD | `-56.38%` | `88.46` |
| `Live` | `Long` | `3.90` | 2,240,000.00 USD | 0.00 USD | 131.73 USD | `-55.93%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,240,000.00 USD | 0.00 USD | 371.88 USD | `-54.91%` | `93.32` |
| `Live` | `Long` | `4.03` | 2,240,000.00 USD | 0.00 USD | 402.70 USD | `-54.46%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,240,000.00 USD | 0.00 USD | 152.29 USD | `-54.23%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,240,000.00 USD | 0.00 USD | 9,290.00 USD | `-53.78%` | `2,273.34` |
| `Live` | `Long` | `4.14` | 2,230,000.00 USD | 0.00 USD | 1,130.00 USD | `-53.10%` | `272.03` |
| `Live` | `Long` | `4.18` | 2,230,000.00 USD | 0.00 USD | 174.89 USD | `-52.65%` | `41.79` |
| `Live` | `Long` | `4.20` | 2,230,000.00 USD | 0.00 USD | 419.50 USD | `-52.54%` | `100.00` |
| `Live` | `Long` | `4.24` | 2,230,000.00 USD | 0.00 USD | 169.40 USD | `-52.08%` | `40.00` |
| `Live` | `Long` | `4.29` | 2,230,000.00 USD | 0.00 USD | 2,440.00 USD | `-51.52%` | `568.43` |
| `Live` | `Long` | `4.30` | 2,230,000.00 USD | 0.00 USD | 174.83 USD | `-51.29%` | `40.61` |
| `Live` | `Long` | `4.32` | 2,230,000.00 USD | 0.00 USD | 852.47 USD | `-51.18%` | `197.56` |
| `Live` | `Long` | `4.33` | 2,220,000.00 USD | 0.00 USD | 2,190.00 USD | `-50.95%` | `504.56` |
| `Live` | `Long` | `4.37` | 2,220,000.00 USD | 0.00 USD | 117.86 USD | `-50.61%` | `27.00` |
| `Live` | `Long` | `4.51` | 2,220,000.00 USD | 0.00 USD | 217.71 USD | `-48.91%` | `48.22` |
| `Live` | `Long` | `4.59` | 2,220,000.00 USD | 0.00 USD | 30,970.00 USD | `-48.01%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 486.93 USD | `-47.78%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,190,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.67%` | `579.06` |
| `Live` | `Long` | `4.66` | 2,190,000.00 USD | 0.00 USD | 105.11 USD | `-47.33%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,190,000.00 USD | 0.00 USD | 3,280.00 USD | `-47.22%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,180,000.00 USD | 0.00 USD | 1,490.00 USD | `-47.10%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,180,000.00 USD | 0.00 USD | 8,490.00 USD | `-46.99%` | `1,812.97` |
| `Live` | `Long` | `4.70` | 2,170,000.00 USD | 0.00 USD | 7,730.00 USD | `-46.88%` | `1,645.98` |
| `Live` | `Long` | `4.75` | 2,170,000.00 USD | 0.00 USD | 240.48 USD | `-46.31%` | `50.68` |
| `Live` | `Long` | `4.76` | 2,170,000.00 USD | 0.00 USD | 105.64 USD | `-46.09%` | `22.17` |
| `Live` | `Long` | `4.80` | 2,170,000.00 USD | 0.00 USD | 15,790.00 USD | `-45.63%` | `3,286.00` |
| `Live` | `Long` | `4.83` | 2,150,000.00 USD | 0.00 USD | 6,380.00 USD | `-45.41%` | `1,323.00` |
| `Live` | `Long` | `4.83` | 2,140,000.00 USD | 0.00 USD | 467.01 USD | `-45.29%` | `96.59` |
| `Live` | `Long` | `4.89` | 2,140,000.00 USD | 0.00 USD | 146.85 USD | `-44.62%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,140,000.00 USD | 0.00 USD | 527.19 USD | `-44.50%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,140,000.00 USD | 0.00 USD | 1,350.00 USD | `-44.39%` | `274.20` |
| `Live` | `Long` | `4.96` | 2,140,000.00 USD | 0.00 USD | 945.36 USD | `-43.94%` | `190.79` |
| `Live` | `Long` | `4.97` | 2,140,000.00 USD | 0.00 USD | 282.23 USD | `-43.71%` | `56.73` |
| `Live` | `Long` | `4.99` | 2,140,000.00 USD | 0.00 USD | 329.11 USD | `-43.60%` | `66.02` |
| `Live` | `Long` | `5.01` | 2,140,000.00 USD | 0.00 USD | 56,390.00 USD | `-43.26%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,080,000.00 USD | 0.00 USD | 167.78 USD | `-43.14%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,080,000.00 USD | 0.00 USD | 314.59 USD | `-43.03%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,080,000.00 USD | 0.00 USD | 504.74 USD | `-42.81%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,080,000.00 USD | 0.00 USD | 318.46 USD | `-42.58%` | `62.75` |
| `Live` | `Long` | `5.09` | 2,080,000.00 USD | 0.00 USD | 4,690.00 USD | `-42.35%` | `920.67` |
| `Live` | `Long` | `5.12` | 2,080,000.00 USD | 0.00 USD | 250.20 USD | `-42.01%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,080,000.00 USD | 0.00 USD | 396.06 USD | `-41.90%` | `77.13` |
| `Live` | `Long` | `5.16` | 2,080,000.00 USD | 0.00 USD | 156,890.00 USD | `-41.67%` | `30,435.20` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 2,300.00 USD | `-41.56%` | `445.16` |
| `Live` | `Long` | `5.17` | 1,920,000.00 USD | 0.00 USD | 1,620.00 USD | `-41.45%` | `312.94` |
| `Live` | `Long` | `5.18` | 1,920,000.00 USD | 0.00 USD | 150.57 USD | `-41.33%` | `29.04` |
| `Live` | `Long` | `5.21` | 1,920,000.00 USD | 0.00 USD | 300.91 USD | `-40.99%` | `57.70` |
| `Live` | `Long` | `5.29` | 1,920,000.00 USD | 0.00 USD | 640.70 USD | `-40.20%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,920,000.00 USD | 0.00 USD | 232.85 USD | `-39.86%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,910,000.00 USD | 0.00 USD | 716.11 USD | `-39.75%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,910,000.00 USD | 0.00 USD | 660.46 USD | `-38.96%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,910,000.00 USD | 0.00 USD | 21,080.00 USD | `-38.73%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,890,000.00 USD | 0.00 USD | 163,110.00 USD | `-38.62%` | `30,067.25` |
| `Live` | `Long` | `5.43` | 1,730,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.51%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,730,000.00 USD | 0.00 USD | 264.72 USD | `-38.17%` | `48.44` |
| `Live` | `Long` | `5.49` | 1,730,000.00 USD | 0.00 USD | 354.06 USD | `-37.94%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,730,000.00 USD | 0.00 USD | 19,290.00 USD | `-37.83%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,710,000.00 USD | 0.00 USD | 367.41 USD | `-37.60%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,710,000.00 USD | 0.00 USD | 121.38 USD | `-37.37%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,710,000.00 USD | 0.00 USD | 967.98 USD | `-37.03%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,710,000.00 USD | 0.00 USD | 63,260.00 USD | `-36.92%` | `11,347.58` |
| `Live` | `Long` | `5.59` | 1,640,000.00 USD | 0.00 USD | 34,430.00 USD | `-36.70%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,610,000.00 USD | 0.00 USD | 22,270.00 USD | `-36.24%` | `3,952.96` |
| `Live` | `Long` | `5.66` | 1,590,000.00 USD | 0.00 USD | 4,160.00 USD | `-36.02%` | `734.88` |
| `Live` | `Long` | `5.70` | 1,580,000.00 USD | 0.00 USD | 405.03 USD | `-35.56%` | `71.12` |
| `Live` | `Long` | `5.71` | 1,580,000.00 USD | 0.00 USD | 2,340.00 USD | `-35.45%` | `409.39` |
| `Live` | `Long` | `5.74` | 1,580,000.00 USD | 0.00 USD | 238.86 USD | `-35.11%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 125.70 USD | `-35.00%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,580,000.00 USD | 0.00 USD | 3,190.00 USD | `-34.88%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,580,000.00 USD | 0.00 USD | 10,850.00 USD | `-34.77%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,570,000.00 USD | 0.00 USD | 801.40 USD | `-34.66%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.55%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,560,000.00 USD | 0.00 USD | 736.72 USD | `-34.43%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,560,000.00 USD | 0.00 USD | 580.50 USD | `-34.32%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,560,000.00 USD | 0.00 USD | 106.65 USD | `-34.21%` | `18.34` |
| `Live` | `Long` | `5.88` | 1,560,000.00 USD | 0.00 USD | 329,350.00 USD | `-33.53%` | `56,059.40` |
| `Live` | `Long` | `5.89` | 1,230,000.00 USD | 0.00 USD | 640.67 USD | `-33.30%` | `108.68` |
| `Live` | `Long` | `5.91` | 1,230,000.00 USD | 0.00 USD | 399.18 USD | `-33.19%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,230,000.00 USD | 0.00 USD | 12,380.00 USD | `-32.62%` | `2,078.19` |
| `Live` | `Long` | `5.97` | 1,220,000.00 USD | 0.00 USD | 585.97 USD | `-32.40%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,220,000.00 USD | 0.00 USD | 447.98 USD | `-32.28%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,220,000.00 USD | 0.00 USD | 341.56 USD | `-32.06%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,220,000.00 USD | 0.00 USD | 446.85 USD | `-31.94%` | `74.29` |
| `Live` | `Long` | `6.03` | 1,220,000.00 USD | 0.00 USD | 404.46 USD | `-31.83%` | `67.13` |
| `Live` | `Long` | `6.04` | 1,220,000.00 USD | 0.00 USD | 331.68 USD | `-31.72%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,210,000.00 USD | 0.00 USD | 448.72 USD | `-31.60%` | `74.23` |
| `Live` | `Long` | `6.05` | 1,210,000.00 USD | 0.00 USD | 1,310.00 USD | `-31.49%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,210,000.00 USD | 0.00 USD | 1,630.00 USD | `-31.38%` | `268.85` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-31.26%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,210,000.00 USD | 0.00 USD | 405.14 USD | `-31.15%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,210,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.04%` | `582.81` |
| `Live` | `Long` | `6.11` | 1,210,000.00 USD | 0.00 USD | 3,200.00 USD | `-30.92%` | `524.73` |
| `Live` | `Long` | `6.12` | 1,200,000.00 USD | 0.00 USD | 137.02 USD | `-30.70%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,200,000.00 USD | 0.00 USD | 2,370.00 USD | `-30.59%` | `386.46` |
| `Live` | `Long` | `6.14` | 1,200,000.00 USD | 0.00 USD | 238.61 USD | `-30.47%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,200,000.00 USD | 0.00 USD | 4,390.00 USD | `-30.36%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 187.29 USD | `-30.25%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,200,000.00 USD | 0.00 USD | 104.36 USD | `-30.13%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,200,000.00 USD | 0.00 USD | 310.25 USD | `-29.79%` | `50.00` |
| `Live` | `Long` | `6.21` | 1,190,000.00 USD | 0.00 USD | 2,560.00 USD | `-29.68%` | `411.30` |
| `Live` | `Long` | `6.22` | 1,190,000.00 USD | 0.00 USD | 715.31 USD | `-29.57%` | `114.91` |
| `Live` | `Long` | `6.25` | 1,190,000.00 USD | 0.00 USD | 972.65 USD | `-29.23%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,190,000.00 USD | 0.00 USD | 2,510.00 USD | `-29.00%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,190,000.00 USD | 0.00 USD | 1,610.00 USD | `-28.89%` | `255.64` |
| `Live` | `Long` | `6.32` | 1,190,000.00 USD | 0.00 USD | 277.04 USD | `-28.55%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,190,000.00 USD | 0.00 USD | 105.25 USD | `-28.44%` | `16.64` |
| `Live` | `Long` | `6.36` | 1,190,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.10%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,180,000.00 USD | 0.00 USD | 284,770.00 USD | `-27.98%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 896,880.00 USD | 0.00 USD | 5,110.00 USD | `-27.87%` | `801.31` |
| `Live` | `Long` | `6.41` | 891,770.00 USD | 0.00 USD | 1,640.00 USD | `-27.53%` | `256.20` |
| `Live` | `Long` | `6.42` | 890,130.00 USD | 0.00 USD | 306.32 USD | `-27.42%` | `47.75` |
| `Live` | `Long` | `6.43` | 889,830.00 USD | 0.00 USD | 6,780.00 USD | `-27.19%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 883,050.00 USD | 0.00 USD | 1,050.00 USD | `-26.85%` | `162.75` |
| `Live` | `Long` | `6.50` | 882,000.00 USD | 0.00 USD | 1,720.00 USD | `-26.51%` | `265.15` |
| `Live` | `Long` | `6.54` | 880,280.00 USD | 0.00 USD | 3,620.00 USD | `-26.06%` | `554.55` |
| `Live` | `Long` | `6.54` | 876,650.00 USD | 0.00 USD | 8,970.00 USD | `-25.95%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 867,680.00 USD | 0.00 USD | 2,170.00 USD | `-25.61%` | `330.00` |
| `Live` | `Long` | `6.58` | 865,510.00 USD | 0.00 USD | 1,100.00 USD | `-25.49%` | `166.55` |
| `Live` | `Long` | `6.62` | 864,410.00 USD | 0.00 USD | 2,110.00 USD | `-25.15%` | `318.57` |
| `Live` | `Long` | `6.70` | 862,310.00 USD | 0.00 USD | 506.54 USD | `-24.25%` | `75.66` |
| `Live` | `Long` | `6.71` | 861,800.00 USD | 0.00 USD | 16,610.00 USD | `-24.14%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 845,190.00 USD | 0.00 USD | 1,330.00 USD | `-23.68%` | `196.95` |
| `Live` | `Long` | `6.78` | 843,860.00 USD | 0.00 USD | 6,780.00 USD | `-23.34%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 837,080.00 USD | 0.00 USD | 16,960.00 USD | `-23.23%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 820,120.00 USD | 0.00 USD | 4,260.00 USD | `-23.12%` | `626.24` |
| `Live` | `Long` | `6.80` | 815,870.00 USD | 0.00 USD | 1,500.00 USD | `-23.00%` | `220.95` |
| `Live` | `Long` | `6.82` | 814,360.00 USD | 0.00 USD | 2,670.00 USD | `-22.89%` | `391.11` |
| `Live` | `Long` | `6.83` | 811,700.00 USD | 0.00 USD | 158.14 USD | `-22.78%` | `23.17` |
| `Live` | `Long` | `6.83` | 811,540.00 USD | 0.00 USD | 4,830.00 USD | `-22.67%` | `706.73` |
| `Live` | `Long` | `6.86` | 806,710.00 USD | 0.00 USD | 18,930.00 USD | `-22.44%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 787,780.00 USD | 0.00 USD | 3,340.00 USD | `-22.33%` | `486.46` |
| `Live` | `Long` | `6.89` | 784,440.00 USD | 0.00 USD | 5,250.00 USD | `-21.99%` | `761.63` |
| `Live` | `Long` | `6.91` | 779,190.00 USD | 0.00 USD | 269.30 USD | `-21.87%` | `39.00` |
| `Live` | `Long` | `6.92` | 778,920.00 USD | 0.00 USD | 1,510.00 USD | `-21.76%` | `217.70` |
| `Live` | `Long` | `6.95` | 777,410.00 USD | 0.00 USD | 3,760.00 USD | `-21.42%` | `541.68` |
| `Live` | `Long` | `6.96` | 773,650.00 USD | 0.00 USD | 3,480.00 USD | `-21.31%` | `500.00` |
| `Live` | `Long` | `6.96` | 770,170.00 USD | 0.00 USD | 28,500.00 USD | `-21.19%` | `4,091.42` |
| `Live` | `Long` | `6.99` | 741,680.00 USD | 0.00 USD | 1,400.00 USD | `-20.97%` | `200.00` |
| `Live` | `Long` | `7.00` | 740,280.00 USD | 0.00 USD | 1,550.00 USD | `-20.85%` | `222.06` |
| `Live` | `Long` | `7.00` | 738,730.00 USD | 0.00 USD | 24,240.00 USD | `-20.74%` | `3,460.54` |
| `Live` | `Long` | `7.04` | 714,480.00 USD | 0.00 USD | 4,100.00 USD | `-20.29%` | `581.44` |
| `Live` | `Long` | `7.08` | 710,390.00 USD | 0.00 USD | 6,700.00 USD | `-19.95%` | `947.44` |
| `Live` | `Long` | `7.08` | 703,680.00 USD | 0.00 USD | 1,670.00 USD | `-19.84%` | `236.20` |
| `Live` | `Long` | `7.11` | 702,010.00 USD | 0.00 USD | 28,230.00 USD | `-19.61%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 673,790.00 USD | 0.00 USD | 379.66 USD | `-19.50%` | `53.36` |
| `Live` | `Long` | `7.13` | 673,410.00 USD | 0.00 USD | 2,300.00 USD | `-19.27%` | `322.72` |
| `Live` | `Long` | `7.14` | 671,100.00 USD | 0.00 USD | 20,950.00 USD | `-19.16%` | `2,931.56` |
| `Live` | `Long` | `7.16` | 650,160.00 USD | 0.00 USD | 1,630.00 USD | `-19.04%` | `228.41` |
| `Live` | `Long` | `7.18` | 648,520.00 USD | 0.00 USD | 1,440.00 USD | `-18.71%` | `200.00` |
| `Live` | `Long` | `7.21` | 647,090.00 USD | 0.00 USD | 581.02 USD | `-18.37%` | `80.53` |
| `Live` | `Long` | `7.24` | 646,510.00 USD | 0.00 USD | 179.65 USD | `-18.14%` | `24.83` |
| `Live` | `Long` | `7.25` | 646,330.00 USD | 0.00 USD | 185.83 USD | `-18.03%` | `25.65` |
| `Live` | `Long` | `7.29` | 646,140.00 USD | 0.00 USD | 36,560.00 USD | `-17.57%` | `5,019.00` |
| `Live` | `Long` | `7.29` | 609,580.00 USD | 0.00 USD | 19,790.00 USD | `-17.46%` | `2,712.69` |
| `Live` | `Long` | `7.32` | 589,790.00 USD | 0.00 USD | 168.76 USD | `-17.23%` | `23.07` |
| `Live` | `Long` | `7.33` | 589,620.00 USD | 0.00 USD | 4,910.00 USD | `-17.12%` | `669.93` |
| `Live` | `Long` | `7.33` | 584,710.00 USD | 0.00 USD | 2,450.00 USD | `-17.01%` | `333.54` |
| `Live` | `Long` | `7.34` | 582,260.00 USD | 0.00 USD | 4,370.00 USD | `-16.89%` | `594.84` |
| `Live` | `Long` | `7.37` | 577,900.00 USD | 0.00 USD | 5,720.00 USD | `-16.67%` | `776.95` |
| `Live` | `Long` | `7.38` | 572,170.00 USD | 0.00 USD | 3,920.00 USD | `-16.56%` | `531.65` |
| `Live` | `Long` | `7.38` | 568,250.00 USD | 0.00 USD | 17,770.00 USD | `-16.44%` | `2,406.10` |
| `Live` | `Long` | `7.39` | 550,480.00 USD | 0.00 USD | 1,550.00 USD | `-16.33%` | `210.17` |
| `Live` | `Long` | `7.42` | 548,930.00 USD | 0.00 USD | 1,540.00 USD | `-15.99%` | `207.34` |
| `Live` | `Long` | `7.45` | 547,390.00 USD | 0.00 USD | 1,700.00 USD | `-15.76%` | `228.34` |
| `Live` | `Long` | `7.46` | 545,690.00 USD | 0.00 USD | 1,370.00 USD | `-15.65%` | `183.84` |
| `Live` | `Long` | `7.46` | 544,320.00 USD | 0.00 USD | 5,430.00 USD | `-15.54%` | `727.40` |
| `Live` | `Long` | `7.47` | 538,890.00 USD | 0.00 USD | 3,210.00 USD | `-15.42%` | `430.09` |
| `Live` | `Long` | `7.50` | 535,670.00 USD | 0.00 USD | 1,580.00 USD | `-15.20%` | `211.22` |
| `Live` | `Long` | `7.50` | 534,090.00 USD | 0.00 USD | 1,080.00 USD | `-15.08%` | `143.74` |
| `Live` | `Long` | `7.53` | 533,010.00 USD | 0.00 USD | 995.86 USD | `-14.86%` | `132.34` |
| `Live` | `Long` | `7.54` | 532,020.00 USD | 0.00 USD | 4,210.00 USD | `-14.75%` | `559.01` |
| `Live` | `Long` | `7.55` | 527,800.00 USD | 0.00 USD | 157.14 USD | `-14.52%` | `20.80` |
| `Live` | `Long` | `7.57` | 527,650.00 USD | 0.00 USD | 118.09 USD | `-14.41%` | `15.61` |
| `Live` | `Long` | `7.58` | 527,530.00 USD | 0.00 USD | 4,260.00 USD | `-14.29%` | `562.89` |
| `Live` | `Long` | `7.59` | 523,270.00 USD | 0.00 USD | 25,140.00 USD | `-14.07%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 498,120.00 USD | 0.00 USD | 312.22 USD | `-13.84%` | `41.00` |
| `Live` | `Long` | `7.62` | 497,810.00 USD | 0.00 USD | 787.51 USD | `-13.73%` | `103.28` |
| `Live` | `Long` | `7.63` | 497,030.00 USD | 0.00 USD | 514.52 USD | `-13.61%` | `67.39` |
| `Live` | `Long` | `7.66` | 496,510.00 USD | 0.00 USD | 135.42 USD | `-13.39%` | `17.69` |
| `Live` | `Long` | `7.67` | 496,380.00 USD | 0.00 USD | 1,740.00 USD | `-13.27%` | `226.45` |
| `Live` | `Long` | `7.68` | 494,640.00 USD | 0.00 USD | 1,120.00 USD | `-13.05%` | `145.25` |
| `Live` | `Long` | `7.70` | 493,520.00 USD | 0.00 USD | 1,460.00 USD | `-12.93%` | `190.36` |
| `Live` | `Long` | `7.71` | 492,060.00 USD | 0.00 USD | 19,410.00 USD | `-12.82%` | `2,518.82` |
| `Live` | `Long` | `7.72` | 472,650.00 USD | 0.00 USD | 2,550.00 USD | `-12.60%` | `330.65` |
| `Live` | `Long` | `7.75` | 470,100.00 USD | 0.00 USD | 893.76 USD | `-12.26%` | `115.25` |
| `Live` | `Long` | `7.76` | 469,200.00 USD | 0.00 USD | 455.73 USD | `-12.14%` | `58.69` |
| `Live` | `Long` | `7.78` | 468,750.00 USD | 0.00 USD | 695.32 USD | `-12.03%` | `89.43` |
| `Live` | `Long` | `7.79` | 468,050.00 USD | 0.00 USD | 3,900.00 USD | `-11.92%` | `500.57` |
| `Live` | `Long` | `7.79` | 464,150.00 USD | 0.00 USD | 1,940.00 USD | `-11.80%` | `248.84` |
| `Live` | `Long` | `7.80` | 462,220.00 USD | 0.00 USD | 633.77 USD | `-11.69%` | `81.20` |
| `Live` | `Long` | `7.82` | 461,580.00 USD | 0.00 USD | 5,280.00 USD | `-11.58%` | `675.43` |
| `Live` | `Long` | `7.84` | 456,300.00 USD | 0.00 USD | 10,930.00 USD | `-11.24%` | `1,393.53` |
| `Live` | `Long` | `7.86` | 445,370.00 USD | 0.00 USD | 2,110.00 USD | `-11.12%` | `269.14` |
| `Live` | `Long` | `7.87` | 443,260.00 USD | 0.00 USD | 176.18 USD | `-11.01%` | `22.40` |
| `Live` | `Long` | `7.88` | 443,080.00 USD | 0.00 USD | 555.19 USD | `-10.90%` | `70.50` |
| `Live` | `Long` | `7.91` | 442,530.00 USD | 0.00 USD | 2,410.00 USD | `-10.56%` | `304.85` |
| `Live` | `Long` | `7.92` | 440,120.00 USD | 0.00 USD | 923.42 USD | `-10.33%` | `116.52` |
| `Live` | `Long` | `7.93` | 439,190.00 USD | 0.00 USD | 1,820.00 USD | `-10.22%` | `228.88` |
| `Live` | `Long` | `7.95` | 437,380.00 USD | 0.00 USD | 127,110.00 USD | `-10.11%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 310,260.00 USD | 0.00 USD | 843.15 USD | `-9.99%` | `105.99` |
| `Live` | `Long` | `7.99` | 309,420.00 USD | 0.00 USD | 1,600.00 USD | `-9.65%` | `200.68` |
| `Live` | `Long` | `8.00` | 307,820.00 USD | 0.00 USD | 210.99 USD | `-9.54%` | `26.39` |
| `Live` | `Long` | `8.03` | 307,610.00 USD | 0.00 USD | 957.70 USD | `-9.20%` | `119.34` |
| `Live` | `Long` | `8.04` | 306,650.00 USD | 0.00 USD | 88,380.00 USD | `-9.09%` | `10,999.50` |
| `Live` | `Long` | `8.04` | 218,270.00 USD | 0.00 USD | 6,890.00 USD | `-8.97%` | `856.44` |
| `Live` | `Long` | `8.05` | 211,380.00 USD | 0.00 USD | 3,340.00 USD | `-8.86%` | `414.27` |
| `Live` | `Long` | `8.06` | 208,040.00 USD | 0.00 USD | 37,830.00 USD | `-8.75%` | `4,690.67` |
| `Live` | `Long` | `8.09` | 170,210.00 USD | 0.00 USD | 617.61 USD | `-8.52%` | `76.39` |
| `Live` | `Long` | `8.10` | 169,590.00 USD | 0.00 USD | 165.46 USD | `-8.41%` | `20.44` |
| `Live` | `Long` | `8.11` | 169,430.00 USD | 0.00 USD | 11,550.00 USD | `-8.30%` | `1,425.26` |
| `Live` | `Long` | `8.12` | 157,870.00 USD | 0.00 USD | 241.26 USD | `-8.18%` | `29.73` |
| `Live` | `Long` | `8.16` | 157,630.00 USD | 0.00 USD | 871.61 USD | `-7.62%` | `106.75` |
| `Live` | `Long` | `8.20` | 156,760.00 USD | 0.00 USD | 1,290.00 USD | `-7.28%` | `157.09` |
| `Live` | `Long` | `8.21` | 155,470.00 USD | 0.00 USD | 1,910.00 USD | `-7.16%` | `232.19` |
| `Live` | `Long` | `8.21` | 153,570.00 USD | 0.00 USD | 147.87 USD | `-7.05%` | `18.00` |
| `Live` | `Long` | `8.22` | 153,420.00 USD | 0.00 USD | 2,100.00 USD | `-6.94%` | `255.16` |
| `Live` | `Long` | `8.23` | 151,320.00 USD | 0.00 USD | 1,160.00 USD | `-6.82%` | `140.81` |
| `Live` | `Long` | `8.24` | 150,160.00 USD | 0.00 USD | 1,300.00 USD | `-6.71%` | `158.06` |
| `Live` | `Long` | `8.26` | 148,860.00 USD | 0.00 USD | 13,810.00 USD | `-6.60%` | `1,673.14` |
| `Live` | `Long` | `8.28` | 135,050.00 USD | 0.00 USD | 9,860.00 USD | `-6.37%` | `1,191.23` |
| `Live` | `Long` | `8.29` | 125,190.00 USD | 0.00 USD | 498.26 USD | `-6.26%` | `60.14` |
| `Live` | `Long` | `8.29` | 124,690.00 USD | 0.00 USD | 18,970.00 USD | `-6.15%` | `2,286.62` |
| `Live` | `Long` | `8.30` | 105,720.00 USD | 0.00 USD | 33,500.00 USD | `-6.03%` | `4,033.57` |
| `Live` | `Long` | `8.31` | 72,230.00 USD | 0.00 USD | 4,550.00 USD | `-5.92%` | `547.70` |
| `Live` | `Long` | `8.34` | 67,670.00 USD | 0.00 USD | 4,630.00 USD | `-5.69%` | `555.62` |
| `Live` | `Long` | `8.36` | 63,040.00 USD | 0.00 USD | 3,410.00 USD | `-5.47%` | `407.63` |
| `Live` | `Long` | `8.37` | 59,640.00 USD | 0.00 USD | 7,160.00 USD | `-5.35%` | `856.48` |
| `Live` | `Long` | `8.38` | 52,470.00 USD | 0.00 USD | 3,410.00 USD | `-5.24%` | `406.80` |
| `Live` | `Long` | `8.38` | 49,060.00 USD | 0.00 USD | 1,870.00 USD | `-5.13%` | `222.50` |
| `Live` | `Long` | `8.39` | 47,200.00 USD | 0.00 USD | 1,680.00 USD | `-5.01%` | `200.00` |
| `Live` | `Long` | `8.40` | 45,520.00 USD | 0.00 USD | 710.22 USD | `-4.90%` | `84.50` |
| `Live` | `Long` | `8.41` | 44,810.00 USD | 0.00 USD | 681.03 USD | `-4.79%` | `80.93` |
| `Live` | `Long` | `8.43` | 44,130.00 USD | 0.00 USD | 674.00 USD | `-4.68%` | `80.00` |
| `Live` | `Long` | `8.44` | 43,450.00 USD | 0.00 USD | 188.61 USD | `-4.56%` | `22.36` |
| `Live` | `Long` | `8.45` | 43,270.00 USD | 0.00 USD | 1,470.00 USD | `-4.45%` | `174.62` |
| `Live` | `Long` | `8.46` | 41,790.00 USD | 0.00 USD | 226.93 USD | `-4.34%` | `26.84` |
| `Live` | `Long` | `8.46` | 41,560.00 USD | 0.00 USD | 1,860.00 USD | `-4.22%` | `220.00` |
| `Live` | `Long` | `8.47` | 39,700.00 USD | 0.00 USD | 12,430.00 USD | `-4.11%` | `1,466.22` |
| `Live` | `Long` | `8.48` | 27,280.00 USD | 0.00 USD | 1,160.00 USD | `-4.00%` | `136.39` |
| `Live` | `Long` | `8.49` | 26,120.00 USD | 0.00 USD | 403.51 USD | `-3.88%` | `47.50` |
| `Live` | `Long` | `8.51` | 25,710.00 USD | 0.00 USD | 6,380.00 USD | `-3.77%` | `750.34` |
| `Live` | `Long` | `8.52` | 19,330.00 USD | 0.00 USD | 7,770.00 USD | `-3.66%` | `912.98` |
| `Live` | `Long` | `8.54` | 11,560.00 USD | 0.00 USD | 6,350.00 USD | `-3.43%` | `743.78` |
| `Live` | `Long` | `8.54` | 5,210.00 USD | 0.00 USD | 1,550.00 USD | `-3.32%` | `180.95` |
| `Live` | `Long` | `8.55` | 3,660.00 USD | 0.00 USD | 684.40 USD | `-3.20%` | `80.00` |
| `Live` | `Long` | `8.61` | 2,980.00 USD | 0.00 USD | 2,980.00 USD | `-2.64%` | `346.30` |
| `Live` | `Short` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | `+3.36%` | `34.41` |
| `Live` | `Short` | `9.20` | 4,120.00 USD | 3,800.00 USD | 0.00 USD | `+4.04%` | `413.79` |
| `Live` | `Short` | `9.29` | 4,220.00 USD | 100.93 USD | 0.00 USD | `+5.06%` | `10.87` |
| `Live` | `Short` | `9.35` | 8,150.00 USD | 3,930.00 USD | 0.00 USD | `+5.73%` | `420.07` |
| `Live` | `Short` | `9.38` | 412,260.00 USD | 404,120.00 USD | 0.00 USD | `+6.19%` | `43,059.94` |
| `Live` | `Short` | `9.41` | 414,740.00 USD | 2,470.00 USD | 0.00 USD | `+6.53%` | `262.71` |
| `Live` | `Short` | `9.46` | 417,740.00 USD | 3,010.00 USD | 0.00 USD | `+6.98%` | `318.12` |
| `Live` | `Short` | `9.73` | 417,940.00 USD | 192.95 USD | 0.00 USD | `+10.15%` | `19.82` |
| `Live` | `Short` | `9.79` | 418,490.00 USD | 551.36 USD | 0.00 USD | `+10.83%` | `56.29` |
| `Live` | `Short` | `9.81` | 418,960.00 USD | 472.10 USD | 0.00 USD | `+11.05%` | `48.10` |
| `Live` | `Short` | `10.09` | 419,070.00 USD | 113.76 USD | 0.00 USD | `+14.11%` | `11.28` |
| `Live` | `Short` | `10.15` | 441,390.00 USD | 22,320.00 USD | 0.00 USD | `+14.90%` | `2,197.71` |
| `Live` | `Short` | `10.21` | 448,720.00 USD | 7,330.00 USD | 0.00 USD | `+15.58%` | `717.30` |
| `Live` | `Short` | `10.23` | 448,830.00 USD | 114.12 USD | 0.00 USD | `+15.80%` | `11.15` |
| `Live` | `Short` | `10.35` | 452,220.00 USD | 3,380.00 USD | 0.00 USD | `+17.05%` | `326.92` |
| `Live` | `Short` | `10.56` | 452,740.00 USD | 523.81 USD | 0.00 USD | `+19.54%` | `49.58` |
| `Live` | `Short` | `10.70` | 489,770.00 USD | 37,030.00 USD | 0.00 USD | `+21.01%` | `3,462.73` |
| `Live` | `Short` | `10.71` | 489,990.00 USD | 218.91 USD | 0.00 USD | `+21.24%` | `20.43` |
| `Live` | `Short` | `10.96` | 491,910.00 USD | 1,920.00 USD | 0.00 USD | `+24.06%` | `174.67` |
| `Live` | `Short` | `11.01` | 498,870.00 USD | 6,970.00 USD | 0.00 USD | `+24.52%` | `633.00` |
| `Live` | `Short` | `11.27` | 510,680.00 USD | 11,810.00 USD | 0.00 USD | `+27.46%` | `1,048.25` |
| `Live` | `Short` | `11.47` | 511,400.00 USD | 720.29 USD | 0.00 USD | `+29.83%` | `62.77` |
| `Live` | `Short` | `11.62` | 523,540.00 USD | 12,140.00 USD | 0.00 USD | `+31.53%` | `1,043.90` |
| `Live` | `Short` | `11.70` | 524,320.00 USD | 778.89 USD | 0.00 USD | `+32.32%` | `66.60` |
| `Live` | `Short` | `11.81` | 583,390.00 USD | 59,080.00 USD | 0.00 USD | `+33.68%` | `5,000.00` |
| `Live` | `Short` | `12.04` | 584,760.00 USD | 1,370.00 USD | 0.00 USD | `+36.17%` | `113.77` |
| `Live` | `Short` | `12.30` | 586,490.00 USD | 1,730.00 USD | 0.00 USD | `+39.23%` | `140.71` |
| `Live` | `Short` | `12.40` | 586,840.00 USD | 343.62 USD | 0.00 USD | `+40.36%` | `27.70` |
| `Live` | `Short` | `12.68` | 587,270.00 USD | 432.22 USD | 0.00 USD | `+43.41%` | `34.10` |
| `Live` | `Short` | `12.76` | 624,000.00 USD | 36,730.00 USD | 0.00 USD | `+44.32%` | `2,879.71` |
| `Live` | `Short` | `12.79` | 624,950.00 USD | 953.38 USD | 0.00 USD | `+44.66%` | `74.57` |
| `Live` | `Short` | `12.96` | 625,050.00 USD | 102.68 USD | 0.00 USD | `+46.69%` | `7.92` |
| `Live` | `Short` | `12.97` | 639,590.00 USD | 14,530.00 USD | 0.00 USD | `+46.81%` | `1,120.14` |
| `Live` | `Short` | `13.20` | 727,530.00 USD | 87,940.00 USD | 0.00 USD | `+49.30%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 962,370.00 USD | 234,840.00 USD | 0.00 USD | `+50.31%` | `17,677.02` |
| `Live` | `Short` | `13.29` | 966,180.00 USD | 3,810.00 USD | 0.00 USD | `+50.43%` | `286.56` |
| `Live` | `Short` | `13.46` | 966,610.00 USD | 430.34 USD | 0.00 USD | `+52.35%` | `31.96` |
| `Live` | `Short` | `13.69` | 966,790.00 USD | 172.29 USD | 0.00 USD | `+54.84%` | `12.59` |
| `Live` | `Short` | `14.14` | 966,950.00 USD | 164.79 USD | 0.00 USD | `+60.04%` | `11.65` |
| `Live` | `Short` | `14.43` | 970,950.00 USD | 4,000.00 USD | 0.00 USD | `+63.21%` | `277.54` |
| `Live` | `Short` | `14.62` | 971,240.00 USD | 288.35 USD | 0.00 USD | `+65.36%` | `19.73` |
| `Live` | `Short` | `14.66` | 972,070.00 USD | 823.29 USD | 0.00 USD | `+65.93%` | `56.14` |
| `Live` | `Short` | `14.84` | 972,310.00 USD | 243.44 USD | 0.00 USD | `+67.85%` | `16.41` |
| `Live` | `Short` | `14.86` | 974,780.00 USD | 2,470.00 USD | 0.00 USD | `+68.08%` | `166.16` |
| `Live` | `Short` | `14.95` | 975,100.00 USD | 322.06 USD | 0.00 USD | `+69.10%` | `21.55` |
| `Live` | `Short` | `15.29` | 975,330.00 USD | 229.43 USD | 0.00 USD | `+73.06%` | `15.00` |
| `Live` | `Short` | `15.35` | 975,560.00 USD | 230.17 USD | 0.00 USD | `+73.62%` | `15.00` |
| `Live` | `Short` | `15.38` | 995,560.00 USD | 20,000.00 USD | 0.00 USD | `+74.07%` | `1,300.00` |
| `Live` | `Short` | `15.49` | 1,150,000.00 USD | 154,950.00 USD | 0.00 USD | `+75.32%` | `10,000.00` |
| `Live` | `Short` | `15.74` | 1,150,000.00 USD | 111.95 USD | 0.00 USD | `+78.15%` | `7.11` |
| `Live` | `Short` | `16.29` | 1,410,000.00 USD | 263,950.00 USD | 0.00 USD | `+84.26%` | `16,208.00` |
| `Live` | `Short` | `16.46` | 1,440,000.00 USD | 22,620.00 USD | 0.00 USD | `+86.29%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,440,000.00 USD | 190.91 USD | 0.00 USD | `+86.86%` | `11.56` |
| `Live` | `Short` | `16.75` | 1,520,000.00 USD | 84,520.00 USD | 0.00 USD | `+89.46%` | `5,047.35` |
| `Live` | `Short` | `16.77` | 1,520,000.00 USD | 340.87 USD | 0.00 USD | `+89.80%` | `20.32` |
| `Live` | `Short` | `17.02` | 1,520,000.00 USD | 191.87 USD | 0.00 USD | `+92.63%` | `11.27` |
| `Live` | `Short` | `17.14` | 1,520,000.00 USD | 1,710.00 USD | 0.00 USD | `+93.87%` | `100.00` |
| `Live` | `Short` | `17.46` | 1,520,000.00 USD | 101.47 USD | 0.00 USD | `+97.61%` | `5.81` |
| `Live` | `Short` | `17.62` | 1,530,000.00 USD | 4,120.00 USD | 0.00 USD | `+99.42%` | `233.67` |
| `Live` | `Short` | `17.64` | 1,530,000.00 USD | 4,930.00 USD | 0.00 USD | `+99.64%` | `279.46` |
| `Live` | `Short` | `17.66` | 1,540,000.00 USD | 2,660.00 USD | 0.00 USD | `+99.87%` | `150.82` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 320,770.00 USD | 0.00 USD | 611.73 USD | `-73.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 320,160.00 USD | 0.00 USD | 793.75 USD | `-54.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 319,370.00 USD | 0.00 USD | 105.04 USD | `-49.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 319,260.00 USD | 0.00 USD | 67,970.00 USD | `-43.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 251,300.00 USD | 0.00 USD | 205.30 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 251,090.00 USD | 0.00 USD | 465.42 USD | `-38.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 250,630.00 USD | 0.00 USD | 349.35 USD | `-37.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 250,280.00 USD | 0.00 USD | 1,330.00 USD | `-34.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 248,950.00 USD | 0.00 USD | 493.50 USD | `-32.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 248,450.00 USD | 0.00 USD | 100.98 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 248,350.00 USD | 0.00 USD | 620.80 USD | `-32.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 247,730.00 USD | 0.00 USD | 4,160.00 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 243,580.00 USD | 0.00 USD | 6,500.00 USD | `-30.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 237,070.00 USD | 0.00 USD | 864.38 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 236,210.00 USD | 0.00 USD | 1,430.00 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 234,780.00 USD | 0.00 USD | 4,340.00 USD | `-26.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 230,440.00 USD | 0.00 USD | 5,520.00 USD | `-24.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 224,920.00 USD | 0.00 USD | 100.72 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 224,820.00 USD | 0.00 USD | 296.34 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 224,520.00 USD | 0.00 USD | 921.19 USD | `-23.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 223,600.00 USD | 0.00 USD | 709.98 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 222,890.00 USD | 0.00 USD | 262.44 USD | `-21.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 222,630.00 USD | 0.00 USD | 3,610.00 USD | `-20.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 219,010.00 USD | 0.00 USD | 6,790.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 212,220.00 USD | 0.00 USD | 9,770.00 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 202,450.00 USD | 0.00 USD | 103.46 USD | `-18.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 202,350.00 USD | 0.00 USD | 603.44 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 201,750.00 USD | 0.00 USD | 891.57 USD | `-17.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 200,860.00 USD | 0.00 USD | 2,300.00 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 198,550.00 USD | 0.00 USD | 129.58 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 198,420.00 USD | 0.00 USD | 236.19 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 198,190.00 USD | 0.00 USD | 199.39 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 197,990.00 USD | 0.00 USD | 4,730.00 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 193,260.00 USD | 0.00 USD | 37,420.00 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 155,830.00 USD | 0.00 USD | 778.49 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 155,050.00 USD | 0.00 USD | 799.83 USD | `-14.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 154,250.00 USD | 0.00 USD | 103.41 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 154,150.00 USD | 0.00 USD | 1,370.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 152,780.00 USD | 0.00 USD | 360.13 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 152,420.00 USD | 0.00 USD | 578.04 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 151,840.00 USD | 0.00 USD | 175.42 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 151,660.00 USD | 0.00 USD | 2,990.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 148,670.00 USD | 0.00 USD | 143.51 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 148,520.00 USD | 0.00 USD | 183.33 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 148,340.00 USD | 0.00 USD | 194.52 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 148,150.00 USD | 0.00 USD | 394.75 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 147,750.00 USD | 0.00 USD | 1,350.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 146,400.00 USD | 0.00 USD | 1,590.00 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 144,820.00 USD | 0.00 USD | 898.42 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 143,920.00 USD | 0.00 USD | 1,350.00 USD | `-9.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 142,570.00 USD | 0.00 USD | 7,400.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 135,180.00 USD | 0.00 USD | 123.58 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 135,050.00 USD | 0.00 USD | 2,110.00 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 132,940.00 USD | 0.00 USD | 563.85 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 132,380.00 USD | 0.00 USD | 105.14 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 132,270.00 USD | 0.00 USD | 367.76 USD | `-8.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 131,910.00 USD | 0.00 USD | 2,330.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 129,570.00 USD | 0.00 USD | 184.13 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 129,390.00 USD | 0.00 USD | 6,500.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 122,890.00 USD | 0.00 USD | 462.15 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 122,420.00 USD | 0.00 USD | 654.53 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 121,770.00 USD | 0.00 USD | 367.91 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 121,400.00 USD | 0.00 USD | 520.75 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 120,880.00 USD | 0.00 USD | 2,900.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 117,980.00 USD | 0.00 USD | 141.04 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 117,840.00 USD | 0.00 USD | 1,780.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 116,050.00 USD | 0.00 USD | 515.66 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 115,540.00 USD | 0.00 USD | 143.54 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 115,390.00 USD | 0.00 USD | 168.64 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 115,220.00 USD | 0.00 USD | 201.49 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 115,020.00 USD | 0.00 USD | 6,530.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 108,500.00 USD | 0.00 USD | 1,140.00 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 107,350.00 USD | 0.00 USD | 2,000.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 105,350.00 USD | 0.00 USD | 756.06 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 104,590.00 USD | 0.00 USD | 970.35 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 103,620.00 USD | 0.00 USD | 5,470.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 98,160.00 USD | 0.00 USD | 1,970.00 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 96,190.00 USD | 0.00 USD | 3,290.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 92,900.00 USD | 0.00 USD | 358.56 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 92,540.00 USD | 0.00 USD | 1,880.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 90,660.00 USD | 0.00 USD | 140.36 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 90,520.00 USD | 0.00 USD | 138.24 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 90,380.00 USD | 0.00 USD | 954.23 USD | `-4.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 89,430.00 USD | 0.00 USD | 769.61 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 88,660.00 USD | 0.00 USD | 489.58 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 88,170.00 USD | 0.00 USD | 1,440.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 86,730.00 USD | 0.00 USD | 198.74 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 86,530.00 USD | 0.00 USD | 1,130.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 85,400.00 USD | 0.00 USD | 132.45 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 85,270.00 USD | 0.00 USD | 428.58 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 84,840.00 USD | 0.00 USD | 2,500.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 82,340.00 USD | 0.00 USD | 435.59 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.61` | 81,900.00 USD | 0.00 USD | 1,080.00 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 80,830.00 USD | 0.00 USD | 1,980.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.62` | 78,850.00 USD | 0.00 USD | 2,740.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.63` | 76,100.00 USD | 0.00 USD | 103.19 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.64` | 76,000.00 USD | 0.00 USD | 103.31 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 75,900.00 USD | 0.00 USD | 1,900.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.66` | 73,990.00 USD | 0.00 USD | 196.87 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.68` | 73,800.00 USD | 0.00 USD | 223.82 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.69` | 73,570.00 USD | 0.00 USD | 990.09 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.70` | 72,580.00 USD | 0.00 USD | 5,010.00 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 67,570.00 USD | 0.00 USD | 6,880.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.71` | 60,690.00 USD | 0.00 USD | 134.30 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.72` | 60,550.00 USD | 0.00 USD | 390.88 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.73` | 60,160.00 USD | 0.00 USD | 1,390.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.74` | 58,770.00 USD | 0.00 USD | 933.70 USD | `-1.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.76` | 57,840.00 USD | 0.00 USD | 6,300.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.77` | 51,540.00 USD | 0.00 USD | 39,810.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.78` | 11,730.00 USD | 0.00 USD | 114.25 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 11,620.00 USD | 0.00 USD | 4,230.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.79` | 7,390.00 USD | 0.00 USD | 2,650.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.80` | 4,740.00 USD | 0.00 USD | 1,760.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.81` | 2,980.00 USD | 0.00 USD | 705.20 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.82` | 2,280.00 USD | 0.00 USD | 2,030.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.84` | 243.40 USD | 0.00 USD | 243.40 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 5,760.00 USD | 5,760.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 5,960.00 USD | 192.86 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 6,570.00 USD | 614.88 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 7,120.00 USD | 543.33 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 8,220.00 USD | 1,100.00 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 8,410.00 USD | 188.66 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 9,200.00 USD | 788.72 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 12,560.00 USD | 3,360.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 12,670.00 USD | 110.58 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 13,680.00 USD | 1,020.00 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 13,910.00 USD | 223.62 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 14,050.00 USD | 137.73 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 14,450.00 USD | 401.63 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 329,600.00 USD | 315,150.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 329,700.00 USD | 104.59 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 330,480.00 USD | 776.54 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 331,010.00 USD | 531.20 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 332,390.00 USD | 1,380.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 333,480.00 USD | 1,090.00 USD | 0.00 USD | `+2.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 334,090.00 USD | 616.37 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 334,190.00 USD | 102.03 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 334,650.00 USD | 453.84 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 334,810.00 USD | 160.99 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 335,220.00 USD | 415.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 336,730.00 USD | 1,510.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 338,770.00 USD | 2,040.00 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 566,410.00 USD | 227,630.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 569,440.00 USD | 3,030.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 571,440.00 USD | 2,000.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 965,650.00 USD | 394,210.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,000,000.00 USD | 39,130.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,010,000.00 USD | 1,590.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 3,320.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,010,000.00 USD | 131.87 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,010,000.00 USD | 687.91 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,010,000.00 USD | 954.71 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,410,000.00 USD | 398,520.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,410,000.00 USD | 205.87 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,410,000.00 USD | 1,960.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,410,000.00 USD | 434.45 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,430,000.00 USD | 18,610.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,430,000.00 USD | 354.81 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,430,000.00 USD | 2,180.00 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,430,000.00 USD | 579.86 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,760,000.00 USD | 327,430.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,760,000.00 USD | 233.38 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 163.41 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,760,000.00 USD | 1,150.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,760,000.00 USD | 660.84 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,770,000.00 USD | 2,480.00 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,770,000.00 USD | 219.84 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,770,000.00 USD | 140.35 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,770,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,770,000.00 USD | 1,780.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,770,000.00 USD | 2,210.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,770,000.00 USD | 288.46 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,780,000.00 USD | 1,600.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,780,000.00 USD | 103.54 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.56` | 1,780,000.00 USD | 535.35 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,780,000.00 USD | 231.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,780,000.00 USD | 221.07 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,780,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,780,000.00 USD | 148.48 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,780,000.00 USD | 329.43 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,780,000.00 USD | 446.58 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,780,000.00 USD | 108.21 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,780,000.00 USD | 169.68 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,780,000.00 USD | 121.87 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,780,000.00 USD | 619.28 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,790,000.00 USD | 5,030.00 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,790,000.00 USD | 340.05 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,790,000.00 USD | 742.12 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,790,000.00 USD | 899.47 USD | 0.00 USD | `+12.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,860,000.00 USD | 70,020.00 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,860,000.00 USD | 373.97 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,870,000.00 USD | 7,500.00 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,870,000.00 USD | 6,370.00 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,870,000.00 USD | 202.10 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 210,980.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 2,080,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 2,080,000.00 USD | 172.16 USD | 0.00 USD | `+15.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 2,080,000.00 USD | 868.36 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 2,090,000.00 USD | 489.40 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 2,090,000.00 USD | 1,200.00 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 2,090,000.00 USD | 118.01 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 2,090,000.00 USD | 312.31 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 2,090,000.00 USD | 1,530.00 USD | 0.00 USD | `+18.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 2,090,000.00 USD | 178.46 USD | 0.00 USD | `+19.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 2,090,000.00 USD | 153.11 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 2,090,000.00 USD | 173.42 USD | 0.00 USD | `+21.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 2,090,000.00 USD | 184.75 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 2,090,000.00 USD | 135.78 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 2,090,000.00 USD | 127.96 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 2,090,000.00 USD | 476.43 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 2,090,000.00 USD | 1,730.00 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 2,090,000.00 USD | 118.97 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 2,090,000.00 USD | 251.06 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 2,090,000.00 USD | 552.44 USD | 0.00 USD | `+23.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 2,090,000.00 USD | 1,750.00 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 2,090,000.00 USD | 320.29 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 2,100,000.00 USD | 1,100.00 USD | 0.00 USD | `+26.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 2,100,000.00 USD | 2,610.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 2,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 2,100,000.00 USD | 1,380.00 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,100,000.00 USD | 2,410.00 USD | 0.00 USD | `+29.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,110,000.00 USD | 9,520.00 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,120,000.00 USD | 3,530.00 USD | 0.00 USD | `+30.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,120,000.00 USD | 7,700.00 USD | 0.00 USD | `+31.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,130,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,130,000.00 USD | 434.61 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,130,000.00 USD | 163.52 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,250,000.00 USD | 124,300.00 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,250,000.00 USD | 2,770.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,260,000.00 USD | 3,350.00 USD | 0.00 USD | `+43.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,260,000.00 USD | 197.97 USD | 0.00 USD | `+44.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,260,000.00 USD | 3,200.00 USD | 0.00 USD | `+46.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,260,000.00 USD | 179.58 USD | 0.00 USD | `+46.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,260,000.00 USD | 720.74 USD | 0.00 USD | `+47.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,260,000.00 USD | 504.17 USD | 0.00 USD | `+47.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,260,000.00 USD | 169.57 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,260,000.00 USD | 159.66 USD | 0.00 USD | `+50.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,260,000.00 USD | 446.52 USD | 0.00 USD | `+51.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,260,000.00 USD | 1,710.00 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,270,000.00 USD | 5,320.00 USD | 0.00 USD | `+52.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,480,000.00 USD | 207,980.00 USD | 0.00 USD | `+52.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,480,000.00 USD | 407.95 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,480,000.00 USD | 174.91 USD | 0.00 USD | `+56.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,490,000.00 USD | 9,230.00 USD | 0.00 USD | `+58.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,490,000.00 USD | 960.26 USD | 0.00 USD | `+60.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,490,000.00 USD | 2,710.00 USD | 0.00 USD | `+62.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,490,000.00 USD | 805.90 USD | 0.00 USD | `+64.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,490,000.00 USD | 655.55 USD | 0.00 USD | `+66.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,500,000.00 USD | 4,890.00 USD | 0.00 USD | `+67.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,500,000.00 USD | 471.09 USD | 0.00 USD | `+68.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,500,000.00 USD | 383.85 USD | 0.00 USD | `+69.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,150,000.00 USD | 652,070.00 USD | 0.00 USD | `+69.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,150,000.00 USD | 111.87 USD | 0.00 USD | `+79.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,150,000.00 USD | 219.91 USD | 0.00 USD | `+81.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 3,150,000.00 USD | 121.74 USD | 0.00 USD | `+91.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 3,150,000.00 USD | 297.59 USD | 0.00 USD | `+92.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.18` | 3,150,000.00 USD | 4,500.00 USD | 0.00 USD | `+94.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 3,280,000.00 USD | 120,270.00 USD | 0.00 USD | `+94.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.34` | 3,280,000.00 USD | 122.39 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.50` | 3,280,000.00 USD | 586.59 USD | 0.00 USD | `+98.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.61` | 3,280,000.00 USD | 580.97 USD | 0.00 USD | `+99.19%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.81` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 16,260.00 USD | 16,110.00 USD | 0.00 USD |
| `7D` | `7.83` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 28,130.00 USD | 2,130.00 USD | 23,900.00 USD |
| `7D` | `7.85` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 15,410.00 USD | 7,840.00 USD | 6,560.00 USD |
| `7D` | `7.87` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 39,380.00 USD | 1,540.00 USD | 21,020.00 USD |
| `7D` | `7.89` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 25,450.00 USD | 18,320.00 USD | 24,180.00 USD |
| `7D` | `7.91` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 29,920.00 USD | 11,120.00 USD | 17,910.00 USD |
| `1D` | `7.92` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 16,360.00 USD | 2,950.00 USD | 11,950.00 USD |
| `1D` | `7.93` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD |
| `7D` | `7.93` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.94` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD |
| `1D` | `7.95` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 74.90 USD | 5,170.00 USD | 5,220.00 USD |
| `7D` | `7.95` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 41,590.00 USD | 9,500.00 USD | 42,480.00 USD |
| `1D` | `7.96` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 2,760.00 USD | 3,170.00 USD | 13.70 USD |
| `1D` | `7.97` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 9,050.00 USD | 1,180.00 USD | 4,040.00 USD |
| `7D` | `7.97` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 35,290.00 USD | 18,700.00 USD | 39,990.00 USD |
| `1D` | `7.98` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `1D` | `7.99` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 482.38 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.99` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 49,120.00 USD | 7,410.00 USD | 45,910.00 USD |
| `1D` | `8.00` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `1D` | `8.01` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 6,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.01` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 49,240.00 USD | 17,990.00 USD | 470.04 USD |
| `1D` | `8.02` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 9,100.00 USD | 770.83 USD | 9.39 USD |
| `1D` | `8.03` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 8,600.00 USD | 1,540.00 USD | 288.16 USD |
| `7D` | `8.03` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 104,360.00 USD | 23,930.00 USD | 48,290.00 USD |
| `1D` | `8.04` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 9,860.00 USD | 0.00 USD | 6,190.00 USD |
| `1D` | `8.05` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 14,360.00 USD | 3,770.00 USD | 330.10 USD |
| `7D` | `8.05` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 36,050.00 USD | 29,270.00 USD | 62,790.00 USD |
| `1D` | `8.06` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 12,030.00 USD | 1,700.00 USD | 5,880.00 USD |
| `1D` | `8.07` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 1,100.00 USD | 2,400.00 USD | 1,530.00 USD |
| `7D` | `8.07` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 63,920.00 USD | 10,930.00 USD | 75,680.00 USD |
| `1D` | `8.08` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 4,700.00 USD | 1,410.00 USD | 3,220.00 USD |
| `1D` | `8.09` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 9,630.00 USD | 1,220.00 USD | 6,380.00 USD |
| `7D` | `8.09` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 36,390.00 USD | 16,210.00 USD | 27,480.00 USD |
| `1D` | `8.10` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 23,830.00 USD | 3,750.00 USD | 8,060.00 USD |
| `1D` | `8.11` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 4,510.00 USD | 4,240.00 USD | 1,360.00 USD |
| `7D` | `8.11` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 36,560.00 USD | 10,160.00 USD | 7,520.00 USD |
| `1D` | `8.12` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 9,910.00 USD | 0.00 USD | 7,240.00 USD |
| `1D` | `8.13` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 7,130.00 USD | 693.45 USD | 1,310.00 USD |
| `7D` | `8.13` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 32,750.00 USD | 11,560.00 USD | 20,710.00 USD |
| `1D` | `8.14` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 16,900.00 USD | 0.00 USD | 26.83 USD |
| `1D` | `8.15` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 14,590.00 USD | 662.47 USD | 5,000.00 USD |
| `7D` | `8.15` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 91,880.00 USD | 5,090.00 USD | 46,670.00 USD |
| `1D` | `8.16` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 385.98 USD | 2,120.00 USD | 47.18 USD |
| `1D` | `8.17` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 2,970.00 USD | 0.00 USD | 12.32 USD |
| `7D` | `8.17` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 6,560.00 USD | 7,770.00 USD | 9,880.00 USD |
| `1D` | `8.18` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 1,150.00 USD | 1,980.00 USD | 466.21 USD |
| `1D` | `8.19` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 4,450.00 USD | 0.00 USD | 19.88 USD |
| `7D` | `8.19` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 30,430.00 USD | 3,170.00 USD | 2,970.00 USD |
| `1D` | `8.20` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 7,720.00 USD | 2,310.00 USD | 445.22 USD |
| `1D` | `8.21` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 2,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.21` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 22,220.00 USD | 0.00 USD | 9,790.00 USD |
| `1D` | `8.22` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 5,330.00 USD | 0.00 USD | 12,570.00 USD |
| `1D` | `8.23` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 20,920.00 USD | 4,080.00 USD | 31,000.00 USD |
| `7D` | `8.23` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 14,630.00 USD | 3,480.00 USD | 108,120.00 USD |
| `1D` | `8.24` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 10,190.00 USD | 1,150.00 USD | 3,510.00 USD |
| `1D` | `8.25` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 8,080.00 USD | 0.00 USD | 6,100.00 USD |
| `7D` | `8.25` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 55,820.00 USD | 5,750.00 USD | 9,460.00 USD |
| `1D` | `8.26` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 215.69 USD | 11,460.00 USD | 0.00 USD |
| `1D` | `8.27` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 11,310.00 USD | 2,760.00 USD | 21.52 USD |
| `7D` | `8.27` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 65,020.00 USD | 14,400.00 USD | 1,220.00 USD |
| `1D` | `8.28` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 74,500.00 USD | 7,070.00 USD | 40,790.00 USD |
| `1D` | `8.29` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 34,850.00 USD | 9,470.00 USD | 4,640.00 USD |
| `7D` | `8.29` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 116,340.00 USD | 19,520.00 USD | 52,950.00 USD |
| `1D` | `8.30` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 53,200.00 USD | 13,130.00 USD | 19,010.00 USD |
| `1D` | `8.31` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 56,000.00 USD | 11,410.00 USD | 1,570.00 USD |
| `7D` | `8.31` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 80,550.00 USD | 13,500.00 USD | 10,760.00 USD |
| `1D` | `8.32` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 19,380.00 USD | 4,190.00 USD | 7,320.00 USD |
| `1D` | `8.33` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 2,970.00 USD | 22,580.00 USD | 9,950.00 USD |
| `7D` | `8.33` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 58,510.00 USD | 36,210.00 USD | 19,880.00 USD |
| `1D` | `8.34` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 14,500.00 USD | 4,810.00 USD | 6,270.00 USD |
| `1D` | `8.35` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 6,790.00 USD | 11,270.00 USD | 16,090.00 USD |
| `7D` | `8.35` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 95,370.00 USD | 5,340.00 USD | 82,090.00 USD |
| `1D` | `8.36` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 4,090.00 USD | 2,420.00 USD | 21,790.00 USD |
| `1D` | `8.37` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 21,970.00 USD | 7,980.00 USD | 8,330.00 USD |
| `7D` | `8.37` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 92,990.00 USD | 31,220.00 USD | 24,200.00 USD |
| `1D` | `8.38` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 36,140.00 USD | 4,080.00 USD | 33,870.00 USD |
| `1D` | `8.39` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 63,440.00 USD | 10,540.00 USD | 56,460.00 USD |
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
| `1D` | `8.50` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 64,670.00 USD | 11,120.00 USD | 28,360.00 USD |
| `1D` | `8.51` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 16,530.00 USD | 48,100.00 USD | 21,930.00 USD |
| `7D` | `8.51` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 227,050.00 USD | 129,490.00 USD | 139,240.00 USD |
| `1D` | `8.52` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 48,940.00 USD | 17,250.00 USD | 23,600.00 USD |
| `1D` | `8.53` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 17,330.00 USD | 29,630.00 USD | 41,670.00 USD |
| `7D` | `8.53` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 414,730.00 USD | 72,650.00 USD | 328,520.00 USD |
| `1D` | `8.54` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 19,400.00 USD | 6,040.00 USD | 43,640.00 USD |
| `1D` | `8.55` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 64,630.00 USD | 19,250.00 USD | 19,190.00 USD |
| `7D` | `8.55` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 279,560.00 USD | 136,440.00 USD | 16,520.00 USD |
| `1D` | `8.56` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 69,420.00 USD | 12,010.00 USD | 67,740.00 USD |
| `1D` | `8.57` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 73,460.00 USD | 11,140.00 USD | 73,570.00 USD |
| `7D` | `8.57` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 709,710.00 USD | 94,290.00 USD | 76,290.00 USD |
| `1D` | `8.58` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 87,680.00 USD | 21,440.00 USD | 39,900.00 USD |
| `1D` | `8.59` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 70,460.00 USD | 29,830.00 USD | 25,420.00 USD |
| `7D` | `8.59` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 279,060.00 USD | 118,220.00 USD | 87,630.00 USD |
| `1D` | `8.60` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 68,090.00 USD | 23,230.00 USD | 39,600.00 USD |
| `1D` | `8.61` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 35,340.00 USD | 12,770.00 USD | 15,710.00 USD |
| `7D` | `8.61` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 88,710.00 USD | 35,810.00 USD | 229,070.00 USD |
| `1D` | `8.62` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 102,610.00 USD | 23,160.00 USD | 30,620.00 USD |
| `1D` | `8.63` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 77,860.00 USD | 21,050.00 USD | 12,350.00 USD |
| `7D` | `8.63` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 51,260.00 USD | 25,450.00 USD | 23,830.00 USD |
| `1D` | `8.64` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 105,620.00 USD | 11,790.00 USD | 19,190.00 USD |
| `1D` | `8.65` | 950,410.00 USD | 0.00 USD | 950,410.00 USD | 50,810.00 USD | 31,510.00 USD | 33,100.00 USD |
| `7D` | `8.65` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 163,720.00 USD | 16,520.00 USD | 57,810.00 USD |
| `1D` | `8.66` | 834,990.00 USD | 0.00 USD | 834,990.00 USD | 74,110.00 USD | 26,760.00 USD | 15,000.00 USD |
| `1D` | `8.67` | 719,120.00 USD | 0.00 USD | 719,120.00 USD | 59,230.00 USD | 5,480.00 USD | 27,430.00 USD |
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
| `1D` | `9.03` | 425,580.00 USD | 425,580.00 USD | 0.00 USD | 54,730.00 USD | 28,060.00 USD | 27,430.00 USD |
| `7D` | `9.03` | 626,990.00 USD | 626,990.00 USD | 0.00 USD | 58,760.00 USD | 101,140.00 USD | 15,140.00 USD |
| `1D` | `9.04` | 466,400.00 USD | 466,400.00 USD | 0.00 USD | 18,960.00 USD | 10,710.00 USD | 11,160.00 USD |
| `1D` | `9.05` | 534,700.00 USD | 534,700.00 USD | 0.00 USD | 3,520.00 USD | 26,530.00 USD | 38,250.00 USD |
| `7D` | `9.05` | 719,540.00 USD | 719,540.00 USD | 0.00 USD | 35,720.00 USD | 17,700.00 USD | 39,130.00 USD |
| `1D` | `9.06` | 586,030.00 USD | 586,030.00 USD | 0.00 USD | 27,120.00 USD | 2,420.00 USD | 21,790.00 USD |
| `1D` | `9.07` | 650,040.00 USD | 650,040.00 USD | 0.00 USD | 14,580.00 USD | 22,140.00 USD | 27,290.00 USD |
| `7D` | `9.07` | 759,900.00 USD | 759,900.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 22,240.00 USD |
| `1D` | `9.08` | 691,660.00 USD | 691,660.00 USD | 0.00 USD | 1,260.00 USD | 6,490.00 USD | 33,870.00 USD |
| `1D` | `9.09` | 850,220.00 USD | 850,220.00 USD | 0.00 USD | 99,950.00 USD | 17,120.00 USD | 41,490.00 USD |
| `7D` | `9.09` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 150,640.00 USD | 8,680.00 USD | 134,960.00 USD |
| `1D` | `9.10` | 945,530.00 USD | 945,530.00 USD | 0.00 USD | 66,840.00 USD | 22,440.00 USD | 6,030.00 USD |
| `1D` | `9.11` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 51,780.00 USD | 9,610.00 USD | 49,760.00 USD |
| `7D` | `9.11` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 847,950.00 USD | 37,620.00 USD | 546,100.00 USD |
| `1D` | `9.12` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 106,750.00 USD | 31,620.00 USD | 6,270.00 USD |
| `1D` | `9.13` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 84,020.00 USD | 20,120.00 USD | 40,100.00 USD |
| `7D` | `9.13` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 690,230.00 USD | 26,540.00 USD | 484,570.00 USD |
| `1D` | `9.14` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 33,890.00 USD | 8,440.00 USD | 27,230.00 USD |
| `1D` | `9.15` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 57,880.00 USD | 22,150.00 USD | 22,630.00 USD |
| `7D` | `9.15` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 249,190.00 USD |
| `1D` | `9.16` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 63,210.00 USD | 18,910.00 USD | 29,260.00 USD |
| `1D` | `9.17` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 107,540.00 USD | 18,740.00 USD | 59,770.00 USD |
| `7D` | `9.17` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 408,450.00 USD | 133,490.00 USD | 285,100.00 USD |
| `1D` | `9.18` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 151,850.00 USD | 40,170.00 USD | 65,100.00 USD |
| `1D` | `9.19` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 97,890.00 USD | 40,200.00 USD | 17,030.00 USD |
| `7D` | `9.19` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 503,250.00 USD | 101,150.00 USD | 193,560.00 USD |
| `1D` | `9.20` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 119,740.00 USD | 10,810.00 USD | 67,770.00 USD |
| `1D` | `9.21` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 48,600.00 USD | 6,420.00 USD | 9,160.00 USD |
| `7D` | `9.21` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 554,780.00 USD | 132,850.00 USD | 277,380.00 USD |
| `1D` | `9.22` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 93,870.00 USD | 10,040.00 USD | 11,100.00 USD |
| `1D` | `9.23` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 57,020.00 USD | 3,310.00 USD | 33,950.00 USD |
| `7D` | `9.23` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 562,300.00 USD | 88,460.00 USD | 371,360.00 USD |
| `1D` | `9.24` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 31,050.00 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `9.25` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 18,710.00 USD | 17,700.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 277,290.00 USD | 73,690.00 USD | 141,060.00 USD |
| `1D` | `9.26` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 16,250.00 USD | 1,210.00 USD | 0.00 USD |
| `1D` | `9.27` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 22,870.00 USD | 13,170.00 USD | 2,560.00 USD |
| `7D` | `9.27` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 156,190.00 USD | 118,550.00 USD | 54,650.00 USD |
| `1D` | `9.28` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 20,250.00 USD | 3,860.00 USD | 27.40 USD |
| `1D` | `9.29` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 48,970.00 USD | 15,680.00 USD | 17,930.00 USD |
| `7D` | `9.29` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 468,150.00 USD | 100,200.00 USD | 290,740.00 USD |
| `1D` | `9.30` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 42,450.00 USD | 9,410.00 USD | 26.83 USD |
| `1D` | `9.31` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 27,590.00 USD | 4,250.00 USD | 25,510.00 USD |
| `7D` | `9.31` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 307,520.00 USD | 55,090.00 USD | 275,740.00 USD |
| `1D` | `9.32` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 9,610.00 USD | 2,530.00 USD | 10,830.00 USD |
| `1D` | `9.33` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 7,010.00 USD | 6,000.00 USD | 4,480.00 USD |
| `7D` | `9.33` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 124,660.00 USD | 64,710.00 USD | 178,910.00 USD |
| `1D` | `9.34` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 15,860.00 USD | 4,190.00 USD | 12,940.00 USD |
| `1D` | `9.35` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 28,980.00 USD | 3,810.00 USD | 24,920.00 USD |
| `7D` | `9.35` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 289,480.00 USD | 93,460.00 USD | 96,160.00 USD |
| `1D` | `9.36` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 66,220.00 USD | 13,630.00 USD | 25,050.00 USD |
| `1D` | `9.37` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 36,610.00 USD | 13,410.00 USD | 6,010.00 USD |
| `7D` | `9.37` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 369,360.00 USD | 34,660.00 USD | 70,260.00 USD |
| `1D` | `9.38` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 47,540.00 USD | 4,040.00 USD | 27,030.00 USD |
| `1D` | `9.39` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 16,910.00 USD | 1,730.00 USD | 3,240.00 USD |
| `7D` | `9.39` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 206,980.00 USD | 62,160.00 USD | 87,830.00 USD |
| `1D` | `9.40` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 44,280.00 USD | 1,210.00 USD | 12.64 USD |
| `1D` | `9.41` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 29,300.00 USD | 1,660.00 USD | 16,970.00 USD |
| `7D` | `9.41` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 265,320.00 USD | 41,500.00 USD | 147,960.00 USD |
| `1D` | `9.42` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 10,620.00 USD | 622.99 USD | 4,010.00 USD |
| `1D` | `9.43` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 10,390.00 USD | 6,940.00 USD | 12,410.00 USD |
| `7D` | `9.43` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 101,970.00 USD | 43,920.00 USD | 95,890.00 USD |
| `1D` | `9.44` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,530.00 USD | 0.00 USD | 48.84 USD |
| `1D` | `9.45` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 1,380.00 USD | 4,940.00 USD | 2,430.00 USD |
| `7D` | `9.45` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 105,560.00 USD | 16,970.00 USD | 9,710.00 USD |
| `1D` | `9.46` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 1,320.00 USD | 4,580.00 USD | 0.00 USD |
| `1D` | `9.47` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 18,220.00 USD | 6,870.00 USD | 192.20 USD |
| `7D` | `9.47` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 53,420.00 USD | 27,650.00 USD | 25,670.00 USD |
| `1D` | `9.48` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 5,190.00 USD |
| `1D` | `9.49` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 21,080.00 USD | 572.85 USD | 5,600.00 USD |
| `7D` | `9.49` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 26,920.00 USD | 36,710.00 USD | 16,150.00 USD |
| `1D` | `9.50` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 11,990.00 USD | 3,160.00 USD | 6,320.00 USD |
| `1D` | `9.51` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 295.05 USD | 0.00 USD | 124.70 USD |
| `7D` | `9.51` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 131,270.00 USD | 43,360.00 USD | 122,810.00 USD |
| `1D` | `9.52` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 17,180.00 USD | 3,070.00 USD | 5,400.00 USD |
| `1D` | `9.53` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 18,780.00 USD | 4,560.00 USD | 0.00 USD |
| `7D` | `9.53` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 187,750.00 USD | 15,360.00 USD | 6,760.00 USD |
| `1D` | `9.54` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 5,910.00 USD | 1,470.00 USD | 2,930.00 USD |
| `1D` | `9.55` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 2,910.00 USD | 6,330.00 USD | 3,100.00 USD |
| `7D` | `9.55` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 28,850.00 USD | 19,960.00 USD | 880.26 USD |
| `1D` | `9.56` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 4,750.00 USD | 1,280.00 USD | 2,530.00 USD |
| `1D` | `9.57` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 1,370.00 USD | 3,100.00 USD | 4,950.00 USD |
| `7D` | `9.57` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 114,070.00 USD | 14,280.00 USD | 33,260.00 USD |
| `1D` | `9.58` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 1,290.00 USD | 563.17 USD | 7,730.00 USD |
| `1D` | `9.59` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 5,050.00 USD | 1,250.00 USD | 1,170.00 USD |
| `7D` | `9.59` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 26,920.00 USD | 15,650.00 USD | 23,150.00 USD |
| `1D` | `9.60` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 11,210.00 USD | 424.36 USD | 11,260.00 USD |
| `1D` | `9.61` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 13,300.00 USD | 2,670.00 USD | 11,670.00 USD |
| `7D` | `9.61` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 82,080.00 USD | 13,850.00 USD | 28,920.00 USD |
| `1D` | `9.62` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.63` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 10,190.00 USD | 4,370.00 USD | 1,150.00 USD |
| `7D` | `9.63` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 42,830.00 USD | 4,500.00 USD | 6,980.00 USD |
| `1D` | `9.64` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,410.00 USD |
| `1D` | `9.65` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 5,960.00 USD | 4,150.00 USD | 1,740.00 USD |
| `7D` | `9.65` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 33,020.00 USD | 20,230.00 USD | 18,210.00 USD |
| `1D` | `9.66` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 8,930.00 USD | 3,480.00 USD | 5,760.00 USD |
| `1D` | `9.67` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `9.67` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 31,000.00 USD | 24,380.00 USD | 18,390.00 USD |
| `1D` | `9.68` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 13,160.00 USD | 2,950.00 USD | 3,970.00 USD |
| `1D` | `9.69` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 7,960.00 USD | 2,710.00 USD | 0.00 USD |
| `7D` | `9.69` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 121,550.00 USD | 17,380.00 USD | 33,860.00 USD |
| `1D` | `9.70` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 11,440.00 USD | 4,150.00 USD | 3,350.00 USD |
| `1D` | `9.71` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 74.90 USD | 5,170.00 USD | 5,250.00 USD |
| `7D` | `9.71` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 92,070.00 USD | 9,500.00 USD | 42,550.00 USD |
| `1D` | `9.72` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 2,760.00 USD | 3,170.00 USD | 57.27 USD |
| `7D` | `9.73` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 3,060.00 USD | 3,160.00 USD | 11,750.00 USD |
| `1D` | `9.74` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 5,260.00 USD | 0.00 USD | 3,140.00 USD |
| `1D` | `9.75` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 3,790.00 USD | 1,180.00 USD | 946.22 USD |
| `7D` | `9.75` | 14,480,000.00 USD | 14,480,000.00 USD | 0.00 USD | 35,970.00 USD | 15,540.00 USD | 29,890.00 USD |
| `1D` | `9.76` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 3,610.00 USD | 1,380.00 USD | 4,440.00 USD |
| `7D` | `9.77` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 51,320.00 USD | 7,410.00 USD | 46,350.00 USD |
| `1D` | `9.78` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 1,840.00 USD | 1,790.00 USD |
| `1D` | `9.79` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.79` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 48,830.00 USD | 17,990.00 USD | 729.68 USD |
| `7D` | `9.81` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 103,830.00 USD | 23,930.00 USD | 48,340.00 USD |
| `7D` | `9.83` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 31,840.00 USD | 29,270.00 USD | 62,530.00 USD |
| `7D` | `9.85` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 50,490.00 USD | 2,210.00 USD | 49,830.00 USD |
| `7D` | `9.87` | 15,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | 15,580.00 USD | 8,710.00 USD | 25,970.00 USD |
| `7D` | `9.89` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 33,970.00 USD | 16,210.00 USD | 27,630.00 USD |
| `7D` | `9.91` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 32,670.00 USD | 10,160.00 USD | 7,620.00 USD |
| `7D` | `9.93` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 31,960.00 USD | 11,560.00 USD | 20,650.00 USD |
| `7D` | `9.95` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 55,780.00 USD | 3,730.00 USD | 24,820.00 USD |
| `7D` | `9.97` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 21,720.00 USD |
| `7D` | `9.99` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 840.10 USD | 7,770.00 USD | 8,430.00 USD |
| `7D` | `10.01` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 15,620.00 USD | 3,170.00 USD | 0.00 USD |
| `7D` | `10.03` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `382.07M` | Total OI Tokens: `43,190,033.6 AVAX`
  * 1h OI Change: `+0.17%` | 4h OI Change: `-0.90%` | 24h OI Change: `-2.86%`
  * Exchange Breakdown: Binance=`89.66M` | Bybit=`59.50M` | OKX=`12.73M` | Hyperliquid=`17.59M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.89K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0054%` | **USDT KuCoin** | `0.0099%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0045%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `55.36%` | `44.64%` | `1.24` | 5,910,000.00 USD |
| `15M` | `Binance` | `58.1%` | `41.9%` | `1.39` | 1,320,000.00 USD |
| `15M` | `OKX` | `88.76%` | `11.24%` | `7.90` | 879,760.00 USD |
| `15M` | `Bybit` | `71.71%` | `28.29%` | `2.53` | 265,600.00 USD |
| `15M` | `KuCoin` | `18.82%` | `81.18%` | `0.23` | 16,350.00 USD |
| `15M` | `Gate` | `40.53%` | `59.47%` | `0.68` | 128,260.00 USD |
| `15M` | `Bitget` | `56.2%` | `43.8%` | `1.28` | 286,540.00 USD |
| `15M` | `BingX` | `45.43%` | `54.57%` | `0.83` | 119,600.00 USD |
| `15M` | `MEXC` | `44.25%` | `55.75%` | `0.79` | 2,260,000.00 USD |
| `15M` | `Bitunix` | `67.07%` | `32.93%` | `2.04` | 132,310.00 USD |
| `15M` | `Hyperliquid` | `27.93%` | `72.07%` | `0.39` | 139,220.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.55%` | `48.45%` | `1.06` | 136,630.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.47%` | `99.53%` | `0.00` | 155,650.00 USD |
| `15M` | `HTX` | `57.13%` | `42.87%` | `1.33` | 5,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `92.9%` | `7.1%` | `13.08` | 34,960.00 USD |
| `15M` | `Aster` | `92.86%` | `7.14%` | `13.01` | 231.34 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `95.02%` | `4.98%` | `19.08` | 31,730.00 USD |
| `15M` | `Whale Positions` | `58.1%` | `41.9%` | `1.39` | 1,320,000.00 USD |
| `15M` | `Global Accounts` | `55.36%` | `44.64%` | `1.24` | 5,910,000.00 USD |
| `1H` | `AVAX` | `43.22%` | `56.78%` | `0.76` | 2,460,000.00 USD |
| `1H` | `Binance` | `56.22%` | `43.78%` | `1.28` | 697,010.00 USD |
| `1H` | `OKX` | `47.63%` | `52.37%` | `0.91` | 158,140.00 USD |
| `1H` | `Bybit` | `83.46%` | `16.54%` | `5.05` | 126,280.00 USD |
| `1H` | `KuCoin` | `49.5%` | `50.5%` | `0.98` | 66,060.00 USD |
| `1H` | `Gate` | `56.08%` | `43.92%` | `1.28` | 81,810.00 USD |
| `1H` | `Bitget` | `66.13%` | `33.87%` | `1.95` | 11,380.00 USD |
| `1H` | `BingX` | `19.5%` | `80.5%` | `0.24` | 324,030.00 USD |
| `1H` | `MEXC` | `68.59%` | `31.41%` | `2.18` | 20,140.00 USD |
| `1H` | `Bitunix` | `56.68%` | `43.32%` | `1.31` | 18,840.00 USD |
| `1H` | `Hyperliquid` | `86.77%` | `13.23%` | `6.56` | 15,650.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.43%` | `51.57%` | `0.94` | 421,660.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `16.14%` | `83.86%` | `0.19` | 427,450.00 USD |
| `1H` | `HTX` | `55.04%` | `44.96%` | `1.22` | 47,600.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.45%` | `48.55%` | `1.06` | 6,940.00 USD |
| `1H` | `Aster` | `8.09%` | `91.91%` | `0.09` | 585.76 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0.36%` | `99.64%` | `0.00` | 36,140.00 USD |
| `1H` | `Whale Positions` | `56.22%` | `43.78%` | `1.28` | 697,010.00 USD |
| `1H` | `Global Accounts` | `43.22%` | `56.78%` | `0.76` | 2,460,000.00 USD |
| `4H` | `AVAX` | `43.57%` | `56.43%` | `0.77` | 76,640,000.00 USD |
| `4H` | `Binance` | `44.94%` | `55.06%` | `0.82` | 23,990,000.00 USD |
| `4H` | `OKX` | `43.47%` | `56.53%` | `0.77` | 5,270,000.00 USD |
| `4H` | `Bybit` | `49.17%` | `50.83%` | `0.97` | 3,970,000.00 USD |
| `4H` | `KuCoin` | `47.62%` | `52.38%` | `0.91` | 610,850.00 USD |
| `4H` | `Gate` | `51.52%` | `48.48%` | `1.06` | 1,400,000.00 USD |
| `4H` | `Bitget` | `43.47%` | `56.53%` | `0.77` | 1,410,000.00 USD |
| `4H` | `BingX` | `44.97%` | `55.03%` | `0.82` | 14,720,000.00 USD |
| `4H` | `MEXC` | `51.43%` | `48.57%` | `1.06` | 4,350,000.00 USD |
| `4H` | `Bitunix` | `51.3%` | `48.7%` | `1.05` | 2,810,000.00 USD |
| `4H` | `Hyperliquid` | `47.35%` | `52.65%` | `0.90` | 530,460.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.04%` | `48.96%` | `1.04` | 11,660,000.00 USD |
| `4H` | `Crypto.com` | `84.65%` | `15.35%` | `5.51` | 14,760.00 USD |
| `4H` | `WhiteBIT` | `0.06%` | `99.94%` | `0.00` | 5,440,000.00 USD |
| `4H` | `HTX` | `27.06%` | `72.94%` | `0.37` | 22,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.9%` | `51.1%` | `0.96` | 254,730.00 USD |
| `4H` | `Aster` | `50.04%` | `49.96%` | `1.00` | 119,820.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.46%` | `46.54%` | `1.15` | 58,670.00 USD |
| `4H` | `Whale Positions` | `44.94%` | `55.06%` | `0.82` | 23,990,000.00 USD |
| `4H` | `Global Accounts` | `43.57%` | `56.43%` | `0.77` | 76,640,000.00 USD |


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
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.86` | `8.84` | 151,926.57 USD | 84,569.22 USD | 67,357.35 USD | 17,211.87 USD | `+11.33%` | `5B / 2S` |

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
| `5m` | -7,280.00 USD | 113,150.00 USD | **`ACCUMULATION`** |
| `15m` | -95,620.00 USD | 342,110.00 USD | **`ACCUMULATION`** |
| `30m` | -75,560.00 USD | 484,590.00 USD | **`ACCUMULATION`** |
| `1h` | -106,380.00 USD | 867,580.00 USD | **`ACCUMULATION`** |
| `2h` | -30,530.00 USD | 543,190.00 USD | **`ACCUMULATION`** |
| `4h` | -180,030.00 USD | -3,080,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 133,500.00 USD | -2,630,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 1,080.00 USD | -2,490,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -190,210.00 USD | -2,440,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -273,070.00 USD | -4,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,790,000.00 USD | -42,290,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -52,980,000.00 USD | -272,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-7.28K` | 15m=`-95.62K` | 1h=`-106.38K` | 24h=`-273.07K`
* Futures Capital Netflows: 5m=`+113.15K` | 15m=`+342.11K` | 1h=`+867.58K` | 24h=`-4.63M`
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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `8.47` (Risk Distance: `0.1087` pts)
  * +2.5R Take Profit: `8.85`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `9.02` (Risk Distance: `0.1087` pts)
  * +2.5R Take Profit: `8.64`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.92`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
