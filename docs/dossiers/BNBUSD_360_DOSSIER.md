# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:51:14 IST` (`2026-10-29 20:21:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `738.20` | **Live Ask Quote**: `738.80` | **Mid Price**: `738.50`
- **Spread Points**: `60.00` | **Spread BPS**: `8.12 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `752.01` (Distance: `-1.80%`)
  * Point of Control (POC) = `750.75` (Distance: `-1.64%`)
  * Value Area Low (VAL) = `740.37` (Distance: `-0.26%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`752.98` | POC=`743.64` | VAL=`742.97`
  * Prior Day Extremes: PDH=`760.90` | PDL=`740.60` | PDC=`754.40`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`748.80` | Weekly POC=`741.00` | Weekly VAL=`734.80`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`759.80` | Low=`743.20`
  * London Session (08:00-16:00 UTC): High=`758.10` | Low=`737.00`
  * New York Session (13:00-21:00 UTC): High=`753.20` | Low=`737.00`
  * Initial Balance (First Hour): IB High=`758.10` | IB Low=`753.70`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `735.55` - `741.45`
  * Optimal Trade Entry (OTE 0.705): `739.98`
  * Structural Invalidation Anchor (0.786): `744.41`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `745.34` | `745.53` | `739.80` | `740.11` | `16,173` | 12,009,773.43 USD | -7,356,148.06 USD | `-61.25%` | -26,831,853.64 USD | `-4.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `740.11` | `740.35` | `737.67` | `739.39` | `9,925` | 7,335,204.13 USD | -2,135,348.30 USD | `-29.11%` | -28,967,201.94 USD | `-1.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `739.39` | `740.44` | `738.26` | `739.95` | `2,562` | 1,894,649.89 USD | 797,097.09 USD | `+42.07%` | -28,170,104.85 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `744.36` | `746.13` | `744.36` | `745.35` | `2,827` | 2,107,319.68 USD | 138,257.94 USD | `+6.56%` | -19,773,345.59 USD | `+0.22` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `745.35` | `746.16` | `745.15` | `745.33` | `2,299` | 1,714,180.55 USD | 297,640.01 USD | `+17.36%` | -19,475,705.58 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `745.34` | `745.53` | `737.67` | `739.84` | `28,649` | 21,231,148.03 USD | -8,701,842.89 USD | `-40.99%` | -28,177,548.47 USD | `-3.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `746.40` | `746.83` | `743.07` | `744.90` | `13,831` | 10,300,433.14 USD | 703,778.72 USD | `+6.83%` | -21,836,543.73 USD | `+0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `744.90` | `746.16` | `743.85` | `745.33` | `9,678` | 7,209,732.85 USD | 951,958.00 USD | `+13.20%` | -20,884,585.73 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `745.34` | `745.53` | `737.67` | `739.84` | `28,649` | 21,231,148.03 USD | -8,701,842.89 USD | `-40.99%` | -29,586,428.62 USD | `-1.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `737.67` | `739.86` | `28,649` | 21,231,495.76 USD | -8,701,495.16 USD | `-40.98%` | -25,479,903.87 USD | `-0.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `747.26` | `759.90` | `745.75` | `748.51` | `156,800` | 118,182,602.62 USD | -8,240,157.99 USD | `-6.97%` | -14,715,810.54 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `748.51` | `753.57` | `738.70` | `740.45` | `333,019` | 248,636,999.78 USD | -10,340,292.49 USD | `-4.16%` | -25,056,103.04 USD | `-1.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -17,010,604.60 USD | `+1.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -16,778,408.72 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `737.67` | `739.86` | `28,649` | 21,231,495.76 USD | -8,701,495.16 USD | `-40.98%` | -25,479,903.87 USD | `-0.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`738.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `738.92` | `1626000000.0000` | 1,201.48 USD | 105,546.69 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `738.94` | `7192000000.0000` | 5,314.46 USD | 104,345.21 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `738.95` | `12029000000.0000` | 8,888.83 USD | 99,030.75 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `738.96` | `1117000000.0000` | 825.42 USD | 90,141.92 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `739.01` | `10277000000.0000` | 7,594.81 USD | 89,316.50 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `739.03` | `48023000000.0000` | 35,490.44 USD | 81,721.70 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `739.04` | `837000000.0000` | 618.58 USD | 46,231.26 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `739.07` | `205000000.0000` | 151.51 USD | 45,612.68 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `739.08` | `241000000.0000` | 178.12 USD | 45,461.17 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `739.09` | `7191000000.0000` | 5,314.80 USD | 45,283.06 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `739.10` | `7709000000.0000` | 5,697.72 USD | 39,968.26 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `739.11` | `13484000000.0000` | 9,966.16 USD | 34,270.54 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `739.12` | `13306000000.0000` | 9,834.73 USD | 24,304.38 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `739.13` | `2910000000.0000` | 2,150.87 USD | 14,469.65 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `739.19` | `837000000.0000` | 618.70 USD | 12,318.78 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `739.22` | `631000000.0000` | 466.45 USD | 11,700.08 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `739.23` | `1077000000.0000` | 796.15 USD | 11,233.63 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `739.25` | `1117000000.0000` | 825.74 USD | 10,437.48 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `739.26` | `659000000.0000` | 487.17 USD | 9,611.74 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `739.31` | `12342000000.0000` | 9,124.56 USD | 9,124.56 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `739.34` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 739.34` | `0.00%` | `-` |
| `ASK` | `739.37` | `1000000000.0000` | 739.37 USD | 739.37 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `739.41` | `1044000000.0000` | 771.94 USD | 1,511.31 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `739.48` | `1117000000.0000` | 826.00 USD | 2,337.31 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `739.50` | `295000000.0000` | 218.15 USD | 2,555.47 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `739.51` | `10704000000.0000` | 7,915.72 USD | 10,471.18 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `739.52` | `140000000.0000` | 103.53 USD | 10,574.71 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `739.53` | `12301000000.0000` | 9,096.96 USD | 19,671.67 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `739.55` | `3617000000.0000` | 2,674.95 USD | 22,346.62 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `739.57` | `1117000000.0000` | 826.10 USD | 23,172.72 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `739.59` | `6851000000.0000` | 5,066.93 USD | 28,239.66 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `739.60` | `544000000.0000` | 402.34 USD | 28,642.00 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `739.61` | `1793000000.0000` | 1,326.12 USD | 29,968.12 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `739.63` | `1273000000.0000` | 941.55 USD | 30,909.67 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `739.64` | `37460000000.0000` | 27,706.91 USD | 58,616.58 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `739.66` | `2653000000.0000` | 1,962.32 USD | 60,578.90 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `739.68` | `140000000.0000` | 103.56 USD | 60,682.45 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `739.70` | `140000000.0000` | 103.56 USD | 60,786.01 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `739.72` | `1397000000.0000` | 1,033.39 USD | 61,819.40 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `739.73` | `6989000000.0000` | 5,169.97 USD | 66,989.37 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `739.74` | `420000000.0000` | 310.69 USD | 67,300.07 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `768` | `0xea00...a918` | `LONG` | 3,030,009.54 USD | `4,098,429,000,000.00` | `787.24` | `740.12` | `0.000000` | -196,417.24 USD | `-6.48%` | `5X Cross` |
| `1068` | `0xb69e...033a` | `LONG` | 2,084,000.02 USD | `2,805,710,000,000.00` | `772.94` | `740.12` | `575.01` | -84,642.56 USD | `-4.06%` | `10X Cross` |
| `1081` | `0xcac1...26b3` | `LONG` | 2,062,357.85 USD | `2,789,043,000,000.00` | `679.91` | `740.12` | `0.000000` | 166,046.68 USD | `+8.05%` | `10X Cross` |
| `1160` | `0x7737...bf66` | `SHORT` | 1,956,002.59 USD | `2,646,179,000,000.00` | `752.73` | `740.12` | `7004.01` | 35,867.99 USD | `+1.83%` | `10X Cross` |
| `1605` | `0xecb6...2b00` | `SHORT` | 1,381,983.30 USD | `1,867,545,000,000.00` | `738.35` | `740.12` | `14841.02` | -3,076.33 USD | `-0.22%` | `5X Cross` |
| `1644` | `0x27c9...d65d` | `SHORT` | 1,320,528.17 USD | `1,786,163,000,000.00` | `762.40` | `740.12` | `1622.38` | 41,239.18 USD | `+3.12%` | `10X Cross` |
| `1738` | `0x07fd...689d` | `LONG` | 1,231,465.12 USD | `1,664,862,000,000.00` | `716.02` | `740.12` | `0.000000` | 39,388.78 USD | `+3.20%` | `10X Cross` |
| `1755` | `0x645b...87b8` | `LONG` | 1,206,687.27 USD | `1,632,357,000,000.00` | `750.75` | `740.12` | `0.000000` | -18,798.90 USD | `-1.56%` | `10X Cross` |
| `2018` | `0xbcd4...0dd2` | `LONG` | 1,001,393.78 USD | `1,354,278,000,000.00` | `746.04` | `740.12` | `0.000000` | -8,950.28 USD | `-0.89%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `745.30` | 53,346.34 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 53.35K USD at 745.3000 USD [API] | `2026-10-27 22:32:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.31` (Vol: 2,400,000.00 USD, Dist: `+2.47%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--0.48%`)
  * 48H Horizon: Short MP=`758.54` (Vol: 2,400,000.00 USD, Dist: `+2.50%`) | Long MP=`736.45` (Vol: 2,100,000.00 USD, Dist: `--0.48%`)
  * 3D Horizon: Short MP=`766.52` (Vol: 2,500,000.00 USD, Dist: `+3.58%`) | Long MP=`736.48` (Vol: 3,000,000.00 USD, Dist: `--0.48%`)
  * 7D Horizon: Short MP=`758.15` (Vol: 2,900,000.00 USD, Dist: `+2.45%`) | Long MP=`728.45` (Vol: 3,700,000.00 USD, Dist: `--1.56%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `156.50` | 159.16 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `166.50` | 607.23 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 124.74 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 295.71 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `211.50` | 1,360.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `212.50` | 260.74 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `217.50` | 1,090.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 4,210.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 306.02 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `257.50` | 4,370.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `265.50` | 835.53 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `274.50` | 21,760.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `301.50` | 6,050.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `303.50` | 22,510.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `304.50` | 349.57 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `306.50` | 299.45 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `308.50` | 977.02 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `310.50` | 1,590.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 501.60 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `315.50` | 1,450.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `316.50` | 21,900.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `323.50` | 895.12 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `328.50` | 315.03 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 1,650.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 377.19 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `334.50` | 312.09 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 1,120.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 652.65 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `350.50` | 1,580.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `352.50` | 12,030.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 366.69 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 103.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 240.43 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,240.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 3,910.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `379.50` | 645.15 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 1,910.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 16,920.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 46,890.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 103.88 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 168.06 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 396.50 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 318.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 605.16 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `402.50` | 1,590.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `408.50` | 3,450.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 28,660.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 614.52 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 106.17 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 13,320.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 350.69 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 465.79 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 2,660.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 1,450.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `427.50` | 141.93 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 638.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `431.50` | 582.09 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `439.50` | 1,800.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `451.50` | 12,680.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `454.50` | 4,220.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `455.50` | 1,070.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 13,790.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `457.50` | 463.45 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `467.50` | 1,950.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 5,450.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 5,410.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `476.50` | 5,800.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 2,550.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 2,120.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,610.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 3,240.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 5,440.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 4,010.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 3,930.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 4,290.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 1,160.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 3,360.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 3,560.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 1,040.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 10,750.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 2,300.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 1,460.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 1,210.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 4,130.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 16,980.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 1,630.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 632.08 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `536.50` | 100.33 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `537.50` | 4,300.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `541.50` | 472.19 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 4,380.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 272.25 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 212,310.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 13,970.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `547.50` | 531.07 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,770.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,290.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 959.69 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,420.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `554.50` | 2,010.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 591.61 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 5,680.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `559.50` | 212.61 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 10,280.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 583.40 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `564.50` | 14,880.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `566.50` | 1,590,000.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `570.50` | 393.64 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 715,280.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 862.44 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 222.91 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 275.37 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 2,320.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 15,440.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 10,240.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 666.88 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,540.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 1,530.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 100.39 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 44,800.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 1,680.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 100.98 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,060.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `599.50` | 116.90 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 303.76 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 1,610.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.50` | 508.62 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 2,210.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `610.50` | 213.67 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 527.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 2,280.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 427.16 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,510.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 343.33 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 5,410.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 1,260.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `622.50` | 2,110.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `623.50` | 1,050.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,460.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 11,970.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 16,020.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 326.30 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 664.32 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `629.50` | 3,680.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `631.50` | 6,320.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `632.50` | 125.87 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `633.50` | 1,920.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `634.50` | 276.64 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 5,910.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `636.50` | 5,140.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 1,110.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 432.90 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `639.50` | 33,550.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 2,310.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `641.50` | 1,670.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 9,470.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `643.50` | 8,490.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.50` | 3,820.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `646.50` | 4,290.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `649.50` | 136.39 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `650.50` | 424.13 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `651.50` | 633.26 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `654.50` | 97,530.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.50` | 2,250.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `656.50` | 122.77 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `658.50` | 4,800.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,340.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `661.50` | 463.71 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `662.50` | 19,830.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `663.50` | 2,070.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.70` | 31,430,000.00 USD | 31,430,000.00 USD | 5,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.50` | 31,430,000.00 USD | 31,430,000.00 USD | 15,920.00 USD | 4,540.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.30` | 31,400,000.00 USD | 31,400,000.00 USD | 20,740.00 USD | 13,710.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 5,440.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.10` | 31,360,000.00 USD | 31,360,000.00 USD | 29,510.00 USD | 11,670.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.90` | 31,300,000.00 USD | 31,300,000.00 USD | 24,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.70` | 31,280,000.00 USD | 31,280,000.00 USD | 63,110.00 USD | 25,520.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.50` | 31,190,000.00 USD | 31,190,000.00 USD | 21,750.00 USD | 3,950.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 3,040.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.30` | 31,150,000.00 USD | 31,150,000.00 USD | 180,930.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 2,570.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.10` | 30,970,000.00 USD | 30,970,000.00 USD | 45,090.00 USD | 11,440.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 3,360.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.90` | 30,900,000.00 USD | 30,900,000.00 USD | 34,940.00 USD | 8,400.00 USD | 9,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 13,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.70` | 30,850,000.00 USD | 30,850,000.00 USD | 71,570.00 USD | 20,180.00 USD | 30,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.50` | 30,720,000.00 USD | 30,720,000.00 USD | 341,560.00 USD | 33,610.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 567.76 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.30` | 30,320,000.00 USD | 30,320,000.00 USD | 207,590.00 USD | 24,950.00 USD | 36,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 259.68 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.10` | 30,050,000.00 USD | 30,050,000.00 USD | 34,650.00 USD | 26,950.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.90` | 29,980,000.00 USD | 29,980,000.00 USD | 137,210.00 USD | 15,000.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.70` | 29,790,000.00 USD | 29,790,000.00 USD | 219,200.00 USD | 26,460.00 USD | 43,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.50` | 29,500,000.00 USD | 29,500,000.00 USD | 238,360.00 USD | 25,700.00 USD | 63,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.30` | 29,170,000.00 USD | 29,170,000.00 USD | 107,140.00 USD | 5,910.00 USD | 6,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 1,610.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.10` | 29,050,000.00 USD | 29,050,000.00 USD | 108,560.00 USD | 5,470.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `679.90` | 28,930,000.00 USD | 28,930,000.00 USD | 53,400.00 USD | 13,050.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.70` | 28,860,000.00 USD | 28,860,000.00 USD | 64,060.00 USD | 9,530.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.50` | 28,770,000.00 USD | 28,770,000.00 USD | 72,680.00 USD | 4,270.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 31,450.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.30` | 28,690,000.00 USD | 28,690,000.00 USD | 14,400.00 USD | 13,390.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.10` | 28,620,000.00 USD | 28,620,000.00 USD | 106,100.00 USD | 10,210.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.90` | 28,500,000.00 USD | 28,500,000.00 USD | 573.20 USD | 11,710.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `684.50` | 42,430.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `684.70` | 28,480,000.00 USD | 28,480,000.00 USD | 49,570.00 USD | 6,480.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.50` | 28,420,000.00 USD | 28,420,000.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `685.50` | 1,290.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `686.50` | 2,280.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `687.50` | 198.69 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.50` | 28,400,000.00 USD | 28,400,000.00 USD | 19,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `689.50` | 885.32 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.30` | 28,380,000.00 USD | 28,380,000.00 USD | 81,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `690.50` | 7,080.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `691.10` | 28,300,000.00 USD | 28,300,000.00 USD | 34,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `691.50` | 5,430.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `691.90` | 28,260,000.00 USD | 28,260,000.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `692.50` | 5,580.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `692.70` | 28,190,000.00 USD | 28,190,000.00 USD | 48,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.50` | 28,140,000.00 USD | 28,140,000.00 USD | 36,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `693.50` | 2,590.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.30` | 28,100,000.00 USD | 28,100,000.00 USD | 16,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `694.50` | 513.93 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.10` | 28,090,000.00 USD | 28,090,000.00 USD | 27,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `695.50` | 470.85 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.90` | 28,060,000.00 USD | 28,060,000.00 USD | 34,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.70` | 28,030,000.00 USD | 28,030,000.00 USD | 27,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `697.50` | 28,000,000.00 USD | 28,000,000.00 USD | 72,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `697.50` | 2,340.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `698.30` | 27,930,000.00 USD | 27,930,000.00 USD | 29,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `698.50` | 303.15 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `699.10` | 27,900,000.00 USD | 27,900,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `699.50` | 20,100.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `699.90` | 27,880,000.00 USD | 27,880,000.00 USD | 8,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `700.50` | 1,130.00 USD | 983,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `700.70` | 27,870,000.00 USD | 27,870,000.00 USD | 22,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.50` | 27,850,000.00 USD | 27,850,000.00 USD | 28,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.30` | 27,820,000.00 USD | 27,820,000.00 USD | 60,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `702.50` | 2,080.00 USD | 982,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.10` | 27,760,000.00 USD | 27,760,000.00 USD | 91,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `703.50` | 3,820.00 USD | 980,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.90` | 27,670,000.00 USD | 27,670,000.00 USD | 51,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `704.50` | 2,720.00 USD | 976,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.70` | 27,610,000.00 USD | 27,610,000.00 USD | 101,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `705.50` | 27,510,000.00 USD | 27,510,000.00 USD | 74,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `705.50` | 88,830.00 USD | 974,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `706.30` | 27,440,000.00 USD | 27,440,000.00 USD | 60,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `706.50` | 34,680.00 USD | 885,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `707.10` | 27,380,000.00 USD | 27,380,000.00 USD | 25,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `707.50` | 22,380.00 USD | 850,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `707.90` | 27,350,000.00 USD | 27,350,000.00 USD | 50,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `708.50` | 171,950.00 USD | 828,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `708.70` | 27,300,000.00 USD | 27,300,000.00 USD | 50,270.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `709.50` | 27,250,000.00 USD | 27,250,000.00 USD | 38,330.00 USD | 25,300.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `709.50` | 339,560.00 USD | 656,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `710.30` | 27,170,000.00 USD | 27,170,000.00 USD | 92,740.00 USD | 34,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `710.50` | 46,020.00 USD | 316,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.10` | 27,040,000.00 USD | 27,040,000.00 USD | 102,220.00 USD | 66,110.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `711.50` | 11,630.00 USD | 270,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.90` | 26,850,000.00 USD | 26,850,000.00 USD | 220,260.00 USD | 12,480.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `712.50` | 229,760.00 USD | 259,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `712.70` | 26,590,000.00 USD | 26,590,000.00 USD | 84,130.00 USD | 44,490.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `713.50` | 26,420,000.00 USD | 26,420,000.00 USD | 236,420.00 USD | 36,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `713.50` | 20,280.00 USD | 29,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `714.30` | 26,150,000.00 USD | 26,150,000.00 USD | 465,170.00 USD | 14,760.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `714.50` | 157.90 USD | 9,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `715.10` | 25,640,000.00 USD | 25,640,000.00 USD | 103,840.00 USD | 10,540.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.90` | 25,510,000.00 USD | 25,510,000.00 USD | 160,860.00 USD | 28,610.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `716.50` | 789.58 USD | 8,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `716.70` | 25,280,000.00 USD | 25,280,000.00 USD | 88,230.00 USD | 31,000.00 USD | 32,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `717.50` | 25,130,000.00 USD | 25,130,000.00 USD | 144,440.00 USD | 73,680.00 USD | 100,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `717.50` | 3,700.00 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `718.30` | 24,810,000.00 USD | 24,810,000.00 USD | 1,060,000.00 USD | 105,150.00 USD | 128,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `718.50` | 104.18 USD | 4,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `719.10` | 23,520,000.00 USD | 23,520,000.00 USD | 811,950.00 USD | 76,100.00 USD | 137,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `719.90` | 22,490,000.00 USD | 22,490,000.00 USD | 240,880.00 USD | 65,800.00 USD | 63,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `720.70` | 22,120,000.00 USD | 22,120,000.00 USD | 428,760.00 USD | 53,100.00 USD | 79,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `721.50` | 21,560,000.00 USD | 21,560,000.00 USD | 472,160.00 USD | 102,240.00 USD | 197,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `721.50` | 998.56 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `722.30` | 20,790,000.00 USD | 20,790,000.00 USD | 905,840.00 USD | 66,420.00 USD | 122,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `723.10` | 19,690,000.00 USD | 19,690,000.00 USD | 632,090.00 USD | 36,240.00 USD | 94,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `723.90` | 18,930,000.00 USD | 18,930,000.00 USD | 244,290.00 USD | 23,200.00 USD | 30,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `724.70` | 18,630,000.00 USD | 18,630,000.00 USD | 259,230.00 USD | 105,290.00 USD | 54,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `725.50` | 18,220,000.00 USD | 18,220,000.00 USD | 202,000.00 USD | 152,060.00 USD | 86,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `726.30` | 17,770,000.00 USD | 17,770,000.00 USD | 643,490.00 USD | 91,860.00 USD | 80,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `727.10` | 16,960,000.00 USD | 16,960,000.00 USD | 354,600.00 USD | 62,590.00 USD | 81,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `727.90` | 16,460,000.00 USD | 16,460,000.00 USD | 362,040.00 USD | 187,450.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `728.70` | 15,780,000.00 USD | 15,780,000.00 USD | 667,330.00 USD | 49,940.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `729.50` | 15,010,000.00 USD | 15,010,000.00 USD | 1,040,000.00 USD | 56,220.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `730.30` | 13,870,000.00 USD | 13,870,000.00 USD | 216,600.00 USD | 76,200.00 USD | 55,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `731.10` | 13,520,000.00 USD | 13,520,000.00 USD | 313,700.00 USD | 41,120.00 USD | 97,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `731.50` | 3,290.00 USD | 3,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `731.90` | 13,070,000.00 USD | 13,070,000.00 USD | 350,450.00 USD | 62,730.00 USD | 139,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `732.70` | 12,510,000.00 USD | 12,510,000.00 USD | 945,530.00 USD | 209,330.00 USD | 194,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `733.50` | 11,160,000.00 USD | 11,160,000.00 USD | 1,610,000.00 USD | 147,090.00 USD | 181,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `734.30` | 9,230,000.00 USD | 9,230,000.00 USD | 1,280,000.00 USD | 153,350.00 USD | 290,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `735.10` | 7,500,000.00 USD | 7,500,000.00 USD | 609,290.00 USD | 173,140.00 USD | 95,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `735.90` | 6,630,000.00 USD | 6,630,000.00 USD | 705,930.00 USD | 92,060.00 USD | 242,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `736.70` | 5,590,000.00 USD | 5,590,000.00 USD | 1,480,000.00 USD | 183,880.00 USD | 290,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `737.50` | 3,630,000.00 USD | 3,630,000.00 USD | 1,680,000.00 USD | 156,810.00 USD | 310,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `738.30` | 1,480,000.00 USD | 1,480,000.00 USD | 1,150,000.00 USD | 34,870.00 USD | 100,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `739.10` | 200,330.00 USD | 200,330.00 USD | 125,830.00 USD | 18,090.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.90` | 564,520.00 USD | 564,520.00 USD | 518,470.00 USD | 0.00 USD | 46,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.70` | 975,520.00 USD | 975,520.00 USD | 403,990.00 USD | 0.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.50` | 1,150,000.00 USD | 1,150,000.00 USD | 174,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.30` | 1,190,000.00 USD | 1,190,000.00 USD | 38,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.50` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.30` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 64,190.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.10` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 125,110.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.90` | 2,040,000.00 USD | 2,040,000.00 USD | 456,130.00 USD | 62,280.00 USD | 66,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.70` | 2,190,000.00 USD | 2,190,000.00 USD | 77,830.00 USD | 24,970.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.50` | 2,550,000.00 USD | 2,550,000.00 USD | 180,040.00 USD | 146,640.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.30` | 3,030,000.00 USD | 3,030,000.00 USD | 469,360.00 USD | 15,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.10` | 3,970,000.00 USD | 3,970,000.00 USD | 848,020.00 USD | 29,520.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.90` | 4,150,000.00 USD | 4,150,000.00 USD | 140,170.00 USD | 21,070.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.70` | 4,610,000.00 USD | 4,610,000.00 USD | 286,530.00 USD | 57,220.00 USD | 113,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.50` | 4,860,000.00 USD | 4,860,000.00 USD | 157,660.00 USD | 62,000.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.30` | 5,470,000.00 USD | 5,470,000.00 USD | 267,050.00 USD | 147,360.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.10` | 7,920,000.00 USD | 7,920,000.00 USD | 2,040,000.00 USD | 196,860.00 USD | 212,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 211.49 USD | 211.49 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.90` | 9,220,000.00 USD | 9,220,000.00 USD | 956,810.00 USD | 110,320.00 USD | 236,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.70` | 10,770,000.00 USD | 10,770,000.00 USD | 1,170,000.00 USD | 181,410.00 USD | 201,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.50` | 11,620,000.00 USD | 11,620,000.00 USD | 614,330.00 USD | 81,400.00 USD | 147,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.30` | 12,760,000.00 USD | 12,760,000.00 USD | 611,810.00 USD | 227,030.00 USD | 309,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.10` | 15,050,000.00 USD | 15,050,000.00 USD | 2,030,000.00 USD | 74,130.00 USD | 177,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 1,050.00 USD | 1,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.90` | 16,610,000.00 USD | 16,610,000.00 USD | 1,090,000.00 USD | 127,480.00 USD | 345,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.70` | 17,580,000.00 USD | 17,580,000.00 USD | 881,020.00 USD | 54,840.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.50` | 18,220,000.00 USD | 18,220,000.00 USD | 463,560.00 USD | 99,410.00 USD | 69,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.30` | 18,990,000.00 USD | 18,990,000.00 USD | 600,390.00 USD | 119,310.00 USD | 55,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.10` | 19,560,000.00 USD | 19,560,000.00 USD | 386,410.00 USD | 71,930.00 USD | 109,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.90` | 20,100,000.00 USD | 20,100,000.00 USD | 411,510.00 USD | 72,630.00 USD | 53,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.70` | 20,850,000.00 USD | 20,850,000.00 USD | 522,790.00 USD | 126,850.00 USD | 106,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.50` | 21,510,000.00 USD | 21,510,000.00 USD | 343,050.00 USD | 103,900.00 USD | 211,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 8,270.00 USD | 9,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.30` | 22,700,000.00 USD | 22,700,000.00 USD | 1,090,000.00 USD | 64,820.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `774.50` | 130.12 USD | 9,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.10` | 23,090,000.00 USD | 23,090,000.00 USD | 255,460.00 USD | 84,870.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.90` | 23,670,000.00 USD | 23,670,000.00 USD | 418,980.00 USD | 93,060.00 USD | 65,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 1,050.00 USD | 10,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.70` | 24,120,000.00 USD | 24,120,000.00 USD | 372,750.00 USD | 14,720.00 USD | 69,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.50` | 24,820,000.00 USD | 24,820,000.00 USD | 535,390.00 USD | 104,660.00 USD | 54,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 2,880.00 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.30` | 25,790,000.00 USD | 25,790,000.00 USD | 776,240.00 USD | 73,550.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 11,100.00 USD | 24,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.10` | 26,730,000.00 USD | 26,730,000.00 USD | 739,180.00 USD | 73,260.00 USD | 125,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `779.50` | 301.67 USD | 25,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.90` | 27,170,000.00 USD | 27,170,000.00 USD | 305,540.00 USD | 65,800.00 USD | 63,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 5,430.00 USD | 30,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.70` | 27,770,000.00 USD | 27,770,000.00 USD | 465,730.00 USD | 53,100.00 USD | 79,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.50` | 28,280,000.00 USD | 28,280,000.00 USD | 219,880.00 USD | 102,240.00 USD | 197,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,620.00 USD | 32,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.30` | 29,560,000.00 USD | 29,560,000.00 USD | 1,130,000.00 USD | 55,190.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 247,020.00 USD | 279,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.10` | 30,370,000.00 USD | 30,370,000.00 USD | 646,700.00 USD | 41,740.00 USD | 117,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.90` | 30,750,000.00 USD | 30,750,000.00 USD | 342,600.00 USD | 14,770.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 2,220.00 USD | 281,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `784.70` | 31,180,000.00 USD | 31,180,000.00 USD | 372,010.00 USD | 32,520.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.50` | 31,460,000.00 USD | 31,460,000.00 USD | 241,040.00 USD | 26,600.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.30` | 31,680,000.00 USD | 31,680,000.00 USD | 150,920.00 USD | 29,730.00 USD | 43,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 607.96 USD | 282,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.10` | 31,860,000.00 USD | 31,860,000.00 USD | 139,020.00 USD | 25,910.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 130,890.00 USD | 412,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.90` | 32,220,000.00 USD | 32,220,000.00 USD | 247,660.00 USD | 34,670.00 USD | 75,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 126.16 USD | 413,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.70` | 32,490,000.00 USD | 32,490,000.00 USD | 152,570.00 USD | 49,210.00 USD | 64,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `789.50` | 32,910,000.00 USD | 32,910,000.00 USD | 378,130.00 USD | 26,520.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 1,980.00 USD | 415,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.30` | 33,090,000.00 USD | 33,090,000.00 USD | 148,670.00 USD | 26,690.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.10` | 33,340,000.00 USD | 33,340,000.00 USD | 201,460.00 USD | 32,830.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `791.50` | 6,430.00 USD | 421,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `791.90` | 33,450,000.00 USD | 33,450,000.00 USD | 114,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.70` | 33,500,000.00 USD | 33,500,000.00 USD | 47,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.50` | 33,530,000.00 USD | 33,530,000.00 USD | 32,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 158.70 USD | 421,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `794.30` | 33,570,000.00 USD | 33,570,000.00 USD | 36,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `794.50` | 179.56 USD | 421,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `795.10` | 33,600,000.00 USD | 33,600,000.00 USD | 29,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 422,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `795.90` | 33,640,000.00 USD | 33,640,000.00 USD | 41,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 172.84 USD | 422,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `796.70` | 33,670,000.00 USD | 33,670,000.00 USD | 28,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `797.50` | 33,730,000.00 USD | 33,730,000.00 USD | 57,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `798.30` | 33,770,000.00 USD | 33,770,000.00 USD | 46,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `799.10` | 33,790,000.00 USD | 33,790,000.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `799.90` | 33,790,000.00 USD | 33,790,000.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `800.70` | 33,800,000.00 USD | 33,800,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `801.50` | 33,820,000.00 USD | 33,820,000.00 USD | 19,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 761.42 USD | 423,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `802.30` | 33,840,000.00 USD | 33,840,000.00 USD | 21,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 279.27 USD | 423,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.10` | 33,850,000.00 USD | 33,850,000.00 USD | 7,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `803.90` | 33,860,000.00 USD | 33,860,000.00 USD | 6,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 1,080.00 USD | 424,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `804.70` | 33,860,000.00 USD | 33,860,000.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `805.50` | 33,870,000.00 USD | 33,870,000.00 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `806.30` | 33,880,000.00 USD | 33,880,000.00 USD | 3,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 44,210.00 USD | 468,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `807.10` | 33,890,000.00 USD | 33,890,000.00 USD | 13,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `807.90` | 33,890,000.00 USD | 33,890,000.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `808.70` | 33,900,000.00 USD | 33,900,000.00 USD | 7,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `809.50` | 33,900,000.00 USD | 33,900,000.00 USD | 4,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `810.30` | 33,910,000.00 USD | 33,910,000.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `810.50` | 5,440.00 USD | 474,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `811.50` | 265.36 USD | 474,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `812.70` | 33,920,000.00 USD | 33,920,000.00 USD | 5,610.00 USD | 0.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `813.50` | 33,940,000.00 USD | 33,940,000.00 USD | 19,630.00 USD | 4,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `814.30` | 33,980,000.00 USD | 33,980,000.00 USD | 17,040.00 USD | 13,710.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.10` | 34,020,000.00 USD | 34,020,000.00 USD | 29,510.00 USD | 8,370.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `815.90` | 34,050,000.00 USD | 34,050,000.00 USD | 18,470.00 USD | 3,300.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `816.70` | 34,110,000.00 USD | 34,110,000.00 USD | 45,300.00 USD | 13,980.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `817.50` | 34,160,000.00 USD | 34,160,000.00 USD | 34,600.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `818.30` | 34,190,000.00 USD | 34,190,000.00 USD | 11,380.00 USD | 3,950.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 205.44 USD | 474,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `819.10` | 34,370,000.00 USD | 34,370,000.00 USD | 180,010.00 USD | 0.00 USD | 1,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `819.90` | 34,420,000.00 USD | 34,420,000.00 USD | 29,650.00 USD | 8,380.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `820.70` | 34,460,000.00 USD | 34,460,000.00 USD | 22,270.00 USD | 9,720.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `821.50` | 34,510,000.00 USD | 34,510,000.00 USD | 58,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,840.00 USD | 486,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `823.50` | 1,730.00 USD | 488,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `831.50` | 10,040.00 USD | 498,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 499,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `835.50` | 340.88 USD | 499,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 625.70 USD | 500,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 125.62 USD | 500,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `839.50` | 572.54 USD | 501,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,680.00 USD | 503,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 153.34 USD | 503,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 173,300.00 USD | 677,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `845.50` | 338,650.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `849.50` | 416.25 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 108.99 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 138.43 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 171.10 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 313.72 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 6,240.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `866.50` | 236.55 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `868.50` | 1,530.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `869.50` | 452,190.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `876.50` | 911.56 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 11,910.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `879.50` | 4,540.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,750.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `889.50` | 772.09 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `892.50` | 3,350.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,510.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 392.04 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 901.23 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 922.34 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 39,480.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `923.50` | 196.71 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 285.05 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `930.50` | 3,240.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 952.65 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `944.50` | 112.40 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `945.50` | 110.62 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 398.14 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `958.50` | 67,090.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `962.50` | 202.12 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `963.50` | 838,250.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `967.50` | 1,940.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `970.50` | 5,780.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `974.50` | 59,840.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `983.50` | 27,790.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 99,550.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 1,570.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1007.50` | 174.30 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 703,540.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1028.50` | 102,850.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 676.71 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1049.50` | 294.91 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 5,220.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1071.50` | 1,550.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1118.50` | 6,160.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1124.50` | 20,050.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1134.50` | 3,800.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1139.50` | 55,050.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1144.50` | 153.36 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 9,150.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1169.50` | 367.22 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1173.50` | 14,380.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1183.50` | 158.59 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1192.50` | 133.56 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 30,170.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1208.50` | 385.51 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1220.50` | 1,220.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 1,030.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1244.50` | 8,710.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1252.50` | 100.20 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1258.50` | 341.05 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1261.50` | 201.84 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1264.50` | 206.11 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1283.50` | 115,520.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1287.50` | 163,360.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1300.50` | 773,450.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1320.50` | 14,140.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1325.50` | 19,880.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 102.29 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1331.50` | 23,490.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1375.50` | 247,750.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1387.50` | 5,540.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1399.50` | 10,090.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1402.50` | 178.12 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1413.50` | 139.94 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1432.50` | 360.99 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1444.50` | 697,520.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1460.50` | 8,940.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1470.50` | 14,460.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `538.50` | 1,680,000.00 USD | 0.00 USD | 1,680.00 USD | `-27.71%` | `TACTICAL (Retail Cluster)` |
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
| `Sell Stop` | `577.50` | 1,660,000.00 USD | 0.00 USD | 285.86 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 1,660,000.00 USD | 0.00 USD | 289.17 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 1,660,000.00 USD | 0.00 USD | 947.96 USD | `-22.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 1,660,000.00 USD | 0.00 USD | 289.59 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
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
| `Sell Stop` | `605.50` | 1,610,000.00 USD | 0.00 USD | 2,610.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
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
| `Sell Stop` | `676.50` | 1,540,000.00 USD | 0.00 USD | 63,000.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 1,470,000.00 USD | 0.00 USD | 3,360.00 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 1,470,000.00 USD | 0.00 USD | 175.31 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 1,470,000.00 USD | 0.00 USD | 2,370.00 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 1,470,000.00 USD | 0.00 USD | 31,240.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,440,000.00 USD | 0.00 USD | 24,240.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 1,410,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 1,410,000.00 USD | 0.00 USD | 7,610.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 1,400,000.00 USD | 0.00 USD | 371.25 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 1,400,000.00 USD | 0.00 USD | 610.01 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 1,400,000.00 USD | 0.00 USD | 2,590.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 1,400,000.00 USD | 0.00 USD | 7,490.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 1,390,000.00 USD | 0.00 USD | 108.57 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 1,390,000.00 USD | 0.00 USD | 2,530.00 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 1,390,000.00 USD | 0.00 USD | 8,410.00 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 1,380,000.00 USD | 0.00 USD | 374.34 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 1,380,000.00 USD | 0.00 USD | 30,620.00 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 1,350,000.00 USD | 0.00 USD | 9,690.00 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 1,340,000.00 USD | 0.00 USD | 4,340.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 1,340,000.00 USD | 0.00 USD | 5,460.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 1,330,000.00 USD | 0.00 USD | 3,300.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 1,330,000.00 USD | 0.00 USD | 190,140.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,140,000.00 USD | 0.00 USD | 3,900.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 1,130,000.00 USD | 0.00 USD | 1,790.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 1,130,000.00 USD | 0.00 USD | 2,790.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 1,130,000.00 USD | 0.00 USD | 1,070.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 1,130,000.00 USD | 0.00 USD | 2,770.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 1,120,000.00 USD | 0.00 USD | 11,860.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 1,110,000.00 USD | 0.00 USD | 205.88 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 1,110,000.00 USD | 0.00 USD | 1,070.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 1,110,000.00 USD | 0.00 USD | 783.29 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 1,110,000.00 USD | 0.00 USD | 623.82 USD | `-4.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 1,110,000.00 USD | 0.00 USD | 402.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 1,110,000.00 USD | 0.00 USD | 2,870.00 USD | `-4.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 1,110,000.00 USD | 0.00 USD | 94,480.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 1,010,000.00 USD | 0.00 USD | 88,360.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 923,500.00 USD | 0.00 USD | 6,050.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 917,450.00 USD | 0.00 USD | 1,470.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `717.50` | 915,980.00 USD | 0.00 USD | 246.82 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `718.50` | 915,730.00 USD | 0.00 USD | 727.84 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `719.50` | 915,010.00 USD | 0.00 USD | 1,270.00 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `720.50` | 913,740.00 USD | 0.00 USD | 2,710.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `721.50` | 911,020.00 USD | 0.00 USD | 6,780.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `722.50` | 904,240.00 USD | 0.00 USD | 114.16 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `723.50` | 904,130.00 USD | 0.00 USD | 605.57 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `724.50` | 903,520.00 USD | 0.00 USD | 9,620.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.50` | 893,910.00 USD | 0.00 USD | 9,140.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `726.50` | 884,760.00 USD | 0.00 USD | 470.77 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `727.50` | 884,290.00 USD | 0.00 USD | 1,650.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `728.50` | 882,640.00 USD | 0.00 USD | 8,950.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `729.50` | 873,700.00 USD | 0.00 USD | 6,820.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `730.50` | 866,870.00 USD | 0.00 USD | 1,640.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `731.50` | 865,230.00 USD | 0.00 USD | 583,440.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `732.50` | 281,790.00 USD | 0.00 USD | 1,600.00 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `733.50` | 280,190.00 USD | 0.00 USD | 2,100.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `734.50` | 278,100.00 USD | 0.00 USD | 651.50 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `735.50` | 277,450.00 USD | 0.00 USD | 1,820.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `736.50` | 275,620.00 USD | 0.00 USD | 5,530.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `737.50` | 270,090.00 USD | 0.00 USD | 7,300.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `738.50` | 262,790.00 USD | 0.00 USD | 5,070.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `739.50` | 257,720.00 USD | 0.00 USD | 790.53 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `740.50` | 256,930.00 USD | 0.00 USD | 155.50 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `741.50` | 256,780.00 USD | 0.00 USD | 6,570.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `742.50` | 250,200.00 USD | 0.00 USD | 247,900.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `743.50` | 2,300.00 USD | 0.00 USD | 897.40 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `744.50` | 1,400.00 USD | 0.00 USD | 1,400.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,000.00 USD | 1,000.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,290.00 USD | 288.90 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,590.00 USD | 301.24 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,750.00 USD | 157.19 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 2,750.00 USD | 999.83 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 3,880.00 USD | 1,130.00 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 4,890.00 USD | 1,010.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 7,620.00 USD | 2,730.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 8,630.00 USD | 1,010.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 9,150.00 USD | 525.13 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 10,130.00 USD | 979.13 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 18,380.00 USD | 8,250.00 USD | 0.00 USD | `+1.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 20,250.00 USD | 1,880.00 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 21,050.00 USD | 799.46 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 21,310.00 USD | 253.67 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 21,480.00 USD | 168.07 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 24,400.00 USD | 2,920.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 27,000.00 USD | 2,610.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 276,670.00 USD | 249,670.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 283,070.00 USD | 6,390.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 361,910.00 USD | 78,840.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 362,240.00 USD | 331.13 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 363,600.00 USD | 1,360.00 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 364,840.00 USD | 1,230.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 365,340.00 USD | 504.02 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 596,730.00 USD | 231,390.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 598,100.00 USD | 1,370.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 607,770.00 USD | 9,670.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 609,020.00 USD | 1,240.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 618,700.00 USD | 9,680.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 624,320.00 USD | 5,620.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 638,550.00 USD | 14,230.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 642,660.00 USD | 4,100.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 648,130.00 USD | 5,470.00 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 654,540.00 USD | 6,420.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 750,730.00 USD | 96,180.00 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 766,600.00 USD | 15,870.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 769,800.00 USD | 3,200.00 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 1,180,000.00 USD | 407,870.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 1,180,000.00 USD | 106.69 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 1,180,000.00 USD | 292.21 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 1,180,000.00 USD | 366.51 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 1,180,000.00 USD | 393.75 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 1,180,000.00 USD | 133.26 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 1,180,000.00 USD | 1,150.00 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 1,180,000.00 USD | 704.44 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 1,180,000.00 USD | 4,160.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `828.50` | 1,610,000.00 USD | 5,780.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 1,610,000.00 USD | 493.32 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `857.50` | 1,650,000.00 USD | 13,180.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `914.50` | 1,780,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
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
| `Buy Stop` | `1200.50` | 1,900,000.00 USD | 62,330.00 USD | 0.00 USD | `+61.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 1,900,000.00 USD | 1,250.00 USD | 0.00 USD | `+61.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 1,900,000.00 USD | 235.49 USD | 0.00 USD | `+64.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 1,910,000.00 USD | 3,580.00 USD | 0.00 USD | `+65.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 1,910,000.00 USD | 421.42 USD | 0.00 USD | `+67.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 1,910,000.00 USD | 3,750.00 USD | 0.00 USD | `+71.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 1,910,000.00 USD | 133.64 USD | 0.00 USD | `+74.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 1,910,000.00 USD | 685.36 USD | 0.00 USD | `+74.59%` | `TACTICAL (Retail Cluster)` |
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
| `1D` | `664.70` | 31,950,000.00 USD | 0.00 USD | 31,950,000.00 USD | 5,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.50` | 31,940,000.00 USD | 0.00 USD | 31,940,000.00 USD | 17,320.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.30` | 31,910,000.00 USD | 0.00 USD | 31,910,000.00 USD | 20,740.00 USD | 15,040.00 USD | 7,420.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.10` | 31,870,000.00 USD | 0.00 USD | 31,870,000.00 USD | 29,510.00 USD | 11,670.00 USD | 13,240.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `667.90` | 31,810,000.00 USD | 0.00 USD | 31,810,000.00 USD | 24,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `668.70` | 31,790,000.00 USD | 0.00 USD | 31,790,000.00 USD | 63,110.00 USD | 25,520.00 USD | 3,620.00 USD |
| `1D` | `669.50` | 31,700,000.00 USD | 0.00 USD | 31,700,000.00 USD | 21,750.00 USD | 3,950.00 USD | 10,960.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.30` | 31,660,000.00 USD | 0.00 USD | 31,660,000.00 USD | 180,930.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.10` | 31,480,000.00 USD | 0.00 USD | 31,480,000.00 USD | 45,090.00 USD | 11,440.00 USD | 11,420.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.90` | 31,410,000.00 USD | 0.00 USD | 31,410,000.00 USD | 34,940.00 USD | 8,400.00 USD | 9,720.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.70` | 31,360,000.00 USD | 0.00 USD | 31,360,000.00 USD | 71,570.00 USD | 20,180.00 USD | 30,760.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.50` | 31,230,000.00 USD | 0.00 USD | 31,230,000.00 USD | 341,560.00 USD | 33,610.00 USD | 28,520.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.30` | 30,830,000.00 USD | 0.00 USD | 30,830,000.00 USD | 207,590.00 USD | 24,950.00 USD | 36,730.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.10` | 30,560,000.00 USD | 0.00 USD | 30,560,000.00 USD | 34,650.00 USD | 26,950.00 USD | 5,300.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `675.90` | 30,490,000.00 USD | 0.00 USD | 30,490,000.00 USD | 137,210.00 USD | 15,000.00 USD | 41,810.00 USD |
| `1D` | `676.70` | 30,300,000.00 USD | 0.00 USD | 30,300,000.00 USD | 219,200.00 USD | 26,460.00 USD | 43,590.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.50` | 30,010,000.00 USD | 0.00 USD | 30,010,000.00 USD | 238,360.00 USD | 25,700.00 USD | 63,560.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.30` | 29,680,000.00 USD | 0.00 USD | 29,680,000.00 USD | 107,140.00 USD | 5,910.00 USD | 6,890.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.10` | 29,560,000.00 USD | 0.00 USD | 29,560,000.00 USD | 108,560.00 USD | 5,470.00 USD | 10,280.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.90` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 53,400.00 USD | 13,050.00 USD | 4,410.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.70` | 29,370,000.00 USD | 0.00 USD | 29,370,000.00 USD | 64,060.00 USD | 5,770.00 USD | 7,370.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.50` | 29,290,000.00 USD | 0.00 USD | 29,290,000.00 USD | 72,680.00 USD | 4,270.00 USD | 5,710.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.30` | 29,210,000.00 USD | 0.00 USD | 29,210,000.00 USD | 14,400.00 USD | 13,390.00 USD | 38,960.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.10` | 29,140,000.00 USD | 0.00 USD | 29,140,000.00 USD | 106,100.00 USD | 10,210.00 USD | 7,590.00 USD |
| `1D` | `683.90` | 29,020,000.00 USD | 0.00 USD | 29,020,000.00 USD | 573.20 USD | 11,710.00 USD | 5,590.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.70` | 29,000,000.00 USD | 0.00 USD | 29,000,000.00 USD | 49,570.00 USD | 6,480.00 USD | 3,410.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.50` | 28,940,000.00 USD | 0.00 USD | 28,940,000.00 USD | 19,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.50` | 28,920,000.00 USD | 0.00 USD | 28,920,000.00 USD | 23,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.30` | 28,900,000.00 USD | 0.00 USD | 28,900,000.00 USD | 81,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `691.10` | 28,820,000.00 USD | 0.00 USD | 28,820,000.00 USD | 34,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.90` | 28,780,000.00 USD | 0.00 USD | 28,780,000.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `1D` | `692.70` | 28,710,000.00 USD | 0.00 USD | 28,710,000.00 USD | 48,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.50` | 28,660,000.00 USD | 0.00 USD | 28,660,000.00 USD | 36,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.30` | 28,620,000.00 USD | 0.00 USD | 28,620,000.00 USD | 16,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.10` | 28,610,000.00 USD | 0.00 USD | 28,610,000.00 USD | 27,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `695.90` | 28,580,000.00 USD | 0.00 USD | 28,580,000.00 USD | 34,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `696.70` | 28,540,000.00 USD | 0.00 USD | 28,540,000.00 USD | 27,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `1D` | `697.50` | 28,520,000.00 USD | 0.00 USD | 28,520,000.00 USD | 72,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `698.30` | 28,440,000.00 USD | 0.00 USD | 28,440,000.00 USD | 29,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `699.10` | 28,410,000.00 USD | 0.00 USD | 28,410,000.00 USD | 18,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `1D` | `699.90` | 28,400,000.00 USD | 0.00 USD | 28,400,000.00 USD | 8,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.70` | 28,390,000.00 USD | 0.00 USD | 28,390,000.00 USD | 22,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.50` | 28,360,000.00 USD | 0.00 USD | 28,360,000.00 USD | 28,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.30` | 28,340,000.00 USD | 0.00 USD | 28,340,000.00 USD | 64,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.10` | 28,270,000.00 USD | 0.00 USD | 28,270,000.00 USD | 91,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `703.90` | 28,180,000.00 USD | 0.00 USD | 28,180,000.00 USD | 51,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `704.70` | 28,130,000.00 USD | 0.00 USD | 28,130,000.00 USD | 101,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `705.50` | 28,030,000.00 USD | 0.00 USD | 28,030,000.00 USD | 74,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `706.30` | 27,950,000.00 USD | 0.00 USD | 27,950,000.00 USD | 60,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `1D` | `707.10` | 27,890,000.00 USD | 0.00 USD | 27,890,000.00 USD | 25,680.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `707.90` | 27,870,000.00 USD | 0.00 USD | 27,870,000.00 USD | 50,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.70` | 27,820,000.00 USD | 0.00 USD | 27,820,000.00 USD | 50,270.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `1D` | `709.50` | 27,760,000.00 USD | 0.00 USD | 27,760,000.00 USD | 38,330.00 USD | 25,300.00 USD | 20,190.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `1D` | `710.30` | 27,680,000.00 USD | 0.00 USD | 27,680,000.00 USD | 92,740.00 USD | 37,710.00 USD | 8,460.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.10` | 27,540,000.00 USD | 0.00 USD | 27,540,000.00 USD | 102,220.00 USD | 66,110.00 USD | 28,450.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `711.90` | 27,340,000.00 USD | 0.00 USD | 27,340,000.00 USD | 220,260.00 USD | 12,480.00 USD | 23,220.00 USD |
| `1D` | `712.70` | 27,080,000.00 USD | 0.00 USD | 27,080,000.00 USD | 84,130.00 USD | 44,490.00 USD | 40,890.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `1D` | `713.50` | 26,920,000.00 USD | 0.00 USD | 26,920,000.00 USD | 236,420.00 USD | 36,340.00 USD | 0.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `1D` | `714.30` | 26,640,000.00 USD | 0.00 USD | 26,640,000.00 USD | 465,170.00 USD | 14,760.00 USD | 27,410.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `715.10` | 26,130,000.00 USD | 0.00 USD | 26,130,000.00 USD | 103,840.00 USD | 10,540.00 USD | 11,420.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `715.90` | 26,010,000.00 USD | 0.00 USD | 26,010,000.00 USD | 160,860.00 USD | 28,610.00 USD | 39,970.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `716.70` | 25,780,000.00 USD | 0.00 USD | 25,780,000.00 USD | 88,230.00 USD | 31,000.00 USD | 32,090.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `1D` | `717.50` | 25,630,000.00 USD | 0.00 USD | 25,630,000.00 USD | 144,440.00 USD | 73,680.00 USD | 100,350.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `718.30` | 25,310,000.00 USD | 0.00 USD | 25,310,000.00 USD | 1,060,000.00 USD | 105,150.00 USD | 128,080.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.10` | 24,010,000.00 USD | 0.00 USD | 24,010,000.00 USD | 811,950.00 USD | 76,100.00 USD | 137,910.00 USD |
| `1D` | `719.90` | 22,990,000.00 USD | 0.00 USD | 22,990,000.00 USD | 240,880.00 USD | 65,800.00 USD | 63,680.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.70` | 22,620,000.00 USD | 0.00 USD | 22,620,000.00 USD | 428,760.00 USD | 53,100.00 USD | 79,750.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.50` | 22,060,000.00 USD | 0.00 USD | 22,060,000.00 USD | 472,160.00 USD | 102,240.00 USD | 197,320.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.30` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 905,840.00 USD | 66,420.00 USD | 122,250.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.10` | 20,190,000.00 USD | 0.00 USD | 20,190,000.00 USD | 632,090.00 USD | 36,240.00 USD | 94,660.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `723.90` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 244,290.00 USD | 23,200.00 USD | 43,980.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.70` | 19,120,000.00 USD | 0.00 USD | 19,120,000.00 USD | 259,230.00 USD | 111,960.00 USD | 71,100.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.50` | 18,670,000.00 USD | 0.00 USD | 18,670,000.00 USD | 202,000.00 USD | 138,800.00 USD | 69,190.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.30` | 18,260,000.00 USD | 0.00 USD | 18,260,000.00 USD | 643,490.00 USD | 91,860.00 USD | 80,490.00 USD |
| `1D` | `727.10` | 17,450,000.00 USD | 0.00 USD | 17,450,000.00 USD | 354,600.00 USD | 62,590.00 USD | 81,120.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.90` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 362,040.00 USD | 187,450.00 USD | 130,690.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.70` | 16,270,000.00 USD | 0.00 USD | 16,270,000.00 USD | 667,330.00 USD | 49,940.00 USD | 57,330.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.50` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 1,040,000.00 USD | 56,220.00 USD | 37,460.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.30` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 216,600.00 USD | 76,200.00 USD | 55,280.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.10` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 313,700.00 USD | 41,120.00 USD | 97,410.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `731.90` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 350,450.00 USD | 62,730.00 USD | 139,810.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.70` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 945,530.00 USD | 209,330.00 USD | 194,340.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.50` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 1,610,000.00 USD | 147,090.00 USD | 181,530.00 USD |
| `1D` | `734.30` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 1,280,000.00 USD | 153,350.00 USD | 290,290.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `735.10` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 609,290.00 USD | 173,140.00 USD | 95,370.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.90` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 705,930.00 USD | 92,060.00 USD | 242,490.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.70` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 1,480,000.00 USD | 183,880.00 USD | 290,430.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.50` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 1,680,000.00 USD | 156,810.00 USD | 310,340.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.30` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,150,000.00 USD | 34,870.00 USD | 100,140.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.10` | 689,070.00 USD | 0.00 USD | 689,070.00 USD | 125,830.00 USD | 18,090.00 USD | 0.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `739.90` | 545,160.00 USD | 0.00 USD | 545,160.00 USD | 518,470.00 USD | 0.00 USD | 26,690.00 USD |
| `1D` | `740.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `740.70` | 411,010.00 USD | 411,010.00 USD | 0.00 USD | 403,990.00 USD | 0.00 USD | 7,010.00 USD |
| `1D` | `741.50` | 585,010.00 USD | 585,010.00 USD | 0.00 USD | 174,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.30` | 623,650.00 USD | 623,650.00 USD | 0.00 USD | 38,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `753.50` | 649,340.00 USD | 649,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,690.00 USD |
| `1D` | `754.30` | 764,180.00 USD | 764,180.00 USD | 0.00 USD | 0.00 USD | 70,850.00 USD | 43,990.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.10` | 926,410.00 USD | 926,410.00 USD | 0.00 USD | 0.00 USD | 125,110.00 USD | 37,120.00 USD |
| `1D` | `755.90` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 456,130.00 USD | 62,280.00 USD | 66,220.00 USD |
| `1D` | `756.70` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 77,830.00 USD | 24,970.00 USD | 49,060.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.50` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 180,040.00 USD | 146,640.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.30` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 469,360.00 USD | 15,010.00 USD | 0.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.10` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 848,020.00 USD | 29,520.00 USD | 54,810.00 USD |
| `1D` | `759.90` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 140,170.00 USD | 21,070.00 USD | 22,840.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.70` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 286,530.00 USD | 57,220.00 USD | 113,560.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.50` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 157,660.00 USD | 62,000.00 USD | 30,570.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.30` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 267,050.00 USD | 147,360.00 USD | 200,700.00 USD |
| `1D` | `763.10` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 2,040,000.00 USD | 196,860.00 USD | 212,100.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.90` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 956,810.00 USD | 110,320.00 USD | 236,480.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.70` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 1,170,000.00 USD | 181,410.00 USD | 201,200.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.50` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 614,330.00 USD | 81,400.00 USD | 147,690.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.30` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 611,810.00 USD | 227,030.00 USD | 309,320.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.10` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 2,030,000.00 USD | 74,130.00 USD | 177,460.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `767.90` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 1,090,000.00 USD | 127,480.00 USD | 345,920.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.70` | 17,060,000.00 USD | 17,060,000.00 USD | 0.00 USD | 881,020.00 USD | 54,840.00 USD | 50,240.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.50` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 463,560.00 USD | 102,750.00 USD | 77,500.00 USD |
| `1D` | `770.30` | 18,470,000.00 USD | 18,470,000.00 USD | 0.00 USD | 600,390.00 USD | 111,580.00 USD | 55,140.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.10` | 18,990,000.00 USD | 18,990,000.00 USD | 0.00 USD | 386,410.00 USD | 53,140.00 USD | 75,700.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `771.90` | 19,530,000.00 USD | 19,530,000.00 USD | 0.00 USD | 411,510.00 USD | 72,630.00 USD | 53,060.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.70` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 522,790.00 USD | 126,850.00 USD | 106,970.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.50` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 343,050.00 USD | 103,900.00 USD | 211,530.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.30` | 22,130,000.00 USD | 22,130,000.00 USD | 0.00 USD | 1,090,000.00 USD | 64,820.00 USD | 33,460.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.10` | 22,520,000.00 USD | 22,520,000.00 USD | 0.00 USD | 255,460.00 USD | 84,870.00 USD | 51,100.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `775.90` | 23,100,000.00 USD | 23,100,000.00 USD | 0.00 USD | 423,190.00 USD | 93,060.00 USD | 65,760.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `776.70` | 23,560,000.00 USD | 23,560,000.00 USD | 0.00 USD | 372,750.00 USD | 14,720.00 USD | 69,910.00 USD |
| `1D` | `777.50` | 24,250,000.00 USD | 24,250,000.00 USD | 0.00 USD | 535,390.00 USD | 104,660.00 USD | 54,080.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.30` | 25,230,000.00 USD | 25,230,000.00 USD | 0.00 USD | 776,240.00 USD | 73,550.00 USD | 126,530.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `779.10` | 26,170,000.00 USD | 26,170,000.00 USD | 0.00 USD | 739,180.00 USD | 73,260.00 USD | 125,870.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.90` | 26,600,000.00 USD | 26,600,000.00 USD | 0.00 USD | 305,540.00 USD | 65,800.00 USD | 63,680.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.70` | 27,200,000.00 USD | 27,200,000.00 USD | 0.00 USD | 465,730.00 USD | 53,100.00 USD | 79,750.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.50` | 27,720,000.00 USD | 27,720,000.00 USD | 0.00 USD | 219,880.00 USD | 102,240.00 USD | 197,320.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.30` | 29,000,000.00 USD | 29,000,000.00 USD | 0.00 USD | 1,130,000.00 USD | 55,190.00 USD | 87,450.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.10` | 29,800,000.00 USD | 29,800,000.00 USD | 0.00 USD | 646,700.00 USD | 41,740.00 USD | 117,800.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `783.90` | 30,180,000.00 USD | 30,180,000.00 USD | 0.00 USD | 342,600.00 USD | 14,770.00 USD | 23,850.00 USD |
| `1D` | `784.70` | 30,610,000.00 USD | 30,610,000.00 USD | 0.00 USD | 372,010.00 USD | 32,520.00 USD | 25,700.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.50` | 30,890,000.00 USD | 30,890,000.00 USD | 0.00 USD | 241,040.00 USD | 22,730.00 USD | 13,340.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.30` | 31,090,000.00 USD | 31,090,000.00 USD | 0.00 USD | 150,920.00 USD | 20,330.00 USD | 26,240.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.10` | 31,270,000.00 USD | 31,270,000.00 USD | 0.00 USD | 139,020.00 USD | 25,910.00 USD | 14,270.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.90` | 31,620,000.00 USD | 31,620,000.00 USD | 0.00 USD | 247,660.00 USD | 34,670.00 USD | 75,010.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.70` | 31,890,000.00 USD | 31,890,000.00 USD | 0.00 USD | 155,720.00 USD | 49,210.00 USD | 64,430.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.50` | 32,310,000.00 USD | 32,310,000.00 USD | 0.00 USD | 378,130.00 USD | 26,520.00 USD | 13,980.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.30` | 32,500,000.00 USD | 32,500,000.00 USD | 0.00 USD | 148,670.00 USD | 26,690.00 USD | 13,860.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.10` | 32,740,000.00 USD | 32,740,000.00 USD | 0.00 USD | 201,460.00 USD | 32,830.00 USD | 8,530.00 USD |
| `1D` | `791.90` | 32,860,000.00 USD | 32,860,000.00 USD | 0.00 USD | 114,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.70` | 32,910,000.00 USD | 32,910,000.00 USD | 0.00 USD | 47,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.50` | 32,940,000.00 USD | 32,940,000.00 USD | 0.00 USD | 32,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `794.30` | 32,980,000.00 USD | 32,980,000.00 USD | 0.00 USD | 36,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `795.10` | 33,000,000.00 USD | 33,000,000.00 USD | 0.00 USD | 29,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `795.90` | 33,050,000.00 USD | 33,050,000.00 USD | 0.00 USD | 41,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `796.70` | 33,070,000.00 USD | 33,070,000.00 USD | 0.00 USD | 28,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `797.50` | 33,130,000.00 USD | 33,130,000.00 USD | 0.00 USD | 57,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `798.30` | 33,180,000.00 USD | 33,180,000.00 USD | 0.00 USD | 46,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.10` | 33,200,000.00 USD | 33,200,000.00 USD | 0.00 USD | 15,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `799.90` | 33,200,000.00 USD | 33,200,000.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `800.70` | 33,210,000.00 USD | 33,210,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `801.50` | 33,230,000.00 USD | 33,230,000.00 USD | 0.00 USD | 19,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `1D` | `802.30` | 33,250,000.00 USD | 33,250,000.00 USD | 0.00 USD | 21,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.10` | 33,260,000.00 USD | 33,260,000.00 USD | 0.00 USD | 7,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `803.90` | 33,260,000.00 USD | 33,260,000.00 USD | 0.00 USD | 6,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 0.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD |
| `1D` | `804.70` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 3,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 0.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD |
| `1D` | `805.50` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 11,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `806.30` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 3,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `1D` | `807.10` | 33,300,000.00 USD | 33,300,000.00 USD | 0.00 USD | 13,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `1D` | `807.90` | 33,300,000.00 USD | 33,300,000.00 USD | 0.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 0.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD |
| `1D` | `808.70` | 33,310,000.00 USD | 33,310,000.00 USD | 0.00 USD | 7,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `1D` | `809.50` | 33,310,000.00 USD | 33,310,000.00 USD | 0.00 USD | 4,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `1D` | `810.30` | 33,310,000.00 USD | 33,310,000.00 USD | 0.00 USD | 2,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `7D` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `1D` | `812.70` | 33,330,000.00 USD | 33,330,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 8,070.00 USD |
| `1D` | `813.50` | 33,360,000.00 USD | 33,360,000.00 USD | 0.00 USD | 21,030.00 USD | 5,880.00 USD | 3,380.00 USD |
| `7D` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `1D` | `814.30` | 33,390,000.00 USD | 33,390,000.00 USD | 0.00 USD | 17,040.00 USD | 13,710.00 USD | 7,420.00 USD |
| `7D` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `1D` | `815.10` | 33,440,000.00 USD | 33,440,000.00 USD | 0.00 USD | 29,510.00 USD | 8,370.00 USD | 3,960.00 USD |
| `7D` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `1D` | `815.90` | 33,470,000.00 USD | 33,470,000.00 USD | 0.00 USD | 18,470.00 USD | 3,300.00 USD | 9,290.00 USD |
| `7D` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `1D` | `816.70` | 33,530,000.00 USD | 33,530,000.00 USD | 0.00 USD | 45,300.00 USD | 13,980.00 USD | 3,620.00 USD |
| `7D` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `1D` | `817.50` | 33,580,000.00 USD | 33,580,000.00 USD | 0.00 USD | 34,600.00 USD | 11,530.00 USD | 0.00 USD |
| `7D` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `1D` | `818.30` | 33,600,000.00 USD | 33,600,000.00 USD | 0.00 USD | 11,380.00 USD | 3,950.00 USD | 10,960.00 USD |
| `7D` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `1D` | `819.10` | 33,780,000.00 USD | 33,780,000.00 USD | 0.00 USD | 180,010.00 USD | 0.00 USD | 1,130.00 USD |
| `7D` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `1D` | `819.90` | 33,830,000.00 USD | 33,830,000.00 USD | 0.00 USD | 29,650.00 USD | 8,380.00 USD | 9,280.00 USD |
| `1D` | `820.70` | 33,870,000.00 USD | 33,870,000.00 USD | 0.00 USD | 22,270.00 USD | 9,720.00 USD | 8,860.00 USD |
| `7D` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `1D` | `821.50` | 33,930,000.00 USD | 33,930,000.00 USD | 0.00 USD | 58,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
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
  * Total Open Interest: `1.22B` | Total OI Tokens: `1,642,316.5 BNB`
  * 1h OI Change: `-0.87%` | 4h OI Change: `-2.10%` | 24h OI Change: `-3.90%`
  * Exchange Breakdown: Binance=`573.40M` | Bybit=`104.86M` | OKX=`53.18M` | Hyperliquid=`45.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `54.75K` | Last 24h: `109.28K` | Last 3d: `307.00K` | Last 7d: `451.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0087%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0087%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0000%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `43.87%` | `56.13%` | `0.78` | 499,590,000.00 USD |
| `15M` | `Binance` | `44.83%` | `55.17%` | `0.81` | 172,480,000.00 USD |
| `15M` | `OKX` | `44.49%` | `55.51%` | `0.80` | 67,230,000.00 USD |
| `15M` | `Bybit` | `37.59%` | `62.41%` | `0.60` | 66,670,000.00 USD |
| `15M` | `KuCoin` | `40.02%` | `59.98%` | `0.67` | 3,650,000.00 USD |
| `15M` | `Gate` | `46.44%` | `53.56%` | `0.87` | 29,970,000.00 USD |
| `15M` | `Bitget` | `37.27%` | `62.73%` | `0.59` | 25,250,000.00 USD |
| `15M` | `BingX` | `47.37%` | `52.63%` | `0.90` | 13,750,000.00 USD |
| `15M` | `MEXC` | `53.92%` | `46.08%` | `1.17` | 39,450,000.00 USD |
| `15M` | `Bitunix` | `44.49%` | `55.51%` | `0.80` | 28,830,000.00 USD |
| `15M` | `Hyperliquid` | `32.87%` | `67.13%` | `0.49` | 17,740,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.23%` | `48.77%` | `1.05` | 4,750,000.00 USD |
| `15M` | `Crypto.com` | `41.94%` | `58.06%` | `0.72` | 1,200,000.00 USD |
| `15M` | `WhiteBIT` | `17.6%` | `82.4%` | `0.21` | 1,240,000.00 USD |
| `15M` | `HTX` | `42.6%` | `57.4%` | `0.74` | 339,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `59.57%` | `40.43%` | `1.47` | 5,420,000.00 USD |
| `15M` | `Aster` | `44.81%` | `55.19%` | `0.81` | 4,400,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `41.47%` | `58.53%` | `0.71` | 17,200,000.00 USD |
| `15M` | `Whale Positions` | `44.83%` | `55.17%` | `0.81` | 172,480,000.00 USD |
| `15M` | `Global Accounts` | `43.87%` | `56.13%` | `0.78` | 499,590,000.00 USD |
| `1H` | `BNB` | `44.73%` | `55.27%` | `0.81` | 693,650,000.00 USD |
| `1H` | `Binance` | `45.61%` | `54.39%` | `0.84` | 237,530,000.00 USD |
| `1H` | `OKX` | `44.74%` | `55.26%` | `0.81` | 94,020,000.00 USD |
| `1H` | `Bybit` | `36.79%` | `63.21%` | `0.58` | 90,760,000.00 USD |
| `1H` | `KuCoin` | `41.91%` | `58.09%` | `0.72` | 4,130,000.00 USD |
| `1H` | `Gate` | `48.54%` | `51.46%` | `0.94` | 47,380,000.00 USD |
| `1H` | `Bitget` | `38.76%` | `61.24%` | `0.63` | 31,380,000.00 USD |
| `1H` | `BingX` | `49.59%` | `50.41%` | `0.98` | 28,330,000.00 USD |
| `1H` | `MEXC` | `54.79%` | `45.21%` | `1.21` | 55,430,000.00 USD |
| `1H` | `Bitunix` | `43.14%` | `56.86%` | `0.76` | 37,440,000.00 USD |
| `1H` | `Hyperliquid` | `38.06%` | `61.94%` | `0.61` | 19,370,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.19%` | `44.81%` | `1.23` | 8,360,000.00 USD |
| `1H` | `Crypto.com` | `45.59%` | `54.41%` | `0.84` | 1,690,000.00 USD |
| `1H` | `WhiteBIT` | `28.34%` | `71.66%` | `0.40` | 5,030,000.00 USD |
| `1H` | `HTX` | `38.93%` | `61.07%` | `0.64` | 571,350.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.3%` | `47.7%` | `1.10` | 6,620,000.00 USD |
| `1H` | `Aster` | `45.57%` | `54.43%` | `0.84` | 5,950,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.02%` | `56.98%` | `0.76` | 19,640,000.00 USD |
| `1H` | `Whale Positions` | `45.61%` | `54.39%` | `0.84` | 237,530,000.00 USD |
| `1H` | `Global Accounts` | `44.73%` | `55.27%` | `0.81` | 693,650,000.00 USD |
| `4H` | `BNB` | `44.49%` | `55.51%` | `0.80` | 1,480,000,000.00 USD |
| `4H` | `Binance` | `45.04%` | `54.96%` | `0.82` | 497,140,000.00 USD |
| `4H` | `OKX` | `43.14%` | `56.86%` | `0.76` | 203,510,000.00 USD |
| `4H` | `Bybit` | `38.44%` | `61.56%` | `0.62` | 161,150,000.00 USD |
| `4H` | `KuCoin` | `43.2%` | `56.8%` | `0.76` | 7,920,000.00 USD |
| `4H` | `Gate` | `48.32%` | `51.68%` | `0.93` | 116,520,000.00 USD |
| `4H` | `Bitget` | `39.5%` | `60.5%` | `0.65` | 56,740,000.00 USD |
| `4H` | `BingX` | `51.27%` | `48.73%` | `1.05` | 69,070,000.00 USD |
| `4H` | `MEXC` | `53.32%` | `46.68%` | `1.14` | 138,270,000.00 USD |
| `4H` | `Bitunix` | `46.14%` | `53.86%` | `0.86` | 84,620,000.00 USD |
| `4H` | `Hyperliquid` | `36.81%` | `63.19%` | `0.58` | 36,700,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.54%` | `47.46%` | `1.11` | 18,230,000.00 USD |
| `4H` | `Crypto.com` | `45.83%` | `54.17%` | `0.85` | 2,990,000.00 USD |
| `4H` | `WhiteBIT` | `14.73%` | `85.27%` | `0.17` | 23,670,000.00 USD |
| `4H` | `HTX` | `36.13%` | `63.87%` | `0.57` | 2,130,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.02%` | `55.98%` | `0.79` | 20,830,000.00 USD |
| `4H` | `Aster` | `42.23%` | `57.77%` | `0.73` | 12,920,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.9%` | `59.1%` | `0.69` | 32,210,000.00 USD |
| `4H` | `Whale Positions` | `45.04%` | `54.96%` | `0.82` | 497,140,000.00 USD |
| `4H` | `Global Accounts` | `44.49%` | `55.51%` | `0.80` | 1,480,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `745.95` | `745.96` | `745.95` | `746.85` | `745.05` | 3,520,898.41 USD | 1,701,969.64 USD | 1,818,928.78 USD | -116,959.14 USD | `-3.32%` | `0B / 0S` |
| `0:00 UTC` | `746.25` | `745.96` | `746.25` | `746.85` | `745.05` | 2,334,703.88 USD | 1,240,058.73 USD | 1,094,645.16 USD | 145,413.57 USD | `+6.23%` | `1B / 0S` |
| `5:00 UTC` | `745.35` | `745.34` | `745.35` | `745.95` | `744.45` | 2,053,811.83 USD | 1,008,932.17 USD | 1,044,879.66 USD | -35,947.48 USD | `-1.75%` | `0B / 0S` |
| `0:00 UTC` | `743.55` | `743.83` | `743.55` | `745.05` | `742.95` | 4,178,944.72 USD | 2,213,489.92 USD | 1,965,454.80 USD | 248,035.12 USD | `+5.94%` | `0B / 1S` |
| `5:00 UTC` | `745.05` | `744.69` | `745.05` | `745.65` | `743.85` | 1,732,972.70 USD | 1,039,625.11 USD | 693,347.59 USD | 346,277.52 USD | `+19.98%` | `0B / 0S` |
| `0:00 UTC` | `744.15` | `744.46` | `744.15` | `745.35` | `743.85` | 2,147,535.09 USD | 1,307,335.66 USD | 840,199.43 USD | 467,136.24 USD | `+21.75%` | `0B / 0S` |
| `5:00 UTC` | `744.45` | `744.43` | `744.45` | `745.05` | `743.85` | 1,240,697.54 USD | 644,810.68 USD | 595,886.86 USD | 48,923.82 USD | `+3.94%` | `0B / 0S` |
| `0:00 UTC` | `745.35` | `745.38` | `745.35` | `746.25` | `744.45` | 2,107,319.68 USD | 1,122,788.81 USD | 984,530.87 USD | 138,257.94 USD | `+6.56%` | `1B / 1S` |
| `5:00 UTC` | `745.35` | `745.55` | `745.35` | `746.25` | `745.05` | 1,714,180.55 USD | 1,005,910.28 USD | 708,270.27 USD | 297,640.01 USD | `+17.36%` | `2B / 0S` |
| `0:00 UTC` | `743.25` | `741.16` | `743.25` | `745.65` | `737.55` | 20,211,595.12 USD | 5,570,091.68 USD | 14,641,503.44 USD | -9,071,411.76 USD | `-44.88%` | `2B / 11S` |

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
| `5m` | 123,980.00 USD | 943,850.00 USD | **`ACCUMULATION`** |
| `15m` | -3,860,000.00 USD | -11,250,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -3,910,000.00 USD | -10,820,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,790,000.00 USD | -10,420,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,820,000.00 USD | -8,250,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -6,120,000.00 USD | -17,280,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,560,000.00 USD | -13,580,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,180,000.00 USD | -2,560,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -13,130,000.00 USD | -22,560,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 1,160,000.00 USD | -36,220,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -31,570,000.00 USD | -54,280,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -129,880,000.00 USD | -380,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+123.98K` | 15m=`-3.86M` | 1h=`-3.79M` | 24h=`+1.16M`
* Futures Capital Netflows: 5m=`+943.85K` | 15m=`-11.25M` | 1h=`-10.42M` | 24h=`-36.22M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `740.37` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `736.89` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `749.06`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `752.01` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `755.49` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `743.32`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`744.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
