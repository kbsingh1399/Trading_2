# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:36:03 IST` (`2026-10-29 20:06:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `740.60` | **Live Ask Quote**: `741.10` | **Mid Price**: `740.85`
- **Spread Points**: `50.00` | **Spread BPS**: `6.75 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `746.75` | VWAP Z-Score: `-0.62` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.15` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.93` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `761.45` | Lower -3.00σ Band: `732.05`
  * Upper +2.51σ Band: `759.05` | Lower -2.51σ Band: `734.45`
  * Upper +2.01σ Band: `756.60` | Lower -2.01σ Band: `736.90`
  * Upper +2.00σ Band: `756.55` | Lower -2.00σ Band: `736.95`
  * Upper +1.28σ Band: `753.02` | Lower -1.28σ Band: `740.48`
  * Upper +1.00σ Band: `751.65` | Lower -1.00σ Band: `741.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`743.89` | EMA-20=`744.67` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`745.68` (Slope: `+0.0000`) | EMA-100=`746.85`
  * Institutional Anchors: EMA-144=`746.95` | EMA-200=`746.28` (Slope: `-0.0376`) | EMA-233=`745.63`
- **Range Boundaries**: 24H High=`759.80` | 24H Low=`737.00` | Weekly High=`760.90` | Weekly Low=`732.50`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `752.43` (Distance: `-1.53%`)
  * Point of Control (POC) = `750.76` (Distance: `-1.31%`)
  * Value Area Low (VAL) = `740.57` (Distance: `+0.04%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `737.89` - `743.81`
  * Optimal Trade Entry (OTE 0.705): `742.33`
  * Structural Invalidation Anchor (0.786): `746.78`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `745.60` | `746.16` | `745.41` | `745.54` | `796` | 593,912.38 USD | 180,571.12 USD | `+30.40%` | -20,361,121.78 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `745.53` | `745.63` | `745.15` | `745.33` | `955` | 711,595.41 USD | -72,326.71 USD | `-10.16%` | -20,433,448.50 USD | `-0.93` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `745.34` | `745.53` | `741.84` | `742.04` | `11,640` | 8,651,688.69 USD | -5,960,752.16 USD | `-68.90%` | -26,394,200.66 USD | `-4.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `744.36` | `746.13` | `744.36` | `745.35` | `2,827` | 2,107,319.68 USD | 138,257.94 USD | `+6.56%` | -19,773,345.59 USD | `+0.22` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `745.35` | `746.16` | `745.15` | `745.33` | `2,299` | 1,714,180.55 USD | 297,640.01 USD | `+17.36%` | -19,475,705.58 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `745.34` | `745.53` | `741.84` | `741.99` | `11,616` | 8,633,762.54 USD | -5,969,997.18 USD | `-69.15%` | -25,445,702.77 USD | `-3.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `746.40` | `746.83` | `743.07` | `744.90` | `13,831` | 10,300,433.14 USD | 703,778.72 USD | `+6.83%` | -21,836,543.73 USD | `+0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `744.90` | `746.16` | `743.85` | `745.33` | `9,678` | 7,209,732.85 USD | 951,958.00 USD | `+13.20%` | -20,884,585.73 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `745.34` | `745.53` | `741.84` | `742.04` | `11,640` | 8,651,688.69 USD | -5,960,752.16 USD | `-68.90%` | -26,845,337.89 USD | `-1.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `741.84` | `741.97` | `11,630` | 8,644,543.32 USD | -5,967,897.54 USD | `-69.04%` | -22,746,306.25 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -14,715,810.54 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -25,056,103.04 USD | `-1.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `741.84` | `741.97` | `11,630` | 8,644,543.32 USD | -5,967,897.54 USD | `-69.04%` | -22,746,306.25 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`740.85`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `744.81` | `851000000.0000` | 633.83 USD | 97,189.66 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.85` | `20595000000.0000` | 15,340.19 USD | 96,555.83 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `744.86` | `1109000000.0000` | 826.05 USD | 81,215.64 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.87` | `1515000000.0000` | 1,128.48 USD | 80,389.59 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `744.89` | `1793000000.0000` | 1,335.59 USD | 79,261.11 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `744.90` | `552000000.0000` | 411.18 USD | 77,925.53 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `744.91` | `2106000000.0000` | 1,568.78 USD | 77,514.34 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `744.92` | `7641000000.0000` | 5,691.93 USD | 75,945.56 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `744.93` | `1343000000.0000` | 1,000.44 USD | 70,253.63 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `744.95` | `37460000000.0000` | 27,905.83 USD | 69,253.19 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `744.96` | `35000000.0000` | 26.07 USD | 41,347.36 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `744.98` | `643000000.0000` | 479.02 USD | 41,321.29 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `744.99` | `24037000000.0000` | 17,907.32 USD | 40,842.26 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `745.00` | `8450000000.0000` | 6,295.25 USD | 22,934.94 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `745.01` | `503000000.0000` | 374.74 USD | 16,639.69 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `745.02` | `831000000.0000` | 619.11 USD | 16,264.95 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `745.03` | `3345000000.0000` | 2,492.13 USD | 15,645.84 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `745.07` | `1109000000.0000` | 826.28 USD | 13,153.71 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `745.09` | `18000000.0000` | 13.41 USD | 12,327.43 USD | `1 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `745.13` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 745.13` | `0.00%` | `-` |
| `BID` | `745.13` | `16526000000.0000` | 12,314.02 USD | 12,314.02 USD | `4 orders` | `-0.00%` | `-` |
| `ASK` | `745.14` | `109000000.0000` | 81.22 USD | 81.22 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `745.24` | `2374000000.0000` | 1,769.20 USD | 1,850.42 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `745.25` | `6195000000.0000` | 4,616.82 USD | 6,467.24 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `745.26` | `831000000.0000` | 619.31 USD | 7,086.55 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `745.31` | `6465000000.0000` | 4,818.43 USD | 11,904.98 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `745.32` | `2755000000.0000` | 2,053.36 USD | 13,958.34 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `745.34` | `8275000000.0000` | 6,167.69 USD | 20,126.03 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `745.37` | `6708000000.0000` | 4,999.94 USD | 25,125.97 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `745.38` | `1109000000.0000` | 826.63 USD | 25,952.60 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `745.39` | `3792000000.0000` | 2,826.52 USD | 28,779.12 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `745.40` | `522000000.0000` | 389.10 USD | 29,168.22 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `745.41` | `13552000000.0000` | 10,101.80 USD | 39,270.01 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `745.42` | `1213000000.0000` | 904.19 USD | 40,174.21 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `745.43` | `3841000000.0000` | 2,863.20 USD | 43,037.40 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `745.44` | `10313000000.0000` | 7,687.72 USD | 50,725.13 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `745.45` | `11590000000.0000` | 8,639.77 USD | 59,364.89 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `745.47` | `280000000.0000` | 208.73 USD | 59,573.62 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `745.48` | `32248000000.0000` | 24,040.24 USD | 83,613.86 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `745.49` | `140000000.0000` | 104.37 USD | 83,718.23 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `745.50` | `2500000000.0000` | 1,863.75 USD | 85,581.98 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `775` | `0xea00...a918` | `LONG` | 3,054,067.32 USD | `4,098,429,000,000.00` | `787.24` | `745.09` | `0.000000` | -172,359.46 USD | `-5.64%` | `5X Cross` |
| `1077` | `0xb69e...033a` | `LONG` | 2,090,590.64 USD | `2,805,710,000,000.00` | `772.94` | `745.09` | `566.16` | -78,051.95 USD | `-3.73%` | `10X Cross` |
| `1088` | `0xcac1...26b3` | `LONG` | 2,078,283.28 USD | `2,789,043,000,000.00` | `679.91` | `745.09` | `0.000000` | 181,972.12 USD | `+8.76%` | `10X Cross` |
| `1164` | `0x7737...bf66` | `SHORT` | 1,971,617.70 USD | `2,646,179,000,000.00` | `752.73` | `745.09` | `7054.04` | 20,252.89 USD | `+1.03%` | `10X Cross` |
| `1561` | `0xecb6...2b00` | `SHORT` | 1,430,176.06 USD | `1,919,416,000,000.00` | `738.35` | `745.09` | `14099.97` | -12,969.99 USD | `-0.91%` | `5X Cross` |
| `1646` | `0x27c9...d65d` | `SHORT` | 1,330,887.91 USD | `1,786,163,000,000.00` | `762.40` | `745.09` | `1575.74` | 30,879.44 USD | `+2.32%` | `10X Cross` |
| `1743` | `0x07fd...689d` | `LONG` | 1,240,588.57 USD | `1,664,862,000,000.00` | `716.02` | `745.09` | `0.000000` | 48,512.22 USD | `+3.91%` | `10X Cross` |
| `1758` | `0x645b...87b8` | `LONG` | 1,216,383.47 USD | `1,632,357,000,000.00` | `750.75` | `745.09` | `0.000000` | -9,102.70 USD | `-0.75%` | `10X Cross` |
| `2019` | `0xbcd4...0dd2` | `LONG` | 1,009,119.94 USD | `1,354,278,000,000.00` | `746.04` | `745.09` | `0.000000` | -1,224.13 USD | `-0.12%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `745.30` | 53,346.34 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 53.35K USD at 745.3000 USD [API] | `2026-10-27 22:32:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.31` (Vol: 2,400,000.00 USD, Dist: `+1.75%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--1.18%`)
  * 48H Horizon: Short MP=`758.54` (Vol: 2,400,000.00 USD, Dist: `+1.78%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--1.18%`)
  * 3D Horizon: Short MP=`766.52` (Vol: 2,500,000.00 USD, Dist: `+2.85%`) | Long MP=`736.48` (Vol: 3,000,000.00 USD, Dist: `--1.18%`)
  * 7D Horizon: Short MP=`758.15` (Vol: 2,900,000.00 USD, Dist: `+1.73%`) | Long MP=`728.45` (Vol: 3,700,000.00 USD, Dist: `--2.26%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `156.50` | 159.16 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 9,040.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `177.50` | 647.34 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 117.96 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `198.50` | 284.25 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `212.50` | 260.74 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `214.50` | 1,070.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 4,170.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `246.50` | 321.68 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `257.50` | 4,370.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `260.50` | 819.79 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `276.50` | 21,920.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `293.50` | 336.94 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `299.50` | 1,580.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `300.50` | 6,030.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `304.50` | 8,030.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `307.50` | 14,650.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `308.50` | 21,340.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 501.60 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `316.50` | 309.22 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `317.50` | 112.08 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `320.50` | 1,360.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `321.50` | 1,020.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `324.50` | 897.89 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 315.03 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 1,650.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 688.34 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `351.50` | 12,000.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `352.50` | 1,590.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `354.50` | 1,160.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 707.35 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 103.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 240.43 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,240.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 953.44 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 645.15 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `380.50` | 2,970.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 14,020.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 2,860.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 103.88 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 47,480.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 396.50 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 605.16 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `408.50` | 3,450.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 30,280.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 106.17 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 13,320.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 465.79 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 2,660.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `426.50` | 359.11 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `427.50` | 141.93 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 638.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `437.50` | 590.19 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `453.50` | 8,620.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `454.50` | 4,220.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 17,550.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `457.50` | 463.45 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `458.50` | 386.06 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `467.50` | 1,950.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `468.50` | 1,100.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 5,450.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 4,380.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 475.50 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `476.50` | 6,380.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.50` | 2,590.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 2,120.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `503.50` | 251.75 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,610.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 158.56 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 8,280.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,010.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 3,780.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 2,700.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 2,750.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 157.11 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 3,360.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 3,560.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 1,040.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 440.99 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,090.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 11,810.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 2,260.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 3,080.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 17,330.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 1,280.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 632.08 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 100.33 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `537.50` | 4,300.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 334.25 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,310.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 491.85 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 14,030.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,770.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 908.88 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 959.69 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 6,530.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 2,010.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 591.61 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 1,300.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 5,680.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `559.50` | 212.61 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 10,280.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 583.40 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `564.50` | 14,210.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `570.50` | 393.64 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 715,280.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.50` | 675.06 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 1,620,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 222.91 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 275.37 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 2,320.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 275.41 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 6,810.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 6,650.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 1,530.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 100.39 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 15,420.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 44,800.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 100.98 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,060.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 1,800.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 303.76 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 1,880.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `608.50` | 511.14 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 330.82 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 527.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 2,280.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 427.16 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 770.62 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 742.20 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,590.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 983.21 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 2,110.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `623.50` | 1,050.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,740.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 11,970.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 16,020.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 664.32 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `629.50` | 3,680.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `631.50` | 6,320.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `632.50` | 125.87 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `633.50` | 1,920.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 5,910.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 1,110.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 5,870.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `639.50` | 33,550.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 2,310.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 1,670.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 485.09 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `643.50` | 8,490.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `644.50` | 9,010.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.50` | 5,980.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `646.50` | 2,120.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `649.50` | 559.87 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `651.50` | 633.26 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `654.50` | 97,530.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `656.50` | 122.77 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `658.50` | 4,800.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,340.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `661.50` | 463.71 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `662.50` | 19,830.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `663.50` | 4,350.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 5,440.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.20` | 32,670,000.00 USD | 32,670,000.00 USD | 64,690.00 USD | 25,520.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 3,040.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.00` | 32,570,000.00 USD | 32,570,000.00 USD | 174,720.00 USD | 2,750.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 2,570.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.80` | 32,390,000.00 USD | 32,390,000.00 USD | 19,310.00 USD | 8,380.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 3,360.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.60` | 32,350,000.00 USD | 32,350,000.00 USD | 43,410.00 USD | 9,720.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `672.40` | 32,290,000.00 USD | 32,290,000.00 USD | 93,500.00 USD | 10,080.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 13,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.20` | 32,150,000.00 USD | 32,150,000.00 USD | 328,000.00 USD | 37,780.00 USD | 26,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 567.76 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.00` | 31,760,000.00 USD | 31,760,000.00 USD | 153,390.00 USD | 23,000.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 259.68 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.80` | 31,570,000.00 USD | 31,570,000.00 USD | 104,430.00 USD | 28,310.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.60` | 31,410,000.00 USD | 31,410,000.00 USD | 134,840.00 USD | 15,770.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.40` | 31,240,000.00 USD | 31,240,000.00 USD | 78,970.00 USD | 31,240.00 USD | 64,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.20` | 31,060,000.00 USD | 31,060,000.00 USD | 269,660.00 USD | 21,680.00 USD | 40,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.00` | 30,730,000.00 USD | 30,730,000.00 USD | 176,540.00 USD | 9,040.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 1,610.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `678.80` | 30,520,000.00 USD | 30,520,000.00 USD | 45,580.00 USD | 9,090.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 901.70 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.60` | 30,450,000.00 USD | 30,450,000.00 USD | 159,490.00 USD | 7,580.00 USD | 6,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.40` | 30,280,000.00 USD | 30,280,000.00 USD | 20,670.00 USD | 9,240.00 USD | 15,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.20` | 30,230,000.00 USD | 30,230,000.00 USD | 89,180.00 USD | 5,770.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 31,450.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `682.00` | 30,130,000.00 USD | 30,130,000.00 USD | 34,070.00 USD | 17,040.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.80` | 30,050,000.00 USD | 30,050,000.00 USD | 127,700.00 USD | 11,650.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.60` | 29,890,000.00 USD | 29,890,000.00 USD | 10,050.00 USD | 11,310.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.40` | 29,870,000.00 USD | 29,870,000.00 USD | 38,150.00 USD | 9,430.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `684.50` | 42,430.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.20` | 29,810,000.00 USD | 29,810,000.00 USD | 30,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `685.50` | 1,290.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `686.50` | 194.28 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `687.50` | 198.69 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.20` | 29,780,000.00 USD | 29,780,000.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `689.50` | 885.32 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `690.00` | 29,780,000.00 USD | 29,780,000.00 USD | 56,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `690.50` | 6,170.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `690.80` | 29,720,000.00 USD | 29,720,000.00 USD | 46,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `691.50` | 5,430.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `691.60` | 29,670,000.00 USD | 29,670,000.00 USD | 54,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.40` | 29,620,000.00 USD | 29,620,000.00 USD | 54,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `692.50` | 5,580.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.20` | 29,570,000.00 USD | 29,570,000.00 USD | 48,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `693.50` | 2,590.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.00` | 29,520,000.00 USD | 29,520,000.00 USD | 32,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `694.50` | 513.93 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.80` | 29,480,000.00 USD | 29,480,000.00 USD | 17,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `695.50` | 299.07 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `695.60` | 29,470,000.00 USD | 29,470,000.00 USD | 34,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.40` | 29,430,000.00 USD | 29,430,000.00 USD | 24,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `696.50` | 3,790.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `697.20` | 29,410,000.00 USD | 29,410,000.00 USD | 70,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `697.50` | 2,160.00 USD | 996,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `698.00` | 29,340,000.00 USD | 29,340,000.00 USD | 50,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `698.50` | 303.15 USD | 994,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `698.80` | 29,290,000.00 USD | 29,290,000.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `699.50` | 20,100.00 USD | 994,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `699.60` | 29,270,000.00 USD | 29,270,000.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.40` | 29,270,000.00 USD | 29,270,000.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `700.50` | 1,130.00 USD | 974,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.20` | 29,250,000.00 USD | 29,250,000.00 USD | 24,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.00` | 29,230,000.00 USD | 29,230,000.00 USD | 28,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `702.50` | 2,260.00 USD | 972,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `702.80` | 29,200,000.00 USD | 29,200,000.00 USD | 115,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `703.50` | 3,820.00 USD | 970,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `703.60` | 29,080,000.00 USD | 29,080,000.00 USD | 57,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.40` | 29,020,000.00 USD | 29,020,000.00 USD | 97,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `704.50` | 2,720.00 USD | 966,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `705.20` | 28,930,000.00 USD | 28,930,000.00 USD | 73,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `705.50` | 86,210.00 USD | 964,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `706.00` | 28,850,000.00 USD | 28,850,000.00 USD | 73,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `706.50` | 28,860.00 USD | 877,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `706.80` | 28,780,000.00 USD | 28,780,000.00 USD | 33,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `707.50` | 22,380.00 USD | 849,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `707.60` | 28,750,000.00 USD | 28,750,000.00 USD | 25,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `708.40` | 28,720,000.00 USD | 28,720,000.00 USD | 53,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `708.50` | 171,950.00 USD | 826,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `709.20` | 28,670,000.00 USD | 28,670,000.00 USD | 28,500.00 USD | 13,950.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `709.50` | 339,560.00 USD | 654,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `710.00` | 28,600,000.00 USD | 28,600,000.00 USD | 93,600.00 USD | 18,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `710.50` | 46,020.00 USD | 315,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `710.80` | 28,490,000.00 USD | 28,490,000.00 USD | 134,360.00 USD | 67,330.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `711.50` | 11,630.00 USD | 269,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `711.60` | 28,270,000.00 USD | 28,270,000.00 USD | 177,560.00 USD | 34,600.00 USD | 33,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.40` | 28,030,000.00 USD | 28,030,000.00 USD | 58,920.00 USD | 4,240.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `712.50` | 229,760.00 USD | 257,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `713.20` | 27,940,000.00 USD | 27,940,000.00 USD | 147,040.00 USD | 73,320.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `713.50` | 20,280.00 USD | 27,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `714.00` | 27,700,000.00 USD | 27,700,000.00 USD | 216,410.00 USD | 19,280.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `714.50` | 157.90 USD | 7,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `714.80` | 27,440,000.00 USD | 27,440,000.00 USD | 503,730.00 USD | 1,230.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.60` | 26,930,000.00 USD | 26,930,000.00 USD | 116,340.00 USD | 27,130.00 USD | 26,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `716.40` | 26,760,000.00 USD | 26,760,000.00 USD | 76,880.00 USD | 35,530.00 USD | 42,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `716.50` | 789.58 USD | 7,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `717.20` | 26,610,000.00 USD | 26,610,000.00 USD | 189,860.00 USD | 30,000.00 USD | 110,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `717.50` | 3,700.00 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `718.00` | 26,280,000.00 USD | 26,280,000.00 USD | 1,040,000.00 USD | 111,290.00 USD | 101,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `718.50` | 1,790.00 USD | 2,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `718.80` | 25,030,000.00 USD | 25,030,000.00 USD | 489,520.00 USD | 80,390.00 USD | 100,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `719.60` | 24,360,000.00 USD | 24,360,000.00 USD | 575,720.00 USD | 77,740.00 USD | 116,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `720.40` | 23,590,000.00 USD | 23,590,000.00 USD | 348,960.00 USD | 51,300.00 USD | 55,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `721.20` | 23,130,000.00 USD | 23,130,000.00 USD | 311,810.00 USD | 124,610.00 USD | 178,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `721.50` | 998.56 USD | 998.56 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `722.00` | 22,510,000.00 USD | 22,510,000.00 USD | 1,020,000.00 USD | 37,060.00 USD | 88,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `722.80` | 21,370,000.00 USD | 21,370,000.00 USD | 629,270.00 USD | 63,740.00 USD | 169,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `723.60` | 20,510,000.00 USD | 20,510,000.00 USD | 416,950.00 USD | 14,770.00 USD | 42,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `724.40` | 20,040,000.00 USD | 20,040,000.00 USD | 259,230.00 USD | 83,130.00 USD | 51,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `725.20` | 19,640,000.00 USD | 19,640,000.00 USD | 173,930.00 USD | 109,030.00 USD | 53,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `726.00` | 19,310,000.00 USD | 19,310,000.00 USD | 358,990.00 USD | 166,310.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `726.80` | 18,720,000.00 USD | 18,720,000.00 USD | 535,650.00 USD | 46,390.00 USD | 70,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `727.60` | 18,070,000.00 USD | 18,070,000.00 USD | 277,460.00 USD | 136,050.00 USD | 192,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `728.40` | 17,460,000.00 USD | 17,460,000.00 USD | 902,960.00 USD | 117,420.00 USD | 33,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `729.20` | 16,410,000.00 USD | 16,410,000.00 USD | 939,580.00 USD | 51,810.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `730.00` | 15,350,000.00 USD | 15,350,000.00 USD | 306,910.00 USD | 51,570.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `730.80` | 14,960,000.00 USD | 14,960,000.00 USD | 380,880.00 USD | 65,180.00 USD | 79,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `731.60` | 14,430,000.00 USD | 14,430,000.00 USD | 157,660.00 USD | 62,000.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `732.40` | 14,150,000.00 USD | 14,150,000.00 USD | 235,470.00 USD | 147,360.00 USD | 205,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `733.20` | 13,560,000.00 USD | 13,560,000.00 USD | 2,140,000.00 USD | 210,290.00 USD | 256,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `734.00` | 10,960,000.00 USD | 10,960,000.00 USD | 1,190,000.00 USD | 152,200.00 USD | 203,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `734.80` | 9,410,000.00 USD | 9,410,000.00 USD | 863,310.00 USD | 126,110.00 USD | 189,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `735.60` | 8,230,000.00 USD | 8,230,000.00 USD | 848,110.00 USD | 81,400.00 USD | 169,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `736.40` | 7,130,000.00 USD | 7,130,000.00 USD | 404,280.00 USD | 234,770.00 USD | 394,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `737.20` | 6,100,000.00 USD | 6,100,000.00 USD | 2,200,000.00 USD | 110,380.00 USD | 174,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `738.00` | 3,620,000.00 USD | 3,620,000.00 USD | 1,220,000.00 USD | 94,940.00 USD | 235,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `738.80` | 2,070,000.00 USD | 2,070,000.00 USD | 680,980.00 USD | 18,090.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `739.60` | 1,330,000.00 USD | 1,330,000.00 USD | 518,470.00 USD | 0.00 USD | 48,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `740.40` | 765,920.00 USD | 765,920.00 USD | 347,860.00 USD | 0.00 USD | 33,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `741.20` | 384,360.00 USD | 384,360.00 USD | 230,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `742.80` | 154,230.00 USD | 154,230.00 USD | 0.00 USD | 0.00 USD | 64,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `743.60` | 89,620.00 USD | 89,620.00 USD | 0.00 USD | 0.00 USD | 48,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `744.40` | 41,100.00 USD | 41,100.00 USD | 0.00 USD | 29,640.00 USD | 11,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.00` | 38,640.00 USD | 38,640.00 USD | 38,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.20` | 51,040.00 USD | 51,040.00 USD | 0.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.00` | 128,730.00 USD | 128,730.00 USD | 0.00 USD | 50,610.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.80` | 234,590.00 USD | 234,590.00 USD | 0.00 USD | 68,750.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.60` | 530,160.00 USD | 530,160.00 USD | 143,570.00 USD | 132,220.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.40` | 991,960.00 USD | 991,960.00 USD | 390,390.00 USD | 24,970.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.20` | 1,310,000.00 USD | 1,310,000.00 USD | 145,940.00 USD | 88,970.00 USD | 81,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.00` | 1,510,000.00 USD | 1,510,000.00 USD | 136,350.00 USD | 67,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.80` | 1,960,000.00 USD | 1,960,000.00 USD | 367,110.00 USD | 28,530.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.60` | 2,940,000.00 USD | 2,940,000.00 USD | 971,100.00 USD | 2,460.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.40` | 3,310,000.00 USD | 3,310,000.00 USD | 245,610.00 USD | 54,260.00 USD | 72,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.20` | 3,550,000.00 USD | 3,550,000.00 USD | 102,000.00 USD | 71,050.00 USD | 66,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.00` | 4,180,000.00 USD | 4,180,000.00 USD | 349,140.00 USD | 60,010.00 USD | 220,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.80` | 6,110,000.00 USD | 6,110,000.00 USD | 1,580,000.00 USD | 168,030.00 USD | 191,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 211.49 USD | 211.49 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.60` | 7,380,000.00 USD | 7,380,000.00 USD | 1,010,000.00 USD | 150,840.00 USD | 111,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.40` | 9,180,000.00 USD | 9,180,000.00 USD | 1,330,000.00 USD | 177,890.00 USD | 290,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.20` | 9,900,000.00 USD | 9,900,000.00 USD | 492,320.00 USD | 144,680.00 USD | 86,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.00` | 11,000,000.00 USD | 11,000,000.00 USD | 705,930.00 USD | 113,780.00 USD | 276,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.80` | 13,110,000.00 USD | 13,110,000.00 USD | 1,690,000.00 USD | 156,820.00 USD | 256,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 1,050.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `767.60` | 14,780,000.00 USD | 14,780,000.00 USD | 1,280,000.00 USD | 136,380.00 USD | 258,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.40` | 16,160,000.00 USD | 16,160,000.00 USD | 1,120,000.00 USD | 69,260.00 USD | 194,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `769.20` | 16,610,000.00 USD | 16,610,000.00 USD | 346,750.00 USD | 64,540.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.00` | 17,430,000.00 USD | 17,430,000.00 USD | 590,250.00 USD | 149,540.00 USD | 82,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.80` | 18,210,000.00 USD | 18,210,000.00 USD | 560,270.00 USD | 88,510.00 USD | 131,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.60` | 18,740,000.00 USD | 18,740,000.00 USD | 413,630.00 USD | 63,410.00 USD | 53,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.40` | 19,480,000.00 USD | 19,480,000.00 USD | 552,350.00 USD | 156,720.00 USD | 36,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.20` | 20,270,000.00 USD | 20,270,000.00 USD | 462,000.00 USD | 89,950.00 USD | 229,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,270.00 USD | 9,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.00` | 21,540,000.00 USD | 21,540,000.00 USD | 1,130,000.00 USD | 62,620.00 USD | 83,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 130.12 USD | 9,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `774.80` | 22,000,000.00 USD | 22,000,000.00 USD | 340,920.00 USD | 63,940.00 USD | 56,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.60` | 22,570,000.00 USD | 22,570,000.00 USD | 388,710.00 USD | 102,110.00 USD | 73,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.40` | 22,910,000.00 USD | 22,910,000.00 USD | 282,120.00 USD | 46,920.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 1,050.00 USD | 10,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.20` | 23,280,000.00 USD | 23,280,000.00 USD | 199,140.00 USD | 73,680.00 USD | 102,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 2,880.00 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.00` | 24,570,000.00 USD | 24,570,000.00 USD | 1,080,000.00 USD | 98,430.00 USD | 106,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 11,100.00 USD | 24,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.80` | 25,270,000.00 USD | 25,270,000.00 USD | 559,680.00 USD | 46,430.00 USD | 96,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.60` | 26,090,000.00 USD | 26,090,000.00 USD | 624,940.00 USD | 77,740.00 USD | 116,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.40` | 26,580,000.00 USD | 26,580,000.00 USD | 388,410.00 USD | 51,300.00 USD | 55,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 5,730.00 USD | 30,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.20` | 27,060,000.00 USD | 27,060,000.00 USD | 219,490.00 USD | 112,470.00 USD | 140,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,620.00 USD | 32,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `782.00` | 27,990,000.00 USD | 27,990,000.00 USD | 819,350.00 USD | 22,830.00 USD | 91,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 247,020.00 USD | 279,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `782.80` | 29,090,000.00 USD | 29,090,000.00 USD | 841,750.00 USD | 90,120.00 USD | 166,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `783.50` | 2,910.00 USD | 282,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `783.60` | 29,700,000.00 USD | 29,700,000.00 USD | 538,790.00 USD | 14,770.00 USD | 53,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.40` | 29,870,000.00 USD | 29,870,000.00 USD | 113,020.00 USD | 32,520.00 USD | 29,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 2,220.00 USD | 284,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.20` | 30,260,000.00 USD | 30,260,000.00 USD | 340,190.00 USD | 22,730.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.00` | 30,560,000.00 USD | 30,560,000.00 USD | 232,430.00 USD | 26,950.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 607.96 USD | 284,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `786.80` | 30,820,000.00 USD | 30,820,000.00 USD | 212,420.00 USD | 29,580.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 130,890.00 USD | 415,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.60` | 31,100,000.00 USD | 31,100,000.00 USD | 235,710.00 USD | 41,700.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `788.40` | 31,410,000.00 USD | 31,410,000.00 USD | 147,170.00 USD | 42,560.00 USD | 118,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 126.16 USD | 415,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `789.20` | 31,890,000.00 USD | 31,890,000.00 USD | 431,710.00 USD | 24,090.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 1,980.00 USD | 417,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `790.00` | 32,140,000.00 USD | 32,140,000.00 USD | 200,110.00 USD | 28,260.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.80` | 32,360,000.00 USD | 32,360,000.00 USD | 166,790.00 USD | 36,750.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `791.50` | 6,430.00 USD | 424,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `791.60` | 32,510,000.00 USD | 32,510,000.00 USD | 146,160.00 USD | 7,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.40` | 32,570,000.00 USD | 32,570,000.00 USD | 57,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.20` | 32,620,000.00 USD | 32,620,000.00 USD | 46,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 158.70 USD | 424,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.00` | 32,640,000.00 USD | 32,640,000.00 USD | 26,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 179.56 USD | 424,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.80` | 32,680,000.00 USD | 32,680,000.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 425,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `795.60` | 32,720,000.00 USD | 32,720,000.00 USD | 38,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `796.40` | 32,750,000.00 USD | 32,750,000.00 USD | 30,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 172.84 USD | 425,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `797.20` | 32,820,000.00 USD | 32,820,000.00 USD | 71,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `798.00` | 32,850,000.00 USD | 32,850,000.00 USD | 30,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `798.80` | 32,870,000.00 USD | 32,870,000.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `799.60` | 32,890,000.00 USD | 32,890,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `800.40` | 32,900,000.00 USD | 32,900,000.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `801.20` | 32,910,000.00 USD | 32,910,000.00 USD | 16,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 761.42 USD | 426,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.00` | 32,930,000.00 USD | 32,930,000.00 USD | 21,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 426,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.80` | 32,950,000.00 USD | 32,950,000.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.60` | 32,960,000.00 USD | 32,960,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `804.40` | 32,960,000.00 USD | 32,960,000.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 1,080.00 USD | 427,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `805.20` | 32,970,000.00 USD | 32,970,000.00 USD | 7,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `806.00` | 32,970,000.00 USD | 32,970,000.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 44,210.00 USD | 471,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `806.80` | 32,980,000.00 USD | 32,980,000.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `807.60` | 33,000,000.00 USD | 33,000,000.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.40` | 33,010,000.00 USD | 33,010,000.00 USD | 10,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `809.20` | 33,010,000.00 USD | 33,010,000.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `810.00` | 33,010,000.00 USD | 33,010,000.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `810.50` | 5,440.00 USD | 477,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `810.80` | 33,010,000.00 USD | 33,010,000.00 USD | 859.37 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `811.50` | 265.36 USD | 477,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `812.40` | 33,020,000.00 USD | 33,020,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `813.20` | 33,040,000.00 USD | 33,040,000.00 USD | 15,920.00 USD | 4,540.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.00` | 33,080,000.00 USD | 33,080,000.00 USD | 18,950.00 USD | 8,810.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.80` | 33,120,000.00 USD | 33,120,000.00 USD | 27,210.00 USD | 13,270.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.60` | 33,150,000.00 USD | 33,150,000.00 USD | 11,690.00 USD | 3,300.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.40` | 33,200,000.00 USD | 33,200,000.00 USD | 45,010.00 USD | 8,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `817.20` | 33,250,000.00 USD | 33,250,000.00 USD | 32,410.00 USD | 17,190.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `818.00` | 33,280,000.00 USD | 33,280,000.00 USD | 19,050.00 USD | 0.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 205.44 USD | 477,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `818.80` | 33,460,000.00 USD | 33,460,000.00 USD | 174,720.00 USD | 2,750.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `819.60` | 33,490,000.00 USD | 33,490,000.00 USD | 16,520.00 USD | 4,460.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.40` | 33,550,000.00 USD | 33,550,000.00 USD | 38,810.00 USD | 6,990.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `821.20` | 33,580,000.00 USD | 33,580,000.00 USD | 27,220.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,840.00 USD | 489,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `821.90` | 33,630,000.00 USD | 33,630,000.00 USD | 47,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 1,730.00 USD | 491,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `825.50` | 9,970.00 USD | 501,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `828.50` | 302.40 USD | 501,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 502,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `835.50` | 340.88 USD | 502,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 625.70 USD | 503,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 125.62 USD | 503,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 572.54 USD | 504,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,680.00 USD | 506,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 153.34 USD | 507,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 173,300.00 USD | 680,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 338,650.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `849.50` | 416.25 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 108.99 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 138.43 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 171.10 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 265.59 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 6,240.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `866.50` | 236.55 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `868.50` | 1,530.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `869.50` | 452,190.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 11,910.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 4,540.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 915.72 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,120.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 1,780.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `888.50` | 636.17 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `889.50` | 772.09 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `892.50` | 3,350.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,120.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `897.50` | 382.33 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 392.04 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 901.23 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 891.38 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 38,590.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `914.50` | 926.39 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,450.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 285.05 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `938.50` | 3,270.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 952.65 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `944.50` | 112.40 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `945.50` | 110.62 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `958.50` | 67,090.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `962.50` | 202.12 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `963.50` | 838,250.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `965.50` | 1,930.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `975.50` | 59,900.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `982.50` | 26,130.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 1,640.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 99,050.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 172.39 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 1,570.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 704,240.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1020.50` | 9,650.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 103,250.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 676.71 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1049.50` | 294.91 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1056.50` | 4,820.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 391.27 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1071.50` | 1,550.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1118.50` | 6,160.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1128.50` | 20,120.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1144.50` | 55,290.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1147.50` | 153.77 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 9,150.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1169.50` | 367.22 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1173.50` | 14,380.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1185.50` | 158.86 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1188.50` | 133.11 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1203.50` | 30,070.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1208.50` | 385.51 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 8,570.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1226.50` | 199.92 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1236.50` | 1,240.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1243.50` | 4,170.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1252.50` | 8,250.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1260.50` | 341.60 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1264.50` | 202.32 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1282.50` | 162,720.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1283.50` | 115,520.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1313.50` | 781,180.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,140.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 102.29 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1354.50` | 20,320.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 246,510.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1375.50` | 158.18 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1381.50` | 5,520.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1402.50` | 178.12 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1411.50` | 10,180.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1413.50` | 139.94 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1432.50` | 360.99 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1444.50` | 697,520.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1466.50` | 8,980.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1470.50` | 14,460.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `156.50` | 4,520,000.00 USD | 0.00 USD | 159.16 USD | `-78.99%` | `1,017,000,000.00` |
| `Live` | `Long` | `166.50` | 4,520,000.00 USD | 0.00 USD | 607.23 USD | `-77.65%` | `3,647,000,000.00` |
| `Live` | `Long` | `178.50` | 4,520,000.00 USD | 0.00 USD | 239.90 USD | `-76.04%` | `1,344,000,000.00` |
| `Live` | `Long` | `202.50` | 4,520,000.00 USD | 0.00 USD | 124.74 USD | `-72.81%` | `616,000,000.00` |
| `Live` | `Long` | `206.50` | 4,520,000.00 USD | 0.00 USD | 295.71 USD | `-72.28%` | `1,432,000,000.00` |
| `Live` | `Long` | `211.50` | 4,520,000.00 USD | 0.00 USD | 1,360.00 USD | `-71.61%` | `6,450,000,000.00` |
| `Live` | `Long` | `212.50` | 4,520,000.00 USD | 0.00 USD | 260.74 USD | `-71.47%` | `1,227,000,000.00` |
| `Live` | `Long` | `217.50` | 4,520,000.00 USD | 0.00 USD | 1,090.00 USD | `-70.80%` | `5,000,000,000.00` |
| `Live` | `Long` | `219.50` | 4,520,000.00 USD | 0.00 USD | 191.18 USD | `-70.53%` | `871,000,000.00` |
| `Live` | `Long` | `228.50` | 4,520,000.00 USD | 0.00 USD | 4,210.00 USD | `-69.32%` | `18,405,000,000.00` |
| `Live` | `Long` | `234.50` | 4,510,000.00 USD | 0.00 USD | 306.02 USD | `-68.52%` | `1,305,000,000.00` |
| `Live` | `Long` | `257.50` | 4,510,000.00 USD | 0.00 USD | 4,370.00 USD | `-65.43%` | `16,965,000,000.00` |
| `Live` | `Long` | `265.50` | 4,510,000.00 USD | 0.00 USD | 835.53 USD | `-64.36%` | `3,147,000,000.00` |
| `Live` | `Long` | `274.50` | 4,510,000.00 USD | 0.00 USD | 21,760.00 USD | `-63.15%` | `79,269,000,000.00` |
| `Live` | `Long` | `301.50` | 4,490,000.00 USD | 0.00 USD | 6,050.00 USD | `-59.52%` | `20,052,000,000.00` |
| `Live` | `Long` | `303.50` | 4,480,000.00 USD | 0.00 USD | 22,510.00 USD | `-59.26%` | `74,167,000,000.00` |
| `Live` | `Long` | `304.50` | 4,460,000.00 USD | 0.00 USD | 349.57 USD | `-59.12%` | `1,148,000,000.00` |
| `Live` | `Long` | `306.50` | 4,460,000.00 USD | 0.00 USD | 299.45 USD | `-58.85%` | `977,000,000.00` |
| `Live` | `Long` | `308.50` | 4,460,000.00 USD | 0.00 USD | 977.02 USD | `-58.58%` | `3,167,000,000.00` |
| `Live` | `Long` | `310.50` | 4,450,000.00 USD | 0.00 USD | 1,590.00 USD | `-58.32%` | `5,132,000,000.00` |
| `Live` | `Long` | `313.50` | 4,450,000.00 USD | 0.00 USD | 501.60 USD | `-57.91%` | `1,600,000,000.00` |
| `Live` | `Long` | `315.50` | 4,450,000.00 USD | 0.00 USD | 1,450.00 USD | `-57.64%` | `4,603,000,000.00` |
| `Live` | `Long` | `316.50` | 4,450,000.00 USD | 0.00 USD | 21,900.00 USD | `-57.51%` | `69,189,000,000.00` |
| `Live` | `Long` | `323.50` | 4,430,000.00 USD | 0.00 USD | 895.12 USD | `-56.57%` | `2,767,000,000.00` |
| `Live` | `Long` | `326.50` | 4,430,000.00 USD | 0.00 USD | 500.85 USD | `-56.17%` | `1,534,000,000.00` |
| `Live` | `Long` | `328.50` | 4,430,000.00 USD | 0.00 USD | 315.03 USD | `-55.90%` | `959,000,000.00` |
| `Live` | `Long` | `332.50` | 4,430,000.00 USD | 0.00 USD | 1,650.00 USD | `-55.36%` | `4,951,000,000.00` |
| `Live` | `Long` | `333.50` | 4,430,000.00 USD | 0.00 USD | 377.19 USD | `-55.23%` | `1,131,000,000.00` |
| `Live` | `Long` | `334.50` | 4,430,000.00 USD | 0.00 USD | 312.09 USD | `-55.09%` | `933,000,000.00` |
| `Live` | `Long` | `342.50` | 4,430,000.00 USD | 0.00 USD | 1,120.00 USD | `-54.02%` | `3,259,000,000.00` |
| `Live` | `Long` | `343.50` | 4,420,000.00 USD | 0.00 USD | 652.65 USD | `-53.89%` | `1,900,000,000.00` |
| `Live` | `Long` | `350.50` | 4,420,000.00 USD | 0.00 USD | 1,580.00 USD | `-52.95%` | `4,504,000,000.00` |
| `Live` | `Long` | `352.50` | 4,420,000.00 USD | 0.00 USD | 12,030.00 USD | `-52.68%` | `34,129,000,000.00` |
| `Live` | `Long` | `359.50` | 4,410,000.00 USD | 0.00 USD | 366.69 USD | `-51.74%` | `1,020,000,000.00` |
| `Live` | `Long` | `366.50` | 4,410,000.00 USD | 0.00 USD | 549.75 USD | `-50.80%` | `1,500,000,000.00` |
| `Live` | `Long` | `370.50` | 4,410,000.00 USD | 0.00 USD | 103.00 USD | `-50.26%` | `278,000,000.00` |
| `Live` | `Long` | `374.50` | 4,410,000.00 USD | 0.00 USD | 240.43 USD | `-49.72%` | `642,000,000.00` |
| `Live` | `Long` | `377.50` | 4,410,000.00 USD | 0.00 USD | 1,240.00 USD | `-49.32%` | `3,277,000,000.00` |
| `Live` | `Long` | `378.50` | 4,410,000.00 USD | 0.00 USD | 3,910.00 USD | `-49.19%` | `10,318,000,000.00` |
| `Live` | `Long` | `379.50` | 4,400,000.00 USD | 0.00 USD | 645.15 USD | `-49.05%` | `1,700,000,000.00` |
| `Live` | `Long` | `382.50` | 4,400,000.00 USD | 0.00 USD | 1,910.00 USD | `-48.65%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 4,400,000.00 USD | 0.00 USD | 10,900.00 USD | `-48.52%` | `28,414,000,000.00` |
| `Live` | `Long` | `385.50` | 4,390,000.00 USD | 0.00 USD | 16,920.00 USD | `-48.25%` | `43,884,000,000.00` |
| `Live` | `Long` | `386.50` | 4,370,000.00 USD | 0.00 USD | 46,890.00 USD | `-48.11%` | `121,315,000,000.00` |
| `Live` | `Long` | `393.50` | 4,330,000.00 USD | 0.00 USD | 103.88 USD | `-47.17%` | `264,000,000.00` |
| `Live` | `Long` | `394.50` | 4,330,000.00 USD | 0.00 USD | 168.06 USD | `-47.04%` | `426,000,000.00` |
| `Live` | `Long` | `395.50` | 4,330,000.00 USD | 0.00 USD | 2,110.00 USD | `-46.90%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 4,320,000.00 USD | 0.00 USD | 396.50 USD | `-46.77%` | `1,000,000,000.00` |
| `Live` | `Long` | `397.50` | 4,320,000.00 USD | 0.00 USD | 318.00 USD | `-46.64%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 4,320,000.00 USD | 0.00 USD | 523.63 USD | `-46.50%` | `1,314,000,000.00` |
| `Live` | `Long` | `400.50` | 4,320,000.00 USD | 0.00 USD | 605.16 USD | `-46.23%` | `1,511,000,000.00` |
| `Live` | `Long` | `402.50` | 4,320,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.97%` | `3,941,000,000.00` |
| `Live` | `Long` | `404.50` | 4,320,000.00 USD | 0.00 USD | 102.34 USD | `-45.70%` | `253,000,000.00` |
| `Live` | `Long` | `408.50` | 4,320,000.00 USD | 0.00 USD | 3,450.00 USD | `-45.16%` | `8,455,000,000.00` |
| `Live` | `Long` | `409.50` | 4,320,000.00 USD | 0.00 USD | 28,660.00 USD | `-45.03%` | `70,000,000,000.00` |
| `Live` | `Long` | `410.50` | 4,290,000.00 USD | 0.00 USD | 614.52 USD | `-44.89%` | `1,497,000,000.00` |
| `Live` | `Long` | `411.50` | 4,290,000.00 USD | 0.00 USD | 106.17 USD | `-44.76%` | `258,000,000.00` |
| `Live` | `Long` | `414.50` | 4,290,000.00 USD | 0.00 USD | 13,320.00 USD | `-44.35%` | `32,128,000,000.00` |
| `Live` | `Long` | `415.50` | 4,270,000.00 USD | 0.00 USD | 1,810.00 USD | `-44.22%` | `4,368,000,000.00` |
| `Live` | `Long` | `416.50` | 4,270,000.00 USD | 0.00 USD | 350.69 USD | `-44.09%` | `842,000,000.00` |
| `Live` | `Long` | `417.50` | 4,270,000.00 USD | 0.00 USD | 7,140.00 USD | `-43.95%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 4,260,000.00 USD | 0.00 USD | 465.79 USD | `-43.82%` | `1,113,000,000.00` |
| `Live` | `Long` | `420.50` | 4,260,000.00 USD | 0.00 USD | 2,660.00 USD | `-43.55%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 4,260,000.00 USD | 0.00 USD | 2,320.00 USD | `-43.41%` | `5,496,000,000.00` |
| `Live` | `Long` | `423.50` | 4,260,000.00 USD | 0.00 USD | 1,450.00 USD | `-43.15%` | `3,419,000,000.00` |
| `Live` | `Long` | `427.50` | 4,260,000.00 USD | 0.00 USD | 141.93 USD | `-42.61%` | `332,000,000.00` |
| `Live` | `Long` | `430.50` | 4,260,000.00 USD | 0.00 USD | 638.00 USD | `-42.21%` | `1,482,000,000.00` |
| `Live` | `Long` | `431.50` | 4,260,000.00 USD | 0.00 USD | 582.09 USD | `-42.07%` | `1,349,000,000.00` |
| `Live` | `Long` | `439.50` | 4,260,000.00 USD | 0.00 USD | 1,800.00 USD | `-41.00%` | `4,087,000,000.00` |
| `Live` | `Long` | `451.50` | 4,250,000.00 USD | 0.00 USD | 12,680.00 USD | `-39.39%` | `28,093,000,000.00` |
| `Live` | `Long` | `454.50` | 4,240,000.00 USD | 0.00 USD | 4,220.00 USD | `-38.98%` | `9,287,000,000.00` |
| `Live` | `Long` | `455.50` | 4,240,000.00 USD | 0.00 USD | 1,070.00 USD | `-38.85%` | `2,339,000,000.00` |
| `Live` | `Long` | `456.50` | 4,240,000.00 USD | 0.00 USD | 13,790.00 USD | `-38.72%` | `30,201,000,000.00` |
| `Live` | `Long` | `457.50` | 4,220,000.00 USD | 0.00 USD | 463.45 USD | `-38.58%` | `1,013,000,000.00` |
| `Live` | `Long` | `467.50` | 4,220,000.00 USD | 0.00 USD | 1,950.00 USD | `-37.24%` | `4,170,000,000.00` |
| `Live` | `Long` | `469.50` | 4,220,000.00 USD | 0.00 USD | 5,450.00 USD | `-36.97%` | `11,600,000,000.00` |
| `Live` | `Long` | `470.50` | 4,220,000.00 USD | 0.00 USD | 5,410.00 USD | `-36.84%` | `11,499,000,000.00` |
| `Live` | `Long` | `476.50` | 4,210,000.00 USD | 0.00 USD | 5,800.00 USD | `-36.03%` | `12,182,000,000.00` |
| `Live` | `Long` | `486.50` | 4,200,000.00 USD | 0.00 USD | 2,550.00 USD | `-34.69%` | `5,235,000,000.00` |
| `Live` | `Long` | `498.50` | 4,200,000.00 USD | 0.00 USD | 2,120.00 USD | `-33.08%` | `4,246,000,000.00` |
| `Live` | `Long` | `501.50` | 4,200,000.00 USD | 0.00 USD | 7,760.00 USD | `-32.67%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 4,190,000.00 USD | 0.00 USD | 109.04 USD | `-32.54%` | `217,000,000.00` |
| `Live` | `Long` | `509.50` | 4,190,000.00 USD | 0.00 USD | 3,610.00 USD | `-31.60%` | `7,091,000,000.00` |
| `Live` | `Long` | `511.50` | 4,190,000.00 USD | 0.00 USD | 3,240.00 USD | `-31.33%` | `6,344,000,000.00` |
| `Live` | `Long` | `512.50` | 4,180,000.00 USD | 0.00 USD | 5,440.00 USD | `-31.20%` | `10,618,000,000.00` |
| `Live` | `Long` | `514.50` | 4,180,000.00 USD | 0.00 USD | 4,010.00 USD | `-30.93%` | `7,787,000,000.00` |
| `Live` | `Long` | `515.50` | 4,180,000.00 USD | 0.00 USD | 3,930.00 USD | `-30.80%` | `7,626,000,000.00` |
| `Live` | `Long` | `516.50` | 4,170,000.00 USD | 0.00 USD | 4,290.00 USD | `-30.66%` | `8,303,000,000.00` |
| `Live` | `Long` | `517.50` | 4,170,000.00 USD | 0.00 USD | 1,160.00 USD | `-30.53%` | `2,246,000,000.00` |
| `Live` | `Long` | `519.50` | 4,170,000.00 USD | 0.00 USD | 3,360.00 USD | `-30.26%` | `6,473,000,000.00` |
| `Live` | `Long` | `520.50` | 4,160,000.00 USD | 0.00 USD | 3,560.00 USD | `-30.12%` | `6,833,000,000.00` |
| `Live` | `Long` | `521.50` | 4,160,000.00 USD | 0.00 USD | 1,040.00 USD | `-29.99%` | `1,987,000,000.00` |
| `Live` | `Long` | `522.50` | 4,160,000.00 USD | 0.00 USD | 10,750.00 USD | `-29.86%` | `20,569,000,000.00` |
| `Live` | `Long` | `523.50` | 4,150,000.00 USD | 0.00 USD | 2,300.00 USD | `-29.72%` | `4,393,000,000.00` |
| `Live` | `Long` | `524.50` | 4,140,000.00 USD | 0.00 USD | 1,460.00 USD | `-29.59%` | `2,790,000,000.00` |
| `Live` | `Long` | `525.50` | 4,140,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.45%` | `2,298,000,000.00` |
| `Live` | `Long` | `526.50` | 4,140,000.00 USD | 0.00 USD | 4,130.00 USD | `-29.32%` | `7,843,000,000.00` |
| `Live` | `Long` | `529.50` | 4,140,000.00 USD | 0.00 USD | 42,820.00 USD | `-28.92%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 4,100,000.00 USD | 0.00 USD | 16,980.00 USD | `-28.78%` | `32,010,000,000.00` |
| `Live` | `Long` | `531.50` | 4,080,000.00 USD | 0.00 USD | 1,630.00 USD | `-28.65%` | `3,067,000,000.00` |
| `Live` | `Long` | `532.50` | 4,080,000.00 USD | 0.00 USD | 632.08 USD | `-28.51%` | `1,187,000,000.00` |
| `Live` | `Long` | `534.50` | 4,080,000.00 USD | 0.00 USD | 555.35 USD | `-28.24%` | `1,039,000,000.00` |
| `Live` | `Long` | `536.50` | 4,080,000.00 USD | 0.00 USD | 100.33 USD | `-27.98%` | `187,000,000.00` |
| `Live` | `Long` | `537.50` | 4,080,000.00 USD | 0.00 USD | 4,300.00 USD | `-27.84%` | `8,000,000,000.00` |
| `Live` | `Long` | `539.50` | 4,070,000.00 USD | 0.00 USD | 490.94 USD | `-27.57%` | `910,000,000.00` |
| `Live` | `Long` | `541.50` | 4,070,000.00 USD | 0.00 USD | 472.19 USD | `-27.30%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 4,070,000.00 USD | 0.00 USD | 4,380.00 USD | `-27.04%` | `8,053,000,000.00` |
| `Live` | `Long` | `544.50` | 4,070,000.00 USD | 0.00 USD | 272.25 USD | `-26.90%` | `500,000,000.00` |
| `Live` | `Long` | `545.50` | 4,070,000.00 USD | 0.00 USD | 212,310.00 USD | `-26.77%` | `389,204,000,000.00` |
| `Live` | `Long` | `546.50` | 3,850,000.00 USD | 0.00 USD | 13,970.00 USD | `-26.63%` | `25,561,000,000.00` |
| `Live` | `Long` | `547.50` | 3,840,000.00 USD | 0.00 USD | 531.07 USD | `-26.50%` | `970,000,000.00` |
| `Live` | `Long` | `549.50` | 3,840,000.00 USD | 0.00 USD | 1,770.00 USD | `-26.23%` | `3,224,000,000.00` |
| `Live` | `Long` | `550.50` | 3,840,000.00 USD | 0.00 USD | 633.63 USD | `-26.10%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 3,840,000.00 USD | 0.00 USD | 1,290.00 USD | `-25.96%` | `2,336,000,000.00` |
| `Live` | `Long` | `552.50` | 3,830,000.00 USD | 0.00 USD | 959.69 USD | `-25.83%` | `1,737,000,000.00` |
| `Live` | `Long` | `553.50` | 3,830,000.00 USD | 0.00 USD | 2,420.00 USD | `-25.69%` | `4,365,000,000.00` |
| `Live` | `Long` | `554.50` | 3,830,000.00 USD | 0.00 USD | 2,010.00 USD | `-25.56%` | `3,625,000,000.00` |
| `Live` | `Long` | `555.50` | 3,830,000.00 USD | 0.00 USD | 591.61 USD | `-25.43%` | `1,065,000,000.00` |
| `Live` | `Long` | `557.50` | 3,830,000.00 USD | 0.00 USD | 5,680.00 USD | `-25.16%` | `10,193,000,000.00` |
| `Live` | `Long` | `559.50` | 3,820,000.00 USD | 0.00 USD | 212.61 USD | `-24.89%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 3,820,000.00 USD | 0.00 USD | 10,280.00 USD | `-24.75%` | `18,342,000,000.00` |
| `Live` | `Long` | `561.50` | 3,810,000.00 USD | 0.00 USD | 583.40 USD | `-24.62%` | `1,039,000,000.00` |
| `Live` | `Long` | `564.50` | 3,810,000.00 USD | 0.00 USD | 14,880.00 USD | `-24.22%` | `26,354,000,000.00` |
| `Live` | `Long` | `566.50` | 3,800,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-23.95%` | `2,805,710,000,000.00` |
| `Live` | `Long` | `570.50` | 2,210,000.00 USD | 0.00 USD | 393.64 USD | `-23.41%` | `690,000,000.00` |
| `Live` | `Long` | `572.50` | 2,210,000.00 USD | 0.00 USD | 715,280.00 USD | `-23.14%` | `1,249,401,000,000.00` |
| `Live` | `Long` | `574.50` | 1,490,000.00 USD | 0.00 USD | 323.44 USD | `-22.87%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 1,490,000.00 USD | 0.00 USD | 862.44 USD | `-22.61%` | `1,496,000,000.00` |
| `Live` | `Long` | `577.50` | 1,490,000.00 USD | 0.00 USD | 222.91 USD | `-22.47%` | `386,000,000.00` |
| `Live` | `Long` | `578.50` | 1,490,000.00 USD | 0.00 USD | 275.37 USD | `-22.34%` | `476,000,000.00` |
| `Live` | `Long` | `579.50` | 1,490,000.00 USD | 0.00 USD | 2,320.00 USD | `-22.20%` | `4,005,000,000.00` |
| `Live` | `Long` | `583.50` | 1,490,000.00 USD | 0.00 USD | 15,440.00 USD | `-21.67%` | `26,453,000,000.00` |
| `Live` | `Long` | `584.50` | 1,470,000.00 USD | 0.00 USD | 10,240.00 USD | `-21.53%` | `17,522,000,000.00` |
| `Live` | `Long` | `585.50` | 1,460,000.00 USD | 0.00 USD | 666.88 USD | `-21.40%` | `1,139,000,000.00` |
| `Live` | `Long` | `586.50` | 1,460,000.00 USD | 0.00 USD | 2,540.00 USD | `-21.26%` | `4,339,000,000.00` |
| `Live` | `Long` | `587.50` | 1,460,000.00 USD | 0.00 USD | 1,530.00 USD | `-21.13%` | `2,612,000,000.00` |
| `Live` | `Long` | `590.50` | 1,460,000.00 USD | 0.00 USD | 100.39 USD | `-20.73%` | `170,000,000.00` |
| `Live` | `Long` | `594.50` | 1,460,000.00 USD | 0.00 USD | 44,800.00 USD | `-20.19%` | `75,354,000,000.00` |
| `Live` | `Long` | `595.50` | 1,410,000.00 USD | 0.00 USD | 1,680.00 USD | `-20.06%` | `2,814,000,000.00` |
| `Live` | `Long` | `597.50` | 1,410,000.00 USD | 0.00 USD | 100.98 USD | `-19.79%` | `169,000,000.00` |
| `Live` | `Long` | `598.50` | 1,410,000.00 USD | 0.00 USD | 1,060.00 USD | `-19.65%` | `1,766,000,000.00` |
| `Live` | `Long` | `599.50` | 1,410,000.00 USD | 0.00 USD | 116.90 USD | `-19.52%` | `195,000,000.00` |
| `Live` | `Long` | `600.50` | 1,410,000.00 USD | 0.00 USD | 945.19 USD | `-19.38%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,410,000.00 USD | 0.00 USD | 303.76 USD | `-19.25%` | `505,000,000.00` |
| `Live` | `Long` | `604.50` | 1,410,000.00 USD | 0.00 USD | 1,610.00 USD | `-18.85%` | `2,671,000,000.00` |
| `Live` | `Long` | `605.50` | 1,410,000.00 USD | 0.00 USD | 508.62 USD | `-18.71%` | `840,000,000.00` |
| `Live` | `Long` | `607.50` | 1,410,000.00 USD | 0.00 USD | 2,210.00 USD | `-18.44%` | `3,633,000,000.00` |
| `Live` | `Long` | `610.50` | 1,400,000.00 USD | 0.00 USD | 213.67 USD | `-18.04%` | `350,000,000.00` |
| `Live` | `Long` | `613.50` | 1,400,000.00 USD | 0.00 USD | 527.00 USD | `-17.64%` | `859,000,000.00` |
| `Live` | `Long` | `614.50` | 1,400,000.00 USD | 0.00 USD | 2,280.00 USD | `-17.50%` | `3,710,000,000.00` |
| `Live` | `Long` | `615.50` | 1,400,000.00 USD | 0.00 USD | 427.16 USD | `-17.37%` | `694,000,000.00` |
| `Live` | `Long` | `616.50` | 1,400,000.00 USD | 0.00 USD | 1,510.00 USD | `-17.24%` | `2,450,000,000.00` |
| `Live` | `Long` | `617.50` | 1,400,000.00 USD | 0.00 USD | 343.33 USD | `-17.10%` | `556,000,000.00` |
| `Live` | `Long` | `620.50` | 1,400,000.00 USD | 0.00 USD | 5,410.00 USD | `-16.70%` | `8,712,000,000.00` |
| `Live` | `Long` | `621.50` | 1,390,000.00 USD | 0.00 USD | 1,260.00 USD | `-16.56%` | `2,020,000,000.00` |
| `Live` | `Long` | `622.50` | 1,390,000.00 USD | 0.00 USD | 2,110.00 USD | `-16.43%` | `3,397,000,000.00` |
| `Live` | `Long` | `623.50` | 1,390,000.00 USD | 0.00 USD | 1,050.00 USD | `-16.30%` | `1,691,000,000.00` |
| `Live` | `Long` | `624.50` | 1,390,000.00 USD | 0.00 USD | 3,460.00 USD | `-16.16%` | `5,547,000,000.00` |
| `Live` | `Long` | `625.50` | 1,390,000.00 USD | 0.00 USD | 11,970.00 USD | `-16.03%` | `19,142,000,000.00` |
| `Live` | `Long` | `626.50` | 1,370,000.00 USD | 0.00 USD | 16,020.00 USD | `-15.89%` | `25,566,000,000.00` |
| `Live` | `Long` | `627.50` | 1,360,000.00 USD | 0.00 USD | 326.30 USD | `-15.76%` | `520,000,000.00` |
| `Live` | `Long` | `628.50` | 1,360,000.00 USD | 0.00 USD | 664.32 USD | `-15.63%` | `1,057,000,000.00` |
| `Live` | `Long` | `629.50` | 1,360,000.00 USD | 0.00 USD | 3,680.00 USD | `-15.49%` | `5,849,000,000.00` |
| `Live` | `Long` | `631.50` | 1,350,000.00 USD | 0.00 USD | 6,320.00 USD | `-15.22%` | `10,000,000,000.00` |
| `Live` | `Long` | `632.50` | 1,350,000.00 USD | 0.00 USD | 125.87 USD | `-15.09%` | `199,000,000.00` |
| `Live` | `Long` | `633.50` | 1,350,000.00 USD | 0.00 USD | 1,920.00 USD | `-14.95%` | `3,038,000,000.00` |
| `Live` | `Long` | `634.50` | 1,340,000.00 USD | 0.00 USD | 276.64 USD | `-14.82%` | `436,000,000.00` |
| `Live` | `Long` | `635.50` | 1,340,000.00 USD | 0.00 USD | 5,910.00 USD | `-14.69%` | `9,302,000,000.00` |
| `Live` | `Long` | `636.50` | 1,340,000.00 USD | 0.00 USD | 5,140.00 USD | `-14.55%` | `8,083,000,000.00` |
| `Live` | `Long` | `637.50` | 1,330,000.00 USD | 0.00 USD | 1,110.00 USD | `-14.42%` | `1,743,000,000.00` |
| `Live` | `Long` | `638.50` | 1,330,000.00 USD | 0.00 USD | 432.90 USD | `-14.28%` | `678,000,000.00` |
| `Live` | `Long` | `639.50` | 1,330,000.00 USD | 0.00 USD | 33,550.00 USD | `-14.15%` | `52,460,000,000.00` |
| `Live` | `Long` | `640.50` | 1,300,000.00 USD | 0.00 USD | 2,310.00 USD | `-14.01%` | `3,600,000,000.00` |
| `Live` | `Long` | `641.50` | 1,300,000.00 USD | 0.00 USD | 1,670.00 USD | `-13.88%` | `2,606,000,000.00` |
| `Live` | `Long` | `642.50` | 1,290,000.00 USD | 0.00 USD | 9,470.00 USD | `-13.75%` | `14,732,000,000.00` |
| `Live` | `Long` | `643.50` | 1,280,000.00 USD | 0.00 USD | 8,490.00 USD | `-13.61%` | `13,199,000,000.00` |
| `Live` | `Long` | `645.50` | 1,280,000.00 USD | 0.00 USD | 3,820.00 USD | `-13.34%` | `5,914,000,000.00` |
| `Live` | `Long` | `646.50` | 1,270,000.00 USD | 0.00 USD | 4,290.00 USD | `-13.21%` | `6,631,000,000.00` |
| `Live` | `Long` | `649.50` | 1,270,000.00 USD | 0.00 USD | 136.39 USD | `-12.81%` | `210,000,000.00` |
| `Live` | `Long` | `650.50` | 1,270,000.00 USD | 0.00 USD | 424.13 USD | `-12.67%` | `652,000,000.00` |
| `Live` | `Long` | `651.50` | 1,270,000.00 USD | 0.00 USD | 633.26 USD | `-12.54%` | `972,000,000.00` |
| `Live` | `Long` | `654.50` | 1,270,000.00 USD | 0.00 USD | 97,530.00 USD | `-12.13%` | `149,014,000,000.00` |
| `Live` | `Long` | `655.50` | 1,170,000.00 USD | 0.00 USD | 2,250.00 USD | `-12.00%` | `3,440,000,000.00` |
| `Live` | `Long` | `656.50` | 1,170,000.00 USD | 0.00 USD | 122.77 USD | `-11.87%` | `187,000,000.00` |
| `Live` | `Long` | `658.50` | 1,170,000.00 USD | 0.00 USD | 4,800.00 USD | `-11.60%` | `7,282,000,000.00` |
| `Live` | `Long` | `660.50` | 1,160,000.00 USD | 0.00 USD | 3,340.00 USD | `-11.33%` | `5,053,000,000.00` |
| `Live` | `Long` | `661.50` | 1,160,000.00 USD | 0.00 USD | 463.71 USD | `-11.19%` | `701,000,000.00` |
| `Live` | `Long` | `662.50` | 1,160,000.00 USD | 0.00 USD | 19,830.00 USD | `-11.06%` | `29,930,000,000.00` |
| `Live` | `Long` | `663.50` | 1,140,000.00 USD | 0.00 USD | 2,070.00 USD | `-10.93%` | `3,115,000,000.00` |
| `Live` | `Long` | `666.50` | 1,140,000.00 USD | 0.00 USD | 5,440.00 USD | `-10.52%` | `8,159,000,000.00` |
| `Live` | `Long` | `669.50` | 1,130,000.00 USD | 0.00 USD | 3,040.00 USD | `-10.12%` | `4,542,000,000.00` |
| `Live` | `Long` | `670.50` | 1,130,000.00 USD | 0.00 USD | 2,570.00 USD | `-9.99%` | `3,839,000,000.00` |
| `Live` | `Long` | `671.50` | 1,130,000.00 USD | 0.00 USD | 3,360.00 USD | `-9.85%` | `5,000,000,000.00` |
| `Live` | `Long` | `672.50` | 1,120,000.00 USD | 0.00 USD | 13,000.00 USD | `-9.72%` | `19,329,000,000.00` |
| `Live` | `Long` | `673.50` | 1,110,000.00 USD | 0.00 USD | 567.76 USD | `-9.58%` | `843,000,000.00` |
| `Live` | `Long` | `674.50` | 1,110,000.00 USD | 0.00 USD | 259.68 USD | `-9.45%` | `385,000,000.00` |
| `Live` | `Long` | `678.50` | 1,110,000.00 USD | 0.00 USD | 1,610.00 USD | `-8.91%` | `2,375,000,000.00` |
| `Live` | `Long` | `681.50` | 1,110,000.00 USD | 0.00 USD | 31,450.00 USD | `-8.51%` | `46,154,000,000.00` |
| `Live` | `Long` | `684.50` | 1,080,000.00 USD | 0.00 USD | 42,430.00 USD | `-8.11%` | `61,984,000,000.00` |
| `Live` | `Long` | `685.50` | 1,030,000.00 USD | 0.00 USD | 1,290.00 USD | `-7.97%` | `1,882,000,000.00` |
| `Live` | `Long` | `686.50` | 1,030,000.00 USD | 0.00 USD | 2,280.00 USD | `-7.84%` | `3,322,000,000.00` |
| `Live` | `Long` | `687.50` | 1,030,000.00 USD | 0.00 USD | 198.69 USD | `-7.70%` | `289,000,000.00` |
| `Live` | `Long` | `689.50` | 1,030,000.00 USD | 0.00 USD | 885.32 USD | `-7.44%` | `1,284,000,000.00` |
| `Live` | `Long` | `690.50` | 1,030,000.00 USD | 0.00 USD | 7,080.00 USD | `-7.30%` | `10,260,000,000.00` |
| `Live` | `Long` | `691.50` | 1,020,000.00 USD | 0.00 USD | 5,430.00 USD | `-7.17%` | `7,853,000,000.00` |
| `Live` | `Long` | `692.50` | 1,020,000.00 USD | 0.00 USD | 5,580.00 USD | `-7.03%` | `8,061,000,000.00` |
| `Live` | `Long` | `693.50` | 1,010,000.00 USD | 0.00 USD | 2,590.00 USD | `-6.90%` | `3,732,000,000.00` |
| `Live` | `Long` | `694.50` | 1,010,000.00 USD | 0.00 USD | 513.93 USD | `-6.76%` | `740,000,000.00` |
| `Live` | `Long` | `695.50` | 1,010,000.00 USD | 0.00 USD | 470.85 USD | `-6.63%` | `677,000,000.00` |
| `Live` | `Long` | `697.50` | 1,010,000.00 USD | 0.00 USD | 2,340.00 USD | `-6.36%` | `3,353,000,000.00` |
| `Live` | `Long` | `698.50` | 1,000,000.00 USD | 0.00 USD | 303.15 USD | `-6.23%` | `434,000,000.00` |
| `Live` | `Long` | `699.50` | 1,000,000.00 USD | 0.00 USD | 20,100.00 USD | `-6.09%` | `28,732,000,000.00` |
| `Live` | `Long` | `700.50` | 983,880.00 USD | 0.00 USD | 1,130.00 USD | `-5.96%` | `1,612,000,000.00` |
| `Live` | `Long` | `702.50` | 982,750.00 USD | 0.00 USD | 2,080.00 USD | `-5.69%` | `2,956,000,000.00` |
| `Live` | `Long` | `703.50` | 980,670.00 USD | 0.00 USD | 3,820.00 USD | `-5.56%` | `5,425,000,000.00` |
| `Live` | `Long` | `704.50` | 976,860.00 USD | 0.00 USD | 2,720.00 USD | `-5.42%` | `3,857,000,000.00` |
| `Live` | `Long` | `705.50` | 974,140.00 USD | 0.00 USD | 88,830.00 USD | `-5.29%` | `125,913,000,000.00` |
| `Live` | `Long` | `706.50` | 885,310.00 USD | 0.00 USD | 34,680.00 USD | `-5.15%` | `49,089,000,000.00` |
| `Live` | `Long` | `707.50` | 850,630.00 USD | 0.00 USD | 22,380.00 USD | `-5.02%` | `31,637,000,000.00` |
| `Live` | `Long` | `708.50` | 828,240.00 USD | 0.00 USD | 171,950.00 USD | `-4.89%` | `242,695,000,000.00` |
| `Live` | `Long` | `709.50` | 656,290.00 USD | 0.00 USD | 339,560.00 USD | `-4.75%` | `478,597,000,000.00` |
| `Live` | `Long` | `710.50` | 316,730.00 USD | 0.00 USD | 46,020.00 USD | `-4.62%` | `64,773,000,000.00` |
| `Live` | `Long` | `711.50` | 270,710.00 USD | 0.00 USD | 11,630.00 USD | `-4.48%` | `16,350,000,000.00` |
| `Live` | `Long` | `712.50` | 259,070.00 USD | 0.00 USD | 229,760.00 USD | `-4.35%` | `322,464,000,000.00` |
| `Live` | `Long` | `713.50` | 29,320.00 USD | 0.00 USD | 20,280.00 USD | `-4.21%` | `28,425,000,000.00` |
| `Live` | `Long` | `714.50` | 9,040.00 USD | 0.00 USD | 157.90 USD | `-4.08%` | `221,000,000.00` |
| `Live` | `Long` | `716.50` | 8,880.00 USD | 0.00 USD | 789.58 USD | `-3.81%` | `1,102,000,000.00` |
| `Live` | `Long` | `717.50` | 8,090.00 USD | 0.00 USD | 3,700.00 USD | `-3.68%` | `5,155,000,000.00` |
| `Live` | `Long` | `718.50` | 4,390.00 USD | 0.00 USD | 104.18 USD | `-3.54%` | `145,000,000.00` |
| `Live` | `Long` | `721.50` | 4,290.00 USD | 0.00 USD | 998.56 USD | `-3.14%` | `1,384,000,000.00` |
| `Live` | `Long` | `731.50` | 3,290.00 USD | 0.00 USD | 3,290.00 USD | `-1.80%` | `4,496,000,000.00` |
| `Live` | `Short` | `763.50` | 211.49 USD | 211.49 USD | 0.00 USD | `+2.50%` | `277,000,000.00` |
| `Live` | `Short` | `767.50` | 1,260.00 USD | 1,050.00 USD | 0.00 USD | `+3.04%` | `1,365,000,000.00` |
| `Live` | `Short` | `768.50` | 1,420.00 USD | 156.77 USD | 0.00 USD | `+3.17%` | `204,000,000.00` |
| `Live` | `Short` | `773.50` | 9,690.00 USD | 8,270.00 USD | 0.00 USD | `+3.84%` | `10,692,000,000.00` |
| `Live` | `Short` | `774.50` | 9,820.00 USD | 130.12 USD | 0.00 USD | `+3.98%` | `168,000,000.00` |
| `Live` | `Short` | `776.50` | 10,870.00 USD | 1,050.00 USD | 0.00 USD | `+4.24%` | `1,351,000,000.00` |
| `Live` | `Short` | `777.50` | 13,750.00 USD | 2,880.00 USD | 0.00 USD | `+4.38%` | `3,705,000,000.00` |
| `Live` | `Short` | `778.50` | 24,850.00 USD | 11,100.00 USD | 0.00 USD | `+4.51%` | `14,263,000,000.00` |
| `Live` | `Short` | `779.50` | 25,150.00 USD | 301.67 USD | 0.00 USD | `+4.65%` | `387,000,000.00` |
| `Live` | `Short` | `780.50` | 30,580.00 USD | 5,430.00 USD | 0.00 USD | `+4.78%` | `6,956,000,000.00` |
| `Live` | `Short` | `781.50` | 32,200.00 USD | 1,620.00 USD | 0.00 USD | `+4.91%` | `2,073,000,000.00` |
| `Live` | `Short` | `782.50` | 279,220.00 USD | 247,020.00 USD | 0.00 USD | `+5.05%` | `315,684,000,000.00` |
| `Live` | `Short` | `784.50` | 281,440.00 USD | 2,220.00 USD | 0.00 USD | `+5.32%` | `2,830,000,000.00` |
| `Live` | `Short` | `786.50` | 282,050.00 USD | 607.96 USD | 0.00 USD | `+5.59%` | `773,000,000.00` |
| `Live` | `Short` | `787.50` | 412,940.00 USD | 130,890.00 USD | 0.00 USD | `+5.72%` | `166,210,000,000.00` |
| `Live` | `Short` | `788.50` | 413,070.00 USD | 126.16 USD | 0.00 USD | `+5.85%` | `160,000,000.00` |
| `Live` | `Short` | `789.50` | 415,050.00 USD | 1,980.00 USD | 0.00 USD | `+5.99%` | `2,511,000,000.00` |
| `Live` | `Short` | `791.50` | 421,480.00 USD | 6,430.00 USD | 0.00 USD | `+6.26%` | `8,118,000,000.00` |
| `Live` | `Short` | `793.50` | 421,630.00 USD | 158.70 USD | 0.00 USD | `+6.53%` | `200,000,000.00` |
| `Live` | `Short` | `794.50` | 421,810.00 USD | 179.56 USD | 0.00 USD | `+6.66%` | `226,000,000.00` |
| `Live` | `Short` | `795.50` | 422,330.00 USD | 518.67 USD | 0.00 USD | `+6.79%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 422,510.00 USD | 172.84 USD | 0.00 USD | `+6.93%` | `217,000,000.00` |
| `Live` | `Short` | `801.50` | 423,270.00 USD | 761.42 USD | 0.00 USD | `+7.60%` | `950,000,000.00` |
| `Live` | `Short` | `802.50` | 423,550.00 USD | 279.27 USD | 0.00 USD | `+7.73%` | `348,000,000.00` |
| `Live` | `Short` | `804.50` | 424,620.00 USD | 1,080.00 USD | 0.00 USD | `+8.00%` | `1,338,000,000.00` |
| `Live` | `Short` | `806.50` | 468,830.00 USD | 44,210.00 USD | 0.00 USD | `+8.27%` | `54,814,000,000.00` |
| `Live` | `Short` | `810.50` | 474,270.00 USD | 5,440.00 USD | 0.00 USD | `+8.81%` | `6,710,000,000.00` |
| `Live` | `Short` | `811.50` | 474,530.00 USD | 265.36 USD | 0.00 USD | `+8.94%` | `327,000,000.00` |
| `Live` | `Short` | `818.50` | 474,740.00 USD | 205.44 USD | 0.00 USD | `+9.88%` | `251,000,000.00` |
| `Live` | `Short` | `821.50` | 486,580.00 USD | 11,840.00 USD | 0.00 USD | `+10.28%` | `14,418,000,000.00` |
| `Live` | `Short` | `823.50` | 488,310.00 USD | 1,730.00 USD | 0.00 USD | `+10.55%` | `2,102,000,000.00` |
| `Live` | `Short` | `831.50` | 498,350.00 USD | 10,040.00 USD | 0.00 USD | `+11.63%` | `12,072,000,000.00` |
| `Live` | `Short` | `834.50` | 499,360.00 USD | 1,010.00 USD | 0.00 USD | `+12.03%` | `1,206,000,000.00` |
| `Live` | `Short` | `835.50` | 499,700.00 USD | 340.88 USD | 0.00 USD | `+12.16%` | `408,000,000.00` |
| `Live` | `Short` | `836.50` | 500,330.00 USD | 625.70 USD | 0.00 USD | `+12.30%` | `748,000,000.00` |
| `Live` | `Short` | `837.50` | 500,450.00 USD | 125.62 USD | 0.00 USD | `+12.43%` | `150,000,000.00` |
| `Live` | `Short` | `839.50` | 501,020.00 USD | 572.54 USD | 0.00 USD | `+12.70%` | `682,000,000.00` |
| `Live` | `Short` | `841.50` | 503,700.00 USD | 2,680.00 USD | 0.00 USD | `+12.97%` | `3,182,000,000.00` |
| `Live` | `Short` | `842.50` | 503,850.00 USD | 153.34 USD | 0.00 USD | `+13.10%` | `182,000,000.00` |
| `Live` | `Short` | `843.50` | 677,160.00 USD | 173,300.00 USD | 0.00 USD | `+13.24%` | `205,454,000,000.00` |
| `Live` | `Short` | `845.50` | 1,020,000.00 USD | 338,650.00 USD | 0.00 USD | `+13.51%` | `400,529,000,000.00` |
| `Live` | `Short` | `848.50` | 1,020,000.00 USD | 289.34 USD | 0.00 USD | `+13.91%` | `341,000,000.00` |
| `Live` | `Short` | `849.50` | 1,020,000.00 USD | 416.25 USD | 0.00 USD | `+14.04%` | `490,000,000.00` |
| `Live` | `Short` | `851.50` | 1,020,000.00 USD | 108.99 USD | 0.00 USD | `+14.31%` | `128,000,000.00` |
| `Live` | `Short` | `854.50` | 1,020,000.00 USD | 138.43 USD | 0.00 USD | `+14.71%` | `162,000,000.00` |
| `Live` | `Short` | `855.50` | 1,020,000.00 USD | 171.10 USD | 0.00 USD | `+14.85%` | `200,000,000.00` |
| `Live` | `Short` | `859.50` | 1,020,000.00 USD | 313.72 USD | 0.00 USD | `+15.39%` | `365,000,000.00` |
| `Live` | `Short` | `864.50` | 1,020,000.00 USD | 6,240.00 USD | 0.00 USD | `+16.06%` | `7,220,000,000.00` |
| `Live` | `Short` | `866.50` | 1,020,000.00 USD | 236.55 USD | 0.00 USD | `+16.33%` | `273,000,000.00` |
| `Live` | `Short` | `868.50` | 1,030,000.00 USD | 1,530.00 USD | 0.00 USD | `+16.59%` | `1,765,000,000.00` |
| `Live` | `Short` | `869.50` | 1,480,000.00 USD | 452,190.00 USD | 0.00 USD | `+16.73%` | `520,062,000,000.00` |
| `Live` | `Short` | `876.50` | 1,480,000.00 USD | 911.56 USD | 0.00 USD | `+17.67%` | `1,040,000,000.00` |
| `Live` | `Short` | `878.50` | 1,490,000.00 USD | 11,910.00 USD | 0.00 USD | `+17.94%` | `13,555,000,000.00` |
| `Live` | `Short` | `879.50` | 1,490,000.00 USD | 4,540.00 USD | 0.00 USD | `+18.07%` | `5,165,000,000.00` |
| `Live` | `Short` | `885.50` | 1,500,000.00 USD | 2,750.00 USD | 0.00 USD | `+18.88%` | `3,111,000,000.00` |
| `Live` | `Short` | `886.50` | 1,500,000.00 USD | 812.92 USD | 0.00 USD | `+19.01%` | `917,000,000.00` |
| `Live` | `Short` | `889.50` | 1,500,000.00 USD | 772.09 USD | 0.00 USD | `+19.41%` | `868,000,000.00` |
| `Live` | `Short` | `892.50` | 1,500,000.00 USD | 3,350.00 USD | 0.00 USD | `+19.82%` | `3,752,000,000.00` |
| `Live` | `Short` | `896.50` | 1,730,000.00 USD | 224,510.00 USD | 0.00 USD | `+20.35%` | `250,426,000,000.00` |
| `Live` | `Short` | `907.50` | 1,730,000.00 USD | 392.04 USD | 0.00 USD | `+21.83%` | `432,000,000.00` |
| `Live` | `Short` | `908.50` | 1,730,000.00 USD | 901.23 USD | 0.00 USD | `+21.96%` | `992,000,000.00` |
| `Live` | `Short` | `910.50` | 1,730,000.00 USD | 922.34 USD | 0.00 USD | `+22.23%` | `1,013,000,000.00` |
| `Live` | `Short` | `911.50` | 1,770,000.00 USD | 39,480.00 USD | 0.00 USD | `+22.37%` | `43,317,000,000.00` |
| `Live` | `Short` | `923.50` | 1,770,000.00 USD | 196.71 USD | 0.00 USD | `+23.98%` | `213,000,000.00` |
| `Live` | `Short` | `925.50` | 1,780,000.00 USD | 9,260.00 USD | 0.00 USD | `+24.25%` | `10,000,000,000.00` |
| `Live` | `Short` | `928.50` | 1,780,000.00 USD | 285.05 USD | 0.00 USD | `+24.65%` | `307,000,000.00` |
| `Live` | `Short` | `930.50` | 1,780,000.00 USD | 3,240.00 USD | 0.00 USD | `+24.92%` | `3,487,000,000.00` |
| `Live` | `Short` | `939.50` | 1,780,000.00 USD | 952.65 USD | 0.00 USD | `+26.13%` | `1,014,000,000.00` |
| `Live` | `Short` | `944.50` | 1,780,000.00 USD | 112.40 USD | 0.00 USD | `+26.80%` | `119,000,000.00` |
| `Live` | `Short` | `945.50` | 1,780,000.00 USD | 110.62 USD | 0.00 USD | `+26.93%` | `117,000,000.00` |
| `Live` | `Short` | `952.50` | 1,780,000.00 USD | 398.14 USD | 0.00 USD | `+27.87%` | `418,000,000.00` |
| `Live` | `Short` | `958.50` | 1,850,000.00 USD | 67,090.00 USD | 0.00 USD | `+28.68%` | `70,000,000,000.00` |
| `Live` | `Short` | `962.50` | 1,850,000.00 USD | 202.12 USD | 0.00 USD | `+29.21%` | `210,000,000.00` |
| `Live` | `Short` | `963.50` | 2,690,000.00 USD | 838,250.00 USD | 0.00 USD | `+29.35%` | `870,000,000,000.00` |
| `Live` | `Short` | `967.50` | 2,690,000.00 USD | 1,940.00 USD | 0.00 USD | `+29.88%` | `2,000,000,000.00` |
| `Live` | `Short` | `970.50` | 2,700,000.00 USD | 5,780.00 USD | 0.00 USD | `+30.29%` | `5,960,000,000.00` |
| `Live` | `Short` | `974.50` | 2,760,000.00 USD | 59,840.00 USD | 0.00 USD | `+30.82%` | `61,406,000,000.00` |
| `Live` | `Short` | `981.50` | 2,770,000.00 USD | 14,480.00 USD | 0.00 USD | `+31.76%` | `14,758,000,000.00` |
| `Live` | `Short` | `983.50` | 2,800,000.00 USD | 27,790.00 USD | 0.00 USD | `+32.03%` | `28,258,000,000.00` |
| `Live` | `Short` | `994.50` | 3,080,000.00 USD | 285,520.00 USD | 0.00 USD | `+33.51%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 3,180,000.00 USD | 99,550.00 USD | 0.00 USD | `+33.64%` | `99,998,000,000.00` |
| `Live` | `Short` | `1005.50` | 3,190,000.00 USD | 1,570.00 USD | 0.00 USD | `+34.99%` | `1,564,000,000.00` |
| `Live` | `Short` | `1007.50` | 3,190,000.00 USD | 174.30 USD | 0.00 USD | `+35.25%` | `173,000,000.00` |
| `Live` | `Short` | `1008.50` | 3,890,000.00 USD | 703,540.00 USD | 0.00 USD | `+35.39%` | `697,611,000,000.00` |
| `Live` | `Short` | `1028.50` | 3,990,000.00 USD | 102,850.00 USD | 0.00 USD | `+38.07%` | `100,000,000,000.00` |
| `Live` | `Short` | `1039.50` | 3,990,000.00 USD | 676.71 USD | 0.00 USD | `+39.55%` | `651,000,000.00` |
| `Live` | `Short` | `1049.50` | 3,990,000.00 USD | 294.91 USD | 0.00 USD | `+40.89%` | `281,000,000.00` |
| `Live` | `Short` | `1050.50` | 3,990,000.00 USD | 500.04 USD | 0.00 USD | `+41.03%` | `476,000,000.00` |
| `Live` | `Short` | `1057.50` | 4,000,000.00 USD | 5,220.00 USD | 0.00 USD | `+41.97%` | `4,936,000,000.00` |
| `Live` | `Short` | `1064.50` | 4,000,000.00 USD | 1,600.00 USD | 0.00 USD | `+42.91%` | `1,500,000,000.00` |
| `Live` | `Short` | `1071.50` | 4,000,000.00 USD | 1,550.00 USD | 0.00 USD | `+43.85%` | `1,446,000,000.00` |
| `Live` | `Short` | `1073.50` | 4,000,000.00 USD | 1,610.00 USD | 0.00 USD | `+44.12%` | `1,500,000,000.00` |
| `Live` | `Short` | `1118.50` | 4,010,000.00 USD | 6,160.00 USD | 0.00 USD | `+50.16%` | `5,508,000,000.00` |
| `Live` | `Short` | `1124.50` | 4,030,000.00 USD | 20,050.00 USD | 0.00 USD | `+50.96%` | `17,826,000,000.00` |
| `Live` | `Short` | `1134.50` | 4,030,000.00 USD | 3,800.00 USD | 0.00 USD | `+52.30%` | `3,350,000,000.00` |
| `Live` | `Short` | `1139.50` | 4,090,000.00 USD | 55,050.00 USD | 0.00 USD | `+52.98%` | `48,311,000,000.00` |
| `Live` | `Short` | `1144.50` | 4,090,000.00 USD | 153.36 USD | 0.00 USD | `+53.65%` | `134,000,000.00` |
| `Live` | `Short` | `1166.50` | 4,100,000.00 USD | 9,150.00 USD | 0.00 USD | `+56.60%` | `7,843,000,000.00` |
| `Live` | `Short` | `1169.50` | 4,100,000.00 USD | 367.22 USD | 0.00 USD | `+57.00%` | `314,000,000.00` |
| `Live` | `Short` | `1173.50` | 4,110,000.00 USD | 14,380.00 USD | 0.00 USD | `+57.54%` | `12,251,000,000.00` |
| `Live` | `Short` | `1183.50` | 4,110,000.00 USD | 158.59 USD | 0.00 USD | `+58.88%` | `134,000,000.00` |
| `Live` | `Short` | `1192.50` | 4,110,000.00 USD | 133.56 USD | 0.00 USD | `+60.09%` | `112,000,000.00` |
| `Live` | `Short` | `1197.50` | 4,110,000.00 USD | 463.43 USD | 0.00 USD | `+60.76%` | `387,000,000.00` |
| `Live` | `Short` | `1207.50` | 4,140,000.00 USD | 30,170.00 USD | 0.00 USD | `+62.10%` | `24,982,000,000.00` |
| `Live` | `Short` | `1208.50` | 4,140,000.00 USD | 385.51 USD | 0.00 USD | `+62.24%` | `319,000,000.00` |
| `Live` | `Short` | `1220.50` | 4,140,000.00 USD | 1,220.00 USD | 0.00 USD | `+63.85%` | `1,000,000,000.00` |
| `Live` | `Short` | `1225.50` | 4,150,000.00 USD | 1,030.00 USD | 0.00 USD | `+64.52%` | `841,000,000.00` |
| `Live` | `Short` | `1244.50` | 4,150,000.00 USD | 8,710.00 USD | 0.00 USD | `+67.07%` | `6,999,000,000.00` |
| `Live` | `Short` | `1252.50` | 4,150,000.00 USD | 100.20 USD | 0.00 USD | `+68.15%` | `80,000,000.00` |
| `Live` | `Short` | `1258.50` | 4,160,000.00 USD | 341.05 USD | 0.00 USD | `+68.95%` | `271,000,000.00` |
| `Live` | `Short` | `1261.50` | 4,160,000.00 USD | 201.84 USD | 0.00 USD | `+69.35%` | `160,000,000.00` |
| `Live` | `Short` | `1264.50` | 4,160,000.00 USD | 206.11 USD | 0.00 USD | `+69.76%` | `163,000,000.00` |
| `Live` | `Short` | `1283.50` | 4,270,000.00 USD | 115,520.00 USD | 0.00 USD | `+72.31%` | `90,000,000,000.00` |
| `Live` | `Short` | `1287.50` | 4,430,000.00 USD | 163,360.00 USD | 0.00 USD | `+72.84%` | `126,881,000,000.00` |
| `Live` | `Short` | `1295.50` | 4,430,000.00 USD | 181.37 USD | 0.00 USD | `+73.92%` | `140,000,000.00` |
| `Live` | `Short` | `1300.50` | 5,210,000.00 USD | 773,450.00 USD | 0.00 USD | `+74.59%` | `594,730,000,000.00` |
| `Live` | `Short` | `1320.50` | 5,220,000.00 USD | 14,140.00 USD | 0.00 USD | `+77.27%` | `10,710,000,000.00` |
| `Live` | `Short` | `1325.50` | 5,240,000.00 USD | 19,880.00 USD | 0.00 USD | `+77.95%` | `15,000,000,000.00` |
| `Live` | `Short` | `1328.50` | 5,240,000.00 USD | 102.29 USD | 0.00 USD | `+78.35%` | `77,000,000.00` |
| `Live` | `Short` | `1331.50` | 5,270,000.00 USD | 23,490.00 USD | 0.00 USD | `+78.75%` | `17,640,000,000.00` |
| `Live` | `Short` | `1375.50` | 5,510,000.00 USD | 247,750.00 USD | 0.00 USD | `+84.66%` | `180,115,000,000.00` |
| `Live` | `Short` | `1387.50` | 5,520,000.00 USD | 5,540.00 USD | 0.00 USD | `+86.27%` | `3,994,000,000.00` |
| `Live` | `Short` | `1399.50` | 5,530,000.00 USD | 10,090.00 USD | 0.00 USD | `+87.88%` | `7,210,000,000.00` |
| `Live` | `Short` | `1402.50` | 5,530,000.00 USD | 178.12 USD | 0.00 USD | `+88.28%` | `127,000,000.00` |
| `Live` | `Short` | `1413.50` | 5,530,000.00 USD | 139.94 USD | 0.00 USD | `+89.76%` | `99,000,000.00` |
| `Live` | `Short` | `1432.50` | 5,530,000.00 USD | 360.99 USD | 0.00 USD | `+92.31%` | `252,000,000.00` |
| `Live` | `Short` | `1444.50` | 6,230,000.00 USD | 697,520.00 USD | 0.00 USD | `+93.92%` | `482,880,000,000.00` |
| `Live` | `Short` | `1460.50` | 6,240,000.00 USD | 8,940.00 USD | 0.00 USD | `+96.07%` | `6,124,000,000.00` |
| `Live` | `Short` | `1470.50` | 6,250,000.00 USD | 14,460.00 USD | 0.00 USD | `+97.41%` | `9,836,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `300.50` | 1,780,000.00 USD | 0.00 USD | 2,400.00 USD | `-59.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 1,780,000.00 USD | 0.00 USD | 333.50 USD | `-55.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `350.50` | 1,780,000.00 USD | 0.00 USD | 127.58 USD | `-52.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 1,780,000.00 USD | 0.00 USD | 5,170.00 USD | `-50.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 1,770,000.00 USD | 0.00 USD | 25,210.00 USD | `-44.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 1,750,000.00 USD | 0.00 USD | 4,550.00 USD | `-44.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 1,740,000.00 USD | 0.00 USD | 698.74 USD | `-38.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 1,740,000.00 USD | 0.00 USD | 3,550.00 USD | `-36.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 1,740,000.00 USD | 0.00 USD | 6,600.00 USD | `-34.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 1,730,000.00 USD | 0.00 USD | 214.78 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 1,730,000.00 USD | 0.00 USD | 168.67 USD | `-32.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 1,730,000.00 USD | 0.00 USD | 47,830.00 USD | `-32.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 1,680,000.00 USD | 0.00 USD | 185.97 USD | `-31.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 1,680,000.00 USD | 0.00 USD | 1,030.00 USD | `-30.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 1,680,000.00 USD | 0.00 USD | 125.51 USD | `-30.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 1,680,000.00 USD | 0.00 USD | 280.49 USD | `-30.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 1,680,000.00 USD | 0.00 USD | 258.14 USD | `-29.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 1,680,000.00 USD | 0.00 USD | 485.16 USD | `-29.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 1,680,000.00 USD | 0.00 USD | 4,650.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 1,670,000.00 USD | 0.00 USD | 1,680.00 USD | `-27.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 1,670,000.00 USD | 0.00 USD | 864.80 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 1,670,000.00 USD | 0.00 USD | 1,190.00 USD | `-25.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 1,670,000.00 USD | 0.00 USD | 1,220.00 USD | `-25.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 1,670,000.00 USD | 0.00 USD | 297.12 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 1,670,000.00 USD | 0.00 USD | 748.48 USD | `-24.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 1,670,000.00 USD | 0.00 USD | 566.50 USD | `-23.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 1,670,000.00 USD | 0.00 USD | 126.55 USD | `-23.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 1,670,000.00 USD | 0.00 USD | 5,680.00 USD | `-23.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 1,660,000.00 USD | 0.00 USD | 4,760.00 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 1,660,000.00 USD | 0.00 USD | 1,700.00 USD | `-23.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 1,660,000.00 USD | 0.00 USD | 291.91 USD | `-23.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 1,660,000.00 USD | 0.00 USD | 469.61 USD | `-22.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 1,660,000.00 USD | 0.00 USD | 289.98 USD | `-22.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 1,650,000.00 USD | 0.00 USD | 285.86 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 1,650,000.00 USD | 0.00 USD | 289.17 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 1,650,000.00 USD | 0.00 USD | 947.96 USD | `-22.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 1,650,000.00 USD | 0.00 USD | 289.59 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 1,650,000.00 USD | 0.00 USD | 287.67 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 1,650,000.00 USD | 0.00 USD | 288.74 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 1,650,000.00 USD | 0.00 USD | 1,090.00 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 1,650,000.00 USD | 0.00 USD | 34,020.00 USD | `-21.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 1,620,000.00 USD | 0.00 USD | 289.05 USD | `-21.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 1,620,000.00 USD | 0.00 USD | 287.78 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,620,000.00 USD | 0.00 USD | 7,990.00 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,610,000.00 USD | 0.00 USD | 540.31 USD | `-20.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 1,610,000.00 USD | 0.00 USD | 282.74 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,610,000.00 USD | 0.00 USD | 170.05 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `594.50` | 1,610,000.00 USD | 0.00 USD | 286.55 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,610,000.00 USD | 0.00 USD | 244.79 USD | `-19.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,610,000.00 USD | 0.00 USD | 3,760.00 USD | `-19.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,600,000.00 USD | 0.00 USD | 2,610.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `606.50` | 1,600,000.00 USD | 0.00 USD | 103.11 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,600,000.00 USD | 0.00 USD | 170.00 USD | `-17.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 1,600,000.00 USD | 0.00 USD | 1,380.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,600,000.00 USD | 0.00 USD | 269.15 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,600,000.00 USD | 0.00 USD | 1,740.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,600,000.00 USD | 0.00 USD | 120.83 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,600,000.00 USD | 0.00 USD | 105.49 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,600,000.00 USD | 0.00 USD | 170.76 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,600,000.00 USD | 0.00 USD | 276.16 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,600,000.00 USD | 0.00 USD | 4,570.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 1,590,000.00 USD | 0.00 USD | 2,550.00 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,590,000.00 USD | 0.00 USD | 560.60 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,590,000.00 USD | 0.00 USD | 154.27 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,590,000.00 USD | 0.00 USD | 971.04 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,590,000.00 USD | 0.00 USD | 1,610.00 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,590,000.00 USD | 0.00 USD | 14,000.00 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,570,000.00 USD | 0.00 USD | 2,090.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,570,000.00 USD | 0.00 USD | 2,020.00 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,570,000.00 USD | 0.00 USD | 308.92 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,570,000.00 USD | 0.00 USD | 129.33 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,570,000.00 USD | 0.00 USD | 110.46 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,570,000.00 USD | 0.00 USD | 17,600.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,550,000.00 USD | 0.00 USD | 198.15 USD | `-11.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,550,000.00 USD | 0.00 USD | 1,780.00 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,550,000.00 USD | 0.00 USD | 4,920.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,540,000.00 USD | 0.00 USD | 707.66 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,540,000.00 USD | 0.00 USD | 3,360.00 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 1,540,000.00 USD | 0.00 USD | 245.46 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 1,540,000.00 USD | 0.00 USD | 2,090.00 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 1,540,000.00 USD | 0.00 USD | 825.59 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 1,540,000.00 USD | 0.00 USD | 1,760.00 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 1,530,000.00 USD | 0.00 USD | 63,000.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 1,470,000.00 USD | 0.00 USD | 3,360.00 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 1,470,000.00 USD | 0.00 USD | 175.31 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 1,470,000.00 USD | 0.00 USD | 2,370.00 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 1,470,000.00 USD | 0.00 USD | 31,240.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,430,000.00 USD | 0.00 USD | 24,240.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 1,410,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 1,410,000.00 USD | 0.00 USD | 7,610.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 1,400,000.00 USD | 0.00 USD | 371.25 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 1,400,000.00 USD | 0.00 USD | 610.01 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 1,400,000.00 USD | 0.00 USD | 2,590.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 1,400,000.00 USD | 0.00 USD | 7,140.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 1,390,000.00 USD | 0.00 USD | 108.57 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 1,390,000.00 USD | 0.00 USD | 2,530.00 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 1,390,000.00 USD | 0.00 USD | 4,560.00 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 1,380,000.00 USD | 0.00 USD | 374.34 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 1,380,000.00 USD | 0.00 USD | 30,340.00 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 1,350,000.00 USD | 0.00 USD | 9,690.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 1,340,000.00 USD | 0.00 USD | 4,340.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 1,340,000.00 USD | 0.00 USD | 5,460.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 1,330,000.00 USD | 0.00 USD | 3,300.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 1,330,000.00 USD | 0.00 USD | 190,140.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,140,000.00 USD | 0.00 USD | 3,900.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 1,140,000.00 USD | 0.00 USD | 1,790.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 1,130,000.00 USD | 0.00 USD | 2,790.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 1,130,000.00 USD | 0.00 USD | 1,070.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 1,130,000.00 USD | 0.00 USD | 2,770.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 1,130,000.00 USD | 0.00 USD | 11,860.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 1,110,000.00 USD | 0.00 USD | 205.88 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 1,110,000.00 USD | 0.00 USD | 1,070.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 1,110,000.00 USD | 0.00 USD | 783.29 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 1,110,000.00 USD | 0.00 USD | 623.82 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 1,110,000.00 USD | 0.00 USD | 402.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 1,110,000.00 USD | 0.00 USD | 2,870.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 1,110,000.00 USD | 0.00 USD | 94,480.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 1,010,000.00 USD | 0.00 USD | 88,360.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 926,190.00 USD | 0.00 USD | 6,050.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 920,130.00 USD | 0.00 USD | 1,470.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `717.50` | 918,660.00 USD | 0.00 USD | 246.82 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `718.50` | 918,420.00 USD | 0.00 USD | 727.84 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `719.50` | 917,690.00 USD | 0.00 USD | 1,270.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `720.50` | 916,420.00 USD | 0.00 USD | 2,710.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `721.50` | 913,710.00 USD | 0.00 USD | 6,780.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `722.50` | 906,920.00 USD | 0.00 USD | 114.16 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `723.50` | 906,810.00 USD | 0.00 USD | 605.57 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `724.50` | 906,200.00 USD | 0.00 USD | 9,620.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.50` | 896,590.00 USD | 0.00 USD | 9,140.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `726.50` | 887,450.00 USD | 0.00 USD | 470.77 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `727.50` | 886,970.00 USD | 0.00 USD | 1,650.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `728.50` | 885,330.00 USD | 0.00 USD | 8,950.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `729.50` | 876,380.00 USD | 0.00 USD | 6,820.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `730.50` | 869,560.00 USD | 0.00 USD | 1,640.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `731.50` | 867,920.00 USD | 0.00 USD | 583,440.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `732.50` | 284,480.00 USD | 0.00 USD | 1,600.00 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `733.50` | 282,880.00 USD | 0.00 USD | 2,100.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `734.50` | 280,780.00 USD | 0.00 USD | 651.50 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `735.50` | 280,130.00 USD | 0.00 USD | 1,820.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `736.50` | 278,310.00 USD | 0.00 USD | 5,760.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `737.50` | 272,550.00 USD | 0.00 USD | 7,300.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `738.50` | 265,250.00 USD | 0.00 USD | 5,860.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `739.50` | 259,390.00 USD | 0.00 USD | 2,460.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `740.50` | 256,930.00 USD | 0.00 USD | 155.50 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `741.50` | 256,780.00 USD | 0.00 USD | 6,570.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `742.50` | 250,200.00 USD | 0.00 USD | 247,900.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `743.50` | 2,300.00 USD | 0.00 USD | 897.40 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `744.50` | 1,400.00 USD | 0.00 USD | 1,400.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,000.00 USD | 1,000.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,290.00 USD | 288.90 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,590.00 USD | 301.24 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 2,310.00 USD | 720.81 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 3,310.00 USD | 999.83 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 4,440.00 USD | 1,130.00 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 5,450.00 USD | 1,010.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 8,180.00 USD | 2,730.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 9,190.00 USD | 1,010.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 9,710.00 USD | 525.13 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 10,690.00 USD | 979.13 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 18,940.00 USD | 8,250.00 USD | 0.00 USD | `+1.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 20,820.00 USD | 1,880.00 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 21,620.00 USD | 799.46 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 21,870.00 USD | 253.67 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 22,040.00 USD | 168.07 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 24,960.00 USD | 2,920.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 27,570.00 USD | 2,610.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 277,240.00 USD | 249,670.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 283,630.00 USD | 6,390.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 362,480.00 USD | 78,840.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 362,810.00 USD | 331.13 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 364,170.00 USD | 1,360.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 365,400.00 USD | 1,230.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 365,900.00 USD | 504.02 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 597,290.00 USD | 231,390.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 598,660.00 USD | 1,370.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 608,330.00 USD | 9,670.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 609,580.00 USD | 1,240.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 619,260.00 USD | 9,680.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 624,880.00 USD | 5,620.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 639,120.00 USD | 14,230.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 643,220.00 USD | 4,100.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 648,690.00 USD | 5,470.00 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 655,110.00 USD | 6,420.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 751,290.00 USD | 96,180.00 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 767,160.00 USD | 15,870.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 770,370.00 USD | 3,200.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 1,180,000.00 USD | 407,870.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 1,180,000.00 USD | 106.69 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 1,180,000.00 USD | 292.21 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 1,180,000.00 USD | 366.51 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 1,180,000.00 USD | 393.75 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 1,180,000.00 USD | 133.26 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 1,180,000.00 USD | 1,150.00 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 1,180,000.00 USD | 704.44 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 1,190,000.00 USD | 4,160.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 1,190,000.00 USD | 1,450.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 1,190,000.00 USD | 3,730.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 1,190,000.00 USD | 3,040.00 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 1,190,000.00 USD | 154.52 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 1,200,000.00 USD | 2,590.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 1,230,000.00 USD | 36,970.00 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 1,230,000.00 USD | 803.50 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 1,230,000.00 USD | 179.63 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 1,240,000.00 USD | 3,860.00 USD | 0.00 USD | `+8.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 1,240,000.00 USD | 3,190.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 1,240,000.00 USD | 868.59 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 1,260,000.00 USD | 15,790.00 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 1,260,000.00 USD | 374.10 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 1,260,000.00 USD | 6,080.00 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 1,260,000.00 USD | 109.82 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 1,270,000.00 USD | 3,210.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 1,270,000.00 USD | 2,610.00 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 1,270,000.00 USD | 162.68 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 1,280,000.00 USD | 7,000.00 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 1,280,000.00 USD | 408.13 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `825.50` | 1,610,000.00 USD | 330,200.00 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 1,610,000.00 USD | 672.77 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 1,610,000.00 USD | 276.38 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 1,620,000.00 USD | 5,780.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 1,620,000.00 USD | 493.32 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 1,620,000.00 USD | 3,270.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 1,620,000.00 USD | 187.15 USD | 0.00 USD | `+12.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 1,620,000.00 USD | 372.24 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 1,620,000.00 USD | 326.62 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 1,620,000.00 USD | 296.34 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 1,620,000.00 USD | 441.26 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 1,620,000.00 USD | 329.87 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 1,620,000.00 USD | 425.97 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 1,630,000.00 USD | 7,860.00 USD | 0.00 USD | `+13.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 1,630,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 1,640,000.00 USD | 11,650.00 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 1,640,000.00 USD | 102.30 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 1,640,000.00 USD | 137.57 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 1,660,000.00 USD | 13,180.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 1,660,000.00 USD | 551.58 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 1,660,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 1,660,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 1,660,000.00 USD | 2,970.00 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 1,660,000.00 USD | 3,460.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 1,670,000.00 USD | 2,610.00 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 1,670,000.00 USD | 228.07 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 1,670,000.00 USD | 1,110.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `874.50` | 1,670,000.00 USD | 582.42 USD | 0.00 USD | `+17.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 1,720,000.00 USD | 54,820.00 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 1,720,000.00 USD | 266.55 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 1,720,000.00 USD | 690.14 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 1,730,000.00 USD | 605.33 USD | 0.00 USD | `+19.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 1,780,000.00 USD | 55,500.00 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 1,790,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 1,790,000.00 USD | 533.99 USD | 0.00 USD | `+23.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 1,790,000.00 USD | 166.43 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 1,790,000.00 USD | 463.01 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 1,790,000.00 USD | 321.50 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `929.50` | 1,810,000.00 USD | 24,800.00 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 1,810,000.00 USD | 552.72 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 1,810,000.00 USD | 196.03 USD | 0.00 USD | `+25.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 1,810,000.00 USD | 287.20 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 1,810,000.00 USD | 782.14 USD | 0.00 USD | `+28.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 1,810,000.00 USD | 498.94 USD | 0.00 USD | `+28.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 1,820,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 1,820,000.00 USD | 293.25 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 1,820,000.00 USD | 1,300.00 USD | 0.00 USD | `+31.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 1,820,000.00 USD | 109.93 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 1,820,000.00 USD | 439.09 USD | 0.00 USD | `+32.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 1,820,000.00 USD | 2,590.00 USD | 0.00 USD | `+32.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 1,820,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 1,830,000.00 USD | 3,990.00 USD | 0.00 USD | `+34.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 1,830,000.00 USD | 938.53 USD | 0.00 USD | `+34.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 1,840,000.00 USD | 12,810.00 USD | 0.00 USD | `+34.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 1,840,000.00 USD | 203.50 USD | 0.00 USD | `+36.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 1,840,000.00 USD | 195.51 USD | 0.00 USD | `+40.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 1,840,000.00 USD | 278.43 USD | 0.00 USD | `+47.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 1,840,000.00 USD | 555.75 USD | 0.00 USD | `+49.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 1,910,000.00 USD | 65,370.00 USD | 0.00 USD | `+61.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 1,910,000.00 USD | 1,250.00 USD | 0.00 USD | `+61.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 1,910,000.00 USD | 235.49 USD | 0.00 USD | `+64.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 1,910,000.00 USD | 3,580.00 USD | 0.00 USD | `+65.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 1,910,000.00 USD | 421.42 USD | 0.00 USD | `+67.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 1,920,000.00 USD | 3,750.00 USD | 0.00 USD | `+71.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 1,920,000.00 USD | 133.64 USD | 0.00 USD | `+74.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 1,920,000.00 USD | 685.36 USD | 0.00 USD | `+74.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 1,940,000.00 USD | 24,400.00 USD | 0.00 USD | `+78.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 1,970,000.00 USD | 33,950.00 USD | 0.00 USD | `+79.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 1,980,000.00 USD | 6,210.00 USD | 0.00 USD | `+82.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 1,980,000.00 USD | 349.06 USD | 0.00 USD | `+83.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 1,980,000.00 USD | 1,060.00 USD | 0.00 USD | `+83.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 2,000,000.00 USD | 19,210.00 USD | 0.00 USD | `+84.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 2,000,000.00 USD | 2,150.00 USD | 0.00 USD | `+88.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `669.20` | 32,670,000.00 USD | 0.00 USD | 32,670,000.00 USD | 64,690.00 USD | 25,520.00 USD | 9,010.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.00` | 32,570,000.00 USD | 0.00 USD | 32,570,000.00 USD | 174,720.00 USD | 2,750.00 USD | 4,170.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `670.80` | 32,390,000.00 USD | 0.00 USD | 32,390,000.00 USD | 19,310.00 USD | 8,380.00 USD | 7,950.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.60` | 32,350,000.00 USD | 0.00 USD | 32,350,000.00 USD | 43,410.00 USD | 9,720.00 USD | 11,320.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.40` | 32,290,000.00 USD | 0.00 USD | 32,290,000.00 USD | 93,500.00 USD | 10,080.00 USD | 33,750.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.20` | 32,150,000.00 USD | 0.00 USD | 32,150,000.00 USD | 328,000.00 USD | 37,780.00 USD | 26,760.00 USD |
| `1D` | `674.00` | 31,760,000.00 USD | 0.00 USD | 31,760,000.00 USD | 153,390.00 USD | 23,000.00 USD | 16,110.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.80` | 31,570,000.00 USD | 0.00 USD | 31,570,000.00 USD | 104,430.00 USD | 28,310.00 USD | 27,680.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.60` | 31,410,000.00 USD | 0.00 USD | 31,410,000.00 USD | 134,840.00 USD | 15,770.00 USD | 20,990.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.40` | 31,240,000.00 USD | 0.00 USD | 31,240,000.00 USD | 78,970.00 USD | 31,240.00 USD | 64,410.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.20` | 31,060,000.00 USD | 0.00 USD | 31,060,000.00 USD | 269,660.00 USD | 21,680.00 USD | 40,550.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.00` | 30,730,000.00 USD | 0.00 USD | 30,730,000.00 USD | 176,540.00 USD | 9,040.00 USD | 26,360.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `678.80` | 30,520,000.00 USD | 0.00 USD | 30,520,000.00 USD | 45,580.00 USD | 9,090.00 USD | 9,940.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.60` | 30,450,000.00 USD | 0.00 USD | 30,450,000.00 USD | 159,490.00 USD | 7,580.00 USD | 6,880.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.40` | 30,280,000.00 USD | 0.00 USD | 30,280,000.00 USD | 20,670.00 USD | 9,240.00 USD | 15,580.00 USD |
| `1D` | `681.20` | 30,230,000.00 USD | 0.00 USD | 30,230,000.00 USD | 89,180.00 USD | 5,770.00 USD | 5,710.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `682.00` | 30,130,000.00 USD | 0.00 USD | 30,130,000.00 USD | 34,070.00 USD | 17,040.00 USD | 28,520.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.80` | 30,050,000.00 USD | 0.00 USD | 30,050,000.00 USD | 127,700.00 USD | 11,650.00 USD | 21,910.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.60` | 29,890,000.00 USD | 0.00 USD | 29,890,000.00 USD | 10,050.00 USD | 11,310.00 USD | 5,590.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.40` | 29,870,000.00 USD | 0.00 USD | 29,870,000.00 USD | 38,150.00 USD | 9,430.00 USD | 3,410.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.20` | 29,810,000.00 USD | 0.00 USD | 29,810,000.00 USD | 30,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.20` | 29,780,000.00 USD | 0.00 USD | 29,780,000.00 USD | 5,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `690.00` | 29,780,000.00 USD | 0.00 USD | 29,780,000.00 USD | 56,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.80` | 29,720,000.00 USD | 0.00 USD | 29,720,000.00 USD | 46,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.60` | 29,670,000.00 USD | 0.00 USD | 29,670,000.00 USD | 54,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `1D` | `692.40` | 29,620,000.00 USD | 0.00 USD | 29,620,000.00 USD | 54,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.20` | 29,570,000.00 USD | 0.00 USD | 29,570,000.00 USD | 48,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.00` | 29,520,000.00 USD | 0.00 USD | 29,520,000.00 USD | 32,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `694.80` | 29,480,000.00 USD | 0.00 USD | 29,480,000.00 USD | 17,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `695.60` | 29,470,000.00 USD | 0.00 USD | 29,470,000.00 USD | 34,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `696.40` | 29,430,000.00 USD | 0.00 USD | 29,430,000.00 USD | 24,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `697.20` | 29,410,000.00 USD | 0.00 USD | 29,410,000.00 USD | 70,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `1D` | `698.00` | 29,340,000.00 USD | 0.00 USD | 29,340,000.00 USD | 50,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `698.80` | 29,290,000.00 USD | 0.00 USD | 29,290,000.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `1D` | `699.60` | 29,270,000.00 USD | 0.00 USD | 29,270,000.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.40` | 29,270,000.00 USD | 0.00 USD | 29,270,000.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.20` | 29,250,000.00 USD | 0.00 USD | 29,250,000.00 USD | 24,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.00` | 29,230,000.00 USD | 0.00 USD | 29,230,000.00 USD | 28,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `702.80` | 29,200,000.00 USD | 0.00 USD | 29,200,000.00 USD | 115,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.60` | 29,080,000.00 USD | 0.00 USD | 29,080,000.00 USD | 57,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `704.40` | 29,020,000.00 USD | 0.00 USD | 29,020,000.00 USD | 97,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `705.20` | 28,930,000.00 USD | 0.00 USD | 28,930,000.00 USD | 73,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `706.00` | 28,850,000.00 USD | 0.00 USD | 28,850,000.00 USD | 73,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `1D` | `706.80` | 28,780,000.00 USD | 0.00 USD | 28,780,000.00 USD | 33,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `707.60` | 28,750,000.00 USD | 0.00 USD | 28,750,000.00 USD | 25,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.40` | 28,720,000.00 USD | 0.00 USD | 28,720,000.00 USD | 53,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `1D` | `709.20` | 28,670,000.00 USD | 0.00 USD | 28,670,000.00 USD | 28,500.00 USD | 13,950.00 USD | 19,740.00 USD |
| `1D` | `710.00` | 28,600,000.00 USD | 0.00 USD | 28,600,000.00 USD | 93,600.00 USD | 18,140.00 USD | 0.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `1D` | `710.80` | 28,490,000.00 USD | 0.00 USD | 28,490,000.00 USD | 134,360.00 USD | 67,330.00 USD | 18,560.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.60` | 28,270,000.00 USD | 0.00 USD | 28,270,000.00 USD | 177,560.00 USD | 34,600.00 USD | 33,110.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `712.40` | 28,030,000.00 USD | 0.00 USD | 28,030,000.00 USD | 58,920.00 USD | 4,240.00 USD | 24,530.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `1D` | `713.20` | 27,940,000.00 USD | 0.00 USD | 27,940,000.00 USD | 147,040.00 USD | 73,320.00 USD | 16,360.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `1D` | `714.00` | 27,700,000.00 USD | 0.00 USD | 27,700,000.00 USD | 216,410.00 USD | 19,280.00 USD | 23,910.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `714.80` | 27,440,000.00 USD | 0.00 USD | 27,440,000.00 USD | 503,730.00 USD | 1,230.00 USD | 4,180.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `715.60` | 26,930,000.00 USD | 0.00 USD | 26,930,000.00 USD | 116,340.00 USD | 27,130.00 USD | 26,690.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `716.40` | 26,760,000.00 USD | 0.00 USD | 26,760,000.00 USD | 76,880.00 USD | 35,530.00 USD | 42,570.00 USD |
| `1D` | `717.20` | 26,610,000.00 USD | 0.00 USD | 26,610,000.00 USD | 189,860.00 USD | 30,000.00 USD | 110,390.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `1D` | `718.00` | 26,280,000.00 USD | 0.00 USD | 26,280,000.00 USD | 1,040,000.00 USD | 111,290.00 USD | 101,600.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.80` | 25,030,000.00 USD | 0.00 USD | 25,030,000.00 USD | 489,520.00 USD | 80,390.00 USD | 100,580.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.60` | 24,360,000.00 USD | 0.00 USD | 24,360,000.00 USD | 575,720.00 USD | 77,740.00 USD | 116,880.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.40` | 23,590,000.00 USD | 0.00 USD | 23,590,000.00 USD | 348,960.00 USD | 51,300.00 USD | 55,360.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.20` | 23,130,000.00 USD | 0.00 USD | 23,130,000.00 USD | 311,810.00 USD | 124,610.00 USD | 178,970.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.00` | 22,510,000.00 USD | 0.00 USD | 22,510,000.00 USD | 1,020,000.00 USD | 37,060.00 USD | 88,730.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `722.80` | 21,370,000.00 USD | 0.00 USD | 21,370,000.00 USD | 629,270.00 USD | 63,740.00 USD | 169,860.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `723.60` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 416,950.00 USD | 14,770.00 USD | 42,350.00 USD |
| `1D` | `724.40` | 20,040,000.00 USD | 0.00 USD | 20,040,000.00 USD | 259,230.00 USD | 83,130.00 USD | 51,560.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `725.20` | 19,640,000.00 USD | 0.00 USD | 19,640,000.00 USD | 173,930.00 USD | 109,030.00 USD | 53,970.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `726.00` | 19,310,000.00 USD | 0.00 USD | 19,310,000.00 USD | 358,990.00 USD | 166,310.00 USD | 59,520.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.80` | 18,720,000.00 USD | 0.00 USD | 18,720,000.00 USD | 535,650.00 USD | 46,390.00 USD | 70,820.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.60` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 277,460.00 USD | 136,050.00 USD | 192,880.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.40` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 902,960.00 USD | 117,420.00 USD | 33,280.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.20` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 939,580.00 USD | 51,810.00 USD | 70,300.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.00` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 306,910.00 USD | 51,570.00 USD | 31,370.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `730.80` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 380,880.00 USD | 65,180.00 USD | 79,940.00 USD |
| `1D` | `731.60` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 157,660.00 USD | 62,000.00 USD | 59,080.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `732.40` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 235,470.00 USD | 147,360.00 USD | 205,810.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `733.20` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 2,140,000.00 USD | 210,290.00 USD | 256,160.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `734.00` | 10,960,000.00 USD | 0.00 USD | 10,960,000.00 USD | 1,190,000.00 USD | 152,200.00 USD | 203,940.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `734.80` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 863,310.00 USD | 126,110.00 USD | 189,680.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.60` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 848,110.00 USD | 81,400.00 USD | 169,050.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.40` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 404,280.00 USD | 234,770.00 USD | 394,650.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.20` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 2,200,000.00 USD | 110,380.00 USD | 174,900.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.00` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 1,220,000.00 USD | 94,940.00 USD | 235,590.00 USD |
| `1D` | `738.80` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 680,980.00 USD | 18,090.00 USD | 36,560.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.60` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 518,470.00 USD | 0.00 USD | 48,980.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `740.40` | 765,920.00 USD | 0.00 USD | 765,920.00 USD | 347,860.00 USD | 0.00 USD | 33,700.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.20` | 384,360.00 USD | 0.00 USD | 384,360.00 USD | 230,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `742.80` | 154,230.00 USD | 0.00 USD | 154,230.00 USD | 0.00 USD | 0.00 USD | 64,610.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.60` | 89,620.00 USD | 0.00 USD | 89,620.00 USD | 0.00 USD | 0.00 USD | 48,510.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.40` | 41,100.00 USD | 0.00 USD | 41,100.00 USD | 0.00 USD | 29,640.00 USD | 11,470.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.00` | 38,640.00 USD | 38,640.00 USD | 0.00 USD | 38,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `753.20` | 51,040.00 USD | 51,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,400.00 USD |
| `1D` | `754.00` | 128,730.00 USD | 128,730.00 USD | 0.00 USD | 0.00 USD | 50,610.00 USD | 27,080.00 USD |
| `1D` | `754.80` | 234,590.00 USD | 234,590.00 USD | 0.00 USD | 0.00 USD | 68,750.00 USD | 37,120.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.60` | 530,160.00 USD | 530,160.00 USD | 0.00 USD | 143,570.00 USD | 132,220.00 USD | 19,780.00 USD |
| `1D` | `756.40` | 991,960.00 USD | 991,960.00 USD | 0.00 USD | 390,390.00 USD | 24,970.00 USD | 46,440.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.20` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 145,940.00 USD | 88,970.00 USD | 81,770.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.00` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 136,350.00 USD | 67,700.00 USD | 0.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `758.80` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 367,110.00 USD | 28,530.00 USD | 47,820.00 USD |
| `1D` | `759.60` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 971,100.00 USD | 2,460.00 USD | 8,370.00 USD |
| `1D` | `760.40` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 245,610.00 USD | 54,260.00 USD | 72,300.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `761.20` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 102,000.00 USD | 71,050.00 USD | 66,230.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `762.00` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 349,140.00 USD | 60,010.00 USD | 220,780.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.80` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 1,580,000.00 USD | 168,030.00 USD | 191,950.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.60` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 1,010,000.00 USD | 150,840.00 USD | 111,740.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.40` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 1,330,000.00 USD | 177,890.00 USD | 290,510.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.20` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 492,320.00 USD | 144,680.00 USD | 86,360.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.00` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 705,930.00 USD | 113,780.00 USD | 276,020.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `766.80` | 13,110,000.00 USD | 13,110,000.00 USD | 0.00 USD | 1,690,000.00 USD | 156,820.00 USD | 256,900.00 USD |
| `1D` | `767.60` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 1,280,000.00 USD | 136,380.00 USD | 258,960.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `768.40` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 1,120,000.00 USD | 69,260.00 USD | 194,600.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `769.20` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 346,750.00 USD | 64,540.00 USD | 36,560.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `770.00` | 17,430,000.00 USD | 17,430,000.00 USD | 0.00 USD | 590,250.00 USD | 149,540.00 USD | 82,560.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `770.80` | 18,210,000.00 USD | 18,210,000.00 USD | 0.00 USD | 560,270.00 USD | 88,510.00 USD | 131,270.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `771.60` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 413,630.00 USD | 63,410.00 USD | 53,060.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.40` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 552,350.00 USD | 156,720.00 USD | 36,590.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.20` | 20,270,000.00 USD | 20,270,000.00 USD | 0.00 USD | 462,000.00 USD | 89,950.00 USD | 229,540.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.00` | 21,540,000.00 USD | 21,540,000.00 USD | 0.00 USD | 1,130,000.00 USD | 62,620.00 USD | 83,150.00 USD |
| `1D` | `774.80` | 22,000,000.00 USD | 22,000,000.00 USD | 0.00 USD | 340,920.00 USD | 63,940.00 USD | 56,380.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.60` | 22,570,000.00 USD | 22,570,000.00 USD | 0.00 USD | 388,710.00 USD | 102,110.00 USD | 73,830.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `776.40` | 22,910,000.00 USD | 22,910,000.00 USD | 0.00 USD | 282,120.00 USD | 46,920.00 USD | 12,730.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `777.20` | 23,280,000.00 USD | 23,280,000.00 USD | 0.00 USD | 199,140.00 USD | 73,680.00 USD | 102,900.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.00` | 24,570,000.00 USD | 24,570,000.00 USD | 0.00 USD | 1,080,000.00 USD | 98,430.00 USD | 106,050.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `778.80` | 25,270,000.00 USD | 25,270,000.00 USD | 0.00 USD | 559,680.00 USD | 46,430.00 USD | 96,130.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.60` | 26,090,000.00 USD | 26,090,000.00 USD | 0.00 USD | 624,940.00 USD | 77,740.00 USD | 116,880.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.40` | 26,580,000.00 USD | 26,580,000.00 USD | 0.00 USD | 388,410.00 USD | 51,300.00 USD | 55,360.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.20` | 27,060,000.00 USD | 27,060,000.00 USD | 0.00 USD | 219,490.00 USD | 112,470.00 USD | 140,920.00 USD |
| `1D` | `782.00` | 27,990,000.00 USD | 27,990,000.00 USD | 0.00 USD | 819,350.00 USD | 22,830.00 USD | 91,390.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.80` | 29,090,000.00 USD | 29,090,000.00 USD | 0.00 USD | 841,750.00 USD | 90,120.00 USD | 166,560.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.60` | 29,700,000.00 USD | 29,700,000.00 USD | 0.00 USD | 538,790.00 USD | 14,770.00 USD | 53,720.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.40` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 113,020.00 USD | 32,520.00 USD | 29,730.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.20` | 30,260,000.00 USD | 30,260,000.00 USD | 0.00 USD | 340,190.00 USD | 22,730.00 USD | 23,020.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.00` | 30,560,000.00 USD | 30,560,000.00 USD | 0.00 USD | 232,430.00 USD | 26,950.00 USD | 43,250.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `786.80` | 30,820,000.00 USD | 30,820,000.00 USD | 0.00 USD | 212,420.00 USD | 29,580.00 USD | 14,270.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.60` | 31,100,000.00 USD | 31,100,000.00 USD | 0.00 USD | 235,710.00 USD | 41,700.00 USD | 10,110.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.40` | 31,410,000.00 USD | 31,410,000.00 USD | 0.00 USD | 147,170.00 USD | 42,560.00 USD | 118,250.00 USD |
| `1D` | `789.20` | 31,890,000.00 USD | 31,890,000.00 USD | 0.00 USD | 431,710.00 USD | 24,090.00 USD | 26,140.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `790.00` | 32,140,000.00 USD | 32,140,000.00 USD | 0.00 USD | 200,110.00 USD | 28,260.00 USD | 22,480.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.80` | 32,360,000.00 USD | 32,360,000.00 USD | 0.00 USD | 166,790.00 USD | 36,750.00 USD | 8,530.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.60` | 32,510,000.00 USD | 32,510,000.00 USD | 0.00 USD | 146,160.00 USD | 7,960.00 USD | 0.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.40` | 32,570,000.00 USD | 32,570,000.00 USD | 0.00 USD | 57,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.20` | 32,620,000.00 USD | 32,620,000.00 USD | 0.00 USD | 46,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.00` | 32,640,000.00 USD | 32,640,000.00 USD | 0.00 USD | 26,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `794.80` | 32,680,000.00 USD | 32,680,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `795.60` | 32,720,000.00 USD | 32,720,000.00 USD | 0.00 USD | 38,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `796.40` | 32,750,000.00 USD | 32,750,000.00 USD | 0.00 USD | 30,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.20` | 32,820,000.00 USD | 32,820,000.00 USD | 0.00 USD | 71,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.00` | 32,850,000.00 USD | 32,850,000.00 USD | 0.00 USD | 30,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.80` | 32,870,000.00 USD | 32,870,000.00 USD | 0.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.60` | 32,890,000.00 USD | 32,890,000.00 USD | 0.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.40` | 32,900,000.00 USD | 32,900,000.00 USD | 0.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.20` | 32,910,000.00 USD | 32,910,000.00 USD | 0.00 USD | 16,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.00` | 32,930,000.00 USD | 32,930,000.00 USD | 0.00 USD | 21,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `802.80` | 32,950,000.00 USD | 32,950,000.00 USD | 0.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.60` | 32,960,000.00 USD | 32,960,000.00 USD | 0.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `804.40` | 32,960,000.00 USD | 32,960,000.00 USD | 0.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 0.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD |
| `1D` | `805.20` | 32,970,000.00 USD | 32,970,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 0.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD |
| `1D` | `806.00` | 32,970,000.00 USD | 32,970,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `806.80` | 32,980,000.00 USD | 32,980,000.00 USD | 0.00 USD | 4,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `1D` | `807.60` | 33,000,000.00 USD | 33,000,000.00 USD | 0.00 USD | 16,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 0.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD |
| `1D` | `808.40` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 10,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `1D` | `809.20` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `1D` | `810.00` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `810.80` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 859.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `1D` | `812.40` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `1D` | `813.20` | 33,040,000.00 USD | 33,040,000.00 USD | 0.00 USD | 15,920.00 USD | 4,540.00 USD | 5,420.00 USD |
| `7D` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `1D` | `814.00` | 33,080,000.00 USD | 33,080,000.00 USD | 0.00 USD | 18,950.00 USD | 8,810.00 USD | 7,420.00 USD |
| `7D` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `1D` | `814.80` | 33,120,000.00 USD | 33,120,000.00 USD | 0.00 USD | 27,210.00 USD | 13,270.00 USD | 3,960.00 USD |
| `7D` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `1D` | `815.60` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 11,690.00 USD | 3,300.00 USD | 9,290.00 USD |
| `7D` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `1D` | `816.40` | 33,200,000.00 USD | 33,200,000.00 USD | 0.00 USD | 45,010.00 USD | 8,330.00 USD | 0.00 USD |
| `7D` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `1D` | `817.20` | 33,250,000.00 USD | 33,250,000.00 USD | 0.00 USD | 32,410.00 USD | 17,190.00 USD | 3,620.00 USD |
| `1D` | `818.00` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 19,050.00 USD | 0.00 USD | 5,390.00 USD |
| `7D` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `1D` | `818.80` | 33,460,000.00 USD | 33,460,000.00 USD | 0.00 USD | 174,720.00 USD | 2,750.00 USD | 4,170.00 USD |
| `7D` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `1D` | `819.60` | 33,490,000.00 USD | 33,490,000.00 USD | 0.00 USD | 16,520.00 USD | 4,460.00 USD | 5,270.00 USD |
| `7D` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `1D` | `820.40` | 33,550,000.00 USD | 33,550,000.00 USD | 0.00 USD | 38,810.00 USD | 6,990.00 USD | 14,000.00 USD |
| `7D` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `1D` | `821.20` | 33,580,000.00 USD | 33,580,000.00 USD | 0.00 USD | 27,220.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
| `1D` | `821.90` | 33,630,000.00 USD | 33,630,000.00 USD | 0.00 USD | 47,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 0.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `7D` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 0.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD |
| `7D` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 0.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD |
| `7D` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 0.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD |
| `7D` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 0.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD |
| `7D` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 0.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD |
| `7D` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 0.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD |
| `7D` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 0.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD |
| `7D` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 0.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD |
| `7D` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 0.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD |
| `7D` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 0.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.23B` | Total OI Tokens: `1,646,672.7 BNB`
  * 1h OI Change: `+0.04%` | 4h OI Change: `-0.71%` | 24h OI Change: `-3.18%`
  * Exchange Breakdown: Binance=`579.79M` | Bybit=`105.72M` | OKX=`53.70M` | Hyperliquid=`46.19M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `65.00K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0103%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0103%` | **USDT BingX** | `0.0108%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0000%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `62.62%` | `37.38%` | `1.68` | 61,500,000.00 USD |
| `15M` | `Binance` | `65.17%` | `34.83%` | `1.87` | 22,850,000.00 USD |
| `15M` | `OKX` | `53.11%` | `46.89%` | `1.13` | 6,550,000.00 USD |
| `15M` | `Bybit` | `61.61%` | `38.39%` | `1.60` | 5,430,000.00 USD |
| `15M` | `KuCoin` | `45.82%` | `54.18%` | `0.85` | 179,490.00 USD |
| `15M` | `Gate` | `58.68%` | `41.32%` | `1.42` | 7,120,000.00 USD |
| `15M` | `Bitget` | `46.15%` | `53.85%` | `0.86` | 1,590,000.00 USD |
| `15M` | `BingX` | `51.69%` | `48.31%` | `1.07` | 2,770,000.00 USD |
| `15M` | `MEXC` | `93.92%` | `6.08%` | `15.45` | 5,640,000.00 USD |
| `15M` | `Bitunix` | `61.81%` | `38.19%` | `1.62` | 2,920,000.00 USD |
| `15M` | `Hyperliquid` | `15.53%` | `84.47%` | `0.18` | 1,220,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.48%` | `43.52%` | `1.30` | 1,170,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 139,920.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 1,340,000.00 USD |
| `15M` | `HTX` | `73.87%` | `26.13%` | `2.83` | 44,460.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `83.33%` | `16.67%` | `5.00` | 310,110.00 USD |
| `15M` | `Aster` | `49.11%` | `50.89%` | `0.97` | 314,950.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.77%` | `47.23%` | `1.12` | 1,900,000.00 USD |
| `15M` | `Whale Positions` | `65.17%` | `34.83%` | `1.87` | 22,850,000.00 USD |
| `15M` | `Global Accounts` | `62.62%` | `37.38%` | `1.68` | 61,500,000.00 USD |
| `1H` | `BNB` | `57.12%` | `42.88%` | `1.33` | 191,550,000.00 USD |
| `1H` | `Binance` | `58.62%` | `41.38%` | `1.42` | 58,740,000.00 USD |
| `1H` | `OKX` | `62.71%` | `37.29%` | `1.68` | 22,540,000.00 USD |
| `1H` | `Bybit` | `68.17%` | `31.83%` | `2.14` | 16,440,000.00 USD |
| `1H` | `KuCoin` | `45.9%` | `54.1%` | `0.85` | 194,970.00 USD |
| `1H` | `Gate` | `57.77%` | `42.23%` | `1.37` | 18,690,000.00 USD |
| `1H` | `Bitget` | `49.76%` | `50.24%` | `0.99` | 7,380,000.00 USD |
| `1H` | `BingX` | `39.28%` | `60.72%` | `0.65` | 16,960,000.00 USD |
| `1H` | `MEXC` | `68.38%` | `31.62%` | `2.16` | 17,730,000.00 USD |
| `1H` | `Bitunix` | `55.36%` | `44.64%` | `1.24` | 9,130,000.00 USD |
| `1H` | `Hyperliquid` | `56.29%` | `43.71%` | `1.29` | 3,420,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.85%` | `48.15%` | `1.08` | 3,930,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 372,840.00 USD |
| `1H` | `WhiteBIT` | `98.15%` | `1.85%` | `53.05` | 5,540,000.00 USD |
| `1H` | `HTX` | `79.28%` | `20.72%` | `3.83` | 149,710.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.98%` | `32.02%` | `2.12` | 1,610,000.00 USD |
| `1H` | `Aster` | `73.66%` | `26.34%` | `2.80` | 1,720,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.09%` | `39.91%` | `1.51` | 6,990,000.00 USD |
| `1H` | `Whale Positions` | `58.62%` | `41.38%` | `1.42` | 58,740,000.00 USD |
| `1H` | `Global Accounts` | `57.12%` | `42.88%` | `1.33` | 191,550,000.00 USD |
| `4H` | `BNB` | `46.22%` | `53.78%` | `0.86` | 1,100,000,000.00 USD |
| `4H` | `Binance` | `46.1%` | `53.9%` | `0.86` | 362,800,000.00 USD |
| `4H` | `OKX` | `45.49%` | `54.51%` | `0.83` | 156,430,000.00 USD |
| `4H` | `Bybit` | `43.56%` | `56.44%` | `0.77` | 98,650,000.00 USD |
| `4H` | `KuCoin` | `44.9%` | `55.1%` | `0.81` | 4,560,000.00 USD |
| `4H` | `Gate` | `49.39%` | `50.61%` | `0.98` | 96,360,000.00 USD |
| `4H` | `Bitget` | `46.17%` | `53.83%` | `0.86` | 35,890,000.00 USD |
| `4H` | `BingX` | `51.72%` | `48.28%` | `1.07` | 61,290,000.00 USD |
| `4H` | `MEXC` | `51.78%` | `48.22%` | `1.07` | 109,180,000.00 USD |
| `4H` | `Bitunix` | `49.65%` | `50.35%` | `0.99` | 64,570,000.00 USD |
| `4H` | `Hyperliquid` | `42.55%` | `57.45%` | `0.74` | 23,590,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.71%` | `47.29%` | `1.11` | 15,650,000.00 USD |
| `4H` | `Crypto.com` | `50.38%` | `49.62%` | `1.02` | 1,760,000.00 USD |
| `4H` | `WhiteBIT` | `13.85%` | `86.15%` | `0.16` | 23,670,000.00 USD |
| `4H` | `HTX` | `40.97%` | `59.03%` | `0.69` | 1,860,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.92%` | `64.08%` | `0.56` | 18,140,000.00 USD |
| `4H` | `Aster` | `43.7%` | `56.3%` | `0.78` | 9,640,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.2%` | `58.8%` | `0.70` | 15,750,000.00 USD |
| `4H` | `Whale Positions` | `46.1%` | `53.9%` | `0.86` | 362,800,000.00 USD |
| `4H` | `Global Accounts` | `46.22%` | `53.78%` | `0.86` | 1,100,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `746.85` | `747.37` | `746.85` | `748.95` | `745.95` | 4,608,707.67 USD | 1,960,110.54 USD | 2,648,597.13 USD | -688,486.59 USD | `-14.94%` | `0B / 2S` |
| `5:00 UTC` | `745.95` | `745.96` | `745.95` | `746.85` | `745.05` | 3,520,898.41 USD | 1,701,969.64 USD | 1,818,928.78 USD | -116,959.14 USD | `-3.32%` | `0B / 0S` |
| `0:00 UTC` | `746.25` | `745.96` | `746.25` | `746.85` | `745.05` | 2,334,703.88 USD | 1,240,058.73 USD | 1,094,645.16 USD | 145,413.57 USD | `+6.23%` | `1B / 0S` |
| `5:00 UTC` | `745.35` | `745.34` | `745.35` | `745.95` | `744.45` | 2,053,811.83 USD | 1,008,932.17 USD | 1,044,879.66 USD | -35,947.48 USD | `-1.75%` | `0B / 0S` |
| `0:00 UTC` | `743.55` | `743.83` | `743.55` | `745.05` | `742.95` | 4,178,944.72 USD | 2,213,489.92 USD | 1,965,454.80 USD | 248,035.12 USD | `+5.94%` | `0B / 1S` |
| `5:00 UTC` | `745.05` | `744.69` | `745.05` | `745.65` | `743.85` | 1,732,972.70 USD | 1,039,625.11 USD | 693,347.59 USD | 346,277.52 USD | `+19.98%` | `0B / 0S` |
| `0:00 UTC` | `744.15` | `744.46` | `744.15` | `745.35` | `743.85` | 2,147,535.09 USD | 1,307,335.66 USD | 840,199.43 USD | 467,136.24 USD | `+21.75%` | `0B / 0S` |
| `5:00 UTC` | `744.45` | `744.43` | `744.45` | `745.05` | `743.85` | 1,240,697.54 USD | 644,810.68 USD | 595,886.86 USD | 48,923.82 USD | `+3.94%` | `0B / 0S` |
| `0:00 UTC` | `745.35` | `745.38` | `745.35` | `746.25` | `744.45` | 2,107,319.68 USD | 1,122,788.81 USD | 984,530.87 USD | 138,257.94 USD | `+6.56%` | `1B / 1S` |
| `5:00 UTC` | `745.35` | `745.56` | `745.35` | `746.25` | `745.05` | 1,685,703.24 USD | 985,117.02 USD | 700,586.22 USD | 284,530.80 USD | `+16.88%` | `2B / 0S` |

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
| `5m` | -1,850,000.00 USD | -7,200,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,890,000.00 USD | -6,900,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,860,000.00 USD | -6,810,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,650,000.00 USD | -5,600,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,960,000.00 USD | -4,040,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,980,000.00 USD | -7,790,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,340,000.00 USD | -11,270,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,770,000.00 USD | 3,140,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -9,730,000.00 USD | -16,370,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 2,950,000.00 USD | -34,110,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -29,470,000.00 USD | -50,250,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -127,870,000.00 USD | -376,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.85M` | 15m=`-1.89M` | 1h=`-1.65M` | 24h=`+2.95M`
* Futures Capital Netflows: 5m=`-7.20M` | 15m=`-6.90M` | 1h=`-5.60M` | 24h=`-34.11M`
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
  * Execution Entry: `740.57` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `737.24` (Risk Distance: `3.33` pts)
  * +2.5R Take Profit: `748.88`
  * Mathematical Lot Sizing: **`3.00 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `752.43` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `755.76` (Risk Distance: `3.33` pts)
  * +2.5R Take Profit: `744.12`
  * Mathematical Lot Sizing: **`3.00 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`746.78`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
