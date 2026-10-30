# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:51:22 IST` (`2026-10-30 10:21:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.46` | **Live Ask Quote**: `8.50` | **Mid Price**: `8.48`
- **Spread Points**: `4.00` | **Spread BPS**: `47.17 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.33` | VWAP Z-Score: `+0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0555` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.87` | Lower -3.00σ Band: `7.80`
  * Upper +2.51σ Band: `8.78` | Lower -2.51σ Band: `7.89`
  * Upper +2.01σ Band: `8.69` | Lower -2.01σ Band: `7.98`
  * Upper +2.00σ Band: `8.69` | Lower -2.00σ Band: `7.98`
  * Upper +1.28σ Band: `8.56` | Lower -1.28σ Band: `8.11`
  * Upper +1.00σ Band: `8.51` | Lower -1.00σ Band: `8.16`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.46` | EMA-20=`8.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.48` (Slope: `+0.0000`) | EMA-100=`8.55`
  * Institutional Anchors: EMA-144=`8.60` | EMA-200=`8.65` (Slope: `-0.2808`) | EMA-233=`8.68`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.59` (Distance: `-1.26%`)
  * Point of Control (POC) = `8.46` (Distance: `+0.31%`)
  * Value Area Low (VAL) = `8.24` (Distance: `+2.91%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.68`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.47` | Low=`8.43`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.45` - `8.51`
  * Optimal Trade Entry (OTE 0.705): `8.50`
  * Structural Invalidation Anchor (0.786): `8.55`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.48` | `8.49` | `8.48` | `8.48` | `24,685` | 209,364.45 USD | 37,960.70 USD | `+18.13%` | -5,645,652.28 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `8.48` | `8.48` | `8.47` | `8.48` | `19,016` | 161,165.41 USD | -18,956.74 USD | `-11.76%` | -5,664,609.02 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.48` | `8.49` | `8.48` | `8.49` | `6,855` | 58,198.62 USD | 49,961.52 USD | `+85.85%` | -5,614,647.50 USD | `+0.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.47` | `8.49` | `8.46` | `8.49` | `107,294` | 909,192.14 USD | -168,371.60 USD | `-18.52%` | -5,589,912.36 USD | `-0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.49` | `8.49` | `8.46` | `8.48` | `97,292` | 824,624.01 USD | -8,463.75 USD | `-1.03%` | -5,598,376.11 USD | `+0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `8.48` | `8.49` | `8.47` | `8.49` | `25,875` | 219,398.00 USD | 31,038.75 USD | `+14.15%` | -5,567,337.36 USD | `+0.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.50` | `8.52` | `8.45` | `8.48` | `439,030` | 3,723,872.89 USD | -159,958.73 USD | `-4.30%` | -5,704,358.65 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.48` | `8.51` | `8.44` | `8.49` | `406,103` | 3,439,281.91 USD | -233,726.45 USD | `-6.80%` | -5,938,085.10 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.49` | `8.49` | `8.46` | `8.49` | `123,167` | 1,044,022.01 USD | 22,575.00 USD | `+2.16%` | -5,915,510.10 USD | `+0.18` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.44` | `8.49` | `968,300` | 8,207,176.80 USD | -371,110.18 USD | `-4.52%` | -5,775,950.18 USD | `+0.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.44` | `8.49` | `968,300` | 8,207,176.80 USD | -371,110.18 USD | `-4.52%` | -5,775,950.18 USD | `+0.41` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.48`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.48` | `150.1200` | 1,273.75 USD | 20,419.62 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.48` | `117.8600` | 999.96 USD | 21,419.58 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.48` | `170.0100` | 1,442.40 USD | 22,861.98 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.48` | `120.0800` | 1,018.73 USD | 23,880.71 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.48` | `89.7800` | 761.65 USD | 24,642.36 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.48` | `1652.6700` | 14,019.93 USD | 38,662.29 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.48` | `707.3100` | 5,999.90 USD | 44,662.19 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.48` | `67.2600` | 570.54 USD | 45,232.73 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.48` | `89.7200` | 761.04 USD | 45,993.77 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.48` | `294.7400` | 2,499.98 USD | 48,493.75 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.48` | `943.1800` | 7,999.86 USD | 56,493.62 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.48` | `89.7200` | 760.98 USD | 57,254.59 USD | `1 orders` | `-0.09%` | `-` |
