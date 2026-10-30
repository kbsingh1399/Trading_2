# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:20:35 IST` (`2026-10-30 08:50:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.43` | **Live Ask Quote**: `8.47` | **Mid Price**: `8.45`
- **Spread Points**: `4.00` | **Spread BPS**: `47.34 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.32` | VWAP Z-Score: `+0.77` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0661` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.04` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.87` | Lower -3.00σ Band: `7.77`
  * Upper +2.51σ Band: `8.78` | Lower -2.51σ Band: `7.86`
  * Upper +2.01σ Band: `8.69` | Lower -2.01σ Band: `7.95`
  * Upper +2.00σ Band: `8.69` | Lower -2.00σ Band: `7.95`
  * Upper +1.28σ Band: `8.55` | Lower -1.28σ Band: `8.08`
  * Upper +1.00σ Band: `8.50` | Lower -1.00σ Band: `8.14`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.50` | EMA-20=`8.49` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.49` (Slope: `+0.0000`) | EMA-100=`8.56`
  * Institutional Anchors: EMA-144=`8.61` | EMA-200=`8.66` (Slope: `-0.1849`) | EMA-233=`8.69`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.53` (Distance: `-0.83%`)
  * Point of Control (POC) = `8.32` (Distance: `+1.61%`)
  * Value Area Low (VAL) = `8.17` (Distance: `+3.50%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.70`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.50` | Low=`8.40`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.42` - `8.48`
  * Optimal Trade Entry (OTE 0.705): `8.47`
  * Structural Invalidation Anchor (0.786): `8.52`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.48` | `8.49` | `8.47` | `8.47` | `23,259` | 197,223.27 USD | -43,641.36 USD | `-22.13%` | -5,617,635.95 USD | `+0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.47` | `8.49` | `8.46` | `8.48` | `26,743` | 226,575.35 USD | -24,399.72 USD | `-10.77%` | -5,642,035.67 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `8.48` | `8.48` | `8.46` | `8.46` | `4,307` | 36,471.10 USD | -13,375.82 USD | `-36.68%` | -5,655,411.49 USD | `+0.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.50` | `8.52` | `8.45` | `8.51` | `215,807` | 1,829,814.14 USD | -91,477.76 USD | `-5.00%` | -5,593,279.36 USD | `-0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.51` | `8.52` | `8.48` | `8.48` | `88,475` | 752,301.06 USD | 19,284.76 USD | `+2.56%` | -5,573,994.60 USD | `+0.02` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `8.48` | `8.49` | `8.46` | `8.46` | `54,395` | 460,997.45 USD | -82,127.70 USD | `-17.82%` | -5,656,122.29 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.55` | `8.68` | `8.54` | `8.63` | `644,719` | 5,556,353.09 USD | 1,642,499.12 USD | `+29.56%` | -4,149,799.31 USD | `+1.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.63` | `8.63` | `8.48` | `8.50` | `671,897` | 5,750,861.25 USD | -1,429,699.87 USD | `-24.86%` | -5,579,499.18 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.50` | `8.52` | `8.45` | `8.46` | `358,676` | 3,043,104.19 USD | -154,312.24 USD | `-5.07%` | -5,733,811.42 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.45` | `8.46` | `358,677` | 3,043,112.65 USD | -154,320.70 USD | `-5.07%` | -5,559,160.70 USD | `+0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.45` | `8.46` | `358,677` | 3,043,112.65 USD | -154,320.70 USD | `-5.07%` | -5,559,160.70 USD | `+0.52` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`8.45`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.46` | `140.6200` | 1,190.33 USD | 1,190.33 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.46` | `99.6100` | 843.16 USD | 2,033.49 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.46` | `99.5800` | 842.89 USD | 2,876.39 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.46` | `99.6200` | 843.20 USD | 3,719.59 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.46` | `60.3400` | 510.72 USD | 4,230.31 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.46` | `103.0300` | 871.99 USD | 5,102.30 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.46` | `99.6100` | 843.02 USD | 5,945.32 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.46` | `99.6200` | 843.06 USD | 6,788.39 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.46` | `105.1500` | 889.79 USD | 7,678.18 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.46` | `99.6200` | 842.92 USD | 8,521.10 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.46` | `18.2000` | 153.99 USD | 8,675.10 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.46` | `18.2200` | 154.16 USD | 8,829.25 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.46` | `99.6200` | 842.85 USD | 9,672.11 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.46` | `343.2300` | 2,903.90 USD | 12,576.01 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `8.46` | `60.3400` | 510.49 USD | 13,086.50 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.46` | `709.1900` | 5,999.68 USD | 19,086.18 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.46` | `24.0600` | 203.54 USD | 19,289.72 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.46` | `99.6100` | 842.67 USD | 20,132.39 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.46` | `99.6200` | 842.72 USD | 20,975.11 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.46` | `1652.6700` | 13,979.94 USD | 34,955.04 USD | `1 orders` | `-0.08%` | `-` |
| `ASK` | `8.47` | `120.0800` | 1,017.16 USD | 59,384.58 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.47` | `99.5900` | 843.59 USD | 58,367.42 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.47` | `91.7000` | 776.74 USD | 57,523.83 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.47` | `1180.6600` | 10,000.66 USD | 56,747.09 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.47` | `27.0900` | 229.45 USD | 46,746.43 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.47` | `1652.6700` | 13,997.78 USD | 46,516.98 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.47` | `99.6100` | 843.67 USD | 32,519.19 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.47` | `91.7000` | 776.65 USD | 31,675.53 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.47` | `88.8300` | 752.33 USD | 30,898.87 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.47` | `200.0000` | 1,693.80 USD | 30,146.55 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.47` | `35.8400` | 303.53 USD | 28,452.75 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.47` | `427.4200` | 3,619.73 USD | 28,149.22 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.47` | `590.4000` | 4,999.92 USD | 24,529.49 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.47` | `56.6000` | 479.32 USD | 19,529.57 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.47` | `99.6100` | 843.53 USD | 19,050.24 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.47` | `200.0000` | 1,693.62 USD | 18,206.72 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.47` | `23.6900` | 200.61 USD | 16,513.10 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.47` | `99.6100` | 843.48 USD | 16,312.49 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.47` | `24.1600` | 204.57 USD | 15,469.01 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.47` | `1802.7300` | 15,264.44 USD | 15,264.44 USD | `3 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.47` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.47` | `0.00%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1490` | `0x7737...bf66` | `SHORT` | 1,454,056.47 USD | `171,568.06` | `7.43` | `8.47` | `111.31` | -178,511.45 USD | `-12.28%` | `10X Cross` |
| `1593` | `0xeadc...9d55` | `LONG` | 1,355,333.44 USD | `160,070.56` | `8.11` | `8.47` | `0.000000` | 57,695.86 USD | `+4.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.63` | 7,999.74 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 8.00K USD at 8.6326 USD [API] | `2026-10-29 08:06:42` |
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
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.60%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.76%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.54%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.78%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.54%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.78%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 462,400.00 USD, Dist: `+9.76%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.81%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.72` | 120.05 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 2,260.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 677.11 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 214.48 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 215.53 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 1,460.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 243.23 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 246.68 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 111.10 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 361.94 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 9,810.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 143.26 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 322.58 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 20,310.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 100.03 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 24,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,240.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 557.73 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 7,570.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 1,530.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.96` | 2,630.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.17` | 388.68 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.42 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 486.93 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 2,930.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.63` | 295.48 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.84` | 532.95 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 209.97 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 506.72 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 2,830.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 167.78 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 314.59 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.07` | 739.39 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 223.43 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 1,040.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 5,800.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.16` | 209.34 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 300.91 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 503.78 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.28` | 160,550.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,160.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.51` | 1,860.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,530.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.62` | 2,810.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.67` | 1,330.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.71` | 147.33 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.92` | 277.35 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 571.86 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 405.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,130.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.26` | 2,420.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 1,430.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,120.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 359,930.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 792,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 791,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 785,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.47` | 1,520.00 USD | 784,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 782,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 781,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,500.00 USD | 772,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.58` | 1,770.00 USD | 771,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 1,100.00 USD | 769,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 3,640.00 USD | 768,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 764,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 764,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 764,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 762,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 16,570.00 USD | 759,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 743,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 736,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 735,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 21,580.00 USD | 727,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,540.00 USD | 705,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 700,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 698,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 288.56 USD | 691,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 691,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 688,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 686,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 685,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 682,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 682,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 674,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 674,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 545,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 544,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 523,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 522,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 498,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 491,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 490,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 488,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 459,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 2,500.00 USD | 459,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 456,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.14` | 6,160,000.00 USD | 6,160,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 456,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.16` | 6,050,000.00 USD | 6,050,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 435,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.18` | 5,990,000.00 USD | 5,990,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 433,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.20` | 5,960,000.00 USD | 5,960,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 28,820.00 USD | 432,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 403,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.22` | 5,940,000.00 USD | 5,940,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 3,590.00 USD | 402,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.24` | 5,920,000.00 USD | 5,920,000.00 USD | 39,910.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 399,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 399,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.26` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 1,810.00 USD | 58.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.26` | 1,450.00 USD | 377,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.28` | 5,860,000.00 USD | 5,860,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 376,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 340,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.30` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.32` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.34` | 552.42 USD | 338,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 3,820.00 USD | 337,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 5,850,000.00 USD | 5,850,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 16,100.00 USD | 333,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 2,130.00 USD | 317,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 5,840,000.00 USD | 5,840,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,080.00 USD | 315,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 5,800,000.00 USD | 5,800,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 314,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 314,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 312,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 309,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 299,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 294,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 293,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 292,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 292,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.52` | 5,710,000.00 USD | 5,710,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 290,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 288,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 5,670,000.00 USD | 5,670,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,510.00 USD | 284,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 5,630,000.00 USD | 5,630,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 283,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 258,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.59` | 4,990,000.00 USD | 4,990,000.00 USD | 1,740.00 USD | 0.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 1,630.00 USD | 257,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 4,980,000.00 USD | 4,980,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.60` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 4,970,000.00 USD | 4,970,000.00 USD | 1,190.00 USD | 761.26 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 256,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 4,960,000.00 USD | 4,960,000.00 USD | 956.60 USD | 0.00 USD | 133.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 2,130.00 USD | 996.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 255,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 4,960,000.00 USD | 4,960,000.00 USD | 1,040.00 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 254,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 4,950,000.00 USD | 4,950,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 5,610,000.00 USD | 5,610,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 817.75 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 254,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 4,900,000.00 USD | 4,900,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 5,560,000.00 USD | 5,560,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 254,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 4,900,000.00 USD | 4,900,000.00 USD | 1,140.00 USD | 587.20 USD | 114.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 254,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 4,900,000.00 USD | 4,900,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.68` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 249,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 248,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 4,890,000.00 USD | 4,890,000.00 USD | 4,140.00 USD | 2,390.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.70` | 5,520,000.00 USD | 5,520,000.00 USD | 393.33 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 4,870,000.00 USD | 4,870,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 4,860,000.00 USD | 4,860,000.00 USD | 701.68 USD | 568.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 5,520,000.00 USD | 5,520,000.00 USD | 38,970.00 USD | 0.00 USD | 40,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 4,850,000.00 USD | 4,850,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 4,840,000.00 USD | 4,840,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 5,440,000.00 USD | 5,440,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 4,820,000.00 USD | 4,820,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 242,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 4,810,000.00 USD | 4,810,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 5,410,000.00 USD | 5,410,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 241,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 4,810,000.00 USD | 4,810,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 8,670.00 USD | 241,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 4,790,000.00 USD | 4,790,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 5,390,000.00 USD | 5,390,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,380.00 USD | 232,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,780,000.00 USD | 4,780,000.00 USD | 18,980.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 231,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 4,750,000.00 USD | 4,750,000.00 USD | 9,300.00 USD | 8,720.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 5,300,000.00 USD | 5,300,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 226,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,730,000.00 USD | 4,730,000.00 USD | 349.70 USD | 728.43 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 4,730,000.00 USD | 4,730,000.00 USD | 2,250.00 USD | 2,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 5,240,000.00 USD | 5,240,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 220,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,730,000.00 USD | 4,730,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 4,690,000.00 USD | 4,690,000.00 USD | 1,060.00 USD | 1,800.00 USD | 10.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 5,230,000.00 USD | 5,230,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 218,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,690,000.00 USD | 4,690,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 4,680,000.00 USD | 4,680,000.00 USD | 5,060.00 USD | 6,690.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 5,170,000.00 USD | 5,170,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 195,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,650,000.00 USD | 4,650,000.00 USD | 13,800.00 USD | 10,860.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 195,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 4,600,000.00 USD | 4,600,000.00 USD | 161,620.00 USD | 5,890.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 5,010,000.00 USD | 5,010,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,400,000.00 USD | 4,400,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 194,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 4,310,000.00 USD | 4,310,000.00 USD | 56,130.00 USD | 6,970.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 4,800,000.00 USD | 4,800,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 179,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,240,000.00 USD | 4,240,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,190,000.00 USD | 4,190,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 4,730,000.00 USD | 4,730,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 176,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,160,000.00 USD | 4,160,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 171,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,140,000.00 USD | 4,140,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 4,610,000.00 USD | 4,610,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 155,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,040,000.00 USD | 4,040,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 770.84 USD | 28,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 3,920,000.00 USD | 3,920,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 4,520,000.00 USD | 4,520,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 3,840,000.00 USD | 3,840,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 27,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 3,810,000.00 USD | 3,810,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 4,400,000.00 USD | 4,400,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 25,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,760,000.00 USD | 3,760,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 530.79 USD | 24,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,740,000.00 USD | 3,740,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 4,170,000.00 USD | 4,170,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,660,000.00 USD | 3,660,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,650,000.00 USD | 3,650,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 4,090,000.00 USD | 4,090,000.00 USD | 15,300.00 USD | 46,670.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,570,000.00 USD | 3,570,000.00 USD | 9,010.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,540,000.00 USD | 3,540,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 3,970,000.00 USD | 3,970,000.00 USD | 460,990.00 USD | 0.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,480,000.00 USD | 3,480,000.00 USD | 317,940.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,100,000.00 USD | 3,100,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 3,420,000.00 USD | 3,420,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 23,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 2,880,000.00 USD | 2,880,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 23,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 2,730,000.00 USD | 2,730,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 3,000,000.00 USD | 3,000,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 2,650,000.00 USD | 2,650,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 2,620,000.00 USD | 2,620,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 2,920,000.00 USD | 2,920,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 2,460,000.00 USD | 2,460,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.12` | 3,220.00 USD | 3,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 2,190,000.00 USD | 2,190,000.00 USD | 13,810.00 USD | 10,020.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 2,840,000.00 USD | 2,840,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,040,000.00 USD | 2,040,000.00 USD | 6,410.00 USD | 4,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 7,660.00 USD | 101,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 2,680,000.00 USD | 2,680,000.00 USD | 160,410.00 USD | 30,700.00 USD | 183,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.14` | 378.74 USD | 1,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.15` | 1,920,000.00 USD | 1,920,000.00 USD | 40,400.00 USD | 11,230.00 USD | 52,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.15` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,810,000.00 USD | 1,810,000.00 USD | 192.50 USD | 21,000.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 2,300,000.00 USD | 2,300,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 1,630,000.00 USD | 1,630,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 1,420,000.00 USD | 1,420,000.00 USD | 7,140.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 2,240,000.00 USD | 2,240,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 1,420,000.00 USD | 1,420,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 1,380,000.00 USD | 1,380,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 2,020,000.00 USD | 2,020,000.00 USD | 174,220.00 USD | 58,100.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 1,340,000.00 USD | 1,340,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 1,280,000.00 USD | 1,280,000.00 USD | 223.44 USD | 3,220.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 1,760,000.00 USD | 1,760,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 1,220,000.00 USD | 1,220,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 1,620,000.00 USD | 1,620,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,140,000.00 USD | 1,140,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 1,500,000.00 USD | 1,500,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,070,000.00 USD | 1,070,000.00 USD | 27,240.00 USD | 9,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,040,000.00 USD | 1,040,000.00 USD | 12,270.00 USD | 4,480.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 1,380,000.00 USD | 1,380,000.00 USD | 224,520.00 USD | 17,210.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,000,000.00 USD | 1,000,000.00 USD | 47,410.00 USD | 9,970.00 USD | 48,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 897,820.00 USD | 897,820.00 USD | 66,820.00 USD | 4,060.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 1,120,000.00 USD | 1,120,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 815,750.00 USD | 815,750.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 809,430.00 USD | 809,430.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 889,340.00 USD | 889,340.00 USD | 0.00 USD | 11,770.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 807,210.00 USD | 807,210.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 770,430.00 USD | 770,430.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 873,150.00 USD | 873,150.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 752,630.00 USD | 752,630.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 737,500.00 USD | 737,500.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 632,110.00 USD | 632,110.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 664,050.00 USD | 664,050.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 517,080.00 USD | 517,080.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 574,370.00 USD | 574,370.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 443,000.00 USD | 443,000.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 424,610.00 USD | 424,610.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 479,830.00 USD | 479,830.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 365,470.00 USD | 365,470.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 268,850.00 USD | 268,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 234,850.00 USD | 234,850.00 USD | 152,190.00 USD | 8,000.00 USD | 74,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 64,870.00 USD | 64,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.46` | 4,110.00 USD | 4,110.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 272,390.00 USD | 272,390.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 544,780.00 USD | 544,780.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 663.00 USD | 663.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 749.80 USD | 749.80 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 1,500.00 USD | 1,500.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 880,280.00 USD | 880,280.00 USD | 144,290.00 USD | 0.00 USD | 191,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.49` | 96,340.00 USD | 96,340.00 USD | 94,820.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.50` | 223,340.00 USD | 223,340.00 USD | 0.00 USD | 0.00 USD | 127,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 881,750.00 USD | 881,750.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.51` | 395,780.00 USD | 395,780.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.52` | 568,750.00 USD | 568,750.00 USD | 168,170.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 1,090,000.00 USD | 1,090,000.00 USD | 113,820.00 USD | 0.00 USD | 92,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.53` | 602,340.00 USD | 602,340.00 USD | 33,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 805,290.00 USD | 805,290.00 USD | 202,800.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 1,450,000.00 USD | 1,450,000.00 USD | 357,740.00 USD | 0.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.55` | 832,070.00 USD | 832,070.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 871,080.00 USD | 871,080.00 USD | 686.73 USD | 38,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 1,710,000.00 USD | 1,710,000.00 USD | 144,180.00 USD | 122,650.00 USD | 790.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.57` | 1,050,000.00 USD | 1,050,000.00 USD | 174,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,100,000.00 USD | 1,100,000.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 1,880,000.00 USD | 1,880,000.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 1,110,000.00 USD | 1,110,000.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 1,110,000.00 USD | 1,110,000.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,280,000.00 USD | 1,280,000.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 1,920,000.00 USD | 1,920,000.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 1,390,000.00 USD | 1,390,000.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,400,000.00 USD | 1,400,000.00 USD | 12,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 1,420,000.00 USD | 1,420,000.00 USD | 342.65 USD | 7,060.00 USD | 8,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 804.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,440,000.00 USD | 1,440,000.00 USD | 880.60 USD | 9,960.00 USD | 56.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,480,000.00 USD | 1,480,000.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 30,000.00 USD | 117,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 3,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,550,000.00 USD | 1,550,000.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,630,000.00 USD | 1,630,000.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 2,280,000.00 USD | 2,280,000.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,660,000.00 USD | 1,660,000.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,750,000.00 USD | 1,750,000.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,820,000.00 USD | 1,820,000.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,880,000.00 USD | 1,880,000.00 USD | 38,500.00 USD | 3,500.00 USD | 17,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 2,360,000.00 USD | 2,360,000.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,940,000.00 USD | 1,940,000.00 USD | 33,520.00 USD | 8,970.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 2,090,000.00 USD | 2,090,000.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 2,620,000.00 USD | 2,620,000.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 2,290,000.00 USD | 2,290,000.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,410,000.00 USD | 2,410,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 2,900,000.00 USD | 2,900,000.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,490,000.00 USD | 2,490,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,640,000.00 USD | 2,640,000.00 USD | 107,040.00 USD | 17,940.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 3,000,000.00 USD | 3,000,000.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,660,000.00 USD | 2,660,000.00 USD | 24,810.00 USD | 4,360.00 USD | 42.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,730,000.00 USD | 2,730,000.00 USD | 2,200.00 USD | 3,530.00 USD | 57,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 3,400,000.00 USD | 3,400,000.00 USD | 345,340.00 USD | 18,440.00 USD | 39,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 9,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,920,000.00 USD | 2,920,000.00 USD | 168,110.00 USD | 18,390.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,990,000.00 USD | 2,990,000.00 USD | 1,500.00 USD | 3,110.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.84` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 3,020,000.00 USD | 3,020,000.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 3,020,000.00 USD | 3,020,000.00 USD | 2,060.00 USD | 1,470.00 USD | 607.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 3,520,000.00 USD | 3,520,000.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.87` | 3,030,000.00 USD | 3,030,000.00 USD | 1,350.00 USD | 0.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 3,050,000.00 USD | 3,050,000.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.89` | 3,100,000.00 USD | 3,100,000.00 USD | 12,390.00 USD | 3,410.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 3,220,000.00 USD | 3,220,000.00 USD | 28,690.00 USD | 5,990.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 3,670,000.00 USD | 3,670,000.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 3,280,000.00 USD | 3,280,000.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 3,290,000.00 USD | 3,290,000.00 USD | 1,110.00 USD | 3,220.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 3,800,000.00 USD | 3,800,000.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 3,360,000.00 USD | 3,360,000.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 3,430,000.00 USD | 3,430,000.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 3,940,000.00 USD | 3,940,000.00 USD | 129,180.00 USD | 0.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.95` | 1,400.00 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.95` | 3,460,000.00 USD | 3,460,000.00 USD | 2,540.00 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 3,470,000.00 USD | 3,470,000.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 3,980,000.00 USD | 3,980,000.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.97` | 10,480.00 USD | 21,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.98` | 3,530,000.00 USD | 3,530,000.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 3,990,000.00 USD | 3,990,000.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 3,600,000.00 USD | 3,600,000.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 561,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 3,670,000.00 USD | 3,670,000.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 4,420,000.00 USD | 4,420,000.00 USD | 370,780.00 USD | 17,920.00 USD | 41,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,750,000.00 USD | 3,750,000.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,820,000.00 USD | 3,820,000.00 USD | 39,120.00 USD | 31,460.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 4,560,000.00 USD | 4,560,000.00 USD | 82,280.00 USD | 56,120.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,990,000.00 USD | 3,990,000.00 USD | 125,760.00 USD | 12,800.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 4,060,000.00 USD | 4,060,000.00 USD | 41,220.00 USD | 8,870.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 4,780,000.00 USD | 4,780,000.00 USD | 136,520.00 USD | 74,750.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 4,120,000.00 USD | 4,120,000.00 USD | 21,980.00 USD | 11,560.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 4,160,000.00 USD | 4,160,000.00 USD | 28,180.00 USD | 6,890.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 4,860,000.00 USD | 4,860,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 4,220,000.00 USD | 4,220,000.00 USD | 13,070.00 USD | 18,070.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 4,270,000.00 USD | 4,270,000.00 USD | 12,960.00 USD | 2,110.00 USD | 33,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 4,400,000.00 USD | 4,400,000.00 USD | 84,640.00 USD | 11,440.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 564,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 4,470,000.00 USD | 4,470,000.00 USD | 16,380.00 USD | 16,280.00 USD | 36,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 6,130,000.00 USD | 6,130,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 4,620,000.00 USD | 4,620,000.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,770,000.00 USD | 4,770,000.00 USD | 102,100.00 USD | 22,410.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 7,130,000.00 USD | 7,130,000.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,910,000.00 USD | 4,910,000.00 USD | 75,260.00 USD | 15,960.00 USD | 40,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,970,000.00 USD | 4,970,000.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 8,180,000.00 USD | 8,180,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.15` | 5,070,000.00 USD | 5,070,000.00 USD | 57,140.00 USD | 23,170.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 5,190,000.00 USD | 5,190,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 8,780,000.00 USD | 8,780,000.00 USD | 358,370.00 USD | 44,360.00 USD | 196,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 5,330,000.00 USD | 5,330,000.00 USD | 80,620.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 5,410,000.00 USD | 5,410,000.00 USD | 28,620.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 9,800,000.00 USD | 9,800,000.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 5,530,000.00 USD | 5,530,000.00 USD | 78,040.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 5,640,000.00 USD | 5,640,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 10,730,000.00 USD | 10,730,000.00 USD | 550,150.00 USD | 134,550.00 USD | 238,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,680,000.00 USD | 5,680,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,750,000.00 USD | 5,750,000.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 11,870,000.00 USD | 11,870,000.00 USD | 620,010.00 USD | 144,840.00 USD | 376,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,760,000.00 USD | 5,760,000.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,800,000.00 USD | 5,800,000.00 USD | 45,960.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 12,390,000.00 USD | 12,390,000.00 USD | 336,360.00 USD | 44,660.00 USD | 136,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,840,000.00 USD | 5,840,000.00 USD | 17,280.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,840,000.00 USD | 5,840,000.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 12,780,000.00 USD | 12,780,000.00 USD | 273,920.00 USD | 96,980.00 USD | 19,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,870,000.00 USD | 5,870,000.00 USD | 23,580.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,880,000.00 USD | 5,880,000.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 13,440,000.00 USD | 13,440,000.00 USD | 428,160.00 USD | 78,420.00 USD | 154,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,920,000.00 USD | 5,920,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 568,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,980,000.00 USD | 5,980,000.00 USD | 39,850.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 14,000,000.00 USD | 14,000,000.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 6,030,000.00 USD | 6,030,000.00 USD | 27,750.00 USD | 5,020.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 6,040,000.00 USD | 6,040,000.00 USD | 9,650.00 USD | 0.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 14,600,000.00 USD | 14,600,000.00 USD | 241,960.00 USD | 51,970.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.32` | 1,350.00 USD | 570,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.33` | 6,060,000.00 USD | 6,060,000.00 USD | 8,050.00 USD | 6,000.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 6,120,000.00 USD | 6,120,000.00 USD | 46,210.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 14,800,000.00 USD | 14,800,000.00 USD | 98,640.00 USD | 41,250.00 USD | 59,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 6,150,000.00 USD | 6,150,000.00 USD | 13,620.00 USD | 817.75 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 6,170,000.00 USD | 6,170,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 15,180,000.00 USD | 15,180,000.00 USD | 215,620.00 USD | 64,120.00 USD | 97,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 6,190,000.00 USD | 6,190,000.00 USD | 12,900.00 USD | 6,260.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 6,220,000.00 USD | 6,220,000.00 USD | 15,290.00 USD | 0.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 15,510,000.00 USD | 15,510,000.00 USD | 224,850.00 USD | 31,100.00 USD | 77,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 6,230,000.00 USD | 6,230,000.00 USD | 9,080.00 USD | 1,600.00 USD | 12.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 6,250,000.00 USD | 6,250,000.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 15,890,000.00 USD | 15,890,000.00 USD | 234,760.00 USD | 42,520.00 USD | 105,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 6,270,000.00 USD | 6,270,000.00 USD | 4,410.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 570,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 6,280,000.00 USD | 6,280,000.00 USD | 9,240.00 USD | 2,390.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 16,070,000.00 USD | 16,070,000.00 USD | 109,230.00 USD | 13,910.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 6,290,000.00 USD | 6,290,000.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 6,290,000.00 USD | 6,290,000.00 USD | 795.69 USD | 568.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 16,210,000.00 USD | 16,210,000.00 USD | 80,230.00 USD | 19,420.00 USD | 43,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 6,300,000.00 USD | 6,300,000.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 6,320,000.00 USD | 6,320,000.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 16,310,000.00 USD | 16,310,000.00 USD | 89,160.00 USD | 4,480.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 6,330,000.00 USD | 6,330,000.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 6,330,000.00 USD | 6,330,000.00 USD | 309.05 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 16,370,000.00 USD | 16,370,000.00 USD | 10,620.00 USD | 11,060.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 6,340,000.00 USD | 6,340,000.00 USD | 9,940.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.50` | 6,340,000.00 USD | 6,340,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 16,500,000.00 USD | 16,500,000.00 USD | 65,230.00 USD | 12,050.00 USD | 52,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.51` | 6,340,000.00 USD | 6,340,000.00 USD | 295.05 USD | 0.00 USD | 124.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 16,610,000.00 USD | 16,610,000.00 USD | 57,650.00 USD | 18,520.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.53` | 6,370,000.00 USD | 6,370,000.00 USD | 18,960.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 6,380,000.00 USD | 6,380,000.00 USD | 4,350.00 USD | 806.35 USD | 1,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 16,640,000.00 USD | 16,640,000.00 USD | 13,190.00 USD | 13,310.00 USD | 930.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 16,650,000.00 USD | 16,650,000.00 USD | 7,430.00 USD | 5,260.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 16,720,000.00 USD | 16,720,000.00 USD | 35,340.00 USD | 2,380.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 16,770,000.00 USD | 16,770,000.00 USD | 31,720.00 USD | 5,460.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 16,810,000.00 USD | 16,810,000.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 570,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 572,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 572,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 573,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 575,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.37` | 20,730.00 USD | 596,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 597,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 598,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.89` | 100.13 USD | 598,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.98` | 54,920.00 USD | 653,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 660,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.06` | 4,170.00 USD | 664,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.19` | 111,850.00 USD | 776,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.24` | 316.55 USD | 776,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 788,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.28` | 270.15 USD | 788,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 800,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.56` | 61,790.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.62` | 240.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.93` | 321.63 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 536.38 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.99` | 4,160.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.07` | 317.61 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.38` | 265,410.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.41` | 23,220.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 24,390.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.91` | 85,210.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.98` | 1,690.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.72` | 2,280,000.00 USD | 0.00 USD | 120.05 USD | `-79.80%` | `70.00` |
| `Live` | `Long` | `1.75` | 2,280,000.00 USD | 0.00 USD | 2,260.00 USD | `-79.33%` | `1,288.03` |
| `Live` | `Long` | `1.85` | 2,280,000.00 USD | 0.00 USD | 677.11 USD | `-78.16%` | `365.02` |
| `Live` | `Long` | `1.86` | 2,280,000.00 USD | 0.00 USD | 214.48 USD | `-78.04%` | `115.00` |
| `Live` | `Long` | `1.95` | 2,280,000.00 USD | 0.00 USD | 215.53 USD | `-77.10%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,280,000.00 USD | 0.00 USD | 1,460.00 USD | `-76.39%` | `727.30` |
| `Live` | `Long` | `2.04` | 2,270,000.00 USD | 0.00 USD | 110.52 USD | `-76.04%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,270,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.68%` | `2,382.76` |
| `Live` | `Long` | `2.12` | 2,270,000.00 USD | 0.00 USD | 243.23 USD | `-75.09%` | `115.00` |
| `Live` | `Long` | `2.15` | 2,270,000.00 USD | 0.00 USD | 246.68 USD | `-74.74%` | `115.00` |
| `Live` | `Long` | `2.21` | 2,270,000.00 USD | 0.00 USD | 111.10 USD | `-73.92%` | `50.16` |
| `Live` | `Long` | `2.23` | 2,270,000.00 USD | 0.00 USD | 361.94 USD | `-73.68%` | `161.94` |
| `Live` | `Long` | `2.46` | 2,270,000.00 USD | 0.00 USD | 9,810.00 USD | `-70.97%` | `3,981.48` |
| `Live` | `Long` | `2.69` | 2,260,000.00 USD | 0.00 USD | 942.44 USD | `-68.38%` | `351.00` |
| `Live` | `Long` | `2.75` | 2,260,000.00 USD | 0.00 USD | 143.26 USD | `-67.56%` | `52.00` |
| `Live` | `Long` | `2.81` | 2,260,000.00 USD | 0.00 USD | 322.58 USD | `-66.97%` | `115.00` |
| `Live` | `Long` | `2.87` | 2,260,000.00 USD | 0.00 USD | 232.67 USD | `-66.26%` | `81.21` |
| `Live` | `Long` | `2.90` | 2,260,000.00 USD | 0.00 USD | 20,310.00 USD | `-65.79%` | `6,990.57` |
| `Live` | `Long` | `2.94` | 2,240,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.44%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,190,000.00 USD | 0.00 USD | 111.12 USD | `-64.97%` | `37.35` |
| `Live` | `Long` | `2.98` | 2,190,000.00 USD | 0.00 USD | 100.03 USD | `-64.85%` | `33.51` |
| `Live` | `Long` | `3.21` | 2,190,000.00 USD | 0.00 USD | 24,000.00 USD | `-62.14%` | `7,465.11` |
| `Live` | `Long` | `3.29` | 2,170,000.00 USD | 0.00 USD | 1,240.00 USD | `-61.20%` | `377.71` |
| `Live` | `Long` | `3.37` | 2,170,000.00 USD | 0.00 USD | 389.53 USD | `-60.37%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,170,000.00 USD | 0.00 USD | 151.88 USD | `-60.26%` | `45.00` |
| `Live` | `Long` | `3.42` | 2,170,000.00 USD | 0.00 USD | 557.73 USD | `-59.67%` | `162.84` |
| `Live` | `Long` | `3.54` | 2,170,000.00 USD | 0.00 USD | 392.22 USD | `-58.25%` | `110.64` |
| `Live` | `Long` | `3.67` | 2,160,000.00 USD | 0.00 USD | 109.95 USD | `-56.84%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,160,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.78%` | `400.00` |
| `Live` | `Long` | `3.79` | 2,160,000.00 USD | 0.00 USD | 7,570.00 USD | `-55.43%` | `2,000.00` |
| `Live` | `Long` | `3.83` | 2,160,000.00 USD | 0.00 USD | 1,530.00 USD | `-54.96%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,150,000.00 USD | 0.00 USD | 131.73 USD | `-54.13%` | `33.82` |
| `Live` | `Long` | `3.96` | 2,150,000.00 USD | 0.00 USD | 2,630.00 USD | `-53.43%` | `666.20` |
| `Live` | `Long` | `4.03` | 2,150,000.00 USD | 0.00 USD | 402.70 USD | `-52.60%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,150,000.00 USD | 0.00 USD | 152.29 USD | `-52.37%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,150,000.00 USD | 0.00 USD | 159.29 USD | `-51.19%` | `38.43` |
| `Live` | `Long` | `4.17` | 2,150,000.00 USD | 0.00 USD | 388.68 USD | `-50.95%` | `93.32` |
| `Live` | `Long` | `4.24` | 2,150,000.00 USD | 0.00 USD | 169.40 USD | `-50.13%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,150,000.00 USD | 0.00 USD | 196.42 USD | `-50.01%` | `46.27` |
| `Live` | `Long` | `4.45` | 2,150,000.00 USD | 0.00 USD | 110.77 USD | `-47.66%` | `24.92` |
| `Live` | `Long` | `4.59` | 2,150,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.89%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,120,000.00 USD | 0.00 USD | 486.93 USD | `-45.65%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,120,000.00 USD | 0.00 USD | 2,930.00 USD | `-45.54%` | `634.06` |
| `Live` | `Long` | `4.63` | 2,120,000.00 USD | 0.00 USD | 295.48 USD | `-45.42%` | `63.75` |
| `Live` | `Long` | `4.66` | 2,120,000.00 USD | 0.00 USD | 105.11 USD | `-45.18%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,120,000.00 USD | 0.00 USD | 3,280.00 USD | `-45.07%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,110,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.95%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,110,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.83%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,100,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.71%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,090,000.00 USD | 0.00 USD | 474.50 USD | `-44.12%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,090,000.00 USD | 0.00 USD | 105.64 USD | `-43.89%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,090,000.00 USD | 0.00 USD | 467.01 USD | `-43.06%` | `96.59` |
| `Live` | `Long` | `4.84` | 2,090,000.00 USD | 0.00 USD | 532.95 USD | `-42.95%` | `110.00` |
| `Live` | `Long` | `4.88` | 2,090,000.00 USD | 0.00 USD | 209.97 USD | `-42.59%` | `43.07` |
| `Live` | `Long` | `4.88` | 2,090,000.00 USD | 0.00 USD | 506.72 USD | `-42.48%` | `103.73` |
| `Live` | `Long` | `4.89` | 2,090,000.00 USD | 0.00 USD | 16,080.00 USD | `-42.36%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,080,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.24%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,070,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.12%` | `251.00` |
| `Live` | `Long` | `4.95` | 2,070,000.00 USD | 0.00 USD | 2,830.00 USD | `-41.77%` | `571.32` |
| `Live` | `Long` | `4.96` | 2,070,000.00 USD | 0.00 USD | 945.36 USD | `-41.65%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,070,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.53%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,060,000.00 USD | 0.00 USD | 282.23 USD | `-41.42%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,060,000.00 USD | 0.00 USD | 269.53 USD | `-41.18%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,060,000.00 USD | 0.00 USD | 56,390.00 USD | `-40.94%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,010,000.00 USD | 0.00 USD | 167.78 USD | `-40.83%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,010,000.00 USD | 0.00 USD | 314.59 USD | `-40.71%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,010,000.00 USD | 0.00 USD | 504.74 USD | `-40.47%` | `99.85` |
| `Live` | `Long` | `5.07` | 2,010,000.00 USD | 0.00 USD | 739.39 USD | `-40.36%` | `145.98` |
| `Live` | `Long` | `5.08` | 2,000,000.00 USD | 0.00 USD | 213.20 USD | `-40.24%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,000,000.00 USD | 0.00 USD | 223.43 USD | `-40.12%` | `43.94` |
| `Live` | `Long` | `5.12` | 2,000,000.00 USD | 0.00 USD | 1,040.00 USD | `-39.77%` | `202.43` |
| `Live` | `Long` | `5.12` | 2,000,000.00 USD | 0.00 USD | 250.20 USD | `-39.65%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,000,000.00 USD | 0.00 USD | 5,800.00 USD | `-39.53%` | `1,130.13` |
| `Live` | `Long` | `5.16` | 2,000,000.00 USD | 0.00 USD | 209.34 USD | `-39.30%` | `40.61` |
| `Live` | `Long` | `5.17` | 2,000,000.00 USD | 0.00 USD | 1,620.00 USD | `-39.06%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,000,000.00 USD | 0.00 USD | 150.57 USD | `-38.94%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,000,000.00 USD | 0.00 USD | 300.91 USD | `-38.59%` | `57.70` |
| `Live` | `Long` | `5.25` | 2,000,000.00 USD | 0.00 USD | 503.78 USD | `-38.24%` | `96.05` |
| `Live` | `Long` | `5.25` | 1,990,000.00 USD | 0.00 USD | 1,050.00 USD | `-38.12%` | `200.00` |
| `Live` | `Long` | `5.26` | 1,990,000.00 USD | 0.00 USD | 2,230.00 USD | `-38.00%` | `423.54` |
| `Live` | `Long` | `5.28` | 1,990,000.00 USD | 0.00 USD | 160,550.00 USD | `-37.88%` | `30,435.20` |
| `Live` | `Long` | `5.29` | 1,830,000.00 USD | 0.00 USD | 640.70 USD | `-37.76%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,830,000.00 USD | 0.00 USD | 232.85 USD | `-37.41%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,830,000.00 USD | 0.00 USD | 716.11 USD | `-37.29%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,830,000.00 USD | 0.00 USD | 660.46 USD | `-36.47%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 20,160.00 USD | `-36.23%` | `3,723.69` |
| `Live` | `Long` | `5.42` | 1,810,000.00 USD | 0.00 USD | 160,400.00 USD | `-36.12%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,650,000.00 USD | 0.00 USD | 1,360.00 USD | `-36.00%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,650,000.00 USD | 0.00 USD | 299.48 USD | `-35.88%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,650,000.00 USD | 0.00 USD | 264.72 USD | `-35.65%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,650,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.53%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,640,000.00 USD | 0.00 USD | 354.06 USD | `-35.41%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,640,000.00 USD | 0.00 USD | 19,290.00 USD | `-35.29%` | `3,510.41` |
| `Live` | `Long` | `5.51` | 1,630,000.00 USD | 0.00 USD | 1,860.00 USD | `-35.06%` | `336.62` |
| `Live` | `Long` | `5.54` | 1,620,000.00 USD | 0.00 USD | 2,880.00 USD | `-34.70%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,620,000.00 USD | 0.00 USD | 63,530.00 USD | `-34.35%` | `11,395.80` |
| `Live` | `Long` | `5.61` | 1,560,000.00 USD | 0.00 USD | 34,490.00 USD | `-34.00%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,520,000.00 USD | 0.00 USD | 2,810.00 USD | `-33.88%` | `500.00` |
| `Live` | `Long` | `5.63` | 1,520,000.00 USD | 0.00 USD | 468.55 USD | `-33.64%` | `83.15` |
| `Live` | `Long` | `5.67` | 1,520,000.00 USD | 0.00 USD | 1,330.00 USD | `-33.17%` | `233.60` |
| `Live` | `Long` | `5.71` | 1,520,000.00 USD | 0.00 USD | 147.33 USD | `-32.70%` | `25.78` |
| `Live` | `Long` | `5.72` | 1,520,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.58%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,520,000.00 USD | 0.00 USD | 661.65 USD | `-32.47%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,510,000.00 USD | 0.00 USD | 125.70 USD | `-32.35%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,510,000.00 USD | 0.00 USD | 3,190.00 USD | `-32.23%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,510,000.00 USD | 0.00 USD | 10,850.00 USD | `-32.11%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,500,000.00 USD | 0.00 USD | 801.40 USD | `-31.99%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,500,000.00 USD | 0.00 USD | 635.31 USD | `-31.76%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,500,000.00 USD | 0.00 USD | 580.50 USD | `-31.64%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,500,000.00 USD | 0.00 USD | 106.65 USD | `-31.52%` | `18.34` |
| `Live` | `Long` | `5.84` | 1,500,000.00 USD | 0.00 USD | 146.13 USD | `-31.17%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,500,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.05%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,500,000.00 USD | 0.00 USD | 984.70 USD | `-30.58%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,490,000.00 USD | 0.00 USD | 399.18 USD | `-30.46%` | `67.60` |
| `Live` | `Long` | `5.92` | 1,490,000.00 USD | 0.00 USD | 277.35 USD | `-30.35%` | `46.89` |
| `Live` | `Long` | `5.96` | 1,490,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.88%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,480,000.00 USD | 0.00 USD | 6,320.00 USD | `-29.76%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,480,000.00 USD | 0.00 USD | 585.97 USD | `-29.64%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,480,000.00 USD | 0.00 USD | 571.86 USD | `-29.29%` | `95.23` |
| `Live` | `Long` | `6.01` | 1,480,000.00 USD | 0.00 USD | 446.85 USD | `-29.17%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,470,000.00 USD | 0.00 USD | 437.84 USD | `-28.82%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,470,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.70%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,470,000.00 USD | 0.00 USD | 265.10 USD | `-28.58%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,470,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.46%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,470,000.00 USD | 0.00 USD | 405.14 USD | `-28.34%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,470,000.00 USD | 0.00 USD | 3,130.00 USD | `-28.23%` | `512.81` |
| `Live` | `Long` | `6.12` | 1,470,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.99%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,470,000.00 USD | 0.00 USD | 137.02 USD | `-27.87%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,470,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.76%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,460,000.00 USD | 0.00 USD | 238.61 USD | `-27.64%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,460,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.52%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,460,000.00 USD | 0.00 USD | 104.36 USD | `-27.28%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,460,000.00 USD | 0.00 USD | 310.25 USD | `-26.93%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,460,000.00 USD | 0.00 USD | 972.65 USD | `-26.34%` | `155.50` |
| `Live` | `Long` | `6.26` | 1,450,000.00 USD | 0.00 USD | 2,420.00 USD | `-26.22%` | `386.46` |
| `Live` | `Long` | `6.28` | 1,450,000.00 USD | 0.00 USD | 2,510.00 USD | `-26.11%` | `400.00` |
| `Live` | `Long` | `6.33` | 1,450,000.00 USD | 0.00 USD | 277.48 USD | `-25.52%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,450,000.00 USD | 0.00 USD | 1,430.00 USD | `-25.40%` | `225.14` |
| `Live` | `Long` | `6.36` | 1,450,000.00 USD | 0.00 USD | 4,470.00 USD | `-25.16%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,440,000.00 USD | 0.00 USD | 284,770.00 USD | `-25.05%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,160,000.00 USD | 0.00 USD | 1,310.00 USD | `-24.93%` | `204.92` |
| `Live` | `Long` | `6.38` | 1,160,000.00 USD | 0.00 USD | 5,120.00 USD | `-24.81%` | `801.31` |
| `Live` | `Long` | `6.42` | 1,150,000.00 USD | 0.00 USD | 359,930.00 USD | `-24.46%` | `56,107.15` |
| `Live` | `Long` | `6.42` | 792,390.00 USD | 0.00 USD | 484.64 USD | `-24.34%` | `75.43` |
| `Live` | `Long` | `6.43` | 791,900.00 USD | 0.00 USD | 6,780.00 USD | `-24.22%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 785,130.00 USD | 0.00 USD | 1,050.00 USD | `-23.87%` | `162.75` |
| `Live` | `Long` | `6.47` | 784,070.00 USD | 0.00 USD | 1,520.00 USD | `-23.75%` | `234.11` |
| `Live` | `Long` | `6.54` | 782,560.00 USD | 0.00 USD | 852.03 USD | `-23.05%` | `130.38` |
| `Live` | `Long` | `6.54` | 781,710.00 USD | 0.00 USD | 8,970.00 USD | `-22.93%` | `1,370.89` |
| `Live` | `Long` | `6.58` | 772,730.00 USD | 0.00 USD | 1,500.00 USD | `-22.57%` | `228.41` |
| `Live` | `Long` | `6.58` | 771,230.00 USD | 0.00 USD | 1,770.00 USD | `-22.46%` | `269.14` |
| `Live` | `Long` | `6.59` | 769,460.00 USD | 0.00 USD | 1,100.00 USD | `-22.34%` | `166.55` |
| `Live` | `Long` | `6.62` | 768,360.00 USD | 0.00 USD | 3,640.00 USD | `-22.10%` | `549.59` |
| `Live` | `Long` | `6.62` | 764,730.00 USD | 0.00 USD | 364.90 USD | `-21.99%` | `55.08` |
| `Live` | `Long` | `6.63` | 764,360.00 USD | 0.00 USD | 245.89 USD | `-21.87%` | `37.06` |
| `Live` | `Long` | `6.67` | 764,110.00 USD | 0.00 USD | 1,320.00 USD | `-21.40%` | `198.12` |
| `Live` | `Long` | `6.68` | 762,790.00 USD | 0.00 USD | 3,160.00 USD | `-21.28%` | `472.28` |
| `Live` | `Long` | `6.71` | 759,630.00 USD | 0.00 USD | 16,570.00 USD | `-21.04%` | `2,471.72` |
| `Live` | `Long` | `6.71` | 743,060.00 USD | 0.00 USD | 6,180.00 USD | `-20.93%` | `920.74` |
| `Live` | `Long` | `6.75` | 736,880.00 USD | 0.00 USD | 1,330.00 USD | `-20.45%` | `196.95` |
| `Live` | `Long` | `6.78` | 735,550.00 USD | 0.00 USD | 7,990.00 USD | `-20.22%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 727,560.00 USD | 0.00 USD | 21,580.00 USD | `-20.10%` | `3,180.66` |
| `Live` | `Long` | `6.79` | 705,970.00 USD | 0.00 USD | 5,540.00 USD | `-19.98%` | `815.34` |
| `Live` | `Long` | `6.80` | 700,430.00 USD | 0.00 USD | 1,500.00 USD | `-19.87%` | `220.95` |
| `Live` | `Long` | `6.82` | 698,930.00 USD | 0.00 USD | 7,230.00 USD | `-19.75%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 691,700.00 USD | 0.00 USD | 288.56 USD | `-19.63%` | `42.28` |
| `Live` | `Long` | `6.87` | 691,410.00 USD | 0.00 USD | 3,340.00 USD | `-19.16%` | `486.46` |
| `Live` | `Long` | `6.88` | 688,070.00 USD | 0.00 USD | 1,580.00 USD | `-18.92%` | `229.18` |
| `Live` | `Long` | `6.92` | 686,490.00 USD | 0.00 USD | 579.62 USD | `-18.45%` | `83.70` |
| `Live` | `Long` | `6.93` | 685,910.00 USD | 0.00 USD | 3,500.00 USD | `-18.33%` | `504.07` |
| `Live` | `Long` | `6.95` | 682,420.00 USD | 0.00 USD | 215.30 USD | `-18.22%` | `31.00` |
| `Live` | `Long` | `6.96` | 682,200.00 USD | 0.00 USD | 7,240.00 USD | `-18.10%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 674,960.00 USD | 0.00 USD | 636.74 USD | `-17.98%` | `91.42` |
| `Live` | `Long` | `6.97` | 674,320.00 USD | 0.00 USD | 128,810.00 USD | `-17.86%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 545,510.00 USD | 0.00 USD | 1,040.00 USD | `-17.63%` | `149.32` |
| `Live` | `Long` | `7.01` | 544,470.00 USD | 0.00 USD | 20,890.00 USD | `-17.39%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 523,580.00 USD | 0.00 USD | 1,370.00 USD | `-17.28%` | `194.51` |
| `Live` | `Long` | `7.07` | 522,210.00 USD | 0.00 USD | 23,960.00 USD | `-16.80%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 498,260.00 USD | 0.00 USD | 6,700.00 USD | `-16.69%` | `947.44` |
| `Live` | `Long` | `7.08` | 491,550.00 USD | 0.00 USD | 1,050.00 USD | `-16.57%` | `148.63` |
| `Live` | `Long` | `7.09` | 490,500.00 USD | 0.00 USD | 2,130.00 USD | `-16.45%` | `300.00` |
| `Live` | `Long` | `7.11` | 488,370.00 USD | 0.00 USD | 28,530.00 USD | `-16.33%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 459,840.00 USD | 0.00 USD | 379.66 USD | `-16.22%` | `53.36` |
| `Live` | `Long` | `7.12` | 459,460.00 USD | 0.00 USD | 2,500.00 USD | `-16.10%` | `350.58` |
| `Live` | `Long` | `7.13` | 456,960.00 USD | 0.00 USD | 777.50 USD | `-15.98%` | `108.97` |
| `Live` | `Long` | `7.14` | 456,190.00 USD | 0.00 USD | 20,270.00 USD | `-15.86%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 435,920.00 USD | 0.00 USD | 2,380.00 USD | `-15.51%` | `331.12` |
| `Live` | `Long` | `7.18` | 433,540.00 USD | 0.00 USD | 1,440.00 USD | `-15.39%` | `200.95` |
| `Live` | `Long` | `7.21` | 432,100.00 USD | 0.00 USD | 28,820.00 USD | `-15.16%` | `4,000.00` |
| `Live` | `Long` | `7.21` | 403,280.00 USD | 0.00 USD | 322.94 USD | `-15.04%` | `44.76` |
| `Live` | `Long` | `7.24` | 402,950.00 USD | 0.00 USD | 3,590.00 USD | `-14.80%` | `496.61` |
| `Live` | `Long` | `7.25` | 399,360.00 USD | 0.00 USD | 185.83 USD | `-14.68%` | `25.65` |
| `Live` | `Long` | `7.25` | 399,180.00 USD | 0.00 USD | 21,280.00 USD | `-14.57%` | `2,933.17` |
| `Live` | `Long` | `7.26` | 377,900.00 USD | 0.00 USD | 1,450.00 USD | `-14.45%` | `200.00` |
| `Live` | `Long` | `7.29` | 376,440.00 USD | 0.00 USD | 36,420.00 USD | `-14.21%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 340,020.00 USD | 0.00 USD | 1,680.00 USD | `-14.10%` | `230.97` |
| `Live` | `Long` | `7.34` | 338,330.00 USD | 0.00 USD | 552.42 USD | `-13.51%` | `75.21` |
| `Live` | `Long` | `7.36` | 337,780.00 USD | 0.00 USD | 3,820.00 USD | `-13.39%` | `519.63` |
| `Live` | `Long` | `7.37` | 333,960.00 USD | 0.00 USD | 16,100.00 USD | `-13.27%` | `2,186.20` |
| `Live` | `Long` | `7.38` | 317,860.00 USD | 0.00 USD | 2,130.00 USD | `-13.15%` | `288.75` |
| `Live` | `Long` | `7.38` | 315,730.00 USD | 0.00 USD | 1,080.00 USD | `-13.04%` | `146.20` |
| `Live` | `Long` | `7.42` | 314,650.00 USD | 0.00 USD | 147.61 USD | `-12.56%` | `19.88` |
| `Live` | `Long` | `7.43` | 314,500.00 USD | 0.00 USD | 2,430.00 USD | `-12.45%` | `327.05` |
| `Live` | `Long` | `7.45` | 312,070.00 USD | 0.00 USD | 2,410.00 USD | `-12.33%` | `324.35` |
| `Live` | `Long` | `7.46` | 309,650.00 USD | 0.00 USD | 10,390.00 USD | `-12.21%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 299,260.00 USD | 0.00 USD | 4,590.00 USD | `-12.09%` | `614.36` |
| `Live` | `Long` | `7.47` | 294,680.00 USD | 0.00 USD | 1,120.00 USD | `-11.98%` | `149.52` |
| `Live` | `Long` | `7.50` | 293,560.00 USD | 0.00 USD | 962.81 USD | `-11.74%` | `128.46` |
| `Live` | `Long` | `7.50` | 292,600.00 USD | 0.00 USD | 421.78 USD | `-11.62%` | `56.20` |
| `Live` | `Long` | `7.51` | 292,180.00 USD | 0.00 USD | 1,710.00 USD | `-11.50%` | `228.21` |
| `Live` | `Long` | `7.53` | 290,460.00 USD | 0.00 USD | 1,570.00 USD | `-11.39%` | `208.52` |
| `Live` | `Long` | `7.54` | 288,890.00 USD | 0.00 USD | 4,210.00 USD | `-11.27%` | `559.01` |
| `Live` | `Long` | `7.55` | 284,680.00 USD | 0.00 USD | 1,510.00 USD | `-11.03%` | `200.00` |
| `Live` | `Long` | `7.57` | 283,170.00 USD | 0.00 USD | 25,060.00 USD | `-10.92%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 258,110.00 USD | 0.00 USD | 118.25 USD | `-10.80%` | `15.61` |
| `Live` | `Long` | `7.59` | 257,990.00 USD | 0.00 USD | 1,630.00 USD | `-10.56%` | `214.22` |
| `Live` | `Long` | `7.62` | 256,370.00 USD | 0.00 USD | 754.04 USD | `-10.33%` | `99.02` |
| `Live` | `Long` | `7.62` | 255,610.00 USD | 0.00 USD | 787.51 USD | `-10.21%` | `103.28` |
| `Live` | `Long` | `7.63` | 254,830.00 USD | 0.00 USD | 378.93 USD | `-10.09%` | `49.63` |
| `Live` | `Long` | `7.66` | 254,450.00 USD | 0.00 USD | 135.42 USD | `-9.86%` | `17.69` |
| `Live` | `Long` | `7.67` | 254,310.00 USD | 0.00 USD | 256.09 USD | `-9.74%` | `33.41` |
| `Live` | `Long` | `7.67` | 254,060.00 USD | 0.00 USD | 4,480.00 USD | `-9.62%` | `583.63` |
| `Live` | `Long` | `7.68` | 249,580.00 USD | 0.00 USD | 739.30 USD | `-9.50%` | `96.20` |
| `Live` | `Long` | `7.70` | 248,840.00 USD | 0.00 USD | 6,690.00 USD | `-9.39%` | `869.22` |
| `Live` | `Long` | `7.75` | 242,150.00 USD | 0.00 USD | 500.12 USD | `-8.68%` | `64.49` |
| `Live` | `Long` | `7.76` | 241,650.00 USD | 0.00 USD | 455.73 USD | `-8.56%` | `58.69` |
| `Live` | `Long` | `7.78` | 241,190.00 USD | 0.00 USD | 8,670.00 USD | `-8.44%` | `1,115.74` |
| `Live` | `Long` | `7.79` | 232,520.00 USD | 0.00 USD | 1,380.00 USD | `-8.33%` | `177.40` |
| `Live` | `Long` | `7.79` | 231,140.00 USD | 0.00 USD | 4,480.00 USD | `-8.21%` | `574.50` |
| `Live` | `Long` | `7.80` | 226,660.00 USD | 0.00 USD | 6,380.00 USD | `-8.09%` | `817.06` |
| `Live` | `Long` | `7.83` | 220,280.00 USD | 0.00 USD | 1,940.00 USD | `-7.85%` | `247.42` |
| `Live` | `Long` | `7.84` | 218,340.00 USD | 0.00 USD | 22,560.00 USD | `-7.62%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 195,780.00 USD | 0.00 USD | 233.83 USD | `-7.38%` | `29.73` |
| `Live` | `Long` | `7.88` | 195,550.00 USD | 0.00 USD | 555.19 USD | `-7.27%` | `70.50` |
| `Live` | `Long` | `7.89` | 194,990.00 USD | 0.00 USD | 15,880.00 USD | `-7.03%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 179,110.00 USD | 0.00 USD | 2,930.00 USD | `-6.91%` | `370.74` |
| `Live` | `Long` | `7.92` | 176,180.00 USD | 0.00 USD | 4,600.00 USD | `-6.68%` | `580.78` |
| `Live` | `Long` | `7.93` | 171,580.00 USD | 0.00 USD | 16,340.00 USD | `-6.56%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 155,230.00 USD | 0.00 USD | 127,110.00 USD | `-6.44%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 28,120.00 USD | 0.00 USD | 770.84 USD | `-6.32%` | `96.90` |
| `Live` | `Long` | `7.97` | 27,350.00 USD | 0.00 USD | 1,580.00 USD | `-6.09%` | `198.26` |
| `Live` | `Long` | `7.99` | 25,770.00 USD | 0.00 USD | 1,280.00 USD | `-5.97%` | `160.68` |
| `Live` | `Long` | `8.00` | 24,480.00 USD | 0.00 USD | 530.79 USD | `-5.85%` | `66.39` |
| `Live` | `Long` | `8.06` | 23,950.00 USD | 0.00 USD | 439.54 USD | `-5.03%` | `54.50` |
| `Live` | `Long` | `8.07` | 23,510.00 USD | 0.00 USD | 21,710.00 USD | `-4.91%` | `2,688.93` |
| `Live` | `Short` | `8.12` | 3,220.00 USD | 3,220.00 USD | 0.00 USD | `-4.44%` | `396.30` |
| `Live` | `Long` | `8.14` | 1,800.00 USD | 0.00 USD | 378.74 USD | `-4.09%` | `46.50` |
| `Live` | `Long` | `8.15` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | `-3.97%` | `174.44` |
| `Live` | `Short` | `8.69` | 3,430.00 USD | 209.31 USD | 0.00 USD | `+2.27%` | `24.10` |
| `Live` | `Short` | `8.82` | 9,430.00 USD | 6,000.00 USD | 0.00 USD | `+3.92%` | `680.16` |
| `Live` | `Short` | `8.95` | 10,830.00 USD | 1,400.00 USD | 0.00 USD | `+5.33%` | `156.50` |
| `Live` | `Short` | `8.97` | 21,310.00 USD | 10,480.00 USD | 0.00 USD | `+5.69%` | `1,167.41` |
| `Live` | `Short` | `8.99` | 561,010.00 USD | 539,710.00 USD | 0.00 USD | `+5.92%` | `60,000.94` |
| `Live` | `Short` | `9.10` | 564,900.00 USD | 3,890.00 USD | 0.00 USD | `+7.10%` | `427.53` |
| `Live` | `Short` | `9.29` | 568,760.00 USD | 3,860.00 USD | 0.00 USD | `+9.46%` | `415.00` |
| `Live` | `Short` | `9.32` | 570,110.00 USD | 1,350.00 USD | 0.00 USD | `+9.81%` | `145.04` |
| `Live` | `Short` | `9.41` | 570,550.00 USD | 440.06 USD | 0.00 USD | `+10.87%` | `46.74` |
| `Live` | `Short` | `9.62` | 570,690.00 USD | 138.98 USD | 0.00 USD | `+13.34%` | `14.44` |
| `Live` | `Short` | `9.64` | 572,630.00 USD | 1,930.00 USD | 0.00 USD | `+13.58%` | `200.61` |
| `Live` | `Short` | `9.73` | 572,820.00 USD | 192.95 USD | 0.00 USD | `+14.64%` | `19.82` |
| `Live` | `Short` | `9.88` | 573,190.00 USD | 371.77 USD | 0.00 USD | `+16.40%` | `37.61` |
| `Live` | `Short` | `10.35` | 575,840.00 USD | 2,650.00 USD | 0.00 USD | `+21.82%` | `256.58` |
| `Live` | `Short` | `10.37` | 596,570.00 USD | 20,730.00 USD | 0.00 USD | `+22.06%` | `2,000.00` |
| `Live` | `Short` | `10.56` | 597,100.00 USD | 523.81 USD | 0.00 USD | `+24.41%` | `49.58` |
| `Live` | `Short` | `10.81` | 598,250.00 USD | 1,150.00 USD | 0.00 USD | `+27.36%` | `106.17` |
| `Live` | `Short` | `10.89` | 598,350.00 USD | 100.13 USD | 0.00 USD | `+28.30%` | `9.19` |
| `Live` | `Short` | `10.98` | 653,270.00 USD | 54,920.00 USD | 0.00 USD | `+29.36%` | `5,000.00` |
| `Live` | `Short` | `11.01` | 660,240.00 USD | 6,970.00 USD | 0.00 USD | `+29.59%` | `633.00` |
| `Live` | `Short` | `11.06` | 664,400.00 USD | 4,170.00 USD | 0.00 USD | `+30.30%` | `376.48` |
| `Live` | `Short` | `11.19` | 776,250.00 USD | 111,850.00 USD | 0.00 USD | `+31.71%` | `10,000.00` |
| `Live` | `Short` | `11.24` | 776,570.00 USD | 316.55 USD | 0.00 USD | `+32.42%` | `28.15` |
| `Live` | `Short` | `11.27` | 788,240.00 USD | 11,670.00 USD | 0.00 USD | `+32.65%` | `1,035.87` |
| `Live` | `Short` | `11.28` | 788,510.00 USD | 270.15 USD | 0.00 USD | `+32.77%` | `23.96` |
| `Live` | `Short` | `11.62` | 800,650.00 USD | 12,140.00 USD | 0.00 USD | `+36.89%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,100,000.00 USD | 296,760.00 USD | 0.00 USD | `+37.60%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 1,100,000.00 USD | 505.74 USD | 0.00 USD | `+40.43%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,100,000.00 USD | 1,050.00 USD | 0.00 USD | `+40.66%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,100,000.00 USD | 1,730.00 USD | 0.00 USD | `+44.90%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,100,000.00 USD | 343.62 USD | 0.00 USD | `+46.08%` | `27.70` |
| `Live` | `Short` | `13.20` | 1,190,000.00 USD | 87,940.00 USD | 0.00 USD | `+55.38%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,190,000.00 USD | 3,810.00 USD | 0.00 USD | `+56.56%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,190,000.00 USD | 430.34 USD | 0.00 USD | `+58.56%` | `31.96` |
| `Live` | `Short` | `13.56` | 1,260,000.00 USD | 61,790.00 USD | 0.00 USD | `+59.74%` | `4,555.14` |
| `Live` | `Short` | `13.69` | 1,260,000.00 USD | 172.29 USD | 0.00 USD | `+61.15%` | `12.59` |
| `Live` | `Short` | `14.62` | 1,260,000.00 USD | 240.00 USD | 0.00 USD | `+72.22%` | `16.41` |
| `Live` | `Short` | `14.66` | 1,260,000.00 USD | 823.29 USD | 0.00 USD | `+72.69%` | `56.14` |
| `Live` | `Short` | `14.93` | 1,260,000.00 USD | 321.63 USD | 0.00 USD | `+75.75%` | `21.55` |
| `Live` | `Short` | `14.95` | 1,260,000.00 USD | 536.38 USD | 0.00 USD | `+75.99%` | `35.89` |
| `Live` | `Short` | `14.99` | 1,260,000.00 USD | 4,160.00 USD | 0.00 USD | `+76.58%` | `277.54` |
| `Live` | `Short` | `15.09` | 1,260,000.00 USD | 219.34 USD | 0.00 USD | `+77.64%` | `14.54` |
| `Live` | `Short` | `15.29` | 1,260,000.00 USD | 229.43 USD | 0.00 USD | `+80.11%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,260,000.00 USD | 230.17 USD | 0.00 USD | `+80.70%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,280,000.00 USD | 20,000.00 USD | 0.00 USD | `+81.17%` | `1,300.00` |
| `Live` | `Short` | `15.77` | 1,280,000.00 USD | 185.55 USD | 0.00 USD | `+85.65%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,280,000.00 USD | 1,700.00 USD | 0.00 USD | `+86.35%` | `107.48` |
| `Live` | `Short` | `16.07` | 1,280,000.00 USD | 317.61 USD | 0.00 USD | `+89.18%` | `19.77` |
| `Live` | `Short` | `16.38` | 1,550,000.00 USD | 265,410.00 USD | 0.00 USD | `+92.83%` | `16,208.00` |
| `Live` | `Short` | `16.41` | 1,570,000.00 USD | 23,220.00 USD | 0.00 USD | `+93.30%` | `1,414.55` |
| `Live` | `Short` | `16.52` | 1,570,000.00 USD | 190.91 USD | 0.00 USD | `+94.48%` | `11.56` |
| `Live` | `Short` | `16.64` | 1,600,000.00 USD | 24,390.00 USD | 0.00 USD | `+95.89%` | `1,466.36` |
| `Live` | `Short` | `16.91` | 1,680,000.00 USD | 85,210.00 USD | 0.00 USD | `+99.19%` | `5,037.66` |
| `Live` | `Short` | `16.98` | 1,680,000.00 USD | 1,690.00 USD | 0.00 USD | `+100.01%` | `99.50` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 372,040.00 USD | 0.00 USD | 611.73 USD | `-72.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 371,430.00 USD | 0.00 USD | 793.75 USD | `-52.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 370,640.00 USD | 0.00 USD | 67,970.00 USD | `-41.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 302,670.00 USD | 0.00 USD | 205.30 USD | `-37.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 302,460.00 USD | 0.00 USD | 465.42 USD | `-35.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 302,000.00 USD | 0.00 USD | 349.35 USD | `-35.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 301,650.00 USD | 0.00 USD | 1,020.00 USD | `-34.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 300,630.00 USD | 0.00 USD | 1,330.00 USD | `-31.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 299,300.00 USD | 0.00 USD | 493.50 USD | `-30.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 298,810.00 USD | 0.00 USD | 100.98 USD | `-29.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 298,710.00 USD | 0.00 USD | 500.70 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 298,210.00 USD | 0.00 USD | 4,160.00 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 294,050.00 USD | 0.00 USD | 6,500.00 USD | `-27.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 287,550.00 USD | 0.00 USD | 906.18 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 286,650.00 USD | 0.00 USD | 127.35 USD | `-26.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 286,520.00 USD | 0.00 USD | 864.38 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 285,650.00 USD | 0.00 USD | 130.10 USD | `-23.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 285,520.00 USD | 0.00 USD | 4,340.00 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 281,180.00 USD | 0.00 USD | 5,520.00 USD | `-21.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 275,660.00 USD | 0.00 USD | 203.67 USD | `-20.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 275,460.00 USD | 0.00 USD | 296.34 USD | `-20.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 275,160.00 USD | 0.00 USD | 921.19 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 274,240.00 USD | 0.00 USD | 709.98 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 273,530.00 USD | 0.00 USD | 4,630.00 USD | `-18.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 268,900.00 USD | 0.00 USD | 691.50 USD | `-18.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 268,210.00 USD | 0.00 USD | 262.44 USD | `-17.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 267,950.00 USD | 0.00 USD | 24,350.00 USD | `-17.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 243,600.00 USD | 0.00 USD | 653.69 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 242,940.00 USD | 0.00 USD | 187.79 USD | `-16.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 242,760.00 USD | 0.00 USD | 6,790.00 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 235,970.00 USD | 0.00 USD | 4,960.00 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 231,010.00 USD | 0.00 USD | 7,210.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 223,800.00 USD | 0.00 USD | 282.74 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 223,520.00 USD | 0.00 USD | 603.44 USD | `-14.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 222,920.00 USD | 0.00 USD | 464.61 USD | `-14.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 222,450.00 USD | 0.00 USD | 2,090.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 220,360.00 USD | 0.00 USD | 129.58 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 220,230.00 USD | 0.00 USD | 114.65 USD | `-13.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 220,110.00 USD | 0.00 USD | 702.75 USD | `-12.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 219,410.00 USD | 0.00 USD | 4,630.00 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 214,780.00 USD | 0.00 USD | 199.39 USD | `-12.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 214,580.00 USD | 0.00 USD | 6,270.00 USD | `-11.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 208,310.00 USD | 0.00 USD | 37,420.00 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 170,890.00 USD | 0.00 USD | 2,120.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 168,770.00 USD | 0.00 USD | 799.83 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 167,970.00 USD | 0.00 USD | 820.44 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 167,150.00 USD | 0.00 USD | 218.24 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 166,930.00 USD | 0.00 USD | 113.78 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 166,810.00 USD | 0.00 USD | 152.10 USD | `-10.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 166,660.00 USD | 0.00 USD | 297.59 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 166,360.00 USD | 0.00 USD | 528.88 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 165,830.00 USD | 0.00 USD | 360.13 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 165,470.00 USD | 0.00 USD | 578.04 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 164,900.00 USD | 0.00 USD | 424.05 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 164,470.00 USD | 0.00 USD | 1,170.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 163,300.00 USD | 0.00 USD | 3,940.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 159,360.00 USD | 0.00 USD | 154.70 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 159,210.00 USD | 0.00 USD | 115.23 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 159,090.00 USD | 0.00 USD | 183.33 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 158,910.00 USD | 0.00 USD | 1,890.00 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 157,010.00 USD | 0.00 USD | 6,840.00 USD | `-6.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 150,180.00 USD | 0.00 USD | 5,710.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 144,470.00 USD | 0.00 USD | 1,590.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 142,880.00 USD | 0.00 USD | 898.42 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 141,980.00 USD | 0.00 USD | 7,960.00 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 134,030.00 USD | 0.00 USD | 246.52 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 133,780.00 USD | 0.00 USD | 1,440.00 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 132,350.00 USD | 0.00 USD | 435.73 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 131,910.00 USD | 0.00 USD | 4,210.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 127,700.00 USD | 0.00 USD | 123.58 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 127,580.00 USD | 0.00 USD | 796.62 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 126,780.00 USD | 0.00 USD | 152.56 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 126,630.00 USD | 0.00 USD | 2,730.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 123,900.00 USD | 0.00 USD | 121.69 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 123,780.00 USD | 0.00 USD | 5,230.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 118,540.00 USD | 0.00 USD | 477.36 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 118,070.00 USD | 0.00 USD | 924.78 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 117,140.00 USD | 0.00 USD | 744.88 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 116,400.00 USD | 0.00 USD | 6,500.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 109,900.00 USD | 0.00 USD | 884.60 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 109,010.00 USD | 0.00 USD | 5,550.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 103,460.00 USD | 0.00 USD | 1,420.00 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 102,040.00 USD | 0.00 USD | 3,080.00 USD | `-3.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 98,950.00 USD | 0.00 USD | 520.75 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 98,430.00 USD | 0.00 USD | 3,020.00 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 95,410.00 USD | 0.00 USD | 141.04 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 95,270.00 USD | 0.00 USD | 22,560.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 72,710.00 USD | 0.00 USD | 515.66 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 72,190.00 USD | 0.00 USD | 139.74 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 72,050.00 USD | 0.00 USD | 490.15 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 71,560.00 USD | 0.00 USD | 197.96 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 71,360.00 USD | 0.00 USD | 9,110.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 62,250.00 USD | 0.00 USD | 535.65 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 61,710.00 USD | 0.00 USD | 734.99 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 60,980.00 USD | 0.00 USD | 2,360.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 58,610.00 USD | 0.00 USD | 311.97 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 58,300.00 USD | 0.00 USD | 15,070.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 43,230.00 USD | 0.00 USD | 245.13 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 42,990.00 USD | 0.00 USD | 1,690.00 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 41,290.00 USD | 0.00 USD | 408.58 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 40,890.00 USD | 0.00 USD | 808.63 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 40,080.00 USD | 0.00 USD | 4,070.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 36,010.00 USD | 0.00 USD | 24,090.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 11,920.00 USD | 0.00 USD | 503.59 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 11,410.00 USD | 0.00 USD | 419.25 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 10,990.00 USD | 0.00 USD | 1,970.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 9,030.00 USD | 0.00 USD | 4,240.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 4,790.00 USD | 0.00 USD | 314.81 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 4,470.00 USD | 0.00 USD | 1,880.00 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 2,590.00 USD | 0.00 USD | 195.52 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 2,400.00 USD | 0.00 USD | 138.24 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 2,260.00 USD | 0.00 USD | 710.81 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 1,550.00 USD | 0.00 USD | 769.61 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 777.14 USD | 0.00 USD | 777.14 USD | `-0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 408.78 USD | 408.78 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 17,420.00 USD | 17,010.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 17,830.00 USD | 408.55 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 18,950.00 USD | 1,130.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 19,240.00 USD | 290.10 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 23,650.00 USD | 4,400.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 33,640.00 USD | 9,990.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 35,230.00 USD | 1,600.00 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 35,800.00 USD | 566.55 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 35,940.00 USD | 143.28 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 38,130.00 USD | 2,180.00 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 38,880.00 USD | 751.56 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 43,080.00 USD | 4,200.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 43,190.00 USD | 107.47 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 43,390.00 USD | 201.97 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 45,270.00 USD | 1,880.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 45,940.00 USD | 673.62 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 46,140.00 USD | 200.85 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 46,320.00 USD | 176.62 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 47,310.00 USD | 990.09 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 47,730.00 USD | 420.32 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 48,300.00 USD | 575.14 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 48,700.00 USD | 399.67 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 49,130.00 USD | 421.85 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 49,460.00 USD | 333.07 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 53,830.00 USD | 4,370.00 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 57,570.00 USD | 3,740.00 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 57,750.00 USD | 173.28 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 57,960.00 USD | 215.16 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 58,350.00 USD | 388.12 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 59,060.00 USD | 711.78 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 78,870.00 USD | 19,810.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 80,900.00 USD | 2,030.00 USD | 0.00 USD | `+3.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 81,140.00 USD | 243.40 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 81,310.00 USD | 168.05 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 81,650.00 USD | 339.94 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 81,810.00 USD | 163.91 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 81,930.00 USD | 110.58 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 82,790.00 USD | 860.96 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 84,720.00 USD | 1,930.00 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 85,510.00 USD | 788.72 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 87,310.00 USD | 1,800.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 87,480.00 USD | 163.33 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 88,260.00 USD | 782.17 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 88,480.00 USD | 223.62 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 625,790.00 USD | 537,310.00 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 626,190.00 USD | 401.63 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 941,340.00 USD | 315,150.00 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 941,680.00 USD | 338.30 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 941,940.00 USD | 260.96 USD | 0.00 USD | `+6.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 943,320.00 USD | 1,380.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 944,410.00 USD | 1,090.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 945,020.00 USD | 616.37 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 945,130.00 USD | 102.03 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 945,580.00 USD | 453.84 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 945,740.00 USD | 160.99 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 945,960.00 USD | 215.98 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 947,470.00 USD | 1,510.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 947,920.00 USD | 451.48 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 948,060.00 USD | 139.58 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 949,350.00 USD | 1,290.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 949,510.00 USD | 166.53 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 951,510.00 USD | 2,000.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,350,000.00 USD | 394,210.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,350,000.00 USD | 119.24 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,350,000.00 USD | 3,020.00 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,350,000.00 USD | 131.87 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,350,000.00 USD | 149.17 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,350,000.00 USD | 2,220.00 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,580,000.00 USD | 231,380.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,580,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,590,000.00 USD | 434.45 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,600,000.00 USD | 18,610.00 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,600,000.00 USD | 166.83 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,600,000.00 USD | 674.29 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,600,000.00 USD | 101.58 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,600,000.00 USD | 109.36 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,600,000.00 USD | 116.69 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,610,000.00 USD | 163.41 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,610,000.00 USD | 102.01 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,610,000.00 USD | 102.12 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,610,000.00 USD | 714.59 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,610,000.00 USD | 928.13 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,610,000.00 USD | 102.45 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,610,000.00 USD | 219.84 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,610,000.00 USD | 1,890.00 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,610,000.00 USD | 1,130.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,610,000.00 USD | 288.46 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,610,000.00 USD | 119.92 USD | 0.00 USD | `+12.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,610,000.00 USD | 231.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,610,000.00 USD | 221.07 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,610,000.00 USD | 992.00 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,610,000.00 USD | 148.48 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,610,000.00 USD | 191.36 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,620,000.00 USD | 4,440.00 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,620,000.00 USD | 108.21 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,620,000.00 USD | 169.68 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,620,000.00 USD | 574.66 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,620,000.00 USD | 121.87 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,620,000.00 USD | 115.88 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,620,000.00 USD | 340.05 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,620,000.00 USD | 742.12 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,620,000.00 USD | 899.47 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,690,000.00 USD | 70,020.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,690,000.00 USD | 373.97 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,700,000.00 USD | 5,050.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,700,000.00 USD | 6,370.00 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,700,000.00 USD | 404.20 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 1,150.00 USD | 0.00 USD | `+19.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,910,000.00 USD | 172.16 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,920,000.00 USD | 922.87 USD | 0.00 USD | `+21.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,920,000.00 USD | 489.40 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,920,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,920,000.00 USD | 118.01 USD | 0.00 USD | `+22.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,920,000.00 USD | 971.48 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,920,000.00 USD | 818.31 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,920,000.00 USD | 312.31 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,920,000.00 USD | 2,290.00 USD | 0.00 USD | `+23.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,920,000.00 USD | 1,890.00 USD | 0.00 USD | `+23.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,920,000.00 USD | 178.46 USD | 0.00 USD | `+24.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,920,000.00 USD | 173.42 USD | 0.00 USD | `+26.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,920,000.00 USD | 184.75 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,920,000.00 USD | 135.78 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,920,000.00 USD | 127.96 USD | 0.00 USD | `+27.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,920,000.00 USD | 476.43 USD | 0.00 USD | `+28.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,930,000.00 USD | 869.35 USD | 0.00 USD | `+28.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,960,000.00 USD | 35,110.00 USD | 0.00 USD | `+28.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,960,000.00 USD | 251.06 USD | 0.00 USD | `+28.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,960,000.00 USD | 552.44 USD | 0.00 USD | `+28.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,960,000.00 USD | 537.26 USD | 0.00 USD | `+29.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,960,000.00 USD | 1,110.00 USD | 0.00 USD | `+30.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,960,000.00 USD | 320.29 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,960,000.00 USD | 1,100.00 USD | 0.00 USD | `+31.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,970,000.00 USD | 2,270.00 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,970,000.00 USD | 1,270.00 USD | 0.00 USD | `+32.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,970,000.00 USD | 1,380.00 USD | 0.00 USD | `+33.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,970,000.00 USD | 2,410.00 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,980,000.00 USD | 9,520.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,980,000.00 USD | 2,050.00 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,980,000.00 USD | 529.11 USD | 0.00 USD | `+35.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,990,000.00 USD | 7,700.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,990,000.00 USD | 906.03 USD | 0.00 USD | `+39.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,990,000.00 USD | 434.61 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,990,000.00 USD | 163.52 USD | 0.00 USD | `+39.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,000,000.00 USD | 10,370.00 USD | 0.00 USD | `+41.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 2,010,000.00 USD | 5,270.00 USD | 0.00 USD | `+43.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 2,010,000.00 USD | 115.02 USD | 0.00 USD | `+44.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,010,000.00 USD | 3,870.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,010,000.00 USD | 197.97 USD | 0.00 USD | `+50.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,020,000.00 USD | 3,200.00 USD | 0.00 USD | `+51.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,020,000.00 USD | 179.58 USD | 0.00 USD | `+52.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,020,000.00 USD | 568.45 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,020,000.00 USD | 169.57 USD | 0.00 USD | `+54.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,020,000.00 USD | 446.52 USD | 0.00 USD | `+57.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,020,000.00 USD | 5,320.00 USD | 0.00 USD | `+58.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,230,000.00 USD | 210,750.00 USD | 0.00 USD | `+59.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,230,000.00 USD | 407.95 USD | 0.00 USD | `+61.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,230,000.00 USD | 174.91 USD | 0.00 USD | `+62.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,240,000.00 USD | 4,680.00 USD | 0.00 USD | `+64.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,240,000.00 USD | 960.26 USD | 0.00 USD | `+67.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,240,000.00 USD | 2,710.00 USD | 0.00 USD | `+69.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,240,000.00 USD | 805.90 USD | 0.00 USD | `+70.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,240,000.00 USD | 655.55 USD | 0.00 USD | `+73.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,250,000.00 USD | 4,890.00 USD | 0.00 USD | `+74.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,250,000.00 USD | 471.09 USD | 0.00 USD | `+75.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,250,000.00 USD | 383.85 USD | 0.00 USD | `+76.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,900,000.00 USD | 654,840.00 USD | 0.00 USD | `+76.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,910,000.00 USD | 1,510.00 USD | 0.00 USD | `+77.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,910,000.00 USD | 111.87 USD | 0.00 USD | `+86.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,910,000.00 USD | 219.91 USD | 0.00 USD | `+88.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,910,000.00 USD | 121.74 USD | 0.00 USD | `+99.66%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.14` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,320.00 USD |
| `7D` | `7.16` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,980.00 USD |
| `7D` | `7.18` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,650.00 USD |
| `7D` | `7.20` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,050.00 USD |
| `7D` | `7.22` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,980.00 USD |
| `7D` | `7.24` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 39,910.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `7.26` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 0.00 USD | 1,810.00 USD | 58.08 USD |
| `7D` | `7.28` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.30` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `7.32` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 5,740.00 USD |
| `7D` | `7.36` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 983.83 USD | 0.00 USD | 864.67 USD |
| `7D` | `7.38` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 46,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.40` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 44,790.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.46` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.48` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.52` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `7.56` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.59` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 1,740.00 USD | 0.00 USD | 7,670.00 USD |
| `1D` | `7.60` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD |
| `7D` | `7.60` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.61` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 1,190.00 USD | 761.26 USD | 11,670.00 USD |
| `1D` | `7.62` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 956.60 USD | 0.00 USD | 133.28 USD |
| `7D` | `7.62` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 0.00 USD | 2,130.00 USD | 996.08 USD |
| `1D` | `7.63` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 1,040.00 USD | 0.00 USD | 8,000.00 USD |
| `1D` | `7.64` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD |
| `7D` | `7.64` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 41,300.00 USD | 0.00 USD | 686.63 USD |
| `1D` | `7.65` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 0.00 USD | 817.75 USD | 9,870.00 USD |
| `1D` | `7.66` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `7D` | `7.66` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,600.00 USD |
| `1D` | `7.67` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 1,140.00 USD | 587.20 USD | 114.38 USD |
| `1D` | `7.68` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `7.68` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `7.69` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `7.70` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 4,140.00 USD | 2,390.00 USD | 16,770.00 USD |
| `7D` | `7.70` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 393.33 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.71` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD |
| `1D` | `7.72` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 701.68 USD | 568.00 USD | 2,430.00 USD |
| `7D` | `7.72` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 38,970.00 USD | 0.00 USD | 40,470.00 USD |
| `1D` | `7.73` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `7.74` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `7D` | `7.74` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `1D` | `7.76` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD |
| `7D` | `7.76` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 812.95 USD | 13,360.00 USD | 11,180.00 USD |
| `1D` | `7.77` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD |
| `1D` | `7.78` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `7D` | `7.78` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,810.00 USD |
| `1D` | `7.79` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 18,980.00 USD | 2,920.00 USD | 7,250.00 USD |
| `1D` | `7.80` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 9,300.00 USD | 8,720.00 USD | 2,270.00 USD |
| `7D` | `7.80` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,770.00 USD |
| `1D` | `7.81` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 349.70 USD | 728.43 USD | 0.00 USD |
| `1D` | `7.82` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 2,250.00 USD | 2,530.00 USD | 0.00 USD |
| `7D` | `7.82` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,710.00 USD |
| `1D` | `7.83` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD |
| `1D` | `7.84` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 1,060.00 USD | 1,800.00 USD | 10.76 USD |
| `7D` | `7.84` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 32,340.00 USD | 2,380.00 USD | 25,450.00 USD |
| `1D` | `7.85` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,650.00 USD |
| `1D` | `7.86` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 5,060.00 USD | 6,690.00 USD | 17,220.00 USD |
| `7D` | `7.86` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 137,360.00 USD | 5,460.00 USD | 18,470.00 USD |
| `1D` | `7.87` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 13,800.00 USD | 10,860.00 USD | 24,540.00 USD |
| `1D` | `7.88` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 161,620.00 USD | 5,890.00 USD | 34,820.00 USD |
| `7D` | `7.88` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 170,100.00 USD | 12,780.00 USD | 30,610.00 USD |
| `1D` | `7.89` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD |
| `1D` | `7.90` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 56,130.00 USD | 6,970.00 USD | 5,990.00 USD |
| `7D` | `7.90` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,230.00 USD |
| `1D` | `7.91` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD |
| `1D` | `7.92` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,760.00 USD |
| `7D` | `7.92` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 55,490.00 USD | 23,630.00 USD | 41,800.00 USD |
| `1D` | `7.93` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `1D` | `7.94` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD |
| `7D` | `7.94` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 51,390.00 USD | 9,960.00 USD | 31,670.00 USD |
| `1D` | `7.95` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD |
| `1D` | `7.96` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `7D` | `7.96` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,430.00 USD |
| `1D` | `7.97` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `1D` | `7.98` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD |
| `7D` | `7.98` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,450.00 USD |
| `1D` | `7.99` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD |
| `1D` | `8.00` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `7D` | `8.00` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,130.00 USD |
| `1D` | `8.01` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD |
| `1D` | `8.02` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD |
| `7D` | `8.02` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 15,300.00 USD | 46,670.00 USD | 58,100.00 USD |
| `1D` | `8.03` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 9,010.00 USD | 12,540.00 USD | 12,890.00 USD |
| `1D` | `8.04` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `8.04` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 460,990.00 USD | 0.00 USD | 86,550.00 USD |
| `1D` | `8.05` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 317,940.00 USD | 6,430.00 USD | 53,960.00 USD |
| `1D` | `8.06` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD |
| `7D` | `8.06` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 336,530.00 USD | 0.00 USD | 86,670.00 USD |
| `1D` | `8.07` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `1D` | `8.08` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `7D` | `8.08` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 5,100.00 USD | 0.00 USD | 73,960.00 USD |
| `1D` | `8.09` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD |
| `1D` | `8.10` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `7D` | `8.10` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 56,590.00 USD | 0.00 USD | 14,820.00 USD |
| `1D` | `8.11` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `1D` | `8.12` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 13,810.00 USD | 10,020.00 USD | 126,250.00 USD |
| `7D` | `8.12` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD |
| `1D` | `8.13` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 6,410.00 USD | 4,510.00 USD | 0.00 USD |
| `1D` | `8.14` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 7,660.00 USD | 101,110.00 USD |
| `7D` | `8.14` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 160,410.00 USD | 30,700.00 USD | 183,790.00 USD |
| `1D` | `8.15` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 40,400.00 USD | 11,230.00 USD | 52,230.00 USD |
| `1D` | `8.16` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 192.50 USD | 21,000.00 USD | 165,460.00 USD |
| `7D` | `8.16` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,310.00 USD |
| `1D` | `8.17` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD |
| `1D` | `8.18` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 7,140.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `8.18` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD |
| `1D` | `8.19` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD |
| `1D` | `8.20` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD |
| `7D` | `8.20` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 174,220.00 USD | 58,100.00 USD | 5,890.00 USD |
| `1D` | `8.21` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD |
| `1D` | `8.22` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD |
| `7D` | `8.22` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `8.23` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD |
| `1D` | `8.24` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 223.44 USD | 3,220.00 USD | 5,970.00 USD |
| `7D` | `8.24` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD |
| `1D` | `8.25` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD |
| `1D` | `8.26` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD |
| `7D` | `8.26` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD |
| `1D` | `8.27` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,140.00 USD |
| `1D` | `8.28` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `7D` | `8.28` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,800.00 USD |
| `1D` | `8.29` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 27,240.00 USD | 9,380.00 USD | 0.00 USD |
| `1D` | `8.30` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 12,270.00 USD | 4,480.00 USD | 16,650.00 USD |
| `7D` | `8.30` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 224,520.00 USD | 17,210.00 USD | 21,020.00 USD |
| `1D` | `8.31` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 47,410.00 USD | 9,970.00 USD | 48,090.00 USD |
| `1D` | `8.32` | 897,820.00 USD | 0.00 USD | 897,820.00 USD | 66,820.00 USD | 4,060.00 USD | 11,190.00 USD |
| `7D` | `8.32` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 220,640.00 USD | 0.00 USD | 5,060.00 USD |
| `1D` | `8.33` | 815,750.00 USD | 0.00 USD | 815,750.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD |
| `1D` | `8.34` | 809,430.00 USD | 0.00 USD | 809,430.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD |
| `7D` | `8.34` | 889,340.00 USD | 0.00 USD | 889,340.00 USD | 0.00 USD | 11,770.00 USD | 4,430.00 USD |
| `1D` | `8.35` | 807,210.00 USD | 0.00 USD | 807,210.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD |
| `1D` | `8.36` | 770,430.00 USD | 0.00 USD | 770,430.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `7D` | `8.36` | 873,150.00 USD | 0.00 USD | 873,150.00 USD | 223,170.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `8.37` | 752,630.00 USD | 0.00 USD | 752,630.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD |
| `1D` | `8.38` | 737,500.00 USD | 0.00 USD | 737,500.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD |
| `7D` | `8.38` | 632,110.00 USD | 0.00 USD | 632,110.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `8.39` | 664,050.00 USD | 0.00 USD | 664,050.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `1D` | `8.40` | 517,080.00 USD | 0.00 USD | 517,080.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD |
| `7D` | `8.40` | 574,370.00 USD | 0.00 USD | 574,370.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD |
| `1D` | `8.41` | 443,000.00 USD | 0.00 USD | 443,000.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD |
| `1D` | `8.42` | 424,610.00 USD | 0.00 USD | 424,610.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `7D` | `8.42` | 479,830.00 USD | 0.00 USD | 479,830.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD |
| `1D` | `8.43` | 365,470.00 USD | 0.00 USD | 365,470.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD |
| `1D` | `8.44` | 268,850.00 USD | 0.00 USD | 268,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD |
| `7D` | `8.44` | 234,850.00 USD | 0.00 USD | 234,850.00 USD | 152,190.00 USD | 8,000.00 USD | 74,660.00 USD |
| `1D` | `8.45` | 64,870.00 USD | 0.00 USD | 64,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `1D` | `8.46` | 4,110.00 USD | 0.00 USD | 4,110.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD |
| `7D` | `8.46` | 272,390.00 USD | 272,390.00 USD | 0.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD |
| `7D` | `8.46` | 544,780.00 USD | 544,780.00 USD | 0.00 USD | 152,650.00 USD | 0.00 USD | 119,740.00 USD |
| `1D` | `8.47` | 663.00 USD | 0.00 USD | 663.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 749.80 USD | 749.80 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 1,500.00 USD | 1,500.00 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.48` | 880,280.00 USD | 880,280.00 USD | 0.00 USD | 144,290.00 USD | 0.00 USD | 191,210.00 USD |
| `1D` | `8.49` | 96,340.00 USD | 96,340.00 USD | 0.00 USD | 94,820.00 USD | 0.00 USD | 12.70 USD |
| `1D` | `8.50` | 223,340.00 USD | 223,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 127,000.00 USD |
| `7D` | `8.50` | 881,750.00 USD | 881,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD |
| `1D` | `8.51` | 395,780.00 USD | 395,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD |
| `1D` | `8.52` | 568,750.00 USD | 568,750.00 USD | 0.00 USD | 168,170.00 USD | 0.00 USD | 4,800.00 USD |
| `7D` | `8.52` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 113,820.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `8.53` | 602,340.00 USD | 602,340.00 USD | 0.00 USD | 33,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.54` | 805,290.00 USD | 805,290.00 USD | 0.00 USD | 202,800.00 USD | 0.00 USD | 156.94 USD |
| `7D` | `8.54` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 357,740.00 USD | 0.00 USD | 1,880.00 USD |
| `1D` | `8.55` | 832,070.00 USD | 832,070.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `1D` | `8.56` | 871,080.00 USD | 871,080.00 USD | 0.00 USD | 686.73 USD | 38,320.00 USD | 0.00 USD |
| `7D` | `8.56` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 144,180.00 USD | 122,650.00 USD | 790.79 USD |
| `1D` | `8.57` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 174,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.58` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.60` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,310.00 USD |
| `1D` | `8.61` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `1D` | `8.62` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD |
| `7D` | `8.62` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.63` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.64` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 12,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.64` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.65` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 342.65 USD | 7,060.00 USD | 8,960.00 USD |
| `1D` | `8.66` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,170.00 USD |
| `7D` | `8.66` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 804.96 USD |
| `1D` | `8.67` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 880.60 USD | 9,960.00 USD | 56.72 USD |
| `1D` | `8.68` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD |
| `7D` | `8.68` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 30,000.00 USD | 117,540.00 USD |
| `1D` | `8.69` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD |
| `1D` | `8.70` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD |
| `7D` | `8.70` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD |
| `7D` | `8.72` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 609.73 USD |
| `1D` | `8.73` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD |
| `1D` | `8.74` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 38,500.00 USD | 3,500.00 USD | 17,580.00 USD |
| `7D` | `8.74` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 51,030.00 USD | 30,470.00 USD | 686.63 USD |
| `1D` | `8.75` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 33,520.00 USD | 8,970.00 USD | 16,930.00 USD |
| `1D` | `8.76` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD |
| `7D` | `8.76` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 196,960.00 USD | 0.00 USD | 58,950.00 USD |
| `1D` | `8.77` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD |
| `1D` | `8.78` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD |
| `7D` | `8.78` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD |
| `1D` | `8.79` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD |
| `1D` | `8.80` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 107,040.00 USD | 17,940.00 USD | 23,840.00 USD |
| `7D` | `8.80` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 32,140.00 USD |
| `1D` | `8.81` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 24,810.00 USD | 4,360.00 USD | 42.52 USD |
| `1D` | `8.82` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 2,200.00 USD | 3,530.00 USD | 57,340.00 USD |
| `7D` | `8.82` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 345,340.00 USD | 18,440.00 USD | 39,280.00 USD |
| `1D` | `8.83` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 168,110.00 USD | 18,390.00 USD | 5,580.00 USD |
| `1D` | `8.84` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 1,500.00 USD | 3,110.00 USD | 66,950.00 USD |
| `7D` | `8.84` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD |
| `1D` | `8.85` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD |
| `1D` | `8.86` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 2,060.00 USD | 1,470.00 USD | 607.55 USD |
| `7D` | `8.86` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 83,000.00 USD |
| `1D` | `8.87` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD | 8,900.00 USD |
| `1D` | `8.88` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD |
| `7D` | `8.88` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 12,390.00 USD | 3,410.00 USD | 32,950.00 USD |
| `1D` | `8.90` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 28,690.00 USD | 5,990.00 USD | 84,550.00 USD |
| `7D` | `8.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 116,250.00 USD |
| `1D` | `8.91` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD |
| `1D` | `8.92` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 1,110.00 USD | 3,220.00 USD | 6,040.00 USD |
| `7D` | `8.92` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD |
| `1D` | `8.93` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD |
| `1D` | `8.94` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD |
| `7D` | `8.94` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 129,180.00 USD | 0.00 USD | 11,850.00 USD |
| `1D` | `8.95` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 2,540.00 USD | 6,630.00 USD | 20,340.00 USD |
| `1D` | `8.96` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD |
| `7D` | `8.96` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 3,320.00 USD | 4,000.00 USD | 26,700.00 USD |
| `1D` | `8.98` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD |
| `1D` | `9.00` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD |
| `7D` | `9.00` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 370,780.00 USD | 17,920.00 USD | 41,010.00 USD |
| `1D` | `9.01` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD |
| `1D` | `9.02` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 39,120.00 USD | 31,460.00 USD | 5,010.00 USD |
| `7D` | `9.02` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 82,280.00 USD | 56,120.00 USD | 1,780.00 USD |
| `1D` | `9.03` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 125,760.00 USD | 12,800.00 USD | 34,410.00 USD |
| `1D` | `9.04` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 41,220.00 USD | 8,870.00 USD | 14,800.00 USD |
| `7D` | `9.04` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 136,520.00 USD | 74,750.00 USD | 16,220.00 USD |
| `1D` | `9.05` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 21,980.00 USD | 11,560.00 USD | 24,060.00 USD |
| `1D` | `9.06` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 28,180.00 USD | 6,890.00 USD | 10,490.00 USD |
| `7D` | `9.06` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,420.00 USD |
| `1D` | `9.07` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 13,070.00 USD | 18,070.00 USD | 28,510.00 USD |
| `1D` | `9.08` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 12,960.00 USD | 2,110.00 USD | 33,970.00 USD |
| `7D` | `9.08` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,080.00 USD |
| `1D` | `9.09` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 84,640.00 USD | 11,440.00 USD | 29,380.00 USD |
| `1D` | `9.10` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 16,380.00 USD | 16,280.00 USD | 36,950.00 USD |
| `7D` | `9.10` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,610.00 USD |
| `1D` | `9.11` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD |
| `1D` | `9.12` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 102,100.00 USD | 22,410.00 USD | 26,360.00 USD |
| `7D` | `9.12` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.13` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 75,260.00 USD | 15,960.00 USD | 40,180.00 USD |
| `1D` | `9.14` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD |
| `7D` | `9.14` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,290.00 USD |
| `1D` | `9.15` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 57,140.00 USD | 23,170.00 USD | 23,060.00 USD |
| `1D` | `9.16` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `7D` | `9.16` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 196,240.00 USD |
| `1D` | `9.17` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 80,620.00 USD | 3,200.00 USD | 49,540.00 USD |
| `1D` | `9.18` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 28,620.00 USD | 26,430.00 USD | 31,220.00 USD |
| `7D` | `9.18` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 566,340.00 USD | 162,460.00 USD | 292,040.00 USD |
| `1D` | `9.19` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 78,040.00 USD | 29,140.00 USD | 7,680.00 USD |
| `1D` | `9.20` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD |
| `7D` | `9.20` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 550,150.00 USD | 134,550.00 USD | 238,840.00 USD |
| `1D` | `9.21` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD |
| `1D` | `9.22` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 620,010.00 USD | 144,840.00 USD | 376,830.00 USD |
| `1D` | `9.23` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD |
| `1D` | `9.24` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 45,960.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `9.24` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 336,360.00 USD | 44,660.00 USD | 136,520.00 USD |
| `1D` | `9.25` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 17,280.00 USD | 5,840.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD |
| `7D` | `9.26` | 12,780,000.00 USD | 12,780,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 19,160.00 USD |
| `1D` | `9.27` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 23,580.00 USD | 1,360.00 USD | 6,640.00 USD |
| `1D` | `9.28` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD |
| `7D` | `9.28` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 428,160.00 USD | 78,420.00 USD | 154,030.00 USD |
| `1D` | `9.29` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD |
| `1D` | `9.30` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 39,850.00 USD | 7,520.00 USD | 11,600.00 USD |
| `7D` | `9.30` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 262,830.00 USD |
| `1D` | `9.31` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 27,750.00 USD | 5,020.00 USD | 12,920.00 USD |
| `1D` | `9.32` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 9,650.00 USD | 0.00 USD | 5,070.00 USD |
| `7D` | `9.32` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 241,960.00 USD | 51,970.00 USD | 309,560.00 USD |
| `1D` | `9.33` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 8,050.00 USD | 6,000.00 USD | 8,120.00 USD |
| `1D` | `9.34` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 46,210.00 USD | 3,660.00 USD | 5,580.00 USD |
| `7D` | `9.34` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 98,640.00 USD | 41,250.00 USD | 59,540.00 USD |
| `1D` | `9.35` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 13,620.00 USD | 817.75 USD | 14,910.00 USD |
| `1D` | `9.36` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `7D` | `9.36` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 215,620.00 USD | 64,120.00 USD | 97,710.00 USD |
| `1D` | `9.37` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 12,900.00 USD | 6,260.00 USD | 2,720.00 USD |
| `1D` | `9.38` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 13,850.00 USD |
| `7D` | `9.38` | 15,510,000.00 USD | 15,510,000.00 USD | 0.00 USD | 224,850.00 USD | 31,100.00 USD | 77,300.00 USD |
| `1D` | `9.39` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 9,080.00 USD | 1,600.00 USD | 12.70 USD |
| `1D` | `9.40` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD |
| `7D` | `9.40` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 105,030.00 USD |
| `1D` | `9.41` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD | 10,140.00 USD |
| `1D` | `9.42` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 9,240.00 USD | 2,390.00 USD | 6,520.00 USD |
| `7D` | `9.42` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 109,230.00 USD | 13,910.00 USD | 51,440.00 USD |
| `1D` | `9.43` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD |
| `1D` | `9.44` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 795.69 USD | 568.00 USD | 2,430.00 USD |
| `7D` | `9.44` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 80,230.00 USD | 19,420.00 USD | 43,220.00 USD |
| `1D` | `9.45` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `9.46` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.46` | 16,310,000.00 USD | 16,310,000.00 USD | 0.00 USD | 89,160.00 USD | 4,480.00 USD | 11,020.00 USD |
| `1D` | `9.47` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD |
| `1D` | `9.48` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 309.05 USD | 494.12 USD | 0.00 USD |
| `7D` | `9.48` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 10,620.00 USD | 11,060.00 USD | 35,620.00 USD |
| `1D` | `9.49` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 9,940.00 USD | 689.91 USD | 3,430.00 USD |
| `1D` | `9.50` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.50` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 65,230.00 USD | 12,050.00 USD | 52,470.00 USD |
| `1D` | `9.51` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 295.05 USD | 0.00 USD | 124.70 USD |
| `1D` | `9.52` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,660.00 USD |
| `7D` | `9.52` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 57,650.00 USD | 18,520.00 USD | 31,860.00 USD |
| `1D` | `9.53` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 18,960.00 USD | 2,920.00 USD | 0.00 USD |
| `1D` | `9.54` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 4,350.00 USD | 806.35 USD | 1,560.00 USD |
| `7D` | `9.54` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 13,190.00 USD | 13,310.00 USD | 930.52 USD |
| `7D` | `9.56` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 7,430.00 USD | 5,260.00 USD | 4,800.00 USD |
| `7D` | `9.58` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 35,340.00 USD | 2,380.00 USD | 27,300.00 USD |
| `7D` | `9.60` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 31,720.00 USD | 5,460.00 USD | 18,390.00 USD |
| `7D` | `9.62` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `352.36M` | Total OI Tokens: `41,613,283.4 AVAX`
  * 1h OI Change: `-0.57%` | 4h OI Change: `-0.89%` | 24h OI Change: `-6.84%`
  * Exchange Breakdown: Binance=`80.02M` | Bybit=`57.33M` | OKX=`11.54M` | Hyperliquid=`16.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.03K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0086%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0067%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `41.24%` | `58.76%` | `0.70` | 5,380,000.00 USD |
| `15M` | `Binance` | `48.77%` | `51.23%` | `0.95` | 1,370,000.00 USD |
| `15M` | `OKX` | `38.97%` | `61.03%` | `0.64` | 276,400.00 USD |
| `15M` | `Bybit` | `44.11%` | `55.89%` | `0.79` | 280,050.00 USD |
| `15M` | `KuCoin` | `47.77%` | `52.23%` | `0.91` | 14,910.00 USD |
| `15M` | `Gate` | `66.53%` | `33.47%` | `1.99` | 55,310.00 USD |
| `15M` | `Bitget` | `44.7%` | `55.3%` | `0.81` | 95,050.00 USD |
| `15M` | `BingX` | `9.22%` | `90.78%` | `0.10` | 619,130.00 USD |
| `15M` | `MEXC` | `49.86%` | `50.14%` | `0.99` | 1,360,000.00 USD |
| `15M` | `Bitunix` | `67.85%` | `32.15%` | `2.11` | 147,990.00 USD |
| `15M` | `Hyperliquid` | `67.39%` | `32.61%` | `2.07` | 126,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.74%` | `50.26%` | `0.99` | 570,600.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.09%` | `99.91%` | `0.00` | 423,910.00 USD |
| `15M` | `HTX` | `72.71%` | `27.29%` | `2.66` | 22,060.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `73.05%` | `26.95%` | `2.71` | 7,240.00 USD |
| `15M` | `Aster` | `49.43%` | `50.57%` | `0.98` | 4,560.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.93%` | `2.07%` | `47.31` | 4,250.00 USD |
| `15M` | `Whale Positions` | `48.77%` | `51.23%` | `0.95` | 1,370,000.00 USD |
| `15M` | `Global Accounts` | `41.24%` | `58.76%` | `0.70` | 5,380,000.00 USD |
| `1H` | `AVAX` | `44.24%` | `55.76%` | `0.79` | 21,110,000.00 USD |
| `1H` | `Binance` | `45.81%` | `54.19%` | `0.85` | 8,230,000.00 USD |
| `1H` | `OKX` | `42.69%` | `57.31%` | `0.74` | 1,530,000.00 USD |
| `1H` | `Bybit` | `49.37%` | `50.63%` | `0.98` | 1,410,000.00 USD |
| `1H` | `KuCoin` | `60.14%` | `39.86%` | `1.51` | 112,860.00 USD |
| `1H` | `Gate` | `42.22%` | `57.78%` | `0.73` | 338,650.00 USD |
| `1H` | `Bitget` | `45.19%` | `54.81%` | `0.82` | 597,930.00 USD |
| `1H` | `BingX` | `29.27%` | `70.73%` | `0.41` | 1,350,000.00 USD |
| `1H` | `MEXC` | `47.99%` | `52.01%` | `0.92` | 3,780,000.00 USD |
| `1H` | `Bitunix` | `49.6%` | `50.4%` | `0.98` | 1,380,000.00 USD |
| `1H` | `Hyperliquid` | `49.08%` | `50.92%` | `0.96` | 367,700.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.12%` | `49.88%` | `1.00` | 945,710.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `6.62%` | `93.38%` | `0.07` | 863,460.00 USD |
| `1H` | `HTX` | `41.09%` | `58.91%` | `0.70` | 52,030.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `76.99%` | `23.01%` | `3.35` | 38,100.00 USD |
| `1H` | `Aster` | `79.78%` | `20.22%` | `3.95` | 74,940.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.44%` | `45.56%` | `1.19` | 49,590.00 USD |
| `1H` | `Whale Positions` | `45.81%` | `54.19%` | `0.85` | 8,230,000.00 USD |
| `1H` | `Global Accounts` | `44.24%` | `55.76%` | `0.79` | 21,110,000.00 USD |
| `4H` | `AVAX` | `45.56%` | `54.44%` | `0.84` | 75,630,000.00 USD |
| `4H` | `Binance` | `50.01%` | `49.99%` | `1.00` | 24,520,000.00 USD |
| `4H` | `OKX` | `49.17%` | `50.83%` | `0.97` | 6,280,000.00 USD |
| `4H` | `Bybit` | `51.36%` | `48.64%` | `1.06` | 7,210,000.00 USD |
| `4H` | `KuCoin` | `49.73%` | `50.27%` | `0.99` | 1,030,000.00 USD |
| `4H` | `Gate` | `49.64%` | `50.36%` | `0.99` | 1,940,000.00 USD |
| `4H` | `Bitget` | `41.21%` | `58.79%` | `0.70` | 2,550,000.00 USD |
| `4H` | `BingX` | `28.85%` | `71.15%` | `0.41` | 10,580,000.00 USD |
| `4H` | `MEXC` | `48.01%` | `51.99%` | `0.92` | 5,590,000.00 USD |
| `4H` | `Bitunix` | `46.33%` | `53.67%` | `0.86` | 1,850,000.00 USD |
| `4H` | `Hyperliquid` | `36.72%` | `63.28%` | `0.58` | 629,610.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.9%` | `49.1%` | `1.04` | 11,240,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `3.31%` | `96.69%` | `0.03` | 1,680,000.00 USD |
| `4H` | `HTX` | `57.09%` | `42.91%` | `1.33` | 336,330.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.99%` | `55.01%` | `0.82` | 125,020.00 USD |
| `4H` | `Aster` | `24.9%` | `75.1%` | `0.33` | 33,140.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `61.08%` | `38.92%` | `1.57` | 27,390.00 USD |
| `4H` | `Whale Positions` | `50.01%` | `49.99%` | `1.00` | 24,520,000.00 USD |
| `4H` | `Global Accounts` | `45.56%` | `54.44%` | `0.84` | 75,630,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.66` | `8.65` | `8.66` | `8.68` | `8.62` | 1,979,129.83 USD | 1,356,800.37 USD | 622,329.46 USD | 734,470.91 USD | `+37.11%` | `18B / 5S` |
| `5:00 UTC` | `8.62` | `8.61` | `8.62` | `8.64` | `8.58` | 677,702.04 USD | 366,387.84 USD | 311,314.20 USD | 55,073.64 USD | `+8.13%` | `8B / 8S` |
| `0:00 UTC` | `8.60` | `8.60` | `8.60` | `8.63` | `8.58` | 929,414.14 USD | 426,619.56 USD | 502,794.57 USD | -76,175.01 USD | `-8.20%` | `4B / 10S` |
| `5:00 UTC` | `8.57` | `8.57` | `8.57` | `8.60` | `8.56` | 1,552,705.44 USD | 422,695.37 USD | 1,130,010.07 USD | -707,314.70 USD | `-45.55%` | `6B / 15S` |
| `0:00 UTC` | `8.56` | `8.56` | `8.56` | `8.62` | `8.50` | 1,991,917.42 USD | 805,962.82 USD | 1,185,954.60 USD | -379,991.79 USD | `-19.08%` | `9B / 38S` |
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.55` | `8.48` | 1,276,824.26 USD | 505,302.94 USD | 771,521.32 USD | -266,218.38 USD | `-20.85%` | `4B / 18S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.52` | `8.45` | 1,829,814.14 USD | 869,168.19 USD | 960,645.95 USD | -91,477.76 USD | `-5.00%` | `11B / 14S` |
| `5:00 UTC` | `8.51` | `8.50` | `8.51` | `8.52` | `8.48` | 752,301.06 USD | 385,792.91 USD | 366,508.15 USD | 19,284.76 USD | `+2.56%` | `8B / 9S` |
| `0:00 UTC` | `8.46` | `8.47` | `8.46` | `8.49` | `8.46` | 681,089.39 USD | 260,569.06 USD | 420,520.33 USD | -159,951.27 USD | `-23.48%` | `1B / 5S` |
| `5:00 UTC` | `8.46` | `8.46` | `8.46` | `8.46` | `8.45` | 88,270.69 USD | 39,225.33 USD | 49,045.36 USD | -9,820.02 USD | `-11.12%` | `1B / 2S` |

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
| `5m` | -59,440.00 USD | -75,310.00 USD | **`DISTRIBUTION`** |
| `15m` | -100,650.00 USD | -245,070.00 USD | **`DISTRIBUTION`** |
| `30m` | -171,410.00 USD | -34,260.00 USD | **`DISTRIBUTION`** |
| `1h` | -299,670.00 USD | -1,170,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -361,870.00 USD | -2,520,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,960.00 USD | -1,780,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 73,020.00 USD | -557,830.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,860.00 USD | -2,880,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,220,000.00 USD | -8,500,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,840,000.00 USD | -12,290,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,610,000.00 USD | -53,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,610,000.00 USD | -265,590,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-59.44K` | 15m=`-100.65K` | 1h=`-299.67K` | 24h=`-2.84M`
* Futures Capital Netflows: 5m=`-75.31K` | 15m=`-245.07K` | 1h=`-1.17M` | 24h=`-12.29M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.03` (Risk Distance: `0.1393` pts)
  * +2.5R Take Profit: `8.52`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.67` (Risk Distance: `0.1393` pts)
  * +2.5R Take Profit: `8.18`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.52`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
