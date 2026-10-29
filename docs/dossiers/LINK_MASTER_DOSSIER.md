# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 03:40:27 IST` (`2026-10-29 22:10:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.91` | **Live Ask Quote**: `11.00` | **Mid Price**: `10.96`
- **Spread Points**: `91.00` | **Spread BPS**: `83.06 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.96` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.03` | Lower -3.00σ Band: `10.88`
  * Upper +2.51σ Band: `11.02` | Lower -2.51σ Band: `10.90`
  * Upper +2.01σ Band: `11.00` | Lower -2.01σ Band: `10.91`
  * Upper +2.00σ Band: `11.00` | Lower -2.00σ Band: `10.91`
  * Upper +1.28σ Band: `10.99` | Lower -1.28σ Band: `10.92`
  * Upper +1.00σ Band: `10.98` | Lower -1.00σ Band: `10.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.96` | EMA-20=`10.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.96` (Slope: `+0.0000`) | EMA-100=`10.96`
  * Institutional Anchors: EMA-144=`10.96` | EMA-200=`10.96` (Slope: `+0.0000`) | EMA-233=`10.96`
- **Range Boundaries**: 24H High=`11.07` | 24H Low=`10.85` | Weekly High=`11.17` | Weekly Low=`10.74`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.13` (Distance: `-1.53%`)
  * Point of Control (POC) = `10.98` (Distance: `-0.15%`)
  * Value Area Low (VAL) = `10.91` (Distance: `+0.40%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.62` | Weekly POC=`11.42` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.90`
  * London Session (08:00-16:00 UTC): High=`11.00` | Low=`10.91`
  * New York Session (13:00-21:00 UTC): High=`11.02` | Low=`10.89`
  * Initial Balance (First Hour): IB High=`10.99` | IB Low=`10.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.91` - `11.00`
  * Optimal Trade Entry (OTE 0.705): `10.98`
  * Structural Invalidation Anchor (0.786): `11.04`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.08` | `11.10` | `11.03` | `11.05` | `58,718` | 649,953.80 USD | 26,486.40 USD | `+4.08%` | -8,419,385.59 USD | `+0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.04` | `11.06` | `10.96` | `10.97` | `180,280` | 1,985,569.76 USD | -352,886.54 USD | `-17.77%` | -8,772,272.13 USD | `-0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `10.97` | `10.97` | `10.96` | `10.96` | `7,799` | 85,503.11 USD | -61,562.40 USD | `-72.00%` | -8,833,834.53 USD | `+0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.19` | `11.27` | `11.10` | `11.11` | `273,518` | 3,064,696.05 USD | -537,371.74 USD | `-17.53%` | -8,266,680.08 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.11` | `11.13` | `11.03` | `11.05` | `223,403` | 2,476,363.14 USD | -129,068.03 USD | `-5.21%` | -8,395,748.11 USD | `+0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `11.04` | `11.06` | `10.96` | `10.96` | `187,567` | 2,065,455.75 USD | -409,237.96 USD | `-19.81%` | -8,804,986.07 USD | `-0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `11.69` | `11.69` | `10.87` | `10.99` | `3,805,467` | 42,673,690.41 USD | -4,269,954.14 USD | `-10.01%` | -5,856,672.77 USD | `-3.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `10.99` | `11.29` | `10.95` | `11.05` | `1,981,647` | 22,042,313.47 USD | -1,846,592.95 USD | `-8.38%` | -7,703,265.72 USD | `-1.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.06` | `10.96` | `10.96` | `188,079` | 2,071,072.87 USD | -414,448.94 USD | `-20.01%` | -8,117,714.66 USD | `-0.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.87` | `10.97` | `5,976,895` | 66,805,744.19 USD | -6,516,594.39 USD | `-9.75%` | -8,235,091.99 USD | `-2.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.87` | `10.97` | `5,976,895` | 66,805,744.19 USD | -6,516,594.39 USD | `-9.75%` | -8,235,091.99 USD | `-2.00` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`10.96`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `501` | `0x73ce...8ce9` | `LONG` | 4,413,727.99 USD | `400,011,600.00` | `12.05` | `10.88` | `9.12` | -406,025.71 USD | `-9.20%` | `5X Cross` |
| `853` | `0xb83d...6e36` | `SHORT` | 2,680,051.96 USD | `242,013,000.00` | `12.93` | `10.88` | `599.09` | 449,842.23 USD | `+16.78%` | `3X Cross` |
| `906` | `0x458d...ab3b` | `LONG` | 2,509,854.38 USD | `227,156,700.00` | `13.13` | `10.88` | `9.34` | -472,376.02 USD | `-18.82%` | `3X Isolated` |
| `1006` | `0xdd53...2b13` | `SHORT` | 2,248,103.07 USD | `206,475,300.00` | `11.92` | `10.88` | `307.02` | 213,119.86 USD | `+9.48%` | `3X Cross` |
| `1018` | `0x3dc9...54b0` | `SHORT` | 2,212,000.00 USD | `200,000,000.00` | `7.56` | `10.88` | `91.42` | -700,841.58 USD | `-31.68%` | `10X Cross` |
| `1042` | `0x45d2...4029` | `SHORT` | 2,140,138.50 USD | `195,500,000.00` | `11.54` | `10.88` | `216.97` | 116,344.93 USD | `+5.44%` | `10X Cross` |
| `1262` | `0x6540...f7b7` | `LONG` | 1,806,033.40 USD | `165,266,600.00` | `12.46` | `10.88` | `7.80` | -252,705.76 USD | `-13.99%` | `5X Isolated` |
| `1299` | `0xeadc...9d55` | `LONG` | 1,741,703.72 USD | `157,691,600.00` | `9.43` | `10.88` | `0.000000` | 255,048.82 USD | `+14.64%` | `10X Cross` |
| `1511` | `0x5b5d...c060` | `SHORT` | 1,463,103.38 USD | `131,775,500.00` | `13.61` | `10.88` | `1282.76` | 330,154.59 USD | `+22.57%` | `3X Cross` |
| `1712` | `0xf6f3...47f8` | `SHORT` | 1,251,582.67 USD | `115,024,600.00` | `11.42` | `10.88` | `20.50` | 61,747.51 USD | `+4.93%` | `5X Cross` |
| `1733` | `0x9df2...c665` | `SHORT` | 1,226,801.94 USD | `112,344,500.00` | `11.48` | `10.88` | `288.46` | 63,353.12 USD | `+5.16%` | `10X Cross` |
| `1875` | `0xfe7e...11b4` | `LONG` | 1,104,268.36 USD | `101,142,000.00` | `14.47` | `10.88` | `5.33` | -358,844.79 USD | `-32.50%` | `5X Isolated` |
| `1899` | `0x8af7...fa05` | `SHORT` | 1,078,169.59 USD | `98,661,200.00` | `14.08` | `10.88` | `205.44` | 311,012.95 USD | `+28.85%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.52` | 6,666.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.67K USD at 11.5200 USD [API] | `2026-10-28 13:52:39` |
| `ANNOUNCEMENT` | `INFO` | `13.19` | 10,315.36 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 10.32K USD at 13.1910 USD [API] | `2026-10-02 18:39:42` |
| `ANNOUNCEMENT` | `INFO` | `11.56` | 5,208.88 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.21K USD at 11.5650 USD [API] | `2026-10-28 15:01:32` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 5,267.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.27K USD at 11.5420 USD [API] | `2026-10-28 16:28:53` |
| `ANNOUNCEMENT` | `INFO` | `11.49` | 5,051.98 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.05K USD at 11.4870 USD [API] | `2026-10-28 17:16:52` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 6,901.90 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.90K USD at 11.5320 USD [API] | `2026-10-28 17:59:13` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 5,026.21 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.03K USD at 11.5280 USD [API] | `2026-10-28 18:00:56` |
| `ANNOUNCEMENT` | `INFO` | `11.62` | 6,665.82 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6190 USD [API] | `2026-10-28 18:30:48` |
| `ANNOUNCEMENT` | `INFO` | `11.70` | 5,466.71 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.6960 USD [API] | `2026-10-28 18:36:16` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 17,715.57 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 17.72K USD at 11.7120 USD [API] | `2026-10-28 18:37:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`12.15` (Vol: 165,900.00 USD, Dist: `+9.19%`) | Long MP=`10.83` (Vol: 149,200.00 USD, Dist: `--2.65%`)
  * 48H Horizon: Short MP=`12.22` (Vol: 221,500.00 USD, Dist: `+9.81%`) | Long MP=`10.83` (Vol: 149,200.00 USD, Dist: `--2.69%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 221,500.00 USD, Dist: `+9.81%`) | Long MP=`10.83` (Vol: 106,000.00 USD, Dist: `--2.69%`)
  * 7D Horizon: Short MP=`12.15` (Vol: 263,600.00 USD, Dist: `+9.22%`) | Long MP=`10.85` (Vol: 218,700.00 USD, Dist: `--2.46%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 486.45 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,230.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 4,150.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 27,030.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 2,620.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 961.07 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 592.95 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,190.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 2,510.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,630.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 3,750.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 13,360.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 6,300.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 12,630.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 4,470.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 17,540.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 50,880.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 239,270.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 883.08 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 91,360.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 886.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 20,990.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 748.14 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,600.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 1,520.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 22,830.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 790.76 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 68,690.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 9,240.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 80,020.00 USD | 11,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 23,300.00 USD | 11,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 7,650.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 34,470.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 37,510.00 USD | 11,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 14,440.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 686,800.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 8,460.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 52,130.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 9,870.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 19,770.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 9,240.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 14,100.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,010.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 171,890.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,410,000.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 29,940.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 35,750.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,780.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 53,810.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 21,580.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,370.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 312,090.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 28,570.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 505,780.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 76,580.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,720,000.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 41,710.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 26,730.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 12,490.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 9,080.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.69` | 6,410,000.00 USD | 6,410,000.00 USD | 5,240.00 USD | 0.00 USD | 18.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 33.95 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 54,360.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.77` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 19,550.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 142.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 2,730,000.00 USD | 2,730,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 2,710,000.00 USD | 2,710,000.00 USD | 13,840.00 USD | 5,510.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 2,690,000.00 USD | 2,690,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 6,330,000.00 USD | 6,330,000.00 USD | 14,920.00 USD | 22,040.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 760,400.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 2,690,000.00 USD | 2,690,000.00 USD | 7,630.00 USD | 11,250.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 6,740.00 USD | 11,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 2,630,000.00 USD | 2,630,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 647,590.00 USD | 989,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 6,250,000.00 USD | 6,250,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 2,620,000.00 USD | 2,620,000.00 USD | 4,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 6,250,000.00 USD | 6,250,000.00 USD | 279.85 USD | 0.00 USD | 5,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 6,240,000.00 USD | 6,240,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 6,190,000.00 USD | 6,190,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 28,910.00 USD | 342,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 2,610,000.00 USD | 2,610,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 6,130,000.00 USD | 6,130,000.00 USD | 56,890.00 USD | 3,240.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 6,050,000.00 USD | 6,050,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 5,990,000.00 USD | 5,990,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 2,600,000.00 USD | 2,600,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 5,880,000.00 USD | 5,880,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 2,570,000.00 USD | 2,570,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 5,580,000.00 USD | 5,580,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 35,700.00 USD | 313,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 2,510,000.00 USD | 2,510,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 5,460,000.00 USD | 5,460,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 2,500,000.00 USD | 2,500,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 5,280,000.00 USD | 5,280,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 2,450,000.00 USD | 2,450,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 5,200,000.00 USD | 5,200,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 2,430,000.00 USD | 2,430,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 5,010,000.00 USD | 5,010,000.00 USD | 58,810.00 USD | 28,270.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 2,380,000.00 USD | 2,380,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 4,900,000.00 USD | 4,900,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 14,650.00 USD | 277,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 2,330,000.00 USD | 2,330,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 4,830,000.00 USD | 4,830,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 2,310,000.00 USD | 2,310,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 4,790,000.00 USD | 4,790,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 2,290,000.00 USD | 2,290,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 4,710,000.00 USD | 4,710,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 2,260,000.00 USD | 2,260,000.00 USD | 20,220.00 USD | 10,800.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 4,570,000.00 USD | 4,570,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 2,220,000.00 USD | 2,220,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 4,500,000.00 USD | 4,500,000.00 USD | 38,090.00 USD | 11,060.00 USD | 42,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 16,780.00 USD | 262,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 2,150,000.00 USD | 2,150,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 4,410,000.00 USD | 4,410,000.00 USD | 56,700.00 USD | 22,760.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 2,130,000.00 USD | 2,130,000.00 USD | 18,720.00 USD | 4,750.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 4,320,000.00 USD | 4,320,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 2,100,000.00 USD | 2,100,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 4,280,000.00 USD | 4,280,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 2,050,000.00 USD | 2,050,000.00 USD | 29,580.00 USD | 4,150.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 4,190,000.00 USD | 4,190,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 1,990,000.00 USD | 1,990,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 4,150,000.00 USD | 4,150,000.00 USD | 55,490.00 USD | 18,800.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 68,110.00 USD | 246,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 1,980,000.00 USD | 1,980,000.00 USD | 58,790.00 USD | 23,780.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 4,050,000.00 USD | 4,050,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 1,890,000.00 USD | 1,890,000.00 USD | 37,820.00 USD | 16,800.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 3,940,000.00 USD | 3,940,000.00 USD | 33,510.00 USD | 35,040.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 1,820,000.00 USD | 1,820,000.00 USD | 15,270.00 USD | 2,520.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 3,840,000.00 USD | 3,840,000.00 USD | 63,970.00 USD | 47,830.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 1,800,000.00 USD | 1,800,000.00 USD | 45,910.00 USD | 25,430.00 USD | 44,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 3,680,000.00 USD | 3,680,000.00 USD | 43,710.00 USD | 37,950.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 1,680,000.00 USD | 1,680,000.00 USD | 13,260.00 USD | 21,530.00 USD | 32,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 3,580,000.00 USD | 3,580,000.00 USD | 30,090.00 USD | 4,420.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 40,290.00 USD | 177,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 1,620,000.00 USD | 1,620,000.00 USD | 57,290.00 USD | 16,150.00 USD | 46,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 3,510,000.00 USD | 3,510,000.00 USD | 21,160.00 USD | 6,740.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 1,500,000.00 USD | 1,500,000.00 USD | 17,410.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 3,450,000.00 USD | 3,450,000.00 USD | 18,290.00 USD | 1,120.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 1,480,000.00 USD | 1,480,000.00 USD | 30,770.00 USD | 9,600.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 3,420,000.00 USD | 3,420,000.00 USD | 16,910.00 USD | 10,190.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 1,420,000.00 USD | 1,420,000.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 3,390,000.00 USD | 3,390,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 1,410,000.00 USD | 1,410,000.00 USD | 12,810.00 USD | 6,780.00 USD | 73,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 3,350,000.00 USD | 3,350,000.00 USD | 17,290.00 USD | 4,890.00 USD | 18,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 50,130.00 USD | 137,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 1,310,000.00 USD | 1,310,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 3,310,000.00 USD | 3,310,000.00 USD | 16,290.00 USD | 15,210.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 1,290,000.00 USD | 1,290,000.00 USD | 86,290.00 USD | 57,540.00 USD | 57.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 3,270,000.00 USD | 3,270,000.00 USD | 57,970.00 USD | 1,400.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,150,000.00 USD | 1,150,000.00 USD | 73,580.00 USD | 27,960.00 USD | 25,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 3,190,000.00 USD | 3,190,000.00 USD | 86,860.00 USD | 80,110.00 USD | 120,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,020,000.00 USD | 1,020,000.00 USD | 30,650.00 USD | 1,080.00 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 2,900,000.00 USD | 2,900,000.00 USD | 193,560.00 USD | 98,340.00 USD | 113,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 991,420.00 USD | 991,420.00 USD | 78,370.00 USD | 44,000.00 USD | 69,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 2,490,000.00 USD | 2,490,000.00 USD | 231,680.00 USD | 80,790.00 USD | 82,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 86,320.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 799,740.00 USD | 799,740.00 USD | 976.86 USD | 32,010.00 USD | 42,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 2,100,000.00 USD | 2,100,000.00 USD | 110,460.00 USD | 44,310.00 USD | 164,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 724,380.00 USD | 724,380.00 USD | 64,750.00 USD | 42,700.00 USD | 106,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 1,780,000.00 USD | 1,780,000.00 USD | 235,210.00 USD | 36,770.00 USD | 196,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 510,350.00 USD | 510,350.00 USD | 23,940.00 USD | 4,880.00 USD | 0.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 1,310,000.00 USD | 1,310,000.00 USD | 274,660.00 USD | 1,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 481,540.00 USD | 481,540.00 USD | 97,980.00 USD | 43,900.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 1,040,000.00 USD | 1,040,000.00 USD | 418,090.00 USD | 21,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 317,520.00 USD | 317,520.00 USD | 98,180.00 USD | 17,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 596,430.00 USD | 596,430.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 1,240.00 USD | 1,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 202,280.00 USD | 202,280.00 USD | 96,940.00 USD | 23,010.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 288,830.00 USD | 288,830.00 USD | 165,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 50,880.00 USD | 50,880.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 123,250.00 USD | 123,250.00 USD | 44,540.00 USD | 22,500.00 USD | 36,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.01` | 19,950.00 USD | 19,950.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 37,550.00 USD | 37,550.00 USD | 0.00 USD | 37,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.03` | 9,370.00 USD | 9,370.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 6,540.00 USD | 6,540.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 14,040.00 USD | 14,040.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 18,180.00 USD | 18,180.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 106.40 USD | 106.40 USD | 0.00 USD | 0.00 USD | 106.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 23,970.00 USD | 23,970.00 USD | 5,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 738.70 USD | 738.70 USD | 632.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 30,790.00 USD | 30,790.00 USD | 6,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 2,630.00 USD | 2,630.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 33,200.00 USD | 33,200.00 USD | 2,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.15` | 450,140.00 USD | 450,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.16` | 30,610.00 USD | 30,610.00 USD | 337.20 USD | 27,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 37,170.00 USD | 37,170.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 78,350.00 USD | 78,350.00 USD | 0.00 USD | 47,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 207,860.00 USD | 207,860.00 USD | 42,870.00 USD | 39,010.00 USD | 47,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 348,330.00 USD | 348,330.00 USD | 311,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 513,560.00 USD | 513,560.00 USD | 262,060.00 USD | 587.72 USD | 43,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 548,900.00 USD | 548,900.00 USD | 200,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 679,270.00 USD | 679,270.00 USD | 69,220.00 USD | 399.60 USD | 96,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 1,010,000.00 USD | 1,010,000.00 USD | 330,300.00 USD | 0.00 USD | 129,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 779,060.00 USD | 779,060.00 USD | 28,620.00 USD | 815.00 USD | 70,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 1,460,000.00 USD | 1,460,000.00 USD | 256,120.00 USD | 0.00 USD | 191,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 1,080,000.00 USD | 1,080,000.00 USD | 62,190.00 USD | 47,250.00 USD | 186,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 1,670,000.00 USD | 1,670,000.00 USD | 104,970.00 USD | 56,970.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 61,620.00 USD | 80,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 1,980,000.00 USD | 1,980,000.00 USD | 28,170.00 USD | 44,160.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 1,430,000.00 USD | 1,430,000.00 USD | 63,250.00 USD | 66,390.00 USD | 82,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 2,130,000.00 USD | 2,130,000.00 USD | 54,410.00 USD | 8,920.00 USD | 81,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 1,680,000.00 USD | 1,680,000.00 USD | 197,970.00 USD | 55,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 60,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 6,720.00 USD | 456,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.36` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 97,070.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 71,610.00 USD | 99,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 1,910,000.00 USD | 1,910,000.00 USD | 51,260.00 USD | 55,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 24,030.00 USD | 96,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 2,260,000.00 USD | 2,260,000.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 2,720,000.00 USD | 2,720,000.00 USD | 133,220.00 USD | 51,980.00 USD | 91,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 2,370,000.00 USD | 2,370,000.00 USD | 42,610.00 USD | 18,500.00 USD | 52,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 2,980,000.00 USD | 2,980,000.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 99,610.00 USD | 556,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 2,470,000.00 USD | 2,470,000.00 USD | 34,610.00 USD | 51,530.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 3,070,000.00 USD | 3,070,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 2,490,000.00 USD | 2,490,000.00 USD | 14,310.00 USD | 4,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 3,210,000.00 USD | 3,210,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 2,590,000.00 USD | 2,590,000.00 USD | 31,090.00 USD | 33,490.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 3,280,000.00 USD | 3,280,000.00 USD | 40,840.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 2,650,000.00 USD | 2,650,000.00 USD | 29,340.00 USD | 13,740.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 3,370,000.00 USD | 3,370,000.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 2,740,000.00 USD | 2,740,000.00 USD | 31,460.00 USD | 16,150.00 USD | 41,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 2,110.00 USD | 558,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 2,820,000.00 USD | 2,820,000.00 USD | 64,190.00 USD | 635.25 USD | 15,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 793.25 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 2,890,000.00 USD | 2,890,000.00 USD | 45,400.00 USD | 335.85 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 3,090,000.00 USD | 3,090,000.00 USD | 124,870.00 USD | 7,320.00 USD | 67,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 3,510,000.00 USD | 3,510,000.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 3,160,000.00 USD | 3,160,000.00 USD | 42,200.00 USD | 0.00 USD | 34,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 3,540,000.00 USD | 3,540,000.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 60,080.00 USD | 618,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.67` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 3,270,000.00 USD | 3,270,000.00 USD | 59,600.00 USD | 28,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 3,840,000.00 USD | 3,840,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 3,520,000.00 USD | 3,520,000.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 3,650,000.00 USD | 3,650,000.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 3,870,000.00 USD | 3,870,000.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 2,100.00 USD | 620,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.76` | 3,700,000.00 USD | 3,700,000.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 4,020,000.00 USD | 4,020,000.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 3,780,000.00 USD | 3,780,000.00 USD | 27,290.00 USD | 18,740.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 4,090,000.00 USD | 4,090,000.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 14,340.00 USD | 473.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 4,260,000.00 USD | 4,260,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 3,830,000.00 USD | 3,830,000.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 4,390,000.00 USD | 4,390,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 3,960,000.00 USD | 3,960,000.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 4,600,000.00 USD | 4,600,000.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 2,440.00 USD | 623,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 4,030,000.00 USD | 4,030,000.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 4,630,000.00 USD | 4,630,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 4,130,000.00 USD | 4,130,000.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 4,690,000.00 USD | 4,690,000.00 USD | 40,020.00 USD | 16,380.00 USD | 71.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 4,190,000.00 USD | 4,190,000.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 4,770,000.00 USD | 4,770,000.00 USD | 82,030.00 USD | 0.00 USD | 397.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 4,360,000.00 USD | 4,360,000.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 4,840,000.00 USD | 4,840,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 4,420,000.00 USD | 4,420,000.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 5,090,000.00 USD | 5,090,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 4,530,000.00 USD | 4,530,000.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 5,700,000.00 USD | 5,700,000.00 USD | 358,410.00 USD | 35,140.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 4,700,000.00 USD | 4,700,000.00 USD | 45,290.00 USD | 23,470.00 USD | 98,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 6,070,000.00 USD | 6,070,000.00 USD | 221,400.00 USD | 17,110.00 USD | 130,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 4,810,000.00 USD | 4,810,000.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 6,490,000.00 USD | 6,490,000.00 USD | 164,140.00 USD | 5,360.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 4,890,000.00 USD | 4,890,000.00 USD | 42,950.00 USD | 12,770.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 7,140,000.00 USD | 7,140,000.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 5,200,000.00 USD | 5,200,000.00 USD | 161,540.00 USD | 56,910.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 7,790,000.00 USD | 7,790,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 5,620,000.00 USD | 5,620,000.00 USD | 187,660.00 USD | 85,390.00 USD | 147,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 8,360,000.00 USD | 8,360,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 5,820,000.00 USD | 5,820,000.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 8,660,000.00 USD | 8,660,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 5,900,000.00 USD | 5,900,000.00 USD | 36,180.00 USD | 16,940.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 8,930,000.00 USD | 8,930,000.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 6,110,000.00 USD | 6,110,000.00 USD | 109,700.00 USD | 46,460.00 USD | 50,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 9,200,000.00 USD | 9,200,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 6,270,000.00 USD | 6,270,000.00 USD | 77,410.00 USD | 33,200.00 USD | 55,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 9,790,000.00 USD | 9,790,000.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 6,510,000.00 USD | 6,510,000.00 USD | 126,410.00 USD | 37,730.00 USD | 67,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 9,950,000.00 USD | 9,950,000.00 USD | 26,820.00 USD | 72,790.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 6,710,000.00 USD | 6,710,000.00 USD | 112,590.00 USD | 48,130.00 USD | 41,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 10,280,000.00 USD | 10,280,000.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 6,860,000.00 USD | 6,860,000.00 USD | 77,890.00 USD | 43,820.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 10,690,000.00 USD | 10,690,000.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 6,920,000.00 USD | 6,920,000.00 USD | 12,890.00 USD | 16,780.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 10,900,000.00 USD | 10,900,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 6,950,000.00 USD | 6,950,000.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 11,200,000.00 USD | 11,200,000.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 552.48 USD | 623,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 7,000,000.00 USD | 7,000,000.00 USD | 19,270.00 USD | 10,210.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 11,430,000.00 USD | 11,430,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 7,130,000.00 USD | 7,130,000.00 USD | 83,960.00 USD | 17,410.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 11,950,000.00 USD | 11,950,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 7,240,000.00 USD | 7,240,000.00 USD | 57,170.00 USD | 14,910.00 USD | 36,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 12,190,000.00 USD | 12,190,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 7,250,000.00 USD | 7,250,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 12,460,000.00 USD | 12,460,000.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 7,290,000.00 USD | 7,290,000.00 USD | 20,540.00 USD | 5,120.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 12,600,000.00 USD | 12,600,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 624,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 7,310,000.00 USD | 7,310,000.00 USD | 8,930.00 USD | 13,210.00 USD | 3,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 12,670,000.00 USD | 12,670,000.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 7,340,000.00 USD | 7,340,000.00 USD | 12,730.00 USD | 6,420.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 13,210,000.00 USD | 13,210,000.00 USD | 160,660.00 USD | 42,040.00 USD | 338,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 7,400,000.00 USD | 7,400,000.00 USD | 18,470.00 USD | 12,140.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 13,410,000.00 USD | 13,410,000.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 7,480,000.00 USD | 7,480,000.00 USD | 57,750.00 USD | 13,980.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 14,010,000.00 USD | 14,010,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 7,510,000.00 USD | 7,510,000.00 USD | 17,590.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 14,420,000.00 USD | 14,420,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.46` | 7,530,000.00 USD | 7,530,000.00 USD | 128.41 USD | 9,440.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 14,570,000.00 USD | 14,570,000.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 7,540,000.00 USD | 7,540,000.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 14,740,000.00 USD | 14,740,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 7,550,000.00 USD | 7,550,000.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 14,990,000.00 USD | 14,990,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 7,610,000.00 USD | 7,610,000.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 15,300,000.00 USD | 15,300,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 7,630,000.00 USD | 7,630,000.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 15,540,000.00 USD | 15,540,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,870.00 USD | 626,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.56` | 7,680,000.00 USD | 7,680,000.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.57` | 15,730,000.00 USD | 15,730,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 7,690,000.00 USD | 7,690,000.00 USD | 6,550.00 USD | 1,030.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 15,850,000.00 USD | 15,850,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 7,710,000.00 USD | 7,710,000.00 USD | 15,650.00 USD | 3,320.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 15,980,000.00 USD | 15,980,000.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 7,750,000.00 USD | 7,750,000.00 USD | 13,530.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 16,150,000.00 USD | 16,150,000.00 USD | 64,120.00 USD | 28,270.00 USD | 81,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 7,790,000.00 USD | 7,790,000.00 USD | 31,080.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 16,350,000.00 USD | 16,350,000.00 USD | 76,240.00 USD | 26,110.00 USD | 90,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 527.51 USD | 626,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 7,820,000.00 USD | 7,820,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.67` | 16,640,000.00 USD | 16,640,000.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 7,840,000.00 USD | 7,840,000.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 16,880,000.00 USD | 16,880,000.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 16,970,000.00 USD | 16,970,000.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 7,870,000.00 USD | 7,870,000.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 17,070,000.00 USD | 17,070,000.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 7,910,000.00 USD | 7,910,000.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 17,140,000.00 USD | 17,140,000.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 7,980,000.00 USD | 7,980,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.77` | 17,220,000.00 USD | 17,220,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 8,000,000.00 USD | 8,000,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 17,310,000.00 USD | 17,310,000.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 8,030,000.00 USD | 8,030,000.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 17,340,000.00 USD | 17,340,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 8,040,000.00 USD | 8,040,000.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 17,360,000.00 USD | 17,360,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 8,070,000.00 USD | 8,070,000.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 17,450,000.00 USD | 17,450,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 627,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 8,110,000.00 USD | 8,110,000.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.87` | 17,480,000.00 USD | 17,480,000.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 8,110,000.00 USD | 8,110,000.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 17,570,000.00 USD | 17,570,000.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 8,140,000.00 USD | 8,140,000.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 17,670,000.00 USD | 17,670,000.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 8,150,000.00 USD | 8,150,000.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 17,700,000.00 USD | 17,700,000.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 8,150,000.00 USD | 8,150,000.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.95` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 1,470.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 17,710,000.00 USD | 17,710,000.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 17,750,000.00 USD | 17,750,000.00 USD | 13,890.00 USD | 10,560.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 17,820,000.00 USD | 17,820,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 17,820,000.00 USD | 17,820,000.00 USD | 1,290.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 17,830,000.00 USD | 17,830,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 17,830,000.00 USD | 17,830,000.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 1,520.00 USD | 628,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.07` | 17,840,000.00 USD | 17,840,000.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 17,850,000.00 USD | 17,850,000.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 17,870,000.00 USD | 17,870,000.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 17,880,000.00 USD | 17,880,000.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.17` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 17,900,000.00 USD | 17,900,000.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 17,920,000.00 USD | 17,920,000.00 USD | 13,890.00 USD | 213.60 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 17,930,000.00 USD | 17,930,000.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 18,000,000.00 USD | 18,000,000.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 18,030,000.00 USD | 18,030,000.00 USD | 10,290.00 USD | 14,120.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 18,040,000.00 USD | 18,040,000.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 18,070,000.00 USD | 18,070,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 18,080,000.00 USD | 18,080,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,280.00 USD | 633,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 2,990.00 USD | 636,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 347.04 USD | 637,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 541.88 USD | 637,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 321.55 USD | 638,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 663,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.15` | 368.14 USD | 663,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 664,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,350.00 USD | 720,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 721,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,530.00 USD | 722,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 17,510.00 USD | 740,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 10,770.00 USD | 750,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 830,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 2,330.00 USD | 832,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 121,870.00 USD | 954,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 5,480.00 USD | 960,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,790.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 72,830.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 707,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.35` | 2,340,000.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,270.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 10,800.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.95` | 17,530.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.45` | 12,670,000.00 USD | 0.00 USD | 1,850.00 USD | `-77.83%` | `756,900.00` |
| `Live` | `Long` | `2.55` | 12,670,000.00 USD | 0.00 USD | 25,070.00 USD | `-76.93%` | `9,829,500.00` |
| `Live` | `Long` | `2.65` | 12,650,000.00 USD | 0.00 USD | 2,550.00 USD | `-76.02%` | `961,300.00` |
| `Live` | `Long` | `2.95` | 12,640,000.00 USD | 0.00 USD | 9,610.00 USD | `-73.31%` | `3,259,000.00` |
| `Live` | `Long` | `3.05` | 12,630,000.00 USD | 0.00 USD | 6,640.00 USD | `-72.40%` | `2,176,000.00` |
| `Live` | `Long` | `3.15` | 12,630,000.00 USD | 0.00 USD | 297.99 USD | `-71.50%` | `94,600.00` |
| `Live` | `Long` | `3.25` | 12,630,000.00 USD | 0.00 USD | 2,990.00 USD | `-70.59%` | `920,000.00` |
| `Live` | `Long` | `3.35` | 12,620,000.00 USD | 0.00 USD | 796.30 USD | `-69.69%` | `237,700.00` |
| `Live` | `Long` | `3.45` | 12,620,000.00 USD | 0.00 USD | 10,470.00 USD | `-68.78%` | `3,034,300.00` |
| `Live` | `Long` | `3.65` | 12,610,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.97%` | `600,000.00` |
| `Live` | `Long` | `3.75` | 12,610,000.00 USD | 0.00 USD | 4,710.00 USD | `-66.07%` | `1,255,000.00` |
| `Live` | `Long` | `3.85` | 12,610,000.00 USD | 0.00 USD | 713.79 USD | `-65.16%` | `185,400.00` |
| `Live` | `Long` | `3.95` | 12,610,000.00 USD | 0.00 USD | 40,120.00 USD | `-64.26%` | `10,155,700.00` |
| `Live` | `Long` | `4.05` | 12,570,000.00 USD | 0.00 USD | 950.54 USD | `-63.35%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 12,560,000.00 USD | 0.00 USD | 251.91 USD | `-62.45%` | `60,700.00` |
| `Live` | `Long` | `4.25` | 12,560,000.00 USD | 0.00 USD | 11,890.00 USD | `-61.54%` | `2,797,900.00` |
| `Live` | `Long` | `4.35` | 12,550,000.00 USD | 0.00 USD | 1,490.00 USD | `-60.64%` | `341,500.00` |
| `Live` | `Long` | `4.45` | 12,550,000.00 USD | 0.00 USD | 381.37 USD | `-59.73%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 12,550,000.00 USD | 0.00 USD | 4,190.00 USD | `-58.83%` | `919,800.00` |
| `Live` | `Long` | `4.65` | 12,550,000.00 USD | 0.00 USD | 383.63 USD | `-57.92%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 12,550,000.00 USD | 0.00 USD | 237,160.00 USD | `-57.02%` | `49,928,100.00` |
| `Live` | `Long` | `4.85` | 12,310,000.00 USD | 0.00 USD | 1,620.00 USD | `-56.11%` | `334,900.00` |
| `Live` | `Long` | `4.95` | 12,310,000.00 USD | 0.00 USD | 883.08 USD | `-55.21%` | `178,400.00` |
| `Live` | `Long` | `5.05` | 12,310,000.00 USD | 0.00 USD | 9,450.00 USD | `-54.30%` | `1,871,300.00` |
| `Live` | `Long` | `5.15` | 12,300,000.00 USD | 0.00 USD | 266.26 USD | `-53.40%` | `51,700.00` |
| `Live` | `Long` | `5.25` | 12,300,000.00 USD | 0.00 USD | 886.73 USD | `-52.49%` | `168,900.00` |
| `Live` | `Long` | `5.35` | 12,300,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.59%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,750,000.00 USD | 0.00 USD | 16,490.00 USD | `-50.68%` | `3,025,500.00` |
| `Live` | `Long` | `5.55` | 11,740,000.00 USD | 0.00 USD | 2,750.00 USD | `-49.78%` | `495,200.00` |
| `Live` | `Long` | `5.65` | 11,730,000.00 USD | 0.00 USD | 35,720.00 USD | `-48.87%` | `6,321,800.00` |
| `Live` | `Long` | `5.75` | 11,700,000.00 USD | 0.00 USD | 102,400.00 USD | `-47.97%` | `17,809,500.00` |
| `Live` | `Long` | `5.85` | 11,600,000.00 USD | 0.00 USD | 20,170.00 USD | `-47.06%` | `3,447,900.00` |
| `Live` | `Long` | `5.95` | 11,580,000.00 USD | 0.00 USD | 5,690.00 USD | `-46.16%` | `956,800.00` |
| `Live` | `Long` | `6.05` | 11,570,000.00 USD | 0.00 USD | 68,200.00 USD | `-45.25%` | `11,272,000.00` |
| `Live` | `Long` | `6.15` | 11,500,000.00 USD | 0.00 USD | 6,240.00 USD | `-44.35%` | `1,013,900.00` |
| `Live` | `Long` | `6.25` | 11,500,000.00 USD | 0.00 USD | 88,130.00 USD | `-43.44%` | `14,101,300.00` |
| `Live` | `Long` | `6.35` | 11,410,000.00 USD | 0.00 USD | 15,990.00 USD | `-42.54%` | `2,518,400.00` |
| `Live` | `Long` | `6.45` | 11,390,000.00 USD | 0.00 USD | 16,300.00 USD | `-41.63%` | `2,527,100.00` |
| `Live` | `Long` | `6.55` | 11,380,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.73%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 11,370,000.00 USD | 0.00 USD | 9,260.00 USD | `-39.82%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 11,360,000.00 USD | 0.00 USD | 3,350.00 USD | `-38.92%` | `496,500.00` |
| `Live` | `Long` | `6.85` | 11,360,000.00 USD | 0.00 USD | 71,320.00 USD | `-38.01%` | `10,412,100.00` |
| `Live` | `Long` | `6.95` | 11,290,000.00 USD | 0.00 USD | 810.37 USD | `-37.11%` | `116,600.00` |
| `Live` | `Long` | `7.05` | 11,290,000.00 USD | 0.00 USD | 2,560.00 USD | `-36.20%` | `363,400.00` |
| `Live` | `Long` | `7.15` | 11,290,000.00 USD | 0.00 USD | 42,950.00 USD | `-35.30%` | `6,007,300.00` |
| `Live` | `Long` | `7.25` | 11,240,000.00 USD | 0.00 USD | 10,500.00 USD | `-34.40%` | `1,448,500.00` |
| `Live` | `Long` | `7.35` | 11,230,000.00 USD | 0.00 USD | 33,870.00 USD | `-33.49%` | `4,607,900.00` |
| `Live` | `Long` | `7.45` | 11,200,000.00 USD | 0.00 USD | 6,280.00 USD | `-32.59%` | `843,100.00` |
| `Live` | `Long` | `7.55` | 11,190,000.00 USD | 0.00 USD | 17,880.00 USD | `-31.68%` | `2,368,600.00` |
| `Live` | `Long` | `7.65` | 11,170,000.00 USD | 0.00 USD | 52,770.00 USD | `-30.78%` | `6,897,400.00` |
| `Live` | `Long` | `7.75` | 11,120,000.00 USD | 0.00 USD | 14,300.00 USD | `-29.87%` | `1,844,600.00` |
| `Live` | `Long` | `7.85` | 11,110,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-28.97%` | `165,733,400.00` |
| `Live` | `Long` | `7.95` | 9,810,000.00 USD | 0.00 USD | 13,390.00 USD | `-28.06%` | `1,684,800.00` |
| `Live` | `Long` | `8.05` | 9,790,000.00 USD | 0.00 USD | 65,630.00 USD | `-27.16%` | `8,152,700.00` |
| `Live` | `Long` | `8.15` | 9,730,000.00 USD | 0.00 USD | 193,680.00 USD | `-26.25%` | `23,764,700.00` |
| `Live` | `Long` | `8.25` | 9,530,000.00 USD | 0.00 USD | 42,600.00 USD | `-25.35%` | `5,163,100.00` |
| `Live` | `Long` | `8.35` | 9,490,000.00 USD | 0.00 USD | 12,890.00 USD | `-24.44%` | `1,543,700.00` |
| `Live` | `Long` | `8.45` | 9,480,000.00 USD | 0.00 USD | 14,470.00 USD | `-23.54%` | `1,712,400.00` |
| `Live` | `Long` | `8.55` | 9,460,000.00 USD | 0.00 USD | 17,800.00 USD | `-22.63%` | `2,082,000.00` |
| `Live` | `Long` | `8.65` | 9,450,000.00 USD | 0.00 USD | 19,940.00 USD | `-21.73%` | `2,305,500.00` |
| `Live` | `Long` | `8.75` | 9,430,000.00 USD | 0.00 USD | 308,140.00 USD | `-20.82%` | `35,215,700.00` |
| `Live` | `Long` | `8.85` | 9,120,000.00 USD | 0.00 USD | 28,570.00 USD | `-19.92%` | `3,228,700.00` |
| `Live` | `Long` | `8.95` | 9,090,000.00 USD | 0.00 USD | 457,490.00 USD | `-19.01%` | `51,116,100.00` |
| `Live` | `Long` | `9.05` | 8,630,000.00 USD | 0.00 USD | 66,460.00 USD | `-18.11%` | `7,343,500.00` |
| `Live` | `Long` | `9.15` | 8,560,000.00 USD | 0.00 USD | 3,770,000.00 USD | `-17.20%` | `412,377,300.00` |
| `Live` | `Long` | `9.25` | 4,790,000.00 USD | 0.00 USD | 5,600.00 USD | `-16.30%` | `605,100.00` |
| `Live` | `Long` | `9.35` | 4,790,000.00 USD | 0.00 USD | 2,160,000.00 USD | `-15.39%` | `231,375,700.00` |
| `Live` | `Long` | `9.45` | 2,620,000.00 USD | 0.00 USD | 33,630.00 USD | `-14.49%` | `3,558,800.00` |
| `Live` | `Long` | `9.55` | 2,590,000.00 USD | 0.00 USD | 14,810.00 USD | `-13.58%` | `1,550,700.00` |
| `Live` | `Long` | `9.65` | 2,570,000.00 USD | 0.00 USD | 10,670.00 USD | `-12.68%` | `1,106,100.00` |
| `Live` | `Long` | `9.75` | 2,560,000.00 USD | 0.00 USD | 156,790.00 USD | `-11.77%` | `16,081,200.00` |
| `Live` | `Long` | `9.85` | 2,410,000.00 USD | 0.00 USD | 118,790.00 USD | `-10.87%` | `12,060,100.00` |
| `Live` | `Long` | `9.95` | 2,290,000.00 USD | 0.00 USD | 829,740.00 USD | `-9.96%` | `83,391,300.00` |
| `Live` | `Long` | `10.05` | 1,460,000.00 USD | 0.00 USD | 660,920.00 USD | `-9.06%` | `65,763,600.00` |
| `Live` | `Long` | `10.15` | 797,240.00 USD | 0.00 USD | 16,120.00 USD | `-8.15%` | `1,588,300.00` |
| `Live` | `Long` | `10.25` | 781,120.00 USD | 0.00 USD | 35,850.00 USD | `-7.25%` | `3,497,200.00` |
| `Live` | `Long` | `10.35` | 745,280.00 USD | 0.00 USD | 6,390.00 USD | `-6.34%` | `617,200.00` |
| `Live` | `Long` | `10.45` | 738,890.00 USD | 0.00 USD | 16,050.00 USD | `-5.44%` | `1,535,700.00` |
| `Live` | `Long` | `10.55` | 722,840.00 USD | 0.00 USD | 439,980.00 USD | `-4.53%` | `41,704,600.00` |
| `Live` | `Long` | `10.65` | 282,860.00 USD | 0.00 USD | 156,990.00 USD | `-3.63%` | `14,741,200.00` |
| `Live` | `Long` | `10.75` | 125,860.00 USD | 0.00 USD | 38,850.00 USD | `-2.72%` | `3,613,800.00` |
| `Live` | `Long` | `10.85` | 87,020.00 USD | 0.00 USD | 86,340.00 USD | `-1.82%` | `7,957,400.00` |
| `Live` | `Long` | `10.95` | 677.80 USD | 0.00 USD | 677.80 USD | `-0.91%` | `61,900.00` |
| `Live` | `Short` | `11.05` | 2,160.00 USD | 2,160.00 USD | 0.00 USD | `-0.01%` | `195,300.00` |
| `Live` | `Short` | `11.25` | 4,580.00 USD | 2,420.00 USD | 0.00 USD | `+1.80%` | `215,000.00` |
| `Live` | `Short` | `11.65` | 10,180.00 USD | 5,600.00 USD | 0.00 USD | `+5.42%` | `480,700.00` |
| `Live` | `Short` | `11.75` | 72,180.00 USD | 62,000.00 USD | 0.00 USD | `+6.33%` | `5,276,800.00` |
| `Live` | `Short` | `12.25` | 73,190.00 USD | 1,010.00 USD | 0.00 USD | `+10.85%` | `82,200.00` |
| `Live` | `Short` | `12.35` | 73,920.00 USD | 736.06 USD | 0.00 USD | `+11.75%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 74,160.00 USD | 242.22 USD | 0.00 USD | `+13.56%` | `19,300.00` |
| `Live` | `Short` | `12.75` | 74,700.00 USD | 531.68 USD | 0.00 USD | `+15.37%` | `41,700.00` |
| `Live` | `Short` | `12.85` | 76,450.00 USD | 1,760.00 USD | 0.00 USD | `+16.28%` | `136,700.00` |
| `Live` | `Short` | `13.45` | 81,740.00 USD | 5,280.00 USD | 0.00 USD | `+21.71%` | `392,900.00` |
| `Live` | `Short` | `13.55` | 83,330.00 USD | 1,590.00 USD | 0.00 USD | `+22.61%` | `117,500.00` |
| `Live` | `Short` | `14.05` | 83,430.00 USD | 102.56 USD | 0.00 USD | `+27.14%` | `7,300.00` |
| `Live` | `Short` | `14.15` | 83,780.00 USD | 349.51 USD | 0.00 USD | `+28.04%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 84,330.00 USD | 544.35 USD | 0.00 USD | `+28.95%` | `38,200.00` |
| `Live` | `Short` | `14.45` | 84,600.00 USD | 276.00 USD | 0.00 USD | `+30.76%` | `19,100.00` |
| `Live` | `Short` | `14.75` | 84,920.00 USD | 321.55 USD | 0.00 USD | `+33.47%` | `21,800.00` |
| `Live` | `Short` | `14.95` | 110,260.00 USD | 25,330.00 USD | 0.00 USD | `+35.28%` | `1,694,600.00` |
| `Live` | `Short` | `15.15` | 172,760.00 USD | 62,510.00 USD | 0.00 USD | `+37.09%` | `4,125,800.00` |
| `Live` | `Short` | `15.25` | 172,920.00 USD | 155.55 USD | 0.00 USD | `+38.00%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 173,760.00 USD | 838.14 USD | 0.00 USD | `+40.71%` | `53,900.00` |
| `Live` | `Short` | `15.65` | 174,040.00 USD | 284.83 USD | 0.00 USD | `+41.62%` | `18,200.00` |
| `Live` | `Short` | `15.85` | 174,310.00 USD | 271.04 USD | 0.00 USD | `+43.43%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 174,450.00 USD | 138.76 USD | 0.00 USD | `+44.33%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 175,850.00 USD | 1,390.00 USD | 0.00 USD | `+47.95%` | `85,300.00` |
| `Live` | `Short` | `16.75` | 193,570.00 USD | 17,720.00 USD | 0.00 USD | `+51.57%` | `1,058,000.00` |
| `Live` | `Short` | `16.95` | 284,170.00 USD | 90,600.00 USD | 0.00 USD | `+53.38%` | `5,345,300.00` |
| `Live` | `Short` | `17.15` | 286,510.00 USD | 2,330.00 USD | 0.00 USD | `+55.19%` | `136,100.00` |
| `Live` | `Short` | `17.45` | 381,520.00 USD | 95,020.00 USD | 0.00 USD | `+57.90%` | `5,445,000.00` |
| `Live` | `Short` | `17.55` | 382,910.00 USD | 1,390.00 USD | 0.00 USD | `+58.81%` | `79,100.00` |
| `Live` | `Short` | `17.75` | 410,230.00 USD | 27,320.00 USD | 0.00 USD | `+60.62%` | `1,539,000.00` |
| `Live` | `Short` | `17.85` | 659,800.00 USD | 249,580.00 USD | 0.00 USD | `+61.52%` | `13,982,000.00` |
| `Live` | `Short` | `17.95` | 660,160.00 USD | 351.82 USD | 0.00 USD | `+62.43%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 667,710.00 USD | 7,550.00 USD | 0.00 USD | `+63.33%` | `418,300.00` |
| `Live` | `Short` | `18.25` | 676,120.00 USD | 8,420.00 USD | 0.00 USD | `+65.14%` | `461,100.00` |
| `Live` | `Short` | `18.35` | 676,240.00 USD | 121.11 USD | 0.00 USD | `+66.05%` | `6,600.00` |
| `Live` | `Short` | `18.45` | 680,130.00 USD | 3,890.00 USD | 0.00 USD | `+66.95%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 710,450.00 USD | 30,310.00 USD | 0.00 USD | `+67.86%` | `1,634,200.00` |
| `Live` | `Short` | `18.65` | 710,630.00 USD | 186.50 USD | 0.00 USD | `+68.76%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 726,710.00 USD | 16,080.00 USD | 0.00 USD | `+69.67%` | `857,700.00` |
| `Live` | `Short` | `18.85` | 727,170.00 USD | 456.17 USD | 0.00 USD | `+70.57%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 800,980.00 USD | 73,810.00 USD | 0.00 USD | `+71.48%` | `3,895,000.00` |
| `Live` | `Short` | `19.05` | 1,520,000.00 USD | 718,380.00 USD | 0.00 USD | `+72.38%` | `37,710,000.00` |
| `Live` | `Short` | `19.55` | 2,340,000.00 USD | 820,020.00 USD | 0.00 USD | `+76.91%` | `41,944,600.00` |
| `Live` | `Short` | `19.65` | 2,380,000.00 USD | 38,790.00 USD | 0.00 USD | `+77.81%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,380,000.00 USD | 291.27 USD | 0.00 USD | `+80.53%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 4,700,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+82.34%` | `115,024,600.00` |
| `Live` | `Short` | `20.55` | 4,700,000.00 USD | 7,250.00 USD | 0.00 USD | `+85.96%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 4,710,000.00 USD | 2,040.00 USD | 0.00 USD | `+88.67%` | `97,800.00` |
| `Live` | `Short` | `21.05` | 4,710,000.00 USD | 5,700.00 USD | 0.00 USD | `+90.48%` | `270,600.00` |
| `Live` | `Short` | `21.35` | 4,710,000.00 USD | 3,680.00 USD | 0.00 USD | `+93.20%` | `172,500.00` |
| `Live` | `Short` | `21.85` | 4,720,000.00 USD | 2,740.00 USD | 0.00 USD | `+97.72%` | `125,600.00` |
| `Live` | `Short` | `21.95` | 4,720,000.00 USD | 140.48 USD | 0.00 USD | `+98.62%` | `6,400.00` |
| `Live` | `Short` | `22.05` | 4,720,000.00 USD | 1,020.00 USD | 0.00 USD | `+99.53%` | `46,100.00` |
| `Live` | `Short` | `22.15` | 4,730,000.00 USD | 16,090.00 USD | 0.00 USD | `+100.43%` | `726,300.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 635,490.00 USD | 0.00 USD | 431.68 USD | `-67.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 635,060.00 USD | 0.00 USD | 290.29 USD | `-58.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 634,770.00 USD | 0.00 USD | 120.22 USD | `-52.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 634,650.00 USD | 0.00 USD | 107.09 USD | `-45.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 634,540.00 USD | 0.00 USD | 4,260.00 USD | `-40.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 630,280.00 USD | 0.00 USD | 133.00 USD | `-39.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 630,150.00 USD | 0.00 USD | 3,770.00 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 626,380.00 USD | 0.00 USD | 2,070.00 USD | `-34.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 624,310.00 USD | 0.00 USD | 3,740.00 USD | `-32.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 620,570.00 USD | 0.00 USD | 1,050.00 USD | `-31.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 619,510.00 USD | 0.00 USD | 146.80 USD | `-28.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 619,370.00 USD | 0.00 USD | 5,000.00 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 614,360.00 USD | 0.00 USD | 564.79 USD | `-26.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 613,800.00 USD | 0.00 USD | 10,660.00 USD | `-25.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 603,140.00 USD | 0.00 USD | 1,360.00 USD | `-23.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 601,780.00 USD | 0.00 USD | 52,990.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 548,790.00 USD | 0.00 USD | 186.84 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 548,610.00 USD | 0.00 USD | 742.88 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 547,860.00 USD | 0.00 USD | 196.47 USD | `-19.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 547,670.00 USD | 0.00 USD | 1,320.00 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 546,350.00 USD | 0.00 USD | 2,240.00 USD | `-18.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 544,110.00 USD | 0.00 USD | 194.90 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 543,910.00 USD | 0.00 USD | 4,940.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 538,970.00 USD | 0.00 USD | 2,090.00 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 536,880.00 USD | 0.00 USD | 10,530.00 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 526,350.00 USD | 0.00 USD | 3,550.00 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 522,800.00 USD | 0.00 USD | 6,490.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 516,310.00 USD | 0.00 USD | 23,380.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 492,930.00 USD | 0.00 USD | 300,150.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 192,780.00 USD | 0.00 USD | 2,590.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 190,190.00 USD | 0.00 USD | 1,050.00 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 189,140.00 USD | 0.00 USD | 93,280.00 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 95,860.00 USD | 0.00 USD | 7,430.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 88,430.00 USD | 0.00 USD | 31,450.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 56,980.00 USD | 0.00 USD | 25,350.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 31,630.00 USD | 0.00 USD | 2,300.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 29,330.00 USD | 0.00 USD | 10,250.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 19,080.00 USD | 0.00 USD | 12,140.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 6,940.00 USD | 0.00 USD | 981.12 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 5,960.00 USD | 0.00 USD | 5,960.00 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 958.90 USD | 958.90 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 66,070.00 USD | 65,110.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 76,080.00 USD | 10,000.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 76,750.00 USD | 674.40 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 78,870.00 USD | 2,120.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 79,600.00 USD | 732.79 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 80,180.00 USD | 578.10 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 80,660.00 USD | 484.67 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 83,960.00 USD | 3,290.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 137,620.00 USD | 53,670.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 138,290.00 USD | 663.39 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 154,270.00 USD | 15,980.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 154,930.00 USD | 658.25 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 155,170.00 USD | 240.28 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 275,470.00 USD | 120,300.00 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 359,340.00 USD | 83,880.00 USD | 0.00 USD | `+14.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 368,780.00 USD | 9,430.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 388,830.00 USD | 20,060.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 389,290.00 USD | 461.02 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 405,920.00 USD | 16,630.00 USD | 0.00 USD | `+18.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 406,970.00 USD | 1,050.00 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 408,290.00 USD | 1,320.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 413,020.00 USD | 4,730.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 415,210.00 USD | 2,200.00 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 415,380.00 USD | 165.31 USD | 0.00 USD | `+22.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 417,530.00 USD | 2,150.00 USD | 0.00 USD | `+23.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 419,590.00 USD | 2,060.00 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 423,940.00 USD | 4,350.00 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 424,210.00 USD | 266.44 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 448,990.00 USD | 24,790.00 USD | 0.00 USD | `+27.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 449,500.00 USD | 506.57 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 452,910.00 USD | 3,410.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 453,630.00 USD | 718.16 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 453,850.00 USD | 218.25 USD | 0.00 USD | `+31.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 456,460.00 USD | 2,610.00 USD | 0.00 USD | `+32.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 469,380.00 USD | 12,920.00 USD | 0.00 USD | `+33.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 470,330.00 USD | 950.82 USD | 0.00 USD | `+35.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 482,950.00 USD | 12,620.00 USD | 0.00 USD | `+36.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 487,060.00 USD | 4,110.00 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 720,100.00 USD | 233,040.00 USD | 0.00 USD | `+38.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 721,280.00 USD | 1,180.00 USD | 0.00 USD | `+38.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 722,170.00 USD | 893.01 USD | 0.00 USD | `+39.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 723,270.00 USD | 1,100.00 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 724,220.00 USD | 949.96 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 726,550.00 USD | 2,330.00 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 731,890.00 USD | 5,340.00 USD | 0.00 USD | `+43.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 737,390.00 USD | 5,500.00 USD | 0.00 USD | `+44.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 746,560.00 USD | 9,170.00 USD | 0.00 USD | `+45.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 753,360.00 USD | 6,800.00 USD | 0.00 USD | `+46.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 772,120.00 USD | 18,760.00 USD | 0.00 USD | `+47.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 806,350.00 USD | 34,220.00 USD | 0.00 USD | `+47.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 812,930.00 USD | 6,580.00 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 822,860.00 USD | 9,930.00 USD | 0.00 USD | `+49.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 836,180.00 USD | 13,320.00 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 850,410.00 USD | 14,240.00 USD | 0.00 USD | `+51.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 934,770.00 USD | 84,360.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 936,460.00 USD | 1,700.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 945,970.00 USD | 9,510.00 USD | 0.00 USD | `+54.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 947,690.00 USD | 1,710.00 USD | 0.00 USD | `+55.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 949,990.00 USD | 2,300.00 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,050,000.00 USD | 98,330.00 USD | 0.00 USD | `+57.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,070,000.00 USD | 19,070.00 USD | 0.00 USD | `+57.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,070,000.00 USD | 4,390.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,080,000.00 USD | 6,200.00 USD | 0.00 USD | `+59.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,080,000.00 USD | 4,440.00 USD | 0.00 USD | `+60.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,090,000.00 USD | 4,460.00 USD | 0.00 USD | `+61.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,090,000.00 USD | 448.75 USD | 0.00 USD | `+62.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,120,000.00 USD | 35,940.00 USD | 0.00 USD | `+63.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,120,000.00 USD | 453.75 USD | 0.00 USD | `+64.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,120,000.00 USD | 830.38 USD | 0.00 USD | `+65.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,130,000.00 USD | 458.75 USD | 0.00 USD | `+66.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,130,000.00 USD | 461.25 USD | 0.00 USD | `+66.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,130,000.00 USD | 4,540.00 USD | 0.00 USD | `+67.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,130,000.00 USD | 466.25 USD | 0.00 USD | `+68.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,130,000.00 USD | 468.75 USD | 0.00 USD | `+69.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,130,000.00 USD | 1,960.00 USD | 0.00 USD | `+70.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,130,000.00 USD | 473.75 USD | 0.00 USD | `+71.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,200,000.00 USD | 67,000.00 USD | 0.00 USD | `+72.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,200,000.00 USD | 574.50 USD | 0.00 USD | `+73.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,200,000.00 USD | 577.50 USD | 0.00 USD | `+74.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,200,000.00 USD | 2,710.00 USD | 0.00 USD | `+75.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,210,000.00 USD | 972.50 USD | 0.00 USD | `+76.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,210,000.00 USD | 7,680.00 USD | 0.00 USD | `+76.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,210,000.00 USD | 786.00 USD | 0.00 USD | `+77.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,220,000.00 USD | 1,690.00 USD | 0.00 USD | `+78.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,220,000.00 USD | 992.50 USD | 0.00 USD | `+79.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,220,000.00 USD | 997.50 USD | 0.00 USD | `+80.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,830,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+81.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,830,000.00 USD | 1,010.00 USD | 0.00 USD | `+82.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,840,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,840,000.00 USD | 1,030.00 USD | 0.00 USD | `+85.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,840,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,840,000.00 USD | 1,860.00 USD | 0.00 USD | `+87.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,840,000.00 USD | 1,410.00 USD | 0.00 USD | `+88.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,840,000.00 USD | 1,050.00 USD | 0.00 USD | `+89.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,850,000.00 USD | 4,000.00 USD | 0.00 USD | `+90.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,900,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,900,000.00 USD | 3,170.00 USD | 0.00 USD | `+94.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,900,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,900,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,900,000.00 USD | 1,090.00 USD | 0.00 USD | `+96.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,910,000.00 USD | 3,280.00 USD | 0.00 USD | `+97.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,910,000.00 USD | 2,110.00 USD | 0.00 USD | `+98.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,910,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,910,000.00 USD | 1,110.00 USD | 0.00 USD | `+100.43%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.69` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 5,240.00 USD | 0.00 USD | 18.90 USD |
| `7D` | `9.71` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD |
| `7D` | `9.73` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `9.75` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 0.00 USD | 33.95 USD | 16,970.00 USD |
| `1D` | `9.77` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 255.10 USD | 0.00 USD |
| `7D` | `9.77` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.79` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 15,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.81` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 0.00 USD | 261.00 USD | 0.00 USD |
| `1D` | `9.83` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 14,560.00 USD | 0.00 USD | 10,450.00 USD |
| `1D` | `9.85` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,820.00 USD | 175.40 USD | 0.00 USD |
| `1D` | `9.87` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 0.00 USD | 142.30 USD | 10,300.00 USD |
| `7D` | `9.89` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD |
| `1D` | `9.91` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD |
| `1D` | `9.93` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD |
| `7D` | `9.93` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.95` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 7,630.00 USD | 6,100.00 USD | 8,640.00 USD |
| `7D` | `9.95` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 14,920.00 USD | 22,040.00 USD | 13,780.00 USD |
| `1D` | `9.97` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 5,500.00 USD | 7,710.00 USD |
| `7D` | `9.97` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD |
| `1D` | `9.99` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 6,390.00 USD | 11,790.00 USD |
| `7D` | `9.99` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 25,690.00 USD |
| `1D` | `10.01` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 254.10 USD | 0.00 USD |
| `7D` | `10.01` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.03` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 115.90 USD | 0.00 USD |
| `1D` | `10.05` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD |
| `7D` | `10.05` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD |
| `7D` | `10.07` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD |
| `1D` | `10.09` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.09` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 2,120.00 USD | 7,510.00 USD | 0.00 USD |
| `7D` | `10.11` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 279.85 USD | 0.00 USD | 5,980.00 USD |
| `1D` | `10.13` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD |
| `7D` | `10.13` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD |
| `1D` | `10.15` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 5,870.00 USD | 104.05 USD | 21.54 USD |
| `7D` | `10.15` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD |
| `7D` | `10.17` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 56,890.00 USD | 3,240.00 USD | 21,610.00 USD |
| `1D` | `10.19` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 77.47 USD | 29.65 USD | 0.00 USD |
| `7D` | `10.19` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD |
| `1D` | `10.21` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 2,730.00 USD | 3,080.00 USD | 12,410.00 USD |
| `7D` | `10.21` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD |
| `1D` | `10.23` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 10,940.00 USD | 7,660.00 USD | 23,780.00 USD |
| `7D` | `10.23` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD |
| `1D` | `10.25` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 26,800.00 USD | 1,680.00 USD | 11,020.00 USD |
| `7D` | `10.25` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD |
| `1D` | `10.27` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 16,480.00 USD | 5,800.00 USD | 4,080.00 USD |
| `7D` | `10.27` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD |
| `1D` | `10.29` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 14,970.00 USD | 6,380.00 USD | 13,760.00 USD |
| `7D` | `10.29` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD |
| `1D` | `10.31` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 20,280.00 USD | 4,360.00 USD | 10,430.00 USD |
| `7D` | `10.31` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD |
| `1D` | `10.33` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 29,650.00 USD | 9,530.00 USD | 12,120.00 USD |
| `7D` | `10.33` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 58,810.00 USD | 28,270.00 USD | 25,780.00 USD |
| `1D` | `10.35` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 12,140.00 USD | 4,310.00 USD | 8,350.00 USD |
| `7D` | `10.35` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,890.00 USD |
| `1D` | `10.37` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 4,360.00 USD | 7,110.00 USD | 16,170.00 USD |
| `7D` | `10.37` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD |
| `1D` | `10.39` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 11,090.00 USD | 5,390.00 USD | 7,150.00 USD |
| `7D` | `10.39` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD |
| `1D` | `10.41` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 21,450.00 USD | 9,160.00 USD | 6,890.00 USD |
| `7D` | `10.41` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,950.00 USD |
| `1D` | `10.43` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 33,530.00 USD | 11,960.00 USD | 12,360.00 USD |
| `7D` | `10.43` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD |
| `1D` | `10.45` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 62,730.00 USD | 9,270.00 USD | 10,510.00 USD |
| `7D` | `10.45` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 38,090.00 USD | 11,060.00 USD | 42,160.00 USD |
| `1D` | `10.47` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 52,640.00 USD | 8,270.00 USD | 37,620.00 USD |
| `7D` | `10.47` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 56,700.00 USD | 22,760.00 USD | 6,560.00 USD |
| `1D` | `10.49` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 24,300.00 USD | 9,610.00 USD | 17,410.00 USD |
| `7D` | `10.49` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD |
| `1D` | `10.51` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 25,930.00 USD | 5,070.00 USD | 6,060.00 USD |
| `7D` | `10.51` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.53` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 19,290.00 USD | 5,270.00 USD | 29,830.00 USD |
| `7D` | `10.53` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD |
| `1D` | `10.55` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 7,160.00 USD | 2,730.00 USD | 1,820.00 USD |
| `7D` | `10.55` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 55,490.00 USD | 18,800.00 USD | 21,160.00 USD |
| `1D` | `10.57` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 51,950.00 USD | 36,690.00 USD | 8,190.00 USD |
| `7D` | `10.57` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD |
| `1D` | `10.59` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 48,910.00 USD | 22,350.00 USD | 26,480.00 USD |
| `7D` | `10.59` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 33,510.00 USD | 35,040.00 USD | 34,450.00 USD |
| `1D` | `10.61` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 37,630.00 USD | 10,090.00 USD | 37,830.00 USD |
| `7D` | `10.61` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 63,970.00 USD | 47,830.00 USD | 44,840.00 USD |
| `1D` | `10.63` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 36,490.00 USD | 32,820.00 USD | 43,190.00 USD |
| `7D` | `10.63` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 43,710.00 USD | 37,950.00 USD | 22,840.00 USD |
| `1D` | `10.65` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 51,920.00 USD | 21,890.00 USD | 40,810.00 USD |
| `7D` | `10.65` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 30,090.00 USD | 4,420.00 USD | 32,540.00 USD |
| `1D` | `10.67` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 81,930.00 USD | 2,270.00 USD | 11,910.00 USD |
| `7D` | `10.67` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 21,160.00 USD | 6,740.00 USD | 36,760.00 USD |
| `1D` | `10.69` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 91,100.00 USD | 22,270.00 USD | 63,310.00 USD |
| `7D` | `10.69` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 18,290.00 USD | 1,120.00 USD | 5,490.00 USD |
| `1D` | `10.71` | 942,410.00 USD | 0.00 USD | 942,410.00 USD | 25,820.00 USD | 1,570.00 USD | 3,730.00 USD |
| `7D` | `10.71` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 16,910.00 USD | 10,190.00 USD | 7,840.00 USD |
| `1D` | `10.73` | 911,300.00 USD | 0.00 USD | 911,300.00 USD | 10,180.00 USD | 4,590.00 USD | 22,700.00 USD |
| `7D` | `10.73` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD |
| `1D` | `10.75` | 873,830.00 USD | 0.00 USD | 873,830.00 USD | 41,860.00 USD | 4,650.00 USD | 54,300.00 USD |
| `7D` | `10.75` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 17,290.00 USD | 4,890.00 USD | 18,450.00 USD |
| `1D` | `10.77` | 773,030.00 USD | 0.00 USD | 773,030.00 USD | 4,380.00 USD | 4,090.00 USD | 2,690.00 USD |
| `7D` | `10.77` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 16,290.00 USD | 15,210.00 USD | 8,860.00 USD |
| `1D` | `10.79` | 761,870.00 USD | 0.00 USD | 761,870.00 USD | 87,840.00 USD | 85,640.00 USD | 103.08 USD |
| `7D` | `10.79` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 57,970.00 USD | 1,400.00 USD | 25,120.00 USD |
| `1D` | `10.81` | 588,280.00 USD | 0.00 USD | 588,280.00 USD | 94,550.00 USD | 39,180.00 USD | 46,740.00 USD |
| `7D` | `10.81` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 86,860.00 USD | 80,110.00 USD | 120,390.00 USD |
| `1D` | `10.83` | 407,810.00 USD | 0.00 USD | 407,810.00 USD | 81,450.00 USD | 14,380.00 USD | 69,350.00 USD |
| `7D` | `10.83` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 193,560.00 USD | 98,340.00 USD | 113,710.00 USD |
| `1D` | `10.85` | 242,640.00 USD | 0.00 USD | 242,640.00 USD | 24,030.00 USD | 60,060.00 USD | 64,740.00 USD |
| `7D` | `10.85` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 231,680.00 USD | 80,790.00 USD | 82,810.00 USD |
| `1D` | `10.87` | 93,800.00 USD | 0.00 USD | 93,800.00 USD | 0.00 USD | 34,650.00 USD | 59,150.00 USD |
| `7D` | `10.87` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 110,460.00 USD | 44,310.00 USD | 164,110.00 USD |
| `1D` | `10.89` | 0.39 USD | 0.00 USD | 0.39 USD | 0.00 USD | 0.00 USD | 0.39 USD |
| `7D` | `10.89` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 235,210.00 USD | 36,770.00 USD | 196,450.00 USD |
| `7D` | `10.91` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 274,660.00 USD | 1,590.00 USD | 0.00 USD |
| `1D` | `10.93` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.93` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 418,090.00 USD | 21,020.00 USD | 0.00 USD |
| `1D` | `10.95` | 7,410.00 USD | 7,410.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD | 0.00 USD |
| `7D` | `10.95` | 596,430.00 USD | 0.00 USD | 596,430.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.97` | 54,460.00 USD | 54,460.00 USD | 0.00 USD | 0.00 USD | 15,600.00 USD | 31,450.00 USD |
| `7D` | `10.97` | 288,830.00 USD | 0.00 USD | 288,830.00 USD | 165,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.99` | 57,340.00 USD | 57,340.00 USD | 0.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.99` | 123,250.00 USD | 0.00 USD | 123,250.00 USD | 44,540.00 USD | 22,500.00 USD | 36,260.00 USD |
| `1D` | `11.01` | 62,160.00 USD | 62,160.00 USD | 0.00 USD | 4,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.01` | 19,950.00 USD | 0.00 USD | 19,950.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.03` | 62,970.00 USD | 62,970.00 USD | 0.00 USD | 806.27 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.03` | 9,370.00 USD | 0.00 USD | 9,370.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.04` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.05` | 64,960.00 USD | 64,960.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.05` | 6,540.00 USD | 6,540.00 USD | 0.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.07` | 66,310.00 USD | 66,310.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.07` | 14,040.00 USD | 14,040.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.09` | 68,050.00 USD | 68,050.00 USD | 0.00 USD | 366.00 USD | 1,280.00 USD | 106.40 USD |
| `7D` | `11.09` | 18,180.00 USD | 18,180.00 USD | 0.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.11` | 145,230.00 USD | 145,230.00 USD | 0.00 USD | 77,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.11` | 23,970.00 USD | 23,970.00 USD | 0.00 USD | 5,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.13` | 282,660.00 USD | 282,660.00 USD | 0.00 USD | 72,780.00 USD | 12,410.00 USD | 52,240.00 USD |
| `7D` | `11.13` | 30,790.00 USD | 30,790.00 USD | 0.00 USD | 6,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.15` | 33,200.00 USD | 33,200.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.17` | 334,290.00 USD | 334,290.00 USD | 0.00 USD | 0.00 USD | 51,630.00 USD | 0.00 USD |
| `7D` | `11.17` | 37,170.00 USD | 37,170.00 USD | 0.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.19` | 419,620.00 USD | 419,620.00 USD | 0.00 USD | 21,840.00 USD | 63,490.00 USD | 0.00 USD |
| `1D` | `11.21` | 605,830.00 USD | 605,830.00 USD | 0.00 USD | 109,000.00 USD | 425.43 USD | 76,790.00 USD |
| `7D` | `11.21` | 348,330.00 USD | 348,330.00 USD | 0.00 USD | 311,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.23` | 856,780.00 USD | 856,780.00 USD | 0.00 USD | 191,590.00 USD | 851.54 USD | 58,500.00 USD |
| `7D` | `11.23` | 548,900.00 USD | 548,900.00 USD | 0.00 USD | 200,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.25` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 90,500.00 USD | 39,180.00 USD | 114,980.00 USD |
| `7D` | `11.25` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 330,300.00 USD | 0.00 USD | 129,430.00 USD |
| `1D` | `11.27` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 66,780.00 USD | 616.75 USD | 142,840.00 USD |
| `7D` | `11.27` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 256,120.00 USD | 0.00 USD | 191,320.00 USD |
| `1D` | `11.29` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 25,480.00 USD | 98,920.00 USD | 153,990.00 USD |
| `7D` | `11.29` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 104,970.00 USD | 56,970.00 USD | 55,980.00 USD |
| `1D` | `11.31` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 63,620.00 USD | 67,210.00 USD | 79,800.00 USD |
| `7D` | `11.31` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 28,170.00 USD | 44,160.00 USD | 236,970.00 USD |
| `1D` | `11.33` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 141,050.00 USD | 29,530.00 USD | 23,800.00 USD |
| `7D` | `11.33` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 54,410.00 USD | 8,920.00 USD | 81,870.00 USD |
| `1D` | `11.35` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 131,530.00 USD | 89,860.00 USD | 26,120.00 USD |
| `7D` | `11.35` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 60,280.00 USD | 0.00 USD |
| `1D` | `11.37` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 51,260.00 USD | 73,030.00 USD | 22,140.00 USD |
| `7D` | `11.37` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 71,610.00 USD | 99,100.00 USD |
| `1D` | `11.39` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 38,270.00 USD | 0.00 USD |
| `7D` | `11.39` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 67,010.00 USD | 34,560.00 USD | 140,440.00 USD |
| `7D` | `11.41` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD |
| `1D` | `11.43` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 50,600.00 USD | 26,360.00 USD | 88,270.00 USD |
| `7D` | `11.43` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 133,220.00 USD | 51,980.00 USD | 91,960.00 USD |
| `1D` | `11.45` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 42,610.00 USD | 69,710.00 USD | 0.00 USD |
| `7D` | `11.45` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD |
| `1D` | `11.47` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 45,250.00 USD | 19,590.00 USD | 23,360.00 USD |
| `7D` | `11.47` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.49` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 37,020.00 USD | 22,330.00 USD | 34,640.00 USD |
| `7D` | `11.49` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.51` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 41,360.00 USD | 28,330.00 USD | 30,920.00 USD |
| `7D` | `11.51` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 40,840.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `11.53` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 31,460.00 USD | 16,860.00 USD | 29,470.00 USD |
| `7D` | `11.53` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD |
| `1D` | `11.55` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 21,770.00 USD | 802.50 USD | 11,900.00 USD |
| `7D` | `11.55` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,460.00 USD |
| `1D` | `11.57` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 87,810.00 USD | 0.00 USD | 23,850.00 USD |
| `7D` | `11.57` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,620.00 USD |
| `1D` | `11.59` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 11,470.00 USD | 7,660.00 USD | 39,570.00 USD |
| `7D` | `11.59` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD |
| `1D` | `11.61` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 151,970.00 USD | 0.00 USD | 71,330.00 USD |
| `7D` | `11.61` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.63` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD |
| `7D` | `11.63` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.65` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD |
| `1D` | `11.67` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.67` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD |
| `1D` | `11.69` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 59,600.00 USD | 28,810.00 USD | 313.96 USD |
| `7D` | `11.69` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.71` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD |
| `7D` | `11.71` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 98,180.00 USD | 839.72 USD | 41,790.00 USD |
| `7D` | `11.73` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD |
| `1D` | `11.75` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 23,350.00 USD | 31,660.00 USD | 61,350.00 USD |
| `7D` | `11.75` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.77` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 44,660.00 USD | 18,670.00 USD | 177.93 USD |
| `7D` | `11.77` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.79` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 4,240.00 USD | 755.20 USD | 40,080.00 USD |
| `7D` | `11.79` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.81` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 13,940.00 USD | 327.53 USD |
| `7D` | `11.81` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.83` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 8,620.00 USD | 11,510.00 USD | 18,420.00 USD |
| `7D` | `11.83` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.85` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 77,060.00 USD | 22,590.00 USD | 82,330.00 USD |
| `7D` | `11.85` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD |
| `1D` | `11.87` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 19,640.00 USD | 26,360.00 USD | 37,840.00 USD |
| `7D` | `11.87` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.89` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 44,180.00 USD | 11,410.00 USD | 14,520.00 USD |
| `7D` | `11.89` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 40,020.00 USD | 16,380.00 USD | 71.80 USD |
| `1D` | `11.91` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 62,930.00 USD | 18,340.00 USD | 18,550.00 USD |
| `7D` | `11.91` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | 397.61 USD |
| `1D` | `11.93` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 79,610.00 USD | 27,850.00 USD | 28,590.00 USD |
| `7D` | `11.93` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.95` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 32,490.00 USD | 14,110.00 USD | 21,750.00 USD |
| `7D` | `11.95` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.97` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 76,180.00 USD | 36,220.00 USD | 97,310.00 USD |
| `7D` | `11.97` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 358,410.00 USD | 35,140.00 USD | 223,430.00 USD |
| `1D` | `11.99` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 50,080.00 USD | 7,710.00 USD | 37,170.00 USD |
| `7D` | `11.99` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 221,400.00 USD | 17,110.00 USD | 130,130.00 USD |
| `1D` | `12.01` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 36,170.00 USD | 9,410.00 USD | 52,750.00 USD |
| `7D` | `12.01` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 164,140.00 USD | 5,360.00 USD | 247,680.00 USD |
| `1D` | `12.03` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 90,560.00 USD | 43,220.00 USD | 36,690.00 USD |
| `7D` | `12.03` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD |
| `1D` | `12.05` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 234,880.00 USD | 68,220.00 USD | 113,670.00 USD |
| `7D` | `12.05` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.07` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 146,960.00 USD | 58,310.00 USD | 113,770.00 USD |
| `7D` | `12.07` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.09` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 21,070.00 USD | 20,350.00 USD | 17,590.00 USD |
| `7D` | `12.09` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD |
| `1D` | `12.11` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 95,070.00 USD | 34,950.00 USD | 55,330.00 USD |
| `7D` | `12.11` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD |
| `1D` | `12.13` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 93,770.00 USD | 33,860.00 USD | 39,740.00 USD |
| `7D` | `12.13` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD |
| `1D` | `12.15` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 113,450.00 USD | 42,360.00 USD | 65,390.00 USD |
| `7D` | `12.15` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD |
| `1D` | `12.17` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 125,480.00 USD | 64,130.00 USD | 69,710.00 USD |
| `7D` | `12.17` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 26,820.00 USD | 72,790.00 USD | 53,310.00 USD |
| `1D` | `12.19` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 61,950.00 USD | 24,200.00 USD | 12,250.00 USD |
| `7D` | `12.19` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD |
| `1D` | `12.21` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 54,170.00 USD | 28,750.00 USD | 50,920.00 USD |
| `7D` | `12.21` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD |
| `1D` | `12.23` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 14,660.00 USD | 24,000.00 USD | 4,690.00 USD |
| `7D` | `12.23` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD |
| `1D` | `12.25` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 4,820.00 USD | 5,430.00 USD | 7,630.00 USD |
| `7D` | `12.25` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD |
| `1D` | `12.27` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 66,620.00 USD | 12,330.00 USD | 31,140.00 USD |
| `7D` | `12.27` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.29` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 39,130.00 USD | 24,690.00 USD | 41,350.00 USD |
| `7D` | `12.29` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD |
| `1D` | `12.31` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 42,360.00 USD | 5,800.00 USD | 14,650.00 USD |
| `7D` | `12.31` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD |
| `1D` | `12.33` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 2,240.00 USD | 3,680.00 USD | 3,290.00 USD |
| `7D` | `12.33` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD |
| `1D` | `12.35` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 18,300.00 USD | 12,610.00 USD | 5,540.00 USD |
| `7D` | `12.35` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD |
| `1D` | `12.37` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 11,580.00 USD | 5,700.00 USD | 3,160.00 USD |
| `7D` | `12.37` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD |
| `1D` | `12.39` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 26,010.00 USD | 12,560.00 USD | 21,550.00 USD |
| `7D` | `12.39` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 160,660.00 USD | 42,040.00 USD | 338,190.00 USD |
| `1D` | `12.41` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 43,450.00 USD | 19,990.00 USD | 23,480.00 USD |
| `7D` | `12.41` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD |
| `1D` | `12.43` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 22,880.00 USD | 5,940.00 USD | 196.48 USD |
| `7D` | `12.43` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD |
| `1D` | `12.45` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 10,770.00 USD | 4,330.00 USD | 6,410.00 USD |
| `7D` | `12.45` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD |
| `1D` | `12.47` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 1,480.00 USD | 12,000.00 USD | 12,410.00 USD |
| `7D` | `12.47` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD |
| `1D` | `12.49` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 595.12 USD | 63.95 USD | 1,500.00 USD |
| `7D` | `12.49` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD |
| `1D` | `12.51` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 12,520.00 USD | 7,590.00 USD | 22,150.00 USD |
| `7D` | `12.51` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD |
| `1D` | `12.53` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 26,930.00 USD | 1,680.00 USD | 11,020.00 USD |
| `7D` | `12.53` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD |
| `1D` | `12.55` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 16,600.00 USD | 5,800.00 USD | 4,080.00 USD |
| `7D` | `12.55` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD |
| `1D` | `12.57` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 16,380.00 USD | 6,380.00 USD | 13,680.00 USD |
| `7D` | `12.57` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD |
| `1D` | `12.59` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 5,250.00 USD | 1,010.00 USD | 3,190.00 USD |
| `7D` | `12.59` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD |
| `1D` | `12.61` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 17,680.00 USD | 3,350.00 USD | 7,170.00 USD |
| `7D` | `12.61` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD |
| `1D` | `12.63` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 29,650.00 USD | 9,530.00 USD | 11,720.00 USD |
| `7D` | `12.63` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 64,120.00 USD | 28,270.00 USD | 81,370.00 USD |
| `1D` | `12.65` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 12,140.00 USD | 4,310.00 USD | 8,350.00 USD |
| `7D` | `12.65` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 76,240.00 USD | 26,110.00 USD | 90,700.00 USD |
| `1D` | `12.67` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 5,450.00 USD | 7,110.00 USD | 16,170.00 USD |
| `7D` | `12.67` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD |
| `1D` | `12.69` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 7,450.00 USD | 5,390.00 USD | 7,260.00 USD |
| `7D` | `12.69` | 16,880,000.00 USD | 16,880,000.00 USD | 0.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD |
| `1D` | `12.71` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 523.46 USD | 31.80 USD | 6,470.00 USD |
| `7D` | `12.71` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD |
| `1D` | `12.73` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 21,450.00 USD | 9,120.00 USD | 1.63 USD |
| `7D` | `12.73` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD |
| `1D` | `12.75` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 33,530.00 USD | 11,330.00 USD | 12,300.00 USD |
| `7D` | `12.75` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD |
| `1D` | `12.77` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 22,310.00 USD | 9,270.00 USD | 10,500.00 USD |
| `7D` | `12.77` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD |
| `1D` | `12.79` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 9,880.00 USD | 2,050.00 USD | 11,260.00 USD |
| `7D` | `12.79` | 17,310,000.00 USD | 17,310,000.00 USD | 0.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD |
| `1D` | `12.80` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 7,290.00 USD | 3,590.00 USD | 7,570.00 USD |
| `7D` | `12.81` | 17,340,000.00 USD | 17,340,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD |
| `7D` | `12.83` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD |
| `7D` | `12.85` | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD |
| `7D` | `12.87` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD |
| `7D` | `12.89` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD |
| `7D` | `12.91` | 17,670,000.00 USD | 17,670,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD |
| `7D` | `12.93` | 17,700,000.00 USD | 17,700,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD |
| `7D` | `12.95` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD |
| `7D` | `12.97` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 13,890.00 USD | 10,560.00 USD | 10,050.00 USD |
| `7D` | `12.99` | 17,820,000.00 USD | 17,820,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD |
| `7D` | `13.01` | 17,820,000.00 USD | 17,820,000.00 USD | 0.00 USD | 1,290.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `13.03` | 17,830,000.00 USD | 17,830,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `7D` | `13.05` | 17,830,000.00 USD | 17,830,000.00 USD | 0.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD |
| `7D` | `13.07` | 17,840,000.00 USD | 17,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `13.09` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `13.11` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD |
| `7D` | `13.13` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.17` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD |
| `7D` | `13.19` | 17,900,000.00 USD | 17,900,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `13.21` | 17,920,000.00 USD | 17,920,000.00 USD | 0.00 USD | 13,890.00 USD | 213.60 USD | 8,930.00 USD |
| `7D` | `13.23` | 17,930,000.00 USD | 17,930,000.00 USD | 0.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD |
| `7D` | `13.25` | 18,000,000.00 USD | 18,000,000.00 USD | 0.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD |
| `7D` | `13.27` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 10,290.00 USD | 14,120.00 USD | 10,920.00 USD |
| `7D` | `13.29` | 18,040,000.00 USD | 18,040,000.00 USD | 0.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD |
| `7D` | `13.31` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 12,560.00 USD | 6,580.00 USD | 6,470.00 USD |
| `7D` | `13.33` | 18,080,000.00 USD | 18,080,000.00 USD | 0.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `517.38M` | Total OI Tokens: `47,586,226.4 LINK`
  * 1h OI Change: `-1.54%` | 4h OI Change: `-7.68%` | 24h OI Change: `-9.82%`
  * Exchange Breakdown: Binance=`98.19M` | Bybit=`61.39M` | OKX=`25.71M` | Hyperliquid=`49.51M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.17K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0061%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0020%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0054%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `49.87%` | `50.13%` | `0.99` | 134,420,000.00 USD |
| `15M` | `Binance` | `50.46%` | `49.54%` | `1.02` | 51,680,000.00 USD |
| `15M` | `OKX` | `49.85%` | `50.15%` | `0.99` | 15,190,000.00 USD |
| `15M` | `Bybit` | `51.11%` | `48.89%` | `1.05` | 33,850,000.00 USD |
| `15M` | `KuCoin` | `58.56%` | `41.44%` | `1.41` | 708,550.00 USD |
| `15M` | `Gate` | `45.25%` | `54.75%` | `0.83` | 4,270,000.00 USD |
| `15M` | `Bitget` | `53.39%` | `46.61%` | `1.15` | 3,540,000.00 USD |
| `15M` | `BingX` | `48.38%` | `51.62%` | `0.94` | 1,150,000.00 USD |
| `15M` | `MEXC` | `43.84%` | `56.16%` | `0.78` | 2,190,000.00 USD |
| `15M` | `Bitunix` | `55.88%` | `44.12%` | `1.27` | 1,820,000.00 USD |
| `15M` | `Hyperliquid` | `54.03%` | `45.97%` | `1.18` | 9,350,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.43%` | `49.57%` | `1.02` | 1,710,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `22.82%` | `77.18%` | `0.30` | 6,020,000.00 USD |
| `15M` | `HTX` | `82.15%` | `17.85%` | `4.60` | 368,660.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `57.36%` | `42.64%` | `1.35` | 723,410.00 USD |
| `15M` | `Aster` | `72.33%` | `27.67%` | `2.61` | 1,300,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `66.61%` | `33.39%` | `1.99` | 559,030.00 USD |
| `15M` | `Whale Positions` | `50.46%` | `49.54%` | `1.02` | 51,680,000.00 USD |
| `15M` | `Global Accounts` | `49.87%` | `50.13%` | `0.99` | 134,420,000.00 USD |
| `1H` | `LINK` | `50.52%` | `49.48%` | `1.02` | 283,370,000.00 USD |
| `1H` | `Binance` | `51.69%` | `48.31%` | `1.07` | 110,120,000.00 USD |
| `1H` | `OKX` | `51.76%` | `48.24%` | `1.07` | 30,430,000.00 USD |
| `1H` | `Bybit` | `51.64%` | `48.36%` | `1.07` | 61,340,000.00 USD |
| `1H` | `KuCoin` | `61.06%` | `38.94%` | `1.57` | 1,460,000.00 USD |
| `1H` | `Gate` | `43.95%` | `56.05%` | `0.78` | 12,350,000.00 USD |
| `1H` | `Bitget` | `54.83%` | `45.17%` | `1.21` | 8,370,000.00 USD |
| `1H` | `BingX` | `43.59%` | `56.41%` | `0.77` | 4,380,000.00 USD |
| `1H` | `MEXC` | `41.14%` | `58.86%` | `0.70` | 4,420,000.00 USD |
| `1H` | `Bitunix` | `58.9%` | `41.1%` | `1.43` | 4,670,000.00 USD |
| `1H` | `Hyperliquid` | `54.36%` | `45.64%` | `1.19` | 15,680,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.38%` | `44.62%` | `1.24` | 6,430,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `32.58%` | `67.42%` | `0.48` | 18,730,000.00 USD |
| `1H` | `HTX` | `60.45%` | `39.55%` | `1.53` | 953,250.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `66.62%` | `33.38%` | `2.00` | 1,710,000.00 USD |
| `1H` | `Aster` | `67.92%` | `32.08%` | `2.12` | 1,460,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `61.51%` | `38.49%` | `1.60` | 869,530.00 USD |
| `1H` | `Whale Positions` | `51.69%` | `48.31%` | `1.07` | 110,120,000.00 USD |
| `1H` | `Global Accounts` | `50.52%` | `49.48%` | `1.02` | 283,370,000.00 USD |
| `4H` | `LINK` | `50.01%` | `49.99%` | `1.00` | 355,740,000.00 USD |
| `4H` | `Binance` | `50.93%` | `49.07%` | `1.04` | 139,400,000.00 USD |
| `4H` | `OKX` | `51.11%` | `48.89%` | `1.05` | 37,350,000.00 USD |
| `4H` | `Bybit` | `51.94%` | `48.06%` | `1.08` | 74,080,000.00 USD |
| `4H` | `KuCoin` | `57.99%` | `42.01%` | `1.38` | 1,900,000.00 USD |
| `4H` | `Gate` | `44.68%` | `55.32%` | `0.81` | 15,330,000.00 USD |
| `4H` | `Bitget` | `54.62%` | `45.38%` | `1.20` | 10,000,000.00 USD |
| `4H` | `BingX` | `34.99%` | `65.01%` | `0.54` | 6,840,000.00 USD |
| `4H` | `MEXC` | `42.17%` | `57.83%` | `0.73` | 5,120,000.00 USD |
| `4H` | `Bitunix` | `56.91%` | `43.09%` | `1.32` | 5,640,000.00 USD |
| `4H` | `Hyperliquid` | `56.43%` | `43.57%` | `1.30` | 21,410,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.05%` | `46.95%` | `1.13` | 9,950,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `30.44%` | `69.56%` | `0.44` | 22,580,000.00 USD |
| `4H` | `HTX` | `59.57%` | `40.43%` | `1.47` | 1,210,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `66.9%` | `33.1%` | `2.02` | 2,200,000.00 USD |
| `4H` | `Aster` | `67.25%` | `32.75%` | `2.05` | 1,700,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `58.79%` | `41.21%` | `1.43` | 1,030,000.00 USD |
| `4H` | `Whale Positions` | `50.93%` | `49.07%` | `1.04` | 139,400,000.00 USD |
| `4H` | `Global Accounts` | `50.01%` | `49.99%` | `1.00` | 355,740,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.70` | `11.70` | `11.70` | `11.72` | `11.68` | 638,959.31 USD | 356,011.33 USD | 282,947.98 USD | 73,063.35 USD | `+11.43%` | `5B / 5S` |
| `0:00 UTC` | `11.53` | `11.52` | `11.53` | `11.69` | `11.42` | 7,042,914.29 USD | 3,385,099.97 USD | 3,657,814.32 USD | -272,714.35 USD | `-3.87%` | `7B / 36S` |
| `5:00 UTC` | `11.53` | `11.53` | `11.53` | `11.57` | `11.50` | 1,919,098.80 USD | 908,695.92 USD | 1,010,402.88 USD | -101,706.95 USD | `-5.30%` | `5B / 9S` |
| `0:00 UTC` | `11.13` | `11.25` | `11.13` | `11.55` | `11.03` | 15,867,227.37 USD | 6,488,166.63 USD | 9,379,060.74 USD | -2,890,894.11 USD | `-18.22%` | `4B / 29S` |
| `5:00 UTC` | `11.00` | `11.03` | `11.00` | `11.19` | `10.87` | 17,839,722.17 USD | 8,415,517.99 USD | 9,424,204.18 USD | -1,008,686.19 USD | `-5.65%` | `9B / 18S` |
| `0:00 UTC` | `11.11` | `11.06` | `11.11` | `11.18` | `10.95` | 10,677,747.31 USD | 5,105,845.59 USD | 5,571,901.72 USD | -466,056.13 USD | `-4.36%` | `1B / 2S` |
| `5:00 UTC` | `11.18` | `11.21` | `11.18` | `11.30` | `11.14` | 5,823,506.96 USD | 2,554,704.96 USD | 3,268,802.01 USD | -714,097.05 USD | `-12.26%` | `10B / 21S` |
| `0:00 UTC` | `11.23` | `11.21` | `11.23` | `11.27` | `11.10` | 3,064,696.05 USD | 1,263,662.15 USD | 1,801,033.90 USD | -537,371.74 USD | `-17.53%` | `20B / 42S` |
| `5:00 UTC` | `11.10` | `11.09` | `11.10` | `11.13` | `11.03` | 2,476,363.14 USD | 1,173,647.56 USD | 1,302,715.59 USD | -129,068.03 USD | `-5.21%` | `19B / 14S` |
| `0:00 UTC` | `11.03` | `11.03` | `11.03` | `11.06` | `11.01` | 981,912.58 USD | 442,806.68 USD | 539,105.90 USD | -96,299.22 USD | `-9.81%` | `7B / 15S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:46` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.58` | 0.00 USD | 0.00 USD |
| `10-28 20:46` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 59,000.00 USD | 0.00 USD |
| `10-28 20:39` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 49,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.47` | 46,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.67` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.75` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 08:00` | `Volume 250K LINK` | `Divergence` | **`BULLISH`** | Drop without taker selling | `11.65` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 250K LINK` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `11.78` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 25,280.00 USD | -661,440.00 USD | **`DISTRIBUTION`** |
| `15m` | 36,010.00 USD | -89,180.00 USD | **`DISTRIBUTION`** |
| `30m` | -279,070.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,600,000.00 USD | -3,110,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -5,380,000.00 USD | -8,780,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,720,000.00 USD | -10,690,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -6,290,000.00 USD | -13,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,220,000.00 USD | -11,490,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,270,000.00 USD | -11,020,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -5,790,000.00 USD | -16,180,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -14,320,000.00 USD | -34,090,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -74,860,000.00 USD | -196,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+25.28K` | 15m=`+36.01K` | 1h=`-1.60M` | 24h=`-5.79M`
* Futures Capital Netflows: 5m=`-661.44K` | 15m=`-89.18K` | 1h=`-3.11M` | 24h=`-16.18M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.91` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `9.58` (Risk Distance: `1.34` pts)
  * +2.5R Take Profit: `14.26`
  * Mathematical Lot Sizing: **`7.48 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.13` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.47` (Risk Distance: `1.34` pts)
  * +2.5R Take Profit: `7.79`
  * Mathematical Lot Sizing: **`7.48 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.04`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
