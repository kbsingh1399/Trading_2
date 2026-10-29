# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:29:18 IST` (`2026-10-29 18:59:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `743.60` | **Live Ask Quote**: `744.20` | **Mid Price**: `743.90`
- **Spread Points**: `60.00` | **Spread BPS**: `8.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `746.88` | VWAP Z-Score: `-0.80` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.40` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `761.72` | Lower -3.00σ Band: `732.03`
  * Upper +2.51σ Band: `759.30` | Lower -2.51σ Band: `734.46`
  * Upper +2.01σ Band: `756.82` | Lower -2.01σ Band: `736.93`
  * Upper +2.00σ Band: `756.77` | Lower -2.00σ Band: `736.98`
  * Upper +1.28σ Band: `753.21` | Lower -1.28σ Band: `740.54`
  * Upper +1.00σ Band: `751.83` | Lower -1.00σ Band: `741.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`744.96` | EMA-20=`745.53` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`746.21` (Slope: `+0.0000`) | EMA-100=`747.23`
  * Institutional Anchors: EMA-144=`747.23` | EMA-200=`746.46` (Slope: `-0.0014`) | EMA-233=`745.69`
- **Range Boundaries**: 24H High=`759.80` | 24H Low=`737.00` | Weekly High=`760.90` | Weekly Low=`732.50`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `752.43` (Distance: `-1.14%`)
  * Point of Control (POC) = `750.76` (Distance: `-0.92%`)
  * Value Area Low (VAL) = `740.42` (Distance: `+0.46%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `740.92` - `746.88`
  * Optimal Trade Entry (OTE 0.705): `745.39`
  * Structural Invalidation Anchor (0.786): `749.85`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `744.05` | `744.54` | `743.59` | `744.47` | `984` | 732,328.55 USD | 197,874.53 USD | `+27.02%` | -15,226,975.20 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `744.47` | `744.75` | `743.80` | `744.13` | `912` | 679,052.54 USD | 11,753.92 USD | `+1.73%` | -15,215,221.29 USD | `+0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `744.13` | `745.26` | `744.13` | `745.25` | `790` | 588,520.35 USD | 269,292.91 USD | `+45.76%` | -14,945,928.37 USD | `+1.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `745.57` | `746.08` | `744.47` | `744.50` | `2,756` | 2,053,811.83 USD | -35,947.48 USD | `-1.75%` | -15,372,523.36 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `744.51` | `744.90` | `743.07` | `744.47` | `5,618` | 4,178,944.72 USD | 248,035.12 USD | `+5.94%` | -15,124,488.24 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `744.47` | `745.26` | `743.80` | `745.17` | `1,711` | 1,274,078.79 USD | 274,615.44 USD | `+21.55%` | -14,849,872.79 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `750.62` | `754.90` | `747.57` | `750.30` | `44,285` | 33,270,591.61 USD | 1,238,846.42 USD | `+3.72%` | -12,819,602.17 USD | `+0.55` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `750.30` | `750.31` | `745.00` | `746.40` | `20,621` | 15,418,790.29 USD | -2,662,387.27 USD | `-17.27%` | -15,481,989.44 USD | `-0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `746.40` | `746.83` | `743.07` | `745.17` | `13,215` | 9,841,539.23 USD | 632,116.65 USD | `+6.42%` | -14,849,872.79 USD | `+0.39` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -24,139,305.42 USD | `-1.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -16,093,806.98 USD | `+1.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.16` | `78,120` | 58,530,943.48 USD | -791,446.55 USD | `-1.35%` | -16,885,253.53 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `760.15` | `761.27` | `744.75` | `747.26` | `127,643` | 95,856,420.87 USD | -6,475,652.55 USD | `-6.76%` | -5,558,854.93 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -13,799,012.93 USD | `-0.92` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -24,139,305.42 USD | `-1.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -16,093,806.98 USD | `+1.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.16` | `78,120` | 58,530,943.48 USD | -791,446.55 USD | `-1.35%` | -16,885,253.53 USD | `+0.32` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`743.90`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `744.36` | `1175000000.0000` | 874.62 USD | 82,216.87 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `744.38` | `470000000.0000` | 349.86 USD | 81,342.25 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `744.41` | `38947000000.0000` | 28,992.54 USD | 80,992.39 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `744.42` | `1175000000.0000` | 874.69 USD | 51,999.85 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.44` | `2689000000.0000` | 2,001.80 USD | 51,125.16 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.45` | `627000000.0000` | 466.77 USD | 49,123.36 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.47` | `6716000000.0000` | 4,999.86 USD | 48,656.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.48` | `7272000000.0000` | 5,413.86 USD | 43,656.73 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.49` | `11666000000.0000` | 8,685.22 USD | 38,242.87 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `744.50` | `10169000000.0000` | 7,570.82 USD | 29,557.65 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `744.52` | `7858000000.0000` | 5,850.44 USD | 21,986.83 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `744.53` | `882000000.0000` | 656.68 USD | 16,136.39 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `744.54` | `1793000000.0000` | 1,334.96 USD | 15,479.72 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `744.57` | `4833000000.0000` | 3,598.51 USD | 14,144.76 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `744.61` | `8270000000.0000` | 6,157.92 USD | 10,546.25 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `744.63` | `2521000000.0000` | 1,877.21 USD | 4,388.33 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `744.65` | `657000000.0000` | 489.24 USD | 2,511.11 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `744.69` | `1177000000.0000` | 876.50 USD | 2,021.88 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `744.71` | `1076000000.0000` | 801.31 USD | 1,145.38 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `744.74` | `462000000.0000` | 344.07 USD | 344.07 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `744.75` | `660000000.0000` | 491.54 USD | 491.54 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `744.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 744.75` | `0.00%` | `-` |