| `ASK` | `8.49` | `1652.6700` | 14,039.43 USD | 78,865.71 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.49` | `89.7200` | 762.16 USD | 64,826.28 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.49` | `89.7200` | 762.10 USD | 64,064.12 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.49` | `79.7800` | 677.66 USD | 63,302.02 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.49` | `47.3100` | 401.85 USD | 62,624.36 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `60.3400` | 512.52 USD | 62,222.51 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `1.9200` | 16.31 USD | 61,709.99 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `1412.8100` | 11,999.98 USD | 61,693.68 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `89.7200` | 762.04 USD | 49,693.70 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.49` | `2.9000` | 24.63 USD | 48,931.66 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `120.0800` | 1,019.83 USD | 48,907.03 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `1648.4900` | 14,000.30 USD | 47,887.20 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `517.1400` | 4,391.91 USD | 33,886.91 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `76.8900` | 652.98 USD | 29,494.99 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.49` | `2950.3600` | 25,055.34 USD | 28,842.01 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `8.49` | `89.7200` | 761.91 USD | 3,786.67 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.49` | `150.9200` | 1,281.61 USD | 3,024.76 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.49` | `25.8500` | 219.51 USD | 1,743.14 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.49` | `89.7200` | 761.85 USD | 1,523.63 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.49` | `89.7200` | 761.79 USD | 761.79 USD | `1 orders` | `+0.02%` | `-` |
| `MID_SPREAD` | `8.49` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.49` | `0.00%` | `-` |
| `BID` | `8.49` | `149.7100` | 1,270.74 USD | 1,270.74 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.49` | `89.7200` | 761.45 USD | 2,032.19 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.49` | `18.8400` | 159.89 USD | 2,192.08 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.49` | `89.7200` | 761.37 USD | 2,953.45 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.49` | `89.7200` | 761.35 USD | 3,714.81 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.49` | `1652.6700` | 14,024.23 USD | 17,739.04 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.49` | `159.9900` | 1,357.61 USD | 19,096.65 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.49` | `5.8000` | 49.22 USD | 19,145.86 USD | `2 orders` | `-0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1471` | `0x7737...bf66` | `SHORT` | 1,454,639.80 USD | `171,568.06` | `7.43` | `8.48` | `111.79` | -179,094.78 USD | `-12.31%` | `10X Cross` |
| `1573` | `0xeadc...9d55` | `LONG` | 1,357,254.29 USD | `160,070.56` | `8.11` | `8.48` | `0.000000` | 59,616.71 USD | `+4.39%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.78` | 14,595.44 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 14.60K USD at 8.7827 USD [API] | `2026-10-29 10:57:18` |
| `ANNOUNCEMENT` | `INFO` | `8.79` | 5,023.36 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.02K USD at 8.7907 USD [API] | `2026-10-29 11:52:34` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,295.54 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 5.30K USD at 8.8074 USD [API] | `2026-10-29 13:20:34` |
| `ANNOUNCEMENT` | `INFO` | `8.80` | 7,335.21 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 7.34K USD at 8.8043 USD [API] | `2026-10-29 13:27:49` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,999.91 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8138 USD [API] | `2026-10-29 14:01:56` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,668.07 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.67K USD at 8.8149 USD [API] | `2026-10-29 14:01:46` |
| `ANNOUNCEMENT` | `INFO` | `8.82` | 9,104.31 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 9.10K USD at 8.8185 USD [API] | `2026-10-29 14:07:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.31%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.03%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.24%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.05%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.24%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.05%`)
  * 7D Horizon: Short MP=`9.23` (Vol: 459,400.00 USD, Dist: `+8.79%`) | Long MP=`8.31` (Vol: 495,000.00 USD, Dist: `--2.01%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.83` | 128.45 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 232.92 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 229.43 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 382.57 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,760.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 254.72 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 260.48 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 619.05 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 381.37 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 928.98 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 151.06 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 2,220.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 103.38 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 22,950.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 12,840.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 24,520.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 604.95 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 2,240.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.09` | 1,640.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.12` | 2,740.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.16` | 8,310.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.30` | 401.74 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 3,420.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.80` | 2,400.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 482.71 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 554.95 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 219.44 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 915.43 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 998.35 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 119.83 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 801.81 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.22` | 122.58 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 213.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,780.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.28` | 160,550.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.38` | 259.66 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 1,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,560.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 1,540.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 147.55 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.99` | 1,400.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,530.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 2,450.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 6,550.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.39` | 5,940.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 1,510.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 361,860.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 810,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 809,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 809,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 2,870.00 USD | 800,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 797,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 795,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 794,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.66` | 1,540.00 USD | 794,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 2,850.00 USD | 792,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 790,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 15,800.00 USD | 786,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 11,000.00 USD | 771,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 760,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 753,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 752,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,020.00 USD | 744,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,170.00 USD | 722,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 717,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 715,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 271.02 USD | 708,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 708,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 263.66 USD | 705,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 704,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 703,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 702,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 699,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 698,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 691,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 691,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 562,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 561,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 540,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 538,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 515,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 508,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 507,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 505,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 476,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 13,410.00 USD | 476,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.14` | 6,480,000.00 USD | 6,480,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 462,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.16` | 6,370,000.00 USD | 6,370,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 442,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.18` | 6,310,000.00 USD | 6,310,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 440,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.20` | 6,290,000.00 USD | 6,290,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 438,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.22` | 6,260,000.00 USD | 6,260,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 438,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.24` | 6,240,000.00 USD | 6,240,000.00 USD | 39,910.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 2,730.00 USD | 436,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 434,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.26` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 1,810.00 USD | 58.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 412,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 376,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.30` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.30` | 2,130.00 USD | 374,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.32` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.33` | 29,300.00 USD | 372,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.33` | 1,030.00 USD | 343,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 552.42 USD | 342,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 3,820.00 USD | 341,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 6,180,000.00 USD | 6,180,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 337,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 2,570.00 USD | 335,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 6,170,000.00 USD | 6,170,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 227.97 USD | 332,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 13,220.00 USD | 332,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 6,130,000.00 USD | 6,130,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 319,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 318,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 316,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 314,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 303,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 299,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 297,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 296,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 2,580.00 USD | 296,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.52` | 6,040,000.00 USD | 6,040,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 293,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 292,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 6,000,000.00 USD | 6,000,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,070.00 USD | 288,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 5,960,000.00 USD | 5,960,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 26,570.00 USD | 287,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 260,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,190,000.00 USD | 5,190,000.00 USD | 2,100.00 USD | 4,900.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.60` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.61` | 1,630.00 USD | 260,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,180,000.00 USD | 5,180,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 258,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,160,000.00 USD | 5,160,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 5,940,000.00 USD | 5,940,000.00 USD | 626.55 USD | 2,130.00 USD | 996.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 258,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,150,000.00 USD | 5,150,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 257,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,130,000.00 USD | 5,130,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 5,930,000.00 USD | 5,930,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 817.75 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 256,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 5,090,000.00 USD | 5,090,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 5,890,000.00 USD | 5,890,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 256,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 5,080,000.00 USD | 5,080,000.00 USD | 1,140.00 USD | 587.20 USD | 114.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 256,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 5,080,000.00 USD | 5,080,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.68` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 252,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 251,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 5,080,000.00 USD | 5,080,000.00 USD | 4,140.00 USD | 2,390.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.70` | 5,850,000.00 USD | 5,850,000.00 USD | 393.33 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 5,050,000.00 USD | 5,050,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 5,040,000.00 USD | 5,040,000.00 USD | 701.68 USD | 568.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 5,850,000.00 USD | 5,850,000.00 USD | 38,970.00 USD | 0.00 USD | 40,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 5,030,000.00 USD | 5,030,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 5,020,000.00 USD | 5,020,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 5,770,000.00 USD | 5,770,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 5,010,000.00 USD | 5,010,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 244,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 4,990,000.00 USD | 4,990,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 5,740,000.00 USD | 5,740,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 244,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 4,990,000.00 USD | 4,990,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 6,310.00 USD | 243,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 4,970,000.00 USD | 4,970,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 5,720,000.00 USD | 5,720,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 237,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,970,000.00 USD | 4,970,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 233,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 4,940,000.00 USD | 4,940,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 5,630,000.00 USD | 5,630,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 7,240.00 USD | 229,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,920,000.00 USD | 4,920,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 4,920,000.00 USD | 4,920,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 5,570,000.00 USD | 5,570,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 221,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,920,000.00 USD | 4,920,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 4,890,000.00 USD | 4,890,000.00 USD | 1,060.00 USD | 1,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 5,560,000.00 USD | 5,560,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 219,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,880,000.00 USD | 4,880,000.00 USD | 3,320.00 USD | 1,250.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 4,880,000.00 USD | 4,880,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 5,500,000.00 USD | 5,500,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 197,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,860,000.00 USD | 4,860,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 197,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 4,810,000.00 USD | 4,810,000.00 USD | 161,670.00 USD | 5,030.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 5,340,000.00 USD | 5,340,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,610,000.00 USD | 4,610,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 196,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 4,520,000.00 USD | 4,520,000.00 USD | 56,620.00 USD | 6,970.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 5,130,000.00 USD | 5,130,000.00 USD | 34,620.00 USD | 12,890.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 180,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,450,000.00 USD | 4,450,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,400,000.00 USD | 4,400,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 5,060,000.00 USD | 5,060,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 177,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,370,000.00 USD | 4,370,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 173,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,350,000.00 USD | 4,350,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 4,940,000.00 USD | 4,940,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 156,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,250,000.00 USD | 4,250,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 156,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,130,000.00 USD | 4,130,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 4,850,000.00 USD | 4,850,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,050,000.00 USD | 4,050,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 28,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,020,000.00 USD | 4,020,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 4,730,000.00 USD | 4,730,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 27,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,970,000.00 USD | 3,970,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 889.52 USD | 25,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,950,000.00 USD | 3,950,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 4,500,000.00 USD | 4,500,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,870,000.00 USD | 3,870,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,860,000.00 USD | 3,860,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 4,410,000.00 USD | 4,410,000.00 USD | 15,300.00 USD | 46,670.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 1,590.00 USD | 25,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,780,000.00 USD | 3,780,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,750,000.00 USD | 3,750,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 4,290,000.00 USD | 4,290,000.00 USD | 462,240.00 USD | 0.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,690,000.00 USD | 3,690,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,310,000.00 USD | 3,310,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 3,750,000.00 USD | 3,750,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 23,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,080,000.00 USD | 3,080,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 2,940,000.00 USD | 2,940,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 3,320,000.00 USD | 3,320,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 2,860,000.00 USD | 2,860,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 2,830,000.00 USD | 2,830,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 3,240,000.00 USD | 3,240,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 2,670,000.00 USD | 2,670,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 738.14 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 2,400,000.00 USD | 2,400,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 3,170,000.00 USD | 3,170,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 521.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,240,000.00 USD | 2,240,000.00 USD | 34,890.00 USD | 9,180.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,190,000.00 USD | 2,190,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 3,010,000.00 USD | 3,010,000.00 USD | 180,540.00 USD | 30,700.00 USD | 183,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 2,060,000.00 USD | 2,060,000.00 USD | 43,510.00 USD | 12,240.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,950,000.00 USD | 1,950,000.00 USD | 192.50 USD | 21,000.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 2,610,000.00 USD | 2,610,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 1,760,000.00 USD | 1,760,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 1,560,000.00 USD | 1,560,000.00 USD | 7,140.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 2,540,000.00 USD | 2,540,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 1,550,000.00 USD | 1,550,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 1,520,000.00 USD | 1,520,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 2,330,000.00 USD | 2,330,000.00 USD | 174,220.00 USD | 58,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 1,480,000.00 USD | 1,480,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 1,410,000.00 USD | 1,410,000.00 USD | 168.44 USD | 3,220.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 2,070,000.00 USD | 2,070,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 1,360,000.00 USD | 1,360,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 1,930,000.00 USD | 1,930,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,280,000.00 USD | 1,280,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 1,810,000.00 USD | 1,810,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,210,000.00 USD | 1,210,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,160,000.00 USD | 1,160,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 1,690,000.00 USD | 1,690,000.00 USD | 264,780.00 USD | 17,210.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,060,000.00 USD | 1,060,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 905,490.00 USD | 905,490.00 USD | 73,050.00 USD | 6,080.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 1,390,000.00 USD | 1,390,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 812,300.00 USD | 812,300.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 805,980.00 USD | 805,980.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 803,760.00 USD | 803,760.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 766,980.00 USD | 766,980.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 1,150,000.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 749,180.00 USD | 749,180.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 734,050.00 USD | 734,050.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 904,500.00 USD | 904,500.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 660,600.00 USD | 660,600.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 513,630.00 USD | 513,630.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 846,760.00 USD | 846,760.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 439,550.00 USD | 439,550.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 421,160.00 USD | 421,160.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 752,220.00 USD | 752,220.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 362,020.00 USD | 362,020.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 265,400.00 USD | 265,400.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 507,240.00 USD | 507,240.00 USD | 152,190.00 USD | 8,000.00 USD | 74,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 61,420.00 USD | 61,420.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 272,390.00 USD | 272,390.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 663.00 USD | 663.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 749.80 USD | 749.80 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 1,500.00 USD | 1,500.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 191,210.00 USD | 191,210.00 USD | 0.00 USD | 0.00 USD | 191,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 382,420.00 USD | 382,420.00 USD | 0.00 USD | 0.00 USD | 191,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.49` | 1,510.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 383,600.00 USD | 383,600.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.51` | 173,950.00 USD | 173,950.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.52` | 337,390.00 USD | 337,390.00 USD | 158,630.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 589,420.00 USD | 589,420.00 USD | 113,820.00 USD | 0.00 USD | 92,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.53` | 361,570.00 USD | 361,570.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 564,530.00 USD | 564,530.00 USD | 202,800.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 949,040.00 USD | 949,040.00 USD | 357,740.00 USD | 0.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.55` | 591,300.00 USD | 591,300.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 630,310.00 USD | 630,310.00 USD | 686.73 USD | 38,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 1,220,000.00 USD | 1,220,000.00 USD | 144,180.00 USD | 122,650.00 USD | 790.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.57` | 781,800.00 USD | 781,800.00 USD | 151,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 840,920.00 USD | 840,920.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 1,390,000.00 USD | 1,390,000.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 842,960.00 USD | 842,960.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 844,160.00 USD | 844,160.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,010,000.00 USD | 1,010,000.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 1,420,000.00 USD | 1,420,000.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 1,140,000.00 USD | 1,140,000.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,230,000.00 USD | 1,230,000.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 1,470,000.00 USD | 1,470,000.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 1,290,000.00 USD | 1,290,000.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,310,000.00 USD | 1,310,000.00 USD | 6,230.00 USD | 2,020.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 416.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,320,000.00 USD | 1,320,000.00 USD | 880.60 USD | 9,960.00 USD | 56.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,360,000.00 USD | 1,360,000.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 30,000.00 USD | 117,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,420,000.00 USD | 1,420,000.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,510,000.00 USD | 1,510,000.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 1,820,000.00 USD | 1,820,000.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,540,000.00 USD | 1,540,000.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,620,000.00 USD | 1,620,000.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,700,000.00 USD | 1,700,000.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,760,000.00 USD | 1,760,000.00 USD | 38,500.00 USD | 3,500.00 USD | 17,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 1,900,000.00 USD | 1,900,000.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,820,000.00 USD | 1,820,000.00 USD | 33,520.00 USD | 8,970.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,970,000.00 USD | 1,970,000.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 2,160,000.00 USD | 2,160,000.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 2,170,000.00 USD | 2,170,000.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,280,000.00 USD | 2,280,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 2,450,000.00 USD | 2,450,000.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,360,000.00 USD | 2,360,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,520,000.00 USD | 2,520,000.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 2,540,000.00 USD | 2,540,000.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,580,000.00 USD | 2,580,000.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,670,000.00 USD | 2,670,000.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 2,960,000.00 USD | 2,960,000.00 USD | 365,470.00 USD | 18,440.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,870,000.00 USD | 2,870,000.00 USD | 171,230.00 USD | 19,400.00 USD | 7,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,930,000.00 USD | 2,930,000.00 USD | 1,500.00 USD | 3,110.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.84` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,960,000.00 USD | 2,960,000.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,960,000.00 USD | 2,960,000.00 USD | 2,060.00 USD | 1,470.00 USD | 607.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 3,080,000.00 USD | 3,080,000.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,970,000.00 USD | 2,970,000.00 USD | 1,410.00 USD | 0.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,990,000.00 USD | 2,990,000.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 3,110,000.00 USD | 3,110,000.00 USD | 1,250.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 3,040,000.00 USD | 3,040,000.00 USD | 13,040.00 USD | 3,410.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 3,140,000.00 USD | 3,140,000.00 USD | 28,690.00 USD | 5,990.00 USD | 65,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 3,230,000.00 USD | 3,230,000.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 3,200,000.00 USD | 3,200,000.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 3,210,000.00 USD | 3,210,000.00 USD | 1,110.00 USD | 3,220.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 3,360,000.00 USD | 3,360,000.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 3,290,000.00 USD | 3,290,000.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 3,350,000.00 USD | 3,350,000.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 3,500,000.00 USD | 3,500,000.00 USD | 129,180.00 USD | 0.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 3,380,000.00 USD | 3,380,000.00 USD | 2,540.00 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 3,390,000.00 USD | 3,390,000.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 3,540,000.00 USD | 3,540,000.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.97` | 10,480.00 USD | 18,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.98` | 3,450,000.00 USD | 3,450,000.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 3,550,000.00 USD | 3,550,000.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 3,530,000.00 USD | 3,530,000.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 558,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 3,590,000.00 USD | 3,590,000.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 3,980,000.00 USD | 3,980,000.00 USD | 370,780.00 USD | 17,920.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,670,000.00 USD | 3,670,000.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,740,000.00 USD | 3,740,000.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 4,120,000.00 USD | 4,120,000.00 USD | 82,280.00 USD | 56,120.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,910,000.00 USD | 3,910,000.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,970,000.00 USD | 3,970,000.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 4,350,000.00 USD | 4,350,000.00 USD | 137,460.00 USD | 74,750.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 4,030,000.00 USD | 4,030,000.00 USD | 21,980.00 USD | 9,980.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 558,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 4,070,000.00 USD | 4,070,000.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 4,420,000.00 USD | 4,420,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 4,130,000.00 USD | 4,130,000.00 USD | 13,070.00 USD | 17,440.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 4,170,000.00 USD | 4,170,000.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 4,280,000.00 USD | 4,280,000.00 USD | 73,070.00 USD | 9,730.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 562,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 4,340,000.00 USD | 4,340,000.00 USD | 16,320.00 USD | 12,520.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 5,700,000.00 USD | 5,700,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 4,500,000.00 USD | 4,500,000.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,650,000.00 USD | 4,650,000.00 USD | 101,900.00 USD | 22,410.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 6,690,000.00 USD | 6,690,000.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,780,000.00 USD | 4,780,000.00 USD | 75,260.00 USD | 15,960.00 USD | 40,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,840,000.00 USD | 4,840,000.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 7,750,000.00 USD | 7,750,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 562,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,950,000.00 USD | 4,950,000.00 USD | 57,140.00 USD | 23,170.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 5,070,000.00 USD | 5,070,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 8,350,000.00 USD | 8,350,000.00 USD | 358,370.00 USD | 44,360.00 USD | 196,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 5,200,000.00 USD | 5,200,000.00 USD | 80,160.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 5,280,000.00 USD | 5,280,000.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 9,370,000.00 USD | 9,370,000.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 5,400,000.00 USD | 5,400,000.00 USD | 78,040.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 5,510,000.00 USD | 5,510,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 10,290,000.00 USD | 10,290,000.00 USD | 550,150.00 USD | 134,550.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,550,000.00 USD | 5,550,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,620,000.00 USD | 5,620,000.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 11,430,000.00 USD | 11,430,000.00 USD | 620,010.00 USD | 144,840.00 USD | 376,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,630,000.00 USD | 5,630,000.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.23` | 225.43 USD | 562,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,680,000.00 USD | 5,680,000.00 USD | 45,890.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 11,950,000.00 USD | 11,950,000.00 USD | 336,360.00 USD | 44,660.00 USD | 136,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,710,000.00 USD | 5,710,000.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,710,000.00 USD | 5,710,000.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 12,340,000.00 USD | 12,340,000.00 USD | 273,920.00 USD | 96,980.00 USD | 19,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,740,000.00 USD | 5,740,000.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.28` | 1,750.00 USD | 564,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,760,000.00 USD | 5,760,000.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 12,900,000.00 USD | 12,900,000.00 USD | 352,980.00 USD | 69,460.00 USD | 136,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,790,000.00 USD | 5,790,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 568,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,850,000.00 USD | 5,850,000.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 13,430,000.00 USD | 13,430,000.00 USD | 199,810.00 USD | 97,780.00 USD | 233,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,900,000.00 USD | 5,900,000.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,920,000.00 USD | 5,920,000.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 14,030,000.00 USD | 14,030,000.00 USD | 242,590.00 USD | 51,970.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,950,000.00 USD | 5,950,000.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 6,010,000.00 USD | 6,010,000.00 USD | 46,210.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 14,230,000.00 USD | 14,230,000.00 USD | 98,640.00 USD | 41,250.00 USD | 59,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 6,040,000.00 USD | 6,040,000.00 USD | 13,620.00 USD | 817.75 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 6,060,000.00 USD | 6,060,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 14,610,000.00 USD | 14,610,000.00 USD | 215,620.00 USD | 64,120.00 USD | 97,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 6,080,000.00 USD | 6,080,000.00 USD | 10,930.00 USD | 6,260.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 6,110,000.00 USD | 6,110,000.00 USD | 14,740.00 USD | 0.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 14,940,000.00 USD | 14,940,000.00 USD | 224,850.00 USD | 31,100.00 USD | 77,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 15,330,000.00 USD | 15,330,000.00 USD | 234,760.00 USD | 42,520.00 USD | 105,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 568,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.42` | 15,500,000.00 USD | 15,500,000.00 USD | 109,230.00 USD | 13,910.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 15,640,000.00 USD | 15,640,000.00 USD | 80,230.00 USD | 19,420.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 15,700,000.00 USD | 15,700,000.00 USD | 51,570.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 15,740,000.00 USD | 15,740,000.00 USD | 10,620.00 USD | 11,060.00 USD | 20,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 15,870,000.00 USD | 15,870,000.00 USD | 65,230.00 USD | 12,050.00 USD | 52,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 15,980,000.00 USD | 15,980,000.00 USD | 57,650.00 USD | 18,520.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 16,000,000.00 USD | 16,000,000.00 USD | 11,650.00 USD | 13,310.00 USD | 930.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 16,020,000.00 USD | 16,020,000.00 USD | 7,430.00 USD | 5,260.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 16,090,000.00 USD | 16,090,000.00 USD | 35,340.00 USD | 2,380.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 16,140,000.00 USD | 16,140,000.00 USD | 31,720.00 USD | 5,460.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 16,180,000.00 USD | 16,180,000.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 568,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 570,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.68` | 319.28 USD | 571,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.69` | 2,600.00 USD | 573,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 573,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 574,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.10` | 119.83 USD | 574,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 577,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.43` | 20,850.00 USD | 597,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 598,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.78` | 173.91 USD | 598,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 599,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 606,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.04` | 55,230.00 USD | 662,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.26` | 112,550.00 USD | 774,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 786,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.36` | 4,270.00 USD | 790,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 802,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 297,090.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.71` | 280.45 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.38` | 57,090.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.46` | 1,700.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 240.49 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.94` | 321.85 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.96` | 75,340.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.10` | 4,190.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.30` | 549.30 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.39` | 20,010.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.16` | 240.86 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.39` | 265,570.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.57` | 23,450.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.59` | 117.92 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.73` | 1,940.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.83` | 2,320,000.00 USD | 0.00 USD | 128.45 USD | `-78.31%` | `70.00` |
| `Live` | `Long` | `1.92` | 2,320,000.00 USD | 0.00 USD | 232.92 USD | `-77.37%` | `121.63` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 229.43 USD | `-76.42%` | `115.00` |
| `Live` | `Long` | `2.00` | 2,320,000.00 USD | 0.00 USD | 382.57 USD | `-76.30%` | `190.81` |
| `Live` | `Long` | `2.04` | 2,320,000.00 USD | 0.00 USD | 110.52 USD | `-75.95%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,320,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.60%` | `2,382.76` |
| `Live` | `Long` | `2.15` | 2,310,000.00 USD | 0.00 USD | 2,760.00 USD | `-74.65%` | `1,288.03` |
| `Live` | `Long` | `2.21` | 2,310,000.00 USD | 0.00 USD | 254.72 USD | `-73.82%` | `115.00` |
| `Live` | `Long` | `2.27` | 2,310,000.00 USD | 0.00 USD | 260.48 USD | `-73.23%` | `115.00` |
| `Live` | `Long` | `2.33` | 2,310,000.00 USD | 0.00 USD | 619.05 USD | `-72.52%` | `266.26` |
| `Live` | `Long` | `2.35` | 2,310,000.00 USD | 0.00 USD | 381.37 USD | `-72.17%` | `161.94` |
| `Live` | `Long` | `2.54` | 2,310,000.00 USD | 0.00 USD | 928.98 USD | `-69.92%` | `365.02` |
| `Live` | `Long` | `2.69` | 2,310,000.00 USD | 0.00 USD | 942.44 USD | `-68.27%` | `351.00` |
| `Live` | `Long` | `2.87` | 2,300,000.00 USD | 0.00 USD | 232.67 USD | `-66.14%` | `81.21` |
| `Live` | `Long` | `2.90` | 2,300,000.00 USD | 0.00 USD | 151.06 USD | `-65.67%` | `52.00` |
| `Live` | `Long` | `2.92` | 2,300,000.00 USD | 0.00 USD | 2,220.00 USD | `-65.55%` | `762.30` |
| `Live` | `Long` | `2.94` | 2,300,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.31%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,260,000.00 USD | 0.00 USD | 111.12 USD | `-64.84%` | `37.35` |
| `Live` | `Long` | `3.08` | 2,260,000.00 USD | 0.00 USD | 103.38 USD | `-63.54%` | `33.51` |
| `Live` | `Long` | `3.12` | 2,260,000.00 USD | 0.00 USD | 22,950.00 USD | `-63.19%` | `7,368.28` |
| `Live` | `Long` | `3.23` | 2,230,000.00 USD | 0.00 USD | 12,840.00 USD | `-61.89%` | `3,981.48` |
| `Live` | `Long` | `3.29` | 2,220,000.00 USD | 0.00 USD | 24,520.00 USD | `-61.18%` | `7,465.11` |
| `Live` | `Long` | `3.37` | 2,200,000.00 USD | 0.00 USD | 389.53 USD | `-60.23%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,200,000.00 USD | 0.00 USD | 151.88 USD | `-60.11%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,200,000.00 USD | 0.00 USD | 392.22 USD | `-58.10%` | `110.64` |
| `Live` | `Long` | `3.67` | 2,200,000.00 USD | 0.00 USD | 109.95 USD | `-56.69%` | `30.00` |
| `Live` | `Long` | `3.71` | 2,200,000.00 USD | 0.00 USD | 604.95 USD | `-56.09%` | `162.84` |
| `Live` | `Long` | `3.75` | 2,200,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.62%` | `400.00` |
| `Live` | `Long` | `3.81` | 2,190,000.00 USD | 0.00 USD | 2,240.00 USD | `-55.03%` | `589.35` |
| `Live` | `Long` | `3.90` | 2,190,000.00 USD | 0.00 USD | 131.73 USD | `-53.97%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,190,000.00 USD | 0.00 USD | 402.70 USD | `-52.43%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,190,000.00 USD | 0.00 USD | 152.29 USD | `-52.19%` | `37.65` |
| `Live` | `Long` | `4.09` | 2,190,000.00 USD | 0.00 USD | 1,640.00 USD | `-51.60%` | `400.00` |
| `Live` | `Long` | `4.12` | 2,190,000.00 USD | 0.00 USD | 2,740.00 USD | `-51.37%` | `666.20` |
| `Live` | `Long` | `4.14` | 2,190,000.00 USD | 0.00 USD | 159.29 USD | `-51.01%` | `38.43` |
| `Live` | `Long` | `4.16` | 2,190,000.00 USD | 0.00 USD | 8,310.00 USD | `-50.89%` | `2,000.00` |
| `Live` | `Long` | `4.24` | 2,180,000.00 USD | 0.00 USD | 169.40 USD | `-49.95%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,180,000.00 USD | 0.00 USD | 196.88 USD | `-49.71%` | `46.27` |
| `Live` | `Long` | `4.30` | 2,180,000.00 USD | 0.00 USD | 401.74 USD | `-49.12%` | `93.32` |
| `Live` | `Long` | `4.45` | 2,180,000.00 USD | 0.00 USD | 110.77 USD | `-47.47%` | `24.92` |
| `Live` | `Long` | `4.59` | 2,180,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.69%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,150,000.00 USD | 0.00 USD | 3,420.00 USD | `-45.34%` | `739.57` |
| `Live` | `Long` | `4.66` | 2,140,000.00 USD | 0.00 USD | 105.11 USD | `-44.99%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,140,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.87%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,140,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.75%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,140,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.63%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,130,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.51%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,120,000.00 USD | 0.00 USD | 474.50 USD | `-43.92%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,120,000.00 USD | 0.00 USD | 105.64 USD | `-43.69%` | `22.17` |
| `Live` | `Long` | `4.80` | 2,120,000.00 USD | 0.00 USD | 2,400.00 USD | `-43.21%` | `500.00` |
| `Live` | `Long` | `4.83` | 2,120,000.00 USD | 0.00 USD | 467.01 USD | `-42.86%` | `96.59` |
| `Live` | `Long` | `4.89` | 2,120,000.00 USD | 0.00 USD | 16,080.00 USD | `-42.15%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,100,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.03%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,100,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.91%` | `251.00` |
| `Live` | `Long` | `4.95` | 2,100,000.00 USD | 0.00 USD | 352.68 USD | `-41.56%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,100,000.00 USD | 0.00 USD | 945.36 USD | `-41.44%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,100,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.32%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,090,000.00 USD | 0.00 USD | 282.23 USD | `-41.20%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,090,000.00 USD | 0.00 USD | 269.53 USD | `-40.97%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,090,000.00 USD | 0.00 USD | 56,390.00 USD | `-40.73%` | `11,243.48` |
| `Live` | `Long` | `5.04` | 2,040,000.00 USD | 0.00 USD | 482.71 USD | `-40.49%` | `95.87` |
| `Live` | `Long` | `5.04` | 2,030,000.00 USD | 0.00 USD | 554.95 USD | `-40.38%` | `110.00` |
| `Live` | `Long` | `5.05` | 2,030,000.00 USD | 0.00 USD | 504.74 USD | `-40.26%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,030,000.00 USD | 0.00 USD | 213.20 USD | `-40.02%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,030,000.00 USD | 0.00 USD | 105.46 USD | `-39.90%` | `20.74` |
| `Live` | `Long` | `5.09` | 2,030,000.00 USD | 0.00 USD | 219.44 USD | `-39.79%` | `43.07` |
| `Live` | `Long` | `5.12` | 2,030,000.00 USD | 0.00 USD | 915.43 USD | `-39.55%` | `178.97` |
| `Live` | `Long` | `5.12` | 2,030,000.00 USD | 0.00 USD | 998.35 USD | `-39.43%` | `194.80` |
| `Live` | `Long` | `5.13` | 2,030,000.00 USD | 0.00 USD | 396.06 USD | `-39.31%` | `77.13` |
| `Live` | `Long` | `5.17` | 2,030,000.00 USD | 0.00 USD | 119.83 USD | `-38.96%` | `23.20` |
| `Live` | `Long` | `5.17` | 2,030,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.84%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,030,000.00 USD | 0.00 USD | 150.57 USD | `-38.72%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,030,000.00 USD | 0.00 USD | 801.81 USD | `-38.37%` | `153.75` |
| `Live` | `Long` | `5.22` | 2,030,000.00 USD | 0.00 USD | 122.58 USD | `-38.25%` | `23.46` |
| `Live` | `Long` | `5.25` | 2,030,000.00 USD | 0.00 USD | 213.00 USD | `-38.01%` | `40.61` |
| `Live` | `Long` | `5.25` | 2,030,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.89%` | `200.00` |
| `Live` | `Long` | `5.26` | 2,030,000.00 USD | 0.00 USD | 2,780.00 USD | `-37.78%` | `527.27` |
| `Live` | `Long` | `5.28` | 2,020,000.00 USD | 0.00 USD | 160,550.00 USD | `-37.66%` | `30,435.20` |
| `Live` | `Long` | `5.29` | 1,860,000.00 USD | 0.00 USD | 640.70 USD | `-37.54%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,860,000.00 USD | 0.00 USD | 232.85 USD | `-37.19%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,860,000.00 USD | 0.00 USD | 716.11 USD | `-37.07%` | `134.48` |
| `Live` | `Long` | `5.38` | 1,860,000.00 USD | 0.00 USD | 259.66 USD | `-36.36%` | `48.22` |
| `Live` | `Long` | `5.39` | 1,860,000.00 USD | 0.00 USD | 1,000.00 USD | `-36.24%` | `186.17` |
| `Live` | `Long` | `5.42` | 1,860,000.00 USD | 0.00 USD | 20,560.00 USD | `-36.00%` | `3,797.34` |
| `Live` | `Long` | `5.42` | 1,840,000.00 USD | 0.00 USD | 160,400.00 USD | `-35.89%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,680,000.00 USD | 0.00 USD | 1,360.00 USD | `-35.77%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,680,000.00 USD | 0.00 USD | 299.48 USD | `-35.65%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,680,000.00 USD | 0.00 USD | 264.72 USD | `-35.41%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,680,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.29%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,680,000.00 USD | 0.00 USD | 354.06 USD | `-35.18%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,680,000.00 USD | 0.00 USD | 19,290.00 USD | `-35.06%` | `3,510.41` |
| `Live` | `Long` | `5.54` | 1,660,000.00 USD | 0.00 USD | 2,880.00 USD | `-34.47%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,650,000.00 USD | 0.00 USD | 63,260.00 USD | `-34.11%` | `11,347.58` |
| `Live` | `Long` | `5.61` | 1,590,000.00 USD | 0.00 USD | 34,490.00 USD | `-33.76%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,560,000.00 USD | 0.00 USD | 468.55 USD | `-33.40%` | `83.15` |
| `Live` | `Long` | `5.71` | 1,560,000.00 USD | 0.00 USD | 1,540.00 USD | `-32.46%` | `270.00` |
| `Live` | `Long` | `5.72` | 1,550,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.34%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,550,000.00 USD | 0.00 USD | 661.65 USD | `-32.22%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,550,000.00 USD | 0.00 USD | 125.70 USD | `-32.10%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,550,000.00 USD | 0.00 USD | 3,190.00 USD | `-31.99%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,550,000.00 USD | 0.00 USD | 10,850.00 USD | `-31.87%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,540,000.00 USD | 0.00 USD | 801.40 USD | `-31.75%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,540,000.00 USD | 0.00 USD | 635.31 USD | `-31.51%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,540,000.00 USD | 0.00 USD | 580.50 USD | `-31.39%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,530,000.00 USD | 0.00 USD | 106.65 USD | `-31.28%` | `18.34` |
| `Live` | `Long` | `5.84` | 1,530,000.00 USD | 0.00 USD | 146.13 USD | `-30.92%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,530,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.80%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,530,000.00 USD | 0.00 USD | 984.70 USD | `-30.33%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,530,000.00 USD | 0.00 USD | 399.18 USD | `-30.21%` | `67.60` |
| `Live` | `Long` | `5.95` | 1,530,000.00 USD | 0.00 USD | 147.55 USD | `-29.74%` | `24.82` |
| `Live` | `Long` | `5.96` | 1,530,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.62%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,520,000.00 USD | 0.00 USD | 6,320.00 USD | `-29.50%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,510,000.00 USD | 0.00 USD | 585.97 USD | `-29.39%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,510,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.27%` | `233.60` |
| `Live` | `Long` | `6.00` | 1,510,000.00 USD | 0.00 USD | 341.56 USD | `-29.03%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,510,000.00 USD | 0.00 USD | 446.85 USD | `-28.91%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,510,000.00 USD | 0.00 USD | 437.84 USD | `-28.56%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,510,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.44%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,510,000.00 USD | 0.00 USD | 265.10 USD | `-28.32%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,510,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.20%` | `278.94` |
| `Live` | `Long` | `6.09` | 1,510,000.00 USD | 0.00 USD | 3,530.00 USD | `-27.97%` | `579.39` |
| `Live` | `Long` | `6.12` | 1,500,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.73%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,500,000.00 USD | 0.00 USD | 137.02 USD | `-27.61%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,500,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.49%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,500,000.00 USD | 0.00 USD | 238.61 USD | `-27.38%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,500,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.26%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,490,000.00 USD | 0.00 USD | 104.36 USD | `-27.02%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,490,000.00 USD | 0.00 USD | 310.25 USD | `-26.67%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,490,000.00 USD | 0.00 USD | 972.65 USD | `-26.08%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,490,000.00 USD | 0.00 USD | 2,510.00 USD | `-25.84%` | `400.00` |
| `Live` | `Long` | `6.33` | 1,490,000.00 USD | 0.00 USD | 277.48 USD | `-25.25%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,490,000.00 USD | 0.00 USD | 2,450.00 USD | `-25.13%` | `386.46` |
| `Live` | `Long` | `6.36` | 1,480,000.00 USD | 0.00 USD | 4,470.00 USD | `-24.89%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,480,000.00 USD | 0.00 USD | 284,770.00 USD | `-24.78%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,200,000.00 USD | 0.00 USD | 1,310.00 USD | `-24.66%` | `204.92` |
| `Live` | `Long` | `6.38` | 1,190,000.00 USD | 0.00 USD | 6,550.00 USD | `-24.54%` | `1,026.45` |
| `Live` | `Long` | `6.39` | 1,190,000.00 USD | 0.00 USD | 5,940.00 USD | `-24.42%` | `928.10` |
| `Live` | `Long` | `6.42` | 1,180,000.00 USD | 0.00 USD | 306.32 USD | `-24.19%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,180,000.00 USD | 0.00 USD | 484.64 USD | `-24.07%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,180,000.00 USD | 0.00 USD | 6,780.00 USD | `-23.95%` | `1,052.89` |
| `Live` | `Long` | `6.45` | 1,170,000.00 USD | 0.00 USD | 1,510.00 USD | `-23.83%` | `234.11` |
| `Live` | `Long` | `6.46` | 1,170,000.00 USD | 0.00 USD | 361,860.00 USD | `-23.71%` | `56,059.40` |
| `Live` | `Long` | `6.46` | 810,960.00 USD | 0.00 USD | 1,050.00 USD | `-23.59%` | `162.75` |
| `Live` | `Long` | `6.54` | 809,910.00 USD | 0.00 USD | 852.03 USD | `-22.77%` | `130.38` |
| `Live` | `Long` | `6.54` | 809,060.00 USD | 0.00 USD | 8,970.00 USD | `-22.65%` | `1,370.89` |
| `Live` | `Long` | `6.59` | 800,090.00 USD | 0.00 USD | 2,870.00 USD | `-22.06%` | `435.69` |
| `Live` | `Long` | `6.62` | 797,210.00 USD | 0.00 USD | 2,110.00 USD | `-21.82%` | `318.57` |
| `Live` | `Long` | `6.62` | 795,110.00 USD | 0.00 USD | 364.90 USD | `-21.70%` | `55.08` |
| `Live` | `Long` | `6.63` | 794,740.00 USD | 0.00 USD | 245.89 USD | `-21.59%` | `37.06` |
| `Live` | `Long` | `6.66` | 794,500.00 USD | 0.00 USD | 1,540.00 USD | `-21.35%` | `231.02` |
| `Live` | `Long` | `6.67` | 792,960.00 USD | 0.00 USD | 2,850.00 USD | `-21.11%` | `426.53` |
| `Live` | `Long` | `6.68` | 790,110.00 USD | 0.00 USD | 3,160.00 USD | `-20.99%` | `472.28` |
| `Live` | `Long` | `6.70` | 786,950.00 USD | 0.00 USD | 15,800.00 USD | `-20.88%` | `2,360.46` |
| `Live` | `Long` | `6.71` | 771,150.00 USD | 0.00 USD | 11,000.00 USD | `-20.76%` | `1,641.31` |
| `Live` | `Long` | `6.71` | 760,150.00 USD | 0.00 USD | 6,180.00 USD | `-20.64%` | `920.74` |
| `Live` | `Long` | `6.75` | 753,960.00 USD | 0.00 USD | 1,330.00 USD | `-20.17%` | `196.95` |
| `Live` | `Long` | `6.78` | 752,630.00 USD | 0.00 USD | 7,990.00 USD | `-19.93%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 744,640.00 USD | 0.00 USD | 22,020.00 USD | `-19.81%` | `3,245.57` |
| `Live` | `Long` | `6.79` | 722,620.00 USD | 0.00 USD | 5,170.00 USD | `-19.69%` | `761.18` |
| `Live` | `Long` | `6.80` | 717,450.00 USD | 0.00 USD | 1,500.00 USD | `-19.58%` | `220.95` |
| `Live` | `Long` | `6.82` | 715,940.00 USD | 0.00 USD | 7,230.00 USD | `-19.46%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 708,710.00 USD | 0.00 USD | 271.02 USD | `-19.34%` | `39.71` |
| `Live` | `Long` | `6.87` | 708,440.00 USD | 0.00 USD | 3,340.00 USD | `-18.87%` | `486.46` |
| `Live` | `Long` | `6.88` | 705,100.00 USD | 0.00 USD | 263.66 USD | `-18.75%` | `38.35` |
| `Live` | `Long` | `6.88` | 704,840.00 USD | 0.00 USD | 1,580.00 USD | `-18.63%` | `229.18` |
| `Live` | `Long` | `6.92` | 703,260.00 USD | 0.00 USD | 579.62 USD | `-18.16%` | `83.70` |
| `Live` | `Long` | `6.93` | 702,680.00 USD | 0.00 USD | 3,500.00 USD | `-18.04%` | `504.07` |
| `Live` | `Long` | `6.95` | 699,180.00 USD | 0.00 USD | 215.30 USD | `-17.92%` | `31.00` |
| `Live` | `Long` | `6.96` | 698,970.00 USD | 0.00 USD | 7,240.00 USD | `-17.80%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 691,720.00 USD | 0.00 USD | 636.74 USD | `-17.69%` | `91.42` |
| `Live` | `Long` | `6.97` | 691,090.00 USD | 0.00 USD | 128,810.00 USD | `-17.57%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 562,280.00 USD | 0.00 USD | 1,040.00 USD | `-17.33%` | `149.32` |
| `Live` | `Long` | `7.01` | 561,240.00 USD | 0.00 USD | 20,890.00 USD | `-17.09%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 540,340.00 USD | 0.00 USD | 1,370.00 USD | `-16.98%` | `194.51` |
| `Live` | `Long` | `7.07` | 538,980.00 USD | 0.00 USD | 23,960.00 USD | `-16.50%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 515,020.00 USD | 0.00 USD | 6,700.00 USD | `-16.38%` | `947.44` |
| `Live` | `Long` | `7.08` | 508,320.00 USD | 0.00 USD | 1,050.00 USD | `-16.27%` | `148.63` |
| `Live` | `Long` | `7.09` | 507,270.00 USD | 0.00 USD | 2,130.00 USD | `-16.15%` | `300.00` |
| `Live` | `Long` | `7.11` | 505,140.00 USD | 0.00 USD | 28,530.00 USD | `-16.03%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 476,610.00 USD | 0.00 USD | 379.66 USD | `-15.91%` | `53.36` |
| `Live` | `Long` | `7.13` | 476,230.00 USD | 0.00 USD | 13,410.00 USD | `-15.68%` | `1,879.32` |
| `Live` | `Long` | `7.14` | 462,820.00 USD | 0.00 USD | 20,270.00 USD | `-15.56%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 442,550.00 USD | 0.00 USD | 2,380.00 USD | `-15.20%` | `331.12` |
| `Live` | `Long` | `7.18` | 440,170.00 USD | 0.00 USD | 1,440.00 USD | `-15.08%` | `200.95` |
| `Live` | `Long` | `7.21` | 438,730.00 USD | 0.00 USD | 322.94 USD | `-14.73%` | `44.76` |
| `Live` | `Long` | `7.24` | 438,410.00 USD | 0.00 USD | 1,480.00 USD | `-14.49%` | `205.21` |
| `Live` | `Long` | `7.25` | 436,920.00 USD | 0.00 USD | 2,730.00 USD | `-14.38%` | `376.23` |
| `Live` | `Long` | `7.25` | 434,200.00 USD | 0.00 USD | 21,280.00 USD | `-14.26%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 412,920.00 USD | 0.00 USD | 36,420.00 USD | `-13.90%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 376,490.00 USD | 0.00 USD | 1,680.00 USD | `-13.78%` | `230.97` |
| `Live` | `Long` | `7.30` | 374,810.00 USD | 0.00 USD | 2,130.00 USD | `-13.67%` | `291.40` |
| `Live` | `Long` | `7.33` | 372,680.00 USD | 0.00 USD | 29,300.00 USD | `-13.43%` | `4,000.00` |
| `Live` | `Long` | `7.33` | 343,380.00 USD | 0.00 USD | 1,030.00 USD | `-13.31%` | `140.00` |
| `Live` | `Long` | `7.34` | 342,350.00 USD | 0.00 USD | 552.42 USD | `-13.19%` | `75.21` |
| `Live` | `Long` | `7.36` | 341,800.00 USD | 0.00 USD | 3,820.00 USD | `-13.08%` | `519.63` |
| `Live` | `Long` | `7.37` | 337,980.00 USD | 0.00 USD | 2,940.00 USD | `-12.96%` | `399.15` |
| `Live` | `Long` | `7.38` | 335,040.00 USD | 0.00 USD | 2,570.00 USD | `-12.84%` | `348.75` |
| `Live` | `Long` | `7.38` | 332,460.00 USD | 0.00 USD | 227.97 USD | `-12.72%` | `30.87` |
| `Live` | `Long` | `7.39` | 332,240.00 USD | 0.00 USD | 13,220.00 USD | `-12.60%` | `1,787.05` |
| `Live` | `Long` | `7.42` | 319,020.00 USD | 0.00 USD | 147.61 USD | `-12.25%` | `19.88` |
| `Live` | `Long` | `7.43` | 318,870.00 USD | 0.00 USD | 2,430.00 USD | `-12.13%` | `327.05` |
| `Live` | `Long` | `7.45` | 316,440.00 USD | 0.00 USD | 2,410.00 USD | `-12.01%` | `324.35` |
| `Live` | `Long` | `7.46` | 314,030.00 USD | 0.00 USD | 10,390.00 USD | `-11.89%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 303,640.00 USD | 0.00 USD | 4,590.00 USD | `-11.78%` | `614.36` |
| `Live` | `Long` | `7.47` | 299,050.00 USD | 0.00 USD | 1,120.00 USD | `-11.66%` | `149.52` |
| `Live` | `Long` | `7.50` | 297,930.00 USD | 0.00 USD | 962.81 USD | `-11.42%` | `128.46` |
| `Live` | `Long` | `7.50` | 296,970.00 USD | 0.00 USD | 421.78 USD | `-11.30%` | `56.20` |
| `Live` | `Long` | `7.51` | 296,550.00 USD | 0.00 USD | 2,580.00 USD | `-11.18%` | `343.54` |
| `Live` | `Long` | `7.53` | 293,970.00 USD | 0.00 USD | 1,570.00 USD | `-11.07%` | `208.52` |
| `Live` | `Long` | `7.54` | 292,400.00 USD | 0.00 USD | 4,210.00 USD | `-10.95%` | `559.01` |
| `Live` | `Long` | `7.55` | 288,190.00 USD | 0.00 USD | 1,070.00 USD | `-10.71%` | `141.09` |
| `Live` | `Long` | `7.57` | 287,120.00 USD | 0.00 USD | 26,570.00 USD | `-10.59%` | `3,512.23` |
| `Live` | `Long` | `7.58` | 260,550.00 USD | 0.00 USD | 118.25 USD | `-10.48%` | `15.61` |
| `Live` | `Long` | `7.61` | 260,430.00 USD | 0.00 USD | 1,630.00 USD | `-10.12%` | `214.22` |
| `Live` | `Long` | `7.62` | 258,800.00 USD | 0.00 USD | 754.04 USD | `-10.00%` | `99.02` |
| `Live` | `Long` | `7.62` | 258,050.00 USD | 0.00 USD | 787.51 USD | `-9.88%` | `103.28` |
| `Live` | `Long` | `7.63` | 257,260.00 USD | 0.00 USD | 378.93 USD | `-9.77%` | `49.63` |
| `Live` | `Long` | `7.66` | 256,880.00 USD | 0.00 USD | 135.42 USD | `-9.53%` | `17.69` |
| `Live` | `Long` | `7.67` | 256,750.00 USD | 0.00 USD | 256.09 USD | `-9.41%` | `33.41` |
| `Live` | `Long` | `7.67` | 256,490.00 USD | 0.00 USD | 4,480.00 USD | `-9.29%` | `583.63` |
| `Live` | `Long` | `7.68` | 252,010.00 USD | 0.00 USD | 739.30 USD | `-9.18%` | `96.20` |
| `Live` | `Long` | `7.70` | 251,270.00 USD | 0.00 USD | 6,690.00 USD | `-9.06%` | `869.22` |
| `Live` | `Long` | `7.75` | 244,580.00 USD | 0.00 USD | 500.12 USD | `-8.35%` | `64.49` |
| `Live` | `Long` | `7.76` | 244,080.00 USD | 0.00 USD | 455.73 USD | `-8.23%` | `58.69` |
| `Live` | `Long` | `7.78` | 243,630.00 USD | 0.00 USD | 6,310.00 USD | `-8.11%` | `812.08` |
| `Live` | `Long` | `7.79` | 237,310.00 USD | 0.00 USD | 3,750.00 USD | `-7.99%` | `481.06` |
| `Live` | `Long` | `7.79` | 233,570.00 USD | 0.00 USD | 4,480.00 USD | `-7.88%` | `574.50` |
| `Live` | `Long` | `7.80` | 229,090.00 USD | 0.00 USD | 7,240.00 USD | `-7.76%` | `928.24` |
| `Live` | `Long` | `7.83` | 221,850.00 USD | 0.00 USD | 1,940.00 USD | `-7.52%` | `247.42` |
| `Live` | `Long` | `7.84` | 219,910.00 USD | 0.00 USD | 22,560.00 USD | `-7.28%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 197,350.00 USD | 0.00 USD | 233.83 USD | `-7.05%` | `29.73` |
| `Live` | `Long` | `7.88` | 197,120.00 USD | 0.00 USD | 555.19 USD | `-6.93%` | `70.50` |
| `Live` | `Long` | `7.89` | 196,560.00 USD | 0.00 USD | 15,880.00 USD | `-6.69%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 180,680.00 USD | 0.00 USD | 2,930.00 USD | `-6.58%` | `370.74` |
| `Live` | `Long` | `7.92` | 177,750.00 USD | 0.00 USD | 4,600.00 USD | `-6.34%` | `580.78` |
| `Live` | `Long` | `7.93` | 173,140.00 USD | 0.00 USD | 16,340.00 USD | `-6.22%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 156,800.00 USD | 0.00 USD | 141.74 USD | `-6.10%` | `17.84` |
| `Live` | `Long` | `7.96` | 156,660.00 USD | 0.00 USD | 127,900.00 USD | `-5.98%` | `16,078.30` |
| `Live` | `Long` | `7.97` | 28,760.00 USD | 0.00 USD | 1,580.00 USD | `-5.75%` | `198.26` |
| `Live` | `Long` | `7.99` | 27,170.00 USD | 0.00 USD | 1,280.00 USD | `-5.63%` | `160.68` |
| `Live` | `Long` | `8.00` | 25,890.00 USD | 0.00 USD | 889.52 USD | `-5.51%` | `111.26` |
| `Live` | `Long` | `8.03` | 25,000.00 USD | 0.00 USD | 1,590.00 USD | `-5.16%` | `198.02` |
| `Live` | `Long` | `8.06` | 23,410.00 USD | 0.00 USD | 439.54 USD | `-4.68%` | `54.50` |
| `Live` | `Long` | `8.07` | 22,970.00 USD | 0.00 USD | 21,710.00 USD | `-4.57%` | `2,688.93` |
| `Live` | `Long` | `8.12` | 1,260.00 USD | 0.00 USD | 738.14 USD | `-4.09%` | `90.96` |
| `Live` | `Long` | `8.12` | 521.62 USD | 0.00 USD | 521.62 USD | `-3.98%` | `64.20` |
| `Live` | `Short` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | `+2.64%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,210.00 USD | 6,000.00 USD | 0.00 USD | `+4.30%` | `680.16` |
| `Live` | `Short` | `8.87` | 7,370.00 USD | 1,160.00 USD | 0.00 USD | `+4.77%` | `130.57` |
| `Live` | `Short` | `8.88` | 8,060.00 USD | 691.70 USD | 0.00 USD | `+5.01%` | `77.85` |
| `Live` | `Short` | `8.97` | 18,540.00 USD | 10,480.00 USD | 0.00 USD | `+6.07%` | `1,167.41` |
| `Live` | `Short` | `8.99` | 558,250.00 USD | 539,710.00 USD | 0.00 USD | `+6.31%` | `60,000.94` |
| `Live` | `Short` | `9.05` | 558,460.00 USD | 213.70 USD | 0.00 USD | `+7.02%` | `23.60` |
| `Live` | `Short` | `9.10` | 562,350.00 USD | 3,890.00 USD | 0.00 USD | `+7.49%` | `427.53` |
| `Live` | `Short` | `9.14` | 562,530.00 USD | 180.80 USD | 0.00 USD | `+8.08%` | `19.77` |
| `Live` | `Short` | `9.23` | 562,760.00 USD | 225.43 USD | 0.00 USD | `+9.14%` | `24.41` |
| `Live` | `Short` | `9.28` | 564,510.00 USD | 1,750.00 USD | 0.00 USD | `+9.62%` | `188.98` |
| `Live` | `Short` | `9.29` | 568,370.00 USD | 3,860.00 USD | 0.00 USD | `+9.85%` | `415.00` |
| `Live` | `Short` | `9.41` | 568,810.00 USD | 440.06 USD | 0.00 USD | `+11.27%` | `46.74` |
| `Live` | `Short` | `9.62` | 568,940.00 USD | 138.98 USD | 0.00 USD | `+13.75%` | `14.44` |
| `Live` | `Short` | `9.64` | 570,880.00 USD | 1,930.00 USD | 0.00 USD | `+13.99%` | `200.61` |
| `Live` | `Short` | `9.68` | 571,200.00 USD | 319.28 USD | 0.00 USD | `+14.34%` | `33.00` |
| `Live` | `Short` | `9.69` | 573,800.00 USD | 2,600.00 USD | 0.00 USD | `+14.46%` | `268.63` |
| `Live` | `Short` | `9.73` | 573,990.00 USD | 192.95 USD | 0.00 USD | `+15.05%` | `19.82` |
| `Live` | `Short` | `9.88` | 574,370.00 USD | 371.77 USD | 0.00 USD | `+16.82%` | `37.61` |
| `Live` | `Short` | `10.10` | 574,480.00 USD | 119.83 USD | 0.00 USD | `+19.31%` | `11.87` |
| `Live` | `Short` | `10.35` | 577,140.00 USD | 2,650.00 USD | 0.00 USD | `+22.26%` | `256.58` |
| `Live` | `Short` | `10.43` | 597,990.00 USD | 20,850.00 USD | 0.00 USD | `+23.21%` | `2,000.00` |
| `Live` | `Short` | `10.56` | 598,510.00 USD | 523.81 USD | 0.00 USD | `+24.86%` | `49.58` |
| `Live` | `Short` | `10.78` | 598,690.00 USD | 173.91 USD | 0.00 USD | `+27.34%` | `16.14` |
| `Live` | `Short` | `10.81` | 599,840.00 USD | 1,150.00 USD | 0.00 USD | `+27.82%` | `106.17` |
| `Live` | `Short` | `11.01` | 606,800.00 USD | 6,970.00 USD | 0.00 USD | `+30.06%` | `633.00` |
| `Live` | `Short` | `11.04` | 662,030.00 USD | 55,230.00 USD | 0.00 USD | `+30.53%` | `5,000.00` |
| `Live` | `Short` | `11.26` | 774,580.00 USD | 112,550.00 USD | 0.00 USD | `+33.02%` | `10,000.00` |
| `Live` | `Short` | `11.27` | 786,250.00 USD | 11,670.00 USD | 0.00 USD | `+33.13%` | `1,035.87` |
| `Live` | `Short` | `11.36` | 790,520.00 USD | 4,270.00 USD | 0.00 USD | `+34.20%` | `376.48` |
| `Live` | `Short` | `11.62` | 802,660.00 USD | 12,140.00 USD | 0.00 USD | `+37.39%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,100,000.00 USD | 297,090.00 USD | 0.00 USD | `+38.10%` | `25,425.17` |
| `Live` | `Short` | `11.71` | 1,100,000.00 USD | 280.45 USD | 0.00 USD | `+38.33%` | `23.96` |
| `Live` | `Short` | `11.93` | 1,100,000.00 USD | 505.74 USD | 0.00 USD | `+40.93%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,100,000.00 USD | 1,050.00 USD | 0.00 USD | `+41.17%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,100,000.00 USD | 1,730.00 USD | 0.00 USD | `+45.43%` | `140.71` |
| `Live` | `Short` | `12.38` | 1,160,000.00 USD | 57,090.00 USD | 0.00 USD | `+46.37%` | `4,610.01` |
| `Live` | `Short` | `12.40` | 1,160,000.00 USD | 343.62 USD | 0.00 USD | `+46.61%` | `27.70` |
| `Live` | `Short` | `12.46` | 1,160,000.00 USD | 1,700.00 USD | 0.00 USD | `+47.32%` | `136.39` |
| `Live` | `Short` | `13.20` | 1,250,000.00 USD | 87,940.00 USD | 0.00 USD | `+55.94%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,250,000.00 USD | 3,810.00 USD | 0.00 USD | `+57.13%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,250,000.00 USD | 430.34 USD | 0.00 USD | `+59.13%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,250,000.00 USD | 172.29 USD | 0.00 USD | `+61.73%` | `12.59` |
| `Live` | `Short` | `14.65` | 1,260,000.00 USD | 240.49 USD | 0.00 USD | `+73.20%` | `16.41` |
| `Live` | `Short` | `14.66` | 1,260,000.00 USD | 823.29 USD | 0.00 USD | `+73.32%` | `56.14` |
| `Live` | `Short` | `14.94` | 1,260,000.00 USD | 321.85 USD | 0.00 USD | `+76.51%` | `21.55` |
| `Live` | `Short` | `14.96` | 1,330,000.00 USD | 75,340.00 USD | 0.00 USD | `+76.74%` | `5,037.66` |
| `Live` | `Short` | `15.09` | 1,330,000.00 USD | 219.34 USD | 0.00 USD | `+78.28%` | `14.54` |
| `Live` | `Short` | `15.10` | 1,340,000.00 USD | 4,190.00 USD | 0.00 USD | `+78.40%` | `277.54` |
| `Live` | `Short` | `15.29` | 1,340,000.00 USD | 229.43 USD | 0.00 USD | `+80.76%` | `15.00` |
| `Live` | `Short` | `15.30` | 1,340,000.00 USD | 549.30 USD | 0.00 USD | `+80.88%` | `35.89` |
| `Live` | `Short` | `15.35` | 1,340,000.00 USD | 230.17 USD | 0.00 USD | `+81.35%` | `15.00` |
| `Live` | `Short` | `15.39` | 1,360,000.00 USD | 20,010.00 USD | 0.00 USD | `+81.94%` | `1,300.00` |
| `Live` | `Short` | `15.77` | 1,360,000.00 USD | 185.55 USD | 0.00 USD | `+86.32%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,360,000.00 USD | 1,700.00 USD | 0.00 USD | `+87.03%` | `107.48` |
| `Live` | `Short` | `16.16` | 1,360,000.00 USD | 240.86 USD | 0.00 USD | `+91.04%` | `14.90` |
| `Live` | `Short` | `16.39` | 1,620,000.00 USD | 265,570.00 USD | 0.00 USD | `+93.64%` | `16,208.00` |
| `Live` | `Short` | `16.52` | 1,620,000.00 USD | 190.91 USD | 0.00 USD | `+95.18%` | `11.56` |
| `Live` | `Short` | `16.57` | 1,650,000.00 USD | 23,450.00 USD | 0.00 USD | `+95.89%` | `1,414.55` |
| `Live` | `Short` | `16.59` | 1,650,000.00 USD | 117.92 USD | 0.00 USD | `+96.01%` | `7.11` |
| `Live` | `Short` | `16.73` | 1,650,000.00 USD | 1,940.00 USD | 0.00 USD | `+97.78%` | `115.73` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 373,770.00 USD | 0.00 USD | 611.73 USD | `-72.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 373,160.00 USD | 0.00 USD | 793.75 USD | `-52.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 372,370.00 USD | 0.00 USD | 67,970.00 USD | `-40.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 304,400.00 USD | 0.00 USD | 205.30 USD | `-37.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 304,200.00 USD | 0.00 USD | 465.42 USD | `-35.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 303,730.00 USD | 0.00 USD | 349.35 USD | `-34.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 303,380.00 USD | 0.00 USD | 1,020.00 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 302,360.00 USD | 0.00 USD | 1,330.00 USD | `-31.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 301,040.00 USD | 0.00 USD | 493.50 USD | `-29.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 300,540.00 USD | 0.00 USD | 100.98 USD | `-29.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 300,440.00 USD | 0.00 USD | 500.70 USD | `-29.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 299,940.00 USD | 0.00 USD | 4,160.00 USD | `-27.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 295,790.00 USD | 0.00 USD | 6,500.00 USD | `-27.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 289,280.00 USD | 0.00 USD | 906.18 USD | `-26.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 288,380.00 USD | 0.00 USD | 127.35 USD | `-26.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 288,250.00 USD | 0.00 USD | 864.38 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 287,390.00 USD | 0.00 USD | 130.10 USD | `-23.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 287,260.00 USD | 0.00 USD | 4,340.00 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 282,920.00 USD | 0.00 USD | 5,520.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 277,390.00 USD | 0.00 USD | 203.67 USD | `-20.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 277,190.00 USD | 0.00 USD | 296.34 USD | `-20.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 276,890.00 USD | 0.00 USD | 921.19 USD | `-20.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 275,970.00 USD | 0.00 USD | 709.98 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 275,260.00 USD | 0.00 USD | 4,630.00 USD | `-18.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 270,640.00 USD | 0.00 USD | 691.50 USD | `-18.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 269,940.00 USD | 0.00 USD | 262.44 USD | `-17.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 269,680.00 USD | 0.00 USD | 24,350.00 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 245,330.00 USD | 0.00 USD | 653.69 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 244,680.00 USD | 0.00 USD | 187.79 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 244,490.00 USD | 0.00 USD | 6,790.00 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 237,700.00 USD | 0.00 USD | 4,960.00 USD | `-15.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 232,740.00 USD | 0.00 USD | 7,210.00 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 225,530.00 USD | 0.00 USD | 282.74 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 225,250.00 USD | 0.00 USD | 603.44 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 224,650.00 USD | 0.00 USD | 464.61 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 224,180.00 USD | 0.00 USD | 2,090.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 222,090.00 USD | 0.00 USD | 129.58 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 221,960.00 USD | 0.00 USD | 114.65 USD | `-13.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 221,840.00 USD | 0.00 USD | 702.75 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 221,140.00 USD | 0.00 USD | 4,630.00 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 216,510.00 USD | 0.00 USD | 199.39 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 216,310.00 USD | 0.00 USD | 6,270.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 210,040.00 USD | 0.00 USD | 37,420.00 USD | `-11.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 172,620.00 USD | 0.00 USD | 2,120.00 USD | `-11.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 170,500.00 USD | 0.00 USD | 799.83 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 169,700.00 USD | 0.00 USD | 820.44 USD | `-10.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 168,880.00 USD | 0.00 USD | 218.24 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 168,660.00 USD | 0.00 USD | 113.78 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 168,540.00 USD | 0.00 USD | 152.10 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 168,390.00 USD | 0.00 USD | 297.59 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 168,100.00 USD | 0.00 USD | 528.88 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 167,570.00 USD | 0.00 USD | 360.13 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 167,210.00 USD | 0.00 USD | 578.04 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 166,630.00 USD | 0.00 USD | 106.32 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 166,520.00 USD | 0.00 USD | 424.05 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 166,100.00 USD | 0.00 USD | 1,170.00 USD | `-7.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 164,930.00 USD | 0.00 USD | 3,940.00 USD | `-7.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 160,990.00 USD | 0.00 USD | 154.70 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 160,830.00 USD | 0.00 USD | 115.23 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 160,720.00 USD | 0.00 USD | 183.33 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 160,530.00 USD | 0.00 USD | 1,890.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 158,640.00 USD | 0.00 USD | 6,840.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 151,800.00 USD | 0.00 USD | 5,710.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 146,090.00 USD | 0.00 USD | 1,590.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 144,510.00 USD | 0.00 USD | 898.42 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 143,610.00 USD | 0.00 USD | 7,960.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 135,650.00 USD | 0.00 USD | 246.52 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 135,410.00 USD | 0.00 USD | 2,420.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 132,990.00 USD | 0.00 USD | 1,440.00 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 131,550.00 USD | 0.00 USD | 435.73 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 131,110.00 USD | 0.00 USD | 4,320.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 126,800.00 USD | 0.00 USD | 123.58 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 126,670.00 USD | 0.00 USD | 796.62 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 125,880.00 USD | 0.00 USD | 152.56 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 125,720.00 USD | 0.00 USD | 2,730.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 122,990.00 USD | 0.00 USD | 121.69 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 122,870.00 USD | 0.00 USD | 5,230.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 117,640.00 USD | 0.00 USD | 477.36 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 117,160.00 USD | 0.00 USD | 16,210.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 100,950.00 USD | 0.00 USD | 744.88 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 100,210.00 USD | 0.00 USD | 6,500.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 93,710.00 USD | 0.00 USD | 884.60 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 92,820.00 USD | 0.00 USD | 5,550.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 87,270.00 USD | 0.00 USD | 121.51 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 87,150.00 USD | 0.00 USD | 3,080.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 84,060.00 USD | 0.00 USD | 520.75 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 83,540.00 USD | 0.00 USD | 3,020.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 80,520.00 USD | 0.00 USD | 141.04 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 80,380.00 USD | 0.00 USD | 22,560.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 57,810.00 USD | 0.00 USD | 515.66 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 57,300.00 USD | 0.00 USD | 139.74 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 57,160.00 USD | 0.00 USD | 490.15 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 56,670.00 USD | 0.00 USD | 197.96 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 56,470.00 USD | 0.00 USD | 9,640.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 46,830.00 USD | 0.00 USD | 535.65 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 46,300.00 USD | 0.00 USD | 734.99 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 45,560.00 USD | 0.00 USD | 828.50 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 44,730.00 USD | 0.00 USD | 311.97 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 44,420.00 USD | 0.00 USD | 5,380.00 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 39,050.00 USD | 0.00 USD | 245.13 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 38,800.00 USD | 0.00 USD | 1,690.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 37,110.00 USD | 0.00 USD | 408.58 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 36,700.00 USD | 0.00 USD | 808.63 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 35,890.00 USD | 0.00 USD | 4,070.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 31,820.00 USD | 0.00 USD | 24,090.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 7,730.00 USD | 0.00 USD | 1,140.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 6,590.00 USD | 0.00 USD | 419.25 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 6,170.00 USD | 0.00 USD | 376.68 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 5,790.00 USD | 0.00 USD | 4,240.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 1,560.00 USD | 0.00 USD | 314.81 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 1,240.00 USD | 0.00 USD | 198.83 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 1,040.00 USD | 0.00 USD | 195.52 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 849.06 USD | 0.00 USD | 138.24 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 710.81 USD | 0.00 USD | 710.81 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 769.61 USD | 769.61 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 1,550.00 USD | 777.14 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 1,960.00 USD | 408.78 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 2,080.00 USD | 122.47 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 3,240.00 USD | 1,160.00 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 3,360.00 USD | 123.27 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 5,530.00 USD | 2,170.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 5,660.00 USD | 123.56 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 15,640.00 USD | 9,990.00 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 18,130.00 USD | 2,490.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 18,700.00 USD | 566.55 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 18,840.00 USD | 143.28 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 18,960.00 USD | 124.28 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 19,070.00 USD | 102.14 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 19,190.00 USD | 124.57 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 19,320.00 USD | 128.51 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 19,520.00 USD | 201.97 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 21,810.00 USD | 2,290.00 USD | 0.00 USD | `+2.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 22,690.00 USD | 877.88 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 22,890.00 USD | 200.85 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 23,060.00 USD | 176.62 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 24,050.00 USD | 990.09 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 24,880.00 USD | 830.81 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 43,840.00 USD | 18,950.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 44,240.00 USD | 399.67 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 44,660.00 USD | 421.85 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 44,900.00 USD | 239.51 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 49,270.00 USD | 4,370.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 53,020.00 USD | 3,740.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 53,190.00 USD | 173.28 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 53,400.00 USD | 215.16 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 53,790.00 USD | 388.12 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 54,500.00 USD | 711.78 USD | 0.00 USD | `+3.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 55,070.00 USD | 563.87 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 55,310.00 USD | 243.40 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 55,480.00 USD | 168.05 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 55,820.00 USD | 339.94 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 56,130.00 USD | 310.98 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 56,240.00 USD | 110.58 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 57,100.00 USD | 860.96 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 59,040.00 USD | 1,930.00 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 59,820.00 USD | 788.72 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 61,630.00 USD | 1,800.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 61,790.00 USD | 163.33 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 62,570.00 USD | 782.17 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 62,800.00 USD | 223.62 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 600,100.00 USD | 537,310.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 600,510.00 USD | 401.63 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 915,660.00 USD | 315,150.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 916,000.00 USD | 338.30 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 916,260.00 USD | 260.96 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 916,480.00 USD | 220.06 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 917,560.00 USD | 1,090.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 918,180.00 USD | 616.37 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 918,280.00 USD | 102.03 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 918,740.00 USD | 453.84 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 918,900.00 USD | 160.99 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 919,110.00 USD | 215.98 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 920,620.00 USD | 1,510.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 921,080.00 USD | 451.48 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 921,210.00 USD | 139.58 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 922,510.00 USD | 1,290.00 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 922,670.00 USD | 166.53 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 924,670.00 USD | 2,000.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,320,000.00 USD | 394,210.00 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,320,000.00 USD | 119.24 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,320,000.00 USD | 3,020.00 USD | 0.00 USD | `+8.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,320,000.00 USD | 131.87 USD | 0.00 USD | `+8.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,320,000.00 USD | 149.17 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,320,000.00 USD | 2,220.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,560,000.00 USD | 231,380.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,560,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,560,000.00 USD | 434.45 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,580,000.00 USD | 18,610.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,580,000.00 USD | 166.83 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,580,000.00 USD | 674.29 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,580,000.00 USD | 101.58 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,580,000.00 USD | 109.36 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,580,000.00 USD | 116.69 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,580,000.00 USD | 163.41 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,580,000.00 USD | 102.01 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,580,000.00 USD | 102.12 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,580,000.00 USD | 714.59 USD | 0.00 USD | `+11.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,580,000.00 USD | 928.13 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,580,000.00 USD | 102.45 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,580,000.00 USD | 219.84 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,580,000.00 USD | 311.69 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,580,000.00 USD | 1,890.00 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,580,000.00 USD | 1,130.00 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,580,000.00 USD | 288.46 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,580,000.00 USD | 119.92 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,580,000.00 USD | 231.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,580,000.00 USD | 221.07 USD | 0.00 USD | `+13.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,590,000.00 USD | 992.00 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,590,000.00 USD | 148.48 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,590,000.00 USD | 191.36 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,590,000.00 USD | 4,440.00 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,590,000.00 USD | 108.21 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,590,000.00 USD | 169.68 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,590,000.00 USD | 574.66 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,590,000.00 USD | 121.87 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,590,000.00 USD | 115.88 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,590,000.00 USD | 340.05 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,590,000.00 USD | 742.12 USD | 0.00 USD | `+16.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,590,000.00 USD | 899.47 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,660,000.00 USD | 70,020.00 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,660,000.00 USD | 373.97 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,670,000.00 USD | 5,050.00 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,680,000.00 USD | 6,370.00 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,680,000.00 USD | 404.20 USD | 0.00 USD | `+19.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,890,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,890,000.00 USD | 1,150.00 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,890,000.00 USD | 172.16 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,890,000.00 USD | 922.87 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,890,000.00 USD | 489.40 USD | 0.00 USD | `+22.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,890,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,890,000.00 USD | 118.01 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,890,000.00 USD | 971.48 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,890,000.00 USD | 818.31 USD | 0.00 USD | `+23.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,890,000.00 USD | 312.31 USD | 0.00 USD | `+24.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,900,000.00 USD | 2,290.00 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,900,000.00 USD | 1,890.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,900,000.00 USD | 178.46 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,900,000.00 USD | 173.42 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,900,000.00 USD | 184.75 USD | 0.00 USD | `+26.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,900,000.00 USD | 135.78 USD | 0.00 USD | `+27.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,900,000.00 USD | 127.96 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,900,000.00 USD | 476.43 USD | 0.00 USD | `+28.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,900,000.00 USD | 869.35 USD | 0.00 USD | `+28.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,930,000.00 USD | 35,110.00 USD | 0.00 USD | `+29.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,930,000.00 USD | 251.06 USD | 0.00 USD | `+29.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,940,000.00 USD | 552.44 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,940,000.00 USD | 537.26 USD | 0.00 USD | `+30.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,940,000.00 USD | 1,110.00 USD | 0.00 USD | `+31.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,940,000.00 USD | 320.29 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,940,000.00 USD | 1,100.00 USD | 0.00 USD | `+32.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,940,000.00 USD | 2,270.00 USD | 0.00 USD | `+32.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,940,000.00 USD | 1,270.00 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,940,000.00 USD | 1,380.00 USD | 0.00 USD | `+34.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,950,000.00 USD | 2,410.00 USD | 0.00 USD | `+34.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,960,000.00 USD | 10,640.00 USD | 0.00 USD | `+35.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,960,000.00 USD | 2,050.00 USD | 0.00 USD | `+35.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,960,000.00 USD | 529.11 USD | 0.00 USD | `+35.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,970,000.00 USD | 7,700.00 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,970,000.00 USD | 906.03 USD | 0.00 USD | `+39.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,970,000.00 USD | 434.61 USD | 0.00 USD | `+40.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,970,000.00 USD | 163.52 USD | 0.00 USD | `+40.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,980,000.00 USD | 10,370.00 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,980,000.00 USD | 5,270.00 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,980,000.00 USD | 115.02 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,990,000.00 USD | 3,870.00 USD | 0.00 USD | `+50.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,990,000.00 USD | 197.97 USD | 0.00 USD | `+51.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,990,000.00 USD | 3,200.00 USD | 0.00 USD | `+52.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,990,000.00 USD | 179.58 USD | 0.00 USD | `+53.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,990,000.00 USD | 568.45 USD | 0.00 USD | `+53.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,990,000.00 USD | 169.57 USD | 0.00 USD | `+55.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,990,000.00 USD | 446.52 USD | 0.00 USD | `+57.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,000,000.00 USD | 5,320.00 USD | 0.00 USD | `+59.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,210,000.00 USD | 210,750.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,210,000.00 USD | 407.95 USD | 0.00 USD | `+61.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,210,000.00 USD | 174.91 USD | 0.00 USD | `+63.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,210,000.00 USD | 4,680.00 USD | 0.00 USD | `+65.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,210,000.00 USD | 960.26 USD | 0.00 USD | `+67.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,220,000.00 USD | 2,710.00 USD | 0.00 USD | `+69.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,220,000.00 USD | 805.90 USD | 0.00 USD | `+71.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,220,000.00 USD | 655.55 USD | 0.00 USD | `+73.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,220,000.00 USD | 4,890.00 USD | 0.00 USD | `+74.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,220,000.00 USD | 471.09 USD | 0.00 USD | `+75.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,220,000.00 USD | 383.85 USD | 0.00 USD | `+76.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,880,000.00 USD | 653,420.00 USD | 0.00 USD | `+77.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,880,000.00 USD | 1,510.00 USD | 0.00 USD | `+78.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,880,000.00 USD | 111.87 USD | 0.00 USD | `+87.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,880,000.00 USD | 219.91 USD | 0.00 USD | `+89.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.14` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,320.00 USD |
| `7D` | `7.16` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD |
| `7D` | `7.18` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD |
| `7D` | `7.20` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD |
| `7D` | `7.22` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,980.00 USD |
| `7D` | `7.24` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 39,910.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `7.26` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 0.00 USD | 1,810.00 USD | 58.08 USD |
| `7D` | `7.30` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `7.32` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD |
| `7D` | `7.36` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD |
| `7D` | `7.38` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.40` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.46` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.48` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.52` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `7.56` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.60` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 2,100.00 USD | 4,900.00 USD | 4,570.00 USD |
| `7D` | `7.60` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.61` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD |
| `1D` | `7.62` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD |
| `7D` | `7.62` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 626.55 USD | 2,130.00 USD | 996.08 USD |
| `1D` | `7.63` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD |
| `1D` | `7.64` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD |
| `7D` | `7.64` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD |
| `1D` | `7.65` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 817.75 USD | 9,870.00 USD |
| `1D` | `7.66` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `7D` | `7.66` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,600.00 USD |
| `1D` | `7.67` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 1,140.00 USD | 587.20 USD | 114.38 USD |
| `1D` | `7.68` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `7.68` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `7.69` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `7.70` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 4,140.00 USD | 2,390.00 USD | 16,770.00 USD |
| `7D` | `7.70` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 393.33 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.71` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD |
| `1D` | `7.72` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 701.68 USD | 568.00 USD | 2,430.00 USD |
| `7D` | `7.72` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 38,970.00 USD | 0.00 USD | 40,470.00 USD |
| `1D` | `7.73` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `7.74` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `7D` | `7.74` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `1D` | `7.76` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD |
| `7D` | `7.76` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD |
| `1D` | `7.77` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD |
| `1D` | `7.78` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `7D` | `7.78` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,810.00 USD |
| `1D` | `7.79` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD |
| `1D` | `7.80` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD |
| `7D` | `7.80` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,770.00 USD |
| `1D` | `7.81` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.82` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD |
| `7D` | `7.82` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD |
| `1D` | `7.83` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD |
| `1D` | `7.84` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 1,060.00 USD | 1,240.00 USD | 0.00 USD |
| `7D` | `7.84` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD |
| `1D` | `7.85` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 3,320.00 USD | 1,250.00 USD | 2,650.00 USD |
| `1D` | `7.86` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD |
| `7D` | `7.86` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD |
| `1D` | `7.87` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD |
| `1D` | `7.88` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 161,670.00 USD | 5,030.00 USD | 33,710.00 USD |
| `7D` | `7.88` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD |
| `1D` | `7.89` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD |
| `1D` | `7.90` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 56,620.00 USD | 6,970.00 USD | 5,990.00 USD |
| `7D` | `7.90` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 34,620.00 USD | 12,890.00 USD | 18,230.00 USD |
| `1D` | `7.91` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD |
| `1D` | `7.92` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,770.00 USD |
| `7D` | `7.92` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD |
| `1D` | `7.93` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `1D` | `7.94` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD |
| `7D` | `7.94` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD |
| `1D` | `7.96` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `7D` | `7.96` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD |
| `1D` | `7.97` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `1D` | `7.98` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD |
| `7D` | `7.98` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,450.00 USD |
| `1D` | `7.99` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD |
| `1D` | `8.00` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `7D` | `8.00` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD |
| `1D` | `8.02` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD |
| `7D` | `8.02` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 15,300.00 USD | 46,670.00 USD | 58,100.00 USD |
| `1D` | `8.03` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD |
| `1D` | `8.04` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `8.04` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 462,240.00 USD | 0.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD |
| `1D` | `8.06` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD |
| `7D` | `8.06` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD |
| `1D` | `8.07` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `1D` | `8.08` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `7D` | `8.08` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD |
| `1D` | `8.09` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD |
| `1D` | `8.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `7D` | `8.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD |
| `1D` | `8.11` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `1D` | `8.12` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,250.00 USD |
| `7D` | `8.12` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD |
| `1D` | `8.13` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 34,890.00 USD | 9,180.00 USD | 1,710.00 USD |
| `1D` | `8.14` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,260.00 USD |
| `7D` | `8.14` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 180,540.00 USD | 30,700.00 USD | 183,790.00 USD |
| `1D` | `8.15` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 43,510.00 USD | 12,240.00 USD | 53,660.00 USD |
| `1D` | `8.16` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 192.50 USD | 21,000.00 USD | 165,460.00 USD |
| `7D` | `8.16` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,310.00 USD |
| `1D` | `8.17` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD |
| `1D` | `8.18` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 7,140.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `8.18` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD |
| `1D` | `8.19` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD |
| `1D` | `8.20` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD |
| `7D` | `8.20` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 174,220.00 USD | 58,100.00 USD | 0.00 USD |
| `1D` | `8.21` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD |
| `1D` | `8.22` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD |
| `7D` | `8.22` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `8.23` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD |
| `1D` | `8.24` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 168.44 USD | 3,220.00 USD | 5,970.00 USD |
| `7D` | `8.24` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD |
| `1D` | `8.25` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD |
| `1D` | `8.26` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD |
| `7D` | `8.26` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD |
| `1D` | `8.27` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD |
| `1D` | `8.28` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `7D` | `8.28` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,800.00 USD |
| `1D` | `8.29` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `8.30` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD |
| `7D` | `8.30` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 264,780.00 USD | 17,210.00 USD | 21,020.00 USD |
| `1D` | `8.31` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD |
| `1D` | `8.32` | 905,490.00 USD | 0.00 USD | 905,490.00 USD | 73,050.00 USD | 6,080.00 USD | 14,060.00 USD |
| `7D` | `8.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD |
| `1D` | `8.33` | 812,300.00 USD | 0.00 USD | 812,300.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD |
| `1D` | `8.34` | 805,980.00 USD | 0.00 USD | 805,980.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD |
| `7D` | `8.34` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 4,430.00 USD |
| `1D` | `8.35` | 803,760.00 USD | 0.00 USD | 803,760.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD |
| `1D` | `8.36` | 766,980.00 USD | 0.00 USD | 766,980.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `7D` | `8.36` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `8.37` | 749,180.00 USD | 0.00 USD | 749,180.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD |
| `1D` | `8.38` | 734,050.00 USD | 0.00 USD | 734,050.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD |
| `7D` | `8.38` | 904,500.00 USD | 0.00 USD | 904,500.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `8.39` | 660,600.00 USD | 0.00 USD | 660,600.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `1D` | `8.40` | 513,630.00 USD | 0.00 USD | 513,630.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD |
| `7D` | `8.40` | 846,760.00 USD | 0.00 USD | 846,760.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD |
| `1D` | `8.41` | 439,550.00 USD | 0.00 USD | 439,550.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD |
| `1D` | `8.42` | 421,160.00 USD | 0.00 USD | 421,160.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `7D` | `8.42` | 752,220.00 USD | 0.00 USD | 752,220.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD |
| `1D` | `8.43` | 362,020.00 USD | 0.00 USD | 362,020.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD |
| `1D` | `8.44` | 265,400.00 USD | 0.00 USD | 265,400.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD |
| `7D` | `8.44` | 507,240.00 USD | 0.00 USD | 507,240.00 USD | 152,190.00 USD | 8,000.00 USD | 74,660.00 USD |
| `1D` | `8.45` | 61,420.00 USD | 0.00 USD | 61,420.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `8.46` | 272,390.00 USD | 0.00 USD | 272,390.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD |
| `1D` | `8.47` | 663.00 USD | 0.00 USD | 663.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 749.80 USD | 749.80 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 1,500.00 USD | 1,500.00 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.48` | 191,210.00 USD | 191,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191,210.00 USD |
| `7D` | `8.48` | 382,420.00 USD | 382,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 191,210.00 USD |
| `1D` | `8.49` | 1,510.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.70 USD |
| `7D` | `8.50` | 383,600.00 USD | 383,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,170.00 USD |
| `1D` | `8.51` | 173,950.00 USD | 173,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD |
| `1D` | `8.52` | 337,390.00 USD | 337,390.00 USD | 0.00 USD | 158,630.00 USD | 0.00 USD | 4,800.00 USD |
| `7D` | `8.52` | 589,420.00 USD | 589,420.00 USD | 0.00 USD | 113,820.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `8.53` | 361,570.00 USD | 361,570.00 USD | 0.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.54` | 564,530.00 USD | 564,530.00 USD | 0.00 USD | 202,800.00 USD | 0.00 USD | 156.94 USD |
| `7D` | `8.54` | 949,040.00 USD | 949,040.00 USD | 0.00 USD | 357,740.00 USD | 0.00 USD | 1,880.00 USD |
| `1D` | `8.55` | 591,300.00 USD | 591,300.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `1D` | `8.56` | 630,310.00 USD | 630,310.00 USD | 0.00 USD | 686.73 USD | 38,320.00 USD | 0.00 USD |
| `7D` | `8.56` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 144,180.00 USD | 122,650.00 USD | 790.79 USD |
| `1D` | `8.57` | 781,800.00 USD | 781,800.00 USD | 0.00 USD | 151,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 840,920.00 USD | 840,920.00 USD | 0.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.58` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 842,960.00 USD | 842,960.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.60` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `8.61` | 844,160.00 USD | 844,160.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `1D` | `8.62` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD |
| `7D` | `8.62` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.63` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD |
| `1D` | `8.64` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD |
| `7D` | `8.64` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.65` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD |
| `1D` | `8.66` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 6,230.00 USD | 2,020.00 USD | 14,040.00 USD |
| `7D` | `8.66` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 416.16 USD |
| `1D` | `8.67` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 880.60 USD | 9,960.00 USD | 56.72 USD |
| `1D` | `8.68` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD |
| `7D` | `8.68` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 30,000.00 USD | 117,540.00 USD |
| `1D` | `8.69` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD |
| `1D` | `8.70` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD |
| `7D` | `8.70` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD |
| `7D` | `8.72` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 609.73 USD |
| `1D` | `8.73` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD |
| `1D` | `8.74` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 38,500.00 USD | 3,500.00 USD | 17,580.00 USD |
| `7D` | `8.74` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD |
| `1D` | `8.75` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 33,520.00 USD | 8,970.00 USD | 16,930.00 USD |
| `1D` | `8.76` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD |
| `7D` | `8.76` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD |
| `1D` | `8.77` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD |
| `1D` | `8.78` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD |
| `7D` | `8.78` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD |
| `1D` | `8.79` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD |
| `1D` | `8.80` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD |
| `7D` | `8.80` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD |
| `1D` | `8.81` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD |
| `1D` | `8.82` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD |
| `7D` | `8.82` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 365,470.00 USD | 18,440.00 USD | 39,280.00 USD |
| `1D` | `8.83` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 171,230.00 USD | 19,400.00 USD | 7,020.00 USD |
| `1D` | `8.84` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 1,500.00 USD | 3,110.00 USD | 59,130.00 USD |
| `7D` | `8.84` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD |
| `1D` | `8.85` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD |
| `1D` | `8.86` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 2,060.00 USD | 1,470.00 USD | 607.55 USD |
| `7D` | `8.86` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD |
| `1D` | `8.87` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 8,900.00 USD |
| `1D` | `8.88` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD |
| `7D` | `8.88` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 13,040.00 USD | 3,410.00 USD | 32,950.00 USD |
| `1D` | `8.90` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 28,690.00 USD | 5,990.00 USD | 65,160.00 USD |
| `7D` | `8.90` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD |
| `1D` | `8.91` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD |
| `1D` | `8.92` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 1,110.00 USD | 3,220.00 USD | 6,040.00 USD |
| `7D` | `8.92` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD |
| `1D` | `8.93` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD |
| `1D` | `8.94` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD |
| `7D` | `8.94` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 129,180.00 USD | 0.00 USD | 11,850.00 USD |
| `1D` | `8.95` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 2,540.00 USD | 6,630.00 USD | 20,340.00 USD |
| `1D` | `8.96` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD |
| `7D` | `8.96` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD |
| `1D` | `8.98` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD |
| `1D` | `9.00` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD |
| `7D` | `9.00` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 370,780.00 USD | 17,920.00 USD | 41,010.00 USD |
| `1D` | `9.01` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD |
| `1D` | `9.02` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD |
| `7D` | `9.02` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 82,280.00 USD | 56,120.00 USD | 1,780.00 USD |
| `1D` | `9.03` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD |
| `1D` | `9.04` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD |
| `7D` | `9.04` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 137,460.00 USD | 74,750.00 USD | 16,220.00 USD |
| `1D` | `9.05` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 21,980.00 USD | 9,980.00 USD | 24,060.00 USD |
| `1D` | `9.06` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD |
| `7D` | `9.06` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.07` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 13,070.00 USD | 17,440.00 USD | 25,460.00 USD |
| `1D` | `9.08` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD |
| `7D` | `9.08` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 73,070.00 USD | 9,730.00 USD | 25,300.00 USD |
| `1D` | `9.10` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 16,320.00 USD | 12,520.00 USD | 34,160.00 USD |
| `7D` | `9.10` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD |
| `1D` | `9.11` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD |
| `1D` | `9.12` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 101,900.00 USD | 22,410.00 USD | 26,360.00 USD |
| `7D` | `9.12` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.13` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 75,260.00 USD | 15,960.00 USD | 40,180.00 USD |
| `1D` | `9.14` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD |
| `7D` | `9.14` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD |
| `1D` | `9.15` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 57,140.00 USD | 23,170.00 USD | 23,040.00 USD |
| `1D` | `9.16` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `7D` | `9.16` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 196,240.00 USD |
| `1D` | `9.17` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 80,160.00 USD | 3,200.00 USD | 49,540.00 USD |
| `1D` | `9.18` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD |
| `7D` | `9.18` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD |
| `1D` | `9.19` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 78,040.00 USD | 29,140.00 USD | 7,680.00 USD |
| `1D` | `9.20` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD |
| `7D` | `9.20` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 550,150.00 USD | 134,550.00 USD | 238,840.00 USD |
| `1D` | `9.21` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD |
| `1D` | `9.22` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 620,010.00 USD | 144,840.00 USD | 376,830.00 USD |
| `1D` | `9.23` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD |
| `1D` | `9.24` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 45,890.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `9.24` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 336,360.00 USD | 44,660.00 USD | 136,520.00 USD |
| `1D` | `9.25` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD |
| `7D` | `9.26` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 19,160.00 USD |
| `1D` | `9.27` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD |
| `1D` | `9.28` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD |
| `7D` | `9.28` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 352,980.00 USD | 69,460.00 USD | 136,920.00 USD |
| `1D` | `9.29` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 16,190.00 USD | 4,140.00 USD | 17,910.00 USD |
| `1D` | `9.30` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD |
| `7D` | `9.30` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 233,360.00 USD |
| `1D` | `9.31` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD |
| `1D` | `9.32` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD |
| `7D` | `9.32` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 242,590.00 USD | 51,970.00 USD | 309,560.00 USD |
| `1D` | `9.33` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD |
| `1D` | `9.34` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 46,210.00 USD | 3,660.00 USD | 5,580.00 USD |
| `7D` | `9.34` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 98,640.00 USD | 41,250.00 USD | 59,540.00 USD |
| `1D` | `9.35` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 13,620.00 USD | 817.75 USD | 14,910.00 USD |
| `1D` | `9.36` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `7D` | `9.36` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 215,620.00 USD | 64,120.00 USD | 97,710.00 USD |
| `1D` | `9.37` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 10,930.00 USD | 6,260.00 USD | 2,610.00 USD |
| `1D` | `9.38` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 14,740.00 USD | 0.00 USD | 13,750.00 USD |
| `7D` | `9.38` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 224,850.00 USD | 31,100.00 USD | 77,300.00 USD |
| `7D` | `9.40` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 105,030.00 USD |
| `7D` | `9.42` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 109,230.00 USD | 13,910.00 USD | 51,440.00 USD |
| `7D` | `9.44` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 80,230.00 USD | 19,420.00 USD | 43,220.00 USD |
| `7D` | `9.46` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 51,570.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `9.48` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 10,620.00 USD | 11,060.00 USD | 20,880.00 USD |
| `7D` | `9.50` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 65,230.00 USD | 12,050.00 USD | 52,470.00 USD |
| `7D` | `9.52` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 57,650.00 USD | 18,520.00 USD | 31,860.00 USD |
| `7D` | `9.54` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 11,650.00 USD | 13,310.00 USD | 930.52 USD |
| `7D` | `9.56` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 7,430.00 USD | 5,260.00 USD | 4,800.00 USD |
| `7D` | `9.58` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 35,340.00 USD | 2,380.00 USD | 26,910.00 USD |
| `7D` | `9.60` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 31,720.00 USD | 5,460.00 USD | 18,390.00 USD |
| `7D` | `9.62` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `352.03M` | Total OI Tokens: `41,509,660.8 AVAX`
  * 1h OI Change: `-0.24%` | 4h OI Change: `-1.54%` | 24h OI Change: `-7.01%`
  * Exchange Breakdown: Binance=`80.10M` | Bybit=`57.15M` | OKX=`11.48M` | Hyperliquid=`16.72M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.96K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0088%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0080%` | **USDT Bitget** | `0.0047%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `42.92%` | `57.08%` | `0.75` | 4,830,000.00 USD |
| `15M` | `Binance` | `47.21%` | `52.79%` | `0.89` | 1,140,000.00 USD |
| `15M` | `OKX` | `36.67%` | `63.33%` | `0.58` | 355,750.00 USD |
| `15M` | `Bybit` | `42.28%` | `57.72%` | `0.73` | 382,120.00 USD |
| `15M` | `KuCoin` | `39.27%` | `60.73%` | `0.65` | 20,650.00 USD |
| `15M` | `Gate` | `38.37%` | `61.63%` | `0.62` | 46,960.00 USD |
| `15M` | `Bitget` | `60.54%` | `39.46%` | `1.53` | 99,750.00 USD |
| `15M` | `BingX` | `11.52%` | `88.48%` | `0.13` | 511,710.00 USD |
| `15M` | `MEXC` | `46.69%` | `53.31%` | `0.88` | 1,590,000.00 USD |
| `15M` | `Bitunix` | `53.74%` | `46.26%` | `1.16` | 87,990.00 USD |
| `15M` | `Hyperliquid` | `32.03%` | `67.97%` | `0.47` | 58,930.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.44%` | `49.56%` | `1.02` | 427,140.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `94.81%` | `5.19%` | `18.27` | 22,210.00 USD |
| `15M` | `HTX` | `10.8%` | `89.2%` | `0.12` | 2,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `60.89%` | `39.11%` | `1.56` | 86,400.00 USD |
| `15M` | `Aster` | `22.91%` | `77.09%` | `0.30` | 2,100.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `68.34%` | `31.66%` | `2.16` | 5,270.00 USD |
| `15M` | `Whale Positions` | `47.21%` | `52.79%` | `0.89` | 1,140,000.00 USD |
| `15M` | `Global Accounts` | `42.92%` | `57.08%` | `0.75` | 4,830,000.00 USD |
| `1H` | `AVAX` | `44.17%` | `55.83%` | `0.79` | 18,850,000.00 USD |
| `1H` | `Binance` | `47.93%` | `52.07%` | `0.92` | 4,890,000.00 USD |
| `1H` | `OKX` | `62.55%` | `37.45%` | `1.67` | 1,220,000.00 USD |
| `1H` | `Bybit` | `46.43%` | `53.57%` | `0.87` | 898,420.00 USD |
| `1H` | `KuCoin` | `50.31%` | `49.69%` | `1.01` | 96,790.00 USD |
| `1H` | `Gate` | `53.1%` | `46.9%` | `1.13` | 510,760.00 USD |
| `1H` | `Bitget` | `30.49%` | `69.51%` | `0.44` | 363,400.00 USD |
| `1H` | `BingX` | `44.85%` | `55.15%` | `0.81` | 952,070.00 USD |
| `1H` | `MEXC` | `48.9%` | `51.1%` | `0.96` | 5,450,000.00 USD |
| `1H` | `Bitunix` | `49.5%` | `50.5%` | `0.98` | 1,450,000.00 USD |
| `1H` | `Hyperliquid` | `37.8%` | `62.2%` | `0.61` | 286,270.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.45%` | `45.55%` | `1.20` | 1,420,000.00 USD |
| `1H` | `Crypto.com` | `95.98%` | `4.02%` | `23.88` | 0.00 USD |
| `1H` | `WhiteBIT` | `6.62%` | `93.38%` | `0.07` | 602,790.00 USD |
| `1H` | `HTX` | `70.48%` | `29.52%` | `2.39` | 7,710.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `16.43%` | `83.57%` | `0.20` | 681,870.00 USD |
| `1H` | `Aster` | `25.79%` | `74.21%` | `0.35` | 3,720.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.01%` | `68.99%` | `0.45` | 32,820.00 USD |
| `1H` | `Whale Positions` | `47.93%` | `52.07%` | `0.92` | 4,890,000.00 USD |
| `1H` | `Global Accounts` | `44.17%` | `55.83%` | `0.79` | 18,850,000.00 USD |
| `4H` | `AVAX` | `47.06%` | `52.94%` | `0.89` | 84,300,000.00 USD |
| `4H` | `Binance` | `49.13%` | `50.87%` | `0.97` | 27,750,000.00 USD |
| `4H` | `OKX` | `49.14%` | `50.86%` | `0.97` | 5,730,000.00 USD |
| `4H` | `Bybit` | `45.15%` | `54.85%` | `0.82` | 5,960,000.00 USD |
| `4H` | `KuCoin` | `51.55%` | `48.45%` | `1.06` | 442,470.00 USD |
| `4H` | `Gate` | `46.39%` | `53.61%` | `0.87` | 2,310,000.00 USD |
| `4H` | `Bitget` | `41.44%` | `58.56%` | `0.71` | 2,650,000.00 USD |
| `4H` | `BingX` | `35.98%` | `64.02%` | `0.56` | 4,190,000.00 USD |
| `4H` | `MEXC` | `49.52%` | `50.48%` | `0.98` | 19,600,000.00 USD |
| `4H` | `Bitunix` | `49.25%` | `50.75%` | `0.97` | 7,290,000.00 USD |
| `4H` | `Hyperliquid` | `45.03%` | `54.97%` | `0.82` | 1,200,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.98%` | `51.02%` | `0.96` | 3,520,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.63%` | `85.37%` | `0.17` | 2,380,000.00 USD |
| `4H` | `HTX` | `41.42%` | `58.58%` | `0.71` | 71,530.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `56.15%` | `43.85%` | `1.28` | 970,780.00 USD |
| `4H` | `Aster` | `77.73%` | `22.27%` | `3.49` | 93,110.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.76%` | `52.24%` | `0.91` | 150,870.00 USD |
| `4H` | `Whale Positions` | `49.13%` | `50.87%` | `0.97` | 27,750,000.00 USD |
| `4H` | `Global Accounts` | `47.06%` | `52.94%` | `0.89` | 84,300,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.52` | `8.45` | 1,829,814.14 USD | 869,168.19 USD | 960,645.95 USD | -91,477.76 USD | `-5.00%` | `11B / 14S` |
| `5:00 UTC` | `8.51` | `8.50` | `8.51` | `8.52` | `8.48` | 752,301.06 USD | 385,792.91 USD | 366,508.15 USD | 19,284.76 USD | `+2.56%` | `8B / 9S` |
| `0:00 UTC` | `8.46` | `8.47` | `8.46` | `8.49` | `8.46` | 681,089.39 USD | 260,569.06 USD | 420,520.33 USD | -159,951.27 USD | `-23.48%` | `1B / 5S` |
| `5:00 UTC` | `8.49` | `8.48` | `8.49` | `8.50` | `8.45` | 460,668.30 USD | 266,426.92 USD | 194,241.38 USD | 72,185.55 USD | `+15.67%` | `10B / 4S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 702,848.74 USD | 346,932.98 USD | 355,915.76 USD | -8,982.78 USD | `-1.28%` | `2B / 6S` |
| `5:00 UTC` | `8.46` | `8.47` | `8.46` | `8.48` | `8.46` | 798,371.69 USD | 455,825.46 USD | 342,546.23 USD | 113,279.23 USD | `+14.19%` | `6B / 4S` |
| `0:00 UTC` | `8.47` | `8.46` | `8.47` | `8.48` | `8.44` | 1,028,869.35 USD | 429,609.02 USD | 599,260.32 USD | -169,651.30 USD | `-16.49%` | `4B / 8S` |
| `5:00 UTC` | `8.47` | `8.47` | `8.47` | `8.49` | `8.46` | 909,192.14 USD | 370,410.27 USD | 538,781.87 USD | -168,371.60 USD | `-18.52%` | `3B / 9S` |
| `0:00 UTC` | `8.47` | `8.48` | `8.47` | `8.49` | `8.46` | 824,624.01 USD | 408,080.13 USD | 416,543.88 USD | -8,463.75 USD | `-1.03%` | `2B / 3S` |
| `5:00 UTC` | `8.48` | `8.48` | `8.48` | `8.48` | `8.47` | 76,492.90 USD | 26,092.40 USD | 50,400.49 USD | -24,308.09 USD | `-31.78%` | `0B / 3S` |

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
| `5m` | -5,080.00 USD | 65,590.00 USD | **`ACCUMULATION`** |
| `15m` | 28,700.00 USD | 88,450.00 USD | **`ACCUMULATION`** |
| `30m` | -30,080.00 USD | -98,720.00 USD | **`DISTRIBUTION`** |
| `1h` | -77,450.00 USD | -201,960.00 USD | **`DISTRIBUTION`** |
| `2h` | -262,240.00 USD | -290,470.00 USD | **`DISTRIBUTION`** |
| `4h` | -353,620.00 USD | -873,450.00 USD | **`DISTRIBUTION`** |
| `6h` | 36,360.00 USD | -1,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 78,530.00 USD | 1,880,000.00 USD | **`ACCUMULATION`** |
| `12h` | -722,040.00 USD | -3,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,840,000.00 USD | -12,400,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,930,000.00 USD | -50,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,530,000.00 USD | -268,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.08K` | 15m=`+28.70K` | 1h=`-77.45K` | 24h=`-2.84M`
* Futures Capital Netflows: 5m=`+65.59K` | 15m=`+88.45K` | 1h=`-201.96K` | 24h=`-12.40M`
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.24` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.11` (Risk Distance: `0.1266` pts)
  * +2.5R Take Profit: `8.56`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.72` (Risk Distance: `0.1266` pts)
  * +2.5R Take Profit: `8.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.55`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
