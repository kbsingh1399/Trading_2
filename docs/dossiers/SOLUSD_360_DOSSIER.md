# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:04:09 IST` (`2026-10-29 17:34:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `101.42` | **Live Ask Quote**: `101.67` | **Mid Price**: `101.55`
- **Spread Points**: `25.00` | **Spread BPS**: `24.62 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `101.55` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `102.26` | Lower -3.00σ Band: `100.83`
  * Upper +2.51σ Band: `102.10` | Lower -2.51σ Band: `100.99`
  * Upper +2.01σ Band: `101.97` | Lower -2.01σ Band: `101.12`
  * Upper +2.00σ Band: `101.95` | Lower -2.00σ Band: `101.14`
  * Upper +1.28σ Band: `101.83` | Lower -1.28σ Band: `101.26`
  * Upper +1.00σ Band: `101.75` | Lower -1.00σ Band: `101.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`101.55` | EMA-20=`101.55` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`101.55` (Slope: `+0.0000`) | EMA-100=`101.55`
  * Institutional Anchors: EMA-144=`101.55` | EMA-200=`101.55` (Slope: `+0.0000`) | EMA-233=`101.55`
- **Range Boundaries**: 24H High=`102.56` | 24H Low=`100.53` | Weekly High=`103.58` | Weekly Low=`99.51`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.35` (Distance: `+0.18%`)
  * Point of Control (POC) = `99.92` (Distance: `+1.62%`)
  * Value Area Low (VAL) = `98.96` (Distance: `+2.60%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.11` | POC=`100.90` | VAL=`100.63`
  * Prior Day Extremes: PDH=`103.63` | PDL=`100.15` | PDC=`102.27`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.48` | Weekly POC=`100.91` | Weekly VAL=`99.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.77` | Low=`98.95`
  * London Session (08:00-16:00 UTC): High=`100.61` | Low=`99.44`
  * New York Session (13:00-21:00 UTC): High=`102.93` | Low=`99.78`
  * Initial Balance (First Hour): IB High=`100.61` | IB Low=`99.91`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `101.14` - `101.95`
  * Optimal Trade Entry (OTE 0.705): `101.75`
  * Structural Invalidation Anchor (0.786): `102.36`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `101.71` | `101.75` | `101.53` | `101.54` | `49,088` | 4,990,178.12 USD | -1,924,619.06 USD | `-38.57%` | -55,735,056.58 USD | `-0.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `101.54` | `101.71` | `101.53` | `101.62` | `48,555` | 4,933,868.73 USD | 646,543.68 USD | `+13.10%` | -55,088,512.91 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `101.63` | `101.78` | `101.58` | `101.64` | `21,711` | 2,208,008.89 USD | -242,976.01 USD | `-11.00%` | -55,331,488.92 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `101.96` | `102.01` | `101.75` | `101.86` | `152,608` | 15,546,239.68 USD | -1,528,058.93 USD | `-9.83%` | -49,119,715.84 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `101.87` | `101.93` | `101.53` | `101.54` | `201,425` | 20,486,970.74 USD | -6,482,853.63 USD | `-31.64%` | -55,602,569.47 USD | `-1.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `101.54` | `101.78` | `101.53` | `101.64` | `70,117` | 7,126,731.26 USD | 403,041.12 USD | `+5.66%` | -55,199,528.35 USD | `+0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `101.75` | `102.70` | `101.69` | `102.66` | `1,128,658` | 115,436,116.22 USD | 3,102,728.09 USD | `+2.69%` | -39,299,496.40 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `102.66` | `103.16` | `101.75` | `101.86` | `1,100,013` | 112,591,915.90 USD | -12,028,545.03 USD | `-10.68%` | -51,328,041.42 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `101.87` | `101.93` | `101.53` | `101.64` | `271,618` | 27,621,412.37 USD | -6,086,721.95 USD | `-22.04%` | -57,414,763.37 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `101.53` | `101.64` | `1,371,556` | 140,205,617.89 USD | -18,108,357.54 USD | `-12.92%` | -61,977,000.75 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.37` | `102.50` | `99.16` | `99.64` | `3,450,297` | 345,810,531.49 USD | -35,022,306.76 USD | `-10.13%` | -43,673,756.58 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -38,017,362.01 USD | `+1.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `101.53` | `101.64` | `1,371,556` | 140,205,617.89 USD | -18,108,357.54 USD | `-12.92%` | -61,977,000.75 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`101.55`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `101.47` | `1951.9100` | 198,060.31 USD | 5,944,134.81 USD | `10 orders` | `-0.19%` | `-` |
| `BID` | `101.48` | `2079.7100` | 211,048.97 USD | 5,746,074.50 USD | `10 orders` | `-0.18%` | `-` |
| `BID` | `101.49` | `2360.7300` | 239,590.49 USD | 5,535,025.53 USD | `15 orders` | `-0.17%` | `-` |
| `BID` | `101.50` | `3107.2800` | 315,388.92 USD | 5,295,435.05 USD | `15 orders` | `-0.16%` | `-` |
| `BID` | `101.51` | `3960.6500` | 402,045.58 USD | 4,980,046.13 USD | `14 orders` | `-0.15%` | `-` |
| `BID` | `101.52` | `3438.5200` | 349,078.55 USD | 4,578,000.54 USD | `15 orders` | `-0.14%` | `-` |
| `BID` | `101.53` | `5416.4100` | 549,928.11 USD | 4,228,921.99 USD | `16 orders` | `-0.13%` | `-` |
| `BID` | `101.54` | `3360.0700` | 341,181.51 USD | 3,678,993.89 USD | `15 orders` | `-0.12%` | `-` |
| `BID` | `101.55` | `3259.5300` | 331,005.27 USD | 3,337,812.38 USD | `12 orders` | `-0.11%` | `-` |
| `BID` | `101.56` | `2413.1800` | 245,082.56 USD | 3,006,807.11 USD | `13 orders` | `-0.10%` | `-` |
| `BID` | `101.57` | `5148.2900` | 522,911.82 USD | 2,761,724.55 USD | `18 orders` | `-0.09%` | `-` |
| `BID` | `101.58` | `3440.4000` | 349,475.83 USD | 2,238,812.73 USD | `19 orders` | `-0.08%` | `-` |
| `BID` | `101.59` | `2021.8100` | 205,395.68 USD | 1,889,336.90 USD | `14 orders` | `-0.07%` | `-` |
| `BID` | `101.60` | `4780.1100` | 485,659.18 USD | 1,683,941.22 USD | `23 orders` | `-0.06%` | `-` |
| `BID` | `101.61` | `1679.7800` | 170,682.45 USD | 1,198,282.04 USD | `24 orders` | `-0.05%` | `-` |
| `BID` | `101.62` | `3533.9900` | 359,124.06 USD | 1,027,599.60 USD | `24 orders` | `-0.04%` | `-` |
| `BID` | `101.63` | `1905.9600` | 193,702.71 USD | 668,475.53 USD | `25 orders` | `-0.03%` | `-` |
| `BID` | `101.64` | `3641.3100` | 370,102.75 USD | 474,772.82 USD | `28 orders` | `-0.02%` | `-` |
| `BID` | `101.65` | `414.7200` | 42,156.29 USD | 104,670.07 USD | `10 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `101.66` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 101.66` | `0.00%` | `-` |
| `BID` | `101.66` | `614.9300` | 62,513.78 USD | 62,513.78 USD | `13 orders` | `-0.00%` | `-` |
| `ASK` | `101.67` | `310.6200` | 31,580.74 USD | 31,580.74 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `101.68` | `604.5700` | 61,472.68 USD | 93,053.41 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `101.69` | `1563.7900` | 159,021.81 USD | 252,075.22 USD | `22 orders` | `+0.02%` | `-` |
| `ASK` | `101.70` | `2650.8900` | 269,595.51 USD | 521,670.73 USD | `18 orders` | `+0.03%` | `-` |
| `ASK` | `101.71` | `1448.6900` | 147,346.26 USD | 669,016.99 USD | `29 orders` | `+0.04%` | `-` |
| `ASK` | `101.72` | `3579.7600` | 364,133.19 USD | 1,033,150.18 USD | `17 orders` | `+0.05%` | `-` |
| `ASK` | `101.73` | `2057.3100` | 209,290.15 USD | 1,242,440.32 USD | `22 orders` | `+0.06%` | `-` |
| `ASK` | `101.74` | `4807.9400` | 489,159.82 USD | 1,731,600.14 USD | `23 orders` | `+0.07%` | `-` |
| `ASK` | `101.75` | `2486.9600` | 253,048.18 USD | 1,984,648.32 USD | `20 orders` | `+0.08%` | `-` |
| `ASK` | `101.76` | `3593.4800` | 365,672.52 USD | 2,350,320.84 USD | `12 orders` | `+0.09%` | `-` |
| `ASK` | `101.77` | `2562.7300` | 260,809.03 USD | 2,611,129.88 USD | `19 orders` | `+0.10%` | `-` |
| `ASK` | `101.78` | `2502.9100` | 254,746.18 USD | 2,865,876.06 USD | `11 orders` | `+0.11%` | `-` |
| `ASK` | `101.79` | `4678.0200` | 476,175.66 USD | 3,342,051.71 USD | `12 orders` | `+0.12%` | `-` |
| `ASK` | `101.80` | `2672.6400` | 272,074.75 USD | 3,614,126.46 USD | `14 orders` | `+0.13%` | `-` |
| `ASK` | `101.81` | `5656.7400` | 575,912.70 USD | 4,190,039.16 USD | `21 orders` | `+0.14%` | `-` |
| `ASK` | `101.82` | `3788.3100` | 385,725.72 USD | 4,575,764.89 USD | `15 orders` | `+0.15%` | `-` |
| `ASK` | `101.83` | `2489.0700` | 253,462.00 USD | 4,829,226.89 USD | `9 orders` | `+0.16%` | `-` |
| `ASK` | `101.84` | `2292.8200` | 233,500.79 USD | 5,062,727.68 USD | `8 orders` | `+0.17%` | `-` |
| `ASK` | `101.85` | `1598.9400` | 162,852.04 USD | 5,225,579.71 USD | `9 orders` | `+0.18%` | `-` |
| `ASK` | `101.86` | `1888.4800` | 192,360.57 USD | 5,417,940.29 USD | `7 orders` | `+0.19%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 73,320,871.98 USD | `721,165.26` | `94.33` | `101.66` | `310.92` | -5,289,981.57 USD | `-7.21%` | `7X Cross` |
| `21` | `0x9c6a...a4ed` | `LONG` | 55,927,415.44 USD | `550,087.69` | `80.86` | `101.66` | `68.17` | 11,448,429.05 USD | `+20.47%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 26,363,033.03 USD | `259,300.02` | `91.42` | `101.66` | `591.81` | -2,657,900.01 USD | `-10.08%` | `5X Cross` |
| `81` | `0x3dc9...54b0` | `SHORT` | 22,367,419.32 USD | `220,000.19` | `105.90` | `101.66` | `163.65` | 931,687.96 USD | `+4.17%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 19,264,464.86 USD | `189,472.50` | `115.21` | `101.66` | `34.65` | -2,564,550.40 USD | `-13.31%` | `20X Cross` |
| `112` | `0x4a20...3c26` | `LONG` | 18,293,400.00 USD | `180,000.00` | `106.43` | `101.66` | `65.07` | -864,878.71 USD | `-4.73%` | `20X Cross` |
| `137` | `0xecb6...2b00` | `SHORT` | 15,011,130.19 USD | `147,645.62` | `102.75` | `101.66` | `314.08` | 159,718.74 USD | `+1.06%` | `20X Cross` |
| `225` | `0xc63a...a3cd` | `LONG` | 10,167,000.00 USD | `100,000.00` | `112.22` | `101.66` | `0.000000` | -1,055,108.97 USD | `-10.38%` | `20X Cross` |
| `236` | `0x7a5a...0394` | `SHORT` | 10,001,555.66 USD | `98,411.45` | `100.92` | `101.66` | `126.43` | -69,977.74 USD | `-0.70%` | `10X Cross` |
| `244` | `0x13da...08be` | `LONG` | 9,727,138.40 USD | `95,711.29` | `100.55` | `101.66` | `98.09` | 103,397.73 USD | `+1.06%` | `20X Isolated` |
| `268` | `0xb581...6f4f` | `LONG` | 9,150,678.00 USD | `90,000.00` | `114.59` | `101.66` | `0.000000` | -1,162,614.29 USD | `-12.71%` | `3X Cross` |
| `291` | `0x645b...87b8` | `SHORT` | 8,500,149.83 USD | `83,605.29` | `103.91` | `101.66` | `327.75` | 186,979.33 USD | `+2.20%` | `20X Cross` |
| `296` | `0xdb3a...cf3b` | `LONG` | 8,321,870.47 USD | `81,851.78` | `106.04` | `101.66` | `45.74` | -357,876.38 USD | `-4.30%` | `4X Cross` |
| `316` | `0xe927...98ef` | `LONG` | 7,928,700.00 USD | `78,000.00` | `96.34` | `101.66` | `38.44` | 414,558.52 USD | `+5.23%` | `3X Cross` |
| `325` | `0xca49...53c8` | `SHORT` | 7,517,830.56 USD | `73,943.45` | `110.70` | `101.66` | `270.27` | 667,791.70 USD | `+8.88%` | `20X Cross` |
| `328` | `0x8ae4...3d60` | `LONG` | 7,338,848.84 USD | `72,180.05` | `111.72` | `101.66` | `0.4113` | -725,311.40 USD | `-9.88%` | `10X Cross` |
| `332` | `0xa0b7...6165` | `SHORT` | 7,223,086.18 USD | `71,044.42` | `107.87` | `101.66` | `190.90` | 440,381.02 USD | `+6.10%` | `2X Cross` |
| `348` | `0xf517...c032` | `SHORT` | 6,891,043.15 USD | `67,778.53` | `84.64` | `101.66` | `232.00` | -1,154,011.98 USD | `-16.75%` | `20X Cross` |
| `486` | `0x7e23...5a5a` | `LONG` | 4,937,558.82 USD | `48,564.56` | `105.17` | `101.66` | `78.11` | -170,010.35 USD | `-3.44%` | `5X Isolated` |
| `582` | `0x2e2b...2fab` | `LONG` | 4,066,800.00 USD | `40,000.00` | `119.55` | `101.66` | `52.64` | -715,235.64 USD | `-17.59%` | `10X Cross` |
| `597` | `0x7fda...17d1` | `SHORT` | 3,985,374.53 USD | `39,199.12` | `103.80` | `101.66` | `1086.98` | 83,530.91 USD | `+2.10%` | `20X Cross` |
| `608` | `0xf899...88db` | `SHORT` | 3,923,228.13 USD | `38,586.27` | `87.86` | `101.66` | `116.84` | -532,852.94 USD | `-13.58%` | `20X Cross` |
| `623` | `0x9946...0852` | `SHORT` | 3,841,580.62 USD | `37,784.80` | `112.11` | `101.66` | `127.50` | 394,646.70 USD | `+10.27%` | `20X Cross` |
| `644` | `0x27b8...12fc` | `LONG` | 3,668,987.73 USD | `36,085.73` | `110.86` | `101.66` | `13.07` | -331,357.52 USD | `-9.03%` | `10X Cross` |
| `651` | `0x9c16...4a6f` | `SHORT` | 3,637,666.18 USD | `35,779.15` | `90.45` | `101.66` | `128.61` | -401,561.15 USD | `-11.04%` | `20X Cross` |
| `656` | `0x3440...32c5` | `SHORT` | 3,612,245.63 USD | `35,529.12` | `95.02` | `101.66` | `166.10` | -236,224.20 USD | `-6.54%` | `20X Cross` |
| `726` | `0x96a7...79df` | `LONG` | 3,252,800.00 USD | `32,000.00` | `74.39` | `101.66` | `0.000000` | 872,394.15 USD | `+26.82%` | `20X Cross` |
| `748` | `0x023a...2355` | `SHORT` | 3,164,500.10 USD | `31,125.21` | `101.48` | `101.66` | `380.59` | -5,804.23 USD | `-0.18%` | `20X Cross` |
| `767` | `0xbe19...8bd1` | `SHORT` | 3,094,805.25 USD | `30,451.69` | `97.62` | `101.66` | `729.29` | -122,258.62 USD | `-3.95%` | `3X Cross` |
| `774` | `0x482b...cae4` | `SHORT` | 3,080,455.10 USD | `30,310.49` | `88.03` | `101.66` | `159.08` | -412,206.81 USD | `-13.38%` | `20X Cross` |
| `791` | `0x610b...b613` | `LONG` | 3,012,132.53 USD | `29,634.14` | `101.23` | `101.66` | `70.38` | 12,133.18 USD | `+0.40%` | `3X Isolated` |
| `803` | `0x45d2...4029` | `SHORT` | 2,969,628.60 USD | `29,220.00` | `93.28` | `101.66` | `1317.66` | -243,852.62 USD | `-8.21%` | `20X Cross` |
| `815` | `0xa61c...66b9` | `LONG` | 2,937,042.96 USD | `28,888.00` | `104.39` | `101.66` | `0.000000` | -78,521.16 USD | `-2.67%` | `5X Cross` |
| `854` | `0x458d...ab3b` | `LONG` | 2,783,688.30 USD | `27,385.03` | `117.17` | `101.66` | `81.06` | -424,974.22 USD | `-15.27%` | `3X Isolated` |
| `913` | `0x051c...693c` | `LONG` | 2,555,450.50 USD | `25,139.70` | `89.76` | `101.66` | `21.27` | 298,889.18 USD | `+11.70%` | `20X Cross` |
| `916` | `0xfc27...9d9d` | `SHORT` | 2,550,258.50 USD | `25,093.56` | `102.81` | `101.66` | `654.33` | 29,669.30 USD | `+1.16%` | `20X Cross` |
| `928` | `0xfc66...ca06` | `SHORT` | 2,517,155.01 USD | `24,758.09` | `102.43` | `101.66` | `1497.20` | 18,845.29 USD | `+0.75%` | `20X Cross` |
| `944` | `0x638f...f5f0` | `LONG` | 2,439,972.00 USD | `24,000.00` | `136.71` | `101.66` | `41.43` | -840,996.54 USD | `-34.47%` | `20X Cross` |
| `1009` | `0x7178...0854` | `LONG` | 2,292,269.24 USD | `22,545.24` | `110.94` | `101.66` | `29.68` | -208,875.23 USD | `-9.11%` | `10X Cross` |
| `1029` | `0x739c...cfb2` | `LONG` | 2,236,740.00 USD | `22,000.00` | `91.95` | `101.66` | `72.43` | 213,832.69 USD | `+9.56%` | `20X Cross` |
| `1038` | `0x69cc...14fd` | `SHORT` | 2,206,398.62 USD | `21,701.57` | `99.01` | `101.66` | `454.40` | -57,745.87 USD | `-2.62%` | `20X Cross` |
| `1053` | `0xb90d...870c` | `SHORT` | 2,147,280.57 USD | `21,120.10` | `102.00` | `101.66` | `111.54` | 7,044.21 USD | `+0.33%` | `20X Cross` |
| `1101` | `0x7737...bf66` | `SHORT` | 2,072,532.99 USD | `20,384.06` | `102.94` | `101.66` | `1012.17` | 25,808.90 USD | `+1.25%` | `10X Cross` |
| `1111` | `0xea00...a918` | `LONG` | 2,035,186.30 USD | `20,022.69` | `66.09` | `101.66` | `0.000000` | 711,877.70 USD | `+34.98%` | `20X Cross` |
| `1112` | `0xbfc7...80b4` | `SHORT` | 2,033,484.00 USD | `20,000.00` | `85.98` | `101.66` | `312.51` | -313,949.50 USD | `-15.44%` | `20X Cross` |
| `1113` | `0x5986...89d9` | `LONG` | 2,033,484.00 USD | `20,000.00` | `101.84` | `101.66` | `43.63` | -3,313.53 USD | `-0.16%` | `20X Cross` |
| `1114` | `0x3fc5...c0c1` | `SHORT` | 2,033,400.00 USD | `20,000.00` | `98.28` | `101.66` | `198.28` | -67,840.16 USD | `-3.34%` | `20X Cross` |
| `1115` | `0xdf60...d3c7` | `LONG` | 2,033,400.00 USD | `20,000.00` | `120.12` | `101.66` | `93.99` | -369,008.53 USD | `-18.15%` | `7X Isolated` |
| `1116` | `0x251f...6e5d` | `LONG` | 2,033,400.00 USD | `20,000.00` | `101.15` | `101.66` | `42.62` | 10,302.23 USD | `+0.51%` | `20X Cross` |
| `1139` | `0xb322...d51f` | `LONG` | 2,010,505.95 USD | `19,774.82` | `102.98` | `101.66` | `55.79` | -25,965.45 USD | `-1.29%` | `20X Cross` |
| `1142` | `0x34e6...8d74` | `LONG` | 2,001,686.08 USD | `19,688.07` | `101.19` | `101.66` | `53.20` | 9,522.28 USD | `+0.48%` | `20X Cross` |
| `1169` | `0x936c...bb0f` | `SHORT` | 1,976,243.16 USD | `19,437.82` | `105.65` | `101.66` | `629.57` | 77,271.22 USD | `+3.91%` | `20X Cross` |
| `1171` | `0x7160...d47c` | `LONG` | 1,975,864.95 USD | `19,434.10` | `105.03` | `101.66` | `79.87` | -65,356.34 USD | `-3.31%` | `20X Cross` |
| `1193` | `0xe097...d0fe` | `LONG` | 1,931,297.90 USD | `18,995.75` | `109.71` | `101.66` | `0.000000` | -152,698.99 USD | `-7.91%` | `20X Cross` |
| `1287` | `0xe98b...8cd5` | `SHORT` | 1,791,366.77 USD | `17,622.89` | `187.95` | `101.66` | `259.80` | 1,520,853.95 USD | `+84.90%` | `20X Cross` |
| `1299` | `0xdf95...7d72` | `SHORT` | 1,773,470.48 USD | `17,443.40` | `104.70` | `101.66` | `2168.27` | 52,793.18 USD | `+2.98%` | `20X Cross` |
| `1326` | `0xee2b...d67e` | `LONG` | 1,724,647.53 USD | `16,963.19` | `119.86` | `101.66` | `18.66` | -308,624.11 USD | `-17.89%` | `4X Cross` |
| `1329` | `0x123d...3bff` | `LONG` | 1,720,096.78 USD | `16,918.43` | `89.53` | `101.66` | `0.000000` | 205,310.29 USD | `+11.94%` | `10X Cross` |
| `1360` | `0x7277...0b98` | `SHORT` | 1,688,038.19 USD | `16,603.11` | `101.18` | `101.66` | `176.90` | -8,109.99 USD | `-0.48%` | `20X Cross` |
| `1445` | `0x73d7...8be1` | `LONG` | 1,593,062.15 USD | `15,668.95` | `106.60` | `101.66` | `68.98` | -77,278.82 USD | `-4.85%` | `20X Cross` |
| `1458` | `0xc74a...ab93` | `LONG` | 1,579,693.74 USD | `15,536.82` | `64.06` | `101.66` | `54.87` | 584,464.91 USD | `+37.00%` | `5X Isolated` |
| `1504` | `0xc7d1...51af` | `SHORT` | 1,524,750.00 USD | `15,000.00` | `105.79` | `101.66` | `138.76` | 62,125.00 USD | `+4.07%` | `20X Cross` |
| `1541` | `0xffb2...5ed6` | `LONG` | 1,474,687.68 USD | `14,504.05` | `117.89` | `101.66` | `90.27` | -235,217.03 USD | `-15.95%` | `20X Cross` |
| `1572` | `0x0d6a...ca57` | `LONG` | 1,444,390.11 USD | `14,206.65` | `110.41` | `101.66` | `91.59` | -124,200.25 USD | `-8.60%` | `5X Isolated` |
| `1852` | `0x1306...0d3d` | `SHORT` | 1,160,652.52 USD | `11,415.88` | `102.00` | `101.66` | `109.35` | 3,767.24 USD | `+0.32%` | `10X Isolated` |
| `1860` | `0x2482...0e55` | `LONG` | 1,155,375.85 USD | `11,363.98` | `122.03` | `101.66` | `94.24` | -231,326.08 USD | `-20.02%` | `20X Isolated` |
| `1879` | `0xe105...6a47` | `LONG` | 1,139,217.43 USD | `11,205.05` | `107.11` | `101.66` | `91.93` | -60,939.62 USD | `-5.35%` | `20X Cross` |
| `1891` | `0x45db...86eb` | `LONG` | 1,128,537.00 USD | `11,100.00` | `110.69` | `101.66` | `67.96` | -100,144.90 USD | `-8.87%` | `5X Cross` |
| `1921` | `0x1d04...7c43` | `LONG` | 1,099,231.64 USD | `10,811.76` | `111.55` | `101.66` | `16.94` | -106,829.85 USD | `-9.72%` | `6X Cross` |
| `2027` | `0x0daf...47e0` | `SHORT` | 1,016,742.00 USD | `10,000.00` | `99.07` | `101.66` | `246.88` | -26,029.78 USD | `-2.56%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `101.25` | 30,442.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 30.44K USD at 101.2500 USD [API] | `2026-10-27 19:45:02` |
| `ANNOUNCEMENT` | `INFO` | `101.15` | 37,585.32 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 37.59K USD at 101.1500 USD [API] | `2026-10-27 19:50:26` |
| `ANNOUNCEMENT` | `INFO` | `101.00` | 69,989.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 69.99K USD at 101.0000 USD [API] | `2026-10-27 20:49:26` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 2,004.24 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 29.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.03K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 288.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.29K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 12.83 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 720.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.72K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 170.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.17K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.95` | 4,794.57 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.79K USD at 106.9500 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.90` | 4,051.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.05K USD at 106.9000 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.90` | 196.70 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 106.9000 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.90` | 423.32 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.42K USD at 106.9000 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.90` | 102.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 106.9000 USD [API] | `2026-10-20 14:07:32` |
| `ANNOUNCEMENT` | `INFO` | `106.90` | 35.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.04K USD at 106.9000 USD [API] | `2026-10-20 14:07:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.65` (Vol: 2,900,000.00 USD, Dist: `+1.98%`) | Long MP=`98.78` (Vol: 4,200,000.00 USD, Dist: `--2.81%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+2.41%`) | Long MP=`98.78` (Vol: 4,300,000.00 USD, Dist: `--2.81%`)
  * 3D Horizon: Short MP=`104.03` (Vol: 4,200,000.00 USD, Dist: `+2.36%`) | Long MP=`99.07` (Vol: 5,900,000.00 USD, Dist: `--2.52%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+2.38%`) | Long MP=`98.63` (Vol: 8,800,000.00 USD, Dist: `--2.95%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `20.50` | 574,410.00 USD | 139,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.50` | 36,490.00 USD | 138,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.50` | 143,270.00 USD | 138,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.50` | 3,710.00 USD | 138,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.50` | 41,710.00 USD | 138,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 34,220.00 USD | 138,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 43,360.00 USD | 138,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 271,040.00 USD | 138,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 39,110.00 USD | 138,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 722,340.00 USD | 138,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 97,320.00 USD | 137,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 79,730.00 USD | 137,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 53,210.00 USD | 137,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 16,730.00 USD | 137,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 6,550,000.00 USD | 137,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 45,060.00 USD | 130,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 28,270.00 USD | 130,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 224,580.00 USD | 130,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,030,000.00 USD | 130,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 230,210.00 USD | 127,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 1,820,000.00 USD | 127,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 97,100.00 USD | 125,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 102,760.00 USD | 125,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 904,870.00 USD | 125,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 68,340.00 USD | 124,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 3,920,000.00 USD | 124,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 11,460.00 USD | 120,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 65,050.00 USD | 120,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 165,150.00 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 79,620.00 USD | 120,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 100,530.00 USD | 120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 858,200.00 USD | 119,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 2,190,000.00 USD | 119,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 1,600,000.00 USD | 116,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 1,120,000.00 USD | 115,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,250,000.00 USD | 114,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 100,740.00 USD | 112,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 144,990.00 USD | 112,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 165,810.00 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 140,800.00 USD | 112,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 269,530.00 USD | 112,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 229,050.00 USD | 112,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 248,340.00 USD | 111,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 237,900.00 USD | 111,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 11,690,000.00 USD | 111,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 178,730.00 USD | 99,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 87,780.00 USD | 99,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 1,100,000.00 USD | 99,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 39,000,000.00 USD | 98,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 297,770.00 USD | 59,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 2,720,000.00 USD | 58,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,810,000.00 USD | 56,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 375,150.00 USD | 54,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 869,180.00 USD | 54,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 390,130.00 USD | 53,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 956,730.00 USD | 52,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 901,590.00 USD | 51,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 832,690.00 USD | 50,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,700,000.00 USD | 50,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 1,880,000.00 USD | 45,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 425,250.00 USD | 43,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 2,560,000.00 USD | 43,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,410,000.00 USD | 40,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 908,370.00 USD | 39,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 574,650.00 USD | 38,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 1,020,000.00 USD | 37,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 778,120.00 USD | 36,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,580,000.00 USD | 35,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 4,050,000.00 USD | 34,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 328,110.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.60` | 410,320,000.00 USD | 410,320,000.00 USD | 700,630.00 USD | 281,700.00 USD | 577,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 408,760,000.00 USD | 408,760,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 407,780,000.00 USD | 407,780,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 406,060,000.00 USD | 406,060,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 404,060,000.00 USD | 404,060,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.50` | 1,800,000.00 USD | 29,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.60` | 402,660,000.00 USD | 402,660,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 399,540,000.00 USD | 399,540,000.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 396,580,000.00 USD | 396,580,000.00 USD | 1,170,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 394,540,000.00 USD | 394,540,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.40` | 238,630,000.00 USD | 238,630,000.00 USD | 249,290.00 USD | 231,510.00 USD | 316,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 392,210,000.00 USD | 392,210,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.50` | 4,240,000.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 237,840,000.00 USD | 237,840,000.00 USD | 56,690.00 USD | 192,290.00 USD | 73,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 388,890,000.00 USD | 388,890,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.80` | 237,510,000.00 USD | 237,510,000.00 USD | 369,020.00 USD | 218,430.00 USD | 123,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 387,260,000.00 USD | 387,260,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.00` | 236,800,000.00 USD | 236,800,000.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 385,060,000.00 USD | 385,060,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.20` | 236,340,000.00 USD | 236,340,000.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 383,320,000.00 USD | 383,320,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.40` | 235,890,000.00 USD | 235,890,000.00 USD | 151,210.00 USD | 110,310.00 USD | 782,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 382,460,000.00 USD | 382,460,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.50` | 1,190,000.00 USD | 23,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 234,850,000.00 USD | 234,850,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 380,550,000.00 USD | 380,550,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.80` | 234,590,000.00 USD | 234,590,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 379,470,000.00 USD | 379,470,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.00` | 234,440,000.00 USD | 234,440,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 379,250,000.00 USD | 379,250,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.20` | 234,270,000.00 USD | 234,270,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 378,850,000.00 USD | 378,850,000.00 USD | 125,700.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.40` | 234,060,000.00 USD | 234,060,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 378,670,000.00 USD | 378,670,000.00 USD | 80,500.00 USD | 115,240.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.50` | 3,140,000.00 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 378,480,000.00 USD | 378,480,000.00 USD | 238,200.00 USD | 343,740.00 USD | 114,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 377,780,000.00 USD | 377,780,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 377,100,000.00 USD | 377,100,000.00 USD | 78,790.00 USD | 153,680.00 USD | 134,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 376,740,000.00 USD | 376,740,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 376,080,000.00 USD | 376,080,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,910,000.00 USD | 19,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 375,780,000.00 USD | 375,780,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 375,700,000.00 USD | 375,700,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 375,680,000.00 USD | 375,680,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.20` | 234,010,000.00 USD | 234,010,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 374,720,000.00 USD | 374,720,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.40` | 233,990,000.00 USD | 233,990,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 374,330,000.00 USD | 374,330,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.50` | 1,800,000.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 233,480,000.00 USD | 233,480,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 372,810,000.00 USD | 372,810,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.80` | 230,910,000.00 USD | 230,910,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 368,760,000.00 USD | 368,760,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.00` | 227,090,000.00 USD | 227,090,000.00 USD | 1,200,000.00 USD | 1,170,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 364,520,000.00 USD | 364,520,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.20` | 223,490,000.00 USD | 223,490,000.00 USD | 1,060,000.00 USD | 1,190,000.00 USD | 693,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 358,090,000.00 USD | 358,090,000.00 USD | 2,940,000.00 USD | 1,970,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.40` | 220,550,000.00 USD | 220,550,000.00 USD | 862,370.00 USD | 983,090.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 351,190,000.00 USD | 351,190,000.00 USD | 2,950,000.00 USD | 643,110.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.50` | 1,410,000.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.60` | 217,600,000.00 USD | 217,600,000.00 USD | 994,840.00 USD | 756,910.00 USD | 933,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 345,220,000.00 USD | 345,220,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.80` | 214,920,000.00 USD | 214,920,000.00 USD | 233,930.00 USD | 700,140.00 USD | 729,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 337,120,000.00 USD | 337,120,000.00 USD | 2,970,000.00 USD | 2,770,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.00` | 213,250,000.00 USD | 213,250,000.00 USD | 102,790.00 USD | 1,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.00` | 328,430,000.00 USD | 328,430,000.00 USD | 5,250,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.20` | 213,150,000.00 USD | 213,150,000.00 USD | 276,590.00 USD | 29,470.00 USD | 332,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.20` | 318,600,000.00 USD | 318,600,000.00 USD | 5,470,000.00 USD | 4,350,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.40` | 212,510,000.00 USD | 212,510,000.00 USD | 1,110,000.00 USD | 998,800.00 USD | 567,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.40` | 305,070,000.00 USD | 305,070,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.50` | 1,830,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.60` | 209,830,000.00 USD | 209,830,000.00 USD | 2,410,000.00 USD | 1,900,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.60` | 294,660,000.00 USD | 294,660,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.80` | 203,130,000.00 USD | 203,130,000.00 USD | 3,880,000.00 USD | 3,190,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.80` | 279,310,000.00 USD | 279,310,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.00` | 193,890,000.00 USD | 193,890,000.00 USD | 3,680,000.00 USD | 3,010,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.00` | 265,850,000.00 USD | 265,850,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.20` | 184,010,000.00 USD | 184,010,000.00 USD | 3,040,000.00 USD | 2,880,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.20` | 241,170,000.00 USD | 241,170,000.00 USD | 7,790,000.00 USD | 6,660,000.00 USD | 5,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.40` | 176,060,000.00 USD | 176,060,000.00 USD | 3,740,000.00 USD | 3,150,000.00 USD | 3,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.40` | 221,050,000.00 USD | 221,050,000.00 USD | 9,460,000.00 USD | 2,950,000.00 USD | 9,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.50` | 11,050,000.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.60` | 165,710,000.00 USD | 165,710,000.00 USD | 6,200,000.00 USD | 4,440,000.00 USD | 6,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.60` | 199,010,000.00 USD | 199,010,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.80` | 148,320,000.00 USD | 148,320,000.00 USD | 7,150,000.00 USD | 6,900,000.00 USD | 5,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.80` | 163,520,000.00 USD | 163,520,000.00 USD | 12,530,000.00 USD | 9,880,000.00 USD | 13,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.00` | 129,210,000.00 USD | 129,210,000.00 USD | 4,640,000.00 USD | 4,540,000.00 USD | 5,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.00` | 128,040,000.00 USD | 128,040,000.00 USD | 13,760,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.20` | 114,900,000.00 USD | 114,900,000.00 USD | 4,370,000.00 USD | 4,670,000.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.20` | 86,890,000.00 USD | 86,890,000.00 USD | 12,550,000.00 USD | 6,970,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.40` | 102,260,000.00 USD | 102,260,000.00 USD | 3,410,000.00 USD | 4,060,000.00 USD | 4,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.40` | 61,980,000.00 USD | 61,980,000.00 USD | 2,300,000.00 USD | 599,290.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.50` | 448,020.00 USD | 554,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `99.60` | 89,920,000.00 USD | 89,920,000.00 USD | 3,230,000.00 USD | 2,990,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.60` | 52,390,000.00 USD | 52,390,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.80` | 80,730,000.00 USD | 80,730,000.00 USD | 1,280,000.00 USD | 2,380,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.80` | 47,920,000.00 USD | 47,920,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.00` | 73,920,000.00 USD | 73,920,000.00 USD | 1,360,000.00 USD | 790,810.00 USD | 453,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.00` | 45,160,000.00 USD | 45,160,000.00 USD | 533,430.00 USD | 36,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.20` | 71,310,000.00 USD | 71,310,000.00 USD | 34,220.00 USD | 341,570.00 USD | 431,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.40` | 70,510,000.00 USD | 70,510,000.00 USD | 718,910.00 USD | 877,160.00 USD | 438,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.40` | 44,590,000.00 USD | 44,590,000.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `100.50` | 106,160.00 USD | 106,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `100.60` | 68,470,000.00 USD | 68,470,000.00 USD | 1,010,000.00 USD | 251,930.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.60` | 43,270,000.00 USD | 43,270,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.80` | 64,420,000.00 USD | 64,420,000.00 USD | 760,660.00 USD | 1,670,000.00 USD | 641,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.80` | 41,500,000.00 USD | 41,500,000.00 USD | 3,660,000.00 USD | 981,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `101.00` | 61,350,000.00 USD | 61,350,000.00 USD | 8,970,000.00 USD | 5,980,000.00 USD | 7,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `101.00` | 36,850,000.00 USD | 36,850,000.00 USD | 2,860,000.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `101.20` | 39,030,000.00 USD | 39,030,000.00 USD | 5,110,000.00 USD | 7,010,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `101.20` | 24,410,000.00 USD | 24,410,000.00 USD | 4,750,000.00 USD | 3,220,000.00 USD | 5,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `101.40` | 21,790,000.00 USD | 21,790,000.00 USD | 692,280.00 USD | 609,630.00 USD | 1,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `101.40` | 10,510,000.00 USD | 10,510,000.00 USD | 3,020,000.00 USD | 0.00 USD | 7,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `101.60` | 20,480,000.00 USD | 20,480,000.00 USD | 5,150,000.00 USD | 2,220,000.00 USD | 13,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 9,850,000.00 USD | 9,850,000.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 19,700,000.00 USD | 19,700,000.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.80` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 29,040,000.00 USD | 29,040,000.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 6,930,000.00 USD | 6,930,000.00 USD | 354,260.00 USD | 0.00 USD | 364,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 30,870,000.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 9,660,000.00 USD | 9,660,000.00 USD | 799,010.00 USD | 1,160,000.00 USD | 764,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 33,110,000.00 USD | 33,110,000.00 USD | 369,280.00 USD | 578,040.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.40` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 36,130,000.00 USD | 36,130,000.00 USD | 1,150,000.00 USD | 299,640.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.60` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 26,340.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 38,550,000.00 USD | 38,550,000.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.80` | 14,710,000.00 USD | 14,710,000.00 USD | 1,220,000.00 USD | 1,650,000.00 USD | 563,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 46,350,000.00 USD | 46,350,000.00 USD | 7,520,000.00 USD | 0.00 USD | 271,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.00` | 18,100,000.00 USD | 18,100,000.00 USD | 2,190,000.00 USD | 1,200,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 60,350,000.00 USD | 60,350,000.00 USD | 11,170,000.00 USD | 0.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.20` | 23,730,000.00 USD | 23,730,000.00 USD | 1,660,000.00 USD | 2,430,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 74,070,000.00 USD | 74,070,000.00 USD | 13,600,000.00 USD | 4,380.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.40` | 31,060,000.00 USD | 31,060,000.00 USD | 4,020,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 89,080,000.00 USD | 89,080,000.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.50` | 70,910.00 USD | 70,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 45,540,000.00 USD | 45,540,000.00 USD | 4,330,000.00 USD | 2,100,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 107,470,000.00 USD | 107,470,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.80` | 54,990,000.00 USD | 54,990,000.00 USD | 3,390,000.00 USD | 2,620,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 119,810,000.00 USD | 119,810,000.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.00` | 67,360,000.00 USD | 67,360,000.00 USD | 4,020,000.00 USD | 3,820,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 148,230,000.00 USD | 148,230,000.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.20` | 76,390,000.00 USD | 76,390,000.00 USD | 3,440,000.00 USD | 2,450,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 168,320,000.00 USD | 168,320,000.00 USD | 7,510,000.00 USD | 6,900,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.40` | 84,550,000.00 USD | 84,550,000.00 USD | 3,160,000.00 USD | 1,660,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 184,450,000.00 USD | 184,450,000.00 USD | 4,800,000.00 USD | 3,700,000.00 USD | 7,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.50` | 1,440,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 92,860,000.00 USD | 92,860,000.00 USD | 2,260,000.00 USD | 2,030,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 202,020,000.00 USD | 202,020,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.80` | 99,040,000.00 USD | 99,040,000.00 USD | 1,540,000.00 USD | 1,580,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 219,110,000.00 USD | 219,110,000.00 USD | 5,130,000.00 USD | 4,150,000.00 USD | 7,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.00` | 101,110,000.00 USD | 101,110,000.00 USD | 501,070.00 USD | 641,540.00 USD | 928,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 235,970,000.00 USD | 235,970,000.00 USD | 5,470,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.20` | 102,290,000.00 USD | 102,290,000.00 USD | 422,890.00 USD | 21,950.00 USD | 732,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 248,400,000.00 USD | 248,400,000.00 USD | 5,320,000.00 USD | 4,850,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.40` | 103,430,000.00 USD | 103,430,000.00 USD | 331,150.00 USD | 7,520.00 USD | 804,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 261,050,000.00 USD | 261,050,000.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.50` | 193,620.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 106,050,000.00 USD | 106,050,000.00 USD | 561,460.00 USD | 995,420.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 279,090,000.00 USD | 279,090,000.00 USD | 6,220,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 108,250,000.00 USD | 108,250,000.00 USD | 693,450.00 USD | 746,040.00 USD | 756,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 290,420,000.00 USD | 290,420,000.00 USD | 3,560,000.00 USD | 3,410,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.00` | 109,840,000.00 USD | 109,840,000.00 USD | 460,610.00 USD | 552,510.00 USD | 576,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 302,020,000.00 USD | 302,020,000.00 USD | 4,740,000.00 USD | 3,150,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.20` | 112,530,000.00 USD | 112,530,000.00 USD | 1,280,000.00 USD | 675,100.00 USD | 740,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 316,520,000.00 USD | 316,520,000.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.40` | 114,590,000.00 USD | 114,590,000.00 USD | 918,780.00 USD | 500,580.00 USD | 640,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 325,030,000.00 USD | 325,030,000.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.50` | 27,960.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 117,350,000.00 USD | 117,350,000.00 USD | 957,870.00 USD | 536,470.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 334,240,000.00 USD | 334,240,000.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 119,350,000.00 USD | 119,350,000.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 340,120,000.00 USD | 340,120,000.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.00` | 120,330,000.00 USD | 120,330,000.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 345,680,000.00 USD | 345,680,000.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.20` | 120,710,000.00 USD | 120,710,000.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 347,400,000.00 USD | 347,400,000.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.40` | 121,190,000.00 USD | 121,190,000.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 348,390,000.00 USD | 348,390,000.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.50` | 367,260.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 121,680,000.00 USD | 121,680,000.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.60` | 349,040,000.00 USD | 349,040,000.00 USD | 498,090.00 USD | 0.00 USD | 154,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.80` | 121,990,000.00 USD | 121,990,000.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 350,100,000.00 USD | 350,100,000.00 USD | 499,750.00 USD | 203,950.00 USD | 357,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.00` | 350,730,000.00 USD | 350,730,000.00 USD | 293,270.00 USD | 252,740.00 USD | 82,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.20` | 353,140,000.00 USD | 353,140,000.00 USD | 966,370.00 USD | 938,650.00 USD | 503,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.40` | 355,630,000.00 USD | 355,630,000.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.50` | 105,510.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 357,050,000.00 USD | 357,050,000.00 USD | 401,600.00 USD | 515,740.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.80` | 359,730,000.00 USD | 359,730,000.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.00` | 121,990,000.00 USD | 121,990,000.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.00` | 360,270,000.00 USD | 360,270,000.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.20` | 122,010,000.00 USD | 122,010,000.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.20` | 361,490,000.00 USD | 361,490,000.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.40` | 122,130,000.00 USD | 122,130,000.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.40` | 361,820,000.00 USD | 361,820,000.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.50` | 1,850,000.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.60` | 122,790,000.00 USD | 122,790,000.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.60` | 362,890,000.00 USD | 362,890,000.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.80` | 123,820,000.00 USD | 123,820,000.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.80` | 363,870,000.00 USD | 363,870,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.00` | 124,890,000.00 USD | 124,890,000.00 USD | 213,690.00 USD | 401,420.00 USD | 453,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.00` | 365,590,000.00 USD | 365,590,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.20` | 125,760,000.00 USD | 125,760,000.00 USD | 228,950.00 USD | 389,380.00 USD | 250,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.20` | 367,590,000.00 USD | 367,590,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.40` | 126,640,000.00 USD | 126,640,000.00 USD | 277,830.00 USD | 269,600.00 USD | 337,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.40` | 368,990,000.00 USD | 368,990,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.50` | 195,170.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.60` | 127,060,000.00 USD | 127,060,000.00 USD | 110,850.00 USD | 71,980.00 USD | 239,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.60` | 370,090,000.00 USD | 370,090,000.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.80` | 127,740,000.00 USD | 127,740,000.00 USD | 155,280.00 USD | 287,250.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.80` | 372,110,000.00 USD | 372,110,000.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.00` | 127,880,000.00 USD | 127,880,000.00 USD | 34,430.00 USD | 101,090.00 USD | 319.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.00` | 375,070,000.00 USD | 375,070,000.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.20` | 128,010,000.00 USD | 128,010,000.00 USD | 58,160.00 USD | 523.35 USD | 75,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.20` | 377,110,000.00 USD | 377,110,000.00 USD | 1,170,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.40` | 128,050,000.00 USD | 128,050,000.00 USD | 37,090.00 USD | 2,670.00 USD | 685.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.40` | 379,440,000.00 USD | 379,440,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.50` | 2,450,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.60` | 128,410,000.00 USD | 128,410,000.00 USD | 23,090.00 USD | 147,570.00 USD | 184,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.60` | 380,400,000.00 USD | 380,400,000.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.80` | 128,810,000.00 USD | 128,810,000.00 USD | 189,110.00 USD | 81,270.00 USD | 131,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.80` | 382,760,000.00 USD | 382,760,000.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.00` | 129,130,000.00 USD | 129,130,000.00 USD | 56,690.00 USD | 192,290.00 USD | 73,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.00` | 384,390,000.00 USD | 384,390,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.20` | 129,840,000.00 USD | 129,840,000.00 USD | 369,020.00 USD | 218,430.00 USD | 123,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.20` | 386,590,000.00 USD | 386,590,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.40` | 130,310,000.00 USD | 130,310,000.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.40` | 388,330,000.00 USD | 388,330,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.50` | 223,220.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `112.60` | 130,760,000.00 USD | 130,760,000.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.60` | 389,190,000.00 USD | 389,190,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.80` | 131,200,000.00 USD | 131,200,000.00 USD | 16,000.00 USD | 63,410.00 USD | 364,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.80` | 390,060,000.00 USD | 390,060,000.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.00` | 131,800,000.00 USD | 131,800,000.00 USD | 135,210.00 USD | 46,900.00 USD | 418,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.00` | 391,100,000.00 USD | 391,100,000.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.20` | 132,060,000.00 USD | 132,060,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.20` | 392,180,000.00 USD | 392,180,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.40` | 132,210,000.00 USD | 132,210,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.40` | 392,410,000.00 USD | 392,410,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.50` | 54,920.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `113.60` | 132,380,000.00 USD | 132,380,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.60` | 392,800,000.00 USD | 392,800,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.80` | 392,800,000.00 USD | 392,800,000.00 USD | 6,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.50` | 62,390.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.50` | 949,020.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.50` | 4,700,000.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.50` | 528,600.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 775,130.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.50` | 326,570.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 57,070.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 35,300.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 103,390.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 8,290.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 200,050.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 8,220.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 12,540,000.00 USD | 27,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 773,060.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 5,700,000.00 USD | 33,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 4,750,000.00 USD | 38,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 1,030,000.00 USD | 39,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 8,270.00 USD | 39,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 215,650.00 USD | 39,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 179,930.00 USD | 39,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 31,190.00 USD | 39,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 587,250.00 USD | 40,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 1,500.00 USD | 40,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 4,660.00 USD | 40,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,320,000.00 USD | 42,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 1,280,000.00 USD | 44,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 14,460.00 USD | 44,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 250,580.00 USD | 44,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 294,930.00 USD | 44,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 112,820.00 USD | 44,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 893,550.00 USD | 45,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 19,490.00 USD | 45,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 705,840.00 USD | 46,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 1,560,000.00 USD | 48,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 888,260.00 USD | 48,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 393,400.00 USD | 49,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 7,100.00 USD | 49,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 18,210.00 USD | 49,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 1,110,000.00 USD | 50,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.50` | 218,290.00 USD | 50,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 56,280.00 USD | 50,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 129,290.00 USD | 50,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 1,470,000.00 USD | 52,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 520,640.00 USD | 52,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 4,830,000.00 USD | 57,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.50` | 152,670.00 USD | 57,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 699,590.00 USD | 58,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 409,130.00 USD | 58,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 35,750,000.00 USD | 94,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 3,770.00 USD | 94,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 1,160,000.00 USD | 95,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 6,060,000.00 USD | 101,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 223,180.00 USD | 102,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 676,710.00 USD | 102,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 462,890.00 USD | 103,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 48,800.00 USD | 103,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 10,230.00 USD | 103,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 54,460.00 USD | 103,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 32,470.00 USD | 103,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 562,210.00 USD | 103,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 900.32 USD | 103,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 49,780.00 USD | 103,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 3,030,000.00 USD | 107,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 1,620.00 USD | 107,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 7,910.00 USD | 107,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 24,640.00 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 589.88 USD | 107,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 200,610.00 USD | 107,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 395,000.00 USD | 107,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 232,980.00 USD | 107,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 22,820.00 USD | 107,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 911,800.00 USD | 108,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 468,500.00 USD | 109,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 40,280.00 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 348,830.00 USD | 109,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 13,820,000.00 USD | 123,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 515.14 USD | 123,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 106,850.00 USD | 123,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 133,820.00 USD | 123,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 57,550.00 USD | 123,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 150,780.00 USD | 123,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 37,190.00 USD | 123,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 4,180,000.00 USD | 128,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 325,080.00 USD | 128,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 59,820.00 USD | 128,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 2,840.00 USD | 128,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 154,420.00 USD | 128,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `202.50` | 17,270.00 USD | 128,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 37,000.00 USD | 128,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `20.50` | 139,500,000.00 USD | 0.00 USD | 574,410.00 USD | `-79.87%` | `28,019.95` |
| `Live` | `Long` | `21.50` | 138,930,000.00 USD | 0.00 USD | 36,490.00 USD | `-78.89%` | `1,697.23` |
| `Live` | `Long` | `22.50` | 138,890,000.00 USD | 0.00 USD | 143,270.00 USD | `-77.91%` | `6,367.56` |
| `Live` | `Long` | `23.50` | 138,750,000.00 USD | 0.00 USD | 3,710.00 USD | `-76.93%` | `158.00` |
| `Live` | `Long` | `24.50` | 138,750,000.00 USD | 0.00 USD | 41,710.00 USD | `-75.95%` | `1,702.33` |
| `Live` | `Long` | `25.50` | 138,700,000.00 USD | 0.00 USD | 34,220.00 USD | `-74.96%` | `1,341.90` |
| `Live` | `Long` | `26.50` | 138,670,000.00 USD | 0.00 USD | 43,360.00 USD | `-73.98%` | `1,636.18` |
| `Live` | `Long` | `27.50` | 138,630,000.00 USD | 0.00 USD | 271,040.00 USD | `-73.00%` | `9,855.96` |
| `Live` | `Long` | `28.50` | 138,350,000.00 USD | 0.00 USD | 39,110.00 USD | `-72.02%` | `1,372.16` |
| `Live` | `Long` | `29.50` | 138,320,000.00 USD | 0.00 USD | 722,340.00 USD | `-71.04%` | `24,486.18` |
| `Live` | `Long` | `30.50` | 137,590,000.00 USD | 0.00 USD | 97,320.00 USD | `-70.05%` | `3,190.93` |
| `Live` | `Long` | `31.50` | 137,500,000.00 USD | 0.00 USD | 79,730.00 USD | `-69.07%` | `2,531.25` |
| `Live` | `Long` | `32.50` | 137,420,000.00 USD | 0.00 USD | 53,210.00 USD | `-68.09%` | `1,637.25` |
| `Live` | `Long` | `33.50` | 137,360,000.00 USD | 0.00 USD | 16,730.00 USD | `-67.11%` | `499.40` |
| `Live` | `Long` | `34.50` | 137,350,000.00 USD | 0.00 USD | 6,550,000.00 USD | `-66.13%` | `189,977.26` |
| `Live` | `Long` | `35.50` | 130,790,000.00 USD | 0.00 USD | 45,060.00 USD | `-65.14%` | `1,269.41` |
| `Live` | `Long` | `36.50` | 130,750,000.00 USD | 0.00 USD | 28,270.00 USD | `-64.16%` | `774.54` |
| `Live` | `Long` | `37.50` | 130,720,000.00 USD | 0.00 USD | 224,580.00 USD | `-63.18%` | `5,988.67` |
| `Live` | `Long` | `38.50` | 130,490,000.00 USD | 0.00 USD | 3,030,000.00 USD | `-62.20%` | `78,687.29` |
| `Live` | `Long` | `39.50` | 127,460,000.00 USD | 0.00 USD | 230,210.00 USD | `-61.22%` | `5,828.16` |
| `Live` | `Long` | `40.50` | 127,230,000.00 USD | 0.00 USD | 1,820,000.00 USD | `-60.24%` | `44,920.88` |
| `Live` | `Long` | `41.50` | 125,420,000.00 USD | 0.00 USD | 97,100.00 USD | `-59.25%` | `2,339.86` |
| `Live` | `Long` | `42.50` | 125,320,000.00 USD | 0.00 USD | 102,760.00 USD | `-58.27%` | `2,417.88` |
| `Live` | `Long` | `43.50` | 125,220,000.00 USD | 0.00 USD | 904,870.00 USD | `-57.29%` | `20,801.63` |
| `Live` | `Long` | `44.50` | 124,310,000.00 USD | 0.00 USD | 68,340.00 USD | `-56.31%` | `1,535.70` |
| `Live` | `Long` | `45.50` | 124,240,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-55.33%` | `86,135.57` |
| `Live` | `Long` | `46.50` | 120,320,000.00 USD | 0.00 USD | 11,460.00 USD | `-54.34%` | `246.43` |
| `Live` | `Long` | `47.50` | 120,310,000.00 USD | 0.00 USD | 65,050.00 USD | `-53.36%` | `1,369.53` |
| `Live` | `Long` | `48.50` | 120,250,000.00 USD | 0.00 USD | 165,150.00 USD | `-52.38%` | `3,405.18` |
| `Live` | `Long` | `49.50` | 120,080,000.00 USD | 0.00 USD | 79,620.00 USD | `-51.40%` | `1,608.47` |
| `Live` | `Long` | `50.50` | 120,000,000.00 USD | 0.00 USD | 100,530.00 USD | `-50.42%` | `1,990.60` |
| `Live` | `Long` | `51.50` | 119,900,000.00 USD | 0.00 USD | 858,200.00 USD | `-49.44%` | `16,664.00` |
| `Live` | `Long` | `52.50` | 119,040,000.00 USD | 0.00 USD | 2,190,000.00 USD | `-48.45%` | `41,721.32` |
| `Live` | `Long` | `53.50` | 116,850,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-47.47%` | `29,990.03` |
| `Live` | `Long` | `54.50` | 115,250,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-46.49%` | `20,562.61` |
| `Live` | `Long` | `55.50` | 114,130,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-45.51%` | `22,470.91` |
| `Live` | `Long` | `56.50` | 112,880,000.00 USD | 0.00 USD | 100,740.00 USD | `-44.53%` | `1,783.00` |
| `Live` | `Long` | `57.50` | 112,780,000.00 USD | 0.00 USD | 144,990.00 USD | `-43.54%` | `2,521.54` |
| `Live` | `Long` | `58.50` | 112,630,000.00 USD | 0.00 USD | 165,810.00 USD | `-42.56%` | `2,834.37` |
| `Live` | `Long` | `59.50` | 112,470,000.00 USD | 0.00 USD | 140,800.00 USD | `-41.58%` | `2,366.44` |
| `Live` | `Long` | `60.50` | 112,330,000.00 USD | 0.00 USD | 269,530.00 USD | `-40.60%` | `4,455.06` |
| `Live` | `Long` | `61.50` | 112,060,000.00 USD | 0.00 USD | 229,050.00 USD | `-39.62%` | `3,724.41` |
| `Live` | `Long` | `62.50` | 111,830,000.00 USD | 0.00 USD | 248,340.00 USD | `-38.64%` | `3,973.37` |
| `Live` | `Long` | `63.50` | 111,580,000.00 USD | 0.00 USD | 237,900.00 USD | `-37.65%` | `3,746.43` |
| `Live` | `Long` | `64.50` | 111,340,000.00 USD | 0.00 USD | 11,690,000.00 USD | `-36.67%` | `181,231.57` |
| `Live` | `Long` | `65.50` | 99,650,000.00 USD | 0.00 USD | 178,730.00 USD | `-35.69%` | `2,728.68` |
| `Live` | `Long` | `66.50` | 99,480,000.00 USD | 0.00 USD | 87,780.00 USD | `-34.71%` | `1,319.93` |
| `Live` | `Long` | `67.50` | 99,390,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-33.73%` | `16,328.43` |
| `Live` | `Long` | `68.50` | 98,290,000.00 USD | 0.00 USD | 39,000,000.00 USD | `-32.74%` | `569,367.43` |
| `Live` | `Long` | `69.50` | 59,280,000.00 USD | 0.00 USD | 297,770.00 USD | `-31.76%` | `4,284.52` |
| `Live` | `Long` | `70.50` | 58,990,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-30.78%` | `38,627.13` |
| `Live` | `Long` | `71.50` | 56,260,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-29.80%` | `25,287.11` |
| `Live` | `Long` | `72.50` | 54,450,000.00 USD | 0.00 USD | 375,150.00 USD | `-28.82%` | `5,174.49` |
| `Live` | `Long` | `73.50` | 54,080,000.00 USD | 0.00 USD | 869,180.00 USD | `-27.84%` | `11,825.59` |
| `Live` | `Long` | `74.50` | 53,210,000.00 USD | 0.00 USD | 390,130.00 USD | `-26.85%` | `5,236.58` |
| `Live` | `Long` | `75.50` | 52,820,000.00 USD | 0.00 USD | 956,730.00 USD | `-25.87%` | `12,671.91` |
| `Live` | `Long` | `76.50` | 51,860,000.00 USD | 0.00 USD | 901,590.00 USD | `-24.89%` | `11,785.50` |
| `Live` | `Long` | `77.50` | 50,960,000.00 USD | 0.00 USD | 832,690.00 USD | `-23.91%` | `10,744.35` |
| `Live` | `Long` | `78.50` | 50,130,000.00 USD | 0.00 USD | 4,700,000.00 USD | `-22.93%` | `59,934.81` |
| `Live` | `Long` | `79.50` | 45,420,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-21.94%` | `23,693.13` |
| `Live` | `Long` | `80.50` | 43,540,000.00 USD | 0.00 USD | 425,250.00 USD | `-20.96%` | `5,282.59` |
| `Live` | `Long` | `81.50` | 43,120,000.00 USD | 0.00 USD | 2,560,000.00 USD | `-19.98%` | `31,426.08` |
| `Live` | `Long` | `82.50` | 40,550,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-19.00%` | `17,047.14` |
| `Live` | `Long` | `83.50` | 39,150,000.00 USD | 0.00 USD | 908,370.00 USD | `-18.02%` | `10,878.69` |
| `Live` | `Long` | `84.50` | 38,240,000.00 USD | 0.00 USD | 574,650.00 USD | `-17.03%` | `6,800.60` |
| `Live` | `Long` | `85.50` | 37,660,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-16.05%` | `11,929.81` |
| `Live` | `Long` | `86.50` | 36,640,000.00 USD | 0.00 USD | 778,120.00 USD | `-15.07%` | `8,995.60` |
| `Live` | `Long` | `87.50` | 35,870,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-14.09%` | `18,021.05` |
| `Live` | `Long` | `88.50` | 34,290,000.00 USD | 0.00 USD | 4,050,000.00 USD | `-13.11%` | `45,707.76` |
| `Live` | `Long` | `89.50` | 30,240,000.00 USD | 0.00 USD | 328,110.00 USD | `-12.13%` | `3,665.98` |
| `Live` | `Long` | `90.50` | 29,920,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-11.14%` | `19,871.97` |
| `Live` | `Long` | `91.50` | 28,120,000.00 USD | 0.00 USD | 4,240,000.00 USD | `-10.16%` | `46,288.08` |
| `Live` | `Long` | `92.50` | 23,880,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-9.18%` | `12,915.48` |
| `Live` | `Long` | `93.50` | 22,690,000.00 USD | 0.00 USD | 3,140,000.00 USD | `-8.20%` | `33,584.02` |
| `Live` | `Long` | `94.50` | 19,550,000.00 USD | 0.00 USD | 2,910,000.00 USD | `-7.22%` | `30,778.10` |
| `Live` | `Long` | `95.50` | 16,640,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-6.23%` | `18,818.29` |
| `Live` | `Long` | `96.50` | 14,840,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-5.25%` | `14,568.70` |
| `Live` | `Long` | `97.50` | 13,440,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-4.27%` | `18,820.31` |
| `Live` | `Long` | `98.50` | 11,600,000.00 USD | 0.00 USD | 11,050,000.00 USD | `-3.29%` | `112,155.03` |
| `Live` | `Long` | `99.50` | 554,170.00 USD | 0.00 USD | 448,020.00 USD | `-2.31%` | `4,502.67` |
| `Live` | `Long` | `100.50` | 106,160.00 USD | 0.00 USD | 106,160.00 USD | `-1.33%` | `1,056.31` |
| `Live` | `Short` | `103.50` | 70,910.00 USD | 70,910.00 USD | 0.00 USD | `+1.62%` | `685.16` |
| `Live` | `Short` | `104.50` | 1,510,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+2.60%` | `13,734.11` |
| `Live` | `Short` | `105.50` | 1,700,000.00 USD | 193,620.00 USD | 0.00 USD | `+3.58%` | `1,835.25` |
| `Live` | `Short` | `106.50` | 1,730,000.00 USD | 27,960.00 USD | 0.00 USD | `+4.57%` | `262.57` |
| `Live` | `Short` | `107.50` | 2,090,000.00 USD | 367,260.00 USD | 0.00 USD | `+5.55%` | `3,416.34` |
| `Live` | `Short` | `108.50` | 2,200,000.00 USD | 105,510.00 USD | 0.00 USD | `+6.53%` | `972.44` |
| `Live` | `Short` | `109.50` | 4,050,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+7.51%` | `16,930.28` |
| `Live` | `Short` | `110.50` | 4,250,000.00 USD | 195,170.00 USD | 0.00 USD | `+8.49%` | `1,766.26` |
| `Live` | `Short` | `111.50` | 6,700,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+9.47%` | `21,965.81` |
| `Live` | `Short` | `112.50` | 6,920,000.00 USD | 223,220.00 USD | 0.00 USD | `+10.46%` | `1,984.18` |
| `Live` | `Short` | `113.50` | 6,980,000.00 USD | 54,920.00 USD | 0.00 USD | `+11.44%` | `483.86` |
| `Live` | `Short` | `114.50` | 7,040,000.00 USD | 62,390.00 USD | 0.00 USD | `+12.42%` | `544.91` |
| `Live` | `Short` | `115.50` | 7,990,000.00 USD | 949,020.00 USD | 0.00 USD | `+13.40%` | `8,216.60` |
| `Live` | `Short` | `116.50` | 12,690,000.00 USD | 4,700,000.00 USD | 0.00 USD | `+14.38%` | `40,324.32` |
| `Live` | `Short` | `117.50` | 13,210,000.00 USD | 528,600.00 USD | 0.00 USD | `+15.37%` | `4,498.74` |
| `Live` | `Short` | `118.50` | 13,990,000.00 USD | 775,130.00 USD | 0.00 USD | `+16.35%` | `6,541.15` |
| `Live` | `Short` | `119.50` | 14,320,000.00 USD | 326,570.00 USD | 0.00 USD | `+17.33%` | `2,732.77` |
| `Live` | `Short` | `120.50` | 14,370,000.00 USD | 57,070.00 USD | 0.00 USD | `+18.31%` | `473.63` |
| `Live` | `Short` | `121.50` | 14,410,000.00 USD | 35,300.00 USD | 0.00 USD | `+19.29%` | `290.56` |
| `Live` | `Short` | `122.50` | 14,510,000.00 USD | 103,390.00 USD | 0.00 USD | `+20.27%` | `844.02` |
| `Live` | `Short` | `123.50` | 14,520,000.00 USD | 8,290.00 USD | 0.00 USD | `+21.26%` | `67.09` |
| `Live` | `Short` | `124.50` | 14,720,000.00 USD | 200,050.00 USD | 0.00 USD | `+22.24%` | `1,606.81` |
| `Live` | `Short` | `125.50` | 14,730,000.00 USD | 8,220.00 USD | 0.00 USD | `+23.22%` | `65.48` |
| `Live` | `Short` | `126.50` | 27,270,000.00 USD | 12,540,000.00 USD | 0.00 USD | `+24.20%` | `99,169.43` |
| `Live` | `Short` | `127.50` | 28,050,000.00 USD | 773,060.00 USD | 0.00 USD | `+25.18%` | `6,063.18` |
| `Live` | `Short` | `128.50` | 33,750,000.00 USD | 5,700,000.00 USD | 0.00 USD | `+26.17%` | `44,368.40` |
| `Live` | `Short` | `129.50` | 38,500,000.00 USD | 4,750,000.00 USD | 0.00 USD | `+27.15%` | `36,692.85` |
| `Live` | `Short` | `130.50` | 39,530,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+28.13%` | `7,866.13` |
| `Live` | `Short` | `131.50` | 39,530,000.00 USD | 8,270.00 USD | 0.00 USD | `+29.11%` | `62.89` |
| `Live` | `Short` | `132.50` | 39,750,000.00 USD | 215,650.00 USD | 0.00 USD | `+30.09%` | `1,627.55` |
| `Live` | `Short` | `133.50` | 39,930,000.00 USD | 179,930.00 USD | 0.00 USD | `+31.08%` | `1,347.76` |
| `Live` | `Short` | `134.50` | 39,960,000.00 USD | 31,190.00 USD | 0.00 USD | `+32.06%` | `231.91` |
| `Live` | `Short` | `135.50` | 40,550,000.00 USD | 587,250.00 USD | 0.00 USD | `+33.04%` | `4,333.95` |
| `Live` | `Short` | `136.50` | 40,550,000.00 USD | 1,500.00 USD | 0.00 USD | `+34.02%` | `10.96` |
| `Live` | `Short` | `137.50` | 40,550,000.00 USD | 4,660.00 USD | 0.00 USD | `+35.00%` | `33.89` |
| `Live` | `Short` | `138.50` | 42,870,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+35.98%` | `16,741.05` |
| `Live` | `Short` | `139.50` | 44,150,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+36.97%` | `9,146.81` |
| `Live` | `Short` | `140.50` | 44,160,000.00 USD | 14,460.00 USD | 0.00 USD | `+37.95%` | `102.92` |
| `Live` | `Short` | `141.50` | 44,410,000.00 USD | 250,580.00 USD | 0.00 USD | `+38.93%` | `1,770.85` |
| `Live` | `Short` | `142.50` | 44,710,000.00 USD | 294,930.00 USD | 0.00 USD | `+39.91%` | `2,069.69` |
| `Live` | `Short` | `143.50` | 44,820,000.00 USD | 112,820.00 USD | 0.00 USD | `+40.89%` | `786.17` |
| `Live` | `Short` | `144.50` | 45,720,000.00 USD | 893,550.00 USD | 0.00 USD | `+41.88%` | `6,183.77` |
| `Live` | `Short` | `145.50` | 45,740,000.00 USD | 19,490.00 USD | 0.00 USD | `+42.86%` | `133.92` |
| `Live` | `Short` | `146.50` | 46,440,000.00 USD | 705,840.00 USD | 0.00 USD | `+43.84%` | `4,818.01` |
| `Live` | `Short` | `147.50` | 48,000,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+44.82%` | `10,572.42` |
| `Live` | `Short` | `148.50` | 48,890,000.00 USD | 888,260.00 USD | 0.00 USD | `+45.80%` | `5,981.52` |
| `Live` | `Short` | `149.50` | 49,280,000.00 USD | 393,400.00 USD | 0.00 USD | `+46.78%` | `2,631.46` |
| `Live` | `Short` | `150.50` | 49,290,000.00 USD | 7,100.00 USD | 0.00 USD | `+47.77%` | `47.16` |
| `Live` | `Short` | `151.50` | 49,310,000.00 USD | 18,210.00 USD | 0.00 USD | `+48.75%` | `120.23` |
| `Live` | `Short` | `152.50` | 50,410,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+49.73%` | `7,254.67` |
| `Live` | `Short` | `153.50` | 50,630,000.00 USD | 218,290.00 USD | 0.00 USD | `+50.71%` | `1,422.07` |
| `Live` | `Short` | `154.50` | 50,690,000.00 USD | 56,280.00 USD | 0.00 USD | `+51.69%` | `364.28` |
| `Live` | `Short` | `155.50` | 50,820,000.00 USD | 129,290.00 USD | 0.00 USD | `+52.68%` | `831.43` |
| `Live` | `Short` | `156.50` | 52,280,000.00 USD | 1,470,000.00 USD | 0.00 USD | `+53.66%` | `9,366.44` |
| `Live` | `Short` | `157.50` | 52,800,000.00 USD | 520,640.00 USD | 0.00 USD | `+54.64%` | `3,305.67` |
| `Live` | `Short` | `158.50` | 57,630,000.00 USD | 4,830,000.00 USD | 0.00 USD | `+55.62%` | `30,460.07` |
| `Live` | `Short` | `159.50` | 57,780,000.00 USD | 152,670.00 USD | 0.00 USD | `+56.60%` | `957.15` |
| `Live` | `Short` | `160.50` | 58,480,000.00 USD | 699,590.00 USD | 0.00 USD | `+57.58%` | `4,358.82` |
| `Live` | `Short` | `161.50` | 58,890,000.00 USD | 409,130.00 USD | 0.00 USD | `+58.57%` | `2,533.33` |
| `Live` | `Short` | `162.50` | 94,650,000.00 USD | 35,750,000.00 USD | 0.00 USD | `+59.55%` | `220,024.05` |
| `Live` | `Short` | `163.50` | 94,650,000.00 USD | 3,770.00 USD | 0.00 USD | `+60.53%` | `23.08` |
| `Live` | `Short` | `164.50` | 95,810,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+61.51%` | `7,071.30` |
| `Live` | `Short` | `165.50` | 101,870,000.00 USD | 6,060,000.00 USD | 0.00 USD | `+62.49%` | `36,592.22` |
| `Live` | `Short` | `166.50` | 102,090,000.00 USD | 223,180.00 USD | 0.00 USD | `+63.48%` | `1,340.45` |
| `Live` | `Short` | `167.50` | 102,770,000.00 USD | 676,710.00 USD | 0.00 USD | `+64.46%` | `4,040.08` |
| `Live` | `Short` | `168.50` | 103,230,000.00 USD | 462,890.00 USD | 0.00 USD | `+65.44%` | `2,747.13` |
| `Live` | `Short` | `169.50` | 103,280,000.00 USD | 48,800.00 USD | 0.00 USD | `+66.42%` | `287.91` |
| `Live` | `Short` | `171.50` | 103,290,000.00 USD | 10,230.00 USD | 0.00 USD | `+68.38%` | `59.65` |
| `Live` | `Short` | `172.50` | 103,350,000.00 USD | 54,460.00 USD | 0.00 USD | `+69.37%` | `315.71` |
| `Live` | `Short` | `173.50` | 103,380,000.00 USD | 32,470.00 USD | 0.00 USD | `+70.35%` | `187.16` |
| `Live` | `Short` | `174.50` | 103,940,000.00 USD | 562,210.00 USD | 0.00 USD | `+71.33%` | `3,221.81` |
| `Live` | `Short` | `175.50` | 103,940,000.00 USD | 900.32 USD | 0.00 USD | `+72.31%` | `5.13` |
| `Live` | `Short` | `176.50` | 103,990,000.00 USD | 49,780.00 USD | 0.00 USD | `+73.29%` | `282.06` |
| `Live` | `Short` | `177.50` | 107,020,000.00 USD | 3,030,000.00 USD | 0.00 USD | `+74.28%` | `17,044.01` |
| `Live` | `Short` | `178.50` | 107,020,000.00 USD | 1,620.00 USD | 0.00 USD | `+75.26%` | `9.06` |
| `Live` | `Short` | `179.50` | 107,030,000.00 USD | 7,910.00 USD | 0.00 USD | `+76.24%` | `44.07` |
| `Live` | `Short` | `180.50` | 107,050,000.00 USD | 24,640.00 USD | 0.00 USD | `+77.22%` | `136.51` |
| `Live` | `Short` | `181.50` | 107,050,000.00 USD | 589.88 USD | 0.00 USD | `+78.20%` | `3.25` |
| `Live` | `Short` | `182.50` | 107,250,000.00 USD | 200,610.00 USD | 0.00 USD | `+79.19%` | `1,099.22` |
| `Live` | `Short` | `183.50` | 107,650,000.00 USD | 395,000.00 USD | 0.00 USD | `+80.17%` | `2,152.58` |
| `Live` | `Short` | `184.50` | 107,880,000.00 USD | 232,980.00 USD | 0.00 USD | `+81.15%` | `1,262.79` |
| `Live` | `Short` | `185.50` | 107,900,000.00 USD | 22,820.00 USD | 0.00 USD | `+82.13%` | `123.01` |
| `Live` | `Short` | `186.50` | 108,820,000.00 USD | 911,800.00 USD | 0.00 USD | `+83.11%` | `4,888.99` |
| `Live` | `Short` | `187.50` | 109,280,000.00 USD | 468,500.00 USD | 0.00 USD | `+84.09%` | `2,498.69` |
| `Live` | `Short` | `188.50` | 109,320,000.00 USD | 40,280.00 USD | 0.00 USD | `+85.08%` | `213.69` |
| `Live` | `Short` | `189.50` | 109,670,000.00 USD | 348,830.00 USD | 0.00 USD | `+86.06%` | `1,840.81` |
| `Live` | `Short` | `190.50` | 123,490,000.00 USD | 13,820,000.00 USD | 0.00 USD | `+87.04%` | `72,553.82` |
| `Live` | `Short` | `191.50` | 123,490,000.00 USD | 515.14 USD | 0.00 USD | `+88.02%` | `2.69` |
| `Live` | `Short` | `192.50` | 123,600,000.00 USD | 106,850.00 USD | 0.00 USD | `+89.00%` | `555.09` |
| `Live` | `Short` | `193.50` | 123,740,000.00 USD | 133,820.00 USD | 0.00 USD | `+89.99%` | `691.56` |
| `Live` | `Short` | `194.50` | 123,790,000.00 USD | 57,550.00 USD | 0.00 USD | `+90.97%` | `295.91` |
| `Live` | `Short` | `195.50` | 123,940,000.00 USD | 150,780.00 USD | 0.00 USD | `+91.95%` | `771.23` |
| `Live` | `Short` | `196.50` | 123,980,000.00 USD | 37,190.00 USD | 0.00 USD | `+92.93%` | `189.25` |
| `Live` | `Short` | `197.50` | 128,170,000.00 USD | 4,180,000.00 USD | 0.00 USD | `+93.91%` | `21,187.04` |
| `Live` | `Short` | `198.50` | 128,490,000.00 USD | 325,080.00 USD | 0.00 USD | `+94.89%` | `1,637.68` |
| `Live` | `Short` | `199.50` | 128,550,000.00 USD | 59,820.00 USD | 0.00 USD | `+95.88%` | `299.84` |
| `Live` | `Short` | `200.50` | 128,550,000.00 USD | 2,840.00 USD | 0.00 USD | `+96.86%` | `14.15` |
| `Live` | `Short` | `201.50` | 128,710,000.00 USD | 154,420.00 USD | 0.00 USD | `+97.84%` | `766.35` |
| `Live` | `Short` | `202.50` | 128,720,000.00 USD | 17,270.00 USD | 0.00 USD | `+98.82%` | `85.29` |
| `Live` | `Short` | `203.50` | 128,760,000.00 USD | 37,000.00 USD | 0.00 USD | `+99.80%` | `181.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.50` | 13,530,000.00 USD | 0.00 USD | 15,460.00 USD | `-76.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.50` | 13,510,000.00 USD | 0.00 USD | 3,830.00 USD | `-74.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.50` | 13,510,000.00 USD | 0.00 USD | 105.20 USD | `-73.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.50` | 13,510,000.00 USD | 0.00 USD | 527.35 USD | `-70.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.50` | 13,510,000.00 USD | 0.00 USD | 829.46 USD | `-67.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.50` | 13,510,000.00 USD | 0.00 USD | 1,320.00 USD | `-66.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.50` | 13,500,000.00 USD | 0.00 USD | 199.88 USD | `-63.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.50` | 13,500,000.00 USD | 0.00 USD | 205.21 USD | `-62.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.50` | 13,500,000.00 USD | 0.00 USD | 3,620.00 USD | `-61.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.50` | 13,500,000.00 USD | 0.00 USD | 423.63 USD | `-60.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.50` | 13,500,000.00 USD | 0.00 USD | 170,330.00 USD | `-58.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.50` | 13,330,000.00 USD | 0.00 USD | 104.40 USD | `-57.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.50` | 13,330,000.00 USD | 0.00 USD | 64,090.00 USD | `-55.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.50` | 13,270,000.00 USD | 0.00 USD | 249.71 USD | `-54.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.50` | 13,260,000.00 USD | 0.00 USD | 332.50 USD | `-53.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.50` | 13,260,000.00 USD | 0.00 USD | 102.82 USD | `-52.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.50` | 13,260,000.00 USD | 0.00 USD | 5,510.00 USD | `-50.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.50` | 13,260,000.00 USD | 0.00 USD | 4,070.00 USD | `-49.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.50` | 13,250,000.00 USD | 0.00 USD | 427.88 USD | `-48.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.50` | 13,250,000.00 USD | 0.00 USD | 26,860.00 USD | `-47.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.50` | 13,230,000.00 USD | 0.00 USD | 785.89 USD | `-46.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.50` | 13,230,000.00 USD | 0.00 USD | 210.90 USD | `-45.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.50` | 13,230,000.00 USD | 0.00 USD | 5,860.00 USD | `-44.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.50` | 13,220,000.00 USD | 0.00 USD | 6,550.00 USD | `-43.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.50` | 13,210,000.00 USD | 0.00 USD | 159.71 USD | `-42.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.50` | 13,210,000.00 USD | 0.00 USD | 10,860.00 USD | `-41.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.50` | 13,200,000.00 USD | 0.00 USD | 40,470.00 USD | `-40.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.50` | 13,160,000.00 USD | 0.00 USD | 18,990.00 USD | `-39.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.50` | 13,140,000.00 USD | 0.00 USD | 4,810.00 USD | `-38.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.50` | 13,140,000.00 USD | 0.00 USD | 13,260.00 USD | `-37.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.50` | 13,130,000.00 USD | 0.00 USD | 129.00 USD | `-36.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.50` | 13,130,000.00 USD | 0.00 USD | 4,650.00 USD | `-35.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.50` | 13,120,000.00 USD | 0.00 USD | 7,690.00 USD | `-34.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.50` | 13,110,000.00 USD | 0.00 USD | 607.50 USD | `-33.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.50` | 13,110,000.00 USD | 0.00 USD | 7,360.00 USD | `-32.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.50` | 13,110,000.00 USD | 0.00 USD | 54,850.00 USD | `-31.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.50` | 13,050,000.00 USD | 0.00 USD | 50,700.00 USD | `-30.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.50` | 13,000,000.00 USD | 0.00 USD | 1,470.00 USD | `-29.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.50` | 13,000,000.00 USD | 0.00 USD | 120,230.00 USD | `-28.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.50` | 12,880,000.00 USD | 0.00 USD | 139.65 USD | `-27.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.50` | 12,880,000.00 USD | 0.00 USD | 52,170.00 USD | `-26.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.50` | 12,830,000.00 USD | 0.00 USD | 26,730.00 USD | `-25.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.50` | 12,800,000.00 USD | 0.00 USD | 16,050.00 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.50` | 12,780,000.00 USD | 0.00 USD | 14,790.00 USD | `-23.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.50` | 12,770,000.00 USD | 0.00 USD | 81,220.00 USD | `-22.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.50` | 12,690,000.00 USD | 0.00 USD | 13,780.00 USD | `-21.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.50` | 12,670,000.00 USD | 0.00 USD | 118,650.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.50` | 12,550,000.00 USD | 0.00 USD | 91,450.00 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.50` | 12,460,000.00 USD | 0.00 USD | 27,520.00 USD | `-19.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.50` | 12,440,000.00 USD | 0.00 USD | 74,090.00 USD | `-18.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.50` | 12,360,000.00 USD | 0.00 USD | 24,890.00 USD | `-17.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.50` | 12,340,000.00 USD | 0.00 USD | 171,750.00 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.50` | 12,160,000.00 USD | 0.00 USD | 16,860.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.50` | 12,150,000.00 USD | 0.00 USD | 233,390.00 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.50` | 11,910,000.00 USD | 0.00 USD | 281,840.00 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.50` | 11,630,000.00 USD | 0.00 USD | 69,740.00 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.50` | 11,560,000.00 USD | 0.00 USD | 175,260.00 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.50` | 11,390,000.00 USD | 0.00 USD | 435,590.00 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.50` | 10,950,000.00 USD | 0.00 USD | 224,950.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.50` | 10,730,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.50` | 9,650,000.00 USD | 0.00 USD | 591,380.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.50` | 9,060,000.00 USD | 0.00 USD | 976,790.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.50` | 8,090,000.00 USD | 0.00 USD | 604,550.00 USD | `-5.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.50` | 7,480,000.00 USD | 0.00 USD | 491,960.00 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.50` | 6,990,000.00 USD | 0.00 USD | 3,480,000.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.50` | 3,510,000.00 USD | 0.00 USD | 910,510.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `100.50` | 2,600,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `101.50` | 797,300.00 USD | 0.00 USD | 797,300.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.50` | 805,020.00 USD | 805,020.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.50` | 1,150,000.00 USD | 348,530.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.50` | 1,900,000.00 USD | 742,710.00 USD | 0.00 USD | `+2.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.50` | 2,330,000.00 USD | 438,000.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.50` | 2,700,000.00 USD | 364,850.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.50` | 2,910,000.00 USD | 210,000.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.50` | 3,270,000.00 USD | 359,420.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.50` | 7,570,000.00 USD | 4,300,000.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.50` | 8,950,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.50` | 9,010,000.00 USD | 54,160.00 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.50` | 9,230,000.00 USD | 222,460.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.50` | 9,510,000.00 USD | 281,630.00 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.50` | 9,540,000.00 USD | 32,520.00 USD | 0.00 USD | `+12.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.50` | 9,660,000.00 USD | 119,540.00 USD | 0.00 USD | `+13.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.50` | 9,710,000.00 USD | 47,920.00 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.50` | 9,970,000.00 USD | 254,840.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.50` | 10,140,000.00 USD | 178,980.00 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.50` | 10,380,000.00 USD | 239,490.00 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.50` | 10,540,000.00 USD | 153,100.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.50` | 10,610,000.00 USD | 75,990.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.50` | 11,140,000.00 USD | 526,980.00 USD | 0.00 USD | `+20.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.50` | 12,210,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+21.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.50` | 12,370,000.00 USD | 166,110.00 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.50` | 12,930,000.00 USD | 554,500.00 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.50` | 13,040,000.00 USD | 114,230.00 USD | 0.00 USD | `+24.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.50` | 13,320,000.00 USD | 275,030.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.50` | 13,370,000.00 USD | 58,000.00 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.50` | 16,030,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+27.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.50` | 16,090,000.00 USD | 54,500.00 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.50` | 16,270,000.00 USD | 179,050.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.50` | 16,290,000.00 USD | 26,010.00 USD | 0.00 USD | `+30.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.50` | 16,310,000.00 USD | 13,090.00 USD | 0.00 USD | `+31.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.50` | 16,560,000.00 USD | 250,620.00 USD | 0.00 USD | `+32.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.50` | 16,630,000.00 USD | 74,880.00 USD | 0.00 USD | `+33.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.50` | 16,640,000.00 USD | 3,770.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.50` | 16,670,000.00 USD | 34,120.00 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.50` | 23,430,000.00 USD | 6,760,000.00 USD | 0.00 USD | `+35.98%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `139.50` | 25,640,000.00 USD | 2,220,000.00 USD | 0.00 USD | `+36.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.50` | 25,930,000.00 USD | 286,300.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.50` | 25,940,000.00 USD | 10,520.00 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.50` | 26,290,000.00 USD | 346,440.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.50` | 26,290,000.00 USD | 529.51 USD | 0.00 USD | `+40.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.50` | 26,560,000.00 USD | 269,670.00 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.50` | 26,570,000.00 USD | 13,070.00 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.50` | 26,770,000.00 USD | 198,500.00 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.50` | 26,820,000.00 USD | 46,350.00 USD | 0.00 USD | `+44.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.50` | 28,150,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+45.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.50` | 28,660,000.00 USD | 512,760.00 USD | 0.00 USD | `+46.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.50` | 28,930,000.00 USD | 269,220.00 USD | 0.00 USD | `+47.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.50` | 28,950,000.00 USD | 16,890.00 USD | 0.00 USD | `+48.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.50` | 28,960,000.00 USD | 12,020.00 USD | 0.00 USD | `+49.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.50` | 28,970,000.00 USD | 11,660.00 USD | 0.00 USD | `+50.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.50` | 28,980,000.00 USD | 12,130.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.50` | 29,000,000.00 USD | 13,650.00 USD | 0.00 USD | `+52.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.50` | 29,000,000.00 USD | 2,230.00 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.50` | 29,020,000.00 USD | 22,350.00 USD | 0.00 USD | `+55.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.50` | 29,020,000.00 USD | 815.04 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.50` | 29,270,000.00 USD | 242,540.00 USD | 0.00 USD | `+57.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.50` | 29,270,000.00 USD | 282.62 USD | 0.00 USD | `+58.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.50` | 29,270,000.00 USD | 5,030.00 USD | 0.00 USD | `+60.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.50` | 29,350,000.00 USD | 83,570.00 USD | 0.00 USD | `+62.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.50` | 29,350,000.00 USD | 517.81 USD | 0.00 USD | `+63.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.50` | 29,360,000.00 USD | 2,030.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.50` | 29,360,000.00 USD | 5,560.00 USD | 0.00 USD | `+65.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.50` | 29,360,000.00 USD | 1,410.00 USD | 0.00 USD | `+66.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.50` | 29,410,000.00 USD | 42,950.00 USD | 0.00 USD | `+67.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.50` | 29,410,000.00 USD | 686.00 USD | 0.00 USD | `+68.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.50` | 29,440,000.00 USD | 36,070.00 USD | 0.00 USD | `+69.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.50` | 29,450,000.00 USD | 6,550.00 USD | 0.00 USD | `+70.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.50` | 29,520,000.00 USD | 74,640.00 USD | 0.00 USD | `+72.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.50` | 29,530,000.00 USD | 1,450.00 USD | 0.00 USD | `+73.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.50` | 29,530,000.00 USD | 2,140.00 USD | 0.00 USD | `+74.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.50` | 29,530,000.00 USD | 2,990.00 USD | 0.00 USD | `+75.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.50` | 29,530,000.00 USD | 262.07 USD | 0.00 USD | `+76.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.50` | 29,630,000.00 USD | 102,680.00 USD | 0.00 USD | `+77.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.50` | 29,640,000.00 USD | 2,730.00 USD | 0.00 USD | `+78.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.50` | 29,660,000.00 USD | 19,620.00 USD | 0.00 USD | `+79.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.50` | 30,210,000.00 USD | 550,500.00 USD | 0.00 USD | `+80.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.50` | 30,240,000.00 USD | 29,490.00 USD | 0.00 USD | `+82.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.50` | 30,430,000.00 USD | 191,020.00 USD | 0.00 USD | `+84.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.50` | 30,570,000.00 USD | 141,530.00 USD | 0.00 USD | `+85.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.50` | 30,610,000.00 USD | 38,960.00 USD | 0.00 USD | `+87.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.50` | 30,610,000.00 USD | 4,280.00 USD | 0.00 USD | `+90.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.50` | 30,610,000.00 USD | 1,760.00 USD | 0.00 USD | `+91.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `196.50` | 30,870,000.00 USD | 253,980.00 USD | 0.00 USD | `+92.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.50` | 30,960,000.00 USD | 94,590.00 USD | 0.00 USD | `+93.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.50` | 31,340,000.00 USD | 374,220.00 USD | 0.00 USD | `+94.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.50` | 31,370,000.00 USD | 28,310.00 USD | 0.00 USD | `+95.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `200.50` | 31,670,000.00 USD | 302,560.00 USD | 0.00 USD | `+96.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `201.50` | 31,670,000.00 USD | 398.97 USD | 0.00 USD | `+97.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `202.50` | 31,670,000.00 USD | 2,430.00 USD | 0.00 USD | `+98.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `203.50` | 31,720,000.00 USD | 48,230.00 USD | 0.00 USD | `+99.80%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `89.60` | 410,320,000.00 USD | 0.00 USD | 410,320,000.00 USD | 700,630.00 USD | 281,700.00 USD | 577,220.00 USD |
| `7D` | `89.80` | 408,760,000.00 USD | 0.00 USD | 408,760,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `7D` | `90.00` | 407,780,000.00 USD | 0.00 USD | 407,780,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `7D` | `90.20` | 406,060,000.00 USD | 0.00 USD | 406,060,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD |
| `7D` | `90.40` | 404,060,000.00 USD | 0.00 USD | 404,060,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD |
| `7D` | `90.60` | 402,660,000.00 USD | 0.00 USD | 402,660,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD |
| `7D` | `90.80` | 399,540,000.00 USD | 0.00 USD | 399,540,000.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `7D` | `91.00` | 396,580,000.00 USD | 0.00 USD | 396,580,000.00 USD | 1,170,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `7D` | `91.20` | 394,540,000.00 USD | 0.00 USD | 394,540,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `91.40` | 238,630,000.00 USD | 0.00 USD | 238,630,000.00 USD | 249,290.00 USD | 231,510.00 USD | 316,210.00 USD |
| `7D` | `91.40` | 392,210,000.00 USD | 0.00 USD | 392,210,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `91.60` | 237,840,000.00 USD | 0.00 USD | 237,840,000.00 USD | 56,690.00 USD | 192,290.00 USD | 73,600.00 USD |
| `7D` | `91.60` | 388,890,000.00 USD | 0.00 USD | 388,890,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `91.80` | 237,510,000.00 USD | 0.00 USD | 237,510,000.00 USD | 369,020.00 USD | 218,430.00 USD | 123,590.00 USD |
| `7D` | `91.80` | 387,260,000.00 USD | 0.00 USD | 387,260,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 236,800,000.00 USD | 0.00 USD | 236,800,000.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD |
| `7D` | `92.00` | 385,060,000.00 USD | 0.00 USD | 385,060,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `92.20` | 236,340,000.00 USD | 0.00 USD | 236,340,000.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD |
| `7D` | `92.20` | 383,320,000.00 USD | 0.00 USD | 383,320,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `92.40` | 235,890,000.00 USD | 0.00 USD | 235,890,000.00 USD | 151,210.00 USD | 110,310.00 USD | 782,700.00 USD |
| `7D` | `92.40` | 382,460,000.00 USD | 0.00 USD | 382,460,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD |
| `1D` | `92.60` | 234,850,000.00 USD | 0.00 USD | 234,850,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD |
| `7D` | `92.60` | 380,550,000.00 USD | 0.00 USD | 380,550,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `92.80` | 234,590,000.00 USD | 0.00 USD | 234,590,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD |
| `7D` | `92.80` | 379,470,000.00 USD | 0.00 USD | 379,470,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `1D` | `93.00` | 234,440,000.00 USD | 0.00 USD | 234,440,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD |
| `7D` | `93.00` | 379,250,000.00 USD | 0.00 USD | 379,250,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `1D` | `93.20` | 234,270,000.00 USD | 0.00 USD | 234,270,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD |
| `7D` | `93.20` | 378,850,000.00 USD | 0.00 USD | 378,850,000.00 USD | 125,700.00 USD | 4,160.00 USD | 49,310.00 USD |
| `1D` | `93.40` | 234,060,000.00 USD | 0.00 USD | 234,060,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD |
| `7D` | `93.40` | 378,670,000.00 USD | 0.00 USD | 378,670,000.00 USD | 80,500.00 USD | 115,240.00 USD | 2,890.00 USD |
| `7D` | `93.60` | 378,480,000.00 USD | 0.00 USD | 378,480,000.00 USD | 238,200.00 USD | 343,740.00 USD | 114,860.00 USD |
| `7D` | `93.80` | 377,780,000.00 USD | 0.00 USD | 377,780,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD |
| `7D` | `94.00` | 377,100,000.00 USD | 0.00 USD | 377,100,000.00 USD | 78,790.00 USD | 153,680.00 USD | 134,360.00 USD |
| `7D` | `94.20` | 376,740,000.00 USD | 0.00 USD | 376,740,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD |
| `7D` | `94.40` | 376,080,000.00 USD | 0.00 USD | 376,080,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD |
| `7D` | `94.60` | 375,780,000.00 USD | 0.00 USD | 375,780,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `94.80` | 375,700,000.00 USD | 0.00 USD | 375,700,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD |
| `7D` | `95.00` | 375,680,000.00 USD | 0.00 USD | 375,680,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD |
| `1D` | `95.20` | 234,010,000.00 USD | 0.00 USD | 234,010,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD |
| `7D` | `95.20` | 374,720,000.00 USD | 0.00 USD | 374,720,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD |
| `1D` | `95.40` | 233,990,000.00 USD | 0.00 USD | 233,990,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD |
| `7D` | `95.40` | 374,330,000.00 USD | 0.00 USD | 374,330,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD |
| `1D` | `95.60` | 233,480,000.00 USD | 0.00 USD | 233,480,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD |
| `7D` | `95.60` | 372,810,000.00 USD | 0.00 USD | 372,810,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD |
| `1D` | `95.80` | 230,910,000.00 USD | 0.00 USD | 230,910,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD |
| `7D` | `95.80` | 368,760,000.00 USD | 0.00 USD | 368,760,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD |
| `1D` | `96.00` | 227,090,000.00 USD | 0.00 USD | 227,090,000.00 USD | 1,200,000.00 USD | 1,170,000.00 USD | 1,230,000.00 USD |
| `7D` | `96.00` | 364,520,000.00 USD | 0.00 USD | 364,520,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD |
| `1D` | `96.20` | 223,490,000.00 USD | 0.00 USD | 223,490,000.00 USD | 1,060,000.00 USD | 1,190,000.00 USD | 693,510.00 USD |
| `7D` | `96.20` | 358,090,000.00 USD | 0.00 USD | 358,090,000.00 USD | 2,940,000.00 USD | 1,970,000.00 USD | 1,990,000.00 USD |
| `1D` | `96.40` | 220,550,000.00 USD | 0.00 USD | 220,550,000.00 USD | 862,370.00 USD | 983,090.00 USD | 1,100,000.00 USD |
| `7D` | `96.40` | 351,190,000.00 USD | 0.00 USD | 351,190,000.00 USD | 2,950,000.00 USD | 643,110.00 USD | 2,370,000.00 USD |
| `1D` | `96.60` | 217,600,000.00 USD | 0.00 USD | 217,600,000.00 USD | 994,840.00 USD | 756,910.00 USD | 933,760.00 USD |
| `7D` | `96.60` | 345,220,000.00 USD | 0.00 USD | 345,220,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD |
| `1D` | `96.80` | 214,920,000.00 USD | 0.00 USD | 214,920,000.00 USD | 233,930.00 USD | 700,140.00 USD | 729,790.00 USD |
| `7D` | `96.80` | 337,120,000.00 USD | 0.00 USD | 337,120,000.00 USD | 2,970,000.00 USD | 2,770,000.00 USD | 2,950,000.00 USD |
| `1D` | `97.00` | 213,250,000.00 USD | 0.00 USD | 213,250,000.00 USD | 102,790.00 USD | 1,310.00 USD | 0.00 USD |
| `7D` | `97.00` | 328,430,000.00 USD | 0.00 USD | 328,430,000.00 USD | 5,250,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD |
| `1D` | `97.20` | 213,150,000.00 USD | 0.00 USD | 213,150,000.00 USD | 276,590.00 USD | 29,470.00 USD | 332,270.00 USD |
| `7D` | `97.20` | 318,600,000.00 USD | 0.00 USD | 318,600,000.00 USD | 5,470,000.00 USD | 4,350,000.00 USD | 3,720,000.00 USD |
| `1D` | `97.40` | 212,510,000.00 USD | 0.00 USD | 212,510,000.00 USD | 1,110,000.00 USD | 998,800.00 USD | 567,270.00 USD |
| `7D` | `97.40` | 305,070,000.00 USD | 0.00 USD | 305,070,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD |
| `1D` | `97.60` | 209,830,000.00 USD | 0.00 USD | 209,830,000.00 USD | 2,410,000.00 USD | 1,900,000.00 USD | 2,390,000.00 USD |
| `7D` | `97.60` | 294,660,000.00 USD | 0.00 USD | 294,660,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD |
| `1D` | `97.80` | 203,130,000.00 USD | 0.00 USD | 203,130,000.00 USD | 3,880,000.00 USD | 3,190,000.00 USD | 2,170,000.00 USD |
| `7D` | `97.80` | 279,310,000.00 USD | 0.00 USD | 279,310,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD |
| `1D` | `98.00` | 193,890,000.00 USD | 0.00 USD | 193,890,000.00 USD | 3,680,000.00 USD | 3,010,000.00 USD | 3,190,000.00 USD |
| `7D` | `98.00` | 265,850,000.00 USD | 0.00 USD | 265,850,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,710,000.00 USD |
| `1D` | `98.20` | 184,010,000.00 USD | 0.00 USD | 184,010,000.00 USD | 3,040,000.00 USD | 2,880,000.00 USD | 2,030,000.00 USD |
| `7D` | `98.20` | 241,170,000.00 USD | 0.00 USD | 241,170,000.00 USD | 7,790,000.00 USD | 6,660,000.00 USD | 5,670,000.00 USD |
| `1D` | `98.40` | 176,060,000.00 USD | 0.00 USD | 176,060,000.00 USD | 3,740,000.00 USD | 3,150,000.00 USD | 3,460,000.00 USD |
| `7D` | `98.40` | 221,050,000.00 USD | 0.00 USD | 221,050,000.00 USD | 9,460,000.00 USD | 2,950,000.00 USD | 9,620,000.00 USD |
| `1D` | `98.60` | 165,710,000.00 USD | 0.00 USD | 165,710,000.00 USD | 6,200,000.00 USD | 4,440,000.00 USD | 6,740,000.00 USD |
| `7D` | `98.60` | 199,010,000.00 USD | 0.00 USD | 199,010,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD |
| `1D` | `98.80` | 148,320,000.00 USD | 0.00 USD | 148,320,000.00 USD | 7,150,000.00 USD | 6,900,000.00 USD | 5,060,000.00 USD |
| `7D` | `98.80` | 163,520,000.00 USD | 0.00 USD | 163,520,000.00 USD | 12,530,000.00 USD | 9,880,000.00 USD | 13,070,000.00 USD |
| `1D` | `99.00` | 129,210,000.00 USD | 0.00 USD | 129,210,000.00 USD | 4,640,000.00 USD | 4,540,000.00 USD | 5,120,000.00 USD |
| `7D` | `99.00` | 128,040,000.00 USD | 0.00 USD | 128,040,000.00 USD | 13,760,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD |
| `1D` | `99.20` | 114,900,000.00 USD | 0.00 USD | 114,900,000.00 USD | 4,370,000.00 USD | 4,670,000.00 USD | 3,600,000.00 USD |
| `7D` | `99.20` | 86,890,000.00 USD | 0.00 USD | 86,890,000.00 USD | 12,550,000.00 USD | 6,970,000.00 USD | 5,390,000.00 USD |
| `1D` | `99.40` | 102,260,000.00 USD | 0.00 USD | 102,260,000.00 USD | 3,410,000.00 USD | 4,060,000.00 USD | 4,870,000.00 USD |
| `7D` | `99.40` | 61,980,000.00 USD | 0.00 USD | 61,980,000.00 USD | 2,300,000.00 USD | 599,290.00 USD | 6,690,000.00 USD |
| `1D` | `99.60` | 89,920,000.00 USD | 0.00 USD | 89,920,000.00 USD | 3,230,000.00 USD | 2,990,000.00 USD | 2,970,000.00 USD |
| `7D` | `99.60` | 52,390,000.00 USD | 0.00 USD | 52,390,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD |
| `1D` | `99.80` | 80,730,000.00 USD | 0.00 USD | 80,730,000.00 USD | 1,280,000.00 USD | 2,380,000.00 USD | 3,150,000.00 USD |
| `7D` | `99.80` | 47,920,000.00 USD | 0.00 USD | 47,920,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD |
| `1D` | `100.00` | 73,920,000.00 USD | 0.00 USD | 73,920,000.00 USD | 1,360,000.00 USD | 790,810.00 USD | 453,250.00 USD |
| `7D` | `100.00` | 45,160,000.00 USD | 0.00 USD | 45,160,000.00 USD | 533,430.00 USD | 36,980.00 USD | 0.00 USD |
| `1D` | `100.20` | 71,310,000.00 USD | 0.00 USD | 71,310,000.00 USD | 34,220.00 USD | 341,570.00 USD | 431,510.00 USD |
| `1D` | `100.40` | 70,510,000.00 USD | 0.00 USD | 70,510,000.00 USD | 718,910.00 USD | 877,160.00 USD | 438,820.00 USD |
| `7D` | `100.40` | 44,590,000.00 USD | 0.00 USD | 44,590,000.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD |
| `1D` | `100.60` | 68,470,000.00 USD | 0.00 USD | 68,470,000.00 USD | 1,010,000.00 USD | 251,930.00 USD | 2,790,000.00 USD |
| `7D` | `100.60` | 43,270,000.00 USD | 0.00 USD | 43,270,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD |
| `1D` | `100.80` | 64,420,000.00 USD | 0.00 USD | 64,420,000.00 USD | 760,660.00 USD | 1,670,000.00 USD | 641,510.00 USD |
| `7D` | `100.80` | 41,500,000.00 USD | 0.00 USD | 41,500,000.00 USD | 3,660,000.00 USD | 981,100.00 USD | 0.00 USD |
| `1D` | `101.00` | 61,350,000.00 USD | 0.00 USD | 61,350,000.00 USD | 8,970,000.00 USD | 5,980,000.00 USD | 7,370,000.00 USD |
| `7D` | `101.00` | 36,850,000.00 USD | 0.00 USD | 36,850,000.00 USD | 2,860,000.00 USD | 4,560,000.00 USD | 5,020,000.00 USD |
| `1D` | `101.20` | 39,030,000.00 USD | 0.00 USD | 39,030,000.00 USD | 5,110,000.00 USD | 7,010,000.00 USD | 5,130,000.00 USD |
| `7D` | `101.20` | 24,410,000.00 USD | 0.00 USD | 24,410,000.00 USD | 4,750,000.00 USD | 3,220,000.00 USD | 5,930,000.00 USD |
| `1D` | `101.40` | 21,790,000.00 USD | 0.00 USD | 21,790,000.00 USD | 692,280.00 USD | 609,630.00 USD | 1,690.00 USD |
| `7D` | `101.40` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 3,020,000.00 USD | 0.00 USD | 7,490,000.00 USD |
| `1D` | `101.60` | 20,480,000.00 USD | 0.00 USD | 20,480,000.00 USD | 5,150,000.00 USD | 2,220,000.00 USD | 13,110,000.00 USD |
| `7D` | `101.60` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD |
| `7D` | `101.60` | 19,700,000.00 USD | 19,700,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD |
| `1D` | `101.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `101.80` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,210,000.00 USD |
| `7D` | `101.80` | 29,040,000.00 USD | 29,040,000.00 USD | 0.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD |
| `1D` | `102.00` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 354,260.00 USD | 0.00 USD | 364,710.00 USD |
| `7D` | `102.00` | 30,870,000.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,830,000.00 USD |
| `1D` | `102.20` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 799,010.00 USD | 1,160,000.00 USD | 764,000.00 USD |
| `7D` | `102.20` | 33,110,000.00 USD | 33,110,000.00 USD | 0.00 USD | 369,280.00 USD | 578,040.00 USD | 1,290,000.00 USD |
| `1D` | `102.40` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,590,000.00 USD |
| `7D` | `102.40` | 36,130,000.00 USD | 36,130,000.00 USD | 0.00 USD | 1,150,000.00 USD | 299,640.00 USD | 1,580,000.00 USD |
| `1D` | `102.60` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 26,340.00 USD | 8,280.00 USD |
| `7D` | `102.60` | 38,550,000.00 USD | 38,550,000.00 USD | 0.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD |
| `1D` | `102.80` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 1,220,000.00 USD | 1,650,000.00 USD | 563,120.00 USD |
| `7D` | `102.80` | 46,350,000.00 USD | 46,350,000.00 USD | 0.00 USD | 7,520,000.00 USD | 0.00 USD | 271,670.00 USD |
| `1D` | `103.00` | 18,100,000.00 USD | 18,100,000.00 USD | 0.00 USD | 2,190,000.00 USD | 1,200,000.00 USD | 0.00 USD |
| `7D` | `103.00` | 60,350,000.00 USD | 60,350,000.00 USD | 0.00 USD | 11,170,000.00 USD | 0.00 USD | 2,830,000.00 USD |
| `1D` | `103.20` | 23,730,000.00 USD | 23,730,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,430,000.00 USD | 1,550,000.00 USD |
| `7D` | `103.20` | 74,070,000.00 USD | 74,070,000.00 USD | 0.00 USD | 13,600,000.00 USD | 4,380.00 USD | 112,320.00 USD |
| `1D` | `103.40` | 31,060,000.00 USD | 31,060,000.00 USD | 0.00 USD | 4,020,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD |
| `7D` | `103.40` | 89,080,000.00 USD | 89,080,000.00 USD | 0.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD |
| `1D` | `103.60` | 45,540,000.00 USD | 45,540,000.00 USD | 0.00 USD | 4,330,000.00 USD | 2,100,000.00 USD | 8,040,000.00 USD |
| `7D` | `103.60` | 107,470,000.00 USD | 107,470,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 54,990,000.00 USD | 54,990,000.00 USD | 0.00 USD | 3,390,000.00 USD | 2,620,000.00 USD | 3,430,000.00 USD |
| `7D` | `103.80` | 119,810,000.00 USD | 119,810,000.00 USD | 0.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 67,360,000.00 USD | 67,360,000.00 USD | 0.00 USD | 4,020,000.00 USD | 3,820,000.00 USD | 4,530,000.00 USD |
| `7D` | `104.00` | 148,230,000.00 USD | 148,230,000.00 USD | 0.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD |
| `1D` | `104.20` | 76,390,000.00 USD | 76,390,000.00 USD | 0.00 USD | 3,440,000.00 USD | 2,450,000.00 USD | 3,140,000.00 USD |
| `7D` | `104.20` | 168,320,000.00 USD | 168,320,000.00 USD | 0.00 USD | 7,510,000.00 USD | 6,900,000.00 USD | 5,680,000.00 USD |
| `1D` | `104.40` | 84,550,000.00 USD | 84,550,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,660,000.00 USD | 3,340,000.00 USD |
| `7D` | `104.40` | 184,450,000.00 USD | 184,450,000.00 USD | 0.00 USD | 4,800,000.00 USD | 3,700,000.00 USD | 7,640,000.00 USD |
| `1D` | `104.60` | 92,860,000.00 USD | 92,860,000.00 USD | 0.00 USD | 2,260,000.00 USD | 2,030,000.00 USD | 4,030,000.00 USD |
| `7D` | `104.60` | 202,020,000.00 USD | 202,020,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD |
| `1D` | `104.80` | 99,040,000.00 USD | 99,040,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,580,000.00 USD | 3,060,000.00 USD |
| `7D` | `104.80` | 219,110,000.00 USD | 219,110,000.00 USD | 0.00 USD | 5,130,000.00 USD | 4,150,000.00 USD | 7,810,000.00 USD |
| `1D` | `105.00` | 101,110,000.00 USD | 101,110,000.00 USD | 0.00 USD | 501,070.00 USD | 641,540.00 USD | 928,370.00 USD |
| `7D` | `105.00` | 235,970,000.00 USD | 235,970,000.00 USD | 0.00 USD | 5,470,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 102,290,000.00 USD | 102,290,000.00 USD | 0.00 USD | 422,890.00 USD | 21,950.00 USD | 732,910.00 USD |
| `7D` | `105.20` | 248,400,000.00 USD | 248,400,000.00 USD | 0.00 USD | 5,320,000.00 USD | 4,850,000.00 USD | 2,270,000.00 USD |
| `1D` | `105.40` | 103,430,000.00 USD | 103,430,000.00 USD | 0.00 USD | 331,150.00 USD | 7,520.00 USD | 804,580.00 USD |
| `7D` | `105.40` | 261,050,000.00 USD | 261,050,000.00 USD | 0.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 5,240,000.00 USD |
| `1D` | `105.60` | 106,050,000.00 USD | 106,050,000.00 USD | 0.00 USD | 561,460.00 USD | 995,420.00 USD | 1,060,000.00 USD |
| `7D` | `105.60` | 279,090,000.00 USD | 279,090,000.00 USD | 0.00 USD | 6,220,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD |
| `1D` | `105.80` | 108,250,000.00 USD | 108,250,000.00 USD | 0.00 USD | 693,450.00 USD | 746,040.00 USD | 756,470.00 USD |
| `7D` | `105.80` | 290,420,000.00 USD | 290,420,000.00 USD | 0.00 USD | 3,560,000.00 USD | 3,410,000.00 USD | 4,360,000.00 USD |
| `1D` | `106.00` | 109,840,000.00 USD | 109,840,000.00 USD | 0.00 USD | 460,610.00 USD | 552,510.00 USD | 576,590.00 USD |
| `7D` | `106.00` | 302,020,000.00 USD | 302,020,000.00 USD | 0.00 USD | 4,740,000.00 USD | 3,150,000.00 USD | 3,710,000.00 USD |
| `1D` | `106.20` | 112,530,000.00 USD | 112,530,000.00 USD | 0.00 USD | 1,280,000.00 USD | 675,100.00 USD | 740,340.00 USD |
| `7D` | `106.20` | 316,520,000.00 USD | 316,520,000.00 USD | 0.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,970,000.00 USD |
| `1D` | `106.40` | 114,590,000.00 USD | 114,590,000.00 USD | 0.00 USD | 918,780.00 USD | 500,580.00 USD | 640,280.00 USD |
| `7D` | `106.40` | 325,030,000.00 USD | 325,030,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 2,250,000.00 USD |
| `1D` | `106.60` | 117,350,000.00 USD | 117,350,000.00 USD | 0.00 USD | 957,870.00 USD | 536,470.00 USD | 1,260,000.00 USD |
| `7D` | `106.60` | 334,240,000.00 USD | 334,240,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD |
| `1D` | `106.80` | 119,350,000.00 USD | 119,350,000.00 USD | 0.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD |
| `7D` | `106.80` | 340,120,000.00 USD | 340,120,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD |
| `1D` | `107.00` | 120,330,000.00 USD | 120,330,000.00 USD | 0.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD |
| `7D` | `107.00` | 345,680,000.00 USD | 345,680,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD |
| `1D` | `107.20` | 120,710,000.00 USD | 120,710,000.00 USD | 0.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD |
| `7D` | `107.20` | 347,400,000.00 USD | 347,400,000.00 USD | 0.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD |
| `1D` | `107.40` | 121,190,000.00 USD | 121,190,000.00 USD | 0.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD |
| `7D` | `107.40` | 348,390,000.00 USD | 348,390,000.00 USD | 0.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD |
| `1D` | `107.60` | 121,680,000.00 USD | 121,680,000.00 USD | 0.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD |
| `7D` | `107.60` | 349,040,000.00 USD | 349,040,000.00 USD | 0.00 USD | 498,090.00 USD | 0.00 USD | 154,920.00 USD |
| `1D` | `107.80` | 121,990,000.00 USD | 121,990,000.00 USD | 0.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD |
| `7D` | `107.80` | 350,100,000.00 USD | 350,100,000.00 USD | 0.00 USD | 499,750.00 USD | 203,950.00 USD | 357,890.00 USD |
| `7D` | `108.00` | 350,730,000.00 USD | 350,730,000.00 USD | 0.00 USD | 293,270.00 USD | 252,740.00 USD | 82,880.00 USD |
| `7D` | `108.20` | 353,140,000.00 USD | 353,140,000.00 USD | 0.00 USD | 966,370.00 USD | 938,650.00 USD | 503,200.00 USD |
| `7D` | `108.40` | 355,630,000.00 USD | 355,630,000.00 USD | 0.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD |
| `7D` | `108.60` | 357,050,000.00 USD | 357,050,000.00 USD | 0.00 USD | 401,600.00 USD | 515,740.00 USD | 505,810.00 USD |
| `7D` | `108.80` | 359,730,000.00 USD | 359,730,000.00 USD | 0.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD |
| `1D` | `109.00` | 121,990,000.00 USD | 121,990,000.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `109.00` | 360,270,000.00 USD | 360,270,000.00 USD | 0.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD |
| `1D` | `109.20` | 122,010,000.00 USD | 122,010,000.00 USD | 0.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD |
| `7D` | `109.20` | 361,490,000.00 USD | 361,490,000.00 USD | 0.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD |
| `1D` | `109.40` | 122,130,000.00 USD | 122,130,000.00 USD | 0.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD |
| `7D` | `109.40` | 361,820,000.00 USD | 361,820,000.00 USD | 0.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD |
| `1D` | `109.60` | 122,790,000.00 USD | 122,790,000.00 USD | 0.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD |
| `7D` | `109.60` | 362,890,000.00 USD | 362,890,000.00 USD | 0.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD |
| `1D` | `109.80` | 123,820,000.00 USD | 123,820,000.00 USD | 0.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD |
| `7D` | `109.80` | 363,870,000.00 USD | 363,870,000.00 USD | 0.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `1D` | `110.00` | 124,890,000.00 USD | 124,890,000.00 USD | 0.00 USD | 213,690.00 USD | 401,420.00 USD | 453,270.00 USD |
| `7D` | `110.00` | 365,590,000.00 USD | 365,590,000.00 USD | 0.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `1D` | `110.20` | 125,760,000.00 USD | 125,760,000.00 USD | 0.00 USD | 228,950.00 USD | 389,380.00 USD | 250,700.00 USD |
| `7D` | `110.20` | 367,590,000.00 USD | 367,590,000.00 USD | 0.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD |
| `1D` | `110.40` | 126,640,000.00 USD | 126,640,000.00 USD | 0.00 USD | 277,830.00 USD | 269,600.00 USD | 337,940.00 USD |
| `7D` | `110.40` | 368,990,000.00 USD | 368,990,000.00 USD | 0.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `110.60` | 127,060,000.00 USD | 127,060,000.00 USD | 0.00 USD | 110,850.00 USD | 71,980.00 USD | 239,910.00 USD |
| `7D` | `110.60` | 370,090,000.00 USD | 370,090,000.00 USD | 0.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD |
| `1D` | `110.80` | 127,740,000.00 USD | 127,740,000.00 USD | 0.00 USD | 155,280.00 USD | 287,250.00 USD | 237,370.00 USD |
| `7D` | `110.80` | 372,110,000.00 USD | 372,110,000.00 USD | 0.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD |
| `1D` | `111.00` | 127,880,000.00 USD | 127,880,000.00 USD | 0.00 USD | 34,430.00 USD | 101,090.00 USD | 319.18 USD |
| `7D` | `111.00` | 375,070,000.00 USD | 375,070,000.00 USD | 0.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `111.20` | 128,010,000.00 USD | 128,010,000.00 USD | 0.00 USD | 58,160.00 USD | 523.35 USD | 75,500.00 USD |
| `7D` | `111.20` | 377,110,000.00 USD | 377,110,000.00 USD | 0.00 USD | 1,170,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `111.40` | 128,050,000.00 USD | 128,050,000.00 USD | 0.00 USD | 37,090.00 USD | 2,670.00 USD | 685.66 USD |
| `7D` | `111.40` | 379,440,000.00 USD | 379,440,000.00 USD | 0.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `111.60` | 128,410,000.00 USD | 128,410,000.00 USD | 0.00 USD | 23,090.00 USD | 147,570.00 USD | 184,010.00 USD |
| `7D` | `111.60` | 380,400,000.00 USD | 380,400,000.00 USD | 0.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD |
| `1D` | `111.80` | 128,810,000.00 USD | 128,810,000.00 USD | 0.00 USD | 189,110.00 USD | 81,270.00 USD | 131,510.00 USD |
| `7D` | `111.80` | 382,760,000.00 USD | 382,760,000.00 USD | 0.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD |
| `1D` | `112.00` | 129,130,000.00 USD | 129,130,000.00 USD | 0.00 USD | 56,690.00 USD | 192,290.00 USD | 73,600.00 USD |
| `7D` | `112.00` | 384,390,000.00 USD | 384,390,000.00 USD | 0.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `112.20` | 129,840,000.00 USD | 129,840,000.00 USD | 0.00 USD | 369,020.00 USD | 218,430.00 USD | 123,590.00 USD |
| `7D` | `112.20` | 386,590,000.00 USD | 386,590,000.00 USD | 0.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `112.40` | 130,310,000.00 USD | 130,310,000.00 USD | 0.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD |
| `7D` | `112.40` | 388,330,000.00 USD | 388,330,000.00 USD | 0.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `112.60` | 130,760,000.00 USD | 130,760,000.00 USD | 0.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD |
| `7D` | `112.60` | 389,190,000.00 USD | 389,190,000.00 USD | 0.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `112.80` | 131,200,000.00 USD | 131,200,000.00 USD | 0.00 USD | 16,000.00 USD | 63,410.00 USD | 364,110.00 USD |
| `7D` | `112.80` | 390,060,000.00 USD | 390,060,000.00 USD | 0.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD |
| `1D` | `113.00` | 131,800,000.00 USD | 131,800,000.00 USD | 0.00 USD | 135,210.00 USD | 46,900.00 USD | 418,590.00 USD |
| `7D` | `113.00` | 391,100,000.00 USD | 391,100,000.00 USD | 0.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD |
| `1D` | `113.20` | 132,060,000.00 USD | 132,060,000.00 USD | 0.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD |
| `7D` | `113.20` | 392,180,000.00 USD | 392,180,000.00 USD | 0.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `113.40` | 132,210,000.00 USD | 132,210,000.00 USD | 0.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD |
| `7D` | `113.40` | 392,410,000.00 USD | 392,410,000.00 USD | 0.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `1D` | `113.60` | 132,380,000.00 USD | 132,380,000.00 USD | 0.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD |
| `7D` | `113.60` | 392,800,000.00 USD | 392,800,000.00 USD | 0.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.80` | 392,800,000.00 USD | 392,800,000.00 USD | 0.00 USD | 6,570.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.30B` | Total OI Tokens: `62,054,767.3 SOL`
  * 1h OI Change: `-0.91%` | 4h OI Change: `-2.30%` | 24h OI Change: `-1.33%`
  * Exchange Breakdown: Binance=`1.10B` | Bybit=`627.41M` | OKX=`358.69M` | Hyperliquid=`571.57M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `197.04K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `49.97%` | `50.03%` | `1.00` | 782,520,000.00 USD |
| `15M` | `Binance` | `39.94%` | `60.06%` | `0.67` | 223,710,000.00 USD |
| `15M` | `OKX` | `52.03%` | `47.97%` | `1.08` | 119,850,000.00 USD |
| `15M` | `Bybit` | `50.74%` | `49.26%` | `1.03` | 56,010,000.00 USD |
| `15M` | `KuCoin` | `52.38%` | `47.62%` | `1.10` | 1,970,000.00 USD |
| `15M` | `Gate` | `48.19%` | `51.81%` | `0.93` | 105,090,000.00 USD |
| `15M` | `Bitget` | `46.48%` | `53.52%` | `0.87` | 43,030,000.00 USD |
| `15M` | `BingX` | `68.68%` | `31.32%` | `2.19` | 13,260,000.00 USD |
| `15M` | `MEXC` | `49.44%` | `50.56%` | `0.98` | 50,010,000.00 USD |
| `15M` | `Bitunix` | `53.63%` | `46.37%` | `1.16` | 31,880,000.00 USD |
| `15M` | `Hyperliquid` | `67.26%` | `32.74%` | `2.05` | 61,820,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `77.22%` | `22.78%` | `3.39` | 5,780,000.00 USD |
| `15M` | `Crypto.com` | `50.42%` | `49.58%` | `1.02` | 8,710,000.00 USD |
| `15M` | `WhiteBIT` | `82.43%` | `17.57%` | `4.69` | 19,760,000.00 USD |
| `15M` | `HTX` | `57.42%` | `42.58%` | `1.35` | 2,350,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `55.17%` | `44.83%` | `1.23` | 15,840,000.00 USD |
| `15M` | `Bitfinex` | `39.81%` | `60.19%` | `0.66` | 381,670.00 USD |
| `15M` | `Kraken` | `63.96%` | `36.04%` | `1.77` | 3,440,000.00 USD |
| `15M` | `Aster` | `43.17%` | `56.83%` | `0.76` | 7,810,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `48.86%` | `51.14%` | `0.96` | 11,810,000.00 USD |
| `15M` | `Whale Positions` | `39.94%` | `60.06%` | `0.67` | 223,710,000.00 USD |
| `15M` | `Global Accounts` | `49.97%` | `50.03%` | `1.00` | 782,520,000.00 USD |
| `1H` | `SOL` | `45.24%` | `54.76%` | `0.83` | 1,590,000,000.00 USD |
| `1H` | `Binance` | `42.5%` | `57.5%` | `0.74` | 511,730,000.00 USD |
| `1H` | `OKX` | `49.08%` | `50.92%` | `0.96` | 259,460,000.00 USD |
| `1H` | `Bybit` | `43.19%` | `56.81%` | `0.76` | 112,230,000.00 USD |
| `1H` | `KuCoin` | `37.15%` | `62.85%` | `0.59` | 4,930,000.00 USD |
| `1H` | `Gate` | `47.14%` | `52.86%` | `0.89` | 268,630,000.00 USD |
| `1H` | `Bitget` | `44.56%` | `55.44%` | `0.80` | 87,830,000.00 USD |
| `1H` | `BingX` | `36.24%` | `63.76%` | `0.57` | 24,110,000.00 USD |
| `1H` | `MEXC` | `52.35%` | `47.65%` | `1.10` | 76,540,000.00 USD |
| `1H` | `Bitunix` | `46.95%` | `53.05%` | `0.89` | 57,910,000.00 USD |
| `1H` | `Hyperliquid` | `36.95%` | `63.05%` | `0.59` | 43,360,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `43.78%` | `56.22%` | `0.78` | 4,160,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `59.06%` | `40.94%` | `1.44` | 52,370,000.00 USD |
| `1H` | `HTX` | `26.41%` | `73.59%` | `0.36` | 18,360,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.58%` | `50.42%` | `0.98` | 11,220,000.00 USD |
| `1H` | `Bitfinex` | `14.44%` | `85.56%` | `0.17` | 574,590.00 USD |
| `1H` | `Kraken` | `29.74%` | `70.26%` | `0.42` | 6,410,000.00 USD |
| `1H` | `Aster` | `27.61%` | `72.39%` | `0.38` | 20,240,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.47%` | `48.53%` | `1.06` | 31,930,000.00 USD |
| `1H` | `Whale Positions` | `42.5%` | `57.5%` | `0.74` | 511,730,000.00 USD |
| `1H` | `Global Accounts` | `45.24%` | `54.76%` | `0.83` | 1,590,000,000.00 USD |
| `4H` | `SOL` | `50.24%` | `49.76%` | `1.01` | 21,140,000,000.00 USD |
| `4H` | `Binance` | `49.63%` | `50.37%` | `0.99` | 6,710,000,000.00 USD |
| `4H` | `OKX` | `50.02%` | `49.98%` | `1.00` | 3,060,000,000.00 USD |
| `4H` | `Bybit` | `49.55%` | `50.45%` | `0.98` | 2,100,000,000.00 USD |
| `4H` | `KuCoin` | `47.94%` | `52.06%` | `0.92` | 83,220,000.00 USD |
| `4H` | `Gate` | `50.17%` | `49.83%` | `1.01` | 2,510,000,000.00 USD |
| `4H` | `Bitget` | `49.54%` | `50.46%` | `0.98` | 1,270,000,000.00 USD |
| `4H` | `BingX` | `49.9%` | `50.1%` | `1.00` | 385,850,000.00 USD |
| `4H` | `MEXC` | `54.13%` | `45.87%` | `1.18` | 1,160,000,000.00 USD |
| `4H` | `Bitunix` | `47.88%` | `52.12%` | `0.92` | 1,060,000,000.00 USD |
| `4H` | `Hyperliquid` | `53.3%` | `46.7%` | `1.14` | 976,630,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.65%` | `50.35%` | `0.99` | 134,580,000.00 USD |
| `4H` | `Crypto.com` | `47.92%` | `52.08%` | `0.92` | 139,200,000.00 USD |
| `4H` | `WhiteBIT` | `56.97%` | `43.03%` | `1.32` | 371,800,000.00 USD |
| `4H` | `HTX` | `47.21%` | `52.79%` | `0.89` | 85,040,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.22%` | `48.78%` | `1.05` | 412,820,000.00 USD |
| `4H` | `Bitfinex` | `65.95%` | `34.05%` | `1.94` | 29,080,000.00 USD |
| `4H` | `Kraken` | `53.09%` | `46.91%` | `1.13` | 162,550,000.00 USD |
| `4H` | `Aster` | `48.04%` | `51.96%` | `0.92` | 227,460,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.19%` | `49.81%` | `1.01` | 265,600,000.00 USD |
| `4H` | `Whale Positions` | `49.63%` | `50.37%` | `0.99` | 6,710,000,000.00 USD |
| `4H` | `Global Accounts` | `50.24%` | `49.76%` | `1.01` | 21,140,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `102.09` | `102.15` | `102.09` | `102.56` | `101.97` | 23,640,474.20 USD | 10,806,979.58 USD | 12,833,494.61 USD | -2,026,515.03 USD | `-8.57%` | `3B / 15S` |
| `0:00 UTC` | `102.35` | `102.36` | `102.35` | `102.59` | `102.00` | 23,533,351.35 USD | 13,604,014.33 USD | 9,929,337.03 USD | 3,674,677.30 USD | `+15.61%` | `11B / 7S` |
| `5:00 UTC` | `102.50` | `102.51` | `102.50` | `102.70` | `102.32` | 23,288,646.41 USD | 10,642,310.31 USD | 12,646,336.10 USD | -2,004,025.79 USD | `-8.61%` | `2B / 8S` |
| `0:00 UTC` | `102.63` | `102.77` | `102.63` | `103.16` | `102.38` | 44,107,518.93 USD | 20,981,384.68 USD | 23,126,134.25 USD | -2,144,749.57 USD | `-4.86%` | `8B / 10S` |
| `5:00 UTC` | `102.31` | `102.32` | `102.31` | `102.66` | `102.10` | 27,443,327.62 USD | 11,049,929.69 USD | 16,393,397.93 USD | -5,343,468.24 USD | `-19.47%` | `1B / 16S` |
| `0:00 UTC` | `102.00` | `102.00` | `102.00` | `102.22` | `101.81` | 25,493,228.16 USD | 11,241,280.68 USD | 14,251,947.48 USD | -3,010,666.79 USD | `-11.81%` | `2B / 10S` |
| `5:00 UTC` | `101.94` | `101.88` | `101.94` | `102.02` | `101.75` | 15,546,239.68 USD | 7,009,090.38 USD | 8,537,149.31 USD | -1,528,058.93 USD | `-9.83%` | `0B / 1S` |
| `0:00 UTC` | `101.70` | `101.72` | `101.70` | `101.94` | `101.53` | 20,486,970.74 USD | 7,002,058.55 USD | 13,484,912.18 USD | -6,482,853.63 USD | `-31.64%` | `0B / 15S` |
| `5:00 UTC` | `101.65` | `101.65` | `101.65` | `101.78` | `101.53` | 12,871,901.66 USD | 6,991,731.87 USD | 5,880,169.78 USD | 1,111,562.09 USD | `+8.64%` | `1B / 2S` |
| `0:00 UTC` | `101.66` | `101.65` | `101.66` | `101.77` | `101.55` | 2,162,629.11 USD | 842,799.42 USD | 1,319,829.69 USD | -477,030.26 USD | `-22.06%` | `5B / 7S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 416,920.00 USD | 1,820,000.00 USD | **`ACCUMULATION`** |
| `15m` | 255,660.00 USD | -1,320,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,290,000.00 USD | -13,870,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,360,000.00 USD | -29,170,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 3,480,000.00 USD | -32,970,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 14,050,000.00 USD | -2,580,000.00 USD | **`ACCUMULATION`** |
| `6h` | 14,630,000.00 USD | -33,080,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 15,370,000.00 USD | -29,560,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 25,140,000.00 USD | -44,230,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 44,100,000.00 USD | -87,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 88,100,000.00 USD | -274,120,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 67,290,000.00 USD | -1,860,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+416.92K` | 15m=`+255.66K` | 1h=`-2.36M` | 24h=`+44.10M`
* Futures Capital Netflows: 5m=`+1.82M` | 15m=`-1.32M` | 1h=`-29.17M` | 24h=`-87.85M`
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
  * Execution Entry: `98.96` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `97.38` (Risk Distance: `1.58` pts)
  * +2.5R Take Profit: `102.90`
  * Mathematical Lot Sizing: **`6.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.35` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.92` (Risk Distance: `1.58` pts)
  * +2.5R Take Profit: `97.41`
  * Mathematical Lot Sizing: **`6.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`102.36`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