| `ASK` | `744.76` | `36000000.0000` | 26.81 USD | 518.35 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `744.80` | `6837000000.0000` | 5,092.20 USD | 5,610.54 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `744.81` | `882000000.0000` | 656.92 USD | 6,267.47 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `744.83` | `112000000.0000` | 83.42 USD | 6,350.89 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `744.86` | `1000000000.0000` | 744.86 USD | 7,095.75 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `744.87` | `7404000000.0000` | 5,515.02 USD | 12,610.76 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `744.88` | `2422000000.0000` | 1,804.10 USD | 14,414.86 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `744.89` | `9092000000.0000` | 6,772.54 USD | 21,187.40 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `744.92` | `2684000000.0000` | 1,999.37 USD | 23,186.77 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `744.93` | `11726000000.0000` | 8,735.05 USD | 31,921.82 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `744.94` | `1162000000.0000` | 865.62 USD | 32,787.44 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `744.95` | `28000000.0000` | 20.86 USD | 32,808.30 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `744.96` | `1343000000.0000` | 1,000.48 USD | 33,808.78 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `744.97` | `11403000000.0000` | 8,494.89 USD | 42,303.67 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `744.99` | `229000000.0000` | 170.60 USD | 42,474.27 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `745.00` | `640000000.0000` | 476.80 USD | 42,951.07 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `745.01` | `10651000000.0000` | 7,935.10 USD | 50,886.18 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `745.02` | `1175000000.0000` | 875.40 USD | 51,761.57 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `745.03` | `14000000.0000` | 10.43 USD | 51,772.00 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `777` | `0xea00...a918` | `LONG` | 3,052,345.98 USD | `4,098,429,000,000.00` | `787.24` | `745.08` | `0.000000` | -174,080.80 USD | `-5.70%` | `5X Cross` |
| `1083` | `0xb69e...033a` | `LONG` | 2,089,159.72 USD | `2,805,710,000,000.00` | `772.94` | `745.08` | `563.01` | -79,482.86 USD | `-3.80%` | `10X Cross` |
| `1092` | `0xcac1...26b3` | `LONG` | 2,077,139.77 USD | `2,789,043,000,000.00` | `679.91` | `745.08` | `0.000000` | 180,828.61 USD | `+8.71%` | `10X Cross` |
| `1164` | `0x7737...bf66` | `SHORT` | 1,971,456.28 USD | `2,646,179,000,000.00` | `752.73` | `745.08` | `7128.99` | 20,414.31 USD | `+1.04%` | `10X Cross` |
| `1562` | `0xecb6...2b00` | `SHORT` | 1,429,885.06 USD | `1,919,180,000,000.00` | `738.35` | `745.08` | `13918.27` | -12,854.77 USD | `-0.90%` | `5X Cross` |
| `1643` | `0x27c9...d65d` | `SHORT` | 1,330,262.76 USD | `1,786,163,000,000.00` | `762.40` | `745.08` | `1583.87` | 31,504.59 USD | `+2.37%` | `10X Cross` |
| `1736` | `0x07fd...689d` | `LONG` | 1,239,922.62 USD | `1,664,862,000,000.00` | `716.02` | `745.08` | `0.000000` | 47,846.28 USD | `+3.86%` | `10X Cross` |
| `1755` | `0x645b...87b8` | `LONG` | 1,215,714.20 USD | `1,632,357,000,000.00` | `750.75` | `745.08` | `0.000000` | -9,771.96 USD | `-0.80%` | `10X Cross` |
| `2014` | `0xbcd4...0dd2` | `LONG` | 1,008,612.08 USD | `1,354,278,000,000.00` | `746.04` | `745.08` | `0.000000` | -1,731.98 USD | `-0.17%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `745.30` | 53,346.34 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 53.35K USD at 745.3000 USD [API] | `2026-10-27 22:32:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.31` (Vol: 2,400,000.00 USD, Dist: `+1.83%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--1.10%`)
  * 48H Horizon: Short MP=`758.54` (Vol: 2,400,000.00 USD, Dist: `+1.86%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--1.10%`)
  * 3D Horizon: Short MP=`766.52` (Vol: 2,500,000.00 USD, Dist: `+2.94%`) | Long MP=`736.48` (Vol: 3,000,000.00 USD, Dist: `--1.10%`)
  * 7D Horizon: Short MP=`758.15` (Vol: 2,900,000.00 USD, Dist: `+1.81%`) | Long MP=`728.45` (Vol: 3,700,000.00 USD, Dist: `--2.18%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `155.50` | 8,500.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `156.50` | 159.16 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 592.64 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `181.50` | 259.91 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 260.35 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `203.50` | 125.36 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 264.42 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `221.50` | 1,110.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `238.50` | 4,390.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `257.50` | 4,370.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `259.50` | 816.65 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `275.50` | 21,840.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `299.50` | 6,010.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `302.50` | 7,980.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `303.50` | 1,600.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `304.50` | 12,940.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `309.50` | 302.38 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 358.75 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 1,830.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `315.50` | 22,940.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `316.50` | 1,620.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `323.50` | 895.12 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 315.03 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 1,650.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 377.19 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `334.50` | 312.09 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `338.50` | 1,100.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `350.50` | 1,580.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `353.50` | 152.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `362.50` | 12,370.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 785.72 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 240.43 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `376.50` | 2,940.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 438.65 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 953.44 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 645.15 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 45,760.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 2,860.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 16,150.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 103.88 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 168.06 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 396.50 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 605.16 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `405.50` | 28,390.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `408.50` | 3,450.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 106.17 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 347.32 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 13,320.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 465.79 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 2,660.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `426.50` | 575.35 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `427.50` | 141.93 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 638.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `432.50` | 364.16 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `446.50` | 12,540.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `453.50` | 1,060.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `454.50` | 4,220.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `457.50` | 9,160.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.50` | 1,020.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 9,830.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `473.50` | 1,970.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `476.50` | 5,800.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 2,550.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 2,120.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,610.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 414.32 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 5,190.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 3,100.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,010.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 5,360.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 2,700.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 1,160.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 3,260.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 3,560.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 11,320.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 599.31 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,090.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 1,460.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 1,210.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 3,080.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `527.50` | 1,050.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 16,980.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 1,280.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 632.08 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 100.33 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `537.50` | 4,300.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 270.25 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 334.25 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 4,050.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,670.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 491.85 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 531.07 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,280.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,770.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 959.69 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,420.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 2,010.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 591.61 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 5,680.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `559.50` | 212.61 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 10,940.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 583.40 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `562.50` | 1,580,000.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `564.50` | 14,210.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 392.26 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 715,280.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 862.44 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 222.91 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 275.37 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 2,320.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 15,440.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 10,910.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,540.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 1,530.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 100.39 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 44,800.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 1,680.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 100.98 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,060.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 116.90 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 303.76 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 509.46 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 1,880.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `608.50` | 329.20 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 527.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 2,280.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 427.16 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,510.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 187.41 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 1,260.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 2,110.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `623.50` | 1,050.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 11,970.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 16,020.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 664.32 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `629.50` | 3,680.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `631.50` | 6,320.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `632.50` | 401.64 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `633.50` | 1,920.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 5,910.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 8,460.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `639.50` | 33,550.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 2,310.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 1,670.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 9,470.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `643.50` | 10,650.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.50` | 3,820.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `646.50` | 2,120.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `649.50` | 559.87 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `651.50` | 633.26 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `654.50` | 97,530.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `656.50` | 122.77 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `657.50` | 2,180.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `658.50` | 4,800.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,340.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `661.50` | 463.71 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `662.50` | 19,830.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `663.50` | 2,070.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 88,580,000.00 USD | 88,580,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 88,440,000.00 USD | 88,440,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 88,290,000.00 USD | 88,290,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 5,440.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 87,890,000.00 USD | 87,890,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.70` | 87,600,000.00 USD | 87,600,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.60` | 87,300,000.00 USD | 87,300,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.80` | 33,180,000.00 USD | 33,180,000.00 USD | 90,000.00 USD | 25,520.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 86,770,000.00 USD | 86,770,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 3,040.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.60` | 33,060,000.00 USD | 33,060,000.00 USD | 174,750.00 USD | 2,750.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `670.40` | 32,870,000.00 USD | 32,870,000.00 USD | 4,950.00 USD | 0.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 86,280,000.00 USD | 86,280,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 2,570.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.20` | 32,870,000.00 USD | 32,870,000.00 USD | 23,150.00 USD | 11,440.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 85,790,000.00 USD | 85,790,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 3,360.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.00` | 32,820,000.00 USD | 32,820,000.00 USD | 37,530.00 USD | 8,400.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 85,360,000.00 USD | 85,360,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 13,020.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.80` | 32,740,000.00 USD | 32,740,000.00 USD | 178,400.00 USD | 30,880.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 85,040,000.00 USD | 85,040,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 567.76 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.60` | 32,530,000.00 USD | 32,530,000.00 USD | 277,730.00 USD | 22,910.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 84,540,000.00 USD | 84,540,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.40` | 32,200,000.00 USD | 32,200,000.00 USD | 162,550.00 USD | 24,950.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 259.68 USD | 999,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 84,010,000.00 USD | 84,010,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.20` | 31,970,000.00 USD | 31,970,000.00 USD | 34,970.00 USD | 26,950.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.80` | 83,690,000.00 USD | 83,690,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.00` | 31,910,000.00 USD | 31,910,000.00 USD | 135,000.00 USD | 40,110.00 USD | 62,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 877.42 USD | 999,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.70` | 83,200,000.00 USD | 83,200,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.80` | 31,670,000.00 USD | 31,670,000.00 USD | 306,990.00 USD | 9,980.00 USD | 46,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.60` | 31,310,000.00 USD | 31,310,000.00 USD | 268,760.00 USD | 21,630.00 USD | 54,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 82,530,000.00 USD | 82,530,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.40` | 30,960,000.00 USD | 30,960,000.00 USD | 72,550.00 USD | 8,360.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 82,050,000.00 USD | 82,050,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 1,610.00 USD | 998,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.20` | 30,870,000.00 USD | 30,870,000.00 USD | 108,560.00 USD | 5,470.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 81,910,000.00 USD | 81,910,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.00` | 30,740,000.00 USD | 30,740,000.00 USD | 54,410.00 USD | 16,810.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 81,740,000.00 USD | 81,740,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.80` | 30,660,000.00 USD | 30,660,000.00 USD | 64,130.00 USD | 5,770.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 81,560,000.00 USD | 81,560,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 31,450.00 USD | 997,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.60` | 30,580,000.00 USD | 30,580,000.00 USD | 73,000.00 USD | 11,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 81,410,000.00 USD | 81,410,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.40` | 30,490,000.00 USD | 30,490,000.00 USD | 34,900.00 USD | 9,220.00 USD | 46,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 81,360,000.00 USD | 81,360,000.00 USD | 181,220.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.20` | 30,400,000.00 USD | 30,400,000.00 USD | 106,980.00 USD | 13,040.00 USD | 7,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 81,140,000.00 USD | 81,140,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.00` | 30,280,000.00 USD | 30,280,000.00 USD | 7,750.00 USD | 12,720.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `684.50` | 42,430.00 USD | 965,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `684.80` | 30,250,000.00 USD | 30,250,000.00 USD | 42,390.00 USD | 2,630.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 81,010,000.00 USD | 81,010,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `685.50` | 1,290.00 USD | 923,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `685.60` | 30,210,000.00 USD | 30,210,000.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 80,720,000.00 USD | 80,720,000.00 USD | 199,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `686.50` | 194.28 USD | 922,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `686.60` | 80,520,000.00 USD | 80,520,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 80,460,000.00 USD | 80,460,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `687.50` | 198.69 USD | 921,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `688.40` | 80,310,000.00 USD | 80,310,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.80` | 30,190,000.00 USD | 30,190,000.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 80,240,000.00 USD | 80,240,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `689.50` | 885.32 USD | 921,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `689.60` | 30,180,000.00 USD | 30,180,000.00 USD | 11,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 80,150,000.00 USD | 80,150,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.40` | 30,170,000.00 USD | 30,170,000.00 USD | 86,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `690.50` | 6,170.00 USD | 920,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `691.10` | 79,720,000.00 USD | 79,720,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.20` | 30,080,000.00 USD | 30,080,000.00 USD | 27,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `691.50` | 5,430.00 USD | 914,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `692.00` | 30,060,000.00 USD | 30,060,000.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 79,220,000.00 USD | 79,220,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `692.50` | 5,580.00 USD | 909,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `692.80` | 29,980,000.00 USD | 29,980,000.00 USD | 46,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 78,820,000.00 USD | 78,820,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `693.50` | 2,590.00 USD | 903,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `693.60` | 29,930,000.00 USD | 29,930,000.00 USD | 36,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 78,520,000.00 USD | 78,520,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.40` | 29,900,000.00 USD | 29,900,000.00 USD | 10,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `694.50` | 513.93 USD | 901,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `694.70` | 78,180,000.00 USD | 78,180,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.20` | 29,890,000.00 USD | 29,890,000.00 USD | 23,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `695.50` | 470.85 USD | 900,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `695.60` | 77,820,000.00 USD | 77,820,000.00 USD | 127,500.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.00` | 29,860,000.00 USD | 29,860,000.00 USD | 40,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 77,670,000.00 USD | 77,670,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.80` | 29,820,000.00 USD | 29,820,000.00 USD | 28,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 77,530,000.00 USD | 77,530,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `697.50` | 2,160.00 USD | 900,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `697.60` | 29,790,000.00 USD | 29,790,000.00 USD | 69,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 77,330,000.00 USD | 77,330,000.00 USD | 277,440.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.40` | 29,720,000.00 USD | 29,720,000.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `698.50` | 178.82 USD | 897,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `699.20` | 29,700,000.00 USD | 29,700,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 76,960,000.00 USD | 76,960,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `699.50` | 20,100.00 USD | 897,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `700.00` | 29,680,000.00 USD | 29,680,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 76,660,000.00 USD | 76,660,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `700.50` | 1,130.00 USD | 877,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `700.80` | 29,670,000.00 USD | 29,670,000.00 USD | 22,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 76,370,000.00 USD | 76,370,000.00 USD | 237,800.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.60` | 29,650,000.00 USD | 29,650,000.00 USD | 37,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 76,110,000.00 USD | 76,110,000.00 USD | 225,720.00 USD | 66,060.00 USD | 103,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.40` | 29,610,000.00 USD | 29,610,000.00 USD | 64,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `702.50` | 2,080.00 USD | 876,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `702.80` | 75,720,000.00 USD | 75,720,000.00 USD | 416,820.00 USD | 74,570.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.20` | 29,550,000.00 USD | 29,550,000.00 USD | 82,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `703.50` | 3,820.00 USD | 874,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `703.70` | 75,190,000.00 USD | 75,190,000.00 USD | 354,550.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.00` | 29,460,000.00 USD | 29,460,000.00 USD | 62,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `704.50` | 2,720.00 USD | 870,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `704.60` | 74,790,000.00 USD | 74,790,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.80` | 29,400,000.00 USD | 29,400,000.00 USD | 92,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 73,920,000.00 USD | 73,920,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `705.50` | 829.67 USD | 867,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `705.60` | 29,310,000.00 USD | 29,310,000.00 USD | 87,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `706.40` | 29,220,000.00 USD | 29,220,000.00 USD | 45,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 72,600,000.00 USD | 72,600,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `706.50` | 23,030.00 USD | 867,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `707.20` | 29,180,000.00 USD | 29,180,000.00 USD | 37,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 71,740,000.00 USD | 71,740,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `707.50` | 22,380.00 USD | 844,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `708.00` | 29,140,000.00 USD | 29,140,000.00 USD | 40,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 70,990,000.00 USD | 70,990,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `708.50` | 171,950.00 USD | 821,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `708.80` | 29,100,000.00 USD | 29,100,000.00 USD | 41,140.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 70,020,000.00 USD | 70,020,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `709.50` | 338,480.00 USD | 649,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `709.60` | 29,050,000.00 USD | 29,050,000.00 USD | 50,110.00 USD | 25,300.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 69,270,000.00 USD | 69,270,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `710.40` | 28,960,000.00 USD | 28,960,000.00 USD | 80,960.00 USD | 34,370.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `710.50` | 41,890.00 USD | 311,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.90` | 68,480,000.00 USD | 68,480,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.20` | 28,830,000.00 USD | 28,830,000.00 USD | 102,220.00 USD | 66,110.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `711.50` | 11,630.00 USD | 269,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `711.80` | 67,160,000.00 USD | 67,160,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.00` | 28,650,000.00 USD | 28,650,000.00 USD | 220,260.00 USD | 12,480.00 USD | 27,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `712.50` | 229,760.00 USD | 257,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `712.70` | 66,200,000.00 USD | 66,200,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.80` | 28,390,000.00 USD | 28,390,000.00 USD | 87,830.00 USD | 52,940.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `713.50` | 22,170.00 USD | 27,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `713.60` | 28,210,000.00 USD | 28,210,000.00 USD | 270,780.00 USD | 25,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `713.60` | 64,560,000.00 USD | 64,560,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `714.40` | 27,920,000.00 USD | 27,920,000.00 USD | 457,280.00 USD | 11,780.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 61,710,000.00 USD | 61,710,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `714.50` | 157.90 USD | 5,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `715.20` | 27,420,000.00 USD | 27,420,000.00 USD | 30,300.00 USD | 4,930.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 60,700,000.00 USD | 60,700,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `716.00` | 27,380,000.00 USD | 27,380,000.00 USD | 82,490.00 USD | 28,610.00 USD | 56,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 58,900,000.00 USD | 58,900,000.00 USD | 1,260,000.00 USD | 374,150.00 USD | 294,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `716.50` | 789.58 USD | 5,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `716.80` | 27,210,000.00 USD | 27,210,000.00 USD | 88,230.00 USD | 34,460.00 USD | 75,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 56,970,000.00 USD | 56,970,000.00 USD | 581,610.00 USD | 408,260.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `717.50` | 3,700.00 USD | 4,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `717.60` | 27,020,000.00 USD | 27,020,000.00 USD | 182,250.00 USD | 92,300.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 55,590,000.00 USD | 55,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `718.40` | 26,700,000.00 USD | 26,700,000.00 USD | 1,030,000.00 USD | 83,070.00 USD | 140,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `718.50` | 104.18 USD | 1,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `719.00` | 53,510,000.00 USD | 53,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `719.20` | 25,450,000.00 USD | 25,450,000.00 USD | 841,130.00 USD | 76,100.00 USD | 145,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 52,490,000.00 USD | 52,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `720.00` | 24,380,000.00 USD | 24,380,000.00 USD | 242,550.00 USD | 76,740.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `720.80` | 24,010,000.00 USD | 24,010,000.00 USD | 436,810.00 USD | 59,550.00 USD | 116,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 51,510,000.00 USD | 51,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `721.50` | 998.56 USD | 998.56 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `721.60` | 23,400,000.00 USD | 23,400,000.00 USD | 768,050.00 USD | 111,750.00 USD | 185,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `721.70` | 50,260,000.00 USD | 50,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `722.40` | 22,340,000.00 USD | 22,340,000.00 USD | 882,710.00 USD | 68,190.00 USD | 135,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `722.60` | 47,430,000.00 USD | 47,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `723.20` | 21,250,000.00 USD | 21,250,000.00 USD | 598,960.00 USD | 29,990.00 USD | 99,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 45,160,000.00 USD | 45,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `724.00` | 20,520,000.00 USD | 20,520,000.00 USD | 173,380.00 USD | 75,600.00 USD | 72,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 44,080,000.00 USD | 44,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `724.80` | 20,200,000.00 USD | 20,200,000.00 USD | 278,640.00 USD | 59,020.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 43,100,000.00 USD | 43,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `725.60` | 19,840,000.00 USD | 19,840,000.00 USD | 345,570.00 USD | 161,610.00 USD | 80,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 40,520,000.00 USD | 40,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `726.40` | 19,250,000.00 USD | 19,250,000.00 USD | 549,370.00 USD | 101,750.00 USD | 80,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 38,690,000.00 USD | 38,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `727.20` | 18,520,000.00 USD | 18,520,000.00 USD | 337,570.00 USD | 51,580.00 USD | 94,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `728.00` | 18,040,000.00 USD | 18,040,000.00 USD | 375,010.00 USD | 195,850.00 USD | 134,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 36,890,000.00 USD | 36,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `728.80` | 17,330,000.00 USD | 17,330,000.00 USD | 712,610.00 USD | 36,560.00 USD | 69,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 32,610,000.00 USD | 32,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `729.60` | 16,510,000.00 USD | 16,510,000.00 USD | 935,470.00 USD | 59,850.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `729.80` | 29,320,000.00 USD | 29,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `730.40` | 15,510,000.00 USD | 15,510,000.00 USD | 206,790.00 USD | 74,990.00 USD | 49,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `730.70` | 27,220,000.00 USD | 27,220,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `731.20` | 15,180,000.00 USD | 15,180,000.00 USD | 133,240.00 USD | 54,800.00 USD | 97,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `731.60` | 23,530,000.00 USD | 23,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `732.00` | 14,890,000.00 USD | 14,890,000.00 USD | 350,450.00 USD | 29,450.00 USD | 164,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 21,610,000.00 USD | 21,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `732.80` | 14,350,000.00 USD | 14,350,000.00 USD | 1,620,000.00 USD | 214,840.00 USD | 248,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 20,820,000.00 USD | 20,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `733.60` | 12,270,000.00 USD | 12,270,000.00 USD | 1,010,000.00 USD | 150,840.00 USD | 111,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 18,420,000.00 USD | 18,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `734.40` | 11,000,000.00 USD | 11,000,000.00 USD | 1,330,000.00 USD | 177,890.00 USD | 290,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `735.20` | 9,200,000.00 USD | 9,200,000.00 USD | 492,320.00 USD | 153,380.00 USD | 86,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 16,310,000.00 USD | 16,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `736.00` | 8,470,000.00 USD | 8,470,000.00 USD | 705,930.00 USD | 145,250.00 USD | 303,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 14,370,000.00 USD | 14,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `736.80` | 7,320,000.00 USD | 7,320,000.00 USD | 1,750,000.00 USD | 156,820.00 USD | 291,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 11,570,000.00 USD | 11,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `737.60` | 5,120,000.00 USD | 5,120,000.00 USD | 1,870,000.00 USD | 184,910.00 USD | 344,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 8,400,000.00 USD | 8,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `738.40` | 2,720,000.00 USD | 2,720,000.00 USD | 1,090,000.00 USD | 41,800.00 USD | 84,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 4,530,000.00 USD | 4,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `739.20` | 1,500,000.00 USD | 1,500,000.00 USD | 252,270.00 USD | 0.00 USD | 78,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `739.70` | 3,830,000.00 USD | 3,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `740.00` | 1,170,000.00 USD | 1,170,000.00 USD | 684,330.00 USD | 0.00 USD | 26,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `740.60` | 3,280,000.00 USD | 3,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `740.80` | 456,110.00 USD | 456,110.00 USD | 239,830.00 USD | 0.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 2,160,000.00 USD | 2,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `741.60` | 209,270.00 USD | 209,270.00 USD | 84,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `743.20` | 124,590.00 USD | 124,590.00 USD | 0.00 USD | 0.00 USD | 113,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `744.00` | 11,470.00 USD | 11,470.00 USD | 0.00 USD | 0.00 USD | 11,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `744.80` | 29,640.00 USD | 29,640.00 USD | 0.00 USD | 29,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.40` | 68,280.00 USD | 68,280.00 USD | 38,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 215,540.00 USD | 215,540.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.60` | 135,650.00 USD | 135,650.00 USD | 0.00 USD | 27,900.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.40` | 171,940.00 USD | 171,940.00 USD | 0.00 USD | 36,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 275,100.00 USD | 275,100.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.20` | 487,290.00 USD | 487,290.00 USD | 143,570.00 USD | 134,660.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.00` | 935,270.00 USD | 935,270.00 USD | 312,560.00 USD | 69,210.00 USD | 66,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.80` | 1,100,000.00 USD | 1,100,000.00 USD | 110,260.00 USD | 8,490.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 322,440.00 USD | 322,440.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.60` | 1,430,000.00 USD | 1,430,000.00 USD | 147,620.00 USD | 146,640.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 911,190.00 USD | 911,190.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.40` | 1,910,000.00 USD | 1,910,000.00 USD | 469,360.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 2,100,000.00 USD | 2,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.20` | 2,790,000.00 USD | 2,790,000.00 USD | 813,190.00 USD | 23,550.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.00` | 2,870,000.00 USD | 2,870,000.00 USD | 19,140.00 USD | 32,160.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.80` | 3,180,000.00 USD | 3,180,000.00 USD | 161,650.00 USD | 34,930.00 USD | 110,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 2,500,000.00 USD | 2,500,000.00 USD | 10,750.00 USD | 223,950.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 1,910.00 USD | 1,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.60` | 3,550,000.00 USD | 3,550,000.00 USD | 157,660.00 USD | 68,930.00 USD | 139,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.40` | 4,040,000.00 USD | 4,040,000.00 USD | 267,050.00 USD | 140,440.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 6,840,000.00 USD | 6,840,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.20` | 6,610,000.00 USD | 6,610,000.00 USD | 2,110,000.00 USD | 210,290.00 USD | 256,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 211.49 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.00` | 8,160,000.00 USD | 8,160,000.00 USD | 1,190,000.00 USD | 152,200.00 USD | 203,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 9,280,000.00 USD | 9,280,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.80` | 9,330,000.00 USD | 9,330,000.00 USD | 863,310.00 USD | 126,110.00 USD | 189,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 11,480,000.00 USD | 11,480,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.60` | 10,480,000.00 USD | 10,480,000.00 USD | 848,110.00 USD | 98,780.00 USD | 196,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 14,470,000.00 USD | 14,470,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.40` | 11,610,000.00 USD | 11,610,000.00 USD | 456,170.00 USD | 257,560.00 USD | 416,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.70` | 19,060,000.00 USD | 19,060,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.20` | 14,200,000.00 USD | 14,200,000.00 USD | 2,280,000.00 USD | 110,380.00 USD | 199,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 1,050.00 USD | 3,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `767.60` | 22,450,000.00 USD | 22,450,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.00` | 15,860,000.00 USD | 15,860,000.00 USD | 1,330,000.00 USD | 88,170.00 USD | 241,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 24,680,000.00 USD | 24,680,000.00 USD | 1,850,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 3,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.80` | 16,780,000.00 USD | 16,780,000.00 USD | 760,940.00 USD | 67,110.00 USD | 85,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 25,830,000.00 USD | 25,830,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.60` | 17,550,000.00 USD | 17,550,000.00 USD | 591,420.00 USD | 99,410.00 USD | 79,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 28,330,000.00 USD | 28,330,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.40` | 18,160,000.00 USD | 18,160,000.00 USD | 458,460.00 USD | 119,310.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.20` | 18,800,000.00 USD | 18,800,000.00 USD | 454,480.00 USD | 71,930.00 USD | 109,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 29,790,000.00 USD | 29,790,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.00` | 19,430,000.00 USD | 19,430,000.00 USD | 477,710.00 USD | 96,300.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 32,210,000.00 USD | 32,210,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.80` | 20,100,000.00 USD | 20,100,000.00 USD | 388,540.00 USD | 120,040.00 USD | 159,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 34,830,000.00 USD | 34,830,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,270.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.60` | 20,860,000.00 USD | 20,860,000.00 USD | 475,810.00 USD | 110,200.00 USD | 172,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.90` | 36,620,000.00 USD | 36,620,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.40` | 22,020,000.00 USD | 22,020,000.00 USD | 1,070,000.00 USD | 53,050.00 USD | 39,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 130.12 USD | 11,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,000,000.00 USD | 39,000,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.20` | 22,410,000.00 USD | 22,410,000.00 USD | 252,160.00 USD | 98,470.00 USD | 42,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 839.09 USD | 12,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `775.70` | 41,490,000.00 USD | 41,490,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.00` | 22,860,000.00 USD | 22,860,000.00 USD | 316,920.00 USD | 73,850.00 USD | 59,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 1,050.00 USD | 13,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 43,770,000.00 USD | 43,770,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.80` | 23,330,000.00 USD | 23,330,000.00 USD | 369,700.00 USD | 14,720.00 USD | 82,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 45,510,000.00 USD | 45,510,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 2,880.00 USD | 16,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `777.60` | 24,040,000.00 USD | 24,040,000.00 USD | 527,350.00 USD | 104,660.00 USD | 85,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `778.40` | 25,050,000.00 USD | 25,050,000.00 USD | 847,200.00 USD | 73,550.00 USD | 90,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 47,200,000.00 USD | 47,200,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 11,100.00 USD | 27,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.20` | 25,980,000.00 USD | 25,980,000.00 USD | 713,740.00 USD | 73,260.00 USD | 138,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 48,750,000.00 USD | 48,750,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.00` | 26,400,000.00 USD | 26,400,000.00 USD | 293,030.00 USD | 76,740.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 50,130,000.00 USD | 50,130,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 202.93 USD | 27,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.80` | 27,040,000.00 USD | 27,040,000.00 USD | 460,570.00 USD | 59,550.00 USD | 116,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 51,740,000.00 USD | 51,740,000.00 USD | 1,280,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 194.59 USD | 27,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.60` | 27,720,000.00 USD | 27,720,000.00 USD | 403,950.00 USD | 104,930.00 USD | 178,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 53,640,000.00 USD | 53,640,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.40` | 28,910,000.00 USD | 28,910,000.00 USD | 1,020,000.00 USD | 63,070.00 USD | 107,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 247,020.00 USD | 275,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 55,630,000.00 USD | 55,630,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.20` | 29,820,000.00 USD | 29,820,000.00 USD | 743,330.00 USD | 41,930.00 USD | 121,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `783.50` | 303.21 USD | 275,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `783.80` | 56,200,000.00 USD | 56,200,000.00 USD | 510,940.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.00` | 30,240,000.00 USD | 30,240,000.00 USD | 377,800.00 USD | 15,180.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 3,100.00 USD | 278,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.70` | 56,510,000.00 USD | 56,510,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.80` | 30,630,000.00 USD | 30,630,000.00 USD | 332,200.00 USD | 32,520.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 3,040.00 USD | 281,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `785.60` | 30,950,000.00 USD | 30,950,000.00 USD | 255,910.00 USD | 40,290.00 USD | 16,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 57,640,000.00 USD | 57,640,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.40` | 31,250,000.00 USD | 31,250,000.00 USD | 236,700.00 USD | 27,720.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 58,030,000.00 USD | 58,030,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,730.00 USD | 286,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.20` | 31,400,000.00 USD | 31,400,000.00 USD | 120,370.00 USD | 14,220.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 58,610,000.00 USD | 58,610,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 130,890.00 USD | 417,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.00` | 31,710,000.00 USD | 31,710,000.00 USD | 180,530.00 USD | 43,090.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 58,970,000.00 USD | 58,970,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 126.16 USD | 417,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.80` | 32,170,000.00 USD | 32,170,000.00 USD | 335,720.00 USD | 59,970.00 USD | 60,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 59,810,000.00 USD | 59,810,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 1,980.00 USD | 419,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.60` | 32,510,000.00 USD | 32,510,000.00 USD | 302,240.00 USD | 15,770.00 USD | 19,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 60,300,000.00 USD | 60,300,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.40` | 32,700,000.00 USD | 32,700,000.00 USD | 151,450.00 USD | 36,300.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 61,180,000.00 USD | 61,180,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.20` | 32,930,000.00 USD | 32,930,000.00 USD | 195,470.00 USD | 23,230.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `791.50` | 2,280.00 USD | 421,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `791.90` | 62,060,000.00 USD | 62,060,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.00` | 33,030,000.00 USD | 33,030,000.00 USD | 105,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.80` | 33,070,000.00 USD | 33,070,000.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 62,280,000.00 USD | 62,280,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 158.70 USD | 421,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `793.60` | 33,100,000.00 USD | 33,100,000.00 USD | 32,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `793.70` | 62,460,000.00 USD | 62,460,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.40` | 33,140,000.00 USD | 33,140,000.00 USD | 35,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 179.56 USD | 421,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 62,780,000.00 USD | 62,780,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.20` | 33,170,000.00 USD | 33,170,000.00 USD | 31,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 62,920,000.00 USD | 62,920,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 422,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.00` | 33,220,000.00 USD | 33,220,000.00 USD | 48,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 63,060,000.00 USD | 63,060,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 172.84 USD | 422,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.80` | 33,250,000.00 USD | 33,250,000.00 USD | 31,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `797.30` | 63,120,000.00 USD | 63,120,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `797.60` | 33,310,000.00 USD | 33,310,000.00 USD | 57,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `798.20` | 63,280,000.00 USD | 63,280,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `798.40` | 33,350,000.00 USD | 33,350,000.00 USD | 38,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 63,320,000.00 USD | 63,320,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `799.20` | 33,360,000.00 USD | 33,360,000.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `800.00` | 33,360,000.00 USD | 33,360,000.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 63,440,000.00 USD | 63,440,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `800.80` | 33,370,000.00 USD | 33,370,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 63,540,000.00 USD | 63,540,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 761.42 USD | 423,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `801.60` | 33,410,000.00 USD | 33,410,000.00 USD | 30,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `801.80` | 63,750,000.00 USD | 63,750,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.40` | 33,430,000.00 USD | 33,430,000.00 USD | 22,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 423,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 63,760,000.00 USD | 63,760,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.20` | 33,440,000.00 USD | 33,440,000.00 USD | 15,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `803.60` | 63,840,000.00 USD | 63,840,000.00 USD | 63,540.00 USD | 5,560.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `804.00` | 33,440,000.00 USD | 33,440,000.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 63,920,000.00 USD | 63,920,000.00 USD | 32,340.00 USD | 22,610.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 1,080.00 USD | 424,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `804.80` | 33,450,000.00 USD | 33,450,000.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,000,000.00 USD | 64,000,000.00 USD | 59,610.00 USD | 12,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `805.60` | 33,460,000.00 USD | 33,460,000.00 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,010,000.00 USD | 64,010,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `806.40` | 33,460,000.00 USD | 33,460,000.00 USD | 3,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 44,210.00 USD | 468,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `807.20` | 33,480,000.00 USD | 33,480,000.00 USD | 15,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,060,000.00 USD | 64,060,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.00` | 33,480,000.00 USD | 33,480,000.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `808.10` | 64,120,000.00 USD | 64,120,000.00 USD | 19,950.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.80` | 33,500,000.00 USD | 33,500,000.00 USD | 14,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.00` | 64,200,000.00 USD | 64,200,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `809.60` | 33,500,000.00 USD | 33,500,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.90` | 64,430,000.00 USD | 64,430,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `810.40` | 33,500,000.00 USD | 33,500,000.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `810.80` | 64,520,000.00 USD | 64,520,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `811.50` | 265.36 USD | 469,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `811.70` | 64,580,000.00 USD | 64,580,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 64,700,000.00 USD | 64,700,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `812.80` | 33,510,000.00 USD | 33,510,000.00 USD | 6,270.00 USD | 0.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 64,950,000.00 USD | 64,950,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `813.60` | 33,540,000.00 USD | 33,540,000.00 USD | 20,530.00 USD | 4,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.40` | 33,590,000.00 USD | 33,590,000.00 USD | 32,830.00 USD | 13,710.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 65,270,000.00 USD | 65,270,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.20` | 33,620,000.00 USD | 33,620,000.00 USD | 8,420.00 USD | 8,370.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `815.30` | 65,480,000.00 USD | 65,480,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.00` | 33,640,000.00 USD | 33,640,000.00 USD | 18,470.00 USD | 3,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 65,790,000.00 USD | 65,790,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.80` | 33,710,000.00 USD | 33,710,000.00 USD | 44,120.00 USD | 17,360.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `817.10` | 66,190,000.00 USD | 66,190,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `817.60` | 33,760,000.00 USD | 33,760,000.00 USD | 41,600.00 USD | 8,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.00` | 66,650,000.00 USD | 66,650,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `818.40` | 33,930,000.00 USD | 33,930,000.00 USD | 160,570.00 USD | 2,750.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 205.44 USD | 469,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 66,880,000.00 USD | 66,880,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 67,390,000.00 USD | 67,390,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.00` | 33,960,000.00 USD | 33,960,000.00 USD | 10,410.00 USD | 8,380.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `820.70` | 67,690,000.00 USD | 67,690,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.80` | 34,000,000.00 USD | 34,000,000.00 USD | 25,080.00 USD | 9,720.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,840.00 USD | 481,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `821.60` | 34,110,000.00 USD | 34,110,000.00 USD | 72,830.00 USD | 1,740.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `821.60` | 67,900,000.00 USD | 67,900,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `822.40` | 34,280,000.00 USD | 34,280,000.00 USD | 135,720.00 USD | 30,880.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 68,400,000.00 USD | 68,400,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `823.20` | 34,610,000.00 USD | 34,610,000.00 USD | 277,730.00 USD | 22,910.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 68,720,000.00 USD | 68,720,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 1,730.00 USD | 482,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `824.00` | 34,820,000.00 USD | 34,820,000.00 USD | 160,660.00 USD | 24,950.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,080,000.00 USD | 69,080,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `824.80` | 34,890,000.00 USD | 34,890,000.00 USD | 32,380.00 USD | 18,680.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 69,440,000.00 USD | 69,440,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `825.60` | 35,000,000.00 USD | 35,000,000.00 USD | 85,670.00 USD | 12,710.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 69,740,000.00 USD | 69,740,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `826.40` | 35,140,000.00 USD | 35,140,000.00 USD | 57,130.00 USD | 35,670.00 USD | 41,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `826.90` | 35,330,000.00 USD | 35,330,000.00 USD | 191,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.00` | 70,380,000.00 USD | 70,380,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 70,750,000.00 USD | 70,750,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `828.80` | 70,940,000.00 USD | 70,940,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,020,000.00 USD | 71,020,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 71,270,000.00 USD | 71,270,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 71,320,000.00 USD | 71,320,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `831.50` | 10,040.00 USD | 492,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 493,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `835.50` | 340.88 USD | 494,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 625.70 USD | 494,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 125.62 USD | 495,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 572.54 USD | 495,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,980.00 USD | 498,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 153.34 USD | 498,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 173,300.00 USD | 672,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 338,650.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `849.50` | 416.25 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 108.99 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 138.43 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 171.10 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 265.59 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 6,240.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `866.50` | 236.55 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `868.50` | 1,530.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `869.50` | 452,190.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 12,820.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 4,540.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,750.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `889.50` | 772.09 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `892.50` | 3,350.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,510.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 392.04 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 901.23 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 39,480.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `924.50` | 196.92 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 285.05 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `931.50` | 3,250.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 1,060.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `945.50` | 110.62 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `959.50` | 67,170.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 58,980.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `963.50` | 838,250.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `967.50` | 1,940.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `983.50` | 1,640.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 27,400.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 384,970.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 703,020.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1019.50` | 9,640.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1029.50` | 102,950.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 676.71 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1040.50` | 180.01 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1049.50` | 294.91 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 391.27 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1071.50` | 1,550.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1113.50` | 19,850.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1118.50` | 6,160.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1147.50` | 153.77 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1165.50` | 56,310.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 9,150.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1169.50` | 367.22 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1173.50` | 14,380.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1187.50` | 159.12 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1200.50` | 134.46 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1205.50` | 1,210.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 30,550.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1208.50` | 8,460.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1252.50` | 100.20 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1258.50` | 341.05 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1263.50` | 205.95 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1265.50` | 202.48 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1278.50` | 162,220.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1283.50` | 115,520.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1290.50` | 8,400.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1291.50` | 4,330.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1296.50` | 771,070.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,140.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1335.50` | 102.83 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1339.50` | 20,090.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1363.50` | 245,430.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1375.50` | 158.18 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1391.50` | 10,030.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1401.50` | 5,600.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1402.50` | 178.12 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1413.50` | 139.94 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1432.50` | 360.99 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1444.50` | 697,520.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1455.50` | 8,910.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1470.50` | 14,460.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `155.50` | 4,400,000.00 USD | 0.00 USD | 8,500.00 USD | `-79.15%` | `54,640,000,000.00` |
| `Live` | `Long` | `156.50` | 4,390,000.00 USD | 0.00 USD | 159.16 USD | `-79.02%` | `1,017,000,000.00` |
| `Live` | `Long` | `162.50` | 4,390,000.00 USD | 0.00 USD | 592.64 USD | `-78.22%` | `3,647,000,000.00` |
| `Live` | `Long` | `178.50` | 4,390,000.00 USD | 0.00 USD | 239.90 USD | `-76.07%` | `1,344,000,000.00` |
| `Live` | `Long` | `181.50` | 4,390,000.00 USD | 0.00 USD | 259.91 USD | `-75.67%` | `1,432,000,000.00` |
| `Live` | `Long` | `199.50` | 4,390,000.00 USD | 0.00 USD | 260.35 USD | `-73.26%` | `1,305,000,000.00` |
| `Live` | `Long` | `203.50` | 4,390,000.00 USD | 0.00 USD | 125.36 USD | `-72.72%` | `616,000,000.00` |
| `Live` | `Long` | `215.50` | 4,390,000.00 USD | 0.00 USD | 264.42 USD | `-71.11%` | `1,227,000,000.00` |
| `Live` | `Long` | `219.50` | 4,390,000.00 USD | 0.00 USD | 191.18 USD | `-70.58%` | `871,000,000.00` |
| `Live` | `Long` | `221.50` | 4,390,000.00 USD | 0.00 USD | 1,110.00 USD | `-70.31%` | `5,000,000,000.00` |
| `Live` | `Long` | `238.50` | 4,380,000.00 USD | 0.00 USD | 4,390.00 USD | `-68.03%` | `18,405,000,000.00` |
| `Live` | `Long` | `257.50` | 4,380,000.00 USD | 0.00 USD | 4,370.00 USD | `-65.48%` | `16,965,000,000.00` |
| `Live` | `Long` | `259.50` | 4,380,000.00 USD | 0.00 USD | 816.65 USD | `-65.21%` | `3,147,000,000.00` |
| `Live` | `Long` | `275.50` | 4,370,000.00 USD | 0.00 USD | 21,840.00 USD | `-63.07%` | `79,269,000,000.00` |
| `Live` | `Long` | `299.50` | 4,350,000.00 USD | 0.00 USD | 6,010.00 USD | `-59.85%` | `20,052,000,000.00` |
| `Live` | `Long` | `302.50` | 4,350,000.00 USD | 0.00 USD | 7,980.00 USD | `-59.45%` | `26,386,000,000.00` |
| `Live` | `Long` | `303.50` | 4,340,000.00 USD | 0.00 USD | 1,600.00 USD | `-59.32%` | `5,281,000,000.00` |
| `Live` | `Long` | `304.50` | 4,340,000.00 USD | 0.00 USD | 12,940.00 USD | `-59.18%` | `42,500,000,000.00` |
| `Live` | `Long` | `309.50` | 4,320,000.00 USD | 0.00 USD | 302.38 USD | `-58.51%` | `977,000,000.00` |
| `Live` | `Long` | `312.50` | 4,320,000.00 USD | 0.00 USD | 358.75 USD | `-58.11%` | `1,148,000,000.00` |
| `Live` | `Long` | `313.50` | 4,320,000.00 USD | 0.00 USD | 1,830.00 USD | `-57.97%` | `5,850,000,000.00` |
| `Live` | `Long` | `315.50` | 4,320,000.00 USD | 0.00 USD | 22,940.00 USD | `-57.71%` | `72,709,000,000.00` |
| `Live` | `Long` | `316.50` | 4,300,000.00 USD | 0.00 USD | 1,620.00 USD | `-57.57%` | `5,132,000,000.00` |
| `Live` | `Long` | `323.50` | 4,300,000.00 USD | 0.00 USD | 895.12 USD | `-56.63%` | `2,767,000,000.00` |
| `Live` | `Long` | `326.50` | 4,300,000.00 USD | 0.00 USD | 500.85 USD | `-56.23%` | `1,534,000,000.00` |
| `Live` | `Long` | `328.50` | 4,300,000.00 USD | 0.00 USD | 315.03 USD | `-55.96%` | `959,000,000.00` |
| `Live` | `Long` | `332.50` | 4,300,000.00 USD | 0.00 USD | 1,650.00 USD | `-55.43%` | `4,951,000,000.00` |
| `Live` | `Long` | `333.50` | 4,290,000.00 USD | 0.00 USD | 377.19 USD | `-55.29%` | `1,131,000,000.00` |
| `Live` | `Long` | `334.50` | 4,290,000.00 USD | 0.00 USD | 312.09 USD | `-55.16%` | `933,000,000.00` |
| `Live` | `Long` | `338.50` | 4,290,000.00 USD | 0.00 USD | 1,100.00 USD | `-54.62%` | `3,259,000,000.00` |
| `Live` | `Long` | `343.50` | 4,290,000.00 USD | 0.00 USD | 652.65 USD | `-53.95%` | `1,900,000,000.00` |
| `Live` | `Long` | `350.50` | 4,290,000.00 USD | 0.00 USD | 1,580.00 USD | `-53.01%` | `4,504,000,000.00` |
| `Live` | `Long` | `353.50` | 4,290,000.00 USD | 0.00 USD | 152.00 USD | `-52.61%` | `430,000,000.00` |
| `Live` | `Long` | `359.50` | 4,290,000.00 USD | 0.00 USD | 212.10 USD | `-51.81%` | `590,000,000.00` |
| `Live` | `Long` | `362.50` | 4,290,000.00 USD | 0.00 USD | 12,370.00 USD | `-51.41%` | `34,129,000,000.00` |
| `Live` | `Long` | `366.50` | 4,280,000.00 USD | 0.00 USD | 549.75 USD | `-50.87%` | `1,500,000,000.00` |
| `Live` | `Long` | `371.50` | 4,280,000.00 USD | 0.00 USD | 785.72 USD | `-50.20%` | `2,115,000,000.00` |
| `Live` | `Long` | `374.50` | 4,280,000.00 USD | 0.00 USD | 240.43 USD | `-49.80%` | `642,000,000.00` |
| `Live` | `Long` | `376.50` | 4,280,000.00 USD | 0.00 USD | 2,940.00 USD | `-49.53%` | `7,799,000,000.00` |
| `Live` | `Long` | `377.50` | 4,270,000.00 USD | 0.00 USD | 438.65 USD | `-49.40%` | `1,162,000,000.00` |
| `Live` | `Long` | `378.50` | 4,270,000.00 USD | 0.00 USD | 953.44 USD | `-49.26%` | `2,519,000,000.00` |
| `Live` | `Long` | `379.50` | 4,270,000.00 USD | 0.00 USD | 645.15 USD | `-49.13%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,270,000.00 USD | 0.00 USD | 45,760.00 USD | `-48.86%` | `119,940,000,000.00` |
| `Live` | `Long` | `382.50` | 4,220,000.00 USD | 0.00 USD | 1,910.00 USD | `-48.73%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 4,220,000.00 USD | 0.00 USD | 10,900.00 USD | `-48.59%` | `28,414,000,000.00` |
| `Live` | `Long` | `385.50` | 4,210,000.00 USD | 0.00 USD | 2,860.00 USD | `-48.32%` | `7,421,000,000.00` |
| `Live` | `Long` | `386.50` | 4,210,000.00 USD | 0.00 USD | 16,150.00 USD | `-48.19%` | `41,779,000,000.00` |
| `Live` | `Long` | `393.50` | 4,190,000.00 USD | 0.00 USD | 103.88 USD | `-47.25%` | `264,000,000.00` |
| `Live` | `Long` | `394.50` | 4,190,000.00 USD | 0.00 USD | 168.06 USD | `-47.12%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 4,190,000.00 USD | 0.00 USD | 2,110.00 USD | `-46.98%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 4,190,000.00 USD | 0.00 USD | 396.50 USD | `-46.85%` | `1,000,000,000.00` |
| `Live` | `Long` | `397.50` | 4,190,000.00 USD | 0.00 USD | 318.00 USD | `-46.71%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 4,190,000.00 USD | 0.00 USD | 523.63 USD | `-46.58%` | `1,314,000,000.00` |
| `Live` | `Long` | `400.50` | 4,190,000.00 USD | 0.00 USD | 605.16 USD | `-46.31%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 4,190,000.00 USD | 0.00 USD | 102.34 USD | `-45.78%` | `253,000,000.00` |
| `Live` | `Long` | `405.50` | 4,190,000.00 USD | 0.00 USD | 28,390.00 USD | `-45.64%` | `70,000,000,000.00` |
| `Live` | `Long` | `408.50` | 4,160,000.00 USD | 0.00 USD | 3,450.00 USD | `-45.24%` | `8,455,000,000.00` |
| `Live` | `Long` | `410.50` | 4,160,000.00 USD | 0.00 USD | 614.52 USD | `-44.97%` | `1,497,000,000.00` |
| `Live` | `Long` | `411.50` | 4,160,000.00 USD | 0.00 USD | 106.17 USD | `-44.84%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 4,160,000.00 USD | 0.00 USD | 347.32 USD | `-44.70%` | `842,000,000.00` |
| `Live` | `Long` | `414.50` | 4,160,000.00 USD | 0.00 USD | 13,320.00 USD | `-44.44%` | `32,128,000,000.00` |
| `Live` | `Long` | `415.50` | 4,140,000.00 USD | 0.00 USD | 1,810.00 USD | `-44.30%` | `4,368,000,000.00` |
| `Live` | `Long` | `417.50` | 4,140,000.00 USD | 0.00 USD | 7,140.00 USD | `-44.03%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 4,130,000.00 USD | 0.00 USD | 465.79 USD | `-43.90%` | `1,113,000,000.00` |
| `Live` | `Long` | `420.50` | 4,130,000.00 USD | 0.00 USD | 2,660.00 USD | `-43.63%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 4,130,000.00 USD | 0.00 USD | 2,320.00 USD | `-43.50%` | `5,496,000,000.00` |
| `Live` | `Long` | `423.50` | 4,130,000.00 USD | 0.00 USD | 1,450.00 USD | `-43.23%` | `3,419,000,000.00` |
| `Live` | `Long` | `426.50` | 4,130,000.00 USD | 0.00 USD | 575.35 USD | `-42.83%` | `1,349,000,000.00` |
| `Live` | `Long` | `427.50` | 4,130,000.00 USD | 0.00 USD | 141.93 USD | `-42.69%` | `332,000,000.00` |
| `Live` | `Long` | `430.50` | 4,130,000.00 USD | 0.00 USD | 638.00 USD | `-42.29%` | `1,482,000,000.00` |
| `Live` | `Long` | `432.50` | 4,130,000.00 USD | 0.00 USD | 364.16 USD | `-42.02%` | `842,000,000.00` |
| `Live` | `Long` | `438.50` | 4,120,000.00 USD | 0.00 USD | 1,790.00 USD | `-41.22%` | `4,087,000,000.00` |
| `Live` | `Long` | `446.50` | 4,120,000.00 USD | 0.00 USD | 12,540.00 USD | `-40.15%` | `28,093,000,000.00` |
| `Live` | `Long` | `453.50` | 4,110,000.00 USD | 0.00 USD | 1,060.00 USD | `-39.21%` | `2,339,000,000.00` |
| `Live` | `Long` | `454.50` | 4,110,000.00 USD | 0.00 USD | 4,220.00 USD | `-39.07%` | `9,287,000,000.00` |
| `Live` | `Long` | `456.50` | 4,110,000.00 USD | 0.00 USD | 4,730.00 USD | `-38.81%` | `10,359,000,000.00` |
| `Live` | `Long` | `457.50` | 4,100,000.00 USD | 0.00 USD | 9,160.00 USD | `-38.67%` | `20,013,000,000.00` |
| `Live` | `Long` | `465.50` | 4,090,000.00 USD | 0.00 USD | 1,020.00 USD | `-37.60%` | `2,198,000,000.00` |
| `Live` | `Long` | `470.50` | 4,090,000.00 USD | 0.00 USD | 9,830.00 USD | `-36.93%` | `20,901,000,000.00` |
| `Live` | `Long` | `473.50` | 4,080,000.00 USD | 0.00 USD | 1,970.00 USD | `-36.53%` | `4,170,000,000.00` |
| `Live` | `Long` | `476.50` | 4,080,000.00 USD | 0.00 USD | 5,800.00 USD | `-36.12%` | `12,182,000,000.00` |
| `Live` | `Long` | `487.50` | 4,070,000.00 USD | 0.00 USD | 2,550.00 USD | `-34.65%` | `5,235,000,000.00` |
| `Live` | `Long` | `498.50` | 4,070,000.00 USD | 0.00 USD | 2,120.00 USD | `-33.18%` | `4,246,000,000.00` |
| `Live` | `Long` | `501.50` | 4,070,000.00 USD | 0.00 USD | 7,760.00 USD | `-32.77%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 4,060,000.00 USD | 0.00 USD | 109.04 USD | `-32.64%` | `217,000,000.00` |
| `Live` | `Long` | `509.50` | 4,060,000.00 USD | 0.00 USD | 3,610.00 USD | `-31.70%` | `7,091,000,000.00` |
| `Live` | `Long` | `511.50` | 4,060,000.00 USD | 0.00 USD | 414.32 USD | `-31.43%` | `810,000,000.00` |
| `Live` | `Long` | `512.50` | 4,060,000.00 USD | 0.00 USD | 5,190.00 USD | `-31.30%` | `10,118,000,000.00` |
| `Live` | `Long` | `513.50` | 4,050,000.00 USD | 0.00 USD | 3,100.00 USD | `-31.16%` | `6,034,000,000.00` |
| `Live` | `Long` | `514.50` | 4,050,000.00 USD | 0.00 USD | 4,010.00 USD | `-31.03%` | `7,787,000,000.00` |
| `Live` | `Long` | `515.50` | 4,040,000.00 USD | 0.00 USD | 5,360.00 USD | `-30.90%` | `10,395,000,000.00` |
| `Live` | `Long` | `516.50` | 4,040,000.00 USD | 0.00 USD | 2,700.00 USD | `-30.76%` | `5,231,000,000.00` |
| `Live` | `Long` | `517.50` | 4,040,000.00 USD | 0.00 USD | 1,160.00 USD | `-30.63%` | `2,246,000,000.00` |
| `Live` | `Long` | `519.50` | 4,030,000.00 USD | 0.00 USD | 3,260.00 USD | `-30.36%` | `6,273,000,000.00` |
| `Live` | `Long` | `520.50` | 4,030,000.00 USD | 0.00 USD | 3,560.00 USD | `-30.23%` | `6,833,000,000.00` |
| `Live` | `Long` | `521.50` | 4,030,000.00 USD | 0.00 USD | 11,320.00 USD | `-30.09%` | `21,712,000,000.00` |
| `Live` | `Long` | `522.50` | 4,020,000.00 USD | 0.00 USD | 599.31 USD | `-29.96%` | `1,147,000,000.00` |
| `Live` | `Long` | `523.50` | 4,020,000.00 USD | 0.00 USD | 2,090.00 USD | `-29.82%` | `3,993,000,000.00` |
| `Live` | `Long` | `524.50` | 4,010,000.00 USD | 0.00 USD | 1,460.00 USD | `-29.69%` | `2,790,000,000.00` |
| `Live` | `Long` | `525.50` | 4,010,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.56%` | `2,298,000,000.00` |
| `Live` | `Long` | `526.50` | 4,010,000.00 USD | 0.00 USD | 3,080.00 USD | `-29.42%` | `5,844,000,000.00` |
| `Live` | `Long` | `527.50` | 4,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-29.29%` | `1,999,000,000.00` |
| `Live` | `Long` | `529.50` | 4,010,000.00 USD | 0.00 USD | 42,820.00 USD | `-29.02%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 3,960,000.00 USD | 0.00 USD | 16,980.00 USD | `-28.89%` | `32,010,000,000.00` |
| `Live` | `Long` | `531.50` | 3,950,000.00 USD | 0.00 USD | 1,280.00 USD | `-28.75%` | `2,402,000,000.00` |
| `Live` | `Long` | `532.50` | 3,950,000.00 USD | 0.00 USD | 632.08 USD | `-28.62%` | `1,187,000,000.00` |
| `Live` | `Long` | `534.50` | 3,950,000.00 USD | 0.00 USD | 555.35 USD | `-28.35%` | `1,039,000,000.00` |
| `Live` | `Long` | `536.50` | 3,940,000.00 USD | 0.00 USD | 100.33 USD | `-28.08%` | `187,000,000.00` |
| `Live` | `Long` | `537.50` | 3,940,000.00 USD | 0.00 USD | 4,300.00 USD | `-27.95%` | `8,000,000,000.00` |
| `Live` | `Long` | `539.50` | 3,940,000.00 USD | 0.00 USD | 490.94 USD | `-27.68%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,940,000.00 USD | 0.00 USD | 270.25 USD | `-27.54%` | `500,000,000.00` |
| `Live` | `Long` | `541.50` | 3,940,000.00 USD | 0.00 USD | 472.19 USD | `-27.41%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,940,000.00 USD | 0.00 USD | 334.25 USD | `-27.14%` | `615,000,000.00` |
| `Live` | `Long` | `544.50` | 3,940,000.00 USD | 0.00 USD | 4,050.00 USD | `-27.01%` | `7,438,000,000.00` |
| `Live` | `Long` | `545.50` | 3,930,000.00 USD | 0.00 USD | 212,670.00 USD | `-26.87%` | `389,869,000,000.00` |
| `Live` | `Long` | `546.50` | 3,720,000.00 USD | 0.00 USD | 491.85 USD | `-26.74%` | `900,000,000.00` |
| `Live` | `Long` | `547.50` | 3,720,000.00 USD | 0.00 USD | 531.07 USD | `-26.61%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 3,720,000.00 USD | 0.00 USD | 1,280.00 USD | `-26.47%` | `2,336,000,000.00` |
| `Live` | `Long` | `549.50` | 3,720,000.00 USD | 0.00 USD | 1,770.00 USD | `-26.34%` | `3,224,000,000.00` |
| `Live` | `Long` | `550.50` | 3,720,000.00 USD | 0.00 USD | 633.63 USD | `-26.20%` | `1,151,000,000.00` |
| `Live` | `Long` | `552.50` | 3,720,000.00 USD | 0.00 USD | 959.69 USD | `-25.94%` | `1,737,000,000.00` |
| `Live` | `Long` | `553.50` | 3,720,000.00 USD | 0.00 USD | 2,420.00 USD | `-25.80%` | `4,365,000,000.00` |
| `Live` | `Long` | `554.50` | 3,710,000.00 USD | 0.00 USD | 2,010.00 USD | `-25.67%` | `3,625,000,000.00` |
| `Live` | `Long` | `555.50` | 3,710,000.00 USD | 0.00 USD | 591.61 USD | `-25.53%` | `1,065,000,000.00` |
| `Live` | `Long` | `557.50` | 3,710,000.00 USD | 0.00 USD | 5,680.00 USD | `-25.27%` | `10,193,000,000.00` |
| `Live` | `Long` | `559.50` | 3,710,000.00 USD | 0.00 USD | 212.61 USD | `-25.00%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 3,710,000.00 USD | 0.00 USD | 10,940.00 USD | `-24.86%` | `19,515,000,000.00` |
| `Live` | `Long` | `561.50` | 3,690,000.00 USD | 0.00 USD | 583.40 USD | `-24.73%` | `1,039,000,000.00` |
| `Live` | `Long` | `562.50` | 3,690,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-24.60%` | `2,805,710,000,000.00` |
| `Live` | `Long` | `564.50` | 2,120,000.00 USD | 0.00 USD | 14,210.00 USD | `-24.33%` | `25,181,000,000.00` |
| `Live` | `Long` | `568.50` | 2,100,000.00 USD | 0.00 USD | 392.26 USD | `-23.79%` | `690,000,000.00` |
| `Live` | `Long` | `572.50` | 2,100,000.00 USD | 0.00 USD | 715,280.00 USD | `-23.26%` | `1,249,401,000,000.00` |
| `Live` | `Long` | `574.50` | 1,390,000.00 USD | 0.00 USD | 323.44 USD | `-22.99%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 1,390,000.00 USD | 0.00 USD | 862.44 USD | `-22.72%` | `1,496,000,000.00` |
| `Live` | `Long` | `577.50` | 1,380,000.00 USD | 0.00 USD | 222.91 USD | `-22.59%` | `386,000,000.00` |
| `Live` | `Long` | `578.50` | 1,380,000.00 USD | 0.00 USD | 275.37 USD | `-22.45%` | `476,000,000.00` |
| `Live` | `Long` | `579.50` | 1,380,000.00 USD | 0.00 USD | 2,320.00 USD | `-22.32%` | `4,005,000,000.00` |
| `Live` | `Long` | `583.50` | 1,380,000.00 USD | 0.00 USD | 15,440.00 USD | `-21.78%` | `26,453,000,000.00` |
| `Live` | `Long` | `584.50` | 1,370,000.00 USD | 0.00 USD | 10,910.00 USD | `-21.65%` | `18,661,000,000.00` |
| `Live` | `Long` | `586.50` | 1,360,000.00 USD | 0.00 USD | 2,540.00 USD | `-21.38%` | `4,339,000,000.00` |
| `Live` | `Long` | `587.50` | 1,350,000.00 USD | 0.00 USD | 1,530.00 USD | `-21.24%` | `2,612,000,000.00` |
| `Live` | `Long` | `590.50` | 1,350,000.00 USD | 0.00 USD | 100.39 USD | `-20.84%` | `170,000,000.00` |
| `Live` | `Long` | `594.50` | 1,350,000.00 USD | 0.00 USD | 44,800.00 USD | `-20.31%` | `75,354,000,000.00` |
| `Live` | `Long` | `596.50` | 1,310,000.00 USD | 0.00 USD | 1,680.00 USD | `-20.04%` | `2,814,000,000.00` |
| `Live` | `Long` | `597.50` | 1,300,000.00 USD | 0.00 USD | 100.98 USD | `-19.90%` | `169,000,000.00` |
| `Live` | `Long` | `598.50` | 1,300,000.00 USD | 0.00 USD | 1,060.00 USD | `-19.77%` | `1,766,000,000.00` |
| `Live` | `Long` | `599.50` | 1,300,000.00 USD | 0.00 USD | 116.90 USD | `-19.64%` | `195,000,000.00` |
| `Live` | `Long` | `600.50` | 1,300,000.00 USD | 0.00 USD | 945.19 USD | `-19.50%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,300,000.00 USD | 0.00 USD | 303.76 USD | `-19.37%` | `505,000,000.00` |
| `Live` | `Long` | `604.50` | 1,300,000.00 USD | 0.00 USD | 1,610.00 USD | `-18.97%` | `2,671,000,000.00` |
| `Live` | `Long` | `606.50` | 1,300,000.00 USD | 0.00 USD | 509.46 USD | `-18.70%` | `840,000,000.00` |
| `Live` | `Long` | `607.50` | 1,300,000.00 USD | 0.00 USD | 1,880.00 USD | `-18.56%` | `3,092,000,000.00` |
| `Live` | `Long` | `608.50` | 1,300,000.00 USD | 0.00 USD | 329.20 USD | `-18.43%` | `541,000,000.00` |
| `Live` | `Long` | `610.50` | 1,300,000.00 USD | 0.00 USD | 213.67 USD | `-18.16%` | `350,000,000.00` |
| `Live` | `Long` | `613.50` | 1,300,000.00 USD | 0.00 USD | 527.00 USD | `-17.76%` | `859,000,000.00` |
| `Live` | `Long` | `614.50` | 1,300,000.00 USD | 0.00 USD | 2,280.00 USD | `-17.63%` | `3,710,000,000.00` |
| `Live` | `Long` | `615.50` | 1,290,000.00 USD | 0.00 USD | 427.16 USD | `-17.49%` | `694,000,000.00` |
| `Live` | `Long` | `616.50` | 1,290,000.00 USD | 0.00 USD | 1,510.00 USD | `-17.36%` | `2,450,000,000.00` |
| `Live` | `Long` | `617.50` | 1,290,000.00 USD | 0.00 USD | 156.23 USD | `-17.22%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,290,000.00 USD | 0.00 USD | 187.41 USD | `-17.09%` | `303,000,000.00` |
| `Live` | `Long` | `620.50` | 1,290,000.00 USD | 0.00 USD | 5,410.00 USD | `-16.82%` | `8,712,000,000.00` |
| `Live` | `Long` | `621.50` | 1,290,000.00 USD | 0.00 USD | 1,260.00 USD | `-16.69%` | `2,020,000,000.00` |
| `Live` | `Long` | `622.50` | 1,290,000.00 USD | 0.00 USD | 2,110.00 USD | `-16.55%` | `3,397,000,000.00` |
| `Live` | `Long` | `623.50` | 1,280,000.00 USD | 0.00 USD | 1,050.00 USD | `-16.42%` | `1,691,000,000.00` |
| `Live` | `Long` | `624.50` | 1,280,000.00 USD | 0.00 USD | 3,460.00 USD | `-16.28%` | `5,547,000,000.00` |
| `Live` | `Long` | `625.50` | 1,280,000.00 USD | 0.00 USD | 11,970.00 USD | `-16.15%` | `19,142,000,000.00` |
| `Live` | `Long` | `626.50` | 1,270,000.00 USD | 0.00 USD | 16,020.00 USD | `-16.02%` | `25,566,000,000.00` |
| `Live` | `Long` | `627.50` | 1,250,000.00 USD | 0.00 USD | 326.30 USD | `-15.88%` | `520,000,000.00` |
| `Live` | `Long` | `628.50` | 1,250,000.00 USD | 0.00 USD | 664.32 USD | `-15.75%` | `1,057,000,000.00` |
| `Live` | `Long` | `629.50` | 1,250,000.00 USD | 0.00 USD | 3,680.00 USD | `-15.61%` | `5,849,000,000.00` |
| `Live` | `Long` | `631.50` | 1,250,000.00 USD | 0.00 USD | 6,320.00 USD | `-15.35%` | `10,000,000,000.00` |
| `Live` | `Long` | `632.50` | 1,240,000.00 USD | 0.00 USD | 401.64 USD | `-15.21%` | `635,000,000.00` |
| `Live` | `Long` | `633.50` | 1,240,000.00 USD | 0.00 USD | 1,920.00 USD | `-15.08%` | `3,038,000,000.00` |
| `Live` | `Long` | `635.50` | 1,240,000.00 USD | 0.00 USD | 5,910.00 USD | `-14.81%` | `9,302,000,000.00` |
| `Live` | `Long` | `637.50` | 1,230,000.00 USD | 0.00 USD | 8,460.00 USD | `-14.54%` | `13,266,000,000.00` |
| `Live` | `Long` | `638.50` | 1,220,000.00 USD | 0.00 USD | 432.90 USD | `-14.41%` | `678,000,000.00` |
| `Live` | `Long` | `639.50` | 1,220,000.00 USD | 0.00 USD | 33,550.00 USD | `-14.27%` | `52,460,000,000.00` |
| `Live` | `Long` | `640.50` | 1,190,000.00 USD | 0.00 USD | 2,310.00 USD | `-14.14%` | `3,600,000,000.00` |
| `Live` | `Long` | `641.50` | 1,190,000.00 USD | 0.00 USD | 1,670.00 USD | `-14.01%` | `2,606,000,000.00` |
| `Live` | `Long` | `642.50` | 1,190,000.00 USD | 0.00 USD | 9,470.00 USD | `-13.87%` | `14,732,000,000.00` |
| `Live` | `Long` | `643.50` | 1,180,000.00 USD | 0.00 USD | 10,650.00 USD | `-13.74%` | `16,549,000,000.00` |
| `Live` | `Long` | `645.50` | 1,170,000.00 USD | 0.00 USD | 3,820.00 USD | `-13.47%` | `5,914,000,000.00` |
| `Live` | `Long` | `646.50` | 1,160,000.00 USD | 0.00 USD | 2,120.00 USD | `-13.34%` | `3,281,000,000.00` |
| `Live` | `Long` | `649.50` | 1,160,000.00 USD | 0.00 USD | 559.87 USD | `-12.93%` | `862,000,000.00` |
| `Live` | `Long` | `651.50` | 1,160,000.00 USD | 0.00 USD | 633.26 USD | `-12.67%` | `972,000,000.00` |
| `Live` | `Long` | `654.50` | 1,160,000.00 USD | 0.00 USD | 97,530.00 USD | `-12.26%` | `149,014,000,000.00` |
| `Live` | `Long` | `656.50` | 1,060,000.00 USD | 0.00 USD | 122.77 USD | `-11.99%` | `187,000,000.00` |
| `Live` | `Long` | `657.50` | 1,060,000.00 USD | 0.00 USD | 2,180.00 USD | `-11.86%` | `3,321,000,000.00` |
| `Live` | `Long` | `658.50` | 1,060,000.00 USD | 0.00 USD | 4,800.00 USD | `-11.73%` | `7,282,000,000.00` |
| `Live` | `Long` | `660.50` | 1,050,000.00 USD | 0.00 USD | 3,340.00 USD | `-11.46%` | `5,053,000,000.00` |
| `Live` | `Long` | `661.50` | 1,050,000.00 USD | 0.00 USD | 463.71 USD | `-11.32%` | `701,000,000.00` |
| `Live` | `Long` | `662.50` | 1,050,000.00 USD | 0.00 USD | 19,830.00 USD | `-11.19%` | `29,930,000,000.00` |
| `Live` | `Long` | `663.50` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-11.06%` | `3,115,000,000.00` |
| `Live` | `Long` | `666.50` | 1,030,000.00 USD | 0.00 USD | 5,440.00 USD | `-10.65%` | `8,159,000,000.00` |
| `Live` | `Long` | `669.50` | 1,020,000.00 USD | 0.00 USD | 3,040.00 USD | `-10.25%` | `4,542,000,000.00` |
| `Live` | `Long` | `670.50` | 1,020,000.00 USD | 0.00 USD | 2,570.00 USD | `-10.12%` | `3,839,000,000.00` |
| `Live` | `Long` | `671.50` | 1,020,000.00 USD | 0.00 USD | 3,360.00 USD | `-9.98%` | `5,000,000,000.00` |
| `Live` | `Long` | `672.50` | 1,010,000.00 USD | 0.00 USD | 13,020.00 USD | `-9.85%` | `19,359,000,000.00` |
| `Live` | `Long` | `673.50` | 1,000,000.00 USD | 0.00 USD | 567.76 USD | `-9.72%` | `843,000,000.00` |
| `Live` | `Long` | `674.50` | 999,990.00 USD | 0.00 USD | 259.68 USD | `-9.58%` | `385,000,000.00` |
| `Live` | `Long` | `676.50` | 999,730.00 USD | 0.00 USD | 877.42 USD | `-9.31%` | `1,297,000,000.00` |
| `Live` | `Long` | `678.50` | 998,860.00 USD | 0.00 USD | 1,610.00 USD | `-9.05%` | `2,375,000,000.00` |
| `Live` | `Long` | `681.50` | 997,240.00 USD | 0.00 USD | 31,450.00 USD | `-8.64%` | `46,154,000,000.00` |
| `Live` | `Long` | `684.50` | 965,790.00 USD | 0.00 USD | 42,430.00 USD | `-8.24%` | `61,984,000,000.00` |
| `Live` | `Long` | `685.50` | 923,360.00 USD | 0.00 USD | 1,290.00 USD | `-8.11%` | `1,882,000,000.00` |
| `Live` | `Long` | `686.50` | 922,070.00 USD | 0.00 USD | 194.28 USD | `-7.97%` | `283,000,000.00` |
| `Live` | `Long` | `687.50` | 921,880.00 USD | 0.00 USD | 198.69 USD | `-7.84%` | `289,000,000.00` |
| `Live` | `Long` | `689.50` | 921,680.00 USD | 0.00 USD | 885.32 USD | `-7.57%` | `1,284,000,000.00` |
| `Live` | `Long` | `690.50` | 920,790.00 USD | 0.00 USD | 6,170.00 USD | `-7.44%` | `8,933,000,000.00` |
| `Live` | `Long` | `691.50` | 914,630.00 USD | 0.00 USD | 5,430.00 USD | `-7.30%` | `7,853,000,000.00` |
| `Live` | `Long` | `692.50` | 909,190.00 USD | 0.00 USD | 5,580.00 USD | `-7.17%` | `8,061,000,000.00` |
| `Live` | `Long` | `693.50` | 903,610.00 USD | 0.00 USD | 2,590.00 USD | `-7.04%` | `3,732,000,000.00` |
| `Live` | `Long` | `694.50` | 901,020.00 USD | 0.00 USD | 513.93 USD | `-6.90%` | `740,000,000.00` |
| `Live` | `Long` | `695.50` | 900,510.00 USD | 0.00 USD | 470.85 USD | `-6.77%` | `677,000,000.00` |
| `Live` | `Long` | `697.50` | 900,040.00 USD | 0.00 USD | 2,160.00 USD | `-6.50%` | `3,097,000,000.00` |
| `Live` | `Long` | `698.50` | 897,880.00 USD | 0.00 USD | 178.82 USD | `-6.36%` | `256,000,000.00` |
| `Live` | `Long` | `699.50` | 897,700.00 USD | 0.00 USD | 20,100.00 USD | `-6.23%` | `28,732,000,000.00` |
| `Live` | `Long` | `700.50` | 877,600.00 USD | 0.00 USD | 1,130.00 USD | `-6.10%` | `1,612,000,000.00` |
| `Live` | `Long` | `702.50` | 876,470.00 USD | 0.00 USD | 2,080.00 USD | `-5.83%` | `2,956,000,000.00` |
| `Live` | `Long` | `703.50` | 874,400.00 USD | 0.00 USD | 3,820.00 USD | `-5.69%` | `5,425,000,000.00` |
| `Live` | `Long` | `704.50` | 870,580.00 USD | 0.00 USD | 2,720.00 USD | `-5.56%` | `3,857,000,000.00` |
| `Live` | `Long` | `705.50` | 867,860.00 USD | 0.00 USD | 829.67 USD | `-5.43%` | `1,176,000,000.00` |
| `Live` | `Long` | `706.50` | 867,030.00 USD | 0.00 USD | 23,030.00 USD | `-5.29%` | `32,594,000,000.00` |
| `Live` | `Long` | `707.50` | 844,010.00 USD | 0.00 USD | 22,380.00 USD | `-5.16%` | `31,637,000,000.00` |
| `Live` | `Long` | `708.50` | 821,620.00 USD | 0.00 USD | 171,950.00 USD | `-5.02%` | `242,695,000,000.00` |
| `Live` | `Long` | `709.50` | 649,670.00 USD | 0.00 USD | 338,480.00 USD | `-4.89%` | `477,065,000,000.00` |
| `Live` | `Long` | `710.50` | 311,200.00 USD | 0.00 USD | 41,890.00 USD | `-4.76%` | `58,960,000,000.00` |
| `Live` | `Long` | `711.50` | 269,300.00 USD | 0.00 USD | 11,630.00 USD | `-4.62%` | `16,350,000,000.00` |
| `Live` | `Long` | `712.50` | 257,670.00 USD | 0.00 USD | 229,760.00 USD | `-4.49%` | `322,464,000,000.00` |
| `Live` | `Long` | `713.50` | 27,920.00 USD | 0.00 USD | 22,170.00 USD | `-4.35%` | `31,068,000,000.00` |
| `Live` | `Long` | `714.50` | 5,750.00 USD | 0.00 USD | 157.90 USD | `-4.22%` | `221,000,000.00` |
| `Live` | `Long` | `716.50` | 5,590.00 USD | 0.00 USD | 789.58 USD | `-3.95%` | `1,102,000,000.00` |
| `Live` | `Long` | `717.50` | 4,800.00 USD | 0.00 USD | 3,700.00 USD | `-3.82%` | `5,155,000,000.00` |
| `Live` | `Long` | `718.50` | 1,100.00 USD | 0.00 USD | 104.18 USD | `-3.68%` | `145,000,000.00` |
| `Live` | `Long` | `721.50` | 998.56 USD | 0.00 USD | 998.56 USD | `-3.28%` | `1,384,000,000.00` |
| `Live` | `Short` | `761.50` | 1,910.00 USD | 1,910.00 USD | 0.00 USD | `+2.08%` | `2,505,000,000.00` |
| `Live` | `Short` | `763.50` | 2,120.00 USD | 211.49 USD | 0.00 USD | `+2.35%` | `277,000,000.00` |
| `Live` | `Short` | `767.50` | 3,170.00 USD | 1,050.00 USD | 0.00 USD | `+2.88%` | `1,365,000,000.00` |
| `Live` | `Short` | `768.50` | 3,320.00 USD | 156.77 USD | 0.00 USD | `+3.02%` | `204,000,000.00` |
| `Live` | `Short` | `773.50` | 11,590.00 USD | 8,270.00 USD | 0.00 USD | `+3.69%` | `10,692,000,000.00` |
| `Live` | `Short` | `774.50` | 11,720.00 USD | 130.12 USD | 0.00 USD | `+3.82%` | `168,000,000.00` |
| `Live` | `Short` | `775.50` | 12,560.00 USD | 839.09 USD | 0.00 USD | `+3.96%` | `1,082,000,000.00` |
| `Live` | `Short` | `776.50` | 13,610.00 USD | 1,050.00 USD | 0.00 USD | `+4.09%` | `1,351,000,000.00` |
| `Live` | `Short` | `777.50` | 16,490.00 USD | 2,880.00 USD | 0.00 USD | `+4.23%` | `3,705,000,000.00` |
| `Live` | `Short` | `778.50` | 27,600.00 USD | 11,100.00 USD | 0.00 USD | `+4.36%` | `14,263,000,000.00` |
| `Live` | `Short` | `780.50` | 27,800.00 USD | 202.93 USD | 0.00 USD | `+4.63%` | `260,000,000.00` |
| `Live` | `Short` | `781.50` | 27,990.00 USD | 194.59 USD | 0.00 USD | `+4.76%` | `249,000,000.00` |
| `Live` | `Short` | `782.50` | 275,020.00 USD | 247,020.00 USD | 0.00 USD | `+4.90%` | `315,684,000,000.00` |
| `Live` | `Short` | `783.50` | 275,320.00 USD | 303.21 USD | 0.00 USD | `+5.03%` | `387,000,000.00` |
| `Live` | `Short` | `784.50` | 278,420.00 USD | 3,100.00 USD | 0.00 USD | `+5.16%` | `3,956,000,000.00` |
| `Live` | `Short` | `785.50` | 281,470.00 USD | 3,040.00 USD | 0.00 USD | `+5.30%` | `3,873,000,000.00` |
| `Live` | `Short` | `786.50` | 286,200.00 USD | 4,730.00 USD | 0.00 USD | `+5.43%` | `6,016,000,000.00` |
| `Live` | `Short` | `787.50` | 417,090.00 USD | 130,890.00 USD | 0.00 USD | `+5.57%` | `166,210,000,000.00` |
| `Live` | `Short` | `788.50` | 417,210.00 USD | 126.16 USD | 0.00 USD | `+5.70%` | `160,000,000.00` |
| `Live` | `Short` | `789.50` | 419,200.00 USD | 1,980.00 USD | 0.00 USD | `+5.83%` | `2,511,000,000.00` |
| `Live` | `Short` | `791.50` | 421,470.00 USD | 2,280.00 USD | 0.00 USD | `+6.10%` | `2,875,000,000.00` |
| `Live` | `Short` | `793.50` | 421,630.00 USD | 158.70 USD | 0.00 USD | `+6.37%` | `200,000,000.00` |
| `Live` | `Short` | `794.50` | 421,810.00 USD | 179.56 USD | 0.00 USD | `+6.50%` | `226,000,000.00` |
| `Live` | `Short` | `795.50` | 422,330.00 USD | 518.67 USD | 0.00 USD | `+6.64%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 422,500.00 USD | 172.84 USD | 0.00 USD | `+6.77%` | `217,000,000.00` |
| `Live` | `Short` | `801.50` | 423,260.00 USD | 761.42 USD | 0.00 USD | `+7.44%` | `950,000,000.00` |
| `Live` | `Short` | `802.50` | 423,540.00 USD | 279.27 USD | 0.00 USD | `+7.58%` | `348,000,000.00` |
| `Live` | `Short` | `804.50` | 424,620.00 USD | 1,080.00 USD | 0.00 USD | `+7.84%` | `1,338,000,000.00` |
| `Live` | `Short` | `806.50` | 468,830.00 USD | 44,210.00 USD | 0.00 USD | `+8.11%` | `54,814,000,000.00` |
| `Live` | `Short` | `811.50` | 469,090.00 USD | 265.36 USD | 0.00 USD | `+8.78%` | `327,000,000.00` |
| `Live` | `Short` | `818.50` | 469,300.00 USD | 205.44 USD | 0.00 USD | `+9.72%` | `251,000,000.00` |
| `Live` | `Short` | `821.50` | 481,140.00 USD | 11,840.00 USD | 0.00 USD | `+10.12%` | `14,418,000,000.00` |
| `Live` | `Short` | `823.50` | 482,870.00 USD | 1,730.00 USD | 0.00 USD | `+10.39%` | `2,102,000,000.00` |
| `Live` | `Short` | `831.50` | 492,910.00 USD | 10,040.00 USD | 0.00 USD | `+11.46%` | `12,072,000,000.00` |
| `Live` | `Short` | `834.50` | 493,920.00 USD | 1,010.00 USD | 0.00 USD | `+11.87%` | `1,206,000,000.00` |
| `Live` | `Short` | `835.50` | 494,260.00 USD | 340.88 USD | 0.00 USD | `+12.00%` | `408,000,000.00` |
| `Live` | `Short` | `836.50` | 494,880.00 USD | 625.70 USD | 0.00 USD | `+12.13%` | `748,000,000.00` |
| `Live` | `Short` | `837.50` | 495,010.00 USD | 125.62 USD | 0.00 USD | `+12.27%` | `150,000,000.00` |
| `Live` | `Short` | `839.50` | 495,580.00 USD | 572.54 USD | 0.00 USD | `+12.54%` | `682,000,000.00` |
| `Live` | `Short` | `841.50` | 498,570.00 USD | 2,980.00 USD | 0.00 USD | `+12.80%` | `3,547,000,000.00` |
| `Live` | `Short` | `842.50` | 498,720.00 USD | 153.34 USD | 0.00 USD | `+12.94%` | `182,000,000.00` |
| `Live` | `Short` | `843.50` | 672,020.00 USD | 173,300.00 USD | 0.00 USD | `+13.07%` | `205,454,000,000.00` |
| `Live` | `Short` | `845.50` | 1,010,000.00 USD | 338,650.00 USD | 0.00 USD | `+13.34%` | `400,529,000,000.00` |
| `Live` | `Short` | `848.50` | 1,010,000.00 USD | 289.34 USD | 0.00 USD | `+13.74%` | `341,000,000.00` |
| `Live` | `Short` | `849.50` | 1,010,000.00 USD | 416.25 USD | 0.00 USD | `+13.88%` | `490,000,000.00` |
| `Live` | `Short` | `851.50` | 1,010,000.00 USD | 108.99 USD | 0.00 USD | `+14.15%` | `128,000,000.00` |
| `Live` | `Short` | `854.50` | 1,010,000.00 USD | 138.43 USD | 0.00 USD | `+14.55%` | `162,000,000.00` |
| `Live` | `Short` | `855.50` | 1,010,000.00 USD | 171.10 USD | 0.00 USD | `+14.68%` | `200,000,000.00` |
| `Live` | `Short` | `859.50` | 1,010,000.00 USD | 265.59 USD | 0.00 USD | `+15.22%` | `309,000,000.00` |
| `Live` | `Short` | `864.50` | 1,020,000.00 USD | 6,240.00 USD | 0.00 USD | `+15.89%` | `7,220,000,000.00` |
| `Live` | `Short` | `866.50` | 1,020,000.00 USD | 236.55 USD | 0.00 USD | `+16.16%` | `273,000,000.00` |
| `Live` | `Short` | `868.50` | 1,020,000.00 USD | 1,530.00 USD | 0.00 USD | `+16.42%` | `1,765,000,000.00` |
| `Live` | `Short` | `869.50` | 1,470,000.00 USD | 452,190.00 USD | 0.00 USD | `+16.56%` | `520,062,000,000.00` |
| `Live` | `Short` | `878.50` | 1,490,000.00 USD | 12,820.00 USD | 0.00 USD | `+17.76%` | `14,595,000,000.00` |
| `Live` | `Short` | `879.50` | 1,490,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.90%` | `5,165,000,000.00` |
| `Live` | `Short` | `885.50` | 1,490,000.00 USD | 2,750.00 USD | 0.00 USD | `+18.70%` | `3,111,000,000.00` |
| `Live` | `Short` | `886.50` | 1,490,000.00 USD | 812.92 USD | 0.00 USD | `+18.84%` | `917,000,000.00` |
| `Live` | `Short` | `889.50` | 1,490,000.00 USD | 772.09 USD | 0.00 USD | `+19.24%` | `868,000,000.00` |
| `Live` | `Short` | `892.50` | 1,500,000.00 USD | 3,350.00 USD | 0.00 USD | `+19.64%` | `3,752,000,000.00` |
| `Live` | `Short` | `896.50` | 1,720,000.00 USD | 224,510.00 USD | 0.00 USD | `+20.18%` | `250,426,000,000.00` |
| `Live` | `Short` | `907.50` | 1,720,000.00 USD | 392.04 USD | 0.00 USD | `+21.65%` | `432,000,000.00` |
| `Live` | `Short` | `908.50` | 1,720,000.00 USD | 901.23 USD | 0.00 USD | `+21.79%` | `992,000,000.00` |
| `Live` | `Short` | `911.50` | 1,760,000.00 USD | 39,480.00 USD | 0.00 USD | `+22.19%` | `43,317,000,000.00` |
| `Live` | `Short` | `924.50` | 1,760,000.00 USD | 196.92 USD | 0.00 USD | `+23.93%` | `213,000,000.00` |
| `Live` | `Short` | `925.50` | 1,770,000.00 USD | 9,260.00 USD | 0.00 USD | `+24.06%` | `10,000,000,000.00` |
| `Live` | `Short` | `928.50` | 1,770,000.00 USD | 285.05 USD | 0.00 USD | `+24.47%` | `307,000,000.00` |
| `Live` | `Short` | `931.50` | 1,780,000.00 USD | 3,250.00 USD | 0.00 USD | `+24.87%` | `3,487,000,000.00` |
| `Live` | `Short` | `939.50` | 1,780,000.00 USD | 1,060.00 USD | 0.00 USD | `+25.94%` | `1,133,000,000.00` |
| `Live` | `Short` | `945.50` | 1,780,000.00 USD | 110.62 USD | 0.00 USD | `+26.75%` | `117,000,000.00` |
| `Live` | `Short` | `952.50` | 1,780,000.00 USD | 398.14 USD | 0.00 USD | `+27.68%` | `418,000,000.00` |
| `Live` | `Short` | `959.50` | 1,840,000.00 USD | 67,170.00 USD | 0.00 USD | `+28.62%` | `70,000,000,000.00` |
| `Live` | `Short` | `960.50` | 1,900,000.00 USD | 58,980.00 USD | 0.00 USD | `+28.76%` | `61,406,000,000.00` |
| `Live` | `Short` | `963.50` | 2,740,000.00 USD | 838,250.00 USD | 0.00 USD | `+29.16%` | `870,000,000,000.00` |
| `Live` | `Short` | `967.50` | 2,740,000.00 USD | 1,940.00 USD | 0.00 USD | `+29.70%` | `2,000,000,000.00` |
| `Live` | `Short` | `981.50` | 2,760,000.00 USD | 14,480.00 USD | 0.00 USD | `+31.57%` | `14,758,000,000.00` |
| `Live` | `Short` | `983.50` | 2,760,000.00 USD | 1,640.00 USD | 0.00 USD | `+31.84%` | `1,667,000,000.00` |
| `Live` | `Short` | `992.50` | 2,790,000.00 USD | 27,400.00 USD | 0.00 USD | `+33.05%` | `27,604,000,000.00` |
| `Live` | `Short` | `994.50` | 3,170,000.00 USD | 384,970.00 USD | 0.00 USD | `+33.31%` | `387,096,000,000.00` |
| `Live` | `Short` | `1005.50` | 3,870,000.00 USD | 703,020.00 USD | 0.00 USD | `+34.79%` | `699,175,000,000.00` |
| `Live` | `Short` | `1019.50` | 3,880,000.00 USD | 9,640.00 USD | 0.00 USD | `+36.67%` | `9,460,000,000.00` |
| `Live` | `Short` | `1029.50` | 3,990,000.00 USD | 102,950.00 USD | 0.00 USD | `+38.01%` | `100,000,000,000.00` |
| `Live` | `Short` | `1039.50` | 3,990,000.00 USD | 676.71 USD | 0.00 USD | `+39.35%` | `651,000,000.00` |
| `Live` | `Short` | `1040.50` | 3,990,000.00 USD | 180.01 USD | 0.00 USD | `+39.48%` | `173,000,000.00` |
| `Live` | `Short` | `1049.50` | 3,990,000.00 USD | 294.91 USD | 0.00 USD | `+40.69%` | `281,000,000.00` |
| `Live` | `Short` | `1050.50` | 3,990,000.00 USD | 500.04 USD | 0.00 USD | `+40.82%` | `476,000,000.00` |
| `Live` | `Short` | `1057.50` | 3,990,000.00 USD | 391.27 USD | 0.00 USD | `+41.76%` | `370,000,000.00` |
| `Live` | `Short` | `1064.50` | 3,990,000.00 USD | 1,600.00 USD | 0.00 USD | `+42.70%` | `1,500,000,000.00` |
| `Live` | `Short` | `1071.50` | 3,990,000.00 USD | 1,550.00 USD | 0.00 USD | `+43.64%` | `1,446,000,000.00` |
| `Live` | `Short` | `1073.50` | 3,990,000.00 USD | 1,610.00 USD | 0.00 USD | `+43.90%` | `1,500,000,000.00` |
| `Live` | `Short` | `1113.50` | 4,010,000.00 USD | 19,850.00 USD | 0.00 USD | `+49.27%` | `17,826,000,000.00` |
| `Live` | `Short` | `1118.50` | 4,020,000.00 USD | 6,160.00 USD | 0.00 USD | `+49.94%` | `5,508,000,000.00` |
| `Live` | `Short` | `1147.50` | 4,020,000.00 USD | 153.77 USD | 0.00 USD | `+53.82%` | `134,000,000.00` |
| `Live` | `Short` | `1165.50` | 4,080,000.00 USD | 56,310.00 USD | 0.00 USD | `+56.24%` | `48,311,000,000.00` |
| `Live` | `Short` | `1166.50` | 4,090,000.00 USD | 9,150.00 USD | 0.00 USD | `+56.37%` | `7,843,000,000.00` |
| `Live` | `Short` | `1169.50` | 4,090,000.00 USD | 367.22 USD | 0.00 USD | `+56.77%` | `314,000,000.00` |
| `Live` | `Short` | `1173.50` | 4,100,000.00 USD | 14,380.00 USD | 0.00 USD | `+57.31%` | `12,251,000,000.00` |
| `Live` | `Short` | `1187.50` | 4,100,000.00 USD | 159.12 USD | 0.00 USD | `+59.19%` | `134,000,000.00` |
| `Live` | `Short` | `1197.50` | 4,100,000.00 USD | 463.43 USD | 0.00 USD | `+60.53%` | `387,000,000.00` |
| `Live` | `Short` | `1200.50` | 4,100,000.00 USD | 134.46 USD | 0.00 USD | `+60.93%` | `112,000,000.00` |
| `Live` | `Short` | `1205.50` | 4,100,000.00 USD | 1,210.00 USD | 0.00 USD | `+61.60%` | `1,000,000,000.00` |
| `Live` | `Short` | `1207.50` | 4,130,000.00 USD | 30,550.00 USD | 0.00 USD | `+61.87%` | `25,301,000,000.00` |
| `Live` | `Short` | `1208.50` | 4,140,000.00 USD | 8,460.00 USD | 0.00 USD | `+62.00%` | `6,999,000,000.00` |
| `Live` | `Short` | `1225.50` | 4,140,000.00 USD | 1,030.00 USD | 0.00 USD | `+64.28%` | `841,000,000.00` |
| `Live` | `Short` | `1252.50` | 4,140,000.00 USD | 100.20 USD | 0.00 USD | `+67.90%` | `80,000,000.00` |
| `Live` | `Short` | `1258.50` | 4,140,000.00 USD | 341.05 USD | 0.00 USD | `+68.70%` | `271,000,000.00` |
| `Live` | `Short` | `1263.50` | 4,140,000.00 USD | 205.95 USD | 0.00 USD | `+69.37%` | `163,000,000.00` |
| `Live` | `Short` | `1265.50` | 4,140,000.00 USD | 202.48 USD | 0.00 USD | `+69.64%` | `160,000,000.00` |
| `Live` | `Short` | `1278.50` | 4,310,000.00 USD | 162,220.00 USD | 0.00 USD | `+71.39%` | `126,881,000,000.00` |
| `Live` | `Short` | `1283.50` | 4,420,000.00 USD | 115,520.00 USD | 0.00 USD | `+72.06%` | `90,000,000,000.00` |
| `Live` | `Short` | `1290.50` | 4,430,000.00 USD | 8,400.00 USD | 0.00 USD | `+72.99%` | `6,508,000,000.00` |
| `Live` | `Short` | `1291.50` | 4,430,000.00 USD | 4,330.00 USD | 0.00 USD | `+73.13%` | `3,350,000,000.00` |
| `Live` | `Short` | `1295.50` | 4,430,000.00 USD | 181.37 USD | 0.00 USD | `+73.66%` | `140,000,000.00` |
| `Live` | `Short` | `1296.50` | 5,210,000.00 USD | 771,070.00 USD | 0.00 USD | `+73.80%` | `594,730,000,000.00` |
| `Live` | `Short` | `1320.50` | 5,220,000.00 USD | 14,140.00 USD | 0.00 USD | `+77.02%` | `10,710,000,000.00` |
| `Live` | `Short` | `1330.50` | 5,240,000.00 USD | 23,470.00 USD | 0.00 USD | `+78.36%` | `17,640,000,000.00` |
| `Live` | `Short` | `1335.50` | 5,240,000.00 USD | 102.83 USD | 0.00 USD | `+79.03%` | `77,000,000.00` |
| `Live` | `Short` | `1339.50` | 5,260,000.00 USD | 20,090.00 USD | 0.00 USD | `+79.56%` | `15,000,000,000.00` |
| `Live` | `Short` | `1363.50` | 5,510,000.00 USD | 245,430.00 USD | 0.00 USD | `+82.78%` | `180,000,000,000.00` |
| `Live` | `Short` | `1375.50` | 5,510,000.00 USD | 158.18 USD | 0.00 USD | `+84.39%` | `115,000,000.00` |
| `Live` | `Short` | `1391.50` | 5,520,000.00 USD | 10,030.00 USD | 0.00 USD | `+86.53%` | `7,210,000,000.00` |
| `Live` | `Short` | `1401.50` | 5,520,000.00 USD | 5,600.00 USD | 0.00 USD | `+87.87%` | `3,994,000,000.00` |
| `Live` | `Short` | `1402.50` | 5,520,000.00 USD | 178.12 USD | 0.00 USD | `+88.01%` | `127,000,000.00` |
| `Live` | `Short` | `1413.50` | 5,520,000.00 USD | 139.94 USD | 0.00 USD | `+89.48%` | `99,000,000.00` |
| `Live` | `Short` | `1432.50` | 5,530,000.00 USD | 360.99 USD | 0.00 USD | `+92.03%` | `252,000,000.00` |
| `Live` | `Short` | `1444.50` | 6,220,000.00 USD | 697,520.00 USD | 0.00 USD | `+93.64%` | `482,880,000,000.00` |
| `Live` | `Short` | `1455.50` | 6,230,000.00 USD | 8,910.00 USD | 0.00 USD | `+95.11%` | `6,124,000,000.00` |
| `Live` | `Short` | `1470.50` | 6,250,000.00 USD | 14,460.00 USD | 0.00 USD | `+97.12%` | `9,836,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `300.50` | 1,690,000.00 USD | 0.00 USD | 2,400.00 USD | `-59.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 1,680,000.00 USD | 0.00 USD | 333.50 USD | `-55.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `350.50` | 1,680,000.00 USD | 0.00 USD | 127.58 USD | `-53.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 1,680,000.00 USD | 0.00 USD | 5,170.00 USD | `-50.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 1,680,000.00 USD | 0.00 USD | 25,210.00 USD | `-44.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 1,650,000.00 USD | 0.00 USD | 4,550.00 USD | `-44.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 1,650,000.00 USD | 0.00 USD | 698.74 USD | `-38.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 1,650,000.00 USD | 0.00 USD | 3,550.00 USD | `-37.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 1,640,000.00 USD | 0.00 USD | 6,600.00 USD | `-34.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 1,640,000.00 USD | 0.00 USD | 214.78 USD | `-33.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 1,640,000.00 USD | 0.00 USD | 168.67 USD | `-32.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 1,640,000.00 USD | 0.00 USD | 47,830.00 USD | `-32.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 1,590,000.00 USD | 0.00 USD | 185.97 USD | `-31.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 1,590,000.00 USD | 0.00 USD | 1,030.00 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 1,590,000.00 USD | 0.00 USD | 125.51 USD | `-30.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 1,590,000.00 USD | 0.00 USD | 280.49 USD | `-30.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 1,590,000.00 USD | 0.00 USD | 258.14 USD | `-30.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 1,590,000.00 USD | 0.00 USD | 485.16 USD | `-29.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 1,590,000.00 USD | 0.00 USD | 4,650.00 USD | `-28.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 1,580,000.00 USD | 0.00 USD | 1,680.00 USD | `-27.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 1,580,000.00 USD | 0.00 USD | 864.80 USD | `-27.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 1,580,000.00 USD | 0.00 USD | 1,190.00 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 1,580,000.00 USD | 0.00 USD | 1,220.00 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 1,580,000.00 USD | 0.00 USD | 297.12 USD | `-25.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 1,580,000.00 USD | 0.00 USD | 748.48 USD | `-24.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 1,580,000.00 USD | 0.00 USD | 566.50 USD | `-24.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 1,580,000.00 USD | 0.00 USD | 126.55 USD | `-23.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 1,580,000.00 USD | 0.00 USD | 5,680.00 USD | `-23.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 1,570,000.00 USD | 0.00 USD | 4,760.00 USD | `-23.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 1,560,000.00 USD | 0.00 USD | 1,700.00 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 1,560,000.00 USD | 0.00 USD | 291.91 USD | `-23.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 1,560,000.00 USD | 0.00 USD | 469.61 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 1,560,000.00 USD | 0.00 USD | 289.98 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 1,560,000.00 USD | 0.00 USD | 285.86 USD | `-22.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 1,560,000.00 USD | 0.00 USD | 289.17 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 1,560,000.00 USD | 0.00 USD | 657.71 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 1,560,000.00 USD | 0.00 USD | 289.59 USD | `-22.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 1,560,000.00 USD | 0.00 USD | 287.67 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 1,560,000.00 USD | 0.00 USD | 288.74 USD | `-21.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 1,560,000.00 USD | 0.00 USD | 1,090.00 USD | `-21.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 1,560,000.00 USD | 0.00 USD | 34,020.00 USD | `-21.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 1,520,000.00 USD | 0.00 USD | 289.05 USD | `-21.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 1,520,000.00 USD | 0.00 USD | 287.78 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,520,000.00 USD | 0.00 USD | 7,990.00 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,520,000.00 USD | 0.00 USD | 540.31 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 1,520,000.00 USD | 0.00 USD | 282.74 USD | `-20.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,520,000.00 USD | 0.00 USD | 170.05 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `594.50` | 1,520,000.00 USD | 0.00 USD | 286.55 USD | `-20.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,510,000.00 USD | 0.00 USD | 244.79 USD | `-19.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,510,000.00 USD | 0.00 USD | 3,760.00 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,510,000.00 USD | 0.00 USD | 102.43 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,510,000.00 USD | 0.00 USD | 102.77 USD | `-18.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,510,000.00 USD | 0.00 USD | 2,610.00 USD | `-18.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `606.50` | 1,510,000.00 USD | 0.00 USD | 103.11 USD | `-18.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,510,000.00 USD | 0.00 USD | 170.00 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 1,510,000.00 USD | 0.00 USD | 1,380.00 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,510,000.00 USD | 0.00 USD | 269.15 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,510,000.00 USD | 0.00 USD | 1,740.00 USD | `-17.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,500,000.00 USD | 0.00 USD | 120.83 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,500,000.00 USD | 0.00 USD | 105.49 USD | `-16.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,500,000.00 USD | 0.00 USD | 170.76 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,500,000.00 USD | 0.00 USD | 276.16 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,500,000.00 USD | 0.00 USD | 4,570.00 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 1,500,000.00 USD | 0.00 USD | 2,550.00 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,500,000.00 USD | 0.00 USD | 560.60 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,500,000.00 USD | 0.00 USD | 154.27 USD | `-13.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,500,000.00 USD | 0.00 USD | 971.04 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,490,000.00 USD | 0.00 USD | 1,610.00 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,490,000.00 USD | 0.00 USD | 14,000.00 USD | `-12.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,480,000.00 USD | 0.00 USD | 2,090.00 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,480,000.00 USD | 0.00 USD | 2,020.00 USD | `-12.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,480,000.00 USD | 0.00 USD | 308.92 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,470,000.00 USD | 0.00 USD | 129.33 USD | `-11.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,470,000.00 USD | 0.00 USD | 110.46 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,470,000.00 USD | 0.00 USD | 17,600.00 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,460,000.00 USD | 0.00 USD | 198.15 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,460,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,460,000.00 USD | 0.00 USD | 4,920.00 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,450,000.00 USD | 0.00 USD | 707.66 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,450,000.00 USD | 0.00 USD | 3,360.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 1,450,000.00 USD | 0.00 USD | 245.46 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 1,450,000.00 USD | 0.00 USD | 2,090.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 1,440,000.00 USD | 0.00 USD | 825.59 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 1,440,000.00 USD | 0.00 USD | 1,760.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 1,440,000.00 USD | 0.00 USD | 63,000.00 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 1,380,000.00 USD | 0.00 USD | 3,360.00 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 1,370,000.00 USD | 0.00 USD | 175.31 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 1,370,000.00 USD | 0.00 USD | 2,370.00 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 1,370,000.00 USD | 0.00 USD | 31,240.00 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,340,000.00 USD | 0.00 USD | 24,240.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 1,320,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 1,320,000.00 USD | 0.00 USD | 7,610.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 1,310,000.00 USD | 0.00 USD | 371.25 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 1,310,000.00 USD | 0.00 USD | 610.01 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 1,310,000.00 USD | 0.00 USD | 2,590.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 1,300,000.00 USD | 0.00 USD | 2,230.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 1,300,000.00 USD | 0.00 USD | 108.57 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 1,300,000.00 USD | 0.00 USD | 2,530.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 1,300,000.00 USD | 0.00 USD | 4,560.00 USD | `-7.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 1,290,000.00 USD | 0.00 USD | 374.34 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 1,290,000.00 USD | 0.00 USD | 30,340.00 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 1,260,000.00 USD | 0.00 USD | 9,690.00 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 1,250,000.00 USD | 0.00 USD | 4,340.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 1,250,000.00 USD | 0.00 USD | 5,000.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 1,250,000.00 USD | 0.00 USD | 3,300.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 1,240,000.00 USD | 0.00 USD | 199,470.00 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,040,000.00 USD | 0.00 USD | 3,900.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 1,040,000.00 USD | 0.00 USD | 1,790.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 1,040,000.00 USD | 0.00 USD | 2,790.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 1,030,000.00 USD | 0.00 USD | 1,070.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 1,030,000.00 USD | 0.00 USD | 2,770.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 1,030,000.00 USD | 0.00 USD | 11,860.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 1,020,000.00 USD | 0.00 USD | 205.88 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 1,020,000.00 USD | 0.00 USD | 1,070.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 1,020,000.00 USD | 0.00 USD | 783.29 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 1,020,000.00 USD | 0.00 USD | 315.46 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 1,020,000.00 USD | 0.00 USD | 402.00 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 1,020,000.00 USD | 0.00 USD | 2,870.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 1,010,000.00 USD | 0.00 USD | 94,480.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 917,980.00 USD | 0.00 USD | 2,000.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 915,980.00 USD | 0.00 USD | 6,400.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 909,580.00 USD | 0.00 USD | 1,470.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `717.50` | 908,110.00 USD | 0.00 USD | 362.34 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `718.50` | 907,750.00 USD | 0.00 USD | 727.84 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `719.50` | 907,020.00 USD | 0.00 USD | 1,270.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `720.50` | 905,750.00 USD | 0.00 USD | 2,710.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `721.50` | 903,040.00 USD | 0.00 USD | 6,780.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `722.50` | 896,260.00 USD | 0.00 USD | 114.16 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `723.50` | 896,140.00 USD | 0.00 USD | 605.57 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `724.50` | 895,540.00 USD | 0.00 USD | 9,620.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.50` | 885,920.00 USD | 0.00 USD | 6,440.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `726.50` | 879,480.00 USD | 0.00 USD | 470.77 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `727.50` | 879,010.00 USD | 0.00 USD | 1,650.00 USD | `-2.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `728.50` | 877,360.00 USD | 0.00 USD | 4,250.00 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `729.50` | 873,110.00 USD | 0.00 USD | 8,340.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `730.50` | 864,770.00 USD | 0.00 USD | 1,640.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `731.50` | 863,130.00 USD | 0.00 USD | 581,920.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `732.50` | 281,210.00 USD | 0.00 USD | 1,600.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `733.50` | 279,610.00 USD | 0.00 USD | 2,100.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `734.50` | 277,510.00 USD | 0.00 USD | 489.18 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `735.50` | 277,020.00 USD | 0.00 USD | 1,820.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `736.50` | 275,200.00 USD | 0.00 USD | 5,760.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `737.50` | 269,440.00 USD | 0.00 USD | 4,950.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `738.50` | 264,490.00 USD | 0.00 USD | 3,000.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `739.50` | 261,500.00 USD | 0.00 USD | 2,460.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `740.50` | 259,040.00 USD | 0.00 USD | 1,590.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `741.50` | 257,450.00 USD | 0.00 USD | 6,240.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `742.50` | 251,200.00 USD | 0.00 USD | 247,900.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `743.50` | 3,300.00 USD | 0.00 USD | 897.40 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `744.50` | 2,400.00 USD | 0.00 USD | 1,400.00 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `745.50` | 1,000.00 USD | 0.00 USD | 1,000.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,250.00 USD | 1,250.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,550.00 USD | 301.24 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 15,880.00 USD | 14,330.00 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 40,890.00 USD | 25,010.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 42,020.00 USD | 1,130.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 43,920.00 USD | 1,900.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 46,650.00 USD | 2,730.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 47,660.00 USD | 1,010.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 48,180.00 USD | 525.13 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 48,290.00 USD | 107.28 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 56,540.00 USD | 8,250.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 58,410.00 USD | 1,880.00 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 64,920.00 USD | 6,500.00 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 65,170.00 USD | 253.67 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 65,680.00 USD | 511.82 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 68,600.00 USD | 2,920.00 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 71,210.00 USD | 2,610.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 282,960.00 USD | 211,750.00 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 289,350.00 USD | 6,390.00 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 368,200.00 USD | 78,840.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 368,530.00 USD | 331.13 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 369,890.00 USD | 1,360.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 371,120.00 USD | 1,230.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 371,630.00 USD | 504.02 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 603,010.00 USD | 231,390.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 604,390.00 USD | 1,370.00 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 614,060.00 USD | 9,670.00 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 615,300.00 USD | 1,240.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 624,980.00 USD | 9,680.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 627,060.00 USD | 2,080.00 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 640,790.00 USD | 13,730.00 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 644,890.00 USD | 4,100.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 650,370.00 USD | 5,470.00 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 656,780.00 USD | 6,420.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 658,630.00 USD | 1,840.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 674,500.00 USD | 15,870.00 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 677,700.00 USD | 3,200.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 1,090,000.00 USD | 407,870.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 1,090,000.00 USD | 106.69 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 1,090,000.00 USD | 292.21 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 1,090,000.00 USD | 366.51 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 1,090,000.00 USD | 393.75 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 1,090,000.00 USD | 133.26 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 1,090,000.00 USD | 1,150.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 1,090,000.00 USD | 704.44 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 1,090,000.00 USD | 4,160.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 1,090,000.00 USD | 1,450.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 1,100,000.00 USD | 3,730.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 1,100,000.00 USD | 3,040.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 1,100,000.00 USD | 154.52 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `797.50` | 1,100,000.00 USD | 2,120.00 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 1,110,000.00 USD | 2,590.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 1,140,000.00 USD | 36,970.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 1,140,000.00 USD | 803.50 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 1,140,000.00 USD | 179.63 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 1,150,000.00 USD | 3,860.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 1,150,000.00 USD | 3,190.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 1,150,000.00 USD | 868.59 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 1,170,000.00 USD | 15,790.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 1,170,000.00 USD | 374.10 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 1,170,000.00 USD | 6,080.00 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 1,170,000.00 USD | 109.82 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 1,180,000.00 USD | 3,210.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 1,180,000.00 USD | 2,610.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 1,180,000.00 USD | 162.68 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 1,190,000.00 USD | 7,000.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 1,190,000.00 USD | 408.13 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `825.50` | 1,520,000.00 USD | 330,200.00 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 1,520,000.00 USD | 672.77 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 1,520,000.00 USD | 276.38 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 1,520,000.00 USD | 5,780.00 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 1,530,000.00 USD | 493.32 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 1,530,000.00 USD | 3,270.00 USD | 0.00 USD | `+11.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 1,530,000.00 USD | 187.15 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 1,530,000.00 USD | 372.24 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 1,530,000.00 USD | 326.62 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 1,530,000.00 USD | 296.34 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 1,530,000.00 USD | 441.26 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 1,530,000.00 USD | 329.87 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 1,530,000.00 USD | 425.97 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 1,540,000.00 USD | 7,860.00 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 1,540,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 1,550,000.00 USD | 11,650.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 1,550,000.00 USD | 102.30 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 1,550,000.00 USD | 137.57 USD | 0.00 USD | `+14.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 1,560,000.00 USD | 13,180.00 USD | 0.00 USD | `+14.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 1,570,000.00 USD | 551.58 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 1,570,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 1,570,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 1,570,000.00 USD | 2,970.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 1,570,000.00 USD | 3,460.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 1,580,000.00 USD | 2,610.00 USD | 0.00 USD | `+16.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 1,580,000.00 USD | 228.07 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 1,580,000.00 USD | 1,110.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `874.50` | 1,580,000.00 USD | 582.42 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 1,630,000.00 USD | 54,820.00 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 1,630,000.00 USD | 266.55 USD | 0.00 USD | `+19.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 1,630,000.00 USD | 690.14 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 1,640,000.00 USD | 605.33 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 1,690,000.00 USD | 55,500.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 1,690,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 1,700,000.00 USD | 533.99 USD | 0.00 USD | `+22.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 1,700,000.00 USD | 166.43 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 1,700,000.00 USD | 463.01 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 1,700,000.00 USD | 321.50 USD | 0.00 USD | `+24.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `929.50` | 1,720,000.00 USD | 24,800.00 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 1,720,000.00 USD | 552.72 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 1,720,000.00 USD | 196.03 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 1,720,000.00 USD | 287.20 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 1,720,000.00 USD | 782.14 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 1,720,000.00 USD | 498.94 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 1,730,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 1,730,000.00 USD | 293.25 USD | 0.00 USD | `+31.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 1,730,000.00 USD | 1,300.00 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 1,730,000.00 USD | 109.93 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 1,730,000.00 USD | 439.09 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 1,730,000.00 USD | 2,590.00 USD | 0.00 USD | `+32.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 1,730,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 1,740,000.00 USD | 3,990.00 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 1,740,000.00 USD | 938.53 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 1,750,000.00 USD | 12,810.00 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 1,750,000.00 USD | 203.50 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 1,750,000.00 USD | 195.51 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 1,750,000.00 USD | 278.43 USD | 0.00 USD | `+47.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 1,750,000.00 USD | 555.75 USD | 0.00 USD | `+49.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 1,810,000.00 USD | 62,330.00 USD | 0.00 USD | `+60.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 1,810,000.00 USD | 1,250.00 USD | 0.00 USD | `+61.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1223.50` | 1,810,000.00 USD | 424.55 USD | 0.00 USD | `+64.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 1,810,000.00 USD | 235.49 USD | 0.00 USD | `+64.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 1,820,000.00 USD | 3,580.00 USD | 0.00 USD | `+64.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 1,820,000.00 USD | 421.42 USD | 0.00 USD | `+67.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 1,820,000.00 USD | 3,750.00 USD | 0.00 USD | `+71.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 1,820,000.00 USD | 133.64 USD | 0.00 USD | `+73.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 1,820,000.00 USD | 685.36 USD | 0.00 USD | `+74.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 1,850,000.00 USD | 24,400.00 USD | 0.00 USD | `+78.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 1,880,000.00 USD | 33,950.00 USD | 0.00 USD | `+79.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 1,890,000.00 USD | 6,210.00 USD | 0.00 USD | `+82.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 1,890,000.00 USD | 349.06 USD | 0.00 USD | `+82.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 1,890,000.00 USD | 1,060.00 USD | 0.00 USD | `+83.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 1,910,000.00 USD | 19,210.00 USD | 0.00 USD | `+83.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 1,910,000.00 USD | 2,150.00 USD | 0.00 USD | `+87.74%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `664.10` | 88,580,000.00 USD | 0.00 USD | 88,580,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `7D` | `665.00` | 88,440,000.00 USD | 0.00 USD | 88,440,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `7D` | `665.90` | 88,290,000.00 USD | 0.00 USD | 88,290,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `7D` | `666.80` | 87,890,000.00 USD | 0.00 USD | 87,890,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `7D` | `667.70` | 87,600,000.00 USD | 0.00 USD | 87,600,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `7D` | `668.60` | 87,300,000.00 USD | 0.00 USD | 87,300,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `668.80` | 33,230,000.00 USD | 0.00 USD | 33,230,000.00 USD | 90,000.00 USD | 25,520.00 USD | 3,620.00 USD |
| `7D` | `669.50` | 86,770,000.00 USD | 0.00 USD | 86,770,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `669.60` | 33,110,000.00 USD | 0.00 USD | 33,110,000.00 USD | 174,750.00 USD | 2,750.00 USD | 9,560.00 USD |
| `1D` | `670.40` | 32,920,000.00 USD | 0.00 USD | 32,920,000.00 USD | 4,950.00 USD | 0.00 USD | 2,620.00 USD |
| `7D` | `670.40` | 86,280,000.00 USD | 0.00 USD | 86,280,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.20` | 32,910,000.00 USD | 0.00 USD | 32,910,000.00 USD | 23,150.00 USD | 11,440.00 USD | 16,650.00 USD |
| `7D` | `671.30` | 85,790,000.00 USD | 0.00 USD | 85,790,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `672.00` | 32,860,000.00 USD | 0.00 USD | 32,860,000.00 USD | 37,530.00 USD | 8,400.00 USD | 26,940.00 USD |
| `7D` | `672.20` | 85,360,000.00 USD | 0.00 USD | 85,360,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.80` | 32,790,000.00 USD | 0.00 USD | 32,790,000.00 USD | 178,400.00 USD | 30,880.00 USD | 6,810.00 USD |
| `7D` | `673.10` | 85,040,000.00 USD | 0.00 USD | 85,040,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.60` | 32,570,000.00 USD | 0.00 USD | 32,570,000.00 USD | 277,730.00 USD | 22,910.00 USD | 28,520.00 USD |
| `7D` | `674.00` | 84,540,000.00 USD | 0.00 USD | 84,540,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.40` | 32,240,000.00 USD | 0.00 USD | 32,240,000.00 USD | 162,550.00 USD | 24,950.00 USD | 39,360.00 USD |
| `7D` | `674.90` | 84,010,000.00 USD | 0.00 USD | 84,010,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.20` | 32,020,000.00 USD | 0.00 USD | 32,020,000.00 USD | 34,970.00 USD | 26,950.00 USD | 2,660.00 USD |
| `7D` | `675.80` | 83,690,000.00 USD | 0.00 USD | 83,690,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.00` | 31,950,000.00 USD | 0.00 USD | 31,950,000.00 USD | 135,000.00 USD | 40,110.00 USD | 62,410.00 USD |
| `7D` | `676.70` | 83,200,000.00 USD | 0.00 USD | 83,200,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `676.80` | 31,710,000.00 USD | 0.00 USD | 31,710,000.00 USD | 306,990.00 USD | 9,980.00 USD | 46,920.00 USD |
| `1D` | `677.60` | 31,350,000.00 USD | 0.00 USD | 31,350,000.00 USD | 268,760.00 USD | 21,630.00 USD | 54,220.00 USD |
| `7D` | `677.60` | 82,530,000.00 USD | 0.00 USD | 82,530,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.40` | 31,000,000.00 USD | 0.00 USD | 31,000,000.00 USD | 72,550.00 USD | 8,360.00 USD | 14,100.00 USD |
| `7D` | `678.50` | 82,050,000.00 USD | 0.00 USD | 82,050,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.20` | 30,910,000.00 USD | 0.00 USD | 30,910,000.00 USD | 108,560.00 USD | 5,470.00 USD | 7,840.00 USD |
| `7D` | `679.40` | 81,910,000.00 USD | 0.00 USD | 81,910,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `680.00` | 30,790,000.00 USD | 0.00 USD | 30,790,000.00 USD | 54,410.00 USD | 16,810.00 USD | 11,780.00 USD |
| `7D` | `680.30` | 81,740,000.00 USD | 0.00 USD | 81,740,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.80` | 30,700,000.00 USD | 0.00 USD | 30,700,000.00 USD | 64,130.00 USD | 5,770.00 USD | 12,510.00 USD |
| `7D` | `681.20` | 81,560,000.00 USD | 0.00 USD | 81,560,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.60` | 30,620,000.00 USD | 0.00 USD | 30,620,000.00 USD | 73,000.00 USD | 11,810.00 USD | 0.00 USD |
| `7D` | `682.10` | 81,410,000.00 USD | 0.00 USD | 81,410,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.40` | 30,540,000.00 USD | 0.00 USD | 30,540,000.00 USD | 34,900.00 USD | 9,220.00 USD | 46,000.00 USD |
| `7D` | `683.00` | 81,360,000.00 USD | 0.00 USD | 81,360,000.00 USD | 181,220.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.20` | 30,450,000.00 USD | 0.00 USD | 30,450,000.00 USD | 106,980.00 USD | 13,040.00 USD | 7,870.00 USD |
| `7D` | `683.90` | 81,140,000.00 USD | 0.00 USD | 81,140,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.00` | 30,320,000.00 USD | 0.00 USD | 30,320,000.00 USD | 7,750.00 USD | 12,720.00 USD | 2,140.00 USD |
| `1D` | `684.80` | 30,300,000.00 USD | 0.00 USD | 30,300,000.00 USD | 42,390.00 USD | 2,630.00 USD | 3,410.00 USD |
| `7D` | `684.80` | 81,010,000.00 USD | 0.00 USD | 81,010,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.60` | 30,250,000.00 USD | 0.00 USD | 30,250,000.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `685.70` | 80,720,000.00 USD | 0.00 USD | 80,720,000.00 USD | 199,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 80,520,000.00 USD | 0.00 USD | 80,520,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `687.50` | 80,460,000.00 USD | 0.00 USD | 80,460,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `688.40` | 80,310,000.00 USD | 0.00 USD | 80,310,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.80` | 30,230,000.00 USD | 0.00 USD | 30,230,000.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `689.30` | 80,240,000.00 USD | 0.00 USD | 80,240,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.60` | 30,220,000.00 USD | 0.00 USD | 30,220,000.00 USD | 11,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `690.20` | 80,150,000.00 USD | 0.00 USD | 80,150,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.40` | 30,210,000.00 USD | 0.00 USD | 30,210,000.00 USD | 86,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `691.10` | 79,720,000.00 USD | 0.00 USD | 79,720,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.20` | 30,130,000.00 USD | 0.00 USD | 30,130,000.00 USD | 27,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `692.00` | 30,100,000.00 USD | 0.00 USD | 30,100,000.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 79,220,000.00 USD | 0.00 USD | 79,220,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `1D` | `692.80` | 30,020,000.00 USD | 0.00 USD | 30,020,000.00 USD | 46,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.90` | 78,820,000.00 USD | 0.00 USD | 78,820,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.60` | 29,980,000.00 USD | 0.00 USD | 29,980,000.00 USD | 36,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `693.80` | 78,520,000.00 USD | 0.00 USD | 78,520,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.40` | 29,940,000.00 USD | 0.00 USD | 29,940,000.00 USD | 10,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `694.70` | 78,180,000.00 USD | 0.00 USD | 78,180,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.20` | 29,930,000.00 USD | 0.00 USD | 29,930,000.00 USD | 25,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `695.60` | 77,820,000.00 USD | 0.00 USD | 77,820,000.00 USD | 127,500.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `696.00` | 29,900,000.00 USD | 0.00 USD | 29,900,000.00 USD | 40,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `696.50` | 77,670,000.00 USD | 0.00 USD | 77,670,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `696.80` | 29,860,000.00 USD | 0.00 USD | 29,860,000.00 USD | 28,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 77,530,000.00 USD | 0.00 USD | 77,530,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `1D` | `697.60` | 29,830,000.00 USD | 0.00 USD | 29,830,000.00 USD | 69,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `698.30` | 77,330,000.00 USD | 0.00 USD | 77,330,000.00 USD | 277,440.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `698.40` | 29,760,000.00 USD | 0.00 USD | 29,760,000.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `699.20` | 29,740,000.00 USD | 0.00 USD | 29,740,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `699.20` | 76,960,000.00 USD | 0.00 USD | 76,960,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `1D` | `700.00` | 29,720,000.00 USD | 0.00 USD | 29,720,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `700.10` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.80` | 29,710,000.00 USD | 0.00 USD | 29,710,000.00 USD | 22,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 76,370,000.00 USD | 0.00 USD | 76,370,000.00 USD | 237,800.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `701.60` | 29,690,000.00 USD | 0.00 USD | 29,690,000.00 USD | 37,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 76,110,000.00 USD | 0.00 USD | 76,110,000.00 USD | 225,720.00 USD | 66,060.00 USD | 103,830.00 USD |
| `1D` | `702.40` | 29,650,000.00 USD | 0.00 USD | 29,650,000.00 USD | 64,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `702.80` | 75,720,000.00 USD | 0.00 USD | 75,720,000.00 USD | 416,820.00 USD | 74,570.00 USD | 36,720.00 USD |
| `1D` | `703.20` | 29,590,000.00 USD | 0.00 USD | 29,590,000.00 USD | 82,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 75,190,000.00 USD | 0.00 USD | 75,190,000.00 USD | 354,550.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `704.00` | 29,500,000.00 USD | 0.00 USD | 29,500,000.00 USD | 62,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `704.60` | 74,790,000.00 USD | 0.00 USD | 74,790,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `704.80` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 92,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.50` | 73,920,000.00 USD | 0.00 USD | 73,920,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `705.60` | 29,350,000.00 USD | 0.00 USD | 29,350,000.00 USD | 87,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `706.40` | 29,260,000.00 USD | 0.00 USD | 29,260,000.00 USD | 45,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `706.40` | 72,600,000.00 USD | 0.00 USD | 72,600,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `1D` | `707.20` | 29,220,000.00 USD | 0.00 USD | 29,220,000.00 USD | 39,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `707.30` | 71,740,000.00 USD | 0.00 USD | 71,740,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `708.00` | 29,180,000.00 USD | 0.00 USD | 29,180,000.00 USD | 40,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 70,990,000.00 USD | 0.00 USD | 70,990,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.80` | 29,140,000.00 USD | 0.00 USD | 29,140,000.00 USD | 41,140.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `709.10` | 70,020,000.00 USD | 0.00 USD | 70,020,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `1D` | `709.60` | 29,090,000.00 USD | 0.00 USD | 29,090,000.00 USD | 50,110.00 USD | 25,300.00 USD | 13,540.00 USD |
| `7D` | `710.00` | 69,270,000.00 USD | 0.00 USD | 69,270,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `1D` | `710.40` | 29,000,000.00 USD | 0.00 USD | 29,000,000.00 USD | 80,960.00 USD | 34,370.00 USD | 18,560.00 USD |
| `7D` | `710.90` | 68,480,000.00 USD | 0.00 USD | 68,480,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.20` | 28,870,000.00 USD | 0.00 USD | 28,870,000.00 USD | 102,220.00 USD | 66,110.00 USD | 9,890.00 USD |
| `7D` | `711.80` | 67,160,000.00 USD | 0.00 USD | 67,160,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `712.00` | 28,690,000.00 USD | 0.00 USD | 28,690,000.00 USD | 220,260.00 USD | 12,480.00 USD | 27,340.00 USD |
| `7D` | `712.70` | 66,200,000.00 USD | 0.00 USD | 66,200,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `1D` | `712.80` | 28,430,000.00 USD | 0.00 USD | 28,430,000.00 USD | 87,830.00 USD | 52,940.00 USD | 36,760.00 USD |
| `1D` | `713.60` | 28,250,000.00 USD | 0.00 USD | 28,250,000.00 USD | 270,780.00 USD | 25,400.00 USD | 0.00 USD |
| `7D` | `713.60` | 64,560,000.00 USD | 0.00 USD | 64,560,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `1D` | `714.40` | 27,950,000.00 USD | 0.00 USD | 27,950,000.00 USD | 457,280.00 USD | 11,780.00 USD | 23,910.00 USD |
| `7D` | `714.50` | 61,710,000.00 USD | 0.00 USD | 61,710,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `715.20` | 27,460,000.00 USD | 0.00 USD | 27,460,000.00 USD | 30,300.00 USD | 4,930.00 USD | 10,060.00 USD |
| `7D` | `715.40` | 60,700,000.00 USD | 0.00 USD | 60,700,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `716.00` | 27,420,000.00 USD | 0.00 USD | 27,420,000.00 USD | 82,490.00 USD | 28,610.00 USD | 56,780.00 USD |
| `7D` | `716.30` | 58,900,000.00 USD | 0.00 USD | 58,900,000.00 USD | 1,260,000.00 USD | 374,150.00 USD | 294,850.00 USD |
| `1D` | `716.80` | 27,250,000.00 USD | 0.00 USD | 27,250,000.00 USD | 88,230.00 USD | 34,460.00 USD | 75,150.00 USD |
| `7D` | `717.20` | 56,970,000.00 USD | 0.00 USD | 56,970,000.00 USD | 581,610.00 USD | 408,260.00 USD | 387,120.00 USD |
| `1D` | `717.60` | 27,050,000.00 USD | 0.00 USD | 27,050,000.00 USD | 182,250.00 USD | 92,300.00 USD | 40,480.00 USD |
| `7D` | `718.10` | 55,590,000.00 USD | 0.00 USD | 55,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.40` | 26,740,000.00 USD | 0.00 USD | 26,740,000.00 USD | 1,030,000.00 USD | 83,070.00 USD | 140,120.00 USD |
| `7D` | `719.00` | 53,510,000.00 USD | 0.00 USD | 53,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.20` | 25,480,000.00 USD | 0.00 USD | 25,480,000.00 USD | 841,130.00 USD | 76,100.00 USD | 145,890.00 USD |
| `7D` | `719.90` | 52,490,000.00 USD | 0.00 USD | 52,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.00` | 24,420,000.00 USD | 0.00 USD | 24,420,000.00 USD | 242,550.00 USD | 76,740.00 USD | 49,760.00 USD |
| `1D` | `720.80` | 24,050,000.00 USD | 0.00 USD | 24,050,000.00 USD | 436,810.00 USD | 59,550.00 USD | 116,790.00 USD |
| `7D` | `720.80` | 51,510,000.00 USD | 0.00 USD | 51,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.60` | 23,440,000.00 USD | 0.00 USD | 23,440,000.00 USD | 768,050.00 USD | 111,750.00 USD | 185,000.00 USD |
| `7D` | `721.70` | 50,260,000.00 USD | 0.00 USD | 50,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.40` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 882,710.00 USD | 68,190.00 USD | 135,150.00 USD |
| `7D` | `722.60` | 47,430,000.00 USD | 0.00 USD | 47,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.20` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 598,960.00 USD | 29,990.00 USD | 99,370.00 USD |
| `7D` | `723.50` | 45,160,000.00 USD | 0.00 USD | 45,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `724.00` | 20,560,000.00 USD | 0.00 USD | 20,560,000.00 USD | 173,380.00 USD | 75,600.00 USD | 72,570.00 USD |
| `7D` | `724.40` | 44,080,000.00 USD | 0.00 USD | 44,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.80` | 20,230,000.00 USD | 0.00 USD | 20,230,000.00 USD | 278,640.00 USD | 59,020.00 USD | 23,020.00 USD |
| `7D` | `725.30` | 43,100,000.00 USD | 0.00 USD | 43,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.60` | 19,870,000.00 USD | 0.00 USD | 19,870,000.00 USD | 345,570.00 USD | 161,610.00 USD | 80,370.00 USD |
| `7D` | `726.20` | 40,520,000.00 USD | 0.00 USD | 40,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.40` | 19,290,000.00 USD | 0.00 USD | 19,290,000.00 USD | 549,370.00 USD | 101,750.00 USD | 80,490.00 USD |
| `7D` | `727.10` | 38,690,000.00 USD | 0.00 USD | 38,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.20` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 337,570.00 USD | 51,580.00 USD | 94,360.00 USD |
| `1D` | `728.00` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 375,010.00 USD | 195,850.00 USD | 134,480.00 USD |
| `7D` | `728.00` | 36,890,000.00 USD | 0.00 USD | 36,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.80` | 17,370,000.00 USD | 0.00 USD | 17,370,000.00 USD | 712,610.00 USD | 36,560.00 USD | 69,610.00 USD |
| `7D` | `728.90` | 32,610,000.00 USD | 0.00 USD | 32,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.60` | 16,550,000.00 USD | 0.00 USD | 16,550,000.00 USD | 935,470.00 USD | 59,850.00 USD | 8,130.00 USD |
| `7D` | `729.80` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.40` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 206,790.00 USD | 74,990.00 USD | 55,280.00 USD |
| `7D` | `730.70` | 27,220,000.00 USD | 0.00 USD | 27,220,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.20` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 133,240.00 USD | 54,800.00 USD | 97,410.00 USD |
| `7D` | `731.60` | 23,530,000.00 USD | 0.00 USD | 23,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `732.00` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 350,450.00 USD | 29,450.00 USD | 164,070.00 USD |
| `7D` | `732.50` | 21,610,000.00 USD | 0.00 USD | 21,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.80` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 1,620,000.00 USD | 214,840.00 USD | 248,660.00 USD |
| `7D` | `733.40` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.60` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 1,010,000.00 USD | 150,840.00 USD | 111,740.00 USD |
| `7D` | `734.30` | 18,420,000.00 USD | 0.00 USD | 18,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `734.40` | 11,030,000.00 USD | 0.00 USD | 11,030,000.00 USD | 1,330,000.00 USD | 177,890.00 USD | 290,510.00 USD |
| `1D` | `735.20` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 492,320.00 USD | 153,380.00 USD | 86,360.00 USD |
| `7D` | `735.20` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `736.00` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 705,930.00 USD | 145,250.00 USD | 303,090.00 USD |
| `7D` | `736.10` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.80` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 1,750,000.00 USD | 156,820.00 USD | 291,460.00 USD |
| `7D` | `737.00` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.60` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 1,870,000.00 USD | 184,910.00 USD | 344,460.00 USD |
| `7D` | `737.90` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.40` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,090,000.00 USD | 41,800.00 USD | 84,100.00 USD |
| `7D` | `738.80` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.20` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 252,270.00 USD | 0.00 USD | 78,820.00 USD |
| `7D` | `739.70` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.00` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 684,330.00 USD | 0.00 USD | 26,690.00 USD |
| `7D` | `740.60` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `740.80` | 485,750.00 USD | 0.00 USD | 485,750.00 USD | 239,830.00 USD | 0.00 USD | 7,010.00 USD |
| `7D` | `741.50` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `741.60` | 238,900.00 USD | 0.00 USD | 238,900.00 USD | 84,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `742.40` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `743.20` | 154,230.00 USD | 0.00 USD | 154,230.00 USD | 0.00 USD | 0.00 USD | 113,120.00 USD |
| `7D` | `743.30` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `744.00` | 41,100.00 USD | 0.00 USD | 41,100.00 USD | 0.00 USD | 0.00 USD | 11,470.00 USD |
| `7D` | `744.20` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.80` | 29,640.00 USD | 0.00 USD | 29,640.00 USD | 0.00 USD | 29,640.00 USD | 0.00 USD |
| `1D` | `745.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `745.10` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.40` | 38,640.00 USD | 38,640.00 USD | 0.00 USD | 38,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.90` | 215,540.00 USD | 215,540.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `753.60` | 106,010.00 USD | 106,010.00 USD | 0.00 USD | 0.00 USD | 27,900.00 USD | 39,480.00 USD |
| `1D` | `754.40` | 142,300.00 USD | 142,300.00 USD | 0.00 USD | 0.00 USD | 36,290.00 USD | 0.00 USD |
| `7D` | `755.00` | 275,100.00 USD | 275,100.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.20` | 457,650.00 USD | 457,650.00 USD | 0.00 USD | 143,570.00 USD | 134,660.00 USD | 37,120.00 USD |
| `1D` | `756.00` | 905,630.00 USD | 905,630.00 USD | 0.00 USD | 312,560.00 USD | 69,210.00 USD | 66,220.00 USD |
| `1D` | `756.80` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 110,260.00 USD | 8,490.00 USD | 49,060.00 USD |
| `7D` | `756.80` | 322,440.00 USD | 322,440.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.60` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 147,620.00 USD | 146,640.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 911,190.00 USD | 911,190.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.40` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 469,360.00 USD | 10,040.00 USD | 0.00 USD |
| `7D` | `758.60` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.20` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 813,190.00 USD | 23,550.00 USD | 47,820.00 USD |
| `1D` | `760.00` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 19,140.00 USD | 32,160.00 USD | 33,360.00 USD |
| `7D` | `760.40` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.80` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 161,650.00 USD | 34,930.00 USD | 110,800.00 USD |
| `7D` | `761.30` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 10,750.00 USD | 223,950.00 USD | 100,630.00 USD |
| `1D` | `761.60` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 157,660.00 USD | 68,930.00 USD | 139,810.00 USD |
| `7D` | `762.20` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.40` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 267,050.00 USD | 140,440.00 USD | 80,970.00 USD |
| `7D` | `763.10` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.20` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 2,110,000.00 USD | 210,290.00 USD | 256,160.00 USD |
| `1D` | `764.00` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 1,190,000.00 USD | 152,200.00 USD | 203,940.00 USD |
| `7D` | `764.00` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.80` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 863,310.00 USD | 126,110.00 USD | 189,680.00 USD |
| `7D` | `764.90` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.60` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 848,110.00 USD | 98,780.00 USD | 196,120.00 USD |
| `7D` | `765.80` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.40` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 456,170.00 USD | 257,560.00 USD | 416,300.00 USD |
| `7D` | `766.70` | 19,060,000.00 USD | 19,060,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.20` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 2,280,000.00 USD | 110,380.00 USD | 199,140.00 USD |
| `7D` | `767.60` | 22,450,000.00 USD | 22,450,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `768.00` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 1,330,000.00 USD | 88,170.00 USD | 241,790.00 USD |
| `7D` | `768.50` | 24,680,000.00 USD | 24,680,000.00 USD | 0.00 USD | 1,850,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.80` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 760,940.00 USD | 67,110.00 USD | 85,110.00 USD |
| `7D` | `769.40` | 25,830,000.00 USD | 25,830,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.60` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 591,420.00 USD | 99,410.00 USD | 79,730.00 USD |
| `7D` | `770.30` | 28,330,000.00 USD | 28,330,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `770.40` | 18,140,000.00 USD | 18,140,000.00 USD | 0.00 USD | 458,460.00 USD | 119,310.00 USD | 36,580.00 USD |
| `1D` | `771.20` | 18,770,000.00 USD | 18,770,000.00 USD | 0.00 USD | 454,480.00 USD | 71,930.00 USD | 109,720.00 USD |
| `7D` | `771.20` | 29,790,000.00 USD | 29,790,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `772.00` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 477,710.00 USD | 96,300.00 USD | 60,380.00 USD |
| `7D` | `772.10` | 32,210,000.00 USD | 32,210,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.80` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 388,540.00 USD | 120,040.00 USD | 159,060.00 USD |
| `7D` | `773.00` | 34,830,000.00 USD | 34,830,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.60` | 20,830,000.00 USD | 20,830,000.00 USD | 0.00 USD | 475,810.00 USD | 110,200.00 USD | 172,170.00 USD |
| `7D` | `773.90` | 36,620,000.00 USD | 36,620,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.40` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 1,070,000.00 USD | 53,050.00 USD | 42,250.00 USD |
| `7D` | `774.80` | 39,000,000.00 USD | 39,000,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.20` | 22,390,000.00 USD | 22,390,000.00 USD | 0.00 USD | 252,160.00 USD | 98,470.00 USD | 42,950.00 USD |
| `7D` | `775.70` | 41,490,000.00 USD | 41,490,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.00` | 22,840,000.00 USD | 22,840,000.00 USD | 0.00 USD | 316,920.00 USD | 73,850.00 USD | 59,620.00 USD |
| `7D` | `776.60` | 43,770,000.00 USD | 43,770,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `776.80` | 23,300,000.00 USD | 23,300,000.00 USD | 0.00 USD | 369,700.00 USD | 14,720.00 USD | 82,040.00 USD |
| `7D` | `777.50` | 45,510,000.00 USD | 45,510,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `777.60` | 24,020,000.00 USD | 24,020,000.00 USD | 0.00 USD | 527,350.00 USD | 104,660.00 USD | 85,040.00 USD |
| `1D` | `778.40` | 25,030,000.00 USD | 25,030,000.00 USD | 0.00 USD | 847,200.00 USD | 73,550.00 USD | 90,770.00 USD |
| `7D` | `778.40` | 47,200,000.00 USD | 47,200,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `779.20` | 25,960,000.00 USD | 25,960,000.00 USD | 0.00 USD | 713,740.00 USD | 73,260.00 USD | 138,550.00 USD |
| `7D` | `779.30` | 48,750,000.00 USD | 48,750,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `780.00` | 26,380,000.00 USD | 26,380,000.00 USD | 0.00 USD | 293,030.00 USD | 76,740.00 USD | 49,760.00 USD |
| `7D` | `780.20` | 50,130,000.00 USD | 50,130,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.80` | 27,020,000.00 USD | 27,020,000.00 USD | 0.00 USD | 460,570.00 USD | 59,550.00 USD | 116,790.00 USD |
| `7D` | `781.10` | 51,740,000.00 USD | 51,740,000.00 USD | 0.00 USD | 1,280,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.60` | 27,710,000.00 USD | 27,710,000.00 USD | 0.00 USD | 406,600.00 USD | 104,930.00 USD | 178,550.00 USD |
| `7D` | `782.00` | 53,640,000.00 USD | 53,640,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.40` | 28,900,000.00 USD | 28,900,000.00 USD | 0.00 USD | 1,020,000.00 USD | 63,070.00 USD | 107,360.00 USD |
| `7D` | `782.90` | 55,630,000.00 USD | 55,630,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.20` | 29,800,000.00 USD | 29,800,000.00 USD | 0.00 USD | 743,330.00 USD | 41,930.00 USD | 121,680.00 USD |
| `7D` | `783.80` | 56,200,000.00 USD | 56,200,000.00 USD | 0.00 USD | 510,940.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.00` | 30,230,000.00 USD | 30,230,000.00 USD | 0.00 USD | 377,800.00 USD | 15,180.00 USD | 30,220.00 USD |
| `7D` | `784.70` | 56,510,000.00 USD | 56,510,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `784.80` | 30,620,000.00 USD | 30,620,000.00 USD | 0.00 USD | 332,200.00 USD | 32,520.00 USD | 24,490.00 USD |
| `1D` | `785.60` | 30,930,000.00 USD | 30,930,000.00 USD | 0.00 USD | 255,910.00 USD | 40,290.00 USD | 16,850.00 USD |
| `7D` | `785.60` | 57,640,000.00 USD | 57,640,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.40` | 31,230,000.00 USD | 31,230,000.00 USD | 0.00 USD | 236,700.00 USD | 27,720.00 USD | 39,740.00 USD |
| `7D` | `786.50` | 58,030,000.00 USD | 58,030,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.20` | 31,380,000.00 USD | 31,380,000.00 USD | 0.00 USD | 120,370.00 USD | 14,220.00 USD | 14,270.00 USD |
| `7D` | `787.40` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `788.00` | 31,690,000.00 USD | 31,690,000.00 USD | 0.00 USD | 180,530.00 USD | 43,090.00 USD | 89,090.00 USD |
| `7D` | `788.30` | 58,970,000.00 USD | 58,970,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.80` | 32,150,000.00 USD | 32,150,000.00 USD | 0.00 USD | 335,720.00 USD | 59,970.00 USD | 60,050.00 USD |
| `7D` | `789.20` | 59,810,000.00 USD | 59,810,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.60` | 32,490,000.00 USD | 32,490,000.00 USD | 0.00 USD | 302,240.00 USD | 15,770.00 USD | 19,710.00 USD |
| `7D` | `790.10` | 60,300,000.00 USD | 60,300,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.40` | 32,680,000.00 USD | 32,680,000.00 USD | 0.00 USD | 151,450.00 USD | 36,300.00 USD | 8,130.00 USD |
| `7D` | `791.00` | 61,180,000.00 USD | 61,180,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.20` | 32,910,000.00 USD | 32,910,000.00 USD | 0.00 USD | 195,470.00 USD | 23,230.00 USD | 8,530.00 USD |
| `7D` | `791.90` | 62,060,000.00 USD | 62,060,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.00` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 105,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `792.80` | 33,050,000.00 USD | 33,050,000.00 USD | 0.00 USD | 34,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 62,280,000.00 USD | 62,280,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.60` | 33,080,000.00 USD | 33,080,000.00 USD | 0.00 USD | 32,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 62,460,000.00 USD | 62,460,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.40` | 33,120,000.00 USD | 33,120,000.00 USD | 0.00 USD | 37,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 62,780,000.00 USD | 62,780,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.20` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 31,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 62,920,000.00 USD | 62,920,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `796.00` | 33,200,000.00 USD | 33,200,000.00 USD | 0.00 USD | 48,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `796.40` | 63,060,000.00 USD | 63,060,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `796.80` | 33,230,000.00 USD | 33,230,000.00 USD | 0.00 USD | 31,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 63,120,000.00 USD | 63,120,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.60` | 33,290,000.00 USD | 33,290,000.00 USD | 0.00 USD | 57,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 63,280,000.00 USD | 63,280,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.40` | 33,330,000.00 USD | 33,330,000.00 USD | 0.00 USD | 38,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `799.10` | 63,320,000.00 USD | 63,320,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.20` | 33,340,000.00 USD | 33,340,000.00 USD | 0.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.00` | 33,350,000.00 USD | 33,350,000.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 63,440,000.00 USD | 63,440,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.80` | 33,360,000.00 USD | 33,360,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 63,540,000.00 USD | 63,540,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.60` | 33,390,000.00 USD | 33,390,000.00 USD | 0.00 USD | 30,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `801.80` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.40` | 33,410,000.00 USD | 33,410,000.00 USD | 0.00 USD | 22,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `802.70` | 63,760,000.00 USD | 63,760,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.20` | 33,430,000.00 USD | 33,430,000.00 USD | 0.00 USD | 15,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 63,840,000.00 USD | 63,840,000.00 USD | 0.00 USD | 63,540.00 USD | 5,560.00 USD | 5,650.00 USD |
| `1D` | `804.00` | 33,430,000.00 USD | 33,430,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 63,920,000.00 USD | 63,920,000.00 USD | 0.00 USD | 32,340.00 USD | 22,610.00 USD | 32,980.00 USD |
| `1D` | `804.80` | 33,430,000.00 USD | 33,430,000.00 USD | 0.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `805.40` | 64,000,000.00 USD | 64,000,000.00 USD | 0.00 USD | 59,610.00 USD | 12,940.00 USD | 0.00 USD |
| `1D` | `805.60` | 33,440,000.00 USD | 33,440,000.00 USD | 0.00 USD | 11,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `806.30` | 64,010,000.00 USD | 64,010,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `806.40` | 33,450,000.00 USD | 33,450,000.00 USD | 0.00 USD | 3,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `807.20` | 33,460,000.00 USD | 33,460,000.00 USD | 0.00 USD | 15,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `807.20` | 64,060,000.00 USD | 64,060,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `1D` | `808.00` | 33,470,000.00 USD | 33,470,000.00 USD | 0.00 USD | 4,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `808.10` | 64,120,000.00 USD | 64,120,000.00 USD | 0.00 USD | 19,950.00 USD | 5,360.00 USD | 29,800.00 USD |
| `1D` | `808.80` | 33,480,000.00 USD | 33,480,000.00 USD | 0.00 USD | 14,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.00` | 64,200,000.00 USD | 64,200,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `1D` | `809.60` | 33,480,000.00 USD | 33,480,000.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.90` | 64,430,000.00 USD | 64,430,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `1D` | `810.40` | 33,480,000.00 USD | 33,480,000.00 USD | 0.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `810.80` | 64,520,000.00 USD | 64,520,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 64,580,000.00 USD | 64,580,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `7D` | `812.60` | 64,700,000.00 USD | 64,700,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `1D` | `812.80` | 33,500,000.00 USD | 33,500,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 5,420.00 USD |
| `7D` | `813.50` | 64,950,000.00 USD | 64,950,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `1D` | `813.60` | 33,520,000.00 USD | 33,520,000.00 USD | 0.00 USD | 20,530.00 USD | 4,540.00 USD | 0.00 USD |
| `1D` | `814.40` | 33,570,000.00 USD | 33,570,000.00 USD | 0.00 USD | 32,830.00 USD | 13,710.00 USD | 7,420.00 USD |
| `7D` | `814.40` | 65,270,000.00 USD | 65,270,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `1D` | `815.20` | 33,600,000.00 USD | 33,600,000.00 USD | 0.00 USD | 8,420.00 USD | 8,370.00 USD | 13,240.00 USD |
| `7D` | `815.30` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `1D` | `816.00` | 33,630,000.00 USD | 33,630,000.00 USD | 0.00 USD | 18,470.00 USD | 3,300.00 USD | 0.00 USD |
| `7D` | `816.20` | 65,790,000.00 USD | 65,790,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `1D` | `816.80` | 33,690,000.00 USD | 33,690,000.00 USD | 0.00 USD | 44,120.00 USD | 17,360.00 USD | 3,620.00 USD |
| `7D` | `817.10` | 66,190,000.00 USD | 66,190,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `1D` | `817.60` | 33,740,000.00 USD | 33,740,000.00 USD | 0.00 USD | 41,600.00 USD | 8,150.00 USD | 0.00 USD |
| `7D` | `818.00` | 66,650,000.00 USD | 66,650,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `1D` | `818.40` | 33,910,000.00 USD | 33,910,000.00 USD | 0.00 USD | 160,570.00 USD | 2,750.00 USD | 9,560.00 USD |
| `7D` | `818.90` | 66,880,000.00 USD | 66,880,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `1D` | `819.20` | 33,920,000.00 USD | 33,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `819.80` | 67,390,000.00 USD | 67,390,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `1D` | `820.00` | 33,940,000.00 USD | 33,940,000.00 USD | 0.00 USD | 10,410.00 USD | 8,380.00 USD | 9,280.00 USD |
| `7D` | `820.70` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `1D` | `820.80` | 33,990,000.00 USD | 33,990,000.00 USD | 0.00 USD | 25,080.00 USD | 9,720.00 USD | 8,860.00 USD |
| `1D` | `821.60` | 34,090,000.00 USD | 34,090,000.00 USD | 0.00 USD | 72,830.00 USD | 1,740.00 USD | 29,210.00 USD |
| `7D` | `821.60` | 67,900,000.00 USD | 67,900,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
| `1D` | `822.40` | 34,260,000.00 USD | 34,260,000.00 USD | 0.00 USD | 135,720.00 USD | 30,880.00 USD | 4,540.00 USD |
| `7D` | `822.50` | 68,400,000.00 USD | 68,400,000.00 USD | 0.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `823.20` | 34,590,000.00 USD | 34,590,000.00 USD | 0.00 USD | 277,730.00 USD | 22,910.00 USD | 28,520.00 USD |
| `7D` | `823.40` | 68,720,000.00 USD | 68,720,000.00 USD | 0.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD |
| `1D` | `824.00` | 34,810,000.00 USD | 34,810,000.00 USD | 0.00 USD | 160,660.00 USD | 24,950.00 USD | 28,720.00 USD |
| `7D` | `824.30` | 69,080,000.00 USD | 69,080,000.00 USD | 0.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD |
| `1D` | `824.80` | 34,870,000.00 USD | 34,870,000.00 USD | 0.00 USD | 32,380.00 USD | 18,680.00 USD | 13,300.00 USD |
| `7D` | `825.20` | 69,440,000.00 USD | 69,440,000.00 USD | 0.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD |
| `1D` | `825.60` | 34,970,000.00 USD | 34,970,000.00 USD | 0.00 USD | 81,190.00 USD | 8,270.00 USD | 11,270.00 USD |
| `1D` | `826.10` | 35,020,000.00 USD | 35,020,000.00 USD | 0.00 USD | 46,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `826.10` | 69,740,000.00 USD | 69,740,000.00 USD | 0.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD |
| `7D` | `827.00` | 70,380,000.00 USD | 70,380,000.00 USD | 0.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD |
| `7D` | `827.90` | 70,750,000.00 USD | 70,750,000.00 USD | 0.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD |
| `7D` | `828.80` | 70,940,000.00 USD | 70,940,000.00 USD | 0.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD |
| `7D` | `829.70` | 71,020,000.00 USD | 71,020,000.00 USD | 0.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD |
| `7D` | `830.60` | 71,270,000.00 USD | 71,270,000.00 USD | 0.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD |
| `7D` | `831.50` | 71,320,000.00 USD | 71,320,000.00 USD | 0.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.23B` | Total OI Tokens: `1,646,651.7 BNB`
  * 1h OI Change: `-0.16%` | 4h OI Change: `-0.90%` | 24h OI Change: `-2.81%`
  * Exchange Breakdown: Binance=`580.06M` | Bybit=`105.81M` | OKX=`53.70M` | Hyperliquid=`46.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `81.68K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0141%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0141%` | **USDT BingX** | `0.0144%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0000%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `59.11%` | `40.89%` | `1.45` | 44,020,000.00 USD |
| `15M` | `Binance` | `57.94%` | `42.06%` | `1.38` | 12,110,000.00 USD |
| `15M` | `OKX` | `52.09%` | `47.91%` | `1.09` | 6,430,000.00 USD |
| `15M` | `Bybit` | `74.55%` | `25.45%` | `2.93` | 3,980,000.00 USD |
| `15M` | `KuCoin` | `45.9%` | `54.1%` | `0.85` | 61,090.00 USD |
| `15M` | `Gate` | `56.05%` | `43.95%` | `1.28` | 4,300,000.00 USD |
| `15M` | `Bitget` | `85.69%` | `14.31%` | `5.99` | 1,440,000.00 USD |
| `15M` | `BingX` | `49.61%` | `50.39%` | `0.98` | 2,890,000.00 USD |
| `15M` | `MEXC` | `68.96%` | `31.04%` | `2.22` | 5,510,000.00 USD |
| `15M` | `Bitunix` | `59.84%` | `40.16%` | `1.49` | 2,910,000.00 USD |
| `15M` | `Hyperliquid` | `76.29%` | `23.71%` | `3.22` | 780,260.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `66.26%` | `33.74%` | `1.96` | 780,770.00 USD |
| `15M` | `Crypto.com` | `68.99%` | `31.01%` | `2.22` | 85,630.00 USD |
| `15M` | `WhiteBIT` | `12.27%` | `87.73%` | `0.14` | 1,520,000.00 USD |
| `15M` | `HTX` | `21.48%` | `78.52%` | `0.27` | 98,680.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `73.95%` | `26.05%` | `2.84` | 420,050.00 USD |
| `15M` | `Aster` | `60.6%` | `39.4%` | `1.54` | 214,270.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.06%` | `54.94%` | `0.82` | 495,540.00 USD |
| `15M` | `Whale Positions` | `57.94%` | `42.06%` | `1.38` | 12,110,000.00 USD |
| `15M` | `Global Accounts` | `59.11%` | `40.89%` | `1.45` | 44,020,000.00 USD |
| `1H` | `BNB` | `54.24%` | `45.76%` | `1.19` | 224,210,000.00 USD |
| `1H` | `Binance` | `54.12%` | `45.88%` | `1.18` | 67,340,000.00 USD |
| `1H` | `OKX` | `65.83%` | `34.17%` | `1.93` | 30,920,000.00 USD |
| `1H` | `Bybit` | `50.54%` | `49.46%` | `1.02` | 22,950,000.00 USD |
| `1H` | `KuCoin` | `41.89%` | `58.11%` | `0.72` | 882,480.00 USD |
| `1H` | `Gate` | `57.95%` | `42.05%` | `1.38` | 18,150,000.00 USD |
| `1H` | `Bitget` | `78.15%` | `21.85%` | `3.58` | 6,880,000.00 USD |
| `1H` | `BingX` | `30.84%` | `69.16%` | `0.45` | 13,940,000.00 USD |
| `1H` | `MEXC` | `37.18%` | `62.82%` | `0.59` | 30,560,000.00 USD |
| `1H` | `Bitunix` | `48.45%` | `51.55%` | `0.94` | 13,640,000.00 USD |
| `1H` | `Hyperliquid` | `21.53%` | `78.47%` | `0.27` | 3,950,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.57%` | `44.43%` | `1.25` | 3,010,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 287,850.00 USD |
| `1H` | `WhiteBIT` | `84.01%` | `15.99%` | `5.25` | 6,280,000.00 USD |
| `1H` | `HTX` | `79.79%` | `20.21%` | `3.95` | 477,060.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `39.74%` | `60.26%` | `0.66` | 1,970,000.00 USD |
| `1H` | `Aster` | `59.71%` | `40.29%` | `1.48` | 1,430,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.65%` | `54.35%` | `0.84` | 1,540,000.00 USD |
| `1H` | `Whale Positions` | `54.12%` | `45.88%` | `1.18` | 67,340,000.00 USD |
| `1H` | `Global Accounts` | `54.24%` | `45.76%` | `1.19` | 224,210,000.00 USD |
| `4H` | `BNB` | `47.09%` | `52.91%` | `0.89` | 1,320,000,000.00 USD |
| `4H` | `Binance` | `46.82%` | `53.18%` | `0.88` | 436,000,000.00 USD |
| `4H` | `OKX` | `47.02%` | `52.98%` | `0.89` | 197,130,000.00 USD |
| `4H` | `Bybit` | `49.96%` | `50.04%` | `1.00` | 122,670,000.00 USD |
| `4H` | `KuCoin` | `47.53%` | `52.47%` | `0.91` | 6,250,000.00 USD |
| `4H` | `Gate` | `49.11%` | `50.89%` | `0.97` | 109,150,000.00 USD |
| `4H` | `Bitget` | `49.39%` | `50.61%` | `0.98` | 43,690,000.00 USD |
| `4H` | `BingX` | `48.19%` | `51.81%` | `0.93` | 61,050,000.00 USD |
| `4H` | `MEXC` | `49.13%` | `50.87%` | `0.97` | 132,490,000.00 USD |
| `4H` | `Bitunix` | `50%` | `50%` | `1.00` | 76,200,000.00 USD |
| `4H` | `Hyperliquid` | `44.86%` | `55.14%` | `0.81` | 32,320,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.68%` | `50.32%` | `0.99` | 17,810,000.00 USD |
| `4H` | `Crypto.com` | `47.12%` | `52.88%` | `0.89` | 2,130,000.00 USD |
| `4H` | `WhiteBIT` | `10.26%` | `89.74%` | `0.11` | 24,010,000.00 USD |
| `4H` | `HTX` | `45.05%` | `54.95%` | `0.82` | 2,400,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.72%` | `55.28%` | `0.81` | 29,960,000.00 USD |
| `4H` | `Aster` | `42.88%` | `57.12%` | `0.75` | 13,040,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.39%` | `58.61%` | `0.71` | 11,470,000.00 USD |
| `4H` | `Whale Positions` | `46.82%` | `53.18%` | `0.88` | 436,000,000.00 USD |
| `4H` | `Global Accounts` | `47.09%` | `52.91%` | `0.89` | 1,320,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `749.85` | `749.01` | `749.85` | `750.15` | `747.45` | 7,159,834.50 USD | 3,107,939.33 USD | 4,051,895.17 USD | -943,955.84 USD | `-13.18%` | `0B / 0S` |
| `5:00 UTC` | `750.45` | `750.48` | `750.45` | `751.05` | `749.85` | 4,170,354.29 USD | 2,126,593.29 USD | 2,043,761.00 USD | 82,832.29 USD | `+1.99%` | `0B / 0S` |
| `0:00 UTC` | `748.95` | `749.19` | `748.95` | `750.45` | `748.35` | 3,784,737.73 USD | 1,149,920.62 USD | 2,634,817.11 USD | -1,484,896.49 USD | `-39.23%` | `0B / 3S` |
| `5:00 UTC` | `748.65` | `748.42` | `748.65` | `748.95` | `747.75` | 3,504,446.48 USD | 1,566,200.72 USD | 1,938,245.76 USD | -372,045.05 USD | `-10.62%` | `0B / 1S` |
| `0:00 UTC` | `746.85` | `747.37` | `746.85` | `748.95` | `745.95` | 4,608,707.67 USD | 1,960,110.54 USD | 2,648,597.13 USD | -688,486.59 USD | `-14.94%` | `0B / 2S` |
| `5:00 UTC` | `745.95` | `745.96` | `745.95` | `746.85` | `745.05` | 3,520,898.41 USD | 1,701,969.64 USD | 1,818,928.78 USD | -116,959.14 USD | `-3.32%` | `0B / 0S` |
| `0:00 UTC` | `746.25` | `745.96` | `746.25` | `746.85` | `745.05` | 2,334,703.88 USD | 1,240,058.73 USD | 1,094,645.16 USD | 145,413.57 USD | `+6.23%` | `1B / 0S` |
| `5:00 UTC` | `745.35` | `745.34` | `745.35` | `745.95` | `744.45` | 2,053,811.83 USD | 1,008,932.17 USD | 1,044,879.66 USD | -35,947.48 USD | `-1.75%` | `0B / 0S` |
| `0:00 UTC` | `743.55` | `743.83` | `743.55` | `745.05` | `742.95` | 4,178,944.72 USD | 2,213,489.92 USD | 1,965,454.80 USD | 248,035.12 USD | `+5.94%` | `0B / 1S` |
| `5:00 UTC` | `744.45` | `744.36` | `744.45` | `745.05` | `743.85` | 914,250.95 USD | 526,401.76 USD | 387,849.20 USD | 138,552.56 USD | `+15.15%` | `0B / 0S` |

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
| `5m` | 20,790.00 USD | 623,510.00 USD | **`ACCUMULATION`** |
| `15m` | 9,690.00 USD | 1,040,000.00 USD | **`ACCUMULATION`** |
| `30m` | 27,330.00 USD | 1,110,000.00 USD | **`ACCUMULATION`** |
| `1h` | -164,400.00 USD | 1,730,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,420,000.00 USD | -4,050,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,600,000.00 USD | -5,680,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 562,440.00 USD | 2,310,000.00 USD | **`ACCUMULATION`** |
| `8h` | -8,040,000.00 USD | -4,850,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,750,000.00 USD | -13,310,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 5,650,000.00 USD | -21,040,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -27,850,000.00 USD | -46,280,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -124,850,000.00 USD | -369,540,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+20.79K` | 15m=`+9.69K` | 1h=`-164.40K` | 24h=`+5.65M`
* Futures Capital Netflows: 5m=`+623.51K` | 15m=`+1.04M` | 1h=`+1.73M` | 24h=`-21.04M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `740.42` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `736.64` (Risk Distance: `3.78` pts)
  * +2.5R Take Profit: `749.86`
  * Mathematical Lot Sizing: **`2.64 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `752.43` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `756.21` (Risk Distance: `3.78` pts)
  * +2.5R Take Profit: `742.99`
  * Mathematical Lot Sizing: **`2.64 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`749.85`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
