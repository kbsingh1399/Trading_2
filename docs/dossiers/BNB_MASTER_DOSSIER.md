# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:07:12 IST` (`2026-10-29 17:37:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `746.10` | **Live Ask Quote**: `746.70` | **Mid Price**: `746.40`
- **Spread Points**: `60.00` | **Spread BPS**: `8.04 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `746.40` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.87` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `751.62` | Lower -3.00σ Band: `741.18`
  * Upper +2.51σ Band: `750.51` | Lower -2.51σ Band: `742.29`
  * Upper +2.01σ Band: `749.53` | Lower -2.01σ Band: `743.27`
  * Upper +2.00σ Band: `749.39` | Lower -2.00σ Band: `743.41`
  * Upper +1.28σ Band: `748.49` | Lower -1.28σ Band: `744.31`
  * Upper +1.00σ Band: `747.89` | Lower -1.00σ Band: `744.91`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`746.40` | EMA-20=`746.40` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`746.40` (Slope: `+0.0000`) | EMA-100=`746.40`
  * Institutional Anchors: EMA-144=`746.40` | EMA-200=`746.40` (Slope: `+0.0000`) | EMA-233=`746.40`
- **Range Boundaries**: 24H High=`753.86` | 24H Low=`738.94` | Weekly High=`761.33` | Weekly Low=`731.47`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `752.43` (Distance: `-0.80%`)
  * Point of Control (POC) = `750.76` (Distance: `-0.58%`)
  * Value Area Low (VAL) = `740.27` (Distance: `+0.83%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`752.98` | POC=`743.64` | VAL=`742.97`
  * Prior Day Extremes: PDH=`760.90` | PDL=`740.60` | PDC=`754.40`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`749.00` | Weekly POC=`741.00` | Weekly VAL=`734.80`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`759.80` | Low=`743.20`
  * London Session (08:00-16:00 UTC): High=`758.10` | Low=`737.00`
  * New York Session (13:00-21:00 UTC): High=`753.20` | Low=`737.00`
  * Initial Balance (First Hour): IB High=`758.10` | IB Low=`753.70`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `743.41` - `749.39`
  * Optimal Trade Entry (OTE 0.705): `747.89`
  * Structural Invalidation Anchor (0.786): `752.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `748.66` | `749.31` | `748.39` | `748.39` | `784` | 586,659.58 USD | -103,721.06 USD | `-17.68%` | -14,586,659.98 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `748.39` | `748.93` | `748.24` | `748.42` | `1,303` | 975,391.84 USD | 104,477.72 USD | `+10.71%` | -14,482,182.26 USD | `+0.14` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `748.43` | `748.99` | `747.78` | `748.50` | `2,183` | 1,633,275.14 USD | -591,011.52 USD | `-36.19%` | -15,073,193.78 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `750.24` | `751.04` | `749.70` | `750.30` | `5,557` | 4,170,354.29 USD | 82,832.29 USD | `+1.99%` | -13,440,590.49 USD | `-0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `750.30` | `750.31` | `748.23` | `748.39` | `5,052` | 3,784,737.73 USD | -1,484,896.49 USD | `-39.23%` | -14,925,486.98 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `748.39` | `748.99` | `747.78` | `748.41` | `3,477` | 2,602,200.59 USD | -491,727.89 USD | `-18.90%` | -15,417,214.87 USD | `-0.51` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `748.81` | `753.64` | `748.57` | `750.62` | `37,622` | 28,276,923.64 USD | -2,667,814.74 USD | `-9.43%` | -15,488,624.01 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `750.62` | `754.90` | `747.57` | `750.30` | `44,285` | 33,270,591.61 USD | 1,238,846.42 USD | `+3.72%` | -14,249,777.59 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `750.30` | `750.31` | `747.78` | `748.50` | `8,538` | 6,393,404.71 USD | -1,971,430.29 USD | `-30.84%` | -16,221,207.88 USD | `-0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -24,139,305.42 USD | `-1.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -16,093,806.98 USD | `+1.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `747.57` | `748.41` | `52,814` | 39,657,529.92 USD | -737,777.96 USD | `-1.86%` | -16,831,584.94 USD | `+0.33` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `760.15` | `761.27` | `744.75` | `747.26` | `127,643` | 95,856,420.87 USD | -6,475,652.55 USD | `-6.76%` | -5,558,854.93 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -13,799,012.93 USD | `-0.92` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -24,139,305.42 USD | `-1.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -16,093,806.98 USD | `+1.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `747.57` | `748.41` | `52,814` | 39,657,529.92 USD | -737,777.96 USD | `-1.86%` | -16,831,584.94 USD | `+0.33` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`746.40`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `746.88` | `37460000000.0000` | 27,978.12 USD | 76,453.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `746.92` | `1197000000.0000` | 894.06 USD | 48,475.00 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `746.94` | `32587000000.0000` | 24,340.53 USD | 47,580.94 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `746.95` | `1431000000.0000` | 1,068.89 USD | 23,240.40 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `746.97` | `7222000000.0000` | 5,394.62 USD | 22,171.52 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `747.01` | `220000000.0000` | 164.34 USD | 16,776.90 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `747.02` | `897000000.0000` | 670.08 USD | 16,612.56 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `747.03` | `833000000.0000` | 622.28 USD | 15,942.48 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `747.04` | `6450000000.0000` | 4,818.41 USD | 15,320.20 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `747.06` | `1197000000.0000` | 894.23 USD | 10,501.80 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `747.08` | `654000000.0000` | 488.59 USD | 9,607.57 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `747.09` | `3679000000.0000` | 2,748.54 USD | 9,118.98 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `747.12` | `1197000000.0000` | 894.30 USD | 6,370.43 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `747.14` | `2676000000.0000` | 1,999.35 USD | 5,476.13 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `747.16` | `14000000.0000` | 10.46 USD | 3,476.78 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `747.17` | `897000000.0000` | 670.21 USD | 3,466.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `747.18` | `117000000.0000` | 87.42 USD | 2,796.11 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `747.20` | `1075000000.0000` | 803.24 USD | 2,708.69 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `747.23` | `1197000000.0000` | 894.43 USD | 1,905.45 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `747.24` | `1353000000.0000` | 1,011.02 USD | 1,011.02 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `747.27` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 747.27` | `0.00%` | `-` |
| `ASK` | `747.30` | `8599000000.0000` | 6,426.03 USD | 6,426.03 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `747.33` | `8170000000.0000` | 6,105.69 USD | 12,531.72 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `747.34` | `1026000000.0000` | 766.77 USD | 13,298.49 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `747.36` | `8357000000.0000` | 6,245.69 USD | 19,544.18 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `747.41` | `10453000000.0000` | 7,812.68 USD | 27,356.85 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `747.42` | `10904000000.0000` | 8,149.87 USD | 35,506.72 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `747.45` | `12265000000.0000` | 9,167.47 USD | 44,674.20 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `747.46` | `17963000000.0000` | 13,426.62 USD | 58,100.82 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `747.47` | `6616000000.0000` | 4,945.26 USD | 63,046.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `747.48` | `700000000.0000` | 523.24 USD | 63,569.32 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `747.49` | `1177000000.0000` | 879.80 USD | 64,449.11 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `747.50` | `51093000000.0000` | 38,192.02 USD | 102,641.13 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `747.51` | `1000000000.0000` | 747.51 USD | 103,388.64 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `747.53` | `2819000000.0000` | 2,107.29 USD | 105,495.93 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `747.55` | `1197000000.0000` | 894.82 USD | 106,390.74 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `747.57` | `529000000.0000` | 395.46 USD | 106,786.21 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `747.58` | `1793000000.0000` | 1,340.41 USD | 108,126.62 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `747.59` | `1192000000.0000` | 891.13 USD | 109,017.75 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `747.60` | `3400000000.0000` | 2,541.84 USD | 111,559.59 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `747.61` | `1197000000.0000` | 894.89 USD | 112,454.48 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `777` | `0xea00...a918` | `LONG` | 3,065,706.86 USD | `4,098,429,000,000.00` | `787.24` | `748.15` | `0.000000` | -160,719.92 USD | `-5.24%` | `5X Cross` |
| `1084` | `0xb69e...033a` | `LONG` | 2,098,979.71 USD | `2,805,710,000,000.00` | `772.94` | `748.15` | `541.86` | -69,662.88 USD | `-3.32%` | `10X Cross` |
| `1091` | `0xcac1...26b3` | `LONG` | 2,086,734.08 USD | `2,789,043,000,000.00` | `679.91` | `748.15` | `0.000000` | 190,422.92 USD | `+9.13%` | `10X Cross` |
| `1165` | `0x7737...bf66` | `SHORT` | 1,979,632.97 USD | `2,646,179,000,000.00` | `752.73` | `748.15` | `7301.16` | 12,237.61 USD | `+0.62%` | `10X Cross` |
| `1573` | `0xecb6...2b00` | `SHORT` | 1,443,463.51 USD | `1,929,274,000,000.00` | `738.35` | `748.15` | `15931.92` | -18,980.30 USD | `-1.31%` | `5X Cross` |
| `1663` | `0x27c9...d65d` | `SHORT` | 1,336,371.43 USD | `1,786,163,000,000.00` | `762.40` | `748.15` | `1504.45` | 25,395.92 USD | `+1.90%` | `10X Cross` |
| `1758` | `0x07fd...689d` | `LONG` | 1,245,633.10 USD | `1,664,862,000,000.00` | `716.02` | `748.15` | `0.000000` | 53,556.76 USD | `+4.30%` | `10X Cross` |
| `1780` | `0x645b...87b8` | `LONG` | 1,221,145.05 USD | `1,632,357,000,000.00` | `750.75` | `748.15` | `0.000000` | -4,341.11 USD | `-0.36%` | `10X Cross` |
| `2033` | `0xbcd4...0dd2` | `LONG` | 1,013,257.26 USD | `1,354,278,000,000.00` | `746.04` | `748.15` | `0.000000` | 2,913.19 USD | `+0.29%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `745.30` | 53,346.34 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 53.35K USD at 745.3000 USD [API] | `2026-10-27 22:32:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.31` (Vol: 2,400,000.00 USD, Dist: `+1.34%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--1.59%`)
  * 48H Horizon: Short MP=`758.54` (Vol: 2,400,000.00 USD, Dist: `+1.37%`) | Long MP=`737.64` (Vol: 2,200,000.00 USD, Dist: `--1.43%`)
  * 3D Horizon: Short MP=`766.52` (Vol: 2,500,000.00 USD, Dist: `+2.43%`) | Long MP=`736.48` (Vol: 3,000,000.00 USD, Dist: `--1.58%`)
  * 7D Horizon: Short MP=`758.15` (Vol: 2,900,000.00 USD, Dist: `+1.31%`) | Long MP=`728.45` (Vol: 3,700,000.00 USD, Dist: `--2.66%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `156.50` | 159.16 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `218.50` | 134.60 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 460.51 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 712.80 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `237.50` | 1,190.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `257.50` | 9,110.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `274.50` | 21,760.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `289.50` | 916.85 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `293.50` | 286.75 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `296.50` | 5,950.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `297.50` | 20,500.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `300.50` | 1,280.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `310.50` | 1,640.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `311.50` | 109.96 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 2,110.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `319.50` | 366.79 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `320.50` | 886.82 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 315.03 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `330.50` | 1,080.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 1,790.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 377.19 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `335.50` | 313.02 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `338.50` | 23,420.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `348.50` | 2,940.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `354.50` | 749.77 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `355.50` | 42,640.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 2,870.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 240.43 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `375.50` | 13,690.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 438.65 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 953.44 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 645.15 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 321.22 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 16,020.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 435.21 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 168.06 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 396.50 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 605.16 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `405.50` | 28,390.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `407.50` | 3,450.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `408.50` | 551.07 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 106.17 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 13,320.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 974.19 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 465.79 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 2,660.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `427.50` | 12,150.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 638.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `440.50` | 968.22 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `445.50` | 2,330.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `454.50` | 4,220.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `457.50` | 463.45 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `466.50` | 8,860.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 4,380.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `471.50` | 471.50 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `474.50` | 5,500.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `476.50` | 5,330.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `483.50` | 2,020.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 976.51 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `496.50` | 248.25 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 2,120.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,610.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 1,570.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 158.56 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 5,190.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,010.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 3,780.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 12,890.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 1,160.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 6,390.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 3,560.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 1,040.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 440.99 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,090.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 1,460.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 1,210.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 5,730.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `528.50` | 160.14 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 43,440.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 16,980.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 1,490,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 1,880.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 267.75 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 100.33 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `537.50` | 4,300.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 334.25 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,310.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 491.85 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 531.07 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,770.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 959.69 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,420.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 2,010.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 591.61 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 5,680.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `558.50` | 385.36 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `559.50` | 212.61 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 10,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 15,170.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `564.50` | 14,210.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `567.50` | 377.39 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 715,280.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 862.44 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 222.91 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 275.37 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 2,320.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 4,060.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 275.41 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 6,810.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,540.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 1,530.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 1,660.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 100.39 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 1,240.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 44,800.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 100.98 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,560.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 116.90 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 1,270.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 303.76 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 1,880.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 185.28 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 735.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 527.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 2,550.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 427.16 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 770.62 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 1,250.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 2,110.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `623.50` | 1,050.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 11,970.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 16,020.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 664.32 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `629.50` | 3,680.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `631.50` | 6,320.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `632.50` | 125.87 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `633.50` | 4,100.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 5,910.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `636.50` | 5,140.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 10,020.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `639.50` | 34,090.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 3,910.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 1,670.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 485.09 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `643.50` | 8,490.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.50` | 3,820.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `646.50` | 155.81 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `649.50` | 559.87 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `651.50` | 633.26 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `654.50` | 97,640.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `656.50` | 122.77 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `657.50` | 2,180.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `658.50` | 4,800.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,340.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `661.50` | 463.71 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `662.50` | 19,830.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `663.50` | 2,070.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 88,890,000.00 USD | 88,890,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 88,750,000.00 USD | 88,750,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 88,600,000.00 USD | 88,600,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 5,440.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 88,200,000.00 USD | 88,200,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.70` | 87,910,000.00 USD | 87,910,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.60` | 87,610,000.00 USD | 87,610,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 87,080,000.00 USD | 87,080,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 3,040.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `670.40` | 86,590,000.00 USD | 86,590,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 3,460.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `671.30` | 86,100,000.00 USD | 86,100,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 3,360.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `672.20` | 85,670,000.00 USD | 85,670,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 12,130.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.90` | 33,500,000.00 USD | 33,500,000.00 USD | 213,810.00 USD | 35,830.00 USD | 43,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 85,350,000.00 USD | 85,350,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 567.76 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.70` | 33,210,000.00 USD | 33,210,000.00 USD | 277,700.00 USD | 28,940.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 84,850,000.00 USD | 84,850,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.50` | 32,890,000.00 USD | 32,890,000.00 USD | 153,120.00 USD | 41,110.00 USD | 43,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 259.68 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 84,330,000.00 USD | 84,330,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.30` | 32,650,000.00 USD | 32,650,000.00 USD | 60,970.00 USD | 25,690.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.80` | 84,000,000.00 USD | 84,000,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.10` | 32,550,000.00 USD | 32,550,000.00 USD | 133,460.00 USD | 40,110.00 USD | 51,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.70` | 83,510,000.00 USD | 83,510,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.90` | 32,320,000.00 USD | 32,320,000.00 USD | 351,470.00 USD | 12,910.00 USD | 53,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 82,840,000.00 USD | 82,840,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.70` | 31,900,000.00 USD | 31,900,000.00 USD | 259,280.00 USD | 18,700.00 USD | 50,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.50` | 31,580,000.00 USD | 31,580,000.00 USD | 73,950.00 USD | 11,640.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 82,370,000.00 USD | 82,370,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 2,490.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.30` | 31,480,000.00 USD | 31,480,000.00 USD | 108,790.00 USD | 7,970.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 82,220,000.00 USD | 82,220,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.10` | 31,350,000.00 USD | 31,350,000.00 USD | 52,780.00 USD | 11,030.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 82,050,000.00 USD | 82,050,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.90` | 31,270,000.00 USD | 31,270,000.00 USD | 65,540.00 USD | 5,770.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 81,870,000.00 USD | 81,870,000.00 USD | 110,330.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 31,450.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.70` | 31,190,000.00 USD | 31,190,000.00 USD | 75,570.00 USD | 11,810.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 81,720,000.00 USD | 81,720,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.50` | 31,100,000.00 USD | 31,100,000.00 USD | 30,930.00 USD | 12,580.00 USD | 39,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 81,670,000.00 USD | 81,670,000.00 USD | 181,220.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.30` | 31,010,000.00 USD | 31,010,000.00 USD | 107,550.00 USD | 9,680.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 81,450,000.00 USD | 81,450,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.10` | 30,890,000.00 USD | 30,890,000.00 USD | 18,530.00 USD | 12,720.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `684.50` | 42,430.00 USD | 970,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `684.80` | 81,320,000.00 USD | 81,320,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.90` | 30,860,000.00 USD | 30,860,000.00 USD | 31,040.00 USD | 2,630.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `685.50` | 1,290.00 USD | 928,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `685.70` | 30,820,000.00 USD | 30,820,000.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 81,030,000.00 USD | 81,030,000.00 USD | 199,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `686.50` | 194.28 USD | 927,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `686.60` | 80,830,000.00 USD | 80,830,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 80,760,000.00 USD | 80,760,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `687.50` | 374.69 USD | 927,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `688.40` | 80,620,000.00 USD | 80,620,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.90` | 30,800,000.00 USD | 30,800,000.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 80,550,000.00 USD | 80,550,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `689.50` | 885.32 USD | 926,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `689.70` | 30,790,000.00 USD | 30,790,000.00 USD | 23,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 80,460,000.00 USD | 80,460,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.50` | 30,770,000.00 USD | 30,770,000.00 USD | 74,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `690.50` | 6,170.00 USD | 925,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `691.10` | 80,030,000.00 USD | 80,030,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.30` | 30,700,000.00 USD | 30,700,000.00 USD | 33,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `691.50` | 5,430.00 USD | 919,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `692.00` | 79,530,000.00 USD | 79,530,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.10` | 30,660,000.00 USD | 30,660,000.00 USD | 69,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `692.50` | 5,580.00 USD | 914,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `692.90` | 30,590,000.00 USD | 30,590,000.00 USD | 52,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 79,130,000.00 USD | 79,130,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `693.50` | 2,590.00 USD | 908,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `693.70` | 30,540,000.00 USD | 30,540,000.00 USD | 27,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 78,830,000.00 USD | 78,830,000.00 USD | 311,120.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.50` | 30,510,000.00 USD | 30,510,000.00 USD | 17,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `694.50` | 685.47 USD | 906,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `694.70` | 78,480,000.00 USD | 78,480,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.30` | 30,500,000.00 USD | 30,500,000.00 USD | 9,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `695.50` | 299.07 USD | 905,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `695.60` | 78,130,000.00 USD | 78,130,000.00 USD | 127,500.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.10` | 30,490,000.00 USD | 30,490,000.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 77,980,000.00 USD | 77,980,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `696.50` | 1,420.00 USD | 905,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `696.90` | 30,460,000.00 USD | 30,460,000.00 USD | 37,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 77,840,000.00 USD | 77,840,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `697.50` | 742.14 USD | 903,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `697.70` | 30,420,000.00 USD | 30,420,000.00 USD | 62,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 77,630,000.00 USD | 77,630,000.00 USD | 277,440.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.50` | 30,360,000.00 USD | 30,360,000.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `698.50` | 137.60 USD | 902,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `699.20` | 77,260,000.00 USD | 77,260,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.30` | 30,330,000.00 USD | 30,330,000.00 USD | 30,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `699.50` | 20,100.00 USD | 902,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `700.10` | 30,300,000.00 USD | 30,300,000.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 76,960,000.00 USD | 76,960,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `700.50` | 1,130.00 USD | 882,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `700.90` | 30,290,000.00 USD | 30,290,000.00 USD | 25,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 76,670,000.00 USD | 76,670,000.00 USD | 237,800.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.70` | 30,260,000.00 USD | 30,260,000.00 USD | 47,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 76,420,000.00 USD | 76,420,000.00 USD | 256,690.00 USD | 71,500.00 USD | 112,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.50` | 30,220,000.00 USD | 30,220,000.00 USD | 72,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `702.50` | 2,080.00 USD | 881,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `702.80` | 75,970,000.00 USD | 75,970,000.00 USD | 416,820.00 USD | 74,570.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.30` | 30,140,000.00 USD | 30,140,000.00 USD | 75,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `703.50` | 3,820.00 USD | 879,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `703.70` | 75,450,000.00 USD | 75,450,000.00 USD | 354,550.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.10` | 30,070,000.00 USD | 30,070,000.00 USD | 71,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `704.50` | 3,190.00 USD | 875,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `704.60` | 75,050,000.00 USD | 75,050,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.90` | 30,000,000.00 USD | 30,000,000.00 USD | 83,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 74,180,000.00 USD | 74,180,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `705.50` | 829.67 USD | 872,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `705.70` | 29,910,000.00 USD | 29,910,000.00 USD | 86,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 72,860,000.00 USD | 72,860,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `706.50` | 29,830,000.00 USD | 29,830,000.00 USD | 40,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `706.50` | 23,730.00 USD | 871,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `707.30` | 29,790,000.00 USD | 29,790,000.00 USD | 37,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 72,000,000.00 USD | 72,000,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `707.50` | 22,730.00 USD | 847,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `708.10` | 29,750,000.00 USD | 29,750,000.00 USD | 16,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 71,250,000.00 USD | 71,250,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `708.50` | 171,950.00 USD | 825,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `708.90` | 29,730,000.00 USD | 29,730,000.00 USD | 39,580.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 70,270,000.00 USD | 70,270,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `709.50` | 341,220.00 USD | 653,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `709.70` | 29,690,000.00 USD | 29,690,000.00 USD | 90,370.00 USD | 25,300.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 69,530,000.00 USD | 69,530,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `710.50` | 29,560,000.00 USD | 29,560,000.00 USD | 43,470.00 USD | 43,310.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `710.50` | 43,190.00 USD | 311,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.90` | 68,740,000.00 USD | 68,740,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.30` | 29,450,000.00 USD | 29,450,000.00 USD | 102,220.00 USD | 57,170.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `711.50` | 11,390.00 USD | 268,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `711.80` | 67,420,000.00 USD | 67,420,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.10` | 29,280,000.00 USD | 29,280,000.00 USD | 237,490.00 USD | 12,480.00 USD | 47,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `712.50` | 229,760.00 USD | 257,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `712.70` | 66,460,000.00 USD | 66,460,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.90` | 28,990,000.00 USD | 28,990,000.00 USD | 109,400.00 USD | 73,320.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `713.50` | 21,880.00 USD | 27,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `713.60` | 64,820,000.00 USD | 64,820,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `713.70` | 28,790,000.00 USD | 28,790,000.00 USD | 254,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `714.50` | 28,530,000.00 USD | 28,530,000.00 USD | 445,640.00 USD | 6,880.00 USD | 20,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 61,970,000.00 USD | 61,970,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `714.50` | 157.90 USD | 5,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `715.30` | 28,060,000.00 USD | 28,060,000.00 USD | 21,790.00 USD | 16,080.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 60,960,000.00 USD | 60,960,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `716.10` | 28,020,000.00 USD | 28,020,000.00 USD | 58,460.00 USD | 9,800.00 USD | 43,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 59,160,000.00 USD | 59,160,000.00 USD | 1,320,000.00 USD | 385,020.00 USD | 311,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `716.50` | 789.58 USD | 5,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `716.90` | 27,900,000.00 USD | 27,900,000.00 USD | 146,980.00 USD | 30,120.00 USD | 67,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 57,140,000.00 USD | 57,140,000.00 USD | 581,610.00 USD | 408,260.00 USD | 371,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `717.50` | 3,700.00 USD | 4,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `717.70` | 27,660,000.00 USD | 27,660,000.00 USD | 515,310.00 USD | 97,840.00 USD | 51,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 55,780,000.00 USD | 55,780,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `718.50` | 26,990,000.00 USD | 26,990,000.00 USD | 753,870.00 USD | 77,200.00 USD | 122,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `718.50` | 104.18 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `719.00` | 53,690,000.00 USD | 53,690,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `719.30` | 26,040,000.00 USD | 26,040,000.00 USD | 715,270.00 USD | 109,850.00 USD | 161,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 52,670,000.00 USD | 52,670,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `720.10` | 25,050,000.00 USD | 25,050,000.00 USD | 360,270.00 USD | 107,240.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 51,690,000.00 USD | 51,690,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `720.90` | 24,520,000.00 USD | 24,520,000.00 USD | 380,790.00 USD | 60,930.00 USD | 140,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `721.50` | 998.56 USD | 998.56 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `721.70` | 23,940,000.00 USD | 23,940,000.00 USD | 876,410.00 USD | 103,330.00 USD | 167,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `721.70` | 50,450,000.00 USD | 50,450,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `722.50` | 22,790,000.00 USD | 22,790,000.00 USD | 918,750.00 USD | 80,750.00 USD | 160,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `722.60` | 47,610,000.00 USD | 47,610,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `723.30` | 21,630,000.00 USD | 21,630,000.00 USD | 659,110.00 USD | 17,430.00 USD | 73,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 45,340,000.00 USD | 45,340,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `724.10` | 20,880,000.00 USD | 20,880,000.00 USD | 126,140.00 USD | 75,600.00 USD | 82,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 44,270,000.00 USD | 44,270,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `724.90` | 20,600,000.00 USD | 20,600,000.00 USD | 342,160.00 USD | 62,890.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 43,290,000.00 USD | 43,290,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `725.70` | 20,180,000.00 USD | 20,180,000.00 USD | 263,490.00 USD | 202,520.00 USD | 100,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 40,710,000.00 USD | 40,710,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `726.50` | 19,610,000.00 USD | 19,610,000.00 USD | 504,710.00 USD | 56,970.00 USD | 60,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 38,870,000.00 USD | 38,870,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `727.30` | 18,990,000.00 USD | 18,990,000.00 USD | 337,570.00 USD | 51,580.00 USD | 124,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 37,070,000.00 USD | 37,070,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `728.10` | 18,480,000.00 USD | 18,480,000.00 USD | 395,990.00 USD | 195,850.00 USD | 106,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `728.90` | 17,780,000.00 USD | 17,780,000.00 USD | 678,830.00 USD | 40,280.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 32,790,000.00 USD | 32,790,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `729.70` | 17,000,000.00 USD | 17,000,000.00 USD | 901,620.00 USD | 40,430.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `729.80` | 29,500,000.00 USD | 29,500,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `730.50` | 16,050,000.00 USD | 16,050,000.00 USD | 156,880.00 USD | 70,850.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `730.70` | 27,410,000.00 USD | 27,410,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `731.30` | 15,780,000.00 USD | 15,780,000.00 USD | 106,720.00 USD | 39,480.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `731.60` | 23,710,000.00 USD | 23,710,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `732.10` | 15,570,000.00 USD | 15,570,000.00 USD | 307,460.00 USD | 43,990.00 USD | 148,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 21,790,000.00 USD | 21,790,000.00 USD | 465,880.00 USD | 221,510.00 USD | 64,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `732.90` | 15,070,000.00 USD | 15,070,000.00 USD | 2,160,000.00 USD | 232,510.00 USD | 252,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 21,040,000.00 USD | 21,040,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `733.70` | 12,420,000.00 USD | 12,420,000.00 USD | 499,050.00 USD | 154,940.00 USD | 165,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 18,630,000.00 USD | 18,630,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `734.50` | 11,600,000.00 USD | 11,600,000.00 USD | 1,370,000.00 USD | 229,660.00 USD | 269,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 16,520,000.00 USD | 16,520,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `735.30` | 9,730,000.00 USD | 9,730,000.00 USD | 564,120.00 USD | 170,380.00 USD | 164,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `736.10` | 8,830,000.00 USD | 8,830,000.00 USD | 788,290.00 USD | 248,020.00 USD | 342,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 14,580,000.00 USD | 14,580,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `736.90` | 7,450,000.00 USD | 7,450,000.00 USD | 1,650,000.00 USD | 54,050.00 USD | 217,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 11,780,000.00 USD | 11,780,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `737.70` | 5,530,000.00 USD | 5,530,000.00 USD | 2,270,000.00 USD | 184,910.00 USD | 410,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 8,610,000.00 USD | 8,610,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `738.50` | 2,660,000.00 USD | 2,660,000.00 USD | 881,020.00 USD | 41,800.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 4,750,000.00 USD | 4,750,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `739.30` | 1,730,000.00 USD | 1,730,000.00 USD | 463,560.00 USD | 0.00 USD | 78,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `739.70` | 4,050,000.00 USD | 4,050,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `740.10` | 1,190,000.00 USD | 1,190,000.00 USD | 567,420.00 USD | 0.00 USD | 26,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `740.60` | 3,490,000.00 USD | 3,490,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `740.90` | 595,380.00 USD | 595,380.00 USD | 230,130.00 USD | 0.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 2,370,000.00 USD | 2,370,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `743.30` | 358,230.00 USD | 358,230.00 USD | 0.00 USD | 43,530.00 USD | 113,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `744.10` | 201,570.00 USD | 201,570.00 USD | 0.00 USD | 18,830.00 USD | 39,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `744.90` | 143,310.00 USD | 143,310.00 USD | 0.00 USD | 29,640.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `746.00` | 1,210,000.00 USD | 1,210,000.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `746.50` | 97,420.00 USD | 97,420.00 USD | 97,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `746.90` | 215,540.00 USD | 215,540.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.70` | 67,380.00 USD | 67,380.00 USD | 0.00 USD | 27,900.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.50` | 103,670.00 USD | 103,670.00 USD | 0.00 USD | 36,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 59,560.00 USD | 59,560.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.30` | 480,650.00 USD | 480,650.00 USD | 143,570.00 USD | 176,520.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.10` | 867,000.00 USD | 867,000.00 USD | 312,560.00 USD | 27,340.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 106,900.00 USD | 106,900.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.90` | 1,030,000.00 USD | 1,030,000.00 USD | 110,260.00 USD | 8,490.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.70` | 1,460,000.00 USD | 1,460,000.00 USD | 249,860.00 USD | 146,640.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 695,650.00 USD | 695,650.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.50` | 1,800,000.00 USD | 1,800,000.00 USD | 311,230.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 1,880,000.00 USD | 1,880,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.30` | 2,640,000.00 USD | 2,640,000.00 USD | 813,190.00 USD | 13,760.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.10` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 32,160.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.90` | 2,910,000.00 USD | 2,910,000.00 USD | 113,590.00 USD | 25,800.00 USD | 74,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 2,290,000.00 USD | 2,290,000.00 USD | 10,750.00 USD | 223,950.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.70` | 3,360,000.00 USD | 3,360,000.00 USD | 264,780.00 USD | 54,040.00 USD | 135,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 699,820.00 USD | 147,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.50` | 3,820,000.00 USD | 3,820,000.00 USD | 212,650.00 USD | 170,950.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 6,590,000.00 USD | 6,590,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.30` | 6,360,000.00 USD | 6,360,000.00 USD | 2,090,000.00 USD | 173,440.00 USD | 273,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 211.49 USD | 211.49 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `764.00` | 9,030,000.00 USD | 9,030,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.10` | 8,360,000.00 USD | 8,360,000.00 USD | 1,530,000.00 USD | 200,630.00 USD | 269,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.90` | 9,240,000.00 USD | 9,240,000.00 USD | 533,660.00 USD | 190,860.00 USD | 149,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 11,230,000.00 USD | 11,230,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.70` | 10,480,000.00 USD | 10,480,000.00 USD | 898,410.00 USD | 136,000.00 USD | 207,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 14,220,000.00 USD | 14,220,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.50` | 11,960,000.00 USD | 11,960,000.00 USD | 828,340.00 USD | 227,270.00 USD | 426,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.70` | 18,820,000.00 USD | 18,820,000.00 USD | 3,340,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.30` | 14,400,000.00 USD | 14,400,000.00 USD | 2,090,000.00 USD | 126,130.00 USD | 214,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 1,050.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `767.60` | 22,210,000.00 USD | 22,210,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.10` | 16,190,000.00 USD | 16,190,000.00 USD | 1,490,000.00 USD | 72,420.00 USD | 226,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 24,430,000.00 USD | 24,430,000.00 USD | 1,850,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.90` | 17,030,000.00 USD | 17,030,000.00 USD | 680,980.00 USD | 67,110.00 USD | 97,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 25,580,000.00 USD | 25,580,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.70` | 17,730,000.00 USD | 17,730,000.00 USD | 518,470.00 USD | 108,350.00 USD | 67,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 28,090,000.00 USD | 28,090,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.50` | 18,370,000.00 USD | 18,370,000.00 USD | 458,460.00 USD | 137,750.00 USD | 43,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 29,550,000.00 USD | 29,550,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.30` | 19,160,000.00 USD | 19,160,000.00 USD | 626,040.00 USD | 67,920.00 USD | 102,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.10` | 19,670,000.00 USD | 19,670,000.00 USD | 333,140.00 USD | 86,890.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 31,970,000.00 USD | 31,970,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.90` | 20,430,000.00 USD | 20,430,000.00 USD | 500,340.00 USD | 101,060.00 USD | 157,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 34,590,000.00 USD | 34,590,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,270.00 USD | 9,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.70` | 21,260,000.00 USD | 21,260,000.00 USD | 556,120.00 USD | 126,820.00 USD | 140,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.90` | 36,380,000.00 USD | 36,380,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.50` | 22,220,000.00 USD | 22,220,000.00 USD | 894,730.00 USD | 31,540.00 USD | 39,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 436.82 USD | 10,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `774.80` | 38,760,000.00 USD | 38,760,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.30` | 22,580,000.00 USD | 22,580,000.00 USD | 211,980.00 USD | 106,740.00 USD | 42,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 41,250,000.00 USD | 41,250,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.10` | 22,930,000.00 USD | 22,930,000.00 USD | 246,910.00 USD | 57,920.00 USD | 38,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 5,120.00 USD | 15,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 43,530,000.00 USD | 43,530,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.90` | 23,380,000.00 USD | 23,380,000.00 USD | 356,670.00 USD | 22,000.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 45,250,000.00 USD | 45,250,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 132,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 2,880.00 USD | 18,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `777.70` | 24,470,000.00 USD | 24,470,000.00 USD | 880,680.00 USD | 88,980.00 USD | 126,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 46,940,000.00 USD | 46,940,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `778.50` | 25,140,000.00 USD | 25,140,000.00 USD | 532,720.00 USD | 83,240.00 USD | 52,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 11,100.00 USD | 29,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.30` | 26,090,000.00 USD | 26,090,000.00 USD | 698,730.00 USD | 101,050.00 USD | 149,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 48,500,000.00 USD | 48,500,000.00 USD | 1,250,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.10` | 26,640,000.00 USD | 26,640,000.00 USD | 380,830.00 USD | 107,240.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 49,880,000.00 USD | 49,880,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 477.67 USD | 29,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.90` | 27,250,000.00 USD | 27,250,000.00 USD | 406,710.00 USD | 60,930.00 USD | 140,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 51,490,000.00 USD | 51,490,000.00 USD | 1,280,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 194.59 USD | 29,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.70` | 28,000,000.00 USD | 28,000,000.00 USD | 483,750.00 USD | 96,520.00 USD | 167,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 53,390,000.00 USD | 53,390,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.50` | 29,250,000.00 USD | 29,250,000.00 USD | 1,050,000.00 USD | 66,420.00 USD | 127,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 247,020.00 USD | 276,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 55,370,000.00 USD | 55,370,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.30` | 30,200,000.00 USD | 30,200,000.00 USD | 806,240.00 USD | 38,580.00 USD | 106,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 55,950,000.00 USD | 55,950,000.00 USD | 510,940.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.10` | 30,530,000.00 USD | 30,530,000.00 USD | 282,620.00 USD | 29,330.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 2,880.00 USD | 279,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.70` | 56,260,000.00 USD | 56,260,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.90` | 30,920,000.00 USD | 30,920,000.00 USD | 350,760.00 USD | 18,370.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 57,390,000.00 USD | 57,390,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.70` | 31,240,000.00 USD | 31,240,000.00 USD | 227,750.00 USD | 49,690.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.50` | 31,520,000.00 USD | 31,520,000.00 USD | 243,510.00 USD | 18,320.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 57,780,000.00 USD | 57,780,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 607.96 USD | 280,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.30` | 31,710,000.00 USD | 31,710,000.00 USD | 144,290.00 USD | 21,200.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 58,350,000.00 USD | 58,350,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 131,800.00 USD | 412,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.10` | 32,010,000.00 USD | 32,010,000.00 USD | 171,550.00 USD | 49,180.00 USD | 82,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 58,720,000.00 USD | 58,720,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 126.16 USD | 412,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.90` | 32,500,000.00 USD | 32,500,000.00 USD | 376,940.00 USD | 46,900.00 USD | 61,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 59,560,000.00 USD | 59,560,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 95.53 USD | 412,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.70` | 32,850,000.00 USD | 32,850,000.00 USD | 321,570.00 USD | 15,770.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 60,050,000.00 USD | 60,050,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.50` | 33,040,000.00 USD | 33,040,000.00 USD | 143,460.00 USD | 40,430.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `790.50` | 137.55 USD | 412,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `791.00` | 60,930,000.00 USD | 60,930,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.30` | 33,240,000.00 USD | 33,240,000.00 USD | 172,830.00 USD | 19,090.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `791.50` | 2,280.00 USD | 414,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `791.90` | 61,800,000.00 USD | 61,800,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.10` | 33,350,000.00 USD | 33,350,000.00 USD | 105,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 62,020,000.00 USD | 62,020,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.90` | 33,370,000.00 USD | 33,370,000.00 USD | 26,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 158.70 USD | 415,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `793.70` | 33,400,000.00 USD | 33,400,000.00 USD | 26,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `793.70` | 62,210,000.00 USD | 62,210,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.50` | 33,440,000.00 USD | 33,440,000.00 USD | 35,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 179.56 USD | 415,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 62,530,000.00 USD | 62,530,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.30` | 33,460,000.00 USD | 33,460,000.00 USD | 22,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 62,670,000.00 USD | 62,670,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 415,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.10` | 33,500,000.00 USD | 33,500,000.00 USD | 38,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 62,810,000.00 USD | 62,810,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 172.84 USD | 415,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.90` | 33,540,000.00 USD | 33,540,000.00 USD | 40,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `797.30` | 62,870,000.00 USD | 62,870,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `797.70` | 33,600,000.00 USD | 33,600,000.00 USD | 57,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `798.20` | 63,030,000.00 USD | 63,030,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `798.50` | 33,630,000.00 USD | 33,630,000.00 USD | 31,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 63,070,000.00 USD | 63,070,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `799.30` | 33,650,000.00 USD | 33,650,000.00 USD | 22,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 63,180,000.00 USD | 63,180,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `800.10` | 33,660,000.00 USD | 33,660,000.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `800.90` | 33,670,000.00 USD | 33,670,000.00 USD | 14,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 63,290,000.00 USD | 63,290,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 761.42 USD | 416,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `801.70` | 33,710,000.00 USD | 33,710,000.00 USD | 41,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `801.80` | 63,500,000.00 USD | 63,500,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.50` | 33,740,000.00 USD | 33,740,000.00 USD | 23,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 416,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 63,510,000.00 USD | 63,510,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.30` | 33,750,000.00 USD | 33,750,000.00 USD | 16,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `803.60` | 63,580,000.00 USD | 63,580,000.00 USD | 63,540.00 USD | 5,560.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `804.10` | 33,760,000.00 USD | 33,760,000.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 63,670,000.00 USD | 63,670,000.00 USD | 32,340.00 USD | 22,610.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 1,080.00 USD | 417,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `804.90` | 33,760,000.00 USD | 33,760,000.00 USD | 7,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 63,740,000.00 USD | 63,740,000.00 USD | 59,610.00 USD | 12,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `805.70` | 33,770,000.00 USD | 33,770,000.00 USD | 7,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `806.30` | 63,760,000.00 USD | 63,760,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `806.50` | 33,770,000.00 USD | 33,770,000.00 USD | 3,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 44,210.00 USD | 462,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `807.20` | 63,810,000.00 USD | 63,810,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `807.30` | 33,790,000.00 USD | 33,790,000.00 USD | 17,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.10` | 33,800,000.00 USD | 33,800,000.00 USD | 9,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `808.10` | 63,870,000.00 USD | 63,870,000.00 USD | 19,950.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.90` | 33,810,000.00 USD | 33,810,000.00 USD | 7,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.00` | 63,950,000.00 USD | 63,950,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `809.70` | 33,810,000.00 USD | 33,810,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.90` | 64,170,000.00 USD | 64,170,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `810.50` | 33,810,000.00 USD | 33,810,000.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `810.80` | 64,260,000.00 USD | 64,260,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `811.50` | 265.36 USD | 462,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `811.70` | 64,320,000.00 USD | 64,320,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `812.10` | 33,820,000.00 USD | 33,820,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 64,440,000.00 USD | 64,440,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `812.90` | 33,830,000.00 USD | 33,830,000.00 USD | 6,350.00 USD | 0.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 64,700,000.00 USD | 64,700,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `813.70` | 33,860,000.00 USD | 33,860,000.00 USD | 24,280.00 USD | 4,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 65,020,000.00 USD | 65,020,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.50` | 33,900,000.00 USD | 33,900,000.00 USD | 25,330.00 USD | 13,710.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.30` | 33,940,000.00 USD | 33,940,000.00 USD | 8,420.00 USD | 11,670.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `815.30` | 65,230,000.00 USD | 65,230,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.10` | 33,960,000.00 USD | 33,960,000.00 USD | 18,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 65,530,000.00 USD | 65,530,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.90` | 34,030,000.00 USD | 34,030,000.00 USD | 44,120.00 USD | 25,520.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `817.10` | 65,930,000.00 USD | 65,930,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `817.70` | 34,060,000.00 USD | 34,060,000.00 USD | 34,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.00` | 66,390,000.00 USD | 66,390,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `818.50` | 34,230,000.00 USD | 34,230,000.00 USD | 159,290.00 USD | 2,750.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 205.44 USD | 462,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 66,630,000.00 USD | 66,630,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 67,140,000.00 USD | 67,140,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.10` | 34,260,000.00 USD | 34,260,000.00 USD | 6,530.00 USD | 8,380.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `820.70` | 67,440,000.00 USD | 67,440,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.90` | 34,300,000.00 USD | 34,300,000.00 USD | 33,880.00 USD | 6,660.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,840.00 USD | 474,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 67,640,000.00 USD | 67,640,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `821.70` | 34,390,000.00 USD | 34,390,000.00 USD | 61,530.00 USD | 4,650.00 USD | 26,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `822.50` | 34,580,000.00 USD | 34,580,000.00 USD | 144,890.00 USD | 24,530.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 68,140,000.00 USD | 68,140,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `823.30` | 34,880,000.00 USD | 34,880,000.00 USD | 263,550.00 USD | 25,420.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 68,470,000.00 USD | 68,470,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 1,730.00 USD | 476,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `824.10` | 35,120,000.00 USD | 35,120,000.00 USD | 164,500.00 USD | 31,520.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 68,820,000.00 USD | 68,820,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `824.50` | 9,950.00 USD | 486,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `824.90` | 35,200,000.00 USD | 35,200,000.00 USD | 46,480.00 USD | 30,530.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 69,180,000.00 USD | 69,180,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `825.70` | 35,390,000.00 USD | 35,390,000.00 USD | 143,670.00 USD | 12,710.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 69,490,000.00 USD | 69,490,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `826.50` | 35,520,000.00 USD | 35,520,000.00 USD | 22,930.00 USD | 38,850.00 USD | 70,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.00` | 70,130,000.00 USD | 70,130,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `827.30` | 35,880,000.00 USD | 35,880,000.00 USD | 335,600.00 USD | 9,730.00 USD | 18,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 70,490,000.00 USD | 70,490,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `828.10` | 36,180,000.00 USD | 36,180,000.00 USD | 224,680.00 USD | 18,700.00 USD | 50,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `828.80` | 70,680,000.00 USD | 70,680,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `828.90` | 36,300,000.00 USD | 36,300,000.00 USD | 107,140.00 USD | 8,360.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `829.70` | 36,350,000.00 USD | 36,350,000.00 USD | 26,690.00 USD | 5,470.00 USD | 13,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 70,770,000.00 USD | 70,770,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `830.50` | 36,440,000.00 USD | 36,440,000.00 USD | 81,870.00 USD | 5,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 71,020,000.00 USD | 71,020,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `831.10` | 36,490,000.00 USD | 36,490,000.00 USD | 50,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 71,060,000.00 USD | 71,060,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 487,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `835.50` | 340.88 USD | 487,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 625.70 USD | 488,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 125.62 USD | 488,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 572.54 USD | 488,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,680.00 USD | 491,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 324.36 USD | 491,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 173,130.00 USD | 665,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 338,650.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `849.50` | 416.25 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 108.99 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 138.43 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 171.10 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 265.59 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 6,240.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `866.50` | 552.83 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `868.50` | 1,530.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `869.50` | 452,190.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 908.44 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 11,910.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 4,540.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 630.44 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `883.50` | 97,180.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,120.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `889.50` | 772.09 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `892.50` | 3,350.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 381.06 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,120.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 392.04 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 901.23 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 39,480.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 195.64 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 285.05 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 111.21 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 952.65 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `943.50` | 3,290.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `945.50` | 110.62 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `955.50` | 967.92 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `958.50` | 58,860.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 67,230.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `962.50` | 837,380.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `964.50` | 1,930.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 16,120.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1000.50` | 697,960.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 1,570.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1017.50` | 36,680.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1021.50` | 137.90 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 104,630.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1049.50` | 294.91 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 391.27 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1071.50` | 1,550.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 19,400.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1094.50` | 189.35 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1118.50` | 6,160.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1140.50` | 152.83 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1151.50` | 1,150.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1159.50` | 56,020.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 9,150.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1169.50` | 367.22 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1173.50` | 14,380.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1181.50` | 158.32 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1183.50` | 132.55 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1200.50` | 29,990.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1212.50` | 8,490.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1252.50` | 100.20 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1254.50` | 339.97 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1260.50` | 201.68 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1264.50` | 752,040.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1269.50` | 161,080.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1286.50` | 115,780.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1303.50` | 19,550.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,260.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1323.50` | 8,610.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1333.50` | 102.68 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1352.50` | 243,450.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1375.50` | 158.18 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1383.50` | 9,980.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1402.50` | 178.12 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1413.50` | 139.94 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1424.50` | 5,690.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1431.50` | 8,770.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1432.50` | 360.99 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1443.50` | 697,040.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1470.50` | 14,460.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1481.50` | 444,450.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1487.50` | 2,660,000.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `156.50` | 4,300,000.00 USD | 0.00 USD | 159.16 USD | `-79.13%` | `1,017,000,000.00` |
| `Live` | `Long` | `178.50` | 4,300,000.00 USD | 0.00 USD | 239.90 USD | `-76.19%` | `1,344,000,000.00` |
| `Live` | `Long` | `218.50` | 4,300,000.00 USD | 0.00 USD | 134.60 USD | `-70.86%` | `616,000,000.00` |
| `Live` | `Long` | `219.50` | 4,300,000.00 USD | 0.00 USD | 460.51 USD | `-70.72%` | `2,098,000,000.00` |
| `Live` | `Long` | `226.50` | 4,300,000.00 USD | 0.00 USD | 712.80 USD | `-69.79%` | `3,147,000,000.00` |
| `Live` | `Long` | `237.50` | 4,300,000.00 USD | 0.00 USD | 1,190.00 USD | `-68.32%` | `5,000,000,000.00` |
| `Live` | `Long` | `257.50` | 4,300,000.00 USD | 0.00 USD | 9,110.00 USD | `-65.65%` | `35,370,000,000.00` |
| `Live` | `Long` | `274.50` | 4,290,000.00 USD | 0.00 USD | 21,760.00 USD | `-63.39%` | `79,269,000,000.00` |
| `Live` | `Long` | `289.50` | 4,270,000.00 USD | 0.00 USD | 916.85 USD | `-61.39%` | `3,167,000,000.00` |
| `Live` | `Long` | `293.50` | 4,260,000.00 USD | 0.00 USD | 286.75 USD | `-60.85%` | `977,000,000.00` |
| `Live` | `Long` | `296.50` | 4,260,000.00 USD | 0.00 USD | 5,950.00 USD | `-60.45%` | `20,052,000,000.00` |
| `Live` | `Long` | `297.50` | 4,260,000.00 USD | 0.00 USD | 20,500.00 USD | `-60.32%` | `68,912,000,000.00` |
| `Live` | `Long` | `300.50` | 4,240,000.00 USD | 0.00 USD | 1,280.00 USD | `-59.92%` | `4,250,000,000.00` |
| `Live` | `Long` | `310.50` | 4,240,000.00 USD | 0.00 USD | 1,640.00 USD | `-58.59%` | `5,281,000,000.00` |
| `Live` | `Long` | `311.50` | 4,230,000.00 USD | 0.00 USD | 109.96 USD | `-58.45%` | `353,000,000.00` |
| `Live` | `Long` | `313.50` | 4,230,000.00 USD | 0.00 USD | 2,110.00 USD | `-58.19%` | `6,732,000,000.00` |
| `Live` | `Long` | `319.50` | 4,230,000.00 USD | 0.00 USD | 366.79 USD | `-57.39%` | `1,148,000,000.00` |
| `Live` | `Long` | `320.50` | 4,230,000.00 USD | 0.00 USD | 886.82 USD | `-57.25%` | `2,767,000,000.00` |
| `Live` | `Long` | `326.50` | 4,230,000.00 USD | 0.00 USD | 500.85 USD | `-56.45%` | `1,534,000,000.00` |
| `Live` | `Long` | `328.50` | 4,230,000.00 USD | 0.00 USD | 315.03 USD | `-56.18%` | `959,000,000.00` |
| `Live` | `Long` | `330.50` | 4,230,000.00 USD | 0.00 USD | 1,080.00 USD | `-55.92%` | `3,259,000,000.00` |
| `Live` | `Long` | `332.50` | 4,230,000.00 USD | 0.00 USD | 1,790.00 USD | `-55.65%` | `5,381,000,000.00` |
| `Live` | `Long` | `333.50` | 4,230,000.00 USD | 0.00 USD | 377.19 USD | `-55.52%` | `1,131,000,000.00` |
| `Live` | `Long` | `335.50` | 4,230,000.00 USD | 0.00 USD | 313.02 USD | `-55.25%` | `933,000,000.00` |
| `Live` | `Long` | `338.50` | 4,230,000.00 USD | 0.00 USD | 23,420.00 USD | `-54.85%` | `69,189,000,000.00` |
| `Live` | `Long` | `343.50` | 4,200,000.00 USD | 0.00 USD | 652.65 USD | `-54.18%` | `1,900,000,000.00` |
| `Live` | `Long` | `348.50` | 4,200,000.00 USD | 0.00 USD | 2,940.00 USD | `-53.52%` | `8,445,000,000.00` |
| `Live` | `Long` | `354.50` | 4,200,000.00 USD | 0.00 USD | 749.77 USD | `-52.72%` | `2,115,000,000.00` |
| `Live` | `Long` | `355.50` | 4,200,000.00 USD | 0.00 USD | 42,640.00 USD | `-52.58%` | `119,940,000,000.00` |
| `Live` | `Long` | `359.50` | 4,160,000.00 USD | 0.00 USD | 212.10 USD | `-52.05%` | `590,000,000.00` |
| `Live` | `Long` | `366.50` | 4,160,000.00 USD | 0.00 USD | 549.75 USD | `-51.12%` | `1,500,000,000.00` |
| `Live` | `Long` | `367.50` | 4,160,000.00 USD | 0.00 USD | 2,870.00 USD | `-50.98%` | `7,799,000,000.00` |
| `Live` | `Long` | `374.50` | 4,150,000.00 USD | 0.00 USD | 240.43 USD | `-50.05%` | `642,000,000.00` |
| `Live` | `Long` | `375.50` | 4,150,000.00 USD | 0.00 USD | 13,690.00 USD | `-49.92%` | `36,463,000,000.00` |
| `Live` | `Long` | `377.50` | 4,140,000.00 USD | 0.00 USD | 438.65 USD | `-49.65%` | `1,162,000,000.00` |
| `Live` | `Long` | `378.50` | 4,140,000.00 USD | 0.00 USD | 953.44 USD | `-49.52%` | `2,519,000,000.00` |
| `Live` | `Long` | `379.50` | 4,140,000.00 USD | 0.00 USD | 645.15 USD | `-49.38%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,140,000.00 USD | 0.00 USD | 321.22 USD | `-49.12%` | `842,000,000.00` |
| `Live` | `Long` | `382.50` | 4,140,000.00 USD | 0.00 USD | 1,910.00 USD | `-48.98%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 4,130,000.00 USD | 0.00 USD | 10,900.00 USD | `-48.85%` | `28,414,000,000.00` |
| `Live` | `Long` | `385.50` | 4,120,000.00 USD | 0.00 USD | 16,020.00 USD | `-48.58%` | `41,550,000,000.00` |
| `Live` | `Long` | `386.50` | 4,110,000.00 USD | 0.00 USD | 531.44 USD | `-48.45%` | `1,375,000,000.00` |
| `Live` | `Long` | `393.50` | 4,110,000.00 USD | 0.00 USD | 435.21 USD | `-47.52%` | `1,106,000,000.00` |
| `Live` | `Long` | `394.50` | 4,110,000.00 USD | 0.00 USD | 168.06 USD | `-47.38%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 4,110,000.00 USD | 0.00 USD | 2,110.00 USD | `-47.25%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 4,100,000.00 USD | 0.00 USD | 396.50 USD | `-47.11%` | `1,000,000,000.00` |
| `Live` | `Long` | `397.50` | 4,100,000.00 USD | 0.00 USD | 318.00 USD | `-46.98%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 4,100,000.00 USD | 0.00 USD | 523.63 USD | `-46.85%` | `1,314,000,000.00` |
| `Live` | `Long` | `400.50` | 4,100,000.00 USD | 0.00 USD | 605.16 USD | `-46.58%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 4,100,000.00 USD | 0.00 USD | 102.34 USD | `-46.05%` | `253,000,000.00` |
| `Live` | `Long` | `405.50` | 4,100,000.00 USD | 0.00 USD | 28,390.00 USD | `-45.91%` | `70,000,000,000.00` |
| `Live` | `Long` | `407.50` | 4,070,000.00 USD | 0.00 USD | 3,450.00 USD | `-45.65%` | `8,455,000,000.00` |
| `Live` | `Long` | `408.50` | 4,070,000.00 USD | 0.00 USD | 551.07 USD | `-45.51%` | `1,349,000,000.00` |
| `Live` | `Long` | `410.50` | 4,070,000.00 USD | 0.00 USD | 614.52 USD | `-45.25%` | `1,497,000,000.00` |
| `Live` | `Long` | `411.50` | 4,070,000.00 USD | 0.00 USD | 106.17 USD | `-45.11%` | `258,000,000.00` |
| `Live` | `Long` | `414.50` | 4,070,000.00 USD | 0.00 USD | 13,320.00 USD | `-44.71%` | `32,128,000,000.00` |
| `Live` | `Long` | `415.50` | 4,060,000.00 USD | 0.00 USD | 1,810.00 USD | `-44.58%` | `4,368,000,000.00` |
| `Live` | `Long` | `416.50` | 4,050,000.00 USD | 0.00 USD | 974.19 USD | `-44.45%` | `2,339,000,000.00` |
| `Live` | `Long` | `417.50` | 4,050,000.00 USD | 0.00 USD | 7,140.00 USD | `-44.31%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 4,050,000.00 USD | 0.00 USD | 465.79 USD | `-44.18%` | `1,113,000,000.00` |
| `Live` | `Long` | `420.50` | 4,050,000.00 USD | 0.00 USD | 2,660.00 USD | `-43.91%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 4,040,000.00 USD | 0.00 USD | 2,320.00 USD | `-43.78%` | `5,496,000,000.00` |
| `Live` | `Long` | `423.50` | 4,040,000.00 USD | 0.00 USD | 1,450.00 USD | `-43.51%` | `3,419,000,000.00` |
| `Live` | `Long` | `427.50` | 4,040,000.00 USD | 0.00 USD | 12,150.00 USD | `-42.98%` | `28,425,000,000.00` |
| `Live` | `Long` | `430.50` | 4,030,000.00 USD | 0.00 USD | 638.00 USD | `-42.58%` | `1,482,000,000.00` |
| `Live` | `Long` | `438.50` | 4,030,000.00 USD | 0.00 USD | 1,790.00 USD | `-41.51%` | `4,087,000,000.00` |
| `Live` | `Long` | `440.50` | 4,020,000.00 USD | 0.00 USD | 968.22 USD | `-41.25%` | `2,198,000,000.00` |
| `Live` | `Long` | `445.50` | 4,020,000.00 USD | 0.00 USD | 2,330.00 USD | `-40.58%` | `5,235,000,000.00` |
| `Live` | `Long` | `454.50` | 4,020,000.00 USD | 0.00 USD | 4,220.00 USD | `-39.38%` | `9,287,000,000.00` |
| `Live` | `Long` | `456.50` | 4,020,000.00 USD | 0.00 USD | 4,730.00 USD | `-39.11%` | `10,359,000,000.00` |
| `Live` | `Long` | `457.50` | 4,010,000.00 USD | 0.00 USD | 463.45 USD | `-38.98%` | `1,013,000,000.00` |
| `Live` | `Long` | `466.50` | 4,010,000.00 USD | 0.00 USD | 8,860.00 USD | `-37.78%` | `19,000,000,000.00` |
| `Live` | `Long` | `470.50` | 4,000,000.00 USD | 0.00 USD | 4,380.00 USD | `-37.24%` | `9,301,000,000.00` |
| `Live` | `Long` | `471.50` | 4,000,000.00 USD | 0.00 USD | 471.50 USD | `-37.11%` | `1,000,000,000.00` |
| `Live` | `Long` | `474.50` | 4,000,000.00 USD | 0.00 USD | 5,500.00 USD | `-36.71%` | `11,600,000,000.00` |
| `Live` | `Long` | `476.50` | 3,990,000.00 USD | 0.00 USD | 5,330.00 USD | `-36.44%` | `11,182,000,000.00` |
| `Live` | `Long` | `483.50` | 3,990,000.00 USD | 0.00 USD | 2,020.00 USD | `-35.51%` | `4,170,000,000.00` |
| `Live` | `Long` | `488.50` | 3,990,000.00 USD | 0.00 USD | 976.51 USD | `-34.84%` | `1,999,000,000.00` |
| `Live` | `Long` | `496.50` | 3,980,000.00 USD | 0.00 USD | 248.25 USD | `-33.78%` | `500,000,000.00` |
| `Live` | `Long` | `498.50` | 3,980,000.00 USD | 0.00 USD | 2,120.00 USD | `-33.51%` | `4,246,000,000.00` |
| `Live` | `Long` | `501.50` | 3,980,000.00 USD | 0.00 USD | 7,760.00 USD | `-33.11%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 3,970,000.00 USD | 0.00 USD | 109.04 USD | `-32.98%` | `217,000,000.00` |
| `Live` | `Long` | `509.50` | 3,970,000.00 USD | 0.00 USD | 3,610.00 USD | `-32.04%` | `7,091,000,000.00` |
| `Live` | `Long` | `510.50` | 3,970,000.00 USD | 0.00 USD | 1,570.00 USD | `-31.91%` | `3,072,000,000.00` |
| `Live` | `Long` | `511.50` | 3,970,000.00 USD | 0.00 USD | 158.56 USD | `-31.78%` | `310,000,000.00` |
| `Live` | `Long` | `512.50` | 3,970,000.00 USD | 0.00 USD | 5,190.00 USD | `-31.64%` | `10,118,000,000.00` |
| `Live` | `Long` | `514.50` | 3,960,000.00 USD | 0.00 USD | 4,010.00 USD | `-31.38%` | `7,787,000,000.00` |
| `Live` | `Long` | `515.50` | 3,960,000.00 USD | 0.00 USD | 3,780.00 USD | `-31.24%` | `7,323,000,000.00` |
| `Live` | `Long` | `516.50` | 3,960,000.00 USD | 0.00 USD | 12,890.00 USD | `-31.11%` | `24,956,000,000.00` |
| `Live` | `Long` | `517.50` | 3,940,000.00 USD | 0.00 USD | 1,160.00 USD | `-30.98%` | `2,246,000,000.00` |
| `Live` | `Long` | `519.50` | 3,940,000.00 USD | 0.00 USD | 6,390.00 USD | `-30.71%` | `12,307,000,000.00` |
| `Live` | `Long` | `520.50` | 3,940,000.00 USD | 0.00 USD | 3,560.00 USD | `-30.58%` | `6,833,000,000.00` |
| `Live` | `Long` | `521.50` | 3,930,000.00 USD | 0.00 USD | 1,040.00 USD | `-30.44%` | `1,987,000,000.00` |
| `Live` | `Long` | `522.50` | 3,930,000.00 USD | 0.00 USD | 440.99 USD | `-30.31%` | `844,000,000.00` |
| `Live` | `Long` | `523.50` | 3,930,000.00 USD | 0.00 USD | 2,090.00 USD | `-30.18%` | `3,993,000,000.00` |
| `Live` | `Long` | `524.50` | 3,930,000.00 USD | 0.00 USD | 1,460.00 USD | `-30.04%` | `2,790,000,000.00` |
| `Live` | `Long` | `525.50` | 3,930,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.91%` | `2,298,000,000.00` |
| `Live` | `Long` | `526.50` | 3,930,000.00 USD | 0.00 USD | 5,730.00 USD | `-29.78%` | `10,892,000,000.00` |
| `Live` | `Long` | `528.50` | 3,920,000.00 USD | 0.00 USD | 160.14 USD | `-29.51%` | `303,000,000.00` |
| `Live` | `Long` | `529.50` | 3,920,000.00 USD | 0.00 USD | 43,440.00 USD | `-29.38%` | `82,042,000,000.00` |
| `Live` | `Long` | `530.50` | 3,880,000.00 USD | 0.00 USD | 16,980.00 USD | `-29.24%` | `32,010,000,000.00` |
| `Live` | `Long` | `531.50` | 3,860,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-29.11%` | `2,808,112,000,000.00` |
| `Live` | `Long` | `532.50` | 2,370,000.00 USD | 0.00 USD | 1,880.00 USD | `-28.98%` | `3,523,000,000.00` |
| `Live` | `Long` | `534.50` | 2,360,000.00 USD | 0.00 USD | 555.35 USD | `-28.71%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 2,360,000.00 USD | 0.00 USD | 267.75 USD | `-28.58%` | `500,000,000.00` |
| `Live` | `Long` | `536.50` | 2,360,000.00 USD | 0.00 USD | 100.33 USD | `-28.44%` | `187,000,000.00` |
| `Live` | `Long` | `537.50` | 2,360,000.00 USD | 0.00 USD | 4,300.00 USD | `-28.31%` | `8,000,000,000.00` |
| `Live` | `Long` | `539.50` | 2,360,000.00 USD | 0.00 USD | 490.94 USD | `-28.04%` | `910,000,000.00` |
| `Live` | `Long` | `541.50` | 2,360,000.00 USD | 0.00 USD | 472.19 USD | `-27.77%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 2,360,000.00 USD | 0.00 USD | 334.25 USD | `-27.51%` | `615,000,000.00` |
| `Live` | `Long` | `545.50` | 2,360,000.00 USD | 0.00 USD | 212,310.00 USD | `-27.24%` | `389,204,000,000.00` |
| `Live` | `Long` | `546.50` | 2,150,000.00 USD | 0.00 USD | 491.85 USD | `-27.11%` | `900,000,000.00` |
| `Live` | `Long` | `547.50` | 2,150,000.00 USD | 0.00 USD | 531.07 USD | `-26.97%` | `970,000,000.00` |
| `Live` | `Long` | `549.50` | 2,140,000.00 USD | 0.00 USD | 1,770.00 USD | `-26.71%` | `3,224,000,000.00` |
| `Live` | `Long` | `550.50` | 2,140,000.00 USD | 0.00 USD | 633.63 USD | `-26.57%` | `1,151,000,000.00` |
| `Live` | `Long` | `552.50` | 2,140,000.00 USD | 0.00 USD | 959.69 USD | `-26.31%` | `1,737,000,000.00` |
| `Live` | `Long` | `553.50` | 2,140,000.00 USD | 0.00 USD | 2,420.00 USD | `-26.17%` | `4,365,000,000.00` |
| `Live` | `Long` | `554.50` | 2,140,000.00 USD | 0.00 USD | 2,010.00 USD | `-26.04%` | `3,625,000,000.00` |
| `Live` | `Long` | `555.50` | 2,140,000.00 USD | 0.00 USD | 591.61 USD | `-25.91%` | `1,065,000,000.00` |
| `Live` | `Long` | `557.50` | 2,140,000.00 USD | 0.00 USD | 5,680.00 USD | `-25.64%` | `10,193,000,000.00` |
| `Live` | `Long` | `558.50` | 2,130,000.00 USD | 0.00 USD | 385.36 USD | `-25.51%` | `690,000,000.00` |
| `Live` | `Long` | `559.50` | 2,130,000.00 USD | 0.00 USD | 212.61 USD | `-25.37%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 2,130,000.00 USD | 0.00 USD | 10,280.00 USD | `-25.24%` | `18,342,000,000.00` |
| `Live` | `Long` | `561.50` | 2,120,000.00 USD | 0.00 USD | 15,170.00 USD | `-25.11%` | `27,020,000,000.00` |
| `Live` | `Long` | `564.50` | 2,100,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.71%` | `25,181,000,000.00` |
| `Live` | `Long` | `567.50` | 2,090,000.00 USD | 0.00 USD | 377.39 USD | `-24.31%` | `665,000,000.00` |
| `Live` | `Long` | `572.50` | 2,090,000.00 USD | 0.00 USD | 715,280.00 USD | `-23.64%` | `1,249,401,000,000.00` |
| `Live` | `Long` | `574.50` | 1,370,000.00 USD | 0.00 USD | 323.44 USD | `-23.37%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 1,370,000.00 USD | 0.00 USD | 862.44 USD | `-23.11%` | `1,496,000,000.00` |
| `Live` | `Long` | `577.50` | 1,370,000.00 USD | 0.00 USD | 222.91 USD | `-22.97%` | `386,000,000.00` |
| `Live` | `Long` | `578.50` | 1,370,000.00 USD | 0.00 USD | 275.37 USD | `-22.84%` | `476,000,000.00` |
| `Live` | `Long` | `579.50` | 1,370,000.00 USD | 0.00 USD | 2,320.00 USD | `-22.71%` | `4,005,000,000.00` |
| `Live` | `Long` | `580.50` | 1,370,000.00 USD | 0.00 USD | 4,060.00 USD | `-22.57%` | `7,002,000,000.00` |
| `Live` | `Long` | `583.50` | 1,370,000.00 USD | 0.00 USD | 275.41 USD | `-22.17%` | `472,000,000.00` |
| `Live` | `Long` | `584.50` | 1,370,000.00 USD | 0.00 USD | 6,810.00 USD | `-22.04%` | `11,659,000,000.00` |
| `Live` | `Long` | `586.50` | 1,360,000.00 USD | 0.00 USD | 2,540.00 USD | `-21.77%` | `4,339,000,000.00` |
| `Live` | `Long` | `587.50` | 1,360,000.00 USD | 0.00 USD | 1,530.00 USD | `-21.64%` | `2,612,000,000.00` |
| `Live` | `Long` | `588.50` | 1,360,000.00 USD | 0.00 USD | 1,660.00 USD | `-21.51%` | `2,814,000,000.00` |
| `Live` | `Long` | `590.50` | 1,350,000.00 USD | 0.00 USD | 100.39 USD | `-21.24%` | `170,000,000.00` |
| `Live` | `Long` | `592.50` | 1,350,000.00 USD | 0.00 USD | 1,240.00 USD | `-20.97%` | `2,097,000,000.00` |
| `Live` | `Long` | `594.50` | 1,350,000.00 USD | 0.00 USD | 44,800.00 USD | `-20.71%` | `75,354,000,000.00` |
| `Live` | `Long` | `597.50` | 1,310,000.00 USD | 0.00 USD | 100.98 USD | `-20.31%` | `169,000,000.00` |
| `Live` | `Long` | `598.50` | 1,310,000.00 USD | 0.00 USD | 1,560.00 USD | `-20.17%` | `2,606,000,000.00` |
| `Live` | `Long` | `599.50` | 1,310,000.00 USD | 0.00 USD | 116.90 USD | `-20.04%` | `195,000,000.00` |
| `Live` | `Long` | `600.50` | 1,310,000.00 USD | 0.00 USD | 1,270.00 USD | `-19.91%` | `2,115,000,000.00` |
| `Live` | `Long` | `601.50` | 1,300,000.00 USD | 0.00 USD | 303.76 USD | `-19.77%` | `505,000,000.00` |
| `Live` | `Long` | `604.50` | 1,300,000.00 USD | 0.00 USD | 1,610.00 USD | `-19.37%` | `2,671,000,000.00` |
| `Live` | `Long` | `607.50` | 1,300,000.00 USD | 0.00 USD | 1,880.00 USD | `-18.97%` | `3,092,000,000.00` |
| `Live` | `Long` | `610.50` | 1,300,000.00 USD | 0.00 USD | 213.67 USD | `-18.57%` | `350,000,000.00` |
| `Live` | `Long` | `611.50` | 1,300,000.00 USD | 0.00 USD | 185.28 USD | `-18.44%` | `303,000,000.00` |
| `Live` | `Long` | `612.50` | 1,300,000.00 USD | 0.00 USD | 735.00 USD | `-18.31%` | `1,200,000,000.00` |
| `Live` | `Long` | `613.50` | 1,300,000.00 USD | 0.00 USD | 527.00 USD | `-18.17%` | `859,000,000.00` |
| `Live` | `Long` | `614.50` | 1,300,000.00 USD | 0.00 USD | 2,550.00 USD | `-18.04%` | `4,148,000,000.00` |
| `Live` | `Long` | `615.50` | 1,300,000.00 USD | 0.00 USD | 427.16 USD | `-17.90%` | `694,000,000.00` |
| `Live` | `Long` | `616.50` | 1,300,000.00 USD | 0.00 USD | 770.62 USD | `-17.77%` | `1,250,000,000.00` |
| `Live` | `Long` | `617.50` | 1,300,000.00 USD | 0.00 USD | 156.23 USD | `-17.64%` | `253,000,000.00` |
| `Live` | `Long` | `620.50` | 1,300,000.00 USD | 0.00 USD | 5,410.00 USD | `-17.24%` | `8,712,000,000.00` |
| `Live` | `Long` | `621.50` | 1,290,000.00 USD | 0.00 USD | 1,250.00 USD | `-17.10%` | `2,018,000,000.00` |
| `Live` | `Long` | `622.50` | 1,290,000.00 USD | 0.00 USD | 2,110.00 USD | `-16.97%` | `3,397,000,000.00` |
| `Live` | `Long` | `623.50` | 1,290,000.00 USD | 0.00 USD | 1,050.00 USD | `-16.84%` | `1,691,000,000.00` |
| `Live` | `Long` | `624.50` | 1,290,000.00 USD | 0.00 USD | 3,460.00 USD | `-16.70%` | `5,547,000,000.00` |
| `Live` | `Long` | `625.50` | 1,280,000.00 USD | 0.00 USD | 11,970.00 USD | `-16.57%` | `19,142,000,000.00` |
| `Live` | `Long` | `626.50` | 1,270,000.00 USD | 0.00 USD | 16,020.00 USD | `-16.44%` | `25,566,000,000.00` |
| `Live` | `Long` | `627.50` | 1,250,000.00 USD | 0.00 USD | 326.30 USD | `-16.30%` | `520,000,000.00` |
| `Live` | `Long` | `628.50` | 1,250,000.00 USD | 0.00 USD | 664.32 USD | `-16.17%` | `1,057,000,000.00` |
| `Live` | `Long` | `629.50` | 1,250,000.00 USD | 0.00 USD | 3,680.00 USD | `-16.04%` | `5,849,000,000.00` |
| `Live` | `Long` | `631.50` | 1,250,000.00 USD | 0.00 USD | 6,320.00 USD | `-15.77%` | `10,000,000,000.00` |
| `Live` | `Long` | `632.50` | 1,240,000.00 USD | 0.00 USD | 125.87 USD | `-15.64%` | `199,000,000.00` |
| `Live` | `Long` | `633.50` | 1,240,000.00 USD | 0.00 USD | 4,100.00 USD | `-15.50%` | `6,478,000,000.00` |
| `Live` | `Long` | `635.50` | 1,240,000.00 USD | 0.00 USD | 5,910.00 USD | `-15.24%` | `9,302,000,000.00` |
| `Live` | `Long` | `636.50` | 1,230,000.00 USD | 0.00 USD | 5,140.00 USD | `-15.10%` | `8,083,000,000.00` |
| `Live` | `Long` | `637.50` | 1,230,000.00 USD | 0.00 USD | 10,020.00 USD | `-14.97%` | `15,720,000,000.00` |
| `Live` | `Long` | `638.50` | 1,220,000.00 USD | 0.00 USD | 432.90 USD | `-14.84%` | `678,000,000.00` |
| `Live` | `Long` | `639.50` | 1,220,000.00 USD | 0.00 USD | 34,090.00 USD | `-14.70%` | `53,311,000,000.00` |
| `Live` | `Long` | `640.50` | 1,180,000.00 USD | 0.00 USD | 3,910.00 USD | `-14.57%` | `6,099,000,000.00` |
| `Live` | `Long` | `641.50` | 1,180,000.00 USD | 0.00 USD | 1,670.00 USD | `-14.44%` | `2,606,000,000.00` |
| `Live` | `Long` | `642.50` | 1,180,000.00 USD | 0.00 USD | 485.09 USD | `-14.30%` | `755,000,000.00` |
| `Live` | `Long` | `643.50` | 1,180,000.00 USD | 0.00 USD | 8,490.00 USD | `-14.17%` | `13,199,000,000.00` |
| `Live` | `Long` | `645.50` | 1,170,000.00 USD | 0.00 USD | 3,820.00 USD | `-13.90%` | `5,914,000,000.00` |
| `Live` | `Long` | `646.50` | 1,160,000.00 USD | 0.00 USD | 155.81 USD | `-13.77%` | `241,000,000.00` |
| `Live` | `Long` | `649.50` | 1,160,000.00 USD | 0.00 USD | 559.87 USD | `-13.37%` | `862,000,000.00` |
| `Live` | `Long` | `651.50` | 1,160,000.00 USD | 0.00 USD | 633.26 USD | `-13.10%` | `972,000,000.00` |
| `Live` | `Long` | `654.50` | 1,160,000.00 USD | 0.00 USD | 97,640.00 USD | `-12.70%` | `149,175,000,000.00` |
| `Live` | `Long` | `656.50` | 1,070,000.00 USD | 0.00 USD | 122.77 USD | `-12.44%` | `187,000,000.00` |
| `Live` | `Long` | `657.50` | 1,070,000.00 USD | 0.00 USD | 2,180.00 USD | `-12.30%` | `3,321,000,000.00` |
| `Live` | `Long` | `658.50` | 1,060,000.00 USD | 0.00 USD | 4,800.00 USD | `-12.17%` | `7,282,000,000.00` |
| `Live` | `Long` | `660.50` | 1,060,000.00 USD | 0.00 USD | 3,340.00 USD | `-11.90%` | `5,053,000,000.00` |
| `Live` | `Long` | `661.50` | 1,060,000.00 USD | 0.00 USD | 463.71 USD | `-11.77%` | `701,000,000.00` |
| `Live` | `Long` | `662.50` | 1,060,000.00 USD | 0.00 USD | 19,830.00 USD | `-11.64%` | `29,930,000,000.00` |
| `Live` | `Long` | `663.50` | 1,040,000.00 USD | 0.00 USD | 2,070.00 USD | `-11.50%` | `3,115,000,000.00` |
| `Live` | `Long` | `666.50` | 1,030,000.00 USD | 0.00 USD | 5,440.00 USD | `-11.10%` | `8,159,000,000.00` |
| `Live` | `Long` | `669.50` | 1,030,000.00 USD | 0.00 USD | 3,040.00 USD | `-10.70%` | `4,542,000,000.00` |
| `Live` | `Long` | `670.50` | 1,020,000.00 USD | 0.00 USD | 3,460.00 USD | `-10.57%` | `5,166,000,000.00` |
| `Live` | `Long` | `671.50` | 1,020,000.00 USD | 0.00 USD | 3,360.00 USD | `-10.44%` | `5,000,000,000.00` |
| `Live` | `Long` | `672.50` | 1,020,000.00 USD | 0.00 USD | 12,130.00 USD | `-10.30%` | `18,032,000,000.00` |
| `Live` | `Long` | `673.50` | 1,010,000.00 USD | 0.00 USD | 567.76 USD | `-10.17%` | `843,000,000.00` |
| `Live` | `Long` | `674.50` | 1,010,000.00 USD | 0.00 USD | 259.68 USD | `-10.04%` | `385,000,000.00` |
| `Live` | `Long` | `678.50` | 1,000,000.00 USD | 0.00 USD | 2,490.00 USD | `-9.50%` | `3,672,000,000.00` |
| `Live` | `Long` | `681.50` | 1,000,000.00 USD | 0.00 USD | 31,450.00 USD | `-9.10%` | `46,154,000,000.00` |
| `Live` | `Long` | `684.50` | 970,940.00 USD | 0.00 USD | 42,430.00 USD | `-8.70%` | `61,984,000,000.00` |
| `Live` | `Long` | `685.50` | 928,510.00 USD | 0.00 USD | 1,290.00 USD | `-8.57%` | `1,882,000,000.00` |
| `Live` | `Long` | `686.50` | 927,220.00 USD | 0.00 USD | 194.28 USD | `-8.43%` | `283,000,000.00` |
| `Live` | `Long` | `687.50` | 927,030.00 USD | 0.00 USD | 374.69 USD | `-8.30%` | `545,000,000.00` |
| `Live` | `Long` | `689.50` | 926,660.00 USD | 0.00 USD | 885.32 USD | `-8.03%` | `1,284,000,000.00` |
| `Live` | `Long` | `690.50` | 925,770.00 USD | 0.00 USD | 6,170.00 USD | `-7.90%` | `8,933,000,000.00` |
| `Live` | `Long` | `691.50` | 919,600.00 USD | 0.00 USD | 5,430.00 USD | `-7.77%` | `7,853,000,000.00` |
| `Live` | `Long` | `692.50` | 914,170.00 USD | 0.00 USD | 5,580.00 USD | `-7.63%` | `8,061,000,000.00` |
| `Live` | `Long` | `693.50` | 908,590.00 USD | 0.00 USD | 2,590.00 USD | `-7.50%` | `3,732,000,000.00` |
| `Live` | `Long` | `694.50` | 906,000.00 USD | 0.00 USD | 685.47 USD | `-7.37%` | `987,000,000.00` |
| `Live` | `Long` | `695.50` | 905,320.00 USD | 0.00 USD | 299.07 USD | `-7.23%` | `430,000,000.00` |
| `Live` | `Long` | `696.50` | 905,020.00 USD | 0.00 USD | 1,420.00 USD | `-7.10%` | `2,033,000,000.00` |
| `Live` | `Long` | `697.50` | 903,600.00 USD | 0.00 USD | 742.14 USD | `-6.97%` | `1,064,000,000.00` |
| `Live` | `Long` | `698.50` | 902,860.00 USD | 0.00 USD | 137.60 USD | `-6.83%` | `197,000,000.00` |
| `Live` | `Long` | `699.50` | 902,720.00 USD | 0.00 USD | 20,100.00 USD | `-6.70%` | `28,732,000,000.00` |
| `Live` | `Long` | `700.50` | 882,620.00 USD | 0.00 USD | 1,130.00 USD | `-6.57%` | `1,612,000,000.00` |
| `Live` | `Long` | `702.50` | 881,490.00 USD | 0.00 USD | 2,080.00 USD | `-6.30%` | `2,956,000,000.00` |
| `Live` | `Long` | `703.50` | 879,420.00 USD | 0.00 USD | 3,820.00 USD | `-6.17%` | `5,425,000,000.00` |
| `Live` | `Long` | `704.50` | 875,600.00 USD | 0.00 USD | 3,190.00 USD | `-6.03%` | `4,530,000,000.00` |
| `Live` | `Long` | `705.50` | 872,410.00 USD | 0.00 USD | 829.67 USD | `-5.90%` | `1,176,000,000.00` |
| `Live` | `Long` | `706.50` | 871,580.00 USD | 0.00 USD | 23,730.00 USD | `-5.77%` | `33,589,000,000.00` |
| `Live` | `Long` | `707.50` | 847,850.00 USD | 0.00 USD | 22,730.00 USD | `-5.63%` | `32,121,000,000.00` |
| `Live` | `Long` | `708.50` | 825,120.00 USD | 0.00 USD | 171,950.00 USD | `-5.50%` | `242,695,000,000.00` |
| `Live` | `Long` | `709.50` | 653,170.00 USD | 0.00 USD | 341,220.00 USD | `-5.37%` | `480,924,000,000.00` |
| `Live` | `Long` | `710.50` | 311,960.00 USD | 0.00 USD | 43,190.00 USD | `-5.23%` | `60,784,000,000.00` |
| `Live` | `Long` | `711.50` | 268,770.00 USD | 0.00 USD | 11,390.00 USD | `-5.10%` | `16,011,000,000.00` |
| `Live` | `Long` | `712.50` | 257,380.00 USD | 0.00 USD | 229,760.00 USD | `-4.97%` | `322,464,000,000.00` |
| `Live` | `Long` | `713.50` | 27,620.00 USD | 0.00 USD | 21,880.00 USD | `-4.83%` | `30,659,000,000.00` |
| `Live` | `Long` | `714.50` | 5,750.00 USD | 0.00 USD | 157.90 USD | `-4.70%` | `221,000,000.00` |
| `Live` | `Long` | `716.50` | 5,590.00 USD | 0.00 USD | 789.58 USD | `-4.43%` | `1,102,000,000.00` |
| `Live` | `Long` | `717.50` | 4,800.00 USD | 0.00 USD | 3,700.00 USD | `-4.30%` | `5,155,000,000.00` |
| `Live` | `Long` | `718.50` | 1,100.00 USD | 0.00 USD | 104.18 USD | `-4.17%` | `145,000,000.00` |
| `Live` | `Long` | `721.50` | 998.56 USD | 0.00 USD | 998.56 USD | `-3.77%` | `1,384,000,000.00` |
| `Live` | `Short` | `763.50` | 211.49 USD | 211.49 USD | 0.00 USD | `+1.84%` | `277,000,000.00` |
| `Live` | `Short` | `767.50` | 1,260.00 USD | 1,050.00 USD | 0.00 USD | `+2.37%` | `1,365,000,000.00` |
| `Live` | `Short` | `768.50` | 1,420.00 USD | 156.77 USD | 0.00 USD | `+2.50%` | `204,000,000.00` |
| `Live` | `Short` | `773.50` | 9,690.00 USD | 8,270.00 USD | 0.00 USD | `+3.17%` | `10,692,000,000.00` |
| `Live` | `Short` | `774.50` | 10,120.00 USD | 436.82 USD | 0.00 USD | `+3.30%` | `564,000,000.00` |
| `Live` | `Short` | `776.50` | 15,240.00 USD | 5,120.00 USD | 0.00 USD | `+3.57%` | `6,594,000,000.00` |
| `Live` | `Short` | `777.50` | 18,120.00 USD | 2,880.00 USD | 0.00 USD | `+3.70%` | `3,705,000,000.00` |
| `Live` | `Short` | `778.50` | 29,230.00 USD | 11,100.00 USD | 0.00 USD | `+3.84%` | `14,263,000,000.00` |
| `Live` | `Short` | `780.50` | 29,710.00 USD | 477.67 USD | 0.00 USD | `+4.10%` | `612,000,000.00` |
| `Live` | `Short` | `781.50` | 29,900.00 USD | 194.59 USD | 0.00 USD | `+4.24%` | `249,000,000.00` |
| `Live` | `Short` | `782.50` | 276,920.00 USD | 247,020.00 USD | 0.00 USD | `+4.37%` | `315,684,000,000.00` |
| `Live` | `Short` | `784.50` | 279,800.00 USD | 2,880.00 USD | 0.00 USD | `+4.64%` | `3,667,000,000.00` |
| `Live` | `Short` | `786.50` | 280,410.00 USD | 607.96 USD | 0.00 USD | `+4.90%` | `773,000,000.00` |
| `Live` | `Short` | `787.50` | 412,210.00 USD | 131,800.00 USD | 0.00 USD | `+5.04%` | `167,370,000,000.00` |
| `Live` | `Short` | `788.50` | 412,340.00 USD | 126.16 USD | 0.00 USD | `+5.17%` | `160,000,000.00` |
| `Live` | `Short` | `789.50` | 412,430.00 USD | 95.53 USD | 0.00 USD | `+5.30%` | `121,000,000.00` |
| `Live` | `Short` | `790.50` | 412,570.00 USD | 137.55 USD | 0.00 USD | `+5.44%` | `174,000,000.00` |
| `Live` | `Short` | `791.50` | 414,850.00 USD | 2,280.00 USD | 0.00 USD | `+5.57%` | `2,875,000,000.00` |
| `Live` | `Short` | `793.50` | 415,000.00 USD | 158.70 USD | 0.00 USD | `+5.84%` | `200,000,000.00` |
| `Live` | `Short` | `794.50` | 415,180.00 USD | 179.56 USD | 0.00 USD | `+5.97%` | `226,000,000.00` |
| `Live` | `Short` | `795.50` | 415,700.00 USD | 518.67 USD | 0.00 USD | `+6.10%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 415,880.00 USD | 172.84 USD | 0.00 USD | `+6.24%` | `217,000,000.00` |
| `Live` | `Short` | `801.50` | 416,640.00 USD | 761.42 USD | 0.00 USD | `+6.90%` | `950,000,000.00` |
| `Live` | `Short` | `802.50` | 416,920.00 USD | 279.27 USD | 0.00 USD | `+7.04%` | `348,000,000.00` |
| `Live` | `Short` | `804.50` | 417,990.00 USD | 1,080.00 USD | 0.00 USD | `+7.30%` | `1,338,000,000.00` |
| `Live` | `Short` | `806.50` | 462,200.00 USD | 44,210.00 USD | 0.00 USD | `+7.57%` | `54,814,000,000.00` |
| `Live` | `Short` | `811.50` | 462,470.00 USD | 265.36 USD | 0.00 USD | `+8.24%` | `327,000,000.00` |
| `Live` | `Short` | `818.50` | 462,670.00 USD | 205.44 USD | 0.00 USD | `+9.17%` | `251,000,000.00` |
| `Live` | `Short` | `821.50` | 474,520.00 USD | 11,840.00 USD | 0.00 USD | `+9.57%` | `14,418,000,000.00` |
| `Live` | `Short` | `823.50` | 476,250.00 USD | 1,730.00 USD | 0.00 USD | `+9.84%` | `2,102,000,000.00` |
| `Live` | `Short` | `824.50` | 486,200.00 USD | 9,950.00 USD | 0.00 USD | `+9.97%` | `12,072,000,000.00` |
| `Live` | `Short` | `834.50` | 487,210.00 USD | 1,010.00 USD | 0.00 USD | `+11.31%` | `1,206,000,000.00` |
| `Live` | `Short` | `835.50` | 487,550.00 USD | 340.88 USD | 0.00 USD | `+11.44%` | `408,000,000.00` |
| `Live` | `Short` | `836.50` | 488,170.00 USD | 625.70 USD | 0.00 USD | `+11.57%` | `748,000,000.00` |
| `Live` | `Short` | `837.50` | 488,300.00 USD | 125.62 USD | 0.00 USD | `+11.71%` | `150,000,000.00` |
| `Live` | `Short` | `839.50` | 488,870.00 USD | 572.54 USD | 0.00 USD | `+11.97%` | `682,000,000.00` |
| `Live` | `Short` | `841.50` | 491,550.00 USD | 2,680.00 USD | 0.00 USD | `+12.24%` | `3,182,000,000.00` |
| `Live` | `Short` | `842.50` | 491,870.00 USD | 324.36 USD | 0.00 USD | `+12.37%` | `385,000,000.00` |
| `Live` | `Short` | `843.50` | 665,000.00 USD | 173,130.00 USD | 0.00 USD | `+12.51%` | `205,251,000,000.00` |
| `Live` | `Short` | `845.50` | 1,000,000.00 USD | 338,650.00 USD | 0.00 USD | `+12.77%` | `400,529,000,000.00` |
| `Live` | `Short` | `848.50` | 1,000,000.00 USD | 289.34 USD | 0.00 USD | `+13.17%` | `341,000,000.00` |
| `Live` | `Short` | `849.50` | 1,000,000.00 USD | 416.25 USD | 0.00 USD | `+13.31%` | `490,000,000.00` |
| `Live` | `Short` | `851.50` | 1,000,000.00 USD | 108.99 USD | 0.00 USD | `+13.57%` | `128,000,000.00` |
| `Live` | `Short` | `854.50` | 1,000,000.00 USD | 138.43 USD | 0.00 USD | `+13.97%` | `162,000,000.00` |
| `Live` | `Short` | `855.50` | 1,000,000.00 USD | 171.10 USD | 0.00 USD | `+14.11%` | `200,000,000.00` |
| `Live` | `Short` | `859.50` | 1,010,000.00 USD | 265.59 USD | 0.00 USD | `+14.64%` | `309,000,000.00` |
| `Live` | `Short` | `864.50` | 1,010,000.00 USD | 6,240.00 USD | 0.00 USD | `+15.31%` | `7,220,000,000.00` |
| `Live` | `Short` | `866.50` | 1,010,000.00 USD | 552.83 USD | 0.00 USD | `+15.57%` | `638,000,000.00` |
| `Live` | `Short` | `868.50` | 1,010,000.00 USD | 1,530.00 USD | 0.00 USD | `+15.84%` | `1,765,000,000.00` |
| `Live` | `Short` | `869.50` | 1,470,000.00 USD | 452,190.00 USD | 0.00 USD | `+15.97%` | `520,062,000,000.00` |
| `Live` | `Short` | `873.50` | 1,470,000.00 USD | 908.44 USD | 0.00 USD | `+16.51%` | `1,040,000,000.00` |
| `Live` | `Short` | `878.50` | 1,480,000.00 USD | 11,910.00 USD | 0.00 USD | `+17.17%` | `13,555,000,000.00` |
| `Live` | `Short` | `879.50` | 1,480,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.31%` | `5,165,000,000.00` |
| `Live` | `Short` | `880.50` | 1,480,000.00 USD | 630.44 USD | 0.00 USD | `+17.44%` | `716,000,000.00` |
| `Live` | `Short` | `883.50` | 1,580,000.00 USD | 97,180.00 USD | 0.00 USD | `+17.84%` | `109,998,000,000.00` |
| `Live` | `Short` | `885.50` | 1,580,000.00 USD | 2,120.00 USD | 0.00 USD | `+18.11%` | `2,395,000,000.00` |
| `Live` | `Short` | `886.50` | 1,580,000.00 USD | 812.92 USD | 0.00 USD | `+18.24%` | `917,000,000.00` |
| `Live` | `Short` | `889.50` | 1,580,000.00 USD | 772.09 USD | 0.00 USD | `+18.64%` | `868,000,000.00` |
| `Live` | `Short` | `892.50` | 1,590,000.00 USD | 3,350.00 USD | 0.00 USD | `+19.04%` | `3,752,000,000.00` |
| `Live` | `Short` | `894.50` | 1,590,000.00 USD | 381.06 USD | 0.00 USD | `+19.31%` | `426,000,000.00` |
| `Live` | `Short` | `896.50` | 1,810,000.00 USD | 224,120.00 USD | 0.00 USD | `+19.57%` | `250,000,000,000.00` |
| `Live` | `Short` | `907.50` | 1,810,000.00 USD | 392.04 USD | 0.00 USD | `+21.04%` | `432,000,000.00` |
| `Live` | `Short` | `908.50` | 1,810,000.00 USD | 901.23 USD | 0.00 USD | `+21.18%` | `992,000,000.00` |
| `Live` | `Short` | `911.50` | 1,850,000.00 USD | 39,480.00 USD | 0.00 USD | `+21.58%` | `43,317,000,000.00` |
| `Live` | `Short` | `918.50` | 1,850,000.00 USD | 195.64 USD | 0.00 USD | `+22.51%` | `213,000,000.00` |
| `Live` | `Short` | `925.50` | 1,860,000.00 USD | 9,260.00 USD | 0.00 USD | `+23.44%` | `10,000,000,000.00` |
| `Live` | `Short` | `928.50` | 1,860,000.00 USD | 285.05 USD | 0.00 USD | `+23.84%` | `307,000,000.00` |
| `Live` | `Short` | `934.50` | 1,860,000.00 USD | 111.21 USD | 0.00 USD | `+24.64%` | `119,000,000.00` |
| `Live` | `Short` | `939.50` | 1,860,000.00 USD | 952.65 USD | 0.00 USD | `+25.31%` | `1,014,000,000.00` |
| `Live` | `Short` | `943.50` | 1,870,000.00 USD | 3,290.00 USD | 0.00 USD | `+25.84%` | `3,487,000,000.00` |
| `Live` | `Short` | `945.50` | 1,870,000.00 USD | 110.62 USD | 0.00 USD | `+26.11%` | `117,000,000.00` |
| `Live` | `Short` | `952.50` | 1,870,000.00 USD | 398.14 USD | 0.00 USD | `+27.04%` | `418,000,000.00` |
| `Live` | `Short` | `955.50` | 1,870,000.00 USD | 967.92 USD | 0.00 USD | `+27.44%` | `1,013,000,000.00` |
| `Live` | `Short` | `958.50` | 1,930,000.00 USD | 58,860.00 USD | 0.00 USD | `+27.84%` | `61,406,000,000.00` |
| `Live` | `Short` | `960.50` | 1,990,000.00 USD | 67,230.00 USD | 0.00 USD | `+28.11%` | `70,000,000,000.00` |
| `Live` | `Short` | `962.50` | 2,830,000.00 USD | 837,380.00 USD | 0.00 USD | `+28.38%` | `870,000,000,000.00` |
| `Live` | `Short` | `964.50` | 2,830,000.00 USD | 1,930.00 USD | 0.00 USD | `+28.64%` | `2,000,000,000.00` |
| `Live` | `Short` | `981.50` | 2,850,000.00 USD | 16,120.00 USD | 0.00 USD | `+30.91%` | `16,425,000,000.00` |
| `Live` | `Short` | `994.50` | 3,140,000.00 USD | 285,520.00 USD | 0.00 USD | `+32.65%` | `287,098,000,000.00` |
| `Live` | `Short` | `1000.50` | 3,830,000.00 USD | 697,960.00 USD | 0.00 USD | `+33.45%` | `697,611,000,000.00` |
| `Live` | `Short` | `1005.50` | 3,840,000.00 USD | 1,570.00 USD | 0.00 USD | `+34.11%` | `1,564,000,000.00` |
| `Live` | `Short` | `1017.50` | 3,870,000.00 USD | 36,680.00 USD | 0.00 USD | `+35.71%` | `36,051,000,000.00` |
| `Live` | `Short` | `1021.50` | 3,870,000.00 USD | 137.90 USD | 0.00 USD | `+36.25%` | `135,000,000.00` |
| `Live` | `Short` | `1039.50` | 3,980,000.00 USD | 104,630.00 USD | 0.00 USD | `+38.65%` | `100,651,000,000.00` |
| `Live` | `Short` | `1049.50` | 3,980,000.00 USD | 294.91 USD | 0.00 USD | `+39.98%` | `281,000,000.00` |
| `Live` | `Short` | `1050.50` | 3,980,000.00 USD | 500.04 USD | 0.00 USD | `+40.12%` | `476,000,000.00` |
| `Live` | `Short` | `1057.50` | 3,980,000.00 USD | 391.27 USD | 0.00 USD | `+41.05%` | `370,000,000.00` |
| `Live` | `Short` | `1064.50` | 3,980,000.00 USD | 1,600.00 USD | 0.00 USD | `+41.98%` | `1,500,000,000.00` |
| `Live` | `Short` | `1071.50` | 3,980,000.00 USD | 1,550.00 USD | 0.00 USD | `+42.92%` | `1,446,000,000.00` |
| `Live` | `Short` | `1073.50` | 3,980,000.00 USD | 1,610.00 USD | 0.00 USD | `+43.18%` | `1,500,000,000.00` |
| `Live` | `Short` | `1088.50` | 4,000,000.00 USD | 19,400.00 USD | 0.00 USD | `+45.18%` | `17,826,000,000.00` |
| `Live` | `Short` | `1094.50` | 4,000,000.00 USD | 189.35 USD | 0.00 USD | `+45.98%` | `173,000,000.00` |
| `Live` | `Short` | `1118.50` | 4,010,000.00 USD | 6,160.00 USD | 0.00 USD | `+49.19%` | `5,508,000,000.00` |
| `Live` | `Short` | `1140.50` | 4,010,000.00 USD | 152.83 USD | 0.00 USD | `+52.12%` | `134,000,000.00` |
| `Live` | `Short` | `1151.50` | 4,010,000.00 USD | 1,150.00 USD | 0.00 USD | `+53.59%` | `1,000,000,000.00` |
| `Live` | `Short` | `1159.50` | 4,070,000.00 USD | 56,020.00 USD | 0.00 USD | `+54.65%` | `48,311,000,000.00` |
| `Live` | `Short` | `1166.50` | 4,070,000.00 USD | 9,150.00 USD | 0.00 USD | `+55.59%` | `7,843,000,000.00` |
| `Live` | `Short` | `1169.50` | 4,080,000.00 USD | 367.22 USD | 0.00 USD | `+55.99%` | `314,000,000.00` |
| `Live` | `Short` | `1173.50` | 4,090,000.00 USD | 14,380.00 USD | 0.00 USD | `+56.52%` | `12,251,000,000.00` |
| `Live` | `Short` | `1181.50` | 4,090,000.00 USD | 158.32 USD | 0.00 USD | `+57.59%` | `134,000,000.00` |
| `Live` | `Short` | `1183.50` | 4,090,000.00 USD | 132.55 USD | 0.00 USD | `+57.85%` | `112,000,000.00` |
| `Live` | `Short` | `1197.50` | 4,090,000.00 USD | 463.43 USD | 0.00 USD | `+59.72%` | `387,000,000.00` |
| `Live` | `Short` | `1200.50` | 4,120,000.00 USD | 29,990.00 USD | 0.00 USD | `+60.12%` | `24,982,000,000.00` |
| `Live` | `Short` | `1207.50` | 4,120,000.00 USD | 385.19 USD | 0.00 USD | `+61.06%` | `319,000,000.00` |
| `Live` | `Short` | `1212.50` | 4,130,000.00 USD | 8,490.00 USD | 0.00 USD | `+61.72%` | `6,999,000,000.00` |
| `Live` | `Short` | `1225.50` | 4,130,000.00 USD | 1,030.00 USD | 0.00 USD | `+63.46%` | `841,000,000.00` |
| `Live` | `Short` | `1252.50` | 4,130,000.00 USD | 100.20 USD | 0.00 USD | `+67.06%` | `80,000,000.00` |
| `Live` | `Short` | `1254.50` | 4,130,000.00 USD | 339.97 USD | 0.00 USD | `+67.32%` | `271,000,000.00` |
| `Live` | `Short` | `1260.50` | 4,130,000.00 USD | 201.68 USD | 0.00 USD | `+68.12%` | `160,000,000.00` |
| `Live` | `Short` | `1264.50` | 4,880,000.00 USD | 752,040.00 USD | 0.00 USD | `+68.66%` | `594,730,000,000.00` |
| `Live` | `Short` | `1269.50` | 5,040,000.00 USD | 161,080.00 USD | 0.00 USD | `+69.33%` | `126,881,000,000.00` |
| `Live` | `Short` | `1286.50` | 5,160,000.00 USD | 115,780.00 USD | 0.00 USD | `+71.59%` | `90,000,000,000.00` |
| `Live` | `Short` | `1295.50` | 5,160,000.00 USD | 181.37 USD | 0.00 USD | `+72.79%` | `140,000,000.00` |
| `Live` | `Short` | `1303.50` | 5,180,000.00 USD | 19,550.00 USD | 0.00 USD | `+73.86%` | `15,000,000,000.00` |
| `Live` | `Short` | `1320.50` | 5,190,000.00 USD | 14,260.00 USD | 0.00 USD | `+76.13%` | `10,799,000,000.00` |
| `Live` | `Short` | `1323.50` | 5,200,000.00 USD | 8,610.00 USD | 0.00 USD | `+76.53%` | `6,508,000,000.00` |
| `Live` | `Short` | `1330.50` | 5,230,000.00 USD | 23,470.00 USD | 0.00 USD | `+77.46%` | `17,640,000,000.00` |
| `Live` | `Short` | `1333.50` | 5,230,000.00 USD | 102.68 USD | 0.00 USD | `+77.86%` | `77,000,000.00` |
| `Live` | `Short` | `1352.50` | 5,470,000.00 USD | 243,450.00 USD | 0.00 USD | `+80.40%` | `180,000,000,000.00` |
| `Live` | `Short` | `1375.50` | 5,470,000.00 USD | 158.18 USD | 0.00 USD | `+83.46%` | `115,000,000.00` |
| `Live` | `Short` | `1383.50` | 5,480,000.00 USD | 9,980.00 USD | 0.00 USD | `+84.53%` | `7,210,000,000.00` |
| `Live` | `Short` | `1402.50` | 5,480,000.00 USD | 178.12 USD | 0.00 USD | `+87.06%` | `127,000,000.00` |
| `Live` | `Short` | `1413.50` | 5,480,000.00 USD | 139.94 USD | 0.00 USD | `+88.53%` | `99,000,000.00` |
| `Live` | `Short` | `1424.50` | 5,490,000.00 USD | 5,690.00 USD | 0.00 USD | `+90.00%` | `3,994,000,000.00` |
| `Live` | `Short` | `1431.50` | 5,490,000.00 USD | 8,770.00 USD | 0.00 USD | `+90.93%` | `6,124,000,000.00` |
| `Live` | `Short` | `1432.50` | 5,490,000.00 USD | 360.99 USD | 0.00 USD | `+91.07%` | `252,000,000.00` |
| `Live` | `Short` | `1443.50` | 6,190,000.00 USD | 697,040.00 USD | 0.00 USD | `+92.53%` | `482,880,000,000.00` |
| `Live` | `Short` | `1470.50` | 6,210,000.00 USD | 14,460.00 USD | 0.00 USD | `+96.13%` | `9,836,000,000.00` |
| `Live` | `Short` | `1481.50` | 6,650,000.00 USD | 444,450.00 USD | 0.00 USD | `+97.60%` | `300,000,000,000.00` |
| `Live` | `Short` | `1487.50` | 9,310,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+98.40%` | `1,786,163,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `300.50` | 1,730,000.00 USD | 0.00 USD | 2,400.00 USD | `-59.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 1,720,000.00 USD | 0.00 USD | 333.50 USD | `-55.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `350.50` | 1,720,000.00 USD | 0.00 USD | 127.58 USD | `-53.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 1,720,000.00 USD | 0.00 USD | 5,170.00 USD | `-50.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 1,720,000.00 USD | 0.00 USD | 25,210.00 USD | `-45.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 1,690,000.00 USD | 0.00 USD | 4,550.00 USD | `-44.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 1,690,000.00 USD | 0.00 USD | 698.74 USD | `-39.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 1,690,000.00 USD | 0.00 USD | 3,550.00 USD | `-37.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 1,680,000.00 USD | 0.00 USD | 6,600.00 USD | `-34.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 1,680,000.00 USD | 0.00 USD | 214.78 USD | `-33.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 1,680,000.00 USD | 0.00 USD | 168.67 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 1,680,000.00 USD | 0.00 USD | 47,830.00 USD | `-32.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 1,630,000.00 USD | 0.00 USD | 185.97 USD | `-32.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 1,630,000.00 USD | 0.00 USD | 1,030.00 USD | `-31.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 1,630,000.00 USD | 0.00 USD | 125.51 USD | `-31.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 1,630,000.00 USD | 0.00 USD | 280.49 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 1,630,000.00 USD | 0.00 USD | 258.14 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 1,630,000.00 USD | 0.00 USD | 485.16 USD | `-29.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 1,630,000.00 USD | 0.00 USD | 4,650.00 USD | `-28.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 1,620,000.00 USD | 0.00 USD | 1,680.00 USD | `-28.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 1,620,000.00 USD | 0.00 USD | 864.80 USD | `-27.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 1,620,000.00 USD | 0.00 USD | 1,190.00 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 1,620,000.00 USD | 0.00 USD | 1,220.00 USD | `-25.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 1,620,000.00 USD | 0.00 USD | 297.12 USD | `-25.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 1,620,000.00 USD | 0.00 USD | 748.48 USD | `-25.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 1,620,000.00 USD | 0.00 USD | 566.50 USD | `-24.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 1,620,000.00 USD | 0.00 USD | 126.55 USD | `-24.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 1,620,000.00 USD | 0.00 USD | 5,680.00 USD | `-24.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 1,610,000.00 USD | 0.00 USD | 4,760.00 USD | `-23.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 1,610,000.00 USD | 0.00 USD | 1,700.00 USD | `-23.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 1,600,000.00 USD | 0.00 USD | 291.91 USD | `-23.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 1,600,000.00 USD | 0.00 USD | 469.61 USD | `-23.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 1,600,000.00 USD | 0.00 USD | 289.98 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 1,600,000.00 USD | 0.00 USD | 285.86 USD | `-22.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 1,600,000.00 USD | 0.00 USD | 289.17 USD | `-22.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 1,600,000.00 USD | 0.00 USD | 657.71 USD | `-22.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 1,600,000.00 USD | 0.00 USD | 289.59 USD | `-22.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 1,600,000.00 USD | 0.00 USD | 287.67 USD | `-22.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 1,600,000.00 USD | 0.00 USD | 288.74 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 1,600,000.00 USD | 0.00 USD | 1,090.00 USD | `-21.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 1,600,000.00 USD | 0.00 USD | 34,020.00 USD | `-21.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 1,570,000.00 USD | 0.00 USD | 289.05 USD | `-21.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 1,570,000.00 USD | 0.00 USD | 287.78 USD | `-21.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,570,000.00 USD | 0.00 USD | 7,990.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,560,000.00 USD | 0.00 USD | 540.31 USD | `-21.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 1,560,000.00 USD | 0.00 USD | 282.74 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,560,000.00 USD | 0.00 USD | 170.05 USD | `-20.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `594.50` | 1,560,000.00 USD | 0.00 USD | 286.55 USD | `-20.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,560,000.00 USD | 0.00 USD | 244.79 USD | `-20.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,560,000.00 USD | 0.00 USD | 3,760.00 USD | `-19.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,550,000.00 USD | 0.00 USD | 102.43 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,550,000.00 USD | 0.00 USD | 102.77 USD | `-19.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,550,000.00 USD | 0.00 USD | 2,610.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `606.50` | 1,550,000.00 USD | 0.00 USD | 103.11 USD | `-19.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,550,000.00 USD | 0.00 USD | 170.00 USD | `-18.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 1,550,000.00 USD | 0.00 USD | 1,380.00 USD | `-18.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,550,000.00 USD | 0.00 USD | 269.15 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,550,000.00 USD | 0.00 USD | 1,740.00 USD | `-17.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,550,000.00 USD | 0.00 USD | 120.83 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,550,000.00 USD | 0.00 USD | 105.49 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,550,000.00 USD | 0.00 USD | 170.76 USD | `-16.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,540,000.00 USD | 0.00 USD | 276.16 USD | `-15.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,540,000.00 USD | 0.00 USD | 4,570.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 1,540,000.00 USD | 0.00 USD | 2,550.00 USD | `-15.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,540,000.00 USD | 0.00 USD | 560.60 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,540,000.00 USD | 0.00 USD | 154.27 USD | `-13.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,540,000.00 USD | 0.00 USD | 971.04 USD | `-13.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,540,000.00 USD | 0.00 USD | 1,610.00 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,530,000.00 USD | 0.00 USD | 14,000.00 USD | `-13.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,520,000.00 USD | 0.00 USD | 2,090.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,520,000.00 USD | 0.00 USD | 2,020.00 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,520,000.00 USD | 0.00 USD | 308.92 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,520,000.00 USD | 0.00 USD | 129.33 USD | `-12.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,520,000.00 USD | 0.00 USD | 110.46 USD | `-12.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,520,000.00 USD | 0.00 USD | 17,600.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,500,000.00 USD | 0.00 USD | 198.15 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,500,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,500,000.00 USD | 0.00 USD | 4,920.00 USD | `-11.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,490,000.00 USD | 0.00 USD | 707.66 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,490,000.00 USD | 0.00 USD | 3,360.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 1,490,000.00 USD | 0.00 USD | 245.46 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 1,490,000.00 USD | 0.00 USD | 2,090.00 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 1,480,000.00 USD | 0.00 USD | 825.59 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 1,480,000.00 USD | 0.00 USD | 1,760.00 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 1,480,000.00 USD | 0.00 USD | 63,000.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 1,420,000.00 USD | 0.00 USD | 3,360.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 1,420,000.00 USD | 0.00 USD | 175.31 USD | `-9.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 1,420,000.00 USD | 0.00 USD | 2,370.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 1,410,000.00 USD | 0.00 USD | 31,240.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,380,000.00 USD | 0.00 USD | 24,240.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 1,360,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 1,360,000.00 USD | 0.00 USD | 7,610.00 USD | `-8.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 1,350,000.00 USD | 0.00 USD | 371.25 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 1,350,000.00 USD | 0.00 USD | 610.01 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 1,350,000.00 USD | 0.00 USD | 2,590.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 1,350,000.00 USD | 0.00 USD | 2,230.00 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 1,340,000.00 USD | 0.00 USD | 108.57 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 1,340,000.00 USD | 0.00 USD | 2,530.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 1,340,000.00 USD | 0.00 USD | 4,560.00 USD | `-7.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 1,340,000.00 USD | 0.00 USD | 374.34 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 1,340,000.00 USD | 0.00 USD | 30,340.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 1,300,000.00 USD | 0.00 USD | 9,690.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 1,300,000.00 USD | 0.00 USD | 4,340.00 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 1,290,000.00 USD | 0.00 USD | 5,000.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 1,290,000.00 USD | 0.00 USD | 3,300.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 1,280,000.00 USD | 0.00 USD | 199,470.00 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,080,000.00 USD | 0.00 USD | 3,900.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 1,080,000.00 USD | 0.00 USD | 1,790.00 USD | `-6.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 1,080,000.00 USD | 0.00 USD | 2,790.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 1,070,000.00 USD | 0.00 USD | 1,070.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 1,070,000.00 USD | 0.00 USD | 2,770.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 1,070,000.00 USD | 0.00 USD | 11,860.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 1,060,000.00 USD | 0.00 USD | 205.88 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 1,060,000.00 USD | 0.00 USD | 1,070.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 1,060,000.00 USD | 0.00 USD | 783.29 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 1,060,000.00 USD | 0.00 USD | 315.46 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 1,060,000.00 USD | 0.00 USD | 402.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 1,060,000.00 USD | 0.00 USD | 2,870.00 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 1,050,000.00 USD | 0.00 USD | 94,480.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 958,880.00 USD | 0.00 USD | 2,000.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 956,870.00 USD | 0.00 USD | 6,400.00 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 950,470.00 USD | 0.00 USD | 1,470.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `717.50` | 949,000.00 USD | 0.00 USD | 362.34 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `718.50` | 948,640.00 USD | 0.00 USD | 727.84 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `719.50` | 947,910.00 USD | 0.00 USD | 1,270.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `720.50` | 946,650.00 USD | 0.00 USD | 2,710.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `721.50` | 943,930.00 USD | 0.00 USD | 6,780.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `722.50` | 937,150.00 USD | 0.00 USD | 114.16 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `723.50` | 937,040.00 USD | 0.00 USD | 605.57 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `724.50` | 936,430.00 USD | 0.00 USD | 9,620.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.50` | 926,810.00 USD | 0.00 USD | 6,440.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `726.50` | 920,370.00 USD | 0.00 USD | 470.77 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `727.50` | 919,900.00 USD | 0.00 USD | 1,650.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `728.50` | 918,250.00 USD | 0.00 USD | 4,250.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `729.50` | 914,000.00 USD | 0.00 USD | 8,340.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `730.50` | 905,660.00 USD | 0.00 USD | 1,640.00 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `731.50` | 904,020.00 USD | 0.00 USD | 581,920.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `732.50` | 322,100.00 USD | 0.00 USD | 1,600.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `733.50` | 320,500.00 USD | 0.00 USD | 2,100.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `734.50` | 318,410.00 USD | 0.00 USD | 489.18 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `735.50` | 317,920.00 USD | 0.00 USD | 1,820.00 USD | `-1.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `736.50` | 316,100.00 USD | 0.00 USD | 5,760.00 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `737.50` | 310,340.00 USD | 0.00 USD | 4,950.00 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `738.50` | 305,390.00 USD | 0.00 USD | 3,000.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `739.50` | 302,390.00 USD | 0.00 USD | 2,460.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `740.50` | 299,930.00 USD | 0.00 USD | 1,590.00 USD | `-1.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `741.50` | 298,340.00 USD | 0.00 USD | 6,240.00 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `742.50` | 292,100.00 USD | 0.00 USD | 247,900.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `743.50` | 44,190.00 USD | 0.00 USD | 897.40 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `744.50` | 43,300.00 USD | 0.00 USD | 1,400.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `745.50` | 41,890.00 USD | 0.00 USD | 1,000.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `746.50` | 40,890.00 USD | 0.00 USD | 1,250.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `747.50` | 39,650.00 USD | 0.00 USD | 301.24 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `748.50` | 39,350.00 USD | 0.00 USD | 14,330.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `749.50` | 25,010.00 USD | 0.00 USD | 25,010.00 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,130.00 USD | 1,130.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 3,020.00 USD | 1,900.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 5,760.00 USD | 2,730.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 6,760.00 USD | 1,010.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 7,290.00 USD | 525.13 USD | 0.00 USD | `+0.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 7,400.00 USD | 107.28 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 15,640.00 USD | 8,250.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 17,520.00 USD | 1,880.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 24,020.00 USD | 6,500.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 24,280.00 USD | 253.67 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 24,790.00 USD | 511.82 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 27,710.00 USD | 2,920.00 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 30,320.00 USD | 2,610.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 242,070.00 USD | 211,750.00 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 248,460.00 USD | 6,390.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 327,310.00 USD | 78,840.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 327,640.00 USD | 331.13 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 329,000.00 USD | 1,360.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 330,230.00 USD | 1,230.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 330,730.00 USD | 504.02 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 562,120.00 USD | 231,390.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 563,490.00 USD | 1,370.00 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 573,160.00 USD | 9,670.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 574,410.00 USD | 1,240.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 584,090.00 USD | 9,680.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 586,170.00 USD | 2,080.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 599,900.00 USD | 13,730.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 604,000.00 USD | 4,100.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 609,480.00 USD | 5,470.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 615,890.00 USD | 6,420.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 617,730.00 USD | 1,840.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 633,610.00 USD | 15,870.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 636,810.00 USD | 3,200.00 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 1,040,000.00 USD | 407,870.00 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 1,040,000.00 USD | 106.69 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 1,050,000.00 USD | 292.21 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 1,050,000.00 USD | 366.51 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 1,050,000.00 USD | 393.75 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 1,050,000.00 USD | 133.26 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 1,050,000.00 USD | 1,150.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 1,050,000.00 USD | 704.44 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 1,050,000.00 USD | 4,160.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 1,050,000.00 USD | 1,450.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 1,060,000.00 USD | 3,730.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 1,060,000.00 USD | 3,040.00 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 1,060,000.00 USD | 154.52 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `797.50` | 1,060,000.00 USD | 2,120.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 1,070,000.00 USD | 2,590.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 1,100,000.00 USD | 36,970.00 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 1,100,000.00 USD | 803.50 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 1,100,000.00 USD | 179.63 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 1,110,000.00 USD | 3,860.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 1,110,000.00 USD | 3,190.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 1,110,000.00 USD | 868.59 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 1,130,000.00 USD | 15,790.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 1,130,000.00 USD | 374.10 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 1,130,000.00 USD | 6,080.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 1,130,000.00 USD | 109.82 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 1,140,000.00 USD | 3,210.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 1,140,000.00 USD | 2,610.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 1,140,000.00 USD | 162.68 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 1,150,000.00 USD | 7,000.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 1,150,000.00 USD | 408.13 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `825.50` | 1,480,000.00 USD | 330,200.00 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 1,480,000.00 USD | 672.77 USD | 0.00 USD | `+10.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 1,480,000.00 USD | 276.38 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 1,480,000.00 USD | 5,780.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 1,480,000.00 USD | 493.32 USD | 0.00 USD | `+10.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 1,490,000.00 USD | 3,270.00 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 1,490,000.00 USD | 187.15 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 1,490,000.00 USD | 372.24 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 1,490,000.00 USD | 326.62 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 1,490,000.00 USD | 296.34 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 1,490,000.00 USD | 441.26 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 1,490,000.00 USD | 329.87 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 1,490,000.00 USD | 425.97 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 1,500,000.00 USD | 7,860.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 1,500,000.00 USD | 1,150.00 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 1,510,000.00 USD | 11,650.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 1,510,000.00 USD | 102.30 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 1,510,000.00 USD | 137.57 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 1,520,000.00 USD | 13,180.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 1,520,000.00 USD | 551.58 USD | 0.00 USD | `+14.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 1,530,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 1,530,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 1,530,000.00 USD | 2,970.00 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 1,530,000.00 USD | 3,460.00 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 1,540,000.00 USD | 2,610.00 USD | 0.00 USD | `+15.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 1,540,000.00 USD | 228.07 USD | 0.00 USD | `+16.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 1,540,000.00 USD | 1,110.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `874.50` | 1,540,000.00 USD | 582.42 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 1,590,000.00 USD | 54,820.00 USD | 0.00 USD | `+17.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 1,590,000.00 USD | 266.55 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 1,590,000.00 USD | 690.14 USD | 0.00 USD | `+18.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 1,590,000.00 USD | 605.33 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 1,650,000.00 USD | 55,500.00 USD | 0.00 USD | `+20.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 1,650,000.00 USD | 4,150.00 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 1,650,000.00 USD | 533.99 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 1,650,000.00 USD | 166.43 USD | 0.00 USD | `+22.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 1,650,000.00 USD | 463.01 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 1,660,000.00 USD | 321.50 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `929.50` | 1,680,000.00 USD | 24,800.00 USD | 0.00 USD | `+23.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 1,680,000.00 USD | 552.72 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 1,680,000.00 USD | 196.03 USD | 0.00 USD | `+24.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 1,680,000.00 USD | 287.20 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 1,680,000.00 USD | 782.14 USD | 0.00 USD | `+27.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 1,680,000.00 USD | 498.94 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 1,680,000.00 USD | 1,930.00 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 1,680,000.00 USD | 293.25 USD | 0.00 USD | `+30.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 1,690,000.00 USD | 1,300.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 1,690,000.00 USD | 109.93 USD | 0.00 USD | `+30.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 1,690,000.00 USD | 439.09 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 1,690,000.00 USD | 2,590.00 USD | 0.00 USD | `+31.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 1,690,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 1,690,000.00 USD | 3,990.00 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 1,700,000.00 USD | 938.53 USD | 0.00 USD | `+33.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 1,710,000.00 USD | 12,810.00 USD | 0.00 USD | `+33.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 1,710,000.00 USD | 203.50 USD | 0.00 USD | `+35.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 1,710,000.00 USD | 195.51 USD | 0.00 USD | `+39.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 1,710,000.00 USD | 278.43 USD | 0.00 USD | `+46.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 1,710,000.00 USD | 555.75 USD | 0.00 USD | `+48.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 1,770,000.00 USD | 62,330.00 USD | 0.00 USD | `+60.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 1,770,000.00 USD | 1,250.00 USD | 0.00 USD | `+60.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1223.50` | 1,770,000.00 USD | 424.55 USD | 0.00 USD | `+63.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 1,770,000.00 USD | 235.49 USD | 0.00 USD | `+63.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 1,780,000.00 USD | 3,580.00 USD | 0.00 USD | `+64.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 1,780,000.00 USD | 421.42 USD | 0.00 USD | `+66.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 1,780,000.00 USD | 3,750.00 USD | 0.00 USD | `+70.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 1,780,000.00 USD | 133.64 USD | 0.00 USD | `+73.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 1,780,000.00 USD | 685.36 USD | 0.00 USD | `+73.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 1,810,000.00 USD | 24,400.00 USD | 0.00 USD | `+77.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 1,840,000.00 USD | 33,950.00 USD | 0.00 USD | `+78.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 1,850,000.00 USD | 6,210.00 USD | 0.00 USD | `+81.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 1,850,000.00 USD | 349.06 USD | 0.00 USD | `+81.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 1,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+82.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 1,870,000.00 USD | 19,210.00 USD | 0.00 USD | `+83.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 1,870,000.00 USD | 2,150.00 USD | 0.00 USD | `+86.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1499.50` | 1,870,000.00 USD | 635.79 USD | 0.00 USD | `+100.00%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `664.10` | 88,890,000.00 USD | 0.00 USD | 88,890,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `7D` | `665.00` | 88,750,000.00 USD | 0.00 USD | 88,750,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `7D` | `665.90` | 88,600,000.00 USD | 0.00 USD | 88,600,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `7D` | `666.80` | 88,200,000.00 USD | 0.00 USD | 88,200,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `7D` | `667.70` | 87,910,000.00 USD | 0.00 USD | 87,910,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `7D` | `668.60` | 87,610,000.00 USD | 0.00 USD | 87,610,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `7D` | `669.50` | 87,080,000.00 USD | 0.00 USD | 87,080,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `7D` | `670.40` | 86,590,000.00 USD | 0.00 USD | 86,590,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `7D` | `671.30` | 86,100,000.00 USD | 0.00 USD | 86,100,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `7D` | `672.20` | 85,670,000.00 USD | 0.00 USD | 85,670,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.90` | 33,500,000.00 USD | 0.00 USD | 33,500,000.00 USD | 213,810.00 USD | 35,830.00 USD | 43,940.00 USD |
| `7D` | `673.10` | 85,350,000.00 USD | 0.00 USD | 85,350,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.70` | 33,210,000.00 USD | 0.00 USD | 33,210,000.00 USD | 277,700.00 USD | 28,940.00 USD | 12,970.00 USD |
| `7D` | `674.00` | 84,850,000.00 USD | 0.00 USD | 84,850,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.50` | 32,890,000.00 USD | 0.00 USD | 32,890,000.00 USD | 153,120.00 USD | 41,110.00 USD | 43,780.00 USD |
| `7D` | `674.90` | 84,330,000.00 USD | 0.00 USD | 84,330,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.30` | 32,650,000.00 USD | 0.00 USD | 32,650,000.00 USD | 60,970.00 USD | 25,690.00 USD | 17,730.00 USD |
| `7D` | `675.80` | 84,000,000.00 USD | 0.00 USD | 84,000,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.10` | 32,550,000.00 USD | 0.00 USD | 32,550,000.00 USD | 133,460.00 USD | 40,110.00 USD | 51,140.00 USD |
| `7D` | `676.70` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `676.90` | 32,320,000.00 USD | 0.00 USD | 32,320,000.00 USD | 351,470.00 USD | 12,910.00 USD | 53,020.00 USD |
| `7D` | `677.60` | 82,840,000.00 USD | 0.00 USD | 82,840,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `677.70` | 31,900,000.00 USD | 0.00 USD | 31,900,000.00 USD | 259,280.00 USD | 18,700.00 USD | 50,220.00 USD |
| `1D` | `678.50` | 31,580,000.00 USD | 0.00 USD | 31,580,000.00 USD | 73,950.00 USD | 11,640.00 USD | 14,100.00 USD |
| `7D` | `678.50` | 82,370,000.00 USD | 0.00 USD | 82,370,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.30` | 31,480,000.00 USD | 0.00 USD | 31,480,000.00 USD | 108,790.00 USD | 7,970.00 USD | 7,840.00 USD |
| `7D` | `679.40` | 82,220,000.00 USD | 0.00 USD | 82,220,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `680.10` | 31,350,000.00 USD | 0.00 USD | 31,350,000.00 USD | 52,780.00 USD | 11,030.00 USD | 18,580.00 USD |
| `7D` | `680.30` | 82,050,000.00 USD | 0.00 USD | 82,050,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.90` | 31,270,000.00 USD | 0.00 USD | 31,270,000.00 USD | 65,540.00 USD | 5,770.00 USD | 5,710.00 USD |
| `7D` | `681.20` | 81,870,000.00 USD | 0.00 USD | 81,870,000.00 USD | 110,330.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.70` | 31,190,000.00 USD | 0.00 USD | 31,190,000.00 USD | 75,570.00 USD | 11,810.00 USD | 8,780.00 USD |
| `7D` | `682.10` | 81,720,000.00 USD | 0.00 USD | 81,720,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.50` | 31,100,000.00 USD | 0.00 USD | 31,100,000.00 USD | 30,930.00 USD | 12,580.00 USD | 39,510.00 USD |
| `7D` | `683.00` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 181,220.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.30` | 31,010,000.00 USD | 0.00 USD | 31,010,000.00 USD | 107,550.00 USD | 9,680.00 USD | 5,590.00 USD |
| `7D` | `683.90` | 81,450,000.00 USD | 0.00 USD | 81,450,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.10` | 30,890,000.00 USD | 0.00 USD | 30,890,000.00 USD | 18,530.00 USD | 12,720.00 USD | 2,140.00 USD |
| `7D` | `684.80` | 81,320,000.00 USD | 0.00 USD | 81,320,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `684.90` | 30,860,000.00 USD | 0.00 USD | 30,860,000.00 USD | 31,040.00 USD | 2,630.00 USD | 3,410.00 USD |
| `1D` | `685.70` | 30,820,000.00 USD | 0.00 USD | 30,820,000.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `685.70` | 81,030,000.00 USD | 0.00 USD | 81,030,000.00 USD | 199,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 80,830,000.00 USD | 0.00 USD | 80,830,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `687.50` | 80,760,000.00 USD | 0.00 USD | 80,760,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `688.40` | 80,620,000.00 USD | 0.00 USD | 80,620,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.90` | 30,800,000.00 USD | 0.00 USD | 30,800,000.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `689.30` | 80,550,000.00 USD | 0.00 USD | 80,550,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.70` | 30,790,000.00 USD | 0.00 USD | 30,790,000.00 USD | 23,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `690.20` | 80,460,000.00 USD | 0.00 USD | 80,460,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.50` | 30,770,000.00 USD | 0.00 USD | 30,770,000.00 USD | 74,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `691.10` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.30` | 30,700,000.00 USD | 0.00 USD | 30,700,000.00 USD | 33,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 79,530,000.00 USD | 0.00 USD | 79,530,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `1D` | `692.10` | 30,660,000.00 USD | 0.00 USD | 30,660,000.00 USD | 69,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `692.90` | 30,590,000.00 USD | 0.00 USD | 30,590,000.00 USD | 52,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.90` | 79,130,000.00 USD | 0.00 USD | 79,130,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.70` | 30,540,000.00 USD | 0.00 USD | 30,540,000.00 USD | 27,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `693.80` | 78,830,000.00 USD | 0.00 USD | 78,830,000.00 USD | 311,120.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.50` | 30,510,000.00 USD | 0.00 USD | 30,510,000.00 USD | 17,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `694.70` | 78,480,000.00 USD | 0.00 USD | 78,480,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.30` | 30,500,000.00 USD | 0.00 USD | 30,500,000.00 USD | 9,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `695.60` | 78,130,000.00 USD | 0.00 USD | 78,130,000.00 USD | 127,500.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `696.10` | 30,490,000.00 USD | 0.00 USD | 30,490,000.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `696.50` | 77,980,000.00 USD | 0.00 USD | 77,980,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `696.90` | 30,460,000.00 USD | 0.00 USD | 30,460,000.00 USD | 37,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 77,840,000.00 USD | 0.00 USD | 77,840,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `1D` | `697.70` | 30,420,000.00 USD | 0.00 USD | 30,420,000.00 USD | 62,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `698.30` | 77,630,000.00 USD | 0.00 USD | 77,630,000.00 USD | 277,440.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `698.50` | 30,360,000.00 USD | 0.00 USD | 30,360,000.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `699.20` | 77,260,000.00 USD | 0.00 USD | 77,260,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `1D` | `699.30` | 30,330,000.00 USD | 0.00 USD | 30,330,000.00 USD | 30,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `700.10` | 30,300,000.00 USD | 0.00 USD | 30,300,000.00 USD | 15,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `700.10` | 76,960,000.00 USD | 0.00 USD | 76,960,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.90` | 30,290,000.00 USD | 0.00 USD | 30,290,000.00 USD | 25,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 76,670,000.00 USD | 0.00 USD | 76,670,000.00 USD | 237,800.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `701.70` | 30,260,000.00 USD | 0.00 USD | 30,260,000.00 USD | 47,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 76,420,000.00 USD | 0.00 USD | 76,420,000.00 USD | 256,690.00 USD | 71,500.00 USD | 112,350.00 USD |
| `1D` | `702.50` | 30,220,000.00 USD | 0.00 USD | 30,220,000.00 USD | 72,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `702.80` | 75,970,000.00 USD | 0.00 USD | 75,970,000.00 USD | 416,820.00 USD | 74,570.00 USD | 36,720.00 USD |
| `1D` | `703.30` | 30,140,000.00 USD | 0.00 USD | 30,140,000.00 USD | 75,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 354,550.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `704.10` | 30,070,000.00 USD | 0.00 USD | 30,070,000.00 USD | 71,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `704.60` | 75,050,000.00 USD | 0.00 USD | 75,050,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `704.90` | 30,000,000.00 USD | 0.00 USD | 30,000,000.00 USD | 83,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.50` | 74,180,000.00 USD | 0.00 USD | 74,180,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `705.70` | 29,910,000.00 USD | 0.00 USD | 29,910,000.00 USD | 86,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `706.40` | 72,860,000.00 USD | 0.00 USD | 72,860,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `1D` | `706.50` | 29,830,000.00 USD | 0.00 USD | 29,830,000.00 USD | 40,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `707.30` | 29,790,000.00 USD | 0.00 USD | 29,790,000.00 USD | 37,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `707.30` | 72,000,000.00 USD | 0.00 USD | 72,000,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `708.10` | 29,750,000.00 USD | 0.00 USD | 29,750,000.00 USD | 16,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 71,250,000.00 USD | 0.00 USD | 71,250,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.90` | 29,730,000.00 USD | 0.00 USD | 29,730,000.00 USD | 39,580.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `709.10` | 70,270,000.00 USD | 0.00 USD | 70,270,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `1D` | `709.70` | 29,690,000.00 USD | 0.00 USD | 29,690,000.00 USD | 90,370.00 USD | 25,300.00 USD | 13,540.00 USD |
| `7D` | `710.00` | 69,530,000.00 USD | 0.00 USD | 69,530,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `1D` | `710.50` | 29,560,000.00 USD | 0.00 USD | 29,560,000.00 USD | 43,470.00 USD | 43,310.00 USD | 18,560.00 USD |
| `7D` | `710.90` | 68,740,000.00 USD | 0.00 USD | 68,740,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.30` | 29,450,000.00 USD | 0.00 USD | 29,450,000.00 USD | 102,220.00 USD | 57,170.00 USD | 9,890.00 USD |
| `7D` | `711.80` | 67,420,000.00 USD | 0.00 USD | 67,420,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `712.10` | 29,280,000.00 USD | 0.00 USD | 29,280,000.00 USD | 237,490.00 USD | 12,480.00 USD | 47,750.00 USD |
| `7D` | `712.70` | 66,460,000.00 USD | 0.00 USD | 66,460,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `1D` | `712.90` | 28,990,000.00 USD | 0.00 USD | 28,990,000.00 USD | 109,400.00 USD | 73,320.00 USD | 16,360.00 USD |
| `7D` | `713.60` | 64,820,000.00 USD | 0.00 USD | 64,820,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `1D` | `713.70` | 28,790,000.00 USD | 0.00 USD | 28,790,000.00 USD | 254,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `714.50` | 28,530,000.00 USD | 0.00 USD | 28,530,000.00 USD | 445,640.00 USD | 6,880.00 USD | 20,770.00 USD |
| `7D` | `714.50` | 61,970,000.00 USD | 0.00 USD | 61,970,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `715.30` | 28,060,000.00 USD | 0.00 USD | 28,060,000.00 USD | 21,790.00 USD | 16,080.00 USD | 3,740.00 USD |
| `7D` | `715.40` | 60,960,000.00 USD | 0.00 USD | 60,960,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `716.10` | 28,020,000.00 USD | 0.00 USD | 28,020,000.00 USD | 58,460.00 USD | 9,800.00 USD | 43,820.00 USD |
| `7D` | `716.30` | 59,160,000.00 USD | 0.00 USD | 59,160,000.00 USD | 1,320,000.00 USD | 385,020.00 USD | 311,890.00 USD |
| `1D` | `716.90` | 27,900,000.00 USD | 0.00 USD | 27,900,000.00 USD | 146,980.00 USD | 30,120.00 USD | 67,810.00 USD |
| `7D` | `717.20` | 57,140,000.00 USD | 0.00 USD | 57,140,000.00 USD | 581,610.00 USD | 408,260.00 USD | 371,410.00 USD |
| `1D` | `717.70` | 27,660,000.00 USD | 0.00 USD | 27,660,000.00 USD | 515,310.00 USD | 97,840.00 USD | 51,040.00 USD |
| `7D` | `718.10` | 55,780,000.00 USD | 0.00 USD | 55,780,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.50` | 26,990,000.00 USD | 0.00 USD | 26,990,000.00 USD | 753,870.00 USD | 77,200.00 USD | 122,910.00 USD |
| `7D` | `719.00` | 53,690,000.00 USD | 0.00 USD | 53,690,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.30` | 26,040,000.00 USD | 0.00 USD | 26,040,000.00 USD | 715,270.00 USD | 109,850.00 USD | 161,370.00 USD |
| `7D` | `719.90` | 52,670,000.00 USD | 0.00 USD | 52,670,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.10` | 25,050,000.00 USD | 0.00 USD | 25,050,000.00 USD | 360,270.00 USD | 107,240.00 USD | 63,710.00 USD |
| `7D` | `720.80` | 51,690,000.00 USD | 0.00 USD | 51,690,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `720.90` | 24,520,000.00 USD | 0.00 USD | 24,520,000.00 USD | 380,790.00 USD | 60,930.00 USD | 140,180.00 USD |
| `1D` | `721.70` | 23,940,000.00 USD | 0.00 USD | 23,940,000.00 USD | 876,410.00 USD | 103,330.00 USD | 167,740.00 USD |
| `7D` | `721.70` | 50,450,000.00 USD | 0.00 USD | 50,450,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.50` | 22,790,000.00 USD | 0.00 USD | 22,790,000.00 USD | 918,750.00 USD | 80,750.00 USD | 160,840.00 USD |
| `7D` | `722.60` | 47,610,000.00 USD | 0.00 USD | 47,610,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.30` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 659,110.00 USD | 17,430.00 USD | 73,670.00 USD |
| `7D` | `723.50` | 45,340,000.00 USD | 0.00 USD | 45,340,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `724.10` | 20,880,000.00 USD | 0.00 USD | 20,880,000.00 USD | 126,140.00 USD | 75,600.00 USD | 82,250.00 USD |
| `7D` | `724.40` | 44,270,000.00 USD | 0.00 USD | 44,270,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.90` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 342,160.00 USD | 62,890.00 USD | 13,340.00 USD |
| `7D` | `725.30` | 43,290,000.00 USD | 0.00 USD | 43,290,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.70` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 263,490.00 USD | 202,520.00 USD | 100,150.00 USD |
| `7D` | `726.20` | 40,710,000.00 USD | 0.00 USD | 40,710,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.50` | 19,610,000.00 USD | 0.00 USD | 19,610,000.00 USD | 504,710.00 USD | 56,970.00 USD | 60,710.00 USD |
| `7D` | `727.10` | 38,870,000.00 USD | 0.00 USD | 38,870,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.30` | 18,990,000.00 USD | 0.00 USD | 18,990,000.00 USD | 337,570.00 USD | 51,580.00 USD | 124,070.00 USD |
| `7D` | `728.00` | 37,070,000.00 USD | 0.00 USD | 37,070,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.10` | 18,480,000.00 USD | 0.00 USD | 18,480,000.00 USD | 395,990.00 USD | 195,850.00 USD | 106,840.00 USD |
| `1D` | `728.90` | 17,780,000.00 USD | 0.00 USD | 17,780,000.00 USD | 678,830.00 USD | 40,280.00 USD | 61,260.00 USD |
| `7D` | `728.90` | 32,790,000.00 USD | 0.00 USD | 32,790,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.70` | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 901,620.00 USD | 40,430.00 USD | 8,130.00 USD |
| `7D` | `729.80` | 29,500,000.00 USD | 0.00 USD | 29,500,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.50` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 156,880.00 USD | 70,850.00 USD | 41,670.00 USD |
| `7D` | `730.70` | 27,410,000.00 USD | 0.00 USD | 27,410,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.30` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 106,720.00 USD | 39,480.00 USD | 61,970.00 USD |
| `7D` | `731.60` | 23,710,000.00 USD | 0.00 USD | 23,710,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `732.10` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 307,460.00 USD | 43,990.00 USD | 148,520.00 USD |
| `7D` | `732.50` | 21,790,000.00 USD | 0.00 USD | 21,790,000.00 USD | 465,880.00 USD | 221,510.00 USD | 64,980.00 USD |
| `1D` | `732.90` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 2,160,000.00 USD | 232,510.00 USD | 252,700.00 USD |
| `7D` | `733.40` | 21,040,000.00 USD | 0.00 USD | 21,040,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.70` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 499,050.00 USD | 154,940.00 USD | 165,430.00 USD |
| `7D` | `734.30` | 18,630,000.00 USD | 0.00 USD | 18,630,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `734.50` | 11,600,000.00 USD | 0.00 USD | 11,600,000.00 USD | 1,370,000.00 USD | 229,660.00 USD | 269,820.00 USD |
| `7D` | `735.20` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.30` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 564,120.00 USD | 170,380.00 USD | 164,380.00 USD |
| `1D` | `736.10` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 788,290.00 USD | 248,020.00 USD | 342,500.00 USD |
| `7D` | `736.10` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.90` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 1,650,000.00 USD | 54,050.00 USD | 217,520.00 USD |
| `7D` | `737.00` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.70` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 2,270,000.00 USD | 184,910.00 USD | 410,490.00 USD |
| `7D` | `737.90` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.50` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 881,020.00 USD | 41,800.00 USD | 6,720.00 USD |
| `7D` | `738.80` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.30` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 463,560.00 USD | 0.00 USD | 78,820.00 USD |
| `7D` | `739.70` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.10` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 567,420.00 USD | 0.00 USD | 26,690.00 USD |
| `7D` | `740.60` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `740.90` | 595,380.00 USD | 0.00 USD | 595,380.00 USD | 230,130.00 USD | 0.00 USD | 7,010.00 USD |
| `7D` | `741.50` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `7D` | `742.40` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `743.30` | 358,230.00 USD | 0.00 USD | 358,230.00 USD | 0.00 USD | 43,530.00 USD | 113,120.00 USD |
| `7D` | `743.30` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `744.10` | 201,570.00 USD | 0.00 USD | 201,570.00 USD | 0.00 USD | 18,830.00 USD | 39,430.00 USD |
| `7D` | `744.20` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.90` | 143,310.00 USD | 0.00 USD | 143,310.00 USD | 0.00 USD | 29,640.00 USD | 16,260.00 USD |
| `7D` | `745.10` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `746.00` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.50` | 97,420.00 USD | 0.00 USD | 97,420.00 USD | 97,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.90` | 215,540.00 USD | 0.00 USD | 215,540.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `748.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `748.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `753.70` | 67,380.00 USD | 67,380.00 USD | 0.00 USD | 0.00 USD | 27,900.00 USD | 39,480.00 USD |
| `1D` | `754.50` | 103,670.00 USD | 103,670.00 USD | 0.00 USD | 0.00 USD | 36,290.00 USD | 0.00 USD |
| `7D` | `755.00` | 59,560.00 USD | 59,560.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.30` | 480,650.00 USD | 480,650.00 USD | 0.00 USD | 143,570.00 USD | 176,520.00 USD | 56,900.00 USD |
| `1D` | `756.10` | 867,000.00 USD | 867,000.00 USD | 0.00 USD | 312,560.00 USD | 27,340.00 USD | 46,440.00 USD |
| `7D` | `756.80` | 106,900.00 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `756.90` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 110,260.00 USD | 8,490.00 USD | 49,060.00 USD |
| `1D` | `757.70` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 249,860.00 USD | 146,640.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 695,650.00 USD | 695,650.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.50` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 311,230.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `758.60` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.30` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 813,190.00 USD | 13,760.00 USD | 20,870.00 USD |
| `1D` | `760.10` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 32,160.00 USD | 20,870.00 USD |
| `7D` | `760.40` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.90` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 113,590.00 USD | 25,800.00 USD | 74,240.00 USD |
| `7D` | `761.30` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 10,750.00 USD | 223,950.00 USD | 100,630.00 USD |
| `1D` | `761.70` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 264,780.00 USD | 54,040.00 USD | 135,620.00 USD |
| `7D` | `762.20` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 147,850.00 USD |
| `1D` | `762.50` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 212,650.00 USD | 170,950.00 USD | 74,890.00 USD |
| `7D` | `763.10` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.30` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 2,090,000.00 USD | 173,440.00 USD | 273,000.00 USD |
| `7D` | `764.00` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.10` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 1,530,000.00 USD | 200,630.00 USD | 269,540.00 USD |
| `1D` | `764.90` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 533,660.00 USD | 190,860.00 USD | 149,260.00 USD |
| `7D` | `764.90` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.70` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 898,410.00 USD | 136,000.00 USD | 207,520.00 USD |
| `7D` | `765.80` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.50` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 828,340.00 USD | 227,270.00 USD | 426,780.00 USD |
| `7D` | `766.70` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 3,340,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.30` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 2,090,000.00 USD | 126,130.00 USD | 214,710.00 USD |
| `7D` | `767.60` | 22,210,000.00 USD | 22,210,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `768.10` | 16,190,000.00 USD | 16,190,000.00 USD | 0.00 USD | 1,490,000.00 USD | 72,420.00 USD | 226,220.00 USD |
| `7D` | `768.50` | 24,430,000.00 USD | 24,430,000.00 USD | 0.00 USD | 1,850,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.90` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 680,980.00 USD | 67,110.00 USD | 97,310.00 USD |
| `7D` | `769.40` | 25,580,000.00 USD | 25,580,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.70` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 518,470.00 USD | 108,350.00 USD | 67,540.00 USD |
| `7D` | `770.30` | 28,090,000.00 USD | 28,090,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `770.50` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 458,460.00 USD | 137,750.00 USD | 43,590.00 USD |
| `7D` | `771.20` | 29,550,000.00 USD | 29,550,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `771.30` | 19,160,000.00 USD | 19,160,000.00 USD | 0.00 USD | 626,040.00 USD | 67,920.00 USD | 102,710.00 USD |
| `1D` | `772.10` | 19,670,000.00 USD | 19,670,000.00 USD | 0.00 USD | 333,140.00 USD | 86,890.00 USD | 89,650.00 USD |
| `7D` | `772.10` | 31,970,000.00 USD | 31,970,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.90` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 500,340.00 USD | 101,060.00 USD | 157,950.00 USD |
| `7D` | `773.00` | 34,590,000.00 USD | 34,590,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.70` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 556,120.00 USD | 126,820.00 USD | 140,880.00 USD |
| `7D` | `773.90` | 36,380,000.00 USD | 36,380,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.50` | 22,220,000.00 USD | 22,220,000.00 USD | 0.00 USD | 894,730.00 USD | 31,540.00 USD | 39,430.00 USD |
| `7D` | `774.80` | 38,760,000.00 USD | 38,760,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.30` | 22,580,000.00 USD | 22,580,000.00 USD | 0.00 USD | 211,980.00 USD | 106,740.00 USD | 42,280.00 USD |
| `7D` | `775.70` | 41,250,000.00 USD | 41,250,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.10` | 22,930,000.00 USD | 22,930,000.00 USD | 0.00 USD | 246,910.00 USD | 57,920.00 USD | 38,580.00 USD |
| `7D` | `776.60` | 43,530,000.00 USD | 43,530,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `776.90` | 23,380,000.00 USD | 23,380,000.00 USD | 0.00 USD | 356,670.00 USD | 22,000.00 USD | 74,260.00 USD |
| `7D` | `777.50` | 45,250,000.00 USD | 45,250,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 132,740.00 USD |
| `1D` | `777.70` | 24,470,000.00 USD | 24,470,000.00 USD | 0.00 USD | 880,680.00 USD | 88,980.00 USD | 126,350.00 USD |
| `7D` | `778.40` | 46,940,000.00 USD | 46,940,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `778.50` | 25,140,000.00 USD | 25,140,000.00 USD | 0.00 USD | 532,720.00 USD | 83,240.00 USD | 52,870.00 USD |
| `1D` | `779.30` | 26,090,000.00 USD | 26,090,000.00 USD | 0.00 USD | 698,730.00 USD | 101,050.00 USD | 149,650.00 USD |
| `7D` | `779.30` | 48,500,000.00 USD | 48,500,000.00 USD | 0.00 USD | 1,250,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `780.10` | 26,640,000.00 USD | 26,640,000.00 USD | 0.00 USD | 380,830.00 USD | 107,240.00 USD | 63,710.00 USD |
| `7D` | `780.20` | 49,880,000.00 USD | 49,880,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.90` | 27,250,000.00 USD | 27,250,000.00 USD | 0.00 USD | 406,710.00 USD | 60,930.00 USD | 140,180.00 USD |
| `7D` | `781.10` | 51,490,000.00 USD | 51,490,000.00 USD | 0.00 USD | 1,280,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.70` | 28,000,000.00 USD | 28,000,000.00 USD | 0.00 USD | 483,750.00 USD | 96,520.00 USD | 167,740.00 USD |
| `7D` | `782.00` | 53,390,000.00 USD | 53,390,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.50` | 29,250,000.00 USD | 29,250,000.00 USD | 0.00 USD | 1,050,000.00 USD | 66,420.00 USD | 127,920.00 USD |
| `7D` | `782.90` | 55,370,000.00 USD | 55,370,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.30` | 30,200,000.00 USD | 30,200,000.00 USD | 0.00 USD | 806,240.00 USD | 38,580.00 USD | 106,590.00 USD |
| `7D` | `783.80` | 55,950,000.00 USD | 55,950,000.00 USD | 0.00 USD | 510,940.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.10` | 30,530,000.00 USD | 30,530,000.00 USD | 0.00 USD | 282,620.00 USD | 29,330.00 USD | 18,280.00 USD |
| `7D` | `784.70` | 56,260,000.00 USD | 56,260,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `784.90` | 30,920,000.00 USD | 30,920,000.00 USD | 0.00 USD | 350,760.00 USD | 18,370.00 USD | 24,490.00 USD |
| `7D` | `785.60` | 57,390,000.00 USD | 57,390,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `785.70` | 31,240,000.00 USD | 31,240,000.00 USD | 0.00 USD | 227,750.00 USD | 49,690.00 USD | 35,280.00 USD |
| `1D` | `786.50` | 31,520,000.00 USD | 31,520,000.00 USD | 0.00 USD | 243,510.00 USD | 18,320.00 USD | 21,320.00 USD |
| `7D` | `786.50` | 57,780,000.00 USD | 57,780,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.30` | 31,710,000.00 USD | 31,710,000.00 USD | 0.00 USD | 144,290.00 USD | 21,200.00 USD | 24,380.00 USD |
| `7D` | `787.40` | 58,350,000.00 USD | 58,350,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `788.10` | 32,010,000.00 USD | 32,010,000.00 USD | 0.00 USD | 171,550.00 USD | 49,180.00 USD | 82,460.00 USD |
| `7D` | `788.30` | 58,720,000.00 USD | 58,720,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.90` | 32,500,000.00 USD | 32,500,000.00 USD | 0.00 USD | 376,940.00 USD | 46,900.00 USD | 61,930.00 USD |
| `7D` | `789.20` | 59,560,000.00 USD | 59,560,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.70` | 32,850,000.00 USD | 32,850,000.00 USD | 0.00 USD | 321,570.00 USD | 15,770.00 USD | 14,350.00 USD |
| `7D` | `790.10` | 60,050,000.00 USD | 60,050,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.50` | 33,040,000.00 USD | 33,040,000.00 USD | 0.00 USD | 143,460.00 USD | 40,430.00 USD | 8,130.00 USD |
| `7D` | `791.00` | 60,930,000.00 USD | 60,930,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.30` | 33,240,000.00 USD | 33,240,000.00 USD | 0.00 USD | 172,830.00 USD | 19,090.00 USD | 8,530.00 USD |
| `7D` | `791.90` | 61,800,000.00 USD | 61,800,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.10` | 33,350,000.00 USD | 33,350,000.00 USD | 0.00 USD | 105,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 62,020,000.00 USD | 62,020,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `792.90` | 33,370,000.00 USD | 33,370,000.00 USD | 0.00 USD | 26,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `793.70` | 33,400,000.00 USD | 33,400,000.00 USD | 0.00 USD | 26,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 62,210,000.00 USD | 62,210,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.50` | 33,440,000.00 USD | 33,440,000.00 USD | 0.00 USD | 35,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 62,530,000.00 USD | 62,530,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.30` | 33,460,000.00 USD | 33,460,000.00 USD | 0.00 USD | 22,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 62,670,000.00 USD | 62,670,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `796.10` | 33,500,000.00 USD | 33,500,000.00 USD | 0.00 USD | 38,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `796.40` | 62,810,000.00 USD | 62,810,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `796.90` | 33,540,000.00 USD | 33,540,000.00 USD | 0.00 USD | 40,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 62,870,000.00 USD | 62,870,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.70` | 33,600,000.00 USD | 33,600,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.50` | 33,630,000.00 USD | 33,630,000.00 USD | 0.00 USD | 31,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `799.10` | 63,070,000.00 USD | 63,070,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.30` | 33,650,000.00 USD | 33,650,000.00 USD | 0.00 USD | 22,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 63,180,000.00 USD | 63,180,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.10` | 33,660,000.00 USD | 33,660,000.00 USD | 0.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.90` | 33,670,000.00 USD | 33,670,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 63,290,000.00 USD | 63,290,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.70` | 33,710,000.00 USD | 33,710,000.00 USD | 0.00 USD | 41,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `801.80` | 63,500,000.00 USD | 63,500,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.50` | 33,740,000.00 USD | 33,740,000.00 USD | 0.00 USD | 23,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `802.70` | 63,510,000.00 USD | 63,510,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.30` | 33,750,000.00 USD | 33,750,000.00 USD | 0.00 USD | 16,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 63,580,000.00 USD | 63,580,000.00 USD | 0.00 USD | 63,540.00 USD | 5,560.00 USD | 5,650.00 USD |
| `1D` | `804.10` | 33,760,000.00 USD | 33,760,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 63,670,000.00 USD | 63,670,000.00 USD | 0.00 USD | 32,340.00 USD | 22,610.00 USD | 32,980.00 USD |
| `1D` | `804.90` | 33,760,000.00 USD | 33,760,000.00 USD | 0.00 USD | 7,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `805.40` | 63,740,000.00 USD | 63,740,000.00 USD | 0.00 USD | 59,610.00 USD | 12,940.00 USD | 0.00 USD |
| `1D` | `805.70` | 33,770,000.00 USD | 33,770,000.00 USD | 0.00 USD | 7,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `806.30` | 63,760,000.00 USD | 63,760,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `806.50` | 33,770,000.00 USD | 33,770,000.00 USD | 0.00 USD | 3,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `807.20` | 63,810,000.00 USD | 63,810,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `1D` | `807.30` | 33,790,000.00 USD | 33,790,000.00 USD | 0.00 USD | 17,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `808.10` | 33,800,000.00 USD | 33,800,000.00 USD | 0.00 USD | 9,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `808.10` | 63,870,000.00 USD | 63,870,000.00 USD | 0.00 USD | 19,950.00 USD | 5,360.00 USD | 29,800.00 USD |
| `1D` | `808.90` | 33,810,000.00 USD | 33,810,000.00 USD | 0.00 USD | 7,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.00` | 63,950,000.00 USD | 63,950,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `1D` | `809.70` | 33,810,000.00 USD | 33,810,000.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.90` | 64,170,000.00 USD | 64,170,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `1D` | `810.50` | 33,810,000.00 USD | 33,810,000.00 USD | 0.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `810.80` | 64,260,000.00 USD | 64,260,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 64,320,000.00 USD | 64,320,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `1D` | `812.10` | 33,820,000.00 USD | 33,820,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `812.60` | 64,440,000.00 USD | 64,440,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `1D` | `812.90` | 33,830,000.00 USD | 33,830,000.00 USD | 0.00 USD | 6,350.00 USD | 0.00 USD | 5,420.00 USD |
| `7D` | `813.50` | 64,700,000.00 USD | 64,700,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `1D` | `813.70` | 33,860,000.00 USD | 33,860,000.00 USD | 0.00 USD | 24,280.00 USD | 4,540.00 USD | 0.00 USD |
| `7D` | `814.40` | 65,020,000.00 USD | 65,020,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `1D` | `814.50` | 33,900,000.00 USD | 33,900,000.00 USD | 0.00 USD | 25,330.00 USD | 13,710.00 USD | 7,420.00 USD |
| `1D` | `815.30` | 33,940,000.00 USD | 33,940,000.00 USD | 0.00 USD | 8,420.00 USD | 11,670.00 USD | 13,240.00 USD |
| `7D` | `815.30` | 65,230,000.00 USD | 65,230,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `1D` | `816.10` | 33,960,000.00 USD | 33,960,000.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `816.20` | 65,530,000.00 USD | 65,530,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `1D` | `816.90` | 34,030,000.00 USD | 34,030,000.00 USD | 0.00 USD | 44,120.00 USD | 25,520.00 USD | 3,620.00 USD |
| `7D` | `817.10` | 65,930,000.00 USD | 65,930,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `1D` | `817.70` | 34,060,000.00 USD | 34,060,000.00 USD | 0.00 USD | 34,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `818.00` | 66,390,000.00 USD | 66,390,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `1D` | `818.50` | 34,230,000.00 USD | 34,230,000.00 USD | 0.00 USD | 159,290.00 USD | 2,750.00 USD | 8,310.00 USD |
| `7D` | `818.90` | 66,630,000.00 USD | 66,630,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `7D` | `819.80` | 67,140,000.00 USD | 67,140,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `1D` | `820.10` | 34,260,000.00 USD | 34,260,000.00 USD | 0.00 USD | 6,530.00 USD | 8,380.00 USD | 6,630.00 USD |
| `7D` | `820.70` | 67,440,000.00 USD | 67,440,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `1D` | `820.90` | 34,300,000.00 USD | 34,300,000.00 USD | 0.00 USD | 33,880.00 USD | 6,660.00 USD | 5,330.00 USD |
| `7D` | `821.60` | 67,640,000.00 USD | 67,640,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
| `1D` | `821.70` | 34,390,000.00 USD | 34,390,000.00 USD | 0.00 USD | 61,530.00 USD | 4,650.00 USD | 26,100.00 USD |
| `1D` | `822.50` | 34,580,000.00 USD | 34,580,000.00 USD | 0.00 USD | 144,890.00 USD | 24,530.00 USD | 17,840.00 USD |
| `7D` | `822.50` | 68,140,000.00 USD | 68,140,000.00 USD | 0.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `823.30` | 34,880,000.00 USD | 34,880,000.00 USD | 0.00 USD | 263,550.00 USD | 25,420.00 USD | 12,970.00 USD |
| `7D` | `823.40` | 68,470,000.00 USD | 68,470,000.00 USD | 0.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD |
| `1D` | `824.10` | 35,120,000.00 USD | 35,120,000.00 USD | 0.00 USD | 164,500.00 USD | 31,520.00 USD | 39,410.00 USD |
| `7D` | `824.30` | 68,820,000.00 USD | 68,820,000.00 USD | 0.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD |
| `1D` | `824.90` | 35,200,000.00 USD | 35,200,000.00 USD | 0.00 USD | 46,480.00 USD | 30,530.00 USD | 8,670.00 USD |
| `7D` | `825.20` | 69,180,000.00 USD | 69,180,000.00 USD | 0.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD |
| `1D` | `825.70` | 35,390,000.00 USD | 35,390,000.00 USD | 0.00 USD | 143,670.00 USD | 12,710.00 USD | 28,570.00 USD |
| `7D` | `826.10` | 69,490,000.00 USD | 69,490,000.00 USD | 0.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD |
| `1D` | `826.50` | 35,520,000.00 USD | 35,520,000.00 USD | 0.00 USD | 22,930.00 USD | 38,850.00 USD | 70,830.00 USD |
| `7D` | `827.00` | 70,130,000.00 USD | 70,130,000.00 USD | 0.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD |
| `1D` | `827.30` | 35,880,000.00 USD | 35,880,000.00 USD | 0.00 USD | 335,600.00 USD | 9,730.00 USD | 18,190.00 USD |
| `7D` | `827.90` | 70,490,000.00 USD | 70,490,000.00 USD | 0.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `828.10` | 36,180,000.00 USD | 36,180,000.00 USD | 0.00 USD | 224,680.00 USD | 18,700.00 USD | 50,220.00 USD |
| `7D` | `828.80` | 70,680,000.00 USD | 70,680,000.00 USD | 0.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD |
| `1D` | `828.90` | 36,300,000.00 USD | 36,300,000.00 USD | 0.00 USD | 107,140.00 USD | 8,360.00 USD | 8,130.00 USD |
| `1D` | `829.70` | 36,350,000.00 USD | 36,350,000.00 USD | 0.00 USD | 26,690.00 USD | 5,470.00 USD | 13,810.00 USD |
| `7D` | `829.70` | 70,770,000.00 USD | 70,770,000.00 USD | 0.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD |
| `1D` | `830.50` | 36,440,000.00 USD | 36,440,000.00 USD | 0.00 USD | 81,870.00 USD | 5,780.00 USD | 0.00 USD |
| `7D` | `830.60` | 71,020,000.00 USD | 71,020,000.00 USD | 0.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD |
| `1D` | `831.10` | 36,490,000.00 USD | 36,490,000.00 USD | 0.00 USD | 50,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `831.50` | 71,060,000.00 USD | 71,060,000.00 USD | 0.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.23B` | Total OI Tokens: `1,647,534.6 BNB`
  * 1h OI Change: `-0.27%` | 4h OI Change: `-1.10%` | 24h OI Change: `-1.81%`
  * Exchange Breakdown: Binance=`582.34M` | Bybit=`106.22M` | OKX=`54.69M` | Hyperliquid=`46.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `92.18K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0163%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0161%` | **USDT BingX** | `0.0161%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0004%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `48.60%` | `51.40%` | `0.95` | 22,430,000.00 USD |
| `15M` | `Binance` | `56.08%` | `43.92%` | `1.28` | 8,290,000.00 USD |
| `15M` | `OKX` | `62.7%` | `37.3%` | `1.68` | 2,040,000.00 USD |
| `15M` | `Bybit` | `55.69%` | `44.31%` | `1.26` | 2,230,000.00 USD |
| `15M` | `KuCoin` | `52.61%` | `47.39%` | `1.11` | 193,820.00 USD |
| `15M` | `Gate` | `45.15%` | `54.85%` | `0.82` | 1,130,000.00 USD |
| `15M` | `Bitget` | `52.16%` | `47.84%` | `1.09` | 1,120,000.00 USD |
| `15M` | `BingX` | `36.72%` | `63.28%` | `0.58` | 386,110.00 USD |
| `15M` | `MEXC` | `50.46%` | `49.54%` | `1.02` | 2,080,000.00 USD |
| `15M` | `Bitunix` | `54.9%` | `45.1%` | `1.22` | 1,720,000.00 USD |
| `15M` | `Hyperliquid` | `32.07%` | `67.93%` | `0.47` | 398,560.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.01%` | `64.99%` | `0.54` | 135,160.00 USD |
| `15M` | `Crypto.com` | `54.35%` | `45.65%` | `1.19` | 42,080.00 USD |
| `15M` | `WhiteBIT` | `1.8%` | `98.2%` | `0.02` | 1,960,000.00 USD |
| `15M` | `HTX` | `25.65%` | `74.35%` | `0.34` | 7,810.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.44%` | `33.56%` | `1.98` | 60,100.00 USD |
| `15M` | `Aster` | `17.23%` | `82.77%` | `0.21` | 604,520.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.56%` | `43.44%` | `1.30` | 34,190.00 USD |
| `15M` | `Whale Positions` | `56.08%` | `43.92%` | `1.28` | 8,290,000.00 USD |
| `15M` | `Global Accounts` | `48.60%` | `51.40%` | `0.95` | 22,430,000.00 USD |
| `1H` | `BNB` | `43.12%` | `56.88%` | `0.76` | 109,520,000.00 USD |
| `1H` | `Binance` | `47.23%` | `52.77%` | `0.90` | 34,220,000.00 USD |
| `1H` | `OKX` | `46.95%` | `53.05%` | `0.89` | 11,410,000.00 USD |
| `1H` | `Bybit` | `40.28%` | `59.72%` | `0.67` | 14,620,000.00 USD |
| `1H` | `KuCoin` | `41.07%` | `58.93%` | `0.70` | 935,780.00 USD |
| `1H` | `Gate` | `40.62%` | `59.38%` | `0.68` | 5,570,000.00 USD |
| `1H` | `Bitget` | `45.09%` | `54.91%` | `0.82` | 6,880,000.00 USD |
| `1H` | `BingX` | `44.32%` | `55.68%` | `0.80` | 1,770,000.00 USD |
| `1H` | `MEXC` | `47.8%` | `52.2%` | `0.92` | 16,630,000.00 USD |
| `1H` | `Bitunix` | `46.59%` | `53.41%` | `0.87` | 6,380,000.00 USD |
| `1H` | `Hyperliquid` | `27.05%` | `72.95%` | `0.37` | 1,630,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `32.15%` | `67.85%` | `0.47` | 446,210.00 USD |
| `1H` | `Crypto.com` | `53.4%` | `46.6%` | `1.15` | 187,800.00 USD |
| `1H` | `WhiteBIT` | `8.52%` | `91.48%` | `0.09` | 5,540,000.00 USD |
| `1H` | `HTX` | `26.64%` | `73.36%` | `0.36` | 44,710.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.73%` | `32.27%` | `2.10` | 1,040,000.00 USD |
| `1H` | `Aster` | `20.28%` | `79.72%` | `0.25` | 2,110,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `59.87%` | `40.13%` | `1.49` | 109,780.00 USD |
| `1H` | `Whale Positions` | `47.23%` | `52.77%` | `0.90` | 34,220,000.00 USD |
| `1H` | `Global Accounts` | `43.12%` | `56.88%` | `0.76` | 109,520,000.00 USD |
| `4H` | `BNB` | `48.54%` | `51.46%` | `0.94` | 602,330,000.00 USD |
| `4H` | `Binance` | `49.13%` | `50.87%` | `0.97` | 191,960,000.00 USD |
| `4H` | `OKX` | `49.28%` | `50.72%` | `0.97` | 63,530,000.00 USD |
| `4H` | `Bybit` | `48.68%` | `51.32%` | `0.95` | 80,750,000.00 USD |
| `4H` | `KuCoin` | `52.31%` | `47.69%` | `1.10` | 6,650,000.00 USD |
| `4H` | `Gate` | `47.78%` | `52.22%` | `0.91` | 26,120,000.00 USD |
| `4H` | `Bitget` | `47.71%` | `52.29%` | `0.91` | 52,610,000.00 USD |
| `4H` | `BingX` | `44.36%` | `55.64%` | `0.80` | 10,650,000.00 USD |
| `4H` | `MEXC` | `51.71%` | `48.29%` | `1.07` | 86,440,000.00 USD |
| `4H` | `Bitunix` | `48.81%` | `51.19%` | `0.95` | 33,190,000.00 USD |
| `4H` | `Hyperliquid` | `57%` | `43%` | `1.33` | 16,770,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.8%` | `51.2%` | `0.95` | 3,650,000.00 USD |
| `4H` | `Crypto.com` | `48.38%` | `51.62%` | `0.94` | 812,210.00 USD |
| `4H` | `WhiteBIT` | `17.08%` | `82.92%` | `0.21` | 17,930,000.00 USD |
| `4H` | `HTX` | `56.36%` | `43.64%` | `1.29` | 303,690.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.48%` | `37.52%` | `1.67` | 3,890,000.00 USD |
| `4H` | `Aster` | `47.45%` | `52.55%` | `0.90` | 6,380,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.46%` | `52.54%` | `0.90` | 731,630.00 USD |
| `4H` | `Whale Positions` | `49.13%` | `50.87%` | `0.97` | 191,960,000.00 USD |
| `4H` | `Global Accounts` | `48.54%` | `51.46%` | `0.94` | 602,330,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `751.95` | `752.04` | `751.95` | `753.45` | `751.05` | 8,568,644.80 USD | 2,835,818.57 USD | 5,732,826.23 USD | -2,897,007.66 USD | `-33.81%` | `0B / 2S` |
| `0:00 UTC` | `751.65` | `752.51` | `751.65` | `753.75` | `751.35` | 5,013,615.73 USD | 1,961,592.37 USD | 3,052,023.36 USD | -1,090,430.99 USD | `-21.75%` | `0B / 1S` |
| `5:00 UTC` | `750.15` | `751.21` | `750.15` | `752.85` | `749.85` | 4,943,475.52 USD | 2,128,944.58 USD | 2,814,530.94 USD | -685,586.36 USD | `-13.87%` | `0B / 1S` |
| `0:00 UTC` | `754.65` | `752.66` | `754.65` | `754.95` | `749.85` | 15,710,950.58 USD | 9,197,216.85 USD | 6,513,733.73 USD | 2,683,483.11 USD | `+17.08%` | `7B / 2S` |
| `5:00 UTC` | `751.65` | `751.09` | `751.65` | `752.55` | `749.55` | 6,229,452.23 USD | 2,822,969.55 USD | 3,406,482.69 USD | -583,513.14 USD | `-9.37%` | `1B / 3S` |
| `0:00 UTC` | `749.85` | `749.01` | `749.85` | `750.15` | `747.45` | 7,159,834.50 USD | 3,107,939.33 USD | 4,051,895.17 USD | -943,955.84 USD | `-13.18%` | `0B / 0S` |
| `5:00 UTC` | `750.45` | `750.48` | `750.45` | `751.05` | `749.85` | 4,170,354.29 USD | 2,126,593.29 USD | 2,043,761.00 USD | 82,832.29 USD | `+1.99%` | `0B / 0S` |
| `0:00 UTC` | `748.95` | `749.19` | `748.95` | `750.45` | `748.35` | 3,784,737.73 USD | 1,149,920.62 USD | 2,634,817.11 USD | -1,484,896.49 USD | `-39.23%` | `0B / 3S` |
| `5:00 UTC` | `748.65` | `748.42` | `748.65` | `748.95` | `747.75` | 3,504,446.48 USD | 1,566,200.72 USD | 1,938,245.76 USD | -372,045.05 USD | `-10.62%` | `0B / 1S` |
| `0:00 UTC` | `748.35` | `748.33` | `748.35` | `748.65` | `748.05` | 699,092.87 USD | 383,892.81 USD | 315,200.06 USD | 68,692.75 USD | `+9.83%` | `0B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:31` | `Volume 10K BNB` | `Divergence` | **`BULLISH`** | Drop without taker selling | `749.22` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 2` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `747.35` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 2` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `748.41` | 0.00 USD | 0.00 USD |
| `10-28 17:33` | `Range 2` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `760.29` | 1,300.00 USD | 0.00 USD |
| `10-28 16:24` | `Volume 10K BNB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `761.59` | 1,600.00 USD | 0.00 USD |
| `10-28 16:22` | `Range 2` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `761.59` | 0.00 USD | 0.00 USD |
| `10-28 16:00` | `Range 2` | `Divergence` | **`BEARISH`** | Rally without taker buying | `757.65` | 0.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 10K BNB` | `Trapped longs` | **`BEARISH`** | Failed breakout | `753.22` | 2,100.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 10K BNB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `749.29` | 1,800.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 10K BNB` | `Trapped longs` | **`BEARISH`** | Failed breakout | `749.29` | 1,800.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -106,100.00 USD | -605,650.00 USD | **`DISTRIBUTION`** |
| `15m` | -266,920.00 USD | -836,740.00 USD | **`DISTRIBUTION`** |
| `30m` | -578,780.00 USD | -3,610,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,190,000.00 USD | -5,040,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,820,000.00 USD | -5,420,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,320,000.00 USD | -1,540,000.00 USD | **`ACCUMULATION`** |
| `6h` | -5,140,000.00 USD | 7,250,000.00 USD | **`ACCUMULATION`** |
| `8h` | -14,510,000.00 USD | -10,670,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,290,000.00 USD | -25,060,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 6,300,000.00 USD | -22,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -26,550,000.00 USD | -44,460,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -122,030,000.00 USD | -366,490,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-106.10K` | 15m=`-266.92K` | 1h=`-1.19M` | 24h=`+6.30M`
* Futures Capital Netflows: 5m=`-605.65K` | 15m=`-836.74K` | 1h=`-5.04M` | 24h=`-22.79M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Execution Entry: `740.27` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `737.13` (Risk Distance: `3.14` pts)
  * +2.5R Take Profit: `748.12`
  * Mathematical Lot Sizing: **`3.18 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `752.43` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `755.57` (Risk Distance: `3.14` pts)
  * +2.5R Take Profit: `744.58`
  * Mathematical Lot Sizing: **`3.18 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`752.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
