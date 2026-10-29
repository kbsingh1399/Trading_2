# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:36:43 IST` (`2026-10-29 21:06:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.29` | **Live Ask Quote**: `8.32` | **Mid Price**: `8.30`
- **Spread Points**: `3.00` | **Spread BPS**: `36.12 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.72` | VWAP Z-Score: `-2.43` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0900` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `18.60` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `9.20` | Lower -3.00σ Band: `8.24`
  * Upper +2.51σ Band: `9.12` | Lower -2.51σ Band: `8.32`
  * Upper +2.01σ Band: `9.04` | Lower -2.01σ Band: `8.40`
  * Upper +2.00σ Band: `9.04` | Lower -2.00σ Band: `8.40`
  * Upper +1.28σ Band: `8.93` | Lower -1.28σ Band: `8.52`
  * Upper +1.00σ Band: `8.88` | Lower -1.00σ Band: `8.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.63` | EMA-20=`8.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.77` (Slope: `+0.0000`) | EMA-100=`8.79`
  * Institutional Anchors: EMA-144=`8.80` | EMA-200=`8.81` (Slope: `-0.1350`) | EMA-233=`8.82`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`8.24` | Weekly High=`9.14` | Weekly Low=`8.24`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.32` (Distance: `+0.39%`)
  * Point of Control (POC) = `8.29` (Distance: `+0.72%`)
  * Value Area Low (VAL) = `8.29` (Distance: `+0.72%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`8.96` | Weekly POC=`8.91` | Weekly VAL=`8.74`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.33` | Low=`8.29`
  * London Session (08:00-16:00 UTC): High=`8.34` | Low=`8.27`
  * New York Session (13:00-21:00 UTC): High=`8.35` | Low=`8.26`
  * Initial Balance (First Hour): IB High=`8.33` | IB Low=`8.28`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.27` - `8.34`
  * Optimal Trade Entry (OTE 0.705): `8.32`
  * Structural Invalidation Anchor (0.786): `8.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.39` | `8.41` | `8.33` | `8.35` | `188,031` | 1,574,237.89 USD | -29,189.29 USD | `-1.85%` | -10,625,817.97 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `8.35` | `8.40` | `8.31` | `8.32` | `264,537` | 2,209,938.99 USD | 42,053.93 USD | `+1.90%` | -10,583,764.04 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.32` | `8.34` | `8.31` | `8.34` | `22,521` | 187,323.19 USD | -4,642.06 USD | `-2.48%` | -10,588,406.09 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `8.73` | `8.76` | `8.39` | `8.40` | `1,542,699` | 13,163,243.09 USD | -4,068,399.10 USD | `-30.91%` | -7,952,251.97 USD | `-4.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.40` | `8.48` | `8.25` | `8.35` | `2,060,739` | 17,210,058.04 USD | -2,657,495.05 USD | `-15.44%` | -10,609,747.02 USD | `-2.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.35` | `8.40` | `8.31` | `8.34` | `287,058` | 2,397,262.18 USD | 37,411.88 USD | `+1.56%` | -10,572,335.14 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.84` | `8.87` | `8.80` | `8.85` | `249,668` | 2,205,666.85 USD | 221,936.79 USD | `+10.06%` | -4,466,203.86 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `8.85` | `8.86` | `8.25` | `8.35` | `4,480,707` | 38,039,389.45 USD | -6,440,743.86 USD | `-16.93%` | -10,906,947.72 USD | `-4.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.35` | `8.40` | `8.31` | `8.34` | `289,505` | 2,417,655.34 USD | 31,850.15 USD | `+1.32%` | -10,875,097.57 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.33` | `4,769,276` | 40,449,247.38 USD | -6,412,793.23 USD | `-15.85%` | -11,078,804.20 USD | `-1.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `8.59` | `8.80` | `8.57` | `8.62` | `1,816,830` | 15,790,058.74 USD | 58,580.54 USD | `+0.37%` | -2,364,450.84 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.62` | `8.83` | `8.62` | `8.77` | `1,352,753` | 11,811,156.57 USD | 264,257.49 USD | `+2.24%` | -2,100,193.35 USD | `+0.79` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.77` | `9.02` | `8.71` | `9.01` | `2,705,743` | 23,993,018.84 USD | -53,821.97 USD | `-0.22%` | -2,154,015.33 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -4,666,010.97 USD | `-1.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.25` | `8.33` | `4,769,276` | 40,449,247.38 USD | -6,412,793.23 USD | `-15.85%` | -11,078,804.20 USD | `-1.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`8.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.34` | `103.2200` | 861.30 USD | 30,574.39 USD | `1 orders` | `-0.16%` | `-` |
| `BID` | `8.34` | `1663.1800` | 13,877.74 USD | 44,452.13 USD | `1 orders` | `-0.17%` | `-` |
| `BID` | `8.34` | `419.7000` | 3,501.85 USD | 47,953.98 USD | `2 orders` | `-0.17%` | `-` |
| `BID` | `8.34` | `546.5300` | 4,560.03 USD | 52,514.01 USD | `7 orders` | `-0.17%` | `-` |
| `BID` | `8.34` | `103.2200` | 861.11 USD | 53,375.12 USD | `1 orders` | `-0.18%` | `-` |
| `BID` | `8.34` | `103.2200` | 861.00 USD | 54,236.12 USD | `1 orders` | `-0.20%` | `-` |
| `BID` | `8.34` | `4677.2700` | 39,014.51 USD | 93,250.63 USD | `5 orders` | `-0.20%` | `-` |
| `BID` | `8.34` | `3054.1500` | 25,475.28 USD | 118,725.91 USD | `4 orders` | `-0.20%` | `-` |
| `BID` | `8.35` | `26.2800` | 219.45 USD | 1,536.98 USD | `1 orders` | `-0.09%` | `-` |
| `BID` | `8.35` | `179.7900` | 1,500.67 USD | 3,037.65 USD | `1 orders` | `-0.13%` | `-` |
| `BID` | `8.35` | `179.7900` | 1,500.65 USD | 4,538.30 USD | `1 orders` | `-0.13%` | `-` |
| `BID` | `8.35` | `179.7900` | 1,500.64 USD | 6,038.94 USD | `1 orders` | `-0.14%` | `-` |
| `BID` | `8.35` | `2733.2100` | 22,812.74 USD | 28,851.68 USD | `14 orders` | `-0.14%` | `-` |
| `BID` | `8.35` | `103.2200` | 861.41 USD | 29,713.09 USD | `1 orders` | `-0.15%` | `-` |
| `ASK` | `8.36` | `5.9700` | 49.93 USD | 251.24 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.36` | `1.9500` | 16.30 USD | 201.31 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.36` | `22.1300` | 185.00 USD | 185.00 USD | `1 orders` | `+0.02%` | `-` |
| `MID_SPREAD` | `8.36` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.36` | `0.00%` | `-` |
| `BID` | `8.36` | `26.2800` | 219.60 USD | 219.60 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.36` | `26.2800` | 219.59 USD | 439.19 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.36` | `26.2800` | 219.59 USD | 658.78 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.36` | `26.2800` | 219.59 USD | 878.37 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.36` | `26.2800` | 219.59 USD | 1,097.95 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.36` | `26.2800` | 219.58 USD | 1,317.53 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `8.37` | `1197.9600` | 10,032.32 USD | 86,700.27 USD | `1 orders` | `+0.20%` | `-` |
| `ASK` | `8.37` | `368.9700` | 3,089.87 USD | 76,667.95 USD | `1 orders` | `+0.20%` | `-` |
| `ASK` | `8.37` | `1194.4600` | 10,001.93 USD | 73,578.09 USD | `1 orders` | `+0.19%` | `-` |
| `ASK` | `8.37` | `1663.1800` | 13,925.31 USD | 63,576.16 USD | `1 orders` | `+0.18%` | `-` |
| `ASK` | `8.37` | `60.3400` | 505.20 USD | 49,650.85 USD | `1 orders` | `+0.18%` | `-` |
| `ASK` | `8.37` | `955.7700` | 8,001.52 USD | 49,145.65 USD | `1 orders` | `+0.17%` | `-` |
| `ASK` | `8.37` | `91.0500` | 762.15 USD | 41,144.13 USD | `1 orders` | `+0.15%` | `-` |
| `ASK` | `8.37` | `148.1200` | 1,239.82 USD | 40,381.98 USD | `1 orders` | `+0.15%` | `-` |
| `ASK` | `8.37` | `1730.9000` | 14,488.15 USD | 39,142.15 USD | `2 orders` | `+0.15%` | `-` |
| `ASK` | `8.37` | `716.9700` | 6,001.11 USD | 24,654.00 USD | `1 orders` | `+0.15%` | `-` |
| `ASK` | `8.37` | `88.4900` | 740.66 USD | 18,652.89 USD | `1 orders` | `+0.14%` | `-` |
| `ASK` | `8.37` | `298.7200` | 2,499.93 USD | 17,912.23 USD | `1 orders` | `+0.13%` | `-` |
| `ASK` | `8.37` | `1663.1800` | 13,916.49 USD | 15,412.30 USD | `1 orders` | `+0.11%` | `-` |
| `ASK` | `8.37` | `29.6300` | 247.91 USD | 1,495.81 USD | `1 orders` | `+0.11%` | `-` |
| `ASK` | `8.37` | `89.2000` | 746.27 USD | 1,247.90 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `8.37` | `29.9300` | 250.39 USD | 501.63 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `8.38` | `1433.0300` | 12,002.34 USD | 98,702.61 USD | `1 orders` | `+0.21%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1485` | `0x7737...bf66` | `SHORT` | 1,498,389.65 USD | `171,568.06` | `7.43` | `8.37` | `110.10` | -222,844.63 USD | `-14.87%` | `10X Cross` |
| `1570` | `0xeadc...9d55` | `LONG` | 1,395,062.95 USD | `160,070.56` | `8.11` | `8.37` | `0.000000` | 97,425.38 USD | `+6.98%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `9.00` | 5,999.92 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 6.00K USD at 9.0047 USD [API] | `2026-10-28 04:40:18` |
| `ANNOUNCEMENT` | `INFO` | `8.97` | 13,999.97 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 14.00K USD at 8.9652 USD [API] | `2026-10-28 07:13:13` |
| `ANNOUNCEMENT` | `INFO` | `9.04` | 5,146.41 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.15K USD at 9.0426 USD [API] | `2026-10-28 10:00:14` |
| `ANNOUNCEMENT` | `INFO` | `9.00` | 5,999.87 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 9.0026 USD [API] | `2026-10-28 11:27:24` |


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
| `7D` | `Long Liquidation` | `7.36` | 2,610,000.00 USD | 2,610,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 5,720.00 USD | 577,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 3,920.00 USD | 572,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 21.18 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 17,770.00 USD | 568,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.39` | 2,590.00 USD | 550,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 2,600,000.00 USD | 2,600,000.00 USD | 6,810.00 USD | 0.00 USD | 29.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.42` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 18.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 500.00 USD | 547,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 1,490.00 USD | 547,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.44` | 2,590,000.00 USD | 2,590,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.45` | 210.99 USD | 545,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 1,370.00 USD | 545,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.46` | 1,540,000.00 USD | 1,540,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.46` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 1,410.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 9,160.00 USD | 544,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 3,210.00 USD | 535,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 2,580,000.00 USD | 2,580,000.00 USD | 9,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,580.00 USD | 531,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 1,080.00 USD | 530,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.52` | 1,540,000.00 USD | 1,540,000.00 USD | 9,830.00 USD | 7,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 995.86 USD | 529,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 528,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 157.14 USD | 523,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.58` | 4,380.00 USD | 523,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.59` | 25,140.00 USD | 519,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 3,770.00 USD | 74.23 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 312.22 USD | 494,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 493,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.63` | 514.52 USD | 493,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 1,510,000.00 USD | 1,510,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 492,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.66` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 1,740.00 USD | 492,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.68` | 1,120.00 USD | 490,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.70` | 1,460.00 USD | 489,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 1,510,000.00 USD | 1,510,000.00 USD | 321.75 USD | 2,390.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.71` | 19,760.00 USD | 488,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.72` | 1,510,000.00 USD | 1,510,000.00 USD | 4,160.00 USD | 1,630.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.72` | 2,550.00 USD | 468,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.74` | 1,490,000.00 USD | 1,490,000.00 USD | 2,950.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 2,520,000.00 USD | 2,520,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 893.76 USD | 465,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 1,480,000.00 USD | 1,480,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 2,520,000.00 USD | 2,520,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 465,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.78` | 695.32 USD | 464,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 1,470,000.00 USD | 1,470,000.00 USD | 42,650.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 2,510,000.00 USD | 2,510,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,900.00 USD | 463,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.79` | 1,940.00 USD | 459,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 1,410,000.00 USD | 1,410,000.00 USD | 38,450.00 USD | 10,860.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 2,450,000.00 USD | 2,450,000.00 USD | 13,050.00 USD | 12,980.00 USD | 174.42 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 633.77 USD | 458,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.82` | 5,280.00 USD | 457,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.82` | 1,360,000.00 USD | 1,360,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 2,420,000.00 USD | 2,420,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 1,340,000.00 USD | 1,340,000.00 USD | 671.45 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 2,410,000.00 USD | 2,410,000.00 USD | 29,020.00 USD | 2,380.00 USD | 25,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 10,930.00 USD | 452,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.86` | 2,110.00 USD | 441,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.86` | 1,320,000.00 USD | 1,320,000.00 USD | 14,500.00 USD | 1,680.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 2,350,000.00 USD | 2,350,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 176.18 USD | 439,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 438,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 1,290,000.00 USD | 1,290,000.00 USD | 43,790.00 USD | 9,570.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 2,300,000.00 USD | 2,300,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.90` | 1,210,000.00 USD | 1,210,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 2,200,000.00 USD | 2,200,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 505.13 USD | 438,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.92` | 1,180,000.00 USD | 1,180,000.00 USD | 19,860.00 USD | 2,950.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 2,140,000.00 USD | 2,140,000.00 USD | 53,660.00 USD | 8,420.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 1,820.00 USD | 437,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 1,150,000.00 USD | 1,150,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 2,060,000.00 USD | 2,060,000.00 USD | 49,080.00 USD | 9,960.00 USD | 32,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 127,110.00 USD | 436,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.96` | 843.15 USD | 308,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 1,120,000.00 USD | 1,120,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 1,970,000.00 USD | 1,970,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.98` | 1,110,000.00 USD | 1,110,000.00 USD | 14,350.00 USD | 3,300.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 1,920,000.00 USD | 1,920,000.00 USD | 54,090.00 USD | 19,680.00 USD | 70,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,600.00 USD | 308,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.00` | 210.99 USD | 306,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 1,080,000.00 USD | 1,080,000.00 USD | 570.55 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 1,770,000.00 USD | 1,770,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 1,080,000.00 USD | 1,080,000.00 USD | 40,190.00 USD | 8,470.00 USD | 157.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 1,690,000.00 USD | 1,690,000.00 USD | 20,910.00 USD | 28,440.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 957.70 USD | 306,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.04` | 88,380.00 USD | 305,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.04` | 1,030,000.00 USD | 1,030,000.00 USD | 19,460.00 USD | 11,910.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 1,630,000.00 USD | 1,630,000.00 USD | 123,080.00 USD | 38,980.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 6,890.00 USD | 216,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 3,340.00 USD | 210,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 989,160.00 USD | 989,160.00 USD | 27,730.00 USD | 9,400.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 1,390,000.00 USD | 1,390,000.00 USD | 70,840.00 USD | 20,850.00 USD | 85,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 37,830.00 USD | 206,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 945,820.00 USD | 945,820.00 USD | 22,320.00 USD | 3,810.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 1,210,000.00 USD | 1,210,000.00 USD | 7,170.00 USD | 8,710.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 617.61 USD | 168,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.10` | 11,700.00 USD | 168,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.10` | 914,940.00 USD | 914,940.00 USD | 32,980.00 USD | 13,380.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 1,170,000.00 USD | 1,170,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 241.26 USD | 156,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 860,740.00 USD | 860,740.00 USD | 12,010.00 USD | 4,240.00 USD | 22,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 1,080,000.00 USD | 1,080,000.00 USD | 27,520.00 USD | 10,810.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 822,300.00 USD | 822,300.00 USD | 20,690.00 USD | 0.00 USD | 42.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 1,030,000.00 USD | 1,030,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 801,570.00 USD | 801,570.00 USD | 11,720.00 USD | 662.47 USD | 9,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 904,400.00 USD | 904,400.00 USD | 38,430.00 USD | 5,510.00 USD | 29,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.16` | 871.61 USD | 156,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.18` | 235.36 USD | 155,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.18` | 780,160.00 USD | 780,160.00 USD | 53,280.00 USD | 15,390.00 USD | 478.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 830,490.00 USD | 830,490.00 USD | 10,520.00 USD | 6,790.00 USD | 29,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.20` | 1,050.00 USD | 155,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.20` | 711,010.00 USD | 711,010.00 USD | 7,430.00 USD | 20,740.00 USD | 448.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 783,810.00 USD | 783,810.00 USD | 33,800.00 USD | 22,240.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.21` | 1,910.00 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.21` | 147.87 USD | 152,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.22` | 682,390.00 USD | 682,390.00 USD | 7,650.00 USD | 13,850.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 718,360.00 USD | 718,360.00 USD | 19,610.00 USD | 21,570.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.22` | 2,100.00 USD | 152,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.23` | 1,160.00 USD | 149,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.24` | 650,850.00 USD | 650,850.00 USD | 65,360.00 USD | 5,230.00 USD | 34,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 667,020.00 USD | 667,020.00 USD | 39,950.00 USD | 3,480.00 USD | 108,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.24` | 1,300.00 USD | 148,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.26` | 13,810.00 USD | 147,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.26` | 545,740.00 USD | 545,740.00 USD | 15,150.00 USD | 11,460.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 515,150.00 USD | 515,150.00 USD | 30,490.00 USD | 5,750.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.28` | 9,740.00 USD | 133,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.28` | 513,030.00 USD | 513,030.00 USD | 137,750.00 USD | 28,700.00 USD | 79,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 477,280.00 USD | 477,280.00 USD | 122,850.00 USD | 33,920.00 USD | 22,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.29` | 498.26 USD | 123,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.29` | 18,970.00 USD | 123,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.30` | 266,680.00 USD | 266,680.00 USD | 94,260.00 USD | 22,600.00 USD | 23,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 297,590.00 USD | 297,590.00 USD | 152,370.00 USD | 11,360.00 USD | 48,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.30` | 33,500.00 USD | 104,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.31` | 4,550.00 USD | 71,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.32` | 126,010.00 USD | 126,010.00 USD | 73,190.00 USD | 20,010.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 85,430.00 USD | 85,430.00 USD | 61,580.00 USD | 21,100.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.34` | 4,760.00 USD | 66,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.34` | 23,920.00 USD | 23,920.00 USD | 0.00 USD | 0.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.34` | 124,260.00 USD | 124,260.00 USD | 28,220.00 USD | 10,180.00 USD | 85,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.34` | 248,510.00 USD | 248,510.00 USD | 28,220.00 USD | 10,180.00 USD | 85,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.36` | 3,180.00 USD | 61,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.36` | 39,690.00 USD | 39,690.00 USD | 1,810.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.36` | 79,380.00 USD | 79,380.00 USD | 1,810.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.36` | 436,630.00 USD | 436,630.00 USD | 107,760.00 USD | 0.00 USD | 80,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.37` | 7,390.00 USD | 58,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.38` | 132,920.00 USD | 132,920.00 USD | 1,510.00 USD | 0.00 USD | 52,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.38` | 648,520.00 USD | 648,520.00 USD | 143,540.00 USD | 0.00 USD | 68,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.38` | 4,620.00 USD | 51,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.39` | 1,680.00 USD | 46,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.40` | 197,330.00 USD | 197,330.00 USD | 1,220.00 USD | 0.00 USD | 63,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.40` | 862,720.00 USD | 862,720.00 USD | 179,510.00 USD | 0.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.40` | 1,380.00 USD | 44,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.41` | 681.03 USD | 43,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.42` | 198,330.00 USD | 198,330.00 USD | 995.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.42` | 1,040,000.00 USD | 1,040,000.00 USD | 178,300.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.44` | 188.61 USD | 42,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.44` | 198,760.00 USD | 198,760.00 USD | 427.96 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.44` | 1,200,000.00 USD | 1,200,000.00 USD | 155,040.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.45` | 588.70 USD | 42,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.46` | 422.16 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.46` | 198,780.00 USD | 198,780.00 USD | 0.00 USD | 0.00 USD | 18.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.46` | 1,600,000.00 USD | 1,600,000.00 USD | 392,550.00 USD | 0.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.46` | 1,860.00 USD | 41,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.47` | 12,430.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.48` | 237,960.00 USD | 237,960.00 USD | 0.00 USD | 39,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 2,110,000.00 USD | 2,110,000.00 USD | 477,600.00 USD | 35,130.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.48` | 1,160.00 USD | 27,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.49` | 403.51 USD | 26,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.50` | 503,470.00 USD | 503,470.00 USD | 206,180.00 USD | 59,320.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 2,430,000.00 USD | 2,430,000.00 USD | 218,140.00 USD | 100,070.00 USD | 936.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.51` | 6,380.00 USD | 25,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.52` | 7,770.00 USD | 19,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.52` | 692,470.00 USD | 692,470.00 USD | 123,250.00 USD | 65,750.00 USD | 1.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 2,800,000.00 USD | 2,800,000.00 USD | 270,540.00 USD | 98,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 6,350.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.54` | 748,580.00 USD | 748,580.00 USD | 35,370.00 USD | 20,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 3,280,000.00 USD | 3,280,000.00 USD | 379,850.00 USD | 100,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.54` | 1,550.00 USD | 5,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 684.40 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.56` | 1,020,000.00 USD | 1,020,000.00 USD | 158,900.00 USD | 7,860.00 USD | 106,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 4,000,000.00 USD | 4,000,000.00 USD | 593,510.00 USD | 122,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,300,000.00 USD | 1,300,000.00 USD | 136,600.00 USD | 0.00 USD | 144,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 4,760,000.00 USD | 4,760,000.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 53,060.00 USD | 65,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.60` | 4,880,000.00 USD | 4,880,000.00 USD | 75,040.00 USD | 39,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.61` | 2,980.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,530,000.00 USD | 1,530,000.00 USD | 28,330.00 USD | 54,800.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 43,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 21,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 48,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 16,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,670,000.00 USD | 1,670,000.00 USD | 24,580.00 USD | 7,700.00 USD | 39,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 5,340,000.00 USD | 5,340,000.00 USD | 148,470.00 USD | 24,870.00 USD | 223,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,740,000.00 USD | 1,740,000.00 USD | 36,540.00 USD | 10,370.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 23,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,760,000.00 USD | 1,760,000.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 15,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,870,000.00 USD | 1,870,000.00 USD | 97,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 22,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,030,000.00 USD | 2,030,000.00 USD | 107,520.00 USD | 9,440.00 USD | 35,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,140,000.00 USD | 2,140,000.00 USD | 61,700.00 USD | 17,690.00 USD | 37,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 5,550,000.00 USD | 5,550,000.00 USD | 27,360.00 USD | 33,750.00 USD | 18,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,160,000.00 USD | 2,160,000.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 5,650,000.00 USD | 5,650,000.00 USD | 100,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 8,820.00 USD | 68,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,250,000.00 USD | 2,250,000.00 USD | 12,400.00 USD | 2,250.00 USD | 148.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,400,000.00 USD | 2,400,000.00 USD | 29,560.00 USD | 8,140.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,460,000.00 USD | 2,460,000.00 USD | 37,770.00 USD | 7,360.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,530,000.00 USD | 2,530,000.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 5,900,000.00 USD | 5,900,000.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,580,000.00 USD | 2,580,000.00 USD | 24,340.00 USD | 5,550.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.00` | 2,710,000.00 USD | 2,710,000.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 6,240,000.00 USD | 6,240,000.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 2,810,000.00 USD | 2,810,000.00 USD | 39,130.00 USD | 43,160.00 USD | 18,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 6,330,000.00 USD | 6,330,000.00 USD | 34,650.00 USD | 56,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 2,980,000.00 USD | 2,980,000.00 USD | 87,540.00 USD | 43,590.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 6,510,000.00 USD | 6,510,000.00 USD | 90,520.00 USD | 74,750.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,100,000.00 USD | 3,100,000.00 USD | 33,880.00 USD | 33,420.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 6,580,000.00 USD | 6,580,000.00 USD | 5,610.00 USD | 14,960.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,230,000.00 USD | 3,230,000.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 11,960.00 USD | 65,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,540,000.00 USD | 3,540,000.00 USD | 197,560.00 USD | 43,240.00 USD | 63,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 7,860,000.00 USD | 7,860,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 3,800,000.00 USD | 3,800,000.00 USD | 160,000.00 USD | 47,350.00 USD | 56,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 8,850,000.00 USD | 8,850,000.00 USD | 490,020.00 USD | 24,170.00 USD | 479,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.13` | 314.34 USD | 314.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,010,000.00 USD | 4,010,000.00 USD | 118,520.00 USD | 23,510.00 USD | 67,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 9,890,000.00 USD | 9,890,000.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,220,000.00 USD | 4,220,000.00 USD | 121,090.00 USD | 41,060.00 USD | 51,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 10,480,000.00 USD | 10,480,000.00 USD | 358,370.00 USD | 44,360.00 USD | 195,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,550,000.00 USD | 4,550,000.00 USD | 187,840.00 USD | 53,800.00 USD | 86,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 11,490,000.00 USD | 11,490,000.00 USD | 565,140.00 USD | 162,460.00 USD | 273,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 4,890,000.00 USD | 4,890,000.00 USD | 197,260.00 USD | 61,430.00 USD | 81,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 12,390,000.00 USD | 12,390,000.00 USD | 548,100.00 USD | 120,080.00 USD | 237,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.21` | 3,810.00 USD | 4,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,040,000.00 USD | 5,040,000.00 USD | 126,810.00 USD | 12,990.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 13,540,000.00 USD | 13,540,000.00 USD | 585,170.00 USD | 144,840.00 USD | 421,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,150,000.00 USD | 5,150,000.00 USD | 71,810.00 USD | 4,560.00 USD | 27,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 14,090,000.00 USD | 14,090,000.00 USD | 316,220.00 USD | 56,410.00 USD | 170,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,200,000.00 USD | 5,200,000.00 USD | 35,150.00 USD | 8,290.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 14,520,000.00 USD | 14,520,000.00 USD | 273,920.00 USD | 96,980.00 USD | 61,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,260,000.00 USD | 5,260,000.00 USD | 44,130.00 USD | 10,920.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 15,220,000.00 USD | 15,220,000.00 USD | 428,160.00 USD | 103,490.00 USD | 170,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 100.93 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,360,000.00 USD | 5,360,000.00 USD | 58,890.00 USD | 13,560.00 USD | 23,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 15,780,000.00 USD | 15,780,000.00 USD | 199,810.00 USD | 97,780.00 USD | 263,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,420,000.00 USD | 5,420,000.00 USD | 37,200.00 USD | 4,250.00 USD | 23,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 16,450,000.00 USD | 16,450,000.00 USD | 271,660.00 USD | 59,310.00 USD | 337,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,470,000.00 USD | 5,470,000.00 USD | 23,850.00 USD | 10,190.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 16,780,000.00 USD | 16,780,000.00 USD | 203,440.00 USD | 53,150.00 USD | 69,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.35` | 3,930.00 USD | 8,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,580,000.00 USD | 5,580,000.00 USD | 59,430.00 USD | 14,870.00 USD | 30,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 17,180,000.00 USD | 17,180,000.00 USD | 247,120.00 USD | 73,430.00 USD | 85,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,690,000.00 USD | 5,690,000.00 USD | 65,320.00 USD | 17,450.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 17,710,000.00 USD | 17,710,000.00 USD | 383,530.00 USD | 55,400.00 USD | 85,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.38` | 404,120.00 USD | 412,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,740,000.00 USD | 5,740,000.00 USD | 52,090.00 USD | 1,210.00 USD | 25.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 18,120,000.00 USD | 18,120,000.00 USD | 234,760.00 USD | 42,520.00 USD | 137,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 2,470.00 USD | 414,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,800,000.00 USD | 5,800,000.00 USD | 30,730.00 USD | 4,670.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 18,400,000.00 USD | 18,400,000.00 USD | 176,920.00 USD | 19,780.00 USD | 85,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,820,000.00 USD | 5,820,000.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 18,520,000.00 USD | 18,520,000.00 USD | 41,250.00 USD | 19,420.00 USD | 56,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,830,000.00 USD | 5,830,000.00 USD | 1,630.00 USD | 4,580.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 18,630,000.00 USD | 18,630,000.00 USD | 60,020.00 USD | 29,830.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 5,840,000.00 USD | 5,840,000.00 USD | 2,800.00 USD | 1,100.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 18,700,000.00 USD | 18,700,000.00 USD | 12,180.00 USD | 27,840.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.49` | 428.79 USD | 415,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.50` | 5,900,000.00 USD | 5,900,000.00 USD | 42,390.00 USD | 3,730.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 18,900,000.00 USD | 18,900,000.00 USD | 89,460.00 USD | 33,210.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.52` | 5,920,000.00 USD | 5,920,000.00 USD | 17,470.00 USD | 3,070.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 19,080,000.00 USD | 19,080,000.00 USD | 102,150.00 USD | 29,320.00 USD | 51,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.54` | 5,960,000.00 USD | 5,960,000.00 USD | 23,980.00 USD | 7,790.00 USD | 2,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 19,300,000.00 USD | 19,300,000.00 USD | 192,090.00 USD | 25,090.00 USD | 771.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.56` | 5,980,000.00 USD | 5,980,000.00 USD | 6,950.00 USD | 7,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 19,410,000.00 USD | 19,410,000.00 USD | 88,510.00 USD | 5,260.00 USD | 14,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.58` | 5,990,000.00 USD | 5,990,000.00 USD | 1,270.00 USD | 4,910.00 USD | 12,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 19,490,000.00 USD | 19,490,000.00 USD | 35,340.00 USD | 14,530.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.60` | 6,030,000.00 USD | 6,030,000.00 USD | 15,230.00 USD | 1,680.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 19,560,000.00 USD | 19,560,000.00 USD | 38,740.00 USD | 5,460.00 USD | 26,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.62` | 6,070,000.00 USD | 6,070,000.00 USD | 20,200.00 USD | 4,140.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 19,650,000.00 USD | 19,650,000.00 USD | 70,470.00 USD | 1,540.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.64` | 6,100,000.00 USD | 6,100,000.00 USD | 22,380.00 USD | 5,430.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.64` | 19,720,000.00 USD | 19,720,000.00 USD | 35,210.00 USD | 17,650.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.66` | 6,130,000.00 USD | 6,130,000.00 USD | 14,580.00 USD | 7,630.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.66` | 19,800,000.00 USD | 19,800,000.00 USD | 37,340.00 USD | 21,280.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.68` | 6,160,000.00 USD | 6,160,000.00 USD | 16,150.00 USD | 2,950.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.68` | 19,920,000.00 USD | 19,920,000.00 USD | 68,230.00 USD | 20,310.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.70` | 6,190,000.00 USD | 6,190,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.70` | 20,040,000.00 USD | 20,040,000.00 USD | 78,860.00 USD | 12,990.00 USD | 32,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.72` | 6,200,000.00 USD | 6,200,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.72` | 20,150,000.00 USD | 20,150,000.00 USD | 70,300.00 USD | 6,920.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 415,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.74` | 6,220,000.00 USD | 6,220,000.00 USD | 6,960.00 USD | 738.05 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.74` | 20,200,000.00 USD | 20,200,000.00 USD | 21,230.00 USD | 7,200.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.76` | 549.11 USD | 415,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.76` | 6,230,000.00 USD | 6,230,000.00 USD | 7,400.00 USD | 2,560.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.76` | 20,300,000.00 USD | 20,300,000.00 USD | 35,520.00 USD | 12,480.00 USD | 51,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.78` | 470.18 USD | 416,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.78` | 6,230,000.00 USD | 6,230,000.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.78` | 20,380,000.00 USD | 20,380,000.00 USD | 65,390.00 USD | 10,300.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.80` | 6,250,000.00 USD | 6,250,000.00 USD | 12,580.00 USD | 770.83 USD | 9.39 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.80` | 20,430,000.00 USD | 20,430,000.00 USD | 18,630.00 USD | 28,440.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.82` | 6,270,000.00 USD | 6,270,000.00 USD | 14,340.00 USD | 1,540.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.82` | 20,670,000.00 USD | 20,670,000.00 USD | 121,860.00 USD | 27,860.00 USD | 86,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.84` | 20,700,000.00 USD | 20,700,000.00 USD | 9,730.00 USD | 7,850.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.86` | 20,830,000.00 USD | 20,830,000.00 USD | 58,870.00 USD | 2,210.00 USD | 71,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.88` | 20,870,000.00 USD | 20,870,000.00 USD | 7,170.00 USD | 8,710.00 USD | 21,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.90` | 20,960,000.00 USD | 20,960,000.00 USD | 55,970.00 USD | 19,700.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.92` | 21,010,000.00 USD | 21,010,000.00 USD | 27,710.00 USD | 10,810.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.94` | 21,130,000.00 USD | 21,130,000.00 USD | 69,320.00 USD | 11,150.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.96` | 21,170,000.00 USD | 21,170,000.00 USD | 29,800.00 USD | 1,360.00 USD | 10,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.98` | 21,200,000.00 USD | 21,200,000.00 USD | 840.10 USD | 4,150.00 USD | 18,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.00` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.02` | 21,220,000.00 USD | 21,220,000.00 USD | 16,100.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.04` | 21,240,000.00 USD | 21,240,000.00 USD | 505.60 USD | 0.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.06` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.08` | 21,280,000.00 USD | 21,280,000.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `1.74` | 2,290,000.00 USD | 0.00 USD | 190.85 USD | `-79.22%` | `110.00` |
| `Live` | `Long` | `1.78` | 2,290,000.00 USD | 0.00 USD | 197.80 USD | `-78.62%` | `110.81` |
| `Live` | `Long` | `1.82` | 2,290,000.00 USD | 0.00 USD | 200.75 USD | `-78.14%` | `110.00` |
| `Live` | `Long` | `1.84` | 2,290,000.00 USD | 0.00 USD | 129.15 USD | `-77.90%` | `70.00` |
| `Live` | `Long` | `1.86` | 2,290,000.00 USD | 0.00 USD | 1,240.00 USD | `-77.66%` | `666.20` |
| `Live` | `Long` | `1.95` | 2,290,000.00 USD | 0.00 USD | 213.95 USD | `-76.70%` | `110.00` |
| `Live` | `Long` | `2.00` | 2,290,000.00 USD | 0.00 USD | 159.60 USD | `-76.11%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,290,000.00 USD | 0.00 USD | 110.52 USD | `-75.63%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.27%` | `2,382.76` |
| `Live` | `Long` | `2.13` | 2,280,000.00 USD | 0.00 USD | 2,160.00 USD | `-74.43%` | `1,010.81` |
| `Live` | `Long` | `2.19` | 2,280,000.00 USD | 0.00 USD | 874.00 USD | `-73.83%` | `400.00` |
| `Live` | `Long` | `2.42` | 2,280,000.00 USD | 0.00 USD | 814.80 USD | `-70.96%` | `336.00` |
| `Live` | `Long` | `2.46` | 2,280,000.00 USD | 0.00 USD | 9,770.00 USD | `-70.60%` | `3,981.48` |
| `Live` | `Long` | `2.50` | 2,270,000.00 USD | 0.00 USD | 275.55 USD | `-70.00%` | `110.00` |
| `Live` | `Long` | `2.56` | 2,270,000.00 USD | 0.00 USD | 192.38 USD | `-69.28%` | `75.00` |
| `Live` | `Long` | `2.69` | 2,270,000.00 USD | 0.00 USD | 457.99 USD | `-67.72%` | `169.94` |
| `Live` | `Long` | `2.81` | 2,270,000.00 USD | 0.00 USD | 19,610.00 USD | `-66.40%` | `6,990.57` |
| `Live` | `Long` | `2.85` | 2,250,000.00 USD | 0.00 USD | 346.38 USD | `-65.93%` | `121.75` |
| `Live` | `Long` | `2.87` | 2,250,000.00 USD | 0.00 USD | 232.67 USD | `-65.69%` | `81.21` |
| `Live` | `Long` | `2.94` | 2,250,000.00 USD | 0.00 USD | 44,510.00 USD | `-64.85%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,200,000.00 USD | 0.00 USD | 111.12 USD | `-64.37%` | `37.35` |
| `Live` | `Long` | `3.02` | 2,200,000.00 USD | 0.00 USD | 156.78 USD | `-63.89%` | `52.00` |
| `Live` | `Long` | `3.08` | 2,200,000.00 USD | 0.00 USD | 103.38 USD | `-63.05%` | `33.51` |
| `Live` | `Long` | `3.15` | 2,200,000.00 USD | 0.00 USD | 358.84 USD | `-62.33%` | `114.10` |
| `Live` | `Long` | `3.23` | 2,200,000.00 USD | 0.00 USD | 6,470.00 USD | `-61.25%` | `2,000.00` |
| `Live` | `Long` | `3.29` | 2,200,000.00 USD | 0.00 USD | 229.95 USD | `-60.66%` | `70.00` |
| `Live` | `Long` | `3.37` | 2,200,000.00 USD | 0.00 USD | 389.53 USD | `-59.70%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,200,000.00 USD | 0.00 USD | 151.88 USD | `-59.58%` | `45.00` |
| `Live` | `Long` | `3.42` | 2,200,000.00 USD | 0.00 USD | 1,290.00 USD | `-58.98%` | `377.71` |
| `Live` | `Long` | `3.44` | 2,190,000.00 USD | 0.00 USD | 560.98 USD | `-58.74%` | `162.84` |
| `Live` | `Long` | `3.46` | 2,190,000.00 USD | 0.00 USD | 116.50 USD | `-58.62%` | `33.72` |
| `Live` | `Long` | `3.67` | 2,190,000.00 USD | 0.00 USD | 109.95 USD | `-56.10%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,190,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.03%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,190,000.00 USD | 0.00 USD | 131.73 USD | `-53.35%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,190,000.00 USD | 0.00 USD | 402.70 USD | `-51.79%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,190,000.00 USD | 0.00 USD | 152.29 USD | `-51.55%` | `37.65` |
| `Live` | `Long` | `4.14` | 2,190,000.00 USD | 0.00 USD | 594.52 USD | `-50.36%` | `143.43` |
| `Live` | `Long` | `4.18` | 2,190,000.00 USD | 0.00 USD | 174.89 USD | `-49.88%` | `41.79` |
| `Live` | `Long` | `4.21` | 2,190,000.00 USD | 0.00 USD | 268.07 USD | `-49.64%` | `63.75` |
| `Live` | `Long` | `4.24` | 2,190,000.00 USD | 0.00 USD | 169.40 USD | `-49.28%` | `40.00` |
| `Live` | `Long` | `4.38` | 2,190,000.00 USD | 0.00 USD | 188.86 USD | `-47.48%` | `43.07` |
| `Live` | `Long` | `4.59` | 2,190,000.00 USD | 0.00 USD | 30,970.00 USD | `-44.97%` | `6,740.93` |
| `Live` | `Long` | `4.61` | 2,160,000.00 USD | 0.00 USD | 196.50 USD | `-44.85%` | `42.67` |
| `Live` | `Long` | `4.62` | 2,160,000.00 USD | 0.00 USD | 486.93 USD | `-44.73%` | `105.51` |
| `Live` | `Long` | `4.62` | 2,160,000.00 USD | 0.00 USD | 2,680.00 USD | `-44.61%` | `579.06` |
| `Live` | `Long` | `4.66` | 2,160,000.00 USD | 0.00 USD | 105.11 USD | `-44.25%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,160,000.00 USD | 0.00 USD | 3,720.00 USD | `-44.13%` | `797.26` |
| `Live` | `Long` | `4.67` | 2,150,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.01%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,150,000.00 USD | 0.00 USD | 8,380.00 USD | `-43.89%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,140,000.00 USD | 0.00 USD | 7,040.00 USD | `-43.77%` | `1,500.00` |
| `Live` | `Long` | `4.76` | 2,140,000.00 USD | 0.00 USD | 105.64 USD | `-42.93%` | `22.17` |
| `Live` | `Long` | `4.82` | 2,140,000.00 USD | 0.00 USD | 112.96 USD | `-42.33%` | `23.46` |
| `Live` | `Long` | `4.83` | 2,130,000.00 USD | 0.00 USD | 467.01 USD | `-42.09%` | `96.59` |
| `Live` | `Long` | `4.84` | 2,130,000.00 USD | 0.00 USD | 17,130.00 USD | `-41.97%` | `3,536.00` |
| `Live` | `Long` | `4.89` | 2,120,000.00 USD | 0.00 USD | 146.85 USD | `-41.37%` | `30.00` |
| `Live` | `Long` | `4.91` | 2,120,000.00 USD | 0.00 USD | 527.19 USD | `-41.25%` | `107.48` |
| `Live` | `Long` | `4.92` | 2,120,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.13%` | `251.00` |
| `Live` | `Long` | `4.92` | 2,120,000.00 USD | 0.00 USD | 2,960.00 USD | `-41.01%` | `600.00` |
| `Live` | `Long` | `4.96` | 2,110,000.00 USD | 0.00 USD | 945.36 USD | `-40.65%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,110,000.00 USD | 0.00 USD | 4,430.00 USD | `-40.53%` | `893.25` |
| `Live` | `Long` | `4.97` | 2,110,000.00 USD | 0.00 USD | 282.23 USD | `-40.41%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,110,000.00 USD | 0.00 USD | 729.17 USD | `-40.17%` | `145.98` |
| `Live` | `Long` | `5.01` | 2,110,000.00 USD | 0.00 USD | 56,390.00 USD | `-39.94%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,050,000.00 USD | 0.00 USD | 167.78 USD | `-39.82%` | `33.39` |
| `Live` | `Long` | `5.04` | 2,050,000.00 USD | 0.00 USD | 314.59 USD | `-39.70%` | `62.48` |
| `Live` | `Long` | `5.05` | 2,050,000.00 USD | 0.00 USD | 504.74 USD | `-39.46%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,050,000.00 USD | 0.00 USD | 5,660.00 USD | `-39.22%` | `1,115.75` |
| `Live` | `Long` | `5.12` | 2,040,000.00 USD | 0.00 USD | 2,560.00 USD | `-38.74%` | `500.00` |
| `Live` | `Long` | `5.12` | 2,040,000.00 USD | 0.00 USD | 250.20 USD | `-38.62%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,040,000.00 USD | 0.00 USD | 396.06 USD | `-38.50%` | `77.13` |
| `Live` | `Long` | `5.14` | 2,040,000.00 USD | 0.00 USD | 119.36 USD | `-38.38%` | `23.20` |
| `Live` | `Long` | `5.17` | 2,040,000.00 USD | 0.00 USD | 2,300.00 USD | `-38.14%` | `445.16` |
| `Live` | `Long` | `5.17` | 2,040,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.02%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,040,000.00 USD | 0.00 USD | 150.57 USD | `-37.90%` | `29.04` |
| `Live` | `Long` | `5.20` | 2,040,000.00 USD | 0.00 USD | 210.97 USD | `-37.78%` | `40.61` |
| `Live` | `Long` | `5.21` | 2,040,000.00 USD | 0.00 USD | 2,250.00 USD | `-37.54%` | `431.24` |
| `Live` | `Long` | `5.25` | 2,030,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.06%` | `200.00` |
| `Live` | `Long` | `5.29` | 2,030,000.00 USD | 0.00 USD | 640.70 USD | `-36.70%` | `121.23` |
| `Live` | `Long` | `5.29` | 2,030,000.00 USD | 0.00 USD | 161,700.00 USD | `-36.58%` | `30,538.93` |
| `Live` | `Long` | `5.32` | 1,870,000.00 USD | 0.00 USD | 232.85 USD | `-36.34%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,870,000.00 USD | 0.00 USD | 716.11 USD | `-36.22%` | `134.48` |
| `Live` | `Long` | `5.38` | 1,870,000.00 USD | 0.00 USD | 516.27 USD | `-35.62%` | `96.05` |
| `Live` | `Long` | `5.39` | 1,870,000.00 USD | 0.00 USD | 660.46 USD | `-35.38%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,870,000.00 USD | 0.00 USD | 21,080.00 USD | `-35.14%` | `3,892.05` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 161,870.00 USD | `-35.02%` | `29,837.25` |
| `Live` | `Long` | `5.43` | 1,680,000.00 USD | 0.00 USD | 1,360.00 USD | `-34.90%` | `250.00` |
| `Live` | `Long` | `5.46` | 1,680,000.00 USD | 0.00 USD | 264.72 USD | `-34.55%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,680,000.00 USD | 0.00 USD | 1,320.00 USD | `-34.43%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,680,000.00 USD | 0.00 USD | 354.06 USD | `-34.31%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,680,000.00 USD | 0.00 USD | 19,290.00 USD | `-34.19%` | `3,510.41` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 273.16 USD | `-34.07%` | `49.62` |
| `Live` | `Long` | `5.51` | 1,660,000.00 USD | 0.00 USD | 367.41 USD | `-33.95%` | `66.62` |
| `Live` | `Long` | `5.54` | 1,660,000.00 USD | 0.00 USD | 121.38 USD | `-33.71%` | `21.93` |
| `Live` | `Long` | `5.57` | 1,660,000.00 USD | 0.00 USD | 967.98 USD | `-33.35%` | `173.94` |
| `Live` | `Long` | `5.58` | 1,660,000.00 USD | 0.00 USD | 75,940.00 USD | `-33.23%` | `13,620.92` |
| `Live` | `Long` | `5.59` | 1,580,000.00 USD | 0.00 USD | 34,430.00 USD | `-32.99%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,550,000.00 USD | 0.00 USD | 740.27 USD | `-32.51%` | `131.37` |
| `Live` | `Long` | `5.74` | 1,550,000.00 USD | 0.00 USD | 238.86 USD | `-31.31%` | `41.65` |
| `Live` | `Long` | `5.75` | 1,550,000.00 USD | 0.00 USD | 125.70 USD | `-31.19%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,550,000.00 USD | 0.00 USD | 3,190.00 USD | `-31.07%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,550,000.00 USD | 0.00 USD | 13,260.00 USD | `-30.95%` | `2,300.07` |
| `Live` | `Long` | `5.78` | 1,530,000.00 USD | 0.00 USD | 801.40 USD | `-30.83%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,530,000.00 USD | 0.00 USD | 2,890.00 USD | `-30.71%` | `500.00` |
| `Live` | `Long` | `5.79` | 1,530,000.00 USD | 0.00 USD | 736.72 USD | `-30.59%` | `127.13` |
| `Live` | `Long` | `5.80` | 1,530,000.00 USD | 0.00 USD | 580.50 USD | `-30.47%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,530,000.00 USD | 0.00 USD | 106.65 USD | `-30.35%` | `18.34` |
| `Live` | `Long` | `5.89` | 1,530,000.00 USD | 0.00 USD | 984.70 USD | `-29.40%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,530,000.00 USD | 0.00 USD | 2,500.00 USD | `-29.28%` | `424.11` |
| `Live` | `Long` | `5.96` | 1,520,000.00 USD | 0.00 USD | 11,720.00 USD | `-28.68%` | `1,968.19` |
| `Live` | `Long` | `5.97` | 1,510,000.00 USD | 0.00 USD | 585.97 USD | `-28.44%` | `98.07` |
| `Live` | `Long` | `5.99` | 1,510,000.00 USD | 0.00 USD | 447.98 USD | `-28.32%` | `74.85` |
| `Live` | `Long` | `6.00` | 1,510,000.00 USD | 0.00 USD | 1,480.00 USD | `-28.08%` | `246.87` |
| `Live` | `Long` | `6.01` | 1,510,000.00 USD | 0.00 USD | 446.85 USD | `-27.96%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,510,000.00 USD | 0.00 USD | 331.68 USD | `-27.72%` | `54.96` |
| `Live` | `Long` | `6.04` | 1,510,000.00 USD | 0.00 USD | 105.61 USD | `-27.60%` | `17.47` |
| `Live` | `Long` | `6.05` | 1,510,000.00 USD | 0.00 USD | 2,510.00 USD | `-27.48%` | `414.51` |
| `Live` | `Long` | `6.07` | 1,510,000.00 USD | 0.00 USD | 265.10 USD | `-27.36%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,510,000.00 USD | 0.00 USD | 1,690.00 USD | `-27.24%` | `278.94` |
| `Live` | `Long` | `6.08` | 1,500,000.00 USD | 0.00 USD | 405.14 USD | `-27.12%` | `66.58` |
| `Live` | `Long` | `6.09` | 1,500,000.00 USD | 0.00 USD | 3,130.00 USD | `-27.00%` | `512.81` |
| `Live` | `Long` | `6.11` | 1,500,000.00 USD | 0.00 USD | 1,090.00 USD | `-26.88%` | `178.97` |
| `Live` | `Long` | `6.12` | 1,500,000.00 USD | 0.00 USD | 1,140.00 USD | `-26.76%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,500,000.00 USD | 0.00 USD | 137.02 USD | `-26.64%` | `22.37` |
| `Live` | `Long` | `6.14` | 1,500,000.00 USD | 0.00 USD | 238.61 USD | `-26.40%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,500,000.00 USD | 0.00 USD | 4,390.00 USD | `-26.28%` | `713.75` |
| `Live` | `Long` | `6.17` | 1,490,000.00 USD | 0.00 USD | 187.29 USD | `-26.16%` | `30.38` |
| `Live` | `Long` | `6.17` | 1,490,000.00 USD | 0.00 USD | 104.36 USD | `-26.04%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,490,000.00 USD | 0.00 USD | 1,760.00 USD | `-25.68%` | `283.60` |
| `Live` | `Long` | `6.25` | 1,490,000.00 USD | 0.00 USD | 972.65 USD | `-25.08%` | `155.50` |
| `Live` | `Long` | `6.26` | 1,490,000.00 USD | 0.00 USD | 62,650.00 USD | `-24.96%` | `10,000.00` |
| `Live` | `Long` | `6.28` | 1,430,000.00 USD | 0.00 USD | 4,940.00 USD | `-24.84%` | `786.46` |
| `Live` | `Long` | `6.30` | 1,420,000.00 USD | 0.00 USD | 5,310.00 USD | `-24.48%` | `841.80` |
| `Live` | `Long` | `6.32` | 1,420,000.00 USD | 0.00 USD | 277.04 USD | `-24.36%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,420,000.00 USD | 0.00 USD | 4,470.00 USD | `-23.89%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,410,000.00 USD | 0.00 USD | 286,200.00 USD | `-23.77%` | `44,965.21` |
| `Live` | `Long` | `6.38` | 1,130,000.00 USD | 0.00 USD | 5,110.00 USD | `-23.65%` | `801.31` |
| `Live` | `Long` | `6.38` | 1,120,000.00 USD | 0.00 USD | 1,480.00 USD | `-23.53%` | `232.17` |
| `Live` | `Long` | `6.39` | 1,120,000.00 USD | 0.00 USD | 6,450.00 USD | `-23.41%` | `1,008.36` |
| `Live` | `Long` | `6.42` | 1,110,000.00 USD | 0.00 USD | 306.32 USD | `-23.17%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,110,000.00 USD | 0.00 USD | 2,120.00 USD | `-23.05%` | `330.00` |
| `Live` | `Long` | `6.43` | 1,110,000.00 USD | 0.00 USD | 6,780.00 USD | `-22.93%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,100,000.00 USD | 0.00 USD | 1,050.00 USD | `-22.57%` | `162.75` |
| `Live` | `Long` | `6.53` | 1,100,000.00 USD | 0.00 USD | 365,790.00 USD | `-21.85%` | `56,059.40` |
| `Live` | `Long` | `6.54` | 737,870.00 USD | 0.00 USD | 3,620.00 USD | `-21.73%` | `554.55` |
| `Live` | `Long` | `6.54` | 734,240.00 USD | 0.00 USD | 8,970.00 USD | `-21.61%` | `1,370.89` |
| `Live` | `Long` | `6.59` | 725,270.00 USD | 0.00 USD | 1,100.00 USD | `-21.01%` | `166.55` |
| `Live` | `Long` | `6.62` | 724,170.00 USD | 0.00 USD | 2,110.00 USD | `-20.77%` | `318.57` |
| `Live` | `Long` | `6.64` | 722,060.00 USD | 0.00 USD | 3,310.00 USD | `-20.41%` | `497.70` |
| `Live` | `Long` | `6.70` | 718,760.00 USD | 0.00 USD | 506.54 USD | `-19.81%` | `75.66` |
| `Live` | `Long` | `6.71` | 718,250.00 USD | 0.00 USD | 16,610.00 USD | `-19.69%` | `2,477.79` |
| `Live` | `Long` | `6.75` | 701,640.00 USD | 0.00 USD | 1,330.00 USD | `-19.21%` | `196.95` |
| `Live` | `Long` | `6.78` | 700,310.00 USD | 0.00 USD | 6,780.00 USD | `-18.86%` | `1,000.00` |
| `Live` | `Long` | `6.79` | 693,530.00 USD | 0.00 USD | 16,960.00 USD | `-18.74%` | `2,500.00` |
| `Live` | `Long` | `6.79` | 676,570.00 USD | 0.00 USD | 4,930.00 USD | `-18.62%` | `726.24` |
| `Live` | `Long` | `6.80` | 671,640.00 USD | 0.00 USD | 1,500.00 USD | `-18.50%` | `220.95` |
| `Live` | `Long` | `6.82` | 670,130.00 USD | 0.00 USD | 2,670.00 USD | `-18.38%` | `391.11` |
| `Live` | `Long` | `6.83` | 667,470.00 USD | 0.00 USD | 158.14 USD | `-18.26%` | `23.17` |
| `Live` | `Long` | `6.83` | 667,310.00 USD | 0.00 USD | 4,410.00 USD | `-18.14%` | `644.73` |
| `Live` | `Long` | `6.86` | 662,900.00 USD | 0.00 USD | 18,930.00 USD | `-17.90%` | `2,761.63` |
| `Live` | `Long` | `6.87` | 643,970.00 USD | 0.00 USD | 3,340.00 USD | `-17.78%` | `486.46` |
| `Live` | `Long` | `6.89` | 640,630.00 USD | 0.00 USD | 5,250.00 USD | `-17.42%` | `761.63` |
| `Live` | `Long` | `6.91` | 635,380.00 USD | 0.00 USD | 269.30 USD | `-17.30%` | `39.00` |
| `Live` | `Long` | `6.95` | 635,110.00 USD | 0.00 USD | 3,760.00 USD | `-16.82%` | `541.68` |
| `Live` | `Long` | `6.96` | 631,350.00 USD | 0.00 USD | 3,480.00 USD | `-16.70%` | `500.00` |
| `Live` | `Long` | `6.96` | 627,870.00 USD | 0.00 USD | 636.74 USD | `-16.58%` | `91.42` |
| `Live` | `Long` | `6.97` | 627,230.00 USD | 0.00 USD | 961.64 USD | `-16.46%` | `137.87` |
| `Live` | `Long` | `7.00` | 626,270.00 USD | 0.00 USD | 746.58 USD | `-16.22%` | `106.73` |
| `Live` | `Long` | `7.00` | 625,530.00 USD | 0.00 USD | 20,860.00 USD | `-16.10%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 604,670.00 USD | 0.00 USD | 1,860.00 USD | `-15.86%` | `265.15` |
| `Live` | `Long` | `7.04` | 602,800.00 USD | 0.00 USD | 704.50 USD | `-15.62%` | `100.00` |
| `Live` | `Long` | `7.08` | 602,100.00 USD | 0.00 USD | 6,700.00 USD | `-15.26%` | `947.44` |
| `Live` | `Long` | `7.08` | 595,390.00 USD | 0.00 USD | 1,420.00 USD | `-15.14%` | `201.02` |
| `Live` | `Long` | `7.11` | 593,970.00 USD | 0.00 USD | 28,230.00 USD | `-14.90%` | `3,972.61` |
| `Live` | `Long` | `7.12` | 565,750.00 USD | 0.00 USD | 30,390.00 USD | `-14.78%` | `4,271.06` |
| `Live` | `Long` | `7.13` | 535,360.00 USD | 0.00 USD | 2,300.00 USD | `-14.54%` | `322.72` |
| `Live` | `Long` | `7.14` | 533,050.00 USD | 0.00 USD | 21,700.00 USD | `-14.42%` | `3,037.00` |
| `Live` | `Long` | `7.18` | 511,350.00 USD | 0.00 USD | 1,440.00 USD | `-13.94%` | `200.00` |
| `Live` | `Long` | `7.21` | 509,920.00 USD | 0.00 USD | 581.02 USD | `-13.59%` | `80.53` |
| `Live` | `Long` | `7.24` | 509,340.00 USD | 0.00 USD | 179.65 USD | `-13.35%` | `24.83` |
| `Live` | `Long` | `7.25` | 509,160.00 USD | 0.00 USD | 185.83 USD | `-13.23%` | `25.65` |
| `Live` | `Long` | `7.26` | 508,970.00 USD | 0.00 USD | 419.41 USD | `-12.99%` | `57.73` |
| `Live` | `Long` | `7.29` | 508,550.00 USD | 0.00 USD | 38,400.00 USD | `-12.75%` | `5,271.15` |
| `Live` | `Long` | `7.33` | 470,150.00 USD | 0.00 USD | 4,910.00 USD | `-12.27%` | `669.93` |
| `Live` | `Long` | `7.34` | 465,240.00 USD | 0.00 USD | 4,370.00 USD | `-12.03%` | `594.84` |
| `Live` | `Long` | `7.36` | 460,870.00 USD | 0.00 USD | 848.25 USD | `-11.91%` | `115.33` |
| `Live` | `Long` | `7.37` | 460,030.00 USD | 0.00 USD | 23,820.00 USD | `-11.79%` | `3,234.39` |
| `Live` | `Long` | `7.38` | 436,210.00 USD | 0.00 USD | 3,920.00 USD | `-11.67%` | `531.65` |
| `Live` | `Long` | `7.39` | 432,280.00 USD | 0.00 USD | 1,550.00 USD | `-11.43%` | `210.17` |
| `Live` | `Long` | `7.42` | 430,730.00 USD | 0.00 USD | 500.00 USD | `-11.07%` | `67.34` |
| `Live` | `Long` | `7.45` | 430,230.00 USD | 0.00 USD | 210.99 USD | `-10.83%` | `28.34` |
| `Live` | `Long` | `7.46` | 430,020.00 USD | 0.00 USD | 4,590.00 USD | `-10.59%` | `614.36` |
| `Live` | `Long` | `7.47` | 425,430.00 USD | 0.00 USD | 1,120.00 USD | `-10.47%` | `149.52` |
| `Live` | `Long` | `7.50` | 424,320.00 USD | 0.00 USD | 1,110.00 USD | `-10.23%` | `147.46` |
| `Live` | `Long` | `7.50` | 423,210.00 USD | 0.00 USD | 421.78 USD | `-10.11%` | `56.20` |
| `Live` | `Long` | `7.53` | 422,790.00 USD | 0.00 USD | 995.86 USD | `-9.87%` | `132.34` |
| `Live` | `Long` | `7.54` | 421,790.00 USD | 0.00 USD | 4,210.00 USD | `-9.75%` | `559.01` |
| `Live` | `Long` | `7.54` | 417,580.00 USD | 0.00 USD | 3,230.00 USD | `-9.63%` | `428.41` |
| `Live` | `Long` | `7.55` | 414,350.00 USD | 0.00 USD | 1,210.00 USD | `-9.51%` | `160.80` |
| `Live` | `Long` | `7.57` | 413,130.00 USD | 0.00 USD | 26,630.00 USD | `-9.39%` | `3,520.32` |
| `Live` | `Long` | `7.58` | 386,500.00 USD | 0.00 USD | 118.25 USD | `-9.27%` | `15.61` |
| `Live` | `Long` | `7.59` | 386,380.00 USD | 0.00 USD | 25,140.00 USD | `-9.03%` | `3,310.14` |
| `Live` | `Long` | `7.62` | 361,240.00 USD | 0.00 USD | 312.22 USD | `-8.79%` | `41.00` |
| `Live` | `Long` | `7.62` | 360,930.00 USD | 0.00 USD | 787.51 USD | `-8.67%` | `103.28` |
| `Live` | `Long` | `7.63` | 360,140.00 USD | 0.00 USD | 378.93 USD | `-8.56%` | `49.63` |
| `Live` | `Long` | `7.66` | 359,760.00 USD | 0.00 USD | 1,410.00 USD | `-8.32%` | `184.81` |
| `Live` | `Long` | `7.67` | 358,350.00 USD | 0.00 USD | 1,740.00 USD | `-8.20%` | `226.45` |
| `Live` | `Long` | `7.67` | 356,610.00 USD | 0.00 USD | 140.45 USD | `-8.08%` | `18.30` |
| `Live` | `Long` | `7.68` | 356,470.00 USD | 0.00 USD | 1,120.00 USD | `-7.96%` | `145.25` |
| `Live` | `Long` | `7.70` | 355,360.00 USD | 0.00 USD | 1,460.00 USD | `-7.84%` | `190.36` |
| `Live` | `Long` | `7.72` | 353,890.00 USD | 0.00 USD | 2,550.00 USD | `-7.48%` | `330.65` |
| `Live` | `Long` | `7.74` | 351,340.00 USD | 0.00 USD | 1,370.00 USD | `-7.36%` | `176.90` |
| `Live` | `Long` | `7.76` | 349,970.00 USD | 0.00 USD | 455.73 USD | `-7.00%` | `58.69` |
| `Live` | `Long` | `7.78` | 349,510.00 USD | 0.00 USD | 695.32 USD | `-6.88%` | `89.43` |
| `Live` | `Long` | `7.79` | 348,820.00 USD | 0.00 USD | 2,870.00 USD | `-6.76%` | `368.38` |
| `Live` | `Long` | `7.79` | 345,950.00 USD | 0.00 USD | 1,940.00 USD | `-6.64%` | `248.84` |
| `Live` | `Long` | `7.82` | 344,010.00 USD | 0.00 USD | 3,720.00 USD | `-6.40%` | `475.43` |
| `Live` | `Long` | `7.84` | 340,300.00 USD | 0.00 USD | 35,270.00 USD | `-6.04%` | `4,496.09` |
| `Live` | `Long` | `7.86` | 305,020.00 USD | 0.00 USD | 2,110.00 USD | `-5.92%` | `269.14` |
| `Live` | `Long` | `7.87` | 302,910.00 USD | 0.00 USD | 1,590.00 USD | `-5.80%` | `202.23` |
| `Live` | `Long` | `7.88` | 301,320.00 USD | 0.00 USD | 555.19 USD | `-5.68%` | `70.50` |
| `Live` | `Long` | `7.88` | 300,760.00 USD | 0.00 USD | 9,300.00 USD | `-5.56%` | `1,179.30` |
| `Live` | `Long` | `7.89` | 291,470.00 USD | 0.00 USD | 2,250.00 USD | `-5.44%` | `284.70` |
| `Live` | `Long` | `7.91` | 289,220.00 USD | 0.00 USD | 505.13 USD | `-5.32%` | `63.90` |
| `Live` | `Long` | `7.93` | 288,710.00 USD | 0.00 USD | 16,340.00 USD | `-4.96%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 272,370.00 USD | 0.00 USD | 127,110.00 USD | `-4.84%` | `15,999.24` |
| `Live` | `Long` | `7.96` | 145,260.00 USD | 0.00 USD | 467.91 USD | `-4.72%` | `58.82` |
| `Live` | `Long` | `7.99` | 144,790.00 USD | 0.00 USD | 1,600.00 USD | `-4.36%` | `200.68` |
| `Live` | `Long` | `8.00` | 143,190.00 USD | 0.00 USD | 210.99 USD | `-4.24%` | `26.39` |
| `Live` | `Long` | `8.02` | 142,970.00 USD | 0.00 USD | 7,380.00 USD | `-4.00%` | `920.99` |
| `Live` | `Long` | `8.03` | 135,590.00 USD | 0.00 USD | 957.70 USD | `-3.88%` | `119.34` |
| `Live` | `Long` | `8.04` | 134,640.00 USD | 0.00 USD | 89,070.00 USD | `-3.76%` | `11,085.18` |
| `Live` | `Long` | `8.04` | 45,570.00 USD | 0.00 USD | 6,890.00 USD | `-3.64%` | `856.44` |
| `Live` | `Long` | `8.05` | 38,680.00 USD | 0.00 USD | 1,230.00 USD | `-3.52%` | `152.49` |
| `Live` | `Long` | `8.06` | 37,450.00 USD | 0.00 USD | 1,200.00 USD | `-3.41%` | `148.75` |
| `Live` | `Long` | `8.09` | 36,250.00 USD | 0.00 USD | 1,850.00 USD | `-3.17%` | `228.75` |
| `Live` | `Long` | `8.10` | 34,400.00 USD | 0.00 USD | 165.46 USD | `-3.05%` | `20.44` |
| `Live` | `Long` | `8.12` | 34,230.00 USD | 0.00 USD | 241.26 USD | `-2.81%` | `29.73` |
| `Live` | `Long` | `8.12` | 33,990.00 USD | 0.00 USD | 843.86 USD | `-2.69%` | `103.86` |
| `Live` | `Long` | `8.15` | 33,150.00 USD | 0.00 USD | 3,950.00 USD | `-2.33%` | `484.12` |
| `Live` | `Long` | `8.16` | 29,200.00 USD | 0.00 USD | 871.61 USD | `-2.21%` | `106.75` |
| `Live` | `Long` | `8.20` | 28,330.00 USD | 0.00 USD | 409.75 USD | `-1.85%` | `50.00` |
| `Live` | `Long` | `8.21` | 27,920.00 USD | 0.00 USD | 1,910.00 USD | `-1.73%` | `232.19` |
| `Live` | `Long` | `8.21` | 26,010.00 USD | 0.00 USD | 147.87 USD | `-1.61%` | `18.00` |
| `Live` | `Long` | `8.22` | 25,870.00 USD | 0.00 USD | 2,100.00 USD | `-1.49%` | `255.16` |
| `Live` | `Long` | `8.23` | 23,770.00 USD | 0.00 USD | 411.75 USD | `-1.37%` | `50.00` |
| `Live` | `Long` | `8.26` | 23,360.00 USD | 0.00 USD | 12,140.00 USD | `-1.13%` | `1,470.87` |
| `Live` | `Long` | `8.34` | 11,210.00 USD | 0.00 USD | 2,880.00 USD | `-0.17%` | `345.50` |
| `Live` | `Long` | `8.35` | 8,330.00 USD | 0.00 USD | 8,330.00 USD | `-0.05%` | `998.60` |
| `Live` | `Short` | `8.70` | 1,740.00 USD | 1,740.00 USD | 0.00 USD | `+4.14%` | `199.85` |
| `Live` | `Short` | `8.71` | 1,910.00 USD | 174.10 USD | 0.00 USD | `+4.26%` | `20.00` |
| `Live` | `Short` | `8.73` | 2,020.00 USD | 105.17 USD | 0.00 USD | `+4.62%` | `12.04` |
| `Live` | `Short` | `8.74` | 2,650.00 USD | 630.16 USD | 0.00 USD | `+4.74%` | `72.06` |
| `Live` | `Short` | `8.76` | 2,800.00 USD | 155.05 USD | 0.00 USD | `+4.86%` | `17.71` |
| `Live` | `Short` | `8.82` | 3,250.00 USD | 443.10 USD | 0.00 USD | `+5.70%` | `50.21` |
| `Live` | `Short` | `8.86` | 5,150.00 USD | 1,900.00 USD | 0.00 USD | `+6.06%` | `214.65` |
| `Live` | `Short` | `8.89` | 5,150.00 USD | 8.18 USD | 0.00 USD | `+6.54%` | `0.92` |
| `Live` | `Short` | `9.21` | 8,970.00 USD | 3,810.00 USD | 0.00 USD | `+10.37%` | `413.79` |
| `Live` | `Short` | `9.29` | 9,070.00 USD | 100.93 USD | 0.00 USD | `+11.21%` | `10.87` |
| `Live` | `Short` | `9.35` | 12,990.00 USD | 3,930.00 USD | 0.00 USD | `+11.93%` | `420.07` |
| `Live` | `Short` | `9.41` | 13,430.00 USD | 440.06 USD | 0.00 USD | `+12.76%` | `46.74` |
| `Live` | `Short` | `9.73` | 13,630.00 USD | 192.95 USD | 0.00 USD | `+16.60%` | `19.82` |
| `Live` | `Short` | `10.12` | 14,200.00 USD | 569.37 USD | 0.00 USD | `+21.15%` | `56.29` |
| `Live` | `Short` | `10.13` | 14,680.00 USD | 487.49 USD | 0.00 USD | `+21.39%` | `48.10` |
| `Live` | `Short` | `10.21` | 17,910.00 USD | 3,230.00 USD | 0.00 USD | `+22.35%` | `316.22` |
| `Live` | `Short` | `10.23` | 18,030.00 USD | 114.12 USD | 0.00 USD | `+22.59%` | `11.15` |
| `Live` | `Short` | `10.29` | 275,160.00 USD | 257,130.00 USD | 0.00 USD | `+23.18%` | `25,000.94` |
| `Live` | `Short` | `10.35` | 275,570.00 USD | 405.42 USD | 0.00 USD | `+23.90%` | `39.19` |
| `Live` | `Short` | `10.56` | 276,090.00 USD | 523.81 USD | 0.00 USD | `+26.54%` | `49.58` |
| `Live` | `Short` | `10.71` | 276,310.00 USD | 218.91 USD | 0.00 USD | `+28.33%` | `20.43` |
| `Live` | `Short` | `10.96` | 278,230.00 USD | 1,920.00 USD | 0.00 USD | `+31.33%` | `174.67` |
| `Live` | `Short` | `11.01` | 285,190.00 USD | 6,970.00 USD | 0.00 USD | `+31.81%` | `633.00` |
| `Live` | `Short` | `11.12` | 287,610.00 USD | 2,420.00 USD | 0.00 USD | `+33.24%` | `217.39` |
| `Live` | `Short` | `11.27` | 299,280.00 USD | 11,670.00 USD | 0.00 USD | `+34.92%` | `1,035.87` |
| `Live` | `Short` | `11.53` | 356,900.00 USD | 57,620.00 USD | 0.00 USD | `+38.04%` | `5,000.00` |
| `Live` | `Short` | `11.62` | 369,040.00 USD | 12,140.00 USD | 0.00 USD | `+39.23%` | `1,043.90` |
| `Live` | `Short` | `11.63` | 409,330.00 USD | 40,290.00 USD | 0.00 USD | `+39.35%` | `3,462.73` |
| `Live` | `Short` | `11.69` | 706,090.00 USD | 296,760.00 USD | 0.00 USD | `+39.95%` | `25,397.02` |
| `Live` | `Short` | `12.05` | 706,900.00 USD | 802.86 USD | 0.00 USD | `+44.38%` | `66.60` |
| `Live` | `Short` | `12.30` | 708,630.00 USD | 1,730.00 USD | 0.00 USD | `+47.38%` | `140.71` |
| `Live` | `Short` | `12.40` | 708,970.00 USD | 343.62 USD | 0.00 USD | `+48.58%` | `27.70` |
| `Live` | `Short` | `12.62` | 710,410.00 USD | 1,440.00 USD | 0.00 USD | `+51.21%` | `113.77` |
| `Live` | `Short` | `13.04` | 710,850.00 USD | 444.83 USD | 0.00 USD | `+56.24%` | `34.10` |
| `Live` | `Short` | `13.20` | 798,800.00 USD | 87,940.00 USD | 0.00 USD | `+58.04%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 802,610.00 USD | 3,810.00 USD | 0.00 USD | `+59.23%` | `286.56` |
| `Live` | `Short` | `13.46` | 803,040.00 USD | 430.34 USD | 0.00 USD | `+61.27%` | `31.96` |
| `Live` | `Short` | `13.69` | 803,210.00 USD | 172.29 USD | 0.00 USD | `+63.91%` | `12.59` |
| `Live` | `Short` | `13.95` | 843,370.00 USD | 40,160.00 USD | 0.00 USD | `+67.02%` | `2,879.71` |
| `Live` | `Short` | `14.01` | 859,050.00 USD | 15,690.00 USD | 0.00 USD | `+67.74%` | `1,120.14` |
| `Live` | `Short` | `14.40` | 859,340.00 USD | 284.21 USD | 0.00 USD | `+72.53%` | `19.73` |
| `Live` | `Short` | `14.66` | 860,160.00 USD | 823.29 USD | 0.00 USD | `+75.64%` | `56.14` |
| `Live` | `Short` | `15.18` | 864,370.00 USD | 4,210.00 USD | 0.00 USD | `+81.75%` | `277.54` |
| `Live` | `Short` | `15.29` | 867,140.00 USD | 2,770.00 USD | 0.00 USD | `+83.19%` | `181.16` |
| `Live` | `Short` | `15.34` | 867,400.00 USD | 251.65 USD | 0.00 USD | `+83.67%` | `16.41` |
| `Live` | `Short` | `15.35` | 867,630.00 USD | 230.17 USD | 0.00 USD | `+83.79%` | `15.00` |
| `Live` | `Short` | `15.38` | 887,630.00 USD | 20,000.00 USD | 0.00 USD | `+84.27%` | `1,300.00` |
| `Live` | `Short` | `15.70` | 887,960.00 USD | 338.23 USD | 0.00 USD | `+87.98%` | `21.55` |
| `Live` | `Short` | `16.30` | 889,520.00 USD | 1,550.00 USD | 0.00 USD | `+95.29%` | `95.35` |
| `Live` | `Short` | `16.36` | 1,150,000.00 USD | 265,240.00 USD | 0.00 USD | `+96.00%` | `16,208.00` |
| `Live` | `Short` | `16.39` | 1,320,000.00 USD | 163,850.00 USD | 0.00 USD | `+96.24%` | `10,000.00` |
| `Live` | `Short` | `16.41` | 1,320,000.00 USD | 116.71 USD | 0.00 USD | `+96.60%` | `7.11` |
| `Live` | `Short` | `16.43` | 1,340,000.00 USD | 22,580.00 USD | 0.00 USD | `+96.84%` | `1,373.91` |
| `Live` | `Short` | `16.52` | 1,340,000.00 USD | 190.91 USD | 0.00 USD | `+97.80%` | `11.56` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 238,220.00 USD | 0.00 USD | 611.73 USD | `-72.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 237,600.00 USD | 0.00 USD | 793.75 USD | `-52.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 236,810.00 USD | 0.00 USD | 105.04 USD | `-46.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 236,700.00 USD | 0.00 USD | 67,970.00 USD | `-40.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 168,740.00 USD | 0.00 USD | 205.30 USD | `-36.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 168,530.00 USD | 0.00 USD | 465.42 USD | `-34.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 168,070.00 USD | 0.00 USD | 349.35 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 167,720.00 USD | 0.00 USD | 1,330.00 USD | `-30.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 166,390.00 USD | 0.00 USD | 493.50 USD | `-28.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 165,900.00 USD | 0.00 USD | 100.98 USD | `-28.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 165,800.00 USD | 0.00 USD | 500.70 USD | `-28.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 165,290.00 USD | 0.00 USD | 4,160.00 USD | `-26.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 161,140.00 USD | 0.00 USD | 6,500.00 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 154,640.00 USD | 0.00 USD | 864.38 USD | `-24.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 153,770.00 USD | 0.00 USD | 1,760.00 USD | `-22.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 152,020.00 USD | 0.00 USD | 4,340.00 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 147,680.00 USD | 0.00 USD | 5,520.00 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 142,150.00 USD | 0.00 USD | 100.72 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 142,050.00 USD | 0.00 USD | 296.34 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 141,760.00 USD | 0.00 USD | 921.19 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 140,840.00 USD | 0.00 USD | 709.98 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 140,130.00 USD | 0.00 USD | 691.50 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 139,430.00 USD | 0.00 USD | 262.44 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 139,170.00 USD | 0.00 USD | 1,820.00 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 137,350.00 USD | 0.00 USD | 6,790.00 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 130,560.00 USD | 0.00 USD | 9,770.00 USD | `-14.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 120,800.00 USD | 0.00 USD | 103.46 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 120,690.00 USD | 0.00 USD | 603.44 USD | `-13.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 120,090.00 USD | 0.00 USD | 891.57 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 119,200.00 USD | 0.00 USD | 2,090.00 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 117,100.00 USD | 0.00 USD | 129.58 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 116,970.00 USD | 0.00 USD | 236.19 USD | `-12.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 116,740.00 USD | 0.00 USD | 199.39 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 116,540.00 USD | 0.00 USD | 4,730.00 USD | `-10.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 111,810.00 USD | 0.00 USD | 37,420.00 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 74,380.00 USD | 0.00 USD | 778.49 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 73,600.00 USD | 0.00 USD | 799.83 USD | `-9.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 72,800.00 USD | 0.00 USD | 820.44 USD | `-9.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.57` | 71,980.00 USD | 0.00 USD | 103.41 USD | `-9.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 71,880.00 USD | 0.00 USD | 1,370.00 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 70,510.00 USD | 0.00 USD | 915.17 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 69,590.00 USD | 0.00 USD | 360.13 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 69,230.00 USD | 0.00 USD | 578.04 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 68,650.00 USD | 0.00 USD | 175.42 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 68,480.00 USD | 0.00 USD | 3,390.00 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 65,090.00 USD | 0.00 USD | 143.51 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 64,950.00 USD | 0.00 USD | 183.33 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.88` | 64,760.00 USD | 0.00 USD | 194.52 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 64,570.00 USD | 0.00 USD | 552.65 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 64,020.00 USD | 0.00 USD | 12,170.00 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 51,850.00 USD | 0.00 USD | 1,590.00 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 50,270.00 USD | 0.00 USD | 1,370.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 48,890.00 USD | 0.00 USD | 3,990.00 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 44,900.00 USD | 0.00 USD | 1,350.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 43,550.00 USD | 0.00 USD | 8,780.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 34,770.00 USD | 0.00 USD | 123.58 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 34,650.00 USD | 0.00 USD | 2,110.00 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 32,540.00 USD | 0.00 USD | 563.85 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 31,980.00 USD | 0.00 USD | 121.69 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 31,850.00 USD | 0.00 USD | 477.36 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 31,380.00 USD | 0.00 USD | 2,330.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 29,040.00 USD | 0.00 USD | 184.13 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 28,860.00 USD | 0.00 USD | 6,500.00 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 22,360.00 USD | 0.00 USD | 968.39 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 21,390.00 USD | 0.00 USD | 654.53 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 20,730.00 USD | 0.00 USD | 1,750.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 18,980.00 USD | 0.00 USD | 520.75 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 18,460.00 USD | 0.00 USD | 3,020.00 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 15,440.00 USD | 0.00 USD | 141.04 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 15,300.00 USD | 0.00 USD | 3,840.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 11,460.00 USD | 0.00 USD | 515.66 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 10,940.00 USD | 0.00 USD | 143.54 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 10,800.00 USD | 0.00 USD | 168.64 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 10,630.00 USD | 0.00 USD | 201.49 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 10,430.00 USD | 0.00 USD | 6,530.00 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 3,900.00 USD | 0.00 USD | 1,140.00 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 2,760.00 USD | 0.00 USD | 2,000.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 756.06 USD | 0.00 USD | 756.06 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.36` | 970.35 USD | 970.35 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 6,440.00 USD | 5,470.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 8,400.00 USD | 1,970.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 11,690.00 USD | 3,290.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.41` | 12,050.00 USD | 358.56 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.43` | 13,930.00 USD | 1,880.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 14,070.00 USD | 140.36 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.45` | 14,210.00 USD | 138.24 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 15,160.00 USD | 954.23 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 15,930.00 USD | 769.61 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 16,420.00 USD | 489.58 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 17,870.00 USD | 1,440.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 18,070.00 USD | 198.74 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 19,190.00 USD | 1,130.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 19,700.00 USD | 510.39 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 24,110.00 USD | 4,400.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 24,350.00 USD | 243.82 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 24,780.00 USD | 428.58 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 27,280.00 USD | 2,500.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 27,720.00 USD | 435.59 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 28,790.00 USD | 1,080.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 30,770.00 USD | 1,980.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 33,520.00 USD | 2,740.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 33,620.00 USD | 103.19 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 33,720.00 USD | 103.31 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 35,630.00 USD | 1,900.00 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 35,940.00 USD | 307.87 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 36,160.00 USD | 223.82 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 37,150.00 USD | 990.09 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 42,160.00 USD | 5,010.00 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 49,040.00 USD | 6,880.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 49,180.00 USD | 134.30 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 49,570.00 USD | 390.88 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 49,900.00 USD | 333.07 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 50,840.00 USD | 933.70 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 57,130.00 USD | 6,300.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 96,940.00 USD | 39,810.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 97,060.00 USD | 114.25 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 97,450.00 USD | 388.12 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 98,160.00 USD | 711.78 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 99,920.00 USD | 1,760.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.81` | 100,620.00 USD | 705.20 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 102,660.00 USD | 2,030.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 102,900.00 USD | 243.40 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 108,660.00 USD | 5,760.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 108,860.00 USD | 192.86 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 109,470.00 USD | 614.88 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 115,500.00 USD | 6,020.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 116,600.00 USD | 1,100.00 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 116,790.00 USD | 188.66 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 117,580.00 USD | 788.72 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 119,510.00 USD | 1,940.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 119,680.00 USD | 163.33 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 120,460.00 USD | 782.17 USD | 0.00 USD | `+7.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 120,680.00 USD | 223.62 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 120,820.00 USD | 137.73 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 121,220.00 USD | 401.63 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 436,370.00 USD | 315,150.00 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 436,480.00 USD | 104.59 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 437,260.00 USD | 776.54 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 437,790.00 USD | 531.20 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 439,160.00 USD | 1,380.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 440,250.00 USD | 1,090.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 440,870.00 USD | 616.37 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 440,970.00 USD | 102.03 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 441,420.00 USD | 453.84 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 441,590.00 USD | 160.99 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 442,000.00 USD | 415.00 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 443,510.00 USD | 1,510.00 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 445,550.00 USD | 2,040.00 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 673,180.00 USD | 227,630.00 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 677,740.00 USD | 4,560.00 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 679,740.00 USD | 2,000.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,070,000.00 USD | 394,210.00 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,070,000.00 USD | 119.24 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.20` | 1,080,000.00 USD | 1,590.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,080,000.00 USD | 2,660.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,080,000.00 USD | 131.87 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,080,000.00 USD | 687.91 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,080,000.00 USD | 954.71 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,310,000.00 USD | 231,380.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.27` | 1,310,000.00 USD | 205.87 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,310,000.00 USD | 1,960.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,310,000.00 USD | 434.45 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,330,000.00 USD | 18,610.00 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,330,000.00 USD | 166.83 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,340,000.00 USD | 2,180.00 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,340,000.00 USD | 579.86 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,660,000.00 USD | 327,430.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,660,000.00 USD | 116.69 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,660,000.00 USD | 163.41 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,660,000.00 USD | 1,150.00 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,670,000.00 USD | 660.84 USD | 0.00 USD | `+12.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,670,000.00 USD | 714.59 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,670,000.00 USD | 928.13 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,670,000.00 USD | 102.45 USD | 0.00 USD | `+12.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,670,000.00 USD | 219.84 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,670,000.00 USD | 140.35 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,670,000.00 USD | 1,890.00 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.47` | 1,670,000.00 USD | 1,780.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,670,000.00 USD | 2,210.00 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,670,000.00 USD | 288.46 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.51` | 1,680,000.00 USD | 1,600.00 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,680,000.00 USD | 223.46 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,680,000.00 USD | 231.00 USD | 0.00 USD | `+14.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,680,000.00 USD | 221.07 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,680,000.00 USD | 1,470.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,680,000.00 USD | 148.48 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,680,000.00 USD | 191.36 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,680,000.00 USD | 446.58 USD | 0.00 USD | `+16.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,680,000.00 USD | 108.21 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,680,000.00 USD | 169.68 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,680,000.00 USD | 574.66 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,680,000.00 USD | 121.87 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.80` | 1,680,000.00 USD | 619.28 USD | 0.00 USD | `+17.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,680,000.00 USD | 5,030.00 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,680,000.00 USD | 340.05 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,690,000.00 USD | 742.12 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,690,000.00 USD | 899.47 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,760,000.00 USD | 70,020.00 USD | 0.00 USD | `+18.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,760,000.00 USD | 373.97 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,760,000.00 USD | 3,050.00 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,770,000.00 USD | 6,370.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,770,000.00 USD | 202.10 USD | 0.00 USD | `+21.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,980,000.00 USD | 210,980.00 USD | 0.00 USD | `+21.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,980,000.00 USD | 1,150.00 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,980,000.00 USD | 172.16 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,980,000.00 USD | 895.21 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,980,000.00 USD | 489.40 USD | 0.00 USD | `+23.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,980,000.00 USD | 1,200.00 USD | 0.00 USD | `+24.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,980,000.00 USD | 118.01 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,980,000.00 USD | 312.31 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,980,000.00 USD | 2,290.00 USD | 0.00 USD | `+25.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,980,000.00 USD | 178.46 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.62` | 1,980,000.00 USD | 153.11 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,980,000.00 USD | 173.42 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,980,000.00 USD | 184.75 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,990,000.00 USD | 135.78 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,990,000.00 USD | 127.96 USD | 0.00 USD | `+29.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,990,000.00 USD | 476.43 USD | 0.00 USD | `+30.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,990,000.00 USD | 667.39 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,990,000.00 USD | 118.97 USD | 0.00 USD | `+30.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,990,000.00 USD | 251.06 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,990,000.00 USD | 552.44 USD | 0.00 USD | `+30.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,990,000.00 USD | 537.26 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,990,000.00 USD | 320.29 USD | 0.00 USD | `+33.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,990,000.00 USD | 1,100.00 USD | 0.00 USD | `+33.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,990,000.00 USD | 2,610.00 USD | 0.00 USD | `+34.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,990,000.00 USD | 1,270.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,990,000.00 USD | 1,380.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 2,000,000.00 USD | 2,410.00 USD | 0.00 USD | `+36.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 2,010,000.00 USD | 9,520.00 USD | 0.00 USD | `+37.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 2,010,000.00 USD | 1,190.00 USD | 0.00 USD | `+37.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 2,010,000.00 USD | 316.04 USD | 0.00 USD | `+37.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 2,020,000.00 USD | 7,700.00 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 2,020,000.00 USD | 1,130.00 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 2,020,000.00 USD | 434.61 USD | 0.00 USD | `+42.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 2,020,000.00 USD | 163.52 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,140,000.00 USD | 123,650.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.51` | 2,140,000.00 USD | 2,770.00 USD | 0.00 USD | `+49.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,150,000.00 USD | 3,350.00 USD | 0.00 USD | `+52.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,150,000.00 USD | 197.97 USD | 0.00 USD | `+53.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,150,000.00 USD | 3,200.00 USD | 0.00 USD | `+54.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,150,000.00 USD | 179.58 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,150,000.00 USD | 720.74 USD | 0.00 USD | `+55.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.07` | 2,150,000.00 USD | 504.17 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,150,000.00 USD | 169.57 USD | 0.00 USD | `+57.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.30` | 2,150,000.00 USD | 159.66 USD | 0.00 USD | `+59.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,150,000.00 USD | 446.52 USD | 0.00 USD | `+60.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.46` | 2,150,000.00 USD | 1,710.00 USD | 0.00 USD | `+61.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,160,000.00 USD | 5,320.00 USD | 0.00 USD | `+61.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,370,000.00 USD | 207,980.00 USD | 0.00 USD | `+61.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,370,000.00 USD | 407.95 USD | 0.00 USD | `+63.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,370,000.00 USD | 174.91 USD | 0.00 USD | `+65.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,380,000.00 USD | 8,370.00 USD | 0.00 USD | `+67.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,380,000.00 USD | 960.26 USD | 0.00 USD | `+70.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,380,000.00 USD | 2,710.00 USD | 0.00 USD | `+71.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,380,000.00 USD | 805.90 USD | 0.00 USD | `+73.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,380,000.00 USD | 655.55 USD | 0.00 USD | `+76.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,390,000.00 USD | 4,890.00 USD | 0.00 USD | `+77.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,390,000.00 USD | 471.09 USD | 0.00 USD | `+78.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,390,000.00 USD | 383.85 USD | 0.00 USD | `+79.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 3,040,000.00 USD | 652,670.00 USD | 0.00 USD | `+79.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 3,040,000.00 USD | 1,510.00 USD | 0.00 USD | `+80.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 3,040,000.00 USD | 111.87 USD | 0.00 USD | `+89.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 3,040,000.00 USD | 219.91 USD | 0.00 USD | `+91.69%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.36` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 6,810.00 USD | 2,430.00 USD | 0.00 USD |
| `7D` | `7.38` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 21.18 USD |
| `7D` | `7.40` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 6,810.00 USD | 0.00 USD | 29.59 USD |
| `7D` | `7.42` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 18.85 USD |
| `7D` | `7.44` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 331.70 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `7.46` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 723.17 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.46` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 1,410.00 USD | 3,890.00 USD |
| `7D` | `7.48` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 9,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.52` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 9,830.00 USD | 7,230.00 USD | 0.00 USD |
| `7D` | `7.54` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `7.56` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.60` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 3,770.00 USD | 74.23 USD |
| `1D` | `7.62` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 5,440.00 USD |
| `1D` | `7.64` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 986.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.66` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 10,150.00 USD |
| `1D` | `7.70` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 321.75 USD | 2,390.00 USD | 4,010.00 USD |
| `1D` | `7.72` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 4,160.00 USD | 1,630.00 USD | 12,390.00 USD |
| `7D` | `7.72` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 32,590.00 USD |
| `1D` | `7.74` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 2,950.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `7.74` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 976.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.76` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,510.00 USD | 1,100.00 USD | 5,380.00 USD |
| `7D` | `7.76` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 812.95 USD | 5,760.00 USD | 0.00 USD |
| `1D` | `7.78` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 42,650.00 USD | 3,730.00 USD | 8,950.00 USD |
| `7D` | `7.78` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 43,620.00 USD | 4,900.00 USD | 20,160.00 USD |
| `1D` | `7.80` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 38,450.00 USD | 10,860.00 USD | 8,320.00 USD |
| `7D` | `7.80` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 13,050.00 USD | 12,980.00 USD | 174.42 USD |
| `1D` | `7.82` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 5,100.00 USD | 7,610.00 USD | 5,600.00 USD |
| `7D` | `7.82` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 1,450.00 USD | 5,260.00 USD | 4,280.00 USD |
| `1D` | `7.84` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 671.45 USD | 4,910.00 USD | 12,620.00 USD |
| `7D` | `7.84` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 29,020.00 USD | 2,380.00 USD | 25,390.00 USD |
| `1D` | `7.86` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 14,500.00 USD | 1,680.00 USD | 16,260.00 USD |
| `7D` | `7.86` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 25,770.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.88` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 43,790.00 USD | 9,570.00 USD | 22,590.00 USD |
| `7D` | `7.88` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 58,120.00 USD | 12,780.00 USD | 29,280.00 USD |
| `1D` | `7.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 14,150.00 USD | 7,630.00 USD | 7,480.00 USD |
| `7D` | `7.90` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,670.00 USD |
| `1D` | `7.92` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 19,860.00 USD | 2,950.00 USD | 6,190.00 USD |
| `7D` | `7.92` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 53,660.00 USD | 8,420.00 USD | 13,660.00 USD |
| `1D` | `7.94` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD |
| `7D` | `7.94` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 49,080.00 USD | 9,960.00 USD | 32,220.00 USD |
| `1D` | `7.96` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD |
| `7D` | `7.96` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 21,840.00 USD | 6,920.00 USD | 26,140.00 USD |
| `1D` | `7.98` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 14,350.00 USD | 3,300.00 USD | 8,480.00 USD |
| `7D` | `7.98` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 54,090.00 USD | 19,680.00 USD | 70,090.00 USD |
| `1D` | `8.00` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 570.55 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `8.00` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 61,850.00 USD | 10,300.00 USD | 5,230.00 USD |
| `1D` | `8.02` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 40,190.00 USD | 8,470.00 USD | 157.85 USD |
| `7D` | `8.02` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 20,910.00 USD | 28,440.00 USD | 10,280.00 USD |
| `1D` | `8.04` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 19,460.00 USD | 11,910.00 USD | 6,480.00 USD |
| `7D` | `8.04` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 123,080.00 USD | 38,980.00 USD | 86,690.00 USD |
| `1D` | `8.06` | 989,160.00 USD | 0.00 USD | 989,160.00 USD | 27,730.00 USD | 9,400.00 USD | 6,210.00 USD |
| `7D` | `8.06` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 70,840.00 USD | 20,850.00 USD | 85,760.00 USD |
| `1D` | `8.08` | 945,820.00 USD | 0.00 USD | 945,820.00 USD | 22,320.00 USD | 3,810.00 USD | 4,750.00 USD |
| `7D` | `8.08` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 7,170.00 USD | 8,710.00 USD | 21,540.00 USD |
| `1D` | `8.10` | 914,940.00 USD | 0.00 USD | 914,940.00 USD | 32,980.00 USD | 13,380.00 USD | 7,840.00 USD |
| `7D` | `8.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 61,500.00 USD | 19,700.00 USD | 14,150.00 USD |
| `1D` | `8.12` | 860,740.00 USD | 0.00 USD | 860,740.00 USD | 12,010.00 USD | 4,240.00 USD | 22,190.00 USD |
| `7D` | `8.12` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 27,520.00 USD | 10,810.00 USD | 9,550.00 USD |
| `1D` | `8.14` | 822,300.00 USD | 0.00 USD | 822,300.00 USD | 20,690.00 USD | 0.00 USD | 42.96 USD |
| `7D` | `8.14` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 72,460.00 USD | 11,150.00 USD | 39,640.00 USD |
| `1D` | `8.16` | 801,570.00 USD | 0.00 USD | 801,570.00 USD | 11,720.00 USD | 662.47 USD | 9,020.00 USD |
| `7D` | `8.16` | 904,400.00 USD | 0.00 USD | 904,400.00 USD | 38,430.00 USD | 5,510.00 USD | 29,970.00 USD |
| `1D` | `8.18` | 780,160.00 USD | 0.00 USD | 780,160.00 USD | 53,280.00 USD | 15,390.00 USD | 478.53 USD |
| `7D` | `8.18` | 830,490.00 USD | 0.00 USD | 830,490.00 USD | 10,520.00 USD | 6,790.00 USD | 29,370.00 USD |
| `1D` | `8.20` | 711,010.00 USD | 0.00 USD | 711,010.00 USD | 7,430.00 USD | 20,740.00 USD | 448.46 USD |
| `7D` | `8.20` | 783,810.00 USD | 0.00 USD | 783,810.00 USD | 33,800.00 USD | 22,240.00 USD | 9,410.00 USD |
| `1D` | `8.22` | 682,390.00 USD | 0.00 USD | 682,390.00 USD | 7,650.00 USD | 13,850.00 USD | 10,040.00 USD |
| `7D` | `8.22` | 718,360.00 USD | 0.00 USD | 718,360.00 USD | 19,610.00 USD | 21,570.00 USD | 10,160.00 USD |
| `1D` | `8.24` | 650,850.00 USD | 0.00 USD | 650,850.00 USD | 65,360.00 USD | 5,230.00 USD | 34,520.00 USD |
| `7D` | `8.24` | 667,020.00 USD | 0.00 USD | 667,020.00 USD | 39,950.00 USD | 3,480.00 USD | 108,450.00 USD |
| `1D` | `8.26` | 545,740.00 USD | 0.00 USD | 545,740.00 USD | 15,150.00 USD | 11,460.00 USD | 6,100.00 USD |
| `7D` | `8.26` | 515,150.00 USD | 0.00 USD | 515,150.00 USD | 30,490.00 USD | 5,750.00 USD | 1,640.00 USD |
| `1D` | `8.28` | 513,030.00 USD | 0.00 USD | 513,030.00 USD | 137,750.00 USD | 28,700.00 USD | 79,900.00 USD |
| `7D` | `8.28` | 477,280.00 USD | 0.00 USD | 477,280.00 USD | 122,850.00 USD | 33,920.00 USD | 22,920.00 USD |
| `1D` | `8.30` | 266,680.00 USD | 0.00 USD | 266,680.00 USD | 94,260.00 USD | 22,600.00 USD | 23,810.00 USD |
| `7D` | `8.30` | 297,590.00 USD | 0.00 USD | 297,590.00 USD | 152,370.00 USD | 11,360.00 USD | 48,420.00 USD |
| `1D` | `8.32` | 126,010.00 USD | 0.00 USD | 126,010.00 USD | 73,190.00 USD | 20,010.00 USD | 8,890.00 USD |
| `7D` | `8.32` | 85,430.00 USD | 0.00 USD | 85,430.00 USD | 61,580.00 USD | 21,100.00 USD | 2,750.00 USD |
| `1D` | `8.34` | 23,920.00 USD | 0.00 USD | 23,920.00 USD | 0.00 USD | 0.00 USD | 23,920.00 USD |
| `7D` | `8.34` | 124,260.00 USD | 124,260.00 USD | 0.00 USD | 28,220.00 USD | 10,180.00 USD | 85,860.00 USD |
| `7D` | `8.34` | 248,510.00 USD | 248,510.00 USD | 0.00 USD | 28,220.00 USD | 10,180.00 USD | 85,860.00 USD |
| `1D` | `8.36` | 39,690.00 USD | 39,690.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 37,880.00 USD |
| `1D` | `8.36` | 79,380.00 USD | 79,380.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 37,880.00 USD |
| `7D` | `8.36` | 436,630.00 USD | 436,630.00 USD | 0.00 USD | 107,760.00 USD | 0.00 USD | 80,350.00 USD |
| `1D` | `8.38` | 132,920.00 USD | 132,920.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 52,030.00 USD |
| `7D` | `8.38` | 648,520.00 USD | 648,520.00 USD | 0.00 USD | 143,540.00 USD | 0.00 USD | 68,350.00 USD |
| `1D` | `8.40` | 197,330.00 USD | 197,330.00 USD | 0.00 USD | 1,220.00 USD | 0.00 USD | 63,190.00 USD |
| `7D` | `8.40` | 862,720.00 USD | 862,720.00 USD | 0.00 USD | 179,510.00 USD | 0.00 USD | 34,680.00 USD |
| `1D` | `8.42` | 198,330.00 USD | 198,330.00 USD | 0.00 USD | 995.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.42` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 178,300.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `8.44` | 198,760.00 USD | 198,760.00 USD | 0.00 USD | 427.96 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.44` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 155,040.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `8.46` | 198,780.00 USD | 198,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.78 USD |
| `7D` | `8.46` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 392,550.00 USD | 0.00 USD | 3,610.00 USD |
| `1D` | `8.48` | 237,960.00 USD | 237,960.00 USD | 0.00 USD | 0.00 USD | 39,180.00 USD | 0.00 USD |
| `7D` | `8.48` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 477,600.00 USD | 35,130.00 USD | 1,880.00 USD |
| `1D` | `8.50` | 503,470.00 USD | 503,470.00 USD | 0.00 USD | 206,180.00 USD | 59,320.00 USD | 12.70 USD |
| `7D` | `8.50` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 218,140.00 USD | 100,070.00 USD | 936.55 USD |
| `1D` | `8.52` | 692,470.00 USD | 692,470.00 USD | 0.00 USD | 123,250.00 USD | 65,750.00 USD | 1.32 USD |
| `7D` | `8.52` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 270,540.00 USD | 98,920.00 USD | 0.00 USD |
| `1D` | `8.54` | 748,580.00 USD | 748,580.00 USD | 0.00 USD | 35,370.00 USD | 20,740.00 USD | 0.00 USD |
| `7D` | `8.54` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 379,850.00 USD | 100,610.00 USD | 0.00 USD |
| `1D` | `8.56` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 158,900.00 USD | 7,860.00 USD | 106,490.00 USD |
| `7D` | `8.56` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 593,510.00 USD | 122,650.00 USD | 0.00 USD |
| `1D` | `8.58` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 136,600.00 USD | 0.00 USD | 144,480.00 USD |
| `7D` | `8.58` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 599,490.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 53,060.00 USD | 65,000.00 USD |
| `7D` | `8.60` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 75,040.00 USD | 39,160.00 USD | 0.00 USD |
| `1D` | `8.62` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 28,330.00 USD | 54,800.00 USD | 27,290.00 USD |
| `7D` | `8.62` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 43,670.00 USD | 0.00 USD |
| `1D` | `8.64` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 21,050.00 USD | 0.00 USD |
| `7D` | `8.64` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD |
| `1D` | `8.66` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,010.00 USD |
| `7D` | `8.66` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | 0.00 USD |
| `1D` | `8.68` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 24,580.00 USD | 7,700.00 USD | 39,650.00 USD |
| `7D` | `8.68` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 148,470.00 USD | 24,870.00 USD | 223,330.00 USD |
| `1D` | `8.70` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 36,540.00 USD | 10,370.00 USD | 22,180.00 USD |
| `7D` | `8.70` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 23,910.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.74` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 15,900.00 USD | 0.00 USD |
| `7D` | `8.74` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.76` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 97,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.76` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,490.00 USD |
| `1D` | `8.78` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 107,520.00 USD | 9,440.00 USD | 35,600.00 USD |
| `7D` | `8.78` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 58,840.00 USD |
| `1D` | `8.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 61,700.00 USD | 17,690.00 USD | 37,430.00 USD |
| `7D` | `8.80` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 18,460.00 USD |
| `1D` | `8.82` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.82` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 100,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD | 68,750.00 USD |
| `1D` | `8.86` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 12,400.00 USD | 2,250.00 USD | 148.46 USD |
| `7D` | `8.86` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,360.00 USD |
| `1D` | `8.88` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD |
| `7D` | `8.88` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.90` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 29,560.00 USD | 8,140.00 USD | 97,330.00 USD |
| `7D` | `8.90` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.92` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 37,770.00 USD | 7,360.00 USD | 17,020.00 USD |
| `7D` | `8.92` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,620.00 USD |
| `1D` | `8.94` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 41,740.00 USD | 12,260.00 USD | 17,500.00 USD |
| `7D` | `8.94` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 58,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.98` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 24,340.00 USD | 5,550.00 USD | 19,410.00 USD |
| `7D` | `8.98` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `9.00` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 85,360.00 USD | 30,520.00 USD | 11,130.00 USD |
| `7D` | `9.00` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 297,650.00 USD | 11,360.00 USD | 20,780.00 USD |
| `1D` | `9.02` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 39,130.00 USD | 43,160.00 USD | 18,840.00 USD |
| `7D` | `9.02` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 34,650.00 USD | 56,120.00 USD | 0.00 USD |
| `1D` | `9.04` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 87,540.00 USD | 43,590.00 USD | 38,590.00 USD |
| `7D` | `9.04` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 90,520.00 USD | 74,750.00 USD | 15,490.00 USD |
| `1D` | `9.06` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 33,880.00 USD | 33,420.00 USD | 60,040.00 USD |
| `7D` | `9.06` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 5,610.00 USD | 14,960.00 USD | 53,070.00 USD |
| `1D` | `9.08` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 28,800.00 USD | 29,710.00 USD | 70,940.00 USD |
| `7D` | `9.08` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,110.00 USD |
| `1D` | `9.10` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 197,560.00 USD | 43,240.00 USD | 63,030.00 USD |
| `7D` | `9.10` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,370.00 USD |
| `1D` | `9.12` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 160,000.00 USD | 47,350.00 USD | 56,020.00 USD |
| `7D` | `9.12` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 490,020.00 USD | 24,170.00 USD | 479,840.00 USD |
| `1D` | `9.14` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 118,520.00 USD | 23,510.00 USD | 67,330.00 USD |
| `7D` | `9.14` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 479,710.00 USD |
| `1D` | `9.16` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 121,090.00 USD | 41,060.00 USD | 51,890.00 USD |
| `7D` | `9.16` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 195,690.00 USD |
| `1D` | `9.18` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 187,840.00 USD | 53,800.00 USD | 86,140.00 USD |
| `7D` | `9.18` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 565,140.00 USD | 162,460.00 USD | 273,290.00 USD |
| `1D` | `9.20` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 197,260.00 USD | 61,430.00 USD | 81,060.00 USD |
| `7D` | `9.20` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 548,100.00 USD | 120,080.00 USD | 237,070.00 USD |
| `1D` | `9.22` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 126,810.00 USD | 12,990.00 USD | 13,790.00 USD |
| `7D` | `9.22` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 585,170.00 USD | 144,840.00 USD | 421,710.00 USD |
| `1D` | `9.24` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 71,810.00 USD | 4,560.00 USD | 27,900.00 USD |
| `7D` | `9.24` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 316,220.00 USD | 56,410.00 USD | 170,350.00 USD |
| `1D` | `9.26` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 35,150.00 USD | 8,290.00 USD | 9,560.00 USD |
| `7D` | `9.26` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 61,890.00 USD |
| `1D` | `9.28` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 44,130.00 USD | 10,920.00 USD | 2,660.00 USD |
| `7D` | `9.28` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 428,160.00 USD | 103,490.00 USD | 170,460.00 USD |
| `1D` | `9.30` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 58,890.00 USD | 13,560.00 USD | 23,390.00 USD |
| `7D` | `9.30` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 263,160.00 USD |
| `1D` | `9.32` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 37,200.00 USD | 4,250.00 USD | 23,700.00 USD |
| `7D` | `9.32` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 271,660.00 USD | 59,310.00 USD | 337,980.00 USD |
| `1D` | `9.34` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 23,850.00 USD | 10,190.00 USD | 17,530.00 USD |
| `7D` | `9.34` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 203,440.00 USD | 53,150.00 USD | 69,980.00 USD |
| `1D` | `9.36` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 59,430.00 USD | 14,870.00 USD | 30,530.00 USD |
| `7D` | `9.36` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 247,120.00 USD | 73,430.00 USD | 85,080.00 USD |
| `1D` | `9.38` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 65,320.00 USD | 17,450.00 USD | 31,170.00 USD |
| `7D` | `9.38` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 383,530.00 USD | 55,400.00 USD | 85,190.00 USD |
| `1D` | `9.40` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 52,090.00 USD | 1,210.00 USD | 25.34 USD |
| `7D` | `9.40` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 137,440.00 USD |
| `1D` | `9.42` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 30,730.00 USD | 4,670.00 USD | 17,990.00 USD |
| `7D` | `9.42` | 18,400,000.00 USD | 18,400,000.00 USD | 0.00 USD | 176,920.00 USD | 19,780.00 USD | 85,160.00 USD |
| `1D` | `9.44` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 10,560.00 USD | 1,630.00 USD | 12,410.00 USD |
| `7D` | `9.44` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 41,250.00 USD | 19,420.00 USD | 56,640.00 USD |
| `1D` | `9.46` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 1,630.00 USD | 4,580.00 USD | 2,430.00 USD |
| `7D` | `9.46` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 60,020.00 USD | 29,830.00 USD | 19,430.00 USD |
| `1D` | `9.48` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 2,800.00 USD | 1,100.00 USD | 5,380.00 USD |
| `7D` | `9.48` | 18,700,000.00 USD | 18,700,000.00 USD | 0.00 USD | 12,180.00 USD | 27,840.00 USD | 25,650.00 USD |
| `1D` | `9.50` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 42,390.00 USD | 3,730.00 USD | 8,950.00 USD |
| `7D` | `9.50` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 89,460.00 USD | 33,210.00 USD | 83,240.00 USD |
| `1D` | `9.52` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 17,470.00 USD | 3,070.00 USD | 5,520.00 USD |
| `7D` | `9.52` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 102,150.00 USD | 29,320.00 USD | 51,140.00 USD |
| `1D` | `9.54` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 23,980.00 USD | 7,790.00 USD | 2,930.00 USD |
| `7D` | `9.54` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 192,090.00 USD | 25,090.00 USD | 771.81 USD |
| `1D` | `9.56` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 6,950.00 USD | 7,610.00 USD | 5,600.00 USD |
| `7D` | `9.56` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 88,510.00 USD | 5,260.00 USD | 14,190.00 USD |
| `1D` | `9.58` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 1,270.00 USD | 4,910.00 USD | 12,620.00 USD |
| `7D` | `9.58` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 35,340.00 USD | 14,530.00 USD | 27,430.00 USD |
| `1D` | `9.60` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 15,230.00 USD | 1,680.00 USD | 16,260.00 USD |
| `7D` | `9.60` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 38,740.00 USD | 5,460.00 USD | 26,340.00 USD |
| `1D` | `9.62` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 20,200.00 USD | 4,140.00 USD | 14,420.00 USD |
| `7D` | `9.62` | 19,650,000.00 USD | 19,650,000.00 USD | 0.00 USD | 70,470.00 USD | 1,540.00 USD | 17,160.00 USD |
| `1D` | `9.64` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 22,380.00 USD | 5,430.00 USD | 8,050.00 USD |
| `7D` | `9.64` | 19,720,000.00 USD | 19,720,000.00 USD | 0.00 USD | 35,210.00 USD | 17,650.00 USD | 20,050.00 USD |
| `1D` | `9.66` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 14,580.00 USD | 7,630.00 USD | 7,480.00 USD |
| `7D` | `9.66` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 37,340.00 USD | 21,280.00 USD | 18,910.00 USD |
| `1D` | `9.68` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 16,150.00 USD | 2,950.00 USD | 6,270.00 USD |
| `7D` | `9.68` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 68,230.00 USD | 20,310.00 USD | 32,920.00 USD |
| `1D` | `9.70` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 19,500.00 USD | 6,860.00 USD | 3,370.00 USD |
| `7D` | `9.70` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 78,860.00 USD | 12,990.00 USD | 32,510.00 USD |
| `1D` | `9.72` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 2,830.00 USD | 8,870.00 USD | 5,230.00 USD |
| `7D` | `9.72` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 70,300.00 USD | 6,920.00 USD | 26,970.00 USD |
| `1D` | `9.74` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 6,960.00 USD | 738.05 USD | 3,140.00 USD |
| `7D` | `9.74` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 21,230.00 USD | 7,200.00 USD | 19,880.00 USD |
| `1D` | `9.76` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 7,400.00 USD | 2,560.00 USD | 5,340.00 USD |
| `7D` | `9.76` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 35,520.00 USD | 12,480.00 USD | 51,500.00 USD |
| `1D` | `9.78` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 88.17 USD | 1,840.00 USD | 1,790.00 USD |
| `7D` | `9.78` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 65,390.00 USD | 10,300.00 USD | 5,530.00 USD |
| `1D` | `9.80` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 12,580.00 USD | 770.83 USD | 9.39 USD |
| `7D` | `9.80` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 18,630.00 USD | 28,440.00 USD | 10,480.00 USD |
| `1D` | `9.82` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 14,340.00 USD | 1,540.00 USD | 6,190.00 USD |
| `7D` | `9.82` | 20,670,000.00 USD | 20,670,000.00 USD | 0.00 USD | 121,860.00 USD | 27,860.00 USD | 86,430.00 USD |
| `7D` | `9.84` | 20,700,000.00 USD | 20,700,000.00 USD | 0.00 USD | 9,730.00 USD | 7,850.00 USD | 14,040.00 USD |
| `7D` | `9.86` | 20,830,000.00 USD | 20,830,000.00 USD | 0.00 USD | 58,870.00 USD | 2,210.00 USD | 71,760.00 USD |
| `7D` | `9.88` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 7,170.00 USD | 8,710.00 USD | 21,480.00 USD |
| `7D` | `9.90` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 55,970.00 USD | 19,700.00 USD | 14,200.00 USD |
| `7D` | `9.92` | 21,010,000.00 USD | 21,010,000.00 USD | 0.00 USD | 27,710.00 USD | 10,810.00 USD | 9,270.00 USD |
| `7D` | `9.94` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 69,320.00 USD | 11,150.00 USD | 39,790.00 USD |
| `7D` | `9.96` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 29,800.00 USD | 1,360.00 USD | 10,860.00 USD |
| `7D` | `9.98` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 840.10 USD | 4,150.00 USD | 18,960.00 USD |
| `7D` | `10.00` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD |
| `7D` | `10.02` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 16,100.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `10.04` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 505.60 USD | 0.00 USD | 9,730.00 USD |
| `7D` | `10.06` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | 17,230.00 USD |
| `7D` | `10.08` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 23,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `353.49M` | Total OI Tokens: `42,269,912.0 AVAX`
  * 1h OI Change: `-7.53%` | 4h OI Change: `-8.20%` | 24h OI Change: `-10.96%`
  * Exchange Breakdown: Binance=`83.15M` | Bybit=`55.81M` | OKX=`11.80M` | Hyperliquid=`16.29M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.10K` | Last 24h: `33.77K` | Last 3d: `72.05K` | Last 7d: `92.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0060%` | **USDT OKX** | `0.0091%` |
| **USDT Bybit** | `0.0011%` | **USDT KuCoin** | `0.0063%` |
| **USDT MEXC** | `0.0061%` | **USDT BingX** | `0.0092%` |
| **USDT Gate** | `-0.0007%` | **USDT Bitget** | `0.0067%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `45.15%` | `54.85%` | `0.82` | 70,030,000.00 USD |
| `15M` | `Binance` | `44.25%` | `55.75%` | `0.79` | 25,740,000.00 USD |
| `15M` | `OKX` | `50.04%` | `49.96%` | `1.00` | 10,100,000.00 USD |
| `15M` | `Bybit` | `46.39%` | `53.61%` | `0.87` | 8,040,000.00 USD |
| `15M` | `KuCoin` | `59.41%` | `40.59%` | `1.46` | 543,280.00 USD |
| `15M` | `Gate` | `45.19%` | `54.81%` | `0.82` | 770,700.00 USD |
| `15M` | `Bitget` | `45.78%` | `54.22%` | `0.84` | 3,840,000.00 USD |
| `15M` | `BingX` | `36.35%` | `63.65%` | `0.57` | 1,860,000.00 USD |
| `15M` | `MEXC` | `48.97%` | `51.03%` | `0.96` | 9,680,000.00 USD |
| `15M` | `Bitunix` | `40.91%` | `59.09%` | `0.69` | 3,550,000.00 USD |
| `15M` | `Hyperliquid` | `36.33%` | `63.67%` | `0.57` | 2,840,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.97%` | `52.03%` | `0.92` | 1,240,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `14.46%` | `85.54%` | `0.17` | 1,110,000.00 USD |
| `15M` | `HTX` | `46.64%` | `53.36%` | `0.87` | 83,110.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `58.58%` | `41.42%` | `1.41` | 363,020.00 USD |
| `15M` | `Aster` | `43.55%` | `56.45%` | `0.77` | 104,570.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.71%` | `61.29%` | `0.63` | 177,660.00 USD |
| `15M` | `Whale Positions` | `44.25%` | `55.75%` | `0.79` | 25,740,000.00 USD |
| `15M` | `Global Accounts` | `45.15%` | `54.85%` | `0.82` | 70,030,000.00 USD |
| `1H` | `AVAX` | `44.72%` | `55.28%` | `0.81` | 128,050,000.00 USD |
| `1H` | `Binance` | `44.46%` | `55.54%` | `0.80` | 45,120,000.00 USD |
| `1H` | `OKX` | `46.37%` | `53.63%` | `0.86` | 16,610,000.00 USD |
| `1H` | `Bybit` | `44.97%` | `55.03%` | `0.82` | 14,410,000.00 USD |
| `1H` | `KuCoin` | `51.31%` | `48.69%` | `1.05` | 980,740.00 USD |
| `1H` | `Gate` | `41.75%` | `58.25%` | `0.72` | 1,620,000.00 USD |
| `1H` | `Bitget` | `45.74%` | `54.26%` | `0.84` | 6,620,000.00 USD |
| `1H` | `BingX` | `42.83%` | `57.17%` | `0.75` | 3,180,000.00 USD |
| `1H` | `MEXC` | `49.03%` | `50.97%` | `0.96` | 22,640,000.00 USD |
| `1H` | `Bitunix` | `44.12%` | `55.88%` | `0.79` | 5,960,000.00 USD |
| `1H` | `Hyperliquid` | `31.48%` | `68.52%` | `0.46` | 4,310,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.1%` | `50.9%` | `0.96` | 3,050,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `15.3%` | `84.7%` | `0.18` | 1,810,000.00 USD |
| `1H` | `HTX` | `40.79%` | `59.21%` | `0.69` | 116,160.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.22%` | `54.78%` | `0.83` | 820,920.00 USD |
| `1H` | `Aster` | `15.1%` | `84.9%` | `0.18` | 564,630.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.8%` | `62.2%` | `0.61` | 253,560.00 USD |
| `1H` | `Whale Positions` | `44.46%` | `55.54%` | `0.80` | 45,120,000.00 USD |
| `1H` | `Global Accounts` | `44.72%` | `55.28%` | `0.81` | 128,050,000.00 USD |
| `4H` | `AVAX` | `45.47%` | `54.53%` | `0.83` | 193,100,000.00 USD |
| `4H` | `Binance` | `45.75%` | `54.25%` | `0.84` | 61,930,000.00 USD |
| `4H` | `OKX` | `46.6%` | `53.4%` | `0.87` | 22,300,000.00 USD |
| `4H` | `Bybit` | `45.16%` | `54.84%` | `0.82` | 19,070,000.00 USD |
| `4H` | `KuCoin` | `49.84%` | `50.16%` | `0.99` | 1,420,000.00 USD |
| `4H` | `Gate` | `43.49%` | `56.51%` | `0.77` | 2,280,000.00 USD |
| `4H` | `Bitget` | `45.85%` | `54.15%` | `0.85` | 8,380,000.00 USD |
| `4H` | `BingX` | `42.89%` | `57.11%` | `0.75` | 5,820,000.00 USD |
| `4H` | `MEXC` | `49.36%` | `50.64%` | `0.97` | 47,760,000.00 USD |
| `4H` | `Bitunix` | `45.35%` | `54.65%` | `0.83` | 7,740,000.00 USD |
| `4H` | `Hyperliquid` | `31.04%` | `68.96%` | `0.45` | 5,770,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 4,570,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `10.65%` | `89.35%` | `0.12` | 3,750,000.00 USD |
| `4H` | `HTX` | `48.5%` | `51.5%` | `0.94` | 150,270.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.25%` | `54.75%` | `0.83` | 1,210,000.00 USD |
| `4H` | `Aster` | `16.34%` | `83.66%` | `0.20` | 591,250.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.63%` | `58.37%` | `0.71` | 348,850.00 USD |
| `4H` | `Whale Positions` | `45.75%` | `54.25%` | `0.84` | 61,930,000.00 USD |
| `4H` | `Global Accounts` | `45.47%` | `54.53%` | `0.83` | 193,100,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.84` | `8.83` | `8.84` | `8.86` | `8.79` | 750,878.19 USD | 458,225.53 USD | 292,652.66 USD | 165,572.87 USD | `+22.05%` | `19B / 3S` |
| `0:00 UTC` | `8.82` | `8.82` | `8.82` | `8.84` | `8.80` | 637,816.13 USD | 328,825.06 USD | 308,991.07 USD | 19,833.99 USD | `+3.11%` | `4B / 4S` |
| `5:00 UTC` | `8.81` | `8.82` | `8.81` | `8.84` | `8.80` | 548,929.60 USD | 300,754.28 USD | 248,175.32 USD | 52,578.96 USD | `+9.58%` | `18B / 4S` |
| `0:00 UTC` | `8.86` | `8.86` | `8.86` | `8.87` | `8.83` | 587,148.06 USD | 393,702.30 USD | 193,445.76 USD | 200,256.54 USD | `+34.11%` | `5B / 1S` |
| `5:00 UTC` | `8.85` | `8.85` | `8.85` | `8.87` | `8.84` | 431,773.06 USD | 190,520.19 USD | 241,252.88 USD | -50,732.69 USD | `-11.75%` | `8B / 6S` |
| `0:00 UTC` | `8.73` | `8.73` | `8.73` | `8.86` | `8.66` | 5,568,654.06 USD | 2,589,240.15 USD | 2,979,413.92 USD | -390,173.77 USD | `-7.01%` | `5B / 25S` |
| `5:00 UTC` | `8.77` | `8.75` | `8.77` | `8.78` | `8.73` | 2,097,434.25 USD | 1,386,379.16 USD | 711,055.10 USD | 675,324.06 USD | `+32.20%` | `14B / 3S` |
| `0:00 UTC` | `8.61` | `8.53` | `8.61` | `8.76` | `8.39` | 13,163,243.09 USD | 4,547,421.99 USD | 8,615,821.10 USD | -4,068,399.10 USD | `-30.91%` | `4B / 57S` |
| `5:00 UTC` | `8.26` | `8.35` | `8.26` | `8.48` | `8.25` | 17,210,058.04 USD | 7,276,281.50 USD | 9,933,776.55 USD | -2,657,495.05 USD | `-15.44%` | `5B / 17S` |
| `0:00 UTC` | `8.38` | `8.36` | `8.38` | `8.40` | `8.31` | 1,240,765.64 USD | 653,714.39 USD | 587,051.25 USD | 66,663.14 USD | `+5.37%` | `15B / 6S` |

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
| `5m` | -102,620.00 USD | -38,780.00 USD | **`DISTRIBUTION`** |
| `15m` | -331,040.00 USD | -2,040,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,560,000.00 USD | -8,290,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,710,000.00 USD | -7,930,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,010,000.00 USD | -7,790,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,090,000.00 USD | -10,210,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,910,000.00 USD | -11,180,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,820,000.00 USD | -10,060,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,140,000.00 USD | -11,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,790,000.00 USD | -14,150,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,760,000.00 USD | -50,960,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -55,550,000.00 USD | -278,350,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-102.62K` | 15m=`-331.04K` | 1h=`-1.71M` | 24h=`-1.79M`
* Futures Capital Netflows: 5m=`-38.78K` | 15m=`-2.04M` | 1h=`-7.93M` | 24h=`-14.15M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.29` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.14` (Risk Distance: `0.1530` pts)
  * +2.5R Take Profit: `8.67`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.47` (Risk Distance: `0.1530` pts)
  * +2.5R Take Profit: `7.94`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
