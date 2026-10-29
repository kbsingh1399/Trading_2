# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:32:19 IST` (`2026-10-29 19:02:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `100.49` | **Live Ask Quote**: `100.73` | **Mid Price**: `100.61`
- **Spread Points**: `24.00` | **Spread BPS**: `23.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `100.43` | VWAP Z-Score: `-0.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4959` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `38.39` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.03` | Lower -3.00σ Band: `97.83`
  * Upper +2.51σ Band: `102.60` | Lower -2.51σ Band: `98.26`
  * Upper +2.01σ Band: `102.17` | Lower -2.01σ Band: `98.69`
  * Upper +2.00σ Band: `102.16` | Lower -2.00σ Band: `98.70`
  * Upper +1.28σ Band: `101.54` | Lower -1.28σ Band: `99.32`
  * Upper +1.00σ Band: `101.30` | Lower -1.00σ Band: `99.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`100.92` | EMA-20=`101.04` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.83` (Slope: `+0.0000`) | EMA-100=`100.82`
  * Institutional Anchors: EMA-144=`100.83` | EMA-200=`100.78` (Slope: `+0.0678`) | EMA-233=`100.72`
- **Range Boundaries**: 24H High=`103.63` | 24H Low=`98.95` | Weekly High=`103.63` | Weekly Low=`98.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.32` (Distance: `-0.72%`)
  * Point of Control (POC) = `99.92` (Distance: `+0.68%`)
  * Value Area Low (VAL) = `99.18` (Distance: `+1.43%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `100.21` - `101.01`
  * Optimal Trade Entry (OTE 0.705): `100.81`
  * Structural Invalidation Anchor (0.786): `101.41`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.42` | `100.45` | `100.29` | `100.45` | `35,456` | 3,558,884.70 USD | 101,878.58 USD | `+2.86%` | -72,740,712.71 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `100.44` | `100.50` | `100.33` | `100.47` | `29,664` | 2,978,960.26 USD | -387,227.30 USD | `-13.00%` | -73,127,940.02 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `100.48` | `100.73` | `100.47` | `100.71` | `44,447` | 4,472,617.10 USD | 1,519,461.70 USD | `+33.97%` | -71,608,478.32 USD | `+1.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.10` | `101.17` | `100.75` | `100.79` | `76,073` | 7,681,327.85 USD | -601,405.98 USD | `-7.83%` | -64,623,473.63 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `100.78` | `100.80` | `100.29` | `100.45` | `266,327` | 26,755,803.01 USD | -7,312,826.00 USD | `-27.33%` | -71,936,299.63 USD | `-1.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `100.44` | `100.73` | `100.33` | `100.73` | `73,977` | 7,438,039.97 USD | 1,145,362.83 USD | `+15.40%` | -70,790,936.81 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.66` | `103.16` | `101.75` | `101.86` | `1,100,013` | 112,591,915.90 USD | -12,028,545.03 USD | `-10.68%` | -51,660,705.06 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `101.87` | `101.93` | `100.71` | `101.06` | `773,410` | 78,387,335.50 USD | -11,810,112.06 USD | `-15.07%` | -63,470,817.13 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.06` | `101.18` | `100.29` | `100.71` | `533,768` | 53,734,599.06 USD | -7,333,248.12 USD | `-13.65%` | -70,804,065.24 USD | `-0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.29` | `100.71` | `2,407,191` | 244,713,850.46 USD | -31,171,905.21 USD | `-12.74%` | -75,040,548.42 USD | `-1.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.37` | `102.50` | `99.16` | `99.64` | `3,450,297` | 345,810,531.49 USD | -35,022,306.76 USD | `-10.13%` | -43,673,756.58 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -38,017,362.01 USD | `+1.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.29` | `100.71` | `2,407,191` | 244,713,850.46 USD | -31,171,905.21 USD | `-12.74%` | -75,040,548.42 USD | `-1.23` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`100.61`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `100.55` | `467.9100` | 47,048.35 USD | 6,235,915.37 USD | `4 orders` | `-0.19%` | `-` |
| `BID` | `100.56` | `1136.7500` | 114,311.58 USD | 6,188,867.02 USD | `10 orders` | `-0.18%` | `-` |
| `BID` | `100.57` | `3596.8100` | 361,731.18 USD | 6,074,555.44 USD | `8 orders` | `-0.17%` | `-` |
| `BID` | `100.58` | `2797.5600` | 281,378.58 USD | 5,712,824.26 USD | `12 orders` | `-0.16%` | `-` |
| `BID` | `100.59` | `4017.2900` | 404,099.20 USD | 5,431,445.68 USD | `11 orders` | `-0.15%` | `-` |
| `BID` | `100.60` | `5425.4600` | 545,801.28 USD | 5,027,346.48 USD | `18 orders` | `-0.14%` | `-` |
| `BID` | `100.61` | `4468.0600` | 449,531.52 USD | 4,481,545.20 USD | `12 orders` | `-0.13%` | `-` |
| `BID` | `100.62` | `4690.2000` | 471,927.92 USD | 4,032,013.68 USD | `15 orders` | `-0.12%` | `-` |
| `BID` | `100.63` | `4413.7000` | 444,150.63 USD | 3,560,085.76 USD | `17 orders` | `-0.11%` | `-` |
| `BID` | `100.64` | `3657.9900` | 368,140.11 USD | 3,115,935.13 USD | `21 orders` | `-0.10%` | `-` |
| `BID` | `100.65` | `5230.8800` | 526,488.07 USD | 2,747,795.01 USD | `14 orders` | `-0.09%` | `-` |
| `BID` | `100.66` | `2604.5800` | 262,177.02 USD | 2,221,306.94 USD | `17 orders` | `-0.08%` | `-` |
| `BID` | `100.67` | `7223.6800` | 727,207.87 USD | 1,959,129.92 USD | `21 orders` | `-0.07%` | `-` |
| `BID` | `100.68` | `1250.8900` | 125,939.61 USD | 1,231,922.05 USD | `17 orders` | `-0.06%` | `-` |
| `BID` | `100.69` | `4592.5700` | 462,425.87 USD | 1,105,982.45 USD | `25 orders` | `-0.05%` | `-` |
| `BID` | `100.70` | `2204.8500` | 222,028.39 USD | 643,556.58 USD | `31 orders` | `-0.04%` | `-` |
| `BID` | `100.71` | `2712.4700` | 273,172.85 USD | 421,528.18 USD | `19 orders` | `-0.03%` | `-` |
| `BID` | `100.72` | `951.1900` | 95,803.86 USD | 148,355.33 USD | `14 orders` | `-0.02%` | `-` |
| `BID` | `100.73` | `358.0300` | 36,064.36 USD | 52,551.47 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `100.74` | `163.6600` | 16,487.11 USD | 16,487.11 USD | `6 orders` | `-0.00%` | `-` |
| `ASK` | `100.75` | `1540.3000` | 155,185.23 USD | 155,185.23 USD | `43 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `100.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 100.75` | `0.00%` | `-` |
| `ASK` | `100.76` | `2209.9600` | 222,675.57 USD | 377,860.79 USD | `27 orders` | `+0.01%` | `-` |
| `ASK` | `100.77` | `2571.4300` | 259,123.00 USD | 636,983.80 USD | `23 orders` | `+0.02%` | `-` |
| `ASK` | `100.78` | `3558.3100` | 358,606.48 USD | 995,590.28 USD | `33 orders` | `+0.03%` | `-` |
| `ASK` | `100.79` | `3140.1300` | 316,493.70 USD | 1,312,083.98 USD | `21 orders` | `+0.04%` | `-` |
| `ASK` | `100.80` | `3289.7100` | 331,602.77 USD | 1,643,686.75 USD | `27 orders` | `+0.05%` | `-` |
| `ASK` | `100.81` | `3359.2600` | 338,647.00 USD | 1,982,333.75 USD | `28 orders` | `+0.06%` | `-` |
| `ASK` | `100.82` | `1371.8400` | 138,308.91 USD | 2,120,642.66 USD | `15 orders` | `+0.07%` | `-` |
| `ASK` | `100.83` | `2539.8800` | 256,096.10 USD | 2,376,738.76 USD | `17 orders` | `+0.08%` | `-` |
| `ASK` | `100.84` | `2097.1800` | 211,479.63 USD | 2,588,218.39 USD | `15 orders` | `+0.09%` | `-` |
| `ASK` | `100.85` | `3005.7000` | 303,124.84 USD | 2,891,343.23 USD | `19 orders` | `+0.10%` | `-` |
| `ASK` | `100.86` | `2814.1700` | 283,837.19 USD | 3,175,180.42 USD | `16 orders` | `+0.11%` | `-` |
| `ASK` | `100.87` | `2941.1600` | 296,674.81 USD | 3,471,855.23 USD | `18 orders` | `+0.12%` | `-` |
| `ASK` | `100.88` | `1866.3300` | 188,275.37 USD | 3,660,130.60 USD | `10 orders` | `+0.13%` | `-` |
| `ASK` | `100.89` | `2840.1300` | 286,540.72 USD | 3,946,671.32 USD | `14 orders` | `+0.14%` | `-` |
| `ASK` | `100.90` | `5027.1800` | 507,242.46 USD | 4,453,913.78 USD | `13 orders` | `+0.15%` | `-` |
| `ASK` | `100.91` | `2327.1800` | 234,835.73 USD | 4,688,749.51 USD | `9 orders` | `+0.16%` | `-` |
| `ASK` | `100.92` | `2037.8300` | 205,657.80 USD | 4,894,407.32 USD | `14 orders` | `+0.17%` | `-` |
| `ASK` | `100.93` | `536.7200` | 54,171.15 USD | 4,948,578.46 USD | `6 orders` | `+0.18%` | `-` |
| `ASK` | `100.94` | `5007.8600` | 505,493.39 USD | 5,454,071.85 USD | `11 orders` | `+0.19%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 72,679,034.90 USD | `721,165.26` | `94.33` | `100.80` | `316.28` | -4,648,144.49 USD | `-6.40%` | `7X Cross` |
| `21` | `0x9c6a...a4ed` | `LONG` | 55,421,334.77 USD | `550,087.69` | `80.86` | `100.80` | `68.17` | 10,942,348.38 USD | `+19.74%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 26,119,291.01 USD | `259,300.02` | `91.42` | `100.80` | `607.70` | -2,414,158.00 USD | `-9.24%` | `5X Cross` |
| `79` | `0x3dc9...54b0` | `SHORT` | 22,160,619.14 USD | `220,000.19` | `105.90` | `100.80` | `165.19` | 1,138,488.14 USD | `+5.14%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 19,079,880.75 USD | `189,472.50` | `115.21` | `100.80` | `34.72` | -2,749,134.51 USD | `-14.41%` | `20X Cross` |
| `113` | `0x4a20...3c26` | `LONG` | 18,127,800.00 USD | `180,000.00` | `106.43` | `100.80` | `65.59` | -1,030,478.71 USD | `-5.68%` | `20X Cross` |
| `136` | `0xecb6...2b00` | `SHORT` | 15,072,658.27 USD | `149,530.34` | `102.73` | `100.80` | `281.73` | 288,356.17 USD | `+1.91%` | `20X Cross` |
| `226` | `0x7a5a...0394` | `SHORT` | 10,117,599.52 USD | `100,462.71` | `100.92` | `100.80` | `126.91` | 20,694.72 USD | `+0.20%` | `10X Cross` |
| `228` | `0xc63a...a3cd` | `LONG` | 10,070,000.00 USD | `100,000.00` | `112.22` | `100.80` | `0.000000` | -1,152,108.97 USD | `-11.44%` | `20X Cross` |
| `244` | `0x13da...08be` | `LONG` | 9,639,084.02 USD | `95,711.29` | `100.55` | `100.80` | `98.09` | 15,343.34 USD | `+0.16%` | `20X Isolated` |
| `267` | `0xb581...6f4f` | `LONG` | 9,064,800.00 USD | `90,000.00` | `114.59` | `100.80` | `0.000000` | -1,248,492.29 USD | `-13.77%` | `3X Cross` |
| `289` | `0x645b...87b8` | `SHORT` | 8,423,232.97 USD | `83,605.29` | `103.91` | `100.80` | `331.15` | 263,896.20 USD | `+3.13%` | `20X Cross` |
| `298` | `0xdb3a...cf3b` | `LONG` | 8,244,929.80 USD | `81,851.78` | `106.04` | `100.80` | `45.99` | -434,817.06 USD | `-5.27%` | `4X Cross` |
| `315` | `0xe927...98ef` | `LONG` | 7,856,940.00 USD | `78,000.00` | `96.34` | `100.80` | `38.44` | 342,798.52 USD | `+4.36%` | `3X Cross` |
| `323` | `0xca49...53c8` | `SHORT` | 7,446,105.42 USD | `73,943.45` | `110.70` | `100.80` | `274.42` | 739,516.85 USD | `+9.93%` | `20X Cross` |
| `327` | `0x8ae4...3d60` | `LONG` | 7,269,252.84 USD | `72,180.05` | `111.72` | `100.80` | `2.04` | -794,907.40 USD | `-10.94%` | `10X Cross` |
| `334` | `0xa0b7...6165` | `SHORT` | 7,157,725.32 USD | `71,044.42` | `107.87` | `100.80` | `190.90` | 505,741.88 USD | `+7.07%` | `2X Cross` |
| `349` | `0xf517...c032` | `SHORT` | 6,826,673.88 USD | `67,778.53` | `84.64` | `100.80` | `232.27` | -1,089,642.71 USD | `-15.96%` | `20X Cross` |
| `476` | `0x7e23...5a5a` | `LONG` | 4,891,908.13 USD | `48,564.56` | `105.17` | `100.80` | `78.11` | -215,661.03 USD | `-4.41%` | `5X Isolated` |
| `576` | `0x2e2b...2fab` | `LONG` | 4,029,200.00 USD | `40,000.00` | `119.55` | `100.80` | `53.41` | -752,835.64 USD | `-18.68%` | `10X Cross` |
| `581` | `0x7fda...17d1` | `SHORT` | 4,006,399.76 USD | `39,773.65` | `103.76` | `100.80` | `988.85` | 120,465.85 USD | `+3.01%` | `20X Cross` |
| `601` | `0xf899...88db` | `SHORT` | 3,888,724.29 USD | `38,586.27` | `87.86` | `100.80` | `117.03` | -498,349.10 USD | `-12.82%` | `20X Cross` |
| `614` | `0x9946...0852` | `SHORT` | 3,805,696.39 USD | `37,784.80` | `112.11` | `100.80` | `129.27` | 430,530.92 USD | `+11.31%` | `20X Cross` |
| `642` | `0x27b8...12fc` | `LONG` | 3,634,193.87 USD | `36,085.73` | `110.86` | `100.80` | `14.36` | -366,151.39 USD | `-10.08%` | `10X Cross` |
| `646` | `0x9c16...4a6f` | `SHORT` | 3,602,960.40 USD | `35,779.15` | `90.45` | `100.80` | `128.61` | -366,855.38 USD | `-10.18%` | `20X Cross` |
| `652` | `0x3440...32c5` | `SHORT` | 3,578,503.63 USD | `35,529.12` | `95.02` | `100.80` | `167.86` | -202,482.19 USD | `-5.66%` | `20X Cross` |
| `727` | `0x96a7...79df` | `LONG` | 3,223,360.00 USD | `32,000.00` | `74.39` | `100.80` | `0.000000` | 842,954.15 USD | `+26.15%` | `20X Cross` |
| `735` | `0x023a...2355` | `SHORT` | 3,190,212.78 USD | `31,670.93` | `101.47` | `100.80` | `359.08` | 23,401.00 USD | `+0.73%` | `20X Cross` |
| `772` | `0xbe19...8bd1` | `SHORT` | 3,066,789.70 USD | `30,451.69` | `97.62` | `100.80` | `731.31` | -94,243.07 USD | `-3.07%` | `3X Cross` |
| `776` | `0x482b...cae4` | `SHORT` | 3,052,569.45 USD | `30,310.49` | `88.03` | `100.80` | `156.70` | -384,321.16 USD | `-12.59%` | `20X Cross` |
| `786` | `0x610b...b613` | `LONG` | 2,985,046.92 USD | `29,634.14` | `101.23` | `100.80` | `70.38` | -14,952.43 USD | `-0.50%` | `3X Isolated` |
| `800` | `0x45d2...4029` | `SHORT` | 2,942,454.00 USD | `29,220.00` | `93.28` | `100.80` | `1349.50` | -216,678.02 USD | `-7.36%` | `20X Cross` |
| `805` | `0xfc66...ca06` | `SHORT` | 2,926,667.85 USD | `29,060.35` | `102.20` | `100.80` | `1307.87` | 43,230.73 USD | `+1.48%` | `20X Cross` |
| `810` | `0xa61c...66b9` | `LONG` | 2,909,888.24 USD | `28,888.00` | `104.39` | `100.80` | `0.000000` | -105,675.88 USD | `-3.63%` | `5X Cross` |
| `847` | `0x458d...ab3b` | `LONG` | 2,758,494.07 USD | `27,385.03` | `117.17` | `100.80` | `81.07` | -450,168.45 USD | `-16.32%` | `3X Isolated` |
| `880` | `0xfc27...9d9d` | `SHORT` | 2,598,185.30 USD | `25,793.56` | `102.76` | `100.80` | `654.84` | 52,302.50 USD | `+2.01%` | `20X Cross` |
| `908` | `0x051c...693c` | `LONG` | 2,532,321.98 USD | `25,139.70` | `89.76` | `100.80` | `23.36` | 275,760.65 USD | `+10.89%` | `20X Cross` |
| `947` | `0x638f...f5f0` | `LONG` | 2,416,800.00 USD | `24,000.00` | `136.71` | `100.80` | `42.38` | -864,168.54 USD | `-35.76%` | `20X Cross` |
| `1004` | `0x7178...0854` | `LONG` | 2,272,109.29 USD | `22,545.24` | `110.94` | `100.80` | `30.79` | -229,035.19 USD | `-10.08%` | `10X Cross` |
| `1029` | `0x739c...cfb2` | `LONG` | 2,216,060.00 USD | `22,000.00` | `91.95` | `100.80` | `71.98` | 193,152.69 USD | `+8.72%` | `20X Cross` |
| `1037` | `0x69cc...14fd` | `SHORT` | 2,185,782.13 USD | `21,701.57` | `99.01` | `100.80` | `455.69` | -37,129.38 USD | `-1.70%` | `20X Cross` |
| `1059` | `0xb90d...870c` | `SHORT` | 2,127,427.67 USD | `21,120.10` | `102.00` | `100.80` | `111.84` | 26,897.10 USD | `+1.26%` | `20X Cross` |
| `1103` | `0x7737...bf66` | `SHORT` | 2,054,305.57 USD | `20,384.06` | `102.94` | `100.80` | `987.70` | 44,036.32 USD | `+2.14%` | `10X Cross` |
| `1119` | `0xea00...a918` | `LONG` | 2,016,885.56 USD | `20,022.69` | `66.09` | `100.80` | `0.000000` | 693,576.96 USD | `+34.39%` | `20X Cross` |
| `1122` | `0x3fc5...c0c1` | `SHORT` | 2,014,600.00 USD | `20,000.00` | `98.28` | `100.80` | `202.99` | -49,040.16 USD | `-2.43%` | `20X Cross` |
| `1123` | `0xdf60...d3c7` | `LONG` | 2,014,600.00 USD | `20,000.00` | `120.12` | `100.80` | `94.00` | -387,808.53 USD | `-19.25%` | `7X Isolated` |
| `1124` | `0x5986...89d9` | `LONG` | 2,014,600.00 USD | `20,000.00` | `101.84` | `100.80` | `45.29` | -22,197.53 USD | `-1.10%` | `20X Cross` |
| `1126` | `0x251f...6e5d` | `LONG` | 2,014,406.00 USD | `20,000.00` | `101.15` | `100.80` | `46.32` | -8,691.77 USD | `-0.43%` | `20X Cross` |
| `1127` | `0xbfc7...80b4` | `SHORT` | 2,014,102.00 USD | `20,000.00` | `85.98` | `100.80` | `324.75` | -294,567.50 USD | `-14.63%` | `20X Cross` |
| `1145` | `0xb322...d51f` | `LONG` | 1,991,917.62 USD | `19,774.82` | `102.98` | `100.80` | `56.01` | -44,553.78 USD | `-2.24%` | `20X Cross` |
| `1156` | `0x34e6...8d74` | `LONG` | 1,982,588.65 USD | `19,688.07` | `101.19` | `100.80` | `53.20` | -9,575.15 USD | `-0.48%` | `20X Cross` |
| `1172` | `0x936c...bb0f` | `SHORT` | 1,959,332.26 USD | `19,437.82` | `105.65` | `100.80` | `635.10` | 94,182.12 USD | `+4.81%` | `20X Cross` |
| `1174` | `0x7160...d47c` | `LONG` | 1,957,408.38 USD | `19,434.10` | `105.03` | `100.80` | `80.29` | -83,812.91 USD | `-4.28%` | `20X Cross` |
| `1198` | `0xe097...d0fe` | `LONG` | 1,913,061.98 USD | `18,995.75` | `109.71` | `100.80` | `0.000000` | -170,934.91 USD | `-8.94%` | `20X Cross` |
| `1288` | `0xe98b...8cd5` | `SHORT` | 1,775,506.17 USD | `17,622.89` | `187.95` | `100.80` | `260.15` | 1,536,714.56 USD | `+86.55%` | `20X Cross` |
| `1298` | `0xdf95...7d72` | `SHORT` | 1,757,945.85 USD | `17,443.40` | `104.70` | `100.80` | `2207.64` | 68,317.81 USD | `+3.89%` | `20X Cross` |
| `1327` | `0xee2b...d67e` | `LONG` | 1,708,702.13 USD | `16,963.19` | `119.86` | `100.80` | `20.30` | -324,569.51 USD | `-19.00%` | `4X Cross` |
| `1335` | `0x123d...3bff` | `LONG` | 1,704,193.45 USD | `16,918.43` | `89.53` | `100.80` | `0.000000` | 189,406.97 USD | `+11.11%` | `10X Cross` |
| `1361` | `0x7277...0b98` | `SHORT` | 1,672,265.24 USD | `16,603.11` | `101.18` | `100.80` | `179.29` | 7,662.97 USD | `+0.46%` | `20X Cross` |
| `1443` | `0x73d7...8be1` | `LONG` | 1,577,863.26 USD | `15,668.95` | `106.60` | `100.80` | `70.94` | -92,477.70 USD | `-5.86%` | `20X Cross` |
| `1451` | `0xc74a...ab93` | `LONG` | 1,565,800.72 USD | `15,536.82` | `64.06` | `100.80` | `54.88` | 570,571.88 USD | `+36.44%` | `5X Isolated` |
| `1497` | `0xc7d1...51af` | `SHORT` | 1,510,950.00 USD | `15,000.00` | `105.79` | `100.80` | `138.76` | 75,925.00 USD | `+5.02%` | `20X Cross` |
| `1527` | `0xffb2...5ed6` | `LONG` | 1,460,557.83 USD | `14,504.05` | `117.89` | `100.80` | `89.38` | -249,346.88 USD | `-17.07%` | `20X Cross` |
| `1560` | `0x0d6a...ca57` | `LONG` | 1,431,035.85 USD | `14,206.65` | `110.41` | `100.80` | `91.59` | -137,554.50 USD | `-9.61%` | `5X Isolated` |
| `1833` | `0x2482...0e55` | `LONG` | 1,144,693.71 USD | `11,363.98` | `122.03` | `100.80` | `94.24` | -242,008.22 USD | `-21.14%` | `20X Isolated` |
| `1852` | `0xe105...6a47` | `LONG` | 1,128,576.00 USD | `11,205.05` | `107.11` | `100.80` | `92.13` | -71,581.06 USD | `-6.34%` | `20X Cross` |
| `1863` | `0x45db...86eb` | `LONG` | 1,117,771.11 USD | `11,100.00` | `110.69` | `100.80` | `67.96` | -110,910.79 USD | `-9.92%` | `5X Cross` |
| `1897` | `0x1d04...7c43` | `LONG` | 1,089,284.82 USD | `10,811.76` | `111.55` | `100.80` | `17.79` | -116,776.67 USD | `-10.72%` | `6X Cross` |
| `2017` | `0x0daf...47e0` | `SHORT` | 1,007,000.00 USD | `10,000.00` | `99.07` | `100.80` | `250.04` | -16,287.78 USD | `-1.62%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `130.74` | 1,361.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.36K USD at 130.7400 USD [API] | `2026-01-21 15:16:43` |
| `ANNOUNCEMENT` | `INFO` | `122.75` | 4,485.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.49K USD at 122.7500 USD [API] | `2025-12-23 13:36:37` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 3,751.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.75K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 820.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.82K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `126.81` | 3,182.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.18K USD at 126.8100 USD [API] | `2025-12-17 15:52:14` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,808.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.81K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,998.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,510.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.51K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `129.25` | 4,809.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.81K USD at 129.2500 USD [API] | `2025-12-14 23:27:00` |
| `ANNOUNCEMENT` | `INFO` | `134.26` | 5,544.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.54K USD at 134.2600 USD [API] | `2025-12-11 18:35:47` |
| `ANNOUNCEMENT` | `INFO` | `128.92` | 6,032.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.03K USD at 128.9200 USD [API] | `2025-12-07 14:24:53` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 6,367.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.37K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 19.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 12.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 202.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 1,588.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.59K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,040.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.04K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,710.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.71K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 1,543.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.54K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 2,490.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.49K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.65` (Vol: 2,900,000.00 USD, Dist: `+3.04%`) | Long MP=`98.78` (Vol: 4,200,000.00 USD, Dist: `--1.80%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+3.47%`) | Long MP=`98.78` (Vol: 4,300,000.00 USD, Dist: `--1.80%`)
  * 3D Horizon: Short MP=`104.03` (Vol: 4,200,000.00 USD, Dist: `+3.42%`) | Long MP=`99.07` (Vol: 5,800,000.00 USD, Dist: `--1.51%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+3.43%`) | Long MP=`98.63` (Vol: 8,800,000.00 USD, Dist: `--1.95%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `20.50` | 500,800.00 USD | 140,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.50` | 9,590.00 USD | 140,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.50` | 640,090.00 USD | 140,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.50` | 52,490.00 USD | 139,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.50` | 29,610.00 USD | 139,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 14,650.00 USD | 139,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 159,830.00 USD | 139,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 5,310.00 USD | 139,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 25,020.00 USD | 139,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 112,130.00 USD | 139,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 811,380.00 USD | 139,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 65,450.00 USD | 138,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 54,260.00 USD | 138,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 324,140.00 USD | 138,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 6,550,000.00 USD | 138,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 28,890.00 USD | 131,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 13,230.00 USD | 131,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 348,620.00 USD | 131,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,020,000.00 USD | 131,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 74,740.00 USD | 128,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 77,130.00 USD | 128,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 43,170.00 USD | 127,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 1,090,000.00 USD | 127,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 46,760.00 USD | 126,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 305,790.00 USD | 126,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 1,880,000.00 USD | 126,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 6,000.00 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 3,920,000.00 USD | 124,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 64,870.00 USD | 120,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 80,310.00 USD | 120,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 163,360.00 USD | 120,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 800,950.00 USD | 120,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 101,460.00 USD | 119,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 3,420,000.00 USD | 119,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 1,120,000.00 USD | 116,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 182,390.00 USD | 114,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,590,000.00 USD | 114,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 112,290.00 USD | 113,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 184,220.00 USD | 113,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 134,170.00 USD | 112,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 177,470.00 USD | 112,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 228,150.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 217,380.00 USD | 112,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 376,000.00 USD | 112,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 75,240.00 USD | 111,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 11,940,000.00 USD | 111,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 99,120.00 USD | 99,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 1,050,000.00 USD | 99,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 37,930,000.00 USD | 98,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 172,850.00 USD | 60,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 3,590,000.00 USD | 60,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 497,880.00 USD | 56,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 1,920,000.00 USD | 56,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 590,970.00 USD | 54,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 644,710.00 USD | 53,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 871,540.00 USD | 53,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 441,110.00 USD | 52,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 757,050.00 USD | 51,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 5,380,000.00 USD | 51,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 430,910.00 USD | 45,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 2,020,000.00 USD | 45,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 2,600,000.00 USD | 43,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,420,000.00 USD | 40,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 721,890.00 USD | 39,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 610,240.00 USD | 38,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 956,570.00 USD | 37,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 882,970.00 USD | 37,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,420,000.00 USD | 36,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 3,930,000.00 USD | 34,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,870,000.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.90` | 371,170,000.00 USD | 371,170,000.00 USD | 525,310.00 USD | 459,170.00 USD | 925,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.10` | 369,260,000.00 USD | 369,260,000.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.30` | 180,280,000.00 USD | 180,280,000.00 USD | 362,900.00 USD | 537,500.00 USD | 506,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.30` | 367,180,000.00 USD | 367,180,000.00 USD | 703,270.00 USD | 342,020.00 USD | 654,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.50` | 178,870,000.00 USD | 178,870,000.00 USD | 523,240.00 USD | 399,670.00 USD | 473,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.50` | 365,480,000.00 USD | 365,480,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.50` | 426,080.00 USD | 28,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 177,470,000.00 USD | 177,470,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.70` | 362,800,000.00 USD | 362,800,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.90` | 176,970,000.00 USD | 176,970,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.90` | 360,350,000.00 USD | 360,350,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.10` | 176,870,000.00 USD | 176,870,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.10` | 357,970,000.00 USD | 357,970,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.30` | 176,680,000.00 USD | 176,680,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.30` | 356,060,000.00 USD | 356,060,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.50` | 176,530,000.00 USD | 176,530,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.50` | 353,560,000.00 USD | 353,560,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.50` | 3,170,000.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 176,420,000.00 USD | 176,420,000.00 USD | 107,440.00 USD | 112,260.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.70` | 350,650,000.00 USD | 350,650,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.90` | 176,200,000.00 USD | 176,200,000.00 USD | 187,160.00 USD | 63,660.00 USD | 177,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.90` | 349,020,000.00 USD | 349,020,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.10` | 175,770,000.00 USD | 175,770,000.00 USD | 161,220.00 USD | 124,560.00 USD | 64,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.10` | 346,600,000.00 USD | 346,600,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.30` | 175,420,000.00 USD | 175,420,000.00 USD | 219,340.00 USD | 97,250.00 USD | 738,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.30` | 345,290,000.00 USD | 345,290,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.50` | 174,370,000.00 USD | 174,370,000.00 USD | 37,670.00 USD | 53,380.00 USD | 168,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.50` | 343,280,000.00 USD | 343,280,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.50` | 2,310,000.00 USD | 25,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 174,110,000.00 USD | 174,110,000.00 USD | 0.00 USD | 86,970.00 USD | 168,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.70` | 341,880,000.00 USD | 341,880,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.90` | 173,850,000.00 USD | 173,850,000.00 USD | 100,830.00 USD | 0.00 USD | 60,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.90` | 341,610,000.00 USD | 341,610,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.10` | 173,690,000.00 USD | 173,690,000.00 USD | 0.00 USD | 2,580.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.10` | 341,550,000.00 USD | 341,550,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.30` | 173,570,000.00 USD | 173,570,000.00 USD | 0.00 USD | 103,020.00 USD | 99,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.30` | 341,160,000.00 USD | 341,160,000.00 USD | 55,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.50` | 341,050,000.00 USD | 341,050,000.00 USD | 101,820.00 USD | 335,760.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.50` | 3,170,000.00 USD | 23,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.70` | 340,610,000.00 USD | 340,610,000.00 USD | 270,240.00 USD | 262,300.00 USD | 115,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.90` | 339,960,000.00 USD | 339,960,000.00 USD | 236,340.00 USD | 90,940.00 USD | 214,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.10` | 339,420,000.00 USD | 339,420,000.00 USD | 233,120.00 USD | 296,810.00 USD | 321,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.30` | 338,570,000.00 USD | 338,570,000.00 USD | 10,610.00 USD | 0.00 USD | 44,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.50` | 338,510,000.00 USD | 338,510,000.00 USD | 183,750.00 USD | 0.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,910,000.00 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.90` | 338,190,000.00 USD | 338,190,000.00 USD | 297,690.00 USD | 444,840.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.10` | 173,370,000.00 USD | 173,370,000.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.10` | 337,430,000.00 USD | 337,430,000.00 USD | 141,070.00 USD | 115,890.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.30` | 173,360,000.00 USD | 173,360,000.00 USD | 18,710.00 USD | 89,760.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.30` | 337,160,000.00 USD | 337,160,000.00 USD | 251,720.00 USD | 196,820.00 USD | 474,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.50` | 173,240,000.00 USD | 173,240,000.00 USD | 679,320.00 USD | 458,400.00 USD | 465,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.50` | 336,240,000.00 USD | 336,240,000.00 USD | 1,000,000.00 USD | 732,540.00 USD | 341,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.50` | 1,620,000.00 USD | 16,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.70` | 171,640,000.00 USD | 171,640,000.00 USD | 1,490,000.00 USD | 1,130,000.00 USD | 649,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 334,160,000.00 USD | 334,160,000.00 USD | 1,980,000.00 USD | 1,130,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.90` | 168,370,000.00 USD | 168,370,000.00 USD | 1,150,000.00 USD | 885,010.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.90` | 329,600,000.00 USD | 329,600,000.00 USD | 1,610,000.00 USD | 1,260,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 165,100,000.00 USD | 165,100,000.00 USD | 1,430,000.00 USD | 1,420,000.00 USD | 942,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 324,070,000.00 USD | 324,070,000.00 USD | 2,910,000.00 USD | 2,330,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 161,310,000.00 USD | 161,310,000.00 USD | 875,730.00 USD | 1,150,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 316,190,000.00 USD | 316,190,000.00 USD | 2,910,000.00 USD | 1,170,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 158,110,000.00 USD | 158,110,000.00 USD | 1,370,000.00 USD | 924,880.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 309,940,000.00 USD | 309,940,000.00 USD | 2,870,000.00 USD | 1,580,000.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.50` | 1,360,000.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.70` | 154,470,000.00 USD | 154,470,000.00 USD | 681,660.00 USD | 858,670.00 USD | 909,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.70` | 302,910,000.00 USD | 302,910,000.00 USD | 2,220,000.00 USD | 2,450,000.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 152,020,000.00 USD | 152,020,000.00 USD | 383,880.00 USD | 290,640.00 USD | 167,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.90` | 295,870,000.00 USD | 295,870,000.00 USD | 5,140,000.00 USD | 3,170,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.10` | 151,170,000.00 USD | 151,170,000.00 USD | 271,410.00 USD | 113,790.00 USD | 379,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.10` | 284,210,000.00 USD | 284,210,000.00 USD | 4,430,000.00 USD | 2,080,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.30` | 150,410,000.00 USD | 150,410,000.00 USD | 197,550.00 USD | 378,560.00 USD | 121,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.30` | 276,050,000.00 USD | 276,050,000.00 USD | 5,780,000.00 USD | 4,270,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.50` | 149,710,000.00 USD | 149,710,000.00 USD | 1,460,000.00 USD | 1,060,000.00 USD | 960,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.50` | 262,250,000.00 USD | 262,250,000.00 USD | 4,390,000.00 USD | 4,370,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.50` | 2,470,000.00 USD | 13,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.70` | 146,220,000.00 USD | 146,220,000.00 USD | 3,200,000.00 USD | 2,660,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.70` | 249,100,000.00 USD | 249,100,000.00 USD | 5,660,000.00 USD | 3,410,000.00 USD | 5,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.90` | 138,930,000.00 USD | 138,930,000.00 USD | 3,030,000.00 USD | 2,300,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.90` | 234,630,000.00 USD | 234,630,000.00 USD | 8,020,000.00 USD | 6,060,000.00 USD | 7,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.10` | 130,870,000.00 USD | 130,870,000.00 USD | 3,360,000.00 USD | 3,450,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.10` | 213,350,000.00 USD | 213,350,000.00 USD | 8,580,000.00 USD | 7,190,000.00 USD | 7,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.30` | 121,550,000.00 USD | 121,550,000.00 USD | 2,760,000.00 USD | 2,960,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.30` | 190,450,000.00 USD | 190,450,000.00 USD | 7,530,000.00 USD | 4,040,000.00 USD | 7,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.50` | 113,150,000.00 USD | 113,150,000.00 USD | 6,160,000.00 USD | 3,960,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.50` | 171,470,000.00 USD | 171,470,000.00 USD | 10,550,000.00 USD | 7,040,000.00 USD | 9,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.50` | 10,960,000.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.70` | 96,710,000.00 USD | 96,710,000.00 USD | 7,440,000.00 USD | 6,270,000.00 USD | 4,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.70` | 144,820,000.00 USD | 144,820,000.00 USD | 11,830,000.00 USD | 9,800,000.00 USD | 13,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.90` | 78,070,000.00 USD | 78,070,000.00 USD | 5,040,000.00 USD | 4,270,000.00 USD | 5,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.90` | 109,700,000.00 USD | 109,700,000.00 USD | 15,300,000.00 USD | 9,640,000.00 USD | 17,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.10` | 63,020,000.00 USD | 63,020,000.00 USD | 6,070,000.00 USD | 5,760,000.00 USD | 4,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.10` | 67,260,000.00 USD | 67,260,000.00 USD | 18,940,000.00 USD | 12,780,000.00 USD | 10,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.30` | 46,460,000.00 USD | 46,460,000.00 USD | 3,310,000.00 USD | 4,420,000.00 USD | 4,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.30` | 25,160,000.00 USD | 25,160,000.00 USD | 3,040,000.00 USD | 1,180,000.00 USD | 6,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.50` | 33,760,000.00 USD | 33,760,000.00 USD | 5,190,000.00 USD | 3,860,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.50` | 14,860,000.00 USD | 14,860,000.00 USD | 1,370,000.00 USD | 1,380,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.50` | 481,350.00 USD | 519,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `99.70` | 19,470,000.00 USD | 19,470,000.00 USD | 2,480,000.00 USD | 3,410,000.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.70` | 9,160,000.00 USD | 9,160,000.00 USD | 661,070.00 USD | 1,650,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.90` | 10,350,000.00 USD | 10,350,000.00 USD | 1,650,000.00 USD | 1,300,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.90` | 4,610,000.00 USD | 4,610,000.00 USD | 843,730.00 USD | 0.00 USD | 531,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.10` | 6,290,000.00 USD | 6,290,000.00 USD | 1,290,000.00 USD | 914,930.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.10` | 3,230,000.00 USD | 3,230,000.00 USD | 533,430.00 USD | 36,980.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.30` | 2,650,000.00 USD | 2,650,000.00 USD | 163,250.00 USD | 167,670.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.30` | 1,630,000.00 USD | 1,630,000.00 USD | 39,280.00 USD | 68,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.50` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.50` | 1,520,000.00 USD | 1,520,000.00 USD | 39,680.00 USD | 0.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `100.50` | 37,930.00 USD | 37,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.70` | 1,720,000.00 USD | 1,720,000.00 USD | 274,280.00 USD | 970,010.00 USD | 476,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 1,270,000.00 USD | 1,270,000.00 USD | 46,010.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.90` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 953,600.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.90` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 1,610,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.10` | 10,640,000.00 USD | 10,640,000.00 USD | 4,870,000.00 USD | 3,090,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.10` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.30` | 19,590,000.00 USD | 19,590,000.00 USD | 2,660,000.00 USD | 3,940,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.30` | 22,770,000.00 USD | 22,770,000.00 USD | 4,480,000.00 USD | 2,460,000.00 USD | 5,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.50` | 34,430,000.00 USD | 34,430,000.00 USD | 1,940,000.00 USD | 3,350,000.00 USD | 9,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.50` | 34,390,000.00 USD | 34,390,000.00 USD | 2,560,000.00 USD | 0.00 USD | 9,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.50` | 96,850.00 USD | 96,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 47,750,000.00 USD | 47,750,000.00 USD | 4,420,000.00 USD | 0.00 USD | 8,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.70` | 43,730,000.00 USD | 43,730,000.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.90` | 52,280,000.00 USD | 52,280,000.00 USD | 1,320,000.00 USD | 142,780.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 50,190,000.00 USD | 50,190,000.00 USD | 2,670,000.00 USD | 0.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.10` | 53,900,000.00 USD | 53,900,000.00 USD | 407,760.00 USD | 439,590.00 USD | 768,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.10` | 52,910,000.00 USD | 52,910,000.00 USD | 0.00 USD | 0.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.30` | 58,220,000.00 USD | 58,220,000.00 USD | 799,010.00 USD | 1,180,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.30` | 56,810,000.00 USD | 56,810,000.00 USD | 1,520,000.00 USD | 578,040.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.50` | 60,200,000.00 USD | 60,200,000.00 USD | 992,380.00 USD | 292,190.00 USD | 696,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.50` | 59,350,000.00 USD | 59,350,000.00 USD | 680,620.00 USD | 1,280,000.00 USD | 582,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.50` | 11,120.00 USD | 107,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 61,660,000.00 USD | 61,660,000.00 USD | 931,170.00 USD | 524,710.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.70` | 60,080,000.00 USD | 60,080,000.00 USD | 722,800.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.90` | 65,600,000.00 USD | 65,600,000.00 USD | 1,380,000.00 USD | 1,770,000.00 USD | 792,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 79,590,000.00 USD | 79,590,000.00 USD | 16,450,000.00 USD | 0.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.10` | 71,770,000.00 USD | 71,770,000.00 USD | 2,780,000.00 USD | 1,800,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.10` | 84,970,000.00 USD | 84,970,000.00 USD | 4,750,000.00 USD | 4,380.00 USD | 616,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.30` | 76,900,000.00 USD | 76,900,000.00 USD | 2,390,000.00 USD | 1,920,000.00 USD | 815,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.30` | 102,570,000.00 USD | 102,570,000.00 USD | 17,450,000.00 USD | 9,520.00 USD | 140,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.50` | 89,410,000.00 USD | 89,410,000.00 USD | 4,290,000.00 USD | 2,690,000.00 USD | 5,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.50` | 124,070,000.00 USD | 124,070,000.00 USD | 13,580,000.00 USD | 1,770,000.00 USD | 6,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.50` | 29,050.00 USD | 137,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 101,330,000.00 USD | 101,330,000.00 USD | 4,210,000.00 USD | 2,380,000.00 USD | 5,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.70` | 136,290,000.00 USD | 136,290,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.90` | 110,650,000.00 USD | 110,650,000.00 USD | 2,710,000.00 USD | 3,080,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.90` | 153,550,000.00 USD | 153,550,000.00 USD | 8,600,000.00 USD | 2,630,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.10` | 119,690,000.00 USD | 119,690,000.00 USD | 3,450,000.00 USD | 2,370,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.10` | 181,320,000.00 USD | 181,320,000.00 USD | 10,840,000.00 USD | 8,150,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.30` | 127,680,000.00 USD | 127,680,000.00 USD | 2,710,000.00 USD | 2,140,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.30` | 201,630,000.00 USD | 201,630,000.00 USD | 6,740,000.00 USD | 6,260,000.00 USD | 7,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.50` | 135,180,000.00 USD | 135,180,000.00 USD | 2,590,000.00 USD | 2,120,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.50` | 213,360,000.00 USD | 213,360,000.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.50` | 1,190,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 145,050,000.00 USD | 145,050,000.00 USD | 2,650,000.00 USD | 2,140,000.00 USD | 5,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.70` | 233,360,000.00 USD | 233,360,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.90` | 148,020,000.00 USD | 148,020,000.00 USD | 1,020,000.00 USD | 592,030.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 253,960,000.00 USD | 253,960,000.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.10` | 150,460,000.00 USD | 150,460,000.00 USD | 421,810.00 USD | 622,250.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 267,640,000.00 USD | 267,640,000.00 USD | 5,580,000.00 USD | 5,260,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.30` | 151,400,000.00 USD | 151,400,000.00 USD | 506,770.00 USD | 2,430.00 USD | 425,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.30` | 274,040,000.00 USD | 274,040,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.50` | 152,450,000.00 USD | 152,450,000.00 USD | 157,550.00 USD | 209,490.00 USD | 684,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.50` | 293,880,000.00 USD | 293,880,000.00 USD | 5,600,000.00 USD | 6,270,000.00 USD | 7,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.50` | 167,490.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 153,780,000.00 USD | 153,780,000.00 USD | 294,800.00 USD | 506,510.00 USD | 529,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.70` | 308,730,000.00 USD | 308,730,000.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.90` | 154,800,000.00 USD | 154,800,000.00 USD | 215,940.00 USD | 666,590.00 USD | 135,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.90` | 319,270,000.00 USD | 319,270,000.00 USD | 3,930,000.00 USD | 2,260,000.00 USD | 4,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.10` | 156,310,000.00 USD | 156,310,000.00 USD | 716,050.00 USD | 529,140.00 USD | 267,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.10` | 332,730,000.00 USD | 332,730,000.00 USD | 6,810,000.00 USD | 3,690,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.30` | 158,050,000.00 USD | 158,050,000.00 USD | 499,810.00 USD | 619,440.00 USD | 622,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 344,020,000.00 USD | 344,020,000.00 USD | 5,120,000.00 USD | 3,230,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.50` | 159,730,000.00 USD | 159,730,000.00 USD | 1,010,000.00 USD | 336,210.00 USD | 333,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.50` | 349,990,000.00 USD | 349,990,000.00 USD | 1,730,000.00 USD | 2,010,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.50` | 13,380.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.70` | 162,820,000.00 USD | 162,820,000.00 USD | 890,450.00 USD | 383,670.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.70` | 359,720,000.00 USD | 359,720,000.00 USD | 2,290,000.00 USD | 3,150,000.00 USD | 4,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.90` | 163,880,000.00 USD | 163,880,000.00 USD | 317,210.00 USD | 150,690.00 USD | 594,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.90` | 365,500,000.00 USD | 365,500,000.00 USD | 1,190,000.00 USD | 1,120,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.10` | 164,730,000.00 USD | 164,730,000.00 USD | 88,570.00 USD | 254,230.00 USD | 510,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.10` | 368,900,000.00 USD | 368,900,000.00 USD | 1,630,000.00 USD | 508,540.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.30` | 165,200,000.00 USD | 165,200,000.00 USD | 252,090.00 USD | 0.00 USD | 212,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.30` | 369,060,000.00 USD | 369,060,000.00 USD | 0.00 USD | 156,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.50` | 165,490,000.00 USD | 165,490,000.00 USD | 0.00 USD | 6,440.00 USD | 288,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.50` | 370,040,000.00 USD | 370,040,000.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.50` | 368,250.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.70` | 166,020,000.00 USD | 166,020,000.00 USD | 94,360.00 USD | 181,310.00 USD | 249,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.70` | 371,010,000.00 USD | 371,010,000.00 USD | 523,660.00 USD | 11,530.00 USD | 432,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.90` | 166,150,000.00 USD | 166,150,000.00 USD | 0.00 USD | 128,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.90` | 371,180,000.00 USD | 371,180,000.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.10` | 372,810,000.00 USD | 372,810,000.00 USD | 707,230.00 USD | 915,170.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.30` | 375,220,000.00 USD | 375,220,000.00 USD | 1,090,000.00 USD | 697,770.00 USD | 612,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.50` | 376,930,000.00 USD | 376,930,000.00 USD | 835,610.00 USD | 340,050.00 USD | 540,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.50` | 102,250.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 379,300,000.00 USD | 379,300,000.00 USD | 575,510.00 USD | 726,100.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.90` | 380,600,000.00 USD | 380,600,000.00 USD | 414,890.00 USD | 701,350.00 USD | 181,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.10` | 166,150,000.00 USD | 166,150,000.00 USD | 5,350.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.10` | 381,680,000.00 USD | 381,680,000.00 USD | 434,330.00 USD | 185,250.00 USD | 461,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.30` | 166,290,000.00 USD | 166,290,000.00 USD | 126,020.00 USD | 9,360.00 USD | 2,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.30` | 382,540,000.00 USD | 382,540,000.00 USD | 486,260.00 USD | 85,680.00 USD | 286,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.50` | 166,550,000.00 USD | 166,550,000.00 USD | 133,350.00 USD | 84,430.00 USD | 44,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.50` | 382,780,000.00 USD | 382,780,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.50` | 609,280.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.70` | 167,460,000.00 USD | 167,460,000.00 USD | 456,990.00 USD | 277,760.00 USD | 171,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.70` | 383,960,000.00 USD | 383,960,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.90` | 168,400,000.00 USD | 168,400,000.00 USD | 268,320.00 USD | 266,300.00 USD | 405,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.90` | 385,450,000.00 USD | 385,450,000.00 USD | 238,580.00 USD | 447,100.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.10` | 169,440,000.00 USD | 169,440,000.00 USD | 258,510.00 USD | 467,380.00 USD | 313,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.10` | 387,520,000.00 USD | 387,520,000.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.30` | 170,430,000.00 USD | 170,430,000.00 USD | 238,980.00 USD | 342,030.00 USD | 406,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.30` | 389,220,000.00 USD | 389,220,000.00 USD | 703,270.00 USD | 342,020.00 USD | 654,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.50` | 171,080,000.00 USD | 171,080,000.00 USD | 300,210.00 USD | 150,770.00 USD | 197,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.50` | 389,710,000.00 USD | 389,710,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.50` | 195,830.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.70` | 171,820,000.00 USD | 171,820,000.00 USD | 223,030.00 USD | 248,900.00 USD | 276,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.70` | 391,910,000.00 USD | 391,910,000.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.90` | 172,330,000.00 USD | 172,330,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.90` | 394,350,000.00 USD | 394,350,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.10` | 172,430,000.00 USD | 172,430,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.10` | 396,740,000.00 USD | 396,740,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.30` | 172,610,000.00 USD | 172,610,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.30` | 398,640,000.00 USD | 398,640,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.50` | 172,760,000.00 USD | 172,760,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.50` | 401,150,000.00 USD | 401,150,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.50` | 2,390,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.70` | 172,790,000.00 USD | 172,790,000.00 USD | 0.00 USD | 27,410.00 USD | 641.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.70` | 402,290,000.00 USD | 402,290,000.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.90` | 172,880,000.00 USD | 172,880,000.00 USD | 21,670.00 USD | 60,130.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.90` | 404,060,000.00 USD | 404,060,000.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.10` | 173,100,000.00 USD | 173,100,000.00 USD | 107,440.00 USD | 112,260.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.10` | 405,690,000.00 USD | 405,690,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.30` | 173,510,000.00 USD | 173,510,000.00 USD | 178,390.00 USD | 58,870.00 USD | 174,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.30` | 408,100,000.00 USD | 408,100,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.50` | 409,420,000.00 USD | 409,420,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.50` | 125,350.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.70` | 409,940,000.00 USD | 409,940,000.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.90` | 411,430,000.00 USD | 411,430,000.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.10` | 412,820,000.00 USD | 412,820,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.30` | 413,100,000.00 USD | 413,100,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.50` | 413,160,000.00 USD | 413,160,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.50` | 224,480.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.70` | 413,550,000.00 USD | 413,550,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.50` | 62,000.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.50` | 945,940.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.50` | 157,330.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.50` | 4,600,000.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 725,160.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.50` | 358,660.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 7,000.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 113,860.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 82,340.00 USD | 12,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 17,790.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 204,410.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 512,840.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 12,540,000.00 USD | 25,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 770,400.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 10,500,000.00 USD | 37,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 164,320.00 USD | 37,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 602,490.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 18,810.00 USD | 37,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 68,510.00 USD | 37,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 1,270,000.00 USD | 39,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 35,860.00 USD | 39,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 719,490.00 USD | 40,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 8,680.00 USD | 40,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 3,760.00 USD | 40,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,320,000.00 USD | 42,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 1,150,000.00 USD | 43,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 14,240.00 USD | 43,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 462,490.00 USD | 43,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 96,470.00 USD | 44,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 198,910.00 USD | 44,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 957,190.00 USD | 45,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 16,290.00 USD | 45,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 691,960.00 USD | 45,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 103,680.00 USD | 46,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,350,000.00 USD | 48,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 19,740.00 USD | 48,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 5,850.00 USD | 48,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 19,740.00 USD | 48,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 2,330,000.00 USD | 50,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.50` | 429,190.00 USD | 51,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 7,250.00 USD | 51,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 168,990.00 USD | 51,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 5,000,000.00 USD | 56,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 1,660,000.00 USD | 58,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 120,580.00 USD | 58,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.50` | 148,650.00 USD | 58,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 817,810.00 USD | 59,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 297,730.00 USD | 59,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 12,910.00 USD | 59,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 3,880.00 USD | 59,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 261,230.00 USD | 59,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 36,550,000.00 USD | 96,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 1,230,000.00 USD | 97,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 5,980,000.00 USD | 103,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 485,410.00 USD | 103,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 101,700.00 USD | 104,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 231.88 USD | 104,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 509.35 USD | 104,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 65,260.00 USD | 104,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 63,530.00 USD | 104,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 557,520.00 USD | 104,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 4,880.00 USD | 104,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 27,570.00 USD | 104,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 78,100.00 USD | 104,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 2,980,000.00 USD | 107,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 829.29 USD | 107,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 13,820.00 USD | 107,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 11,650.00 USD | 107,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 297,920.00 USD | 108,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 372,500.00 USD | 108,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 165,370.00 USD | 108,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 206,840.00 USD | 108,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 774,320.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 41,020.00 USD | 109,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 187,240.00 USD | 109,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 349,140.00 USD | 110,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 13,880,000.00 USD | 124,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 321.72 USD | 124,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 109,870.00 USD | 124,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 144,570.00 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 148,800.00 USD | 124,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 62,580.00 USD | 124,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 15,680.00 USD | 124,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 246,140.00 USD | 124,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 84,450.00 USD | 124,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 53,380.00 USD | 124,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 314,450.00 USD | 125,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 9,970.00 USD | 125,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `202.50` | 4,310,000.00 USD | 129,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `20.50` | 140,890,000.00 USD | 0.00 USD | 500,800.00 USD | `-79.72%` | `24,429.37` |
| `Live` | `Long` | `21.50` | 140,390,000.00 USD | 0.00 USD | 9,590.00 USD | `-78.73%` | `446.10` |
| `Live` | `Long` | `22.50` | 140,380,000.00 USD | 0.00 USD | 640,090.00 USD | `-77.75%` | `28,448.44` |
| `Live` | `Long` | `23.50` | 139,740,000.00 USD | 0.00 USD | 52,490.00 USD | `-76.76%` | `2,233.79` |
| `Live` | `Long` | `24.50` | 139,690,000.00 USD | 0.00 USD | 29,610.00 USD | `-75.77%` | `1,208.64` |
| `Live` | `Long` | `25.50` | 139,660,000.00 USD | 0.00 USD | 14,650.00 USD | `-74.78%` | `574.36` |
| `Live` | `Long` | `26.50` | 139,650,000.00 USD | 0.00 USD | 159,830.00 USD | `-73.79%` | `6,031.39` |
| `Live` | `Long` | `27.50` | 139,490,000.00 USD | 0.00 USD | 5,310.00 USD | `-72.80%` | `193.26` |
| `Live` | `Long` | `28.50` | 139,480,000.00 USD | 0.00 USD | 25,020.00 USD | `-71.81%` | `877.99` |
| `Live` | `Long` | `29.50` | 139,460,000.00 USD | 0.00 USD | 112,130.00 USD | `-70.82%` | `3,800.88` |
| `Live` | `Long` | `30.50` | 139,350,000.00 USD | 0.00 USD | 811,380.00 USD | `-69.83%` | `26,602.57` |
| `Live` | `Long` | `31.50` | 138,530,000.00 USD | 0.00 USD | 65,450.00 USD | `-68.84%` | `2,077.71` |
| `Live` | `Long` | `32.50` | 138,470,000.00 USD | 0.00 USD | 54,260.00 USD | `-67.85%` | `1,669.61` |
| `Live` | `Long` | `33.50` | 138,410,000.00 USD | 0.00 USD | 324,140.00 USD | `-66.87%` | `9,675.70` |
| `Live` | `Long` | `34.50` | 138,090,000.00 USD | 0.00 USD | 6,550,000.00 USD | `-65.88%` | `189,784.79` |
| `Live` | `Long` | `35.50` | 131,540,000.00 USD | 0.00 USD | 28,890.00 USD | `-64.89%` | `813.68` |
| `Live` | `Long` | `36.50` | 131,510,000.00 USD | 0.00 USD | 13,230.00 USD | `-63.90%` | `362.55` |
| `Live` | `Long` | `37.50` | 131,500,000.00 USD | 0.00 USD | 348,620.00 USD | `-62.91%` | `9,296.55` |
| `Live` | `Long` | `38.50` | 131,150,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-61.92%` | `78,325.77` |
| `Live` | `Long` | `39.50` | 128,140,000.00 USD | 0.00 USD | 74,740.00 USD | `-60.93%` | `1,892.06` |
| `Live` | `Long` | `40.50` | 128,060,000.00 USD | 0.00 USD | 77,130.00 USD | `-59.94%` | `1,904.44` |
| `Live` | `Long` | `41.50` | 127,980,000.00 USD | 0.00 USD | 43,170.00 USD | `-58.95%` | `1,040.15` |
| `Live` | `Long` | `42.50` | 127,940,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-57.96%` | `25,592.18` |
| `Live` | `Long` | `43.50` | 126,850,000.00 USD | 0.00 USD | 46,760.00 USD | `-56.97%` | `1,074.97` |
| `Live` | `Long` | `44.50` | 126,810,000.00 USD | 0.00 USD | 305,790.00 USD | `-55.98%` | `6,871.68` |
| `Live` | `Long` | `45.50` | 126,500,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-55.00%` | `41,399.20` |
| `Live` | `Long` | `46.50` | 124,620,000.00 USD | 0.00 USD | 6,000.00 USD | `-54.01%` | `129.09` |
| `Live` | `Long` | `47.50` | 124,610,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-53.02%` | `82,498.98` |
| `Live` | `Long` | `48.50` | 120,690,000.00 USD | 0.00 USD | 64,870.00 USD | `-52.03%` | `1,337.48` |
| `Live` | `Long` | `49.50` | 120,630,000.00 USD | 0.00 USD | 80,310.00 USD | `-51.04%` | `1,622.49` |
| `Live` | `Long` | `50.50` | 120,550,000.00 USD | 0.00 USD | 163,360.00 USD | `-50.05%` | `3,234.85` |
| `Live` | `Long` | `51.50` | 120,380,000.00 USD | 0.00 USD | 800,950.00 USD | `-49.06%` | `15,552.44` |
| `Live` | `Long` | `52.50` | 119,580,000.00 USD | 0.00 USD | 101,460.00 USD | `-48.07%` | `1,932.48` |
| `Live` | `Long` | `53.50` | 119,480,000.00 USD | 0.00 USD | 3,420,000.00 USD | `-47.08%` | `63,935.80` |
| `Live` | `Long` | `54.50` | 116,060,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-46.09%` | `20,606.51` |
| `Live` | `Long` | `55.50` | 114,940,000.00 USD | 0.00 USD | 182,390.00 USD | `-45.10%` | `3,286.39` |
| `Live` | `Long` | `56.50` | 114,760,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-44.12%` | `28,105.53` |
| `Live` | `Long` | `57.50` | 113,170,000.00 USD | 0.00 USD | 112,290.00 USD | `-43.13%` | `1,952.89` |
| `Live` | `Long` | `58.50` | 113,060,000.00 USD | 0.00 USD | 184,220.00 USD | `-42.14%` | `3,149.06` |
| `Live` | `Long` | `59.50` | 112,870,000.00 USD | 0.00 USD | 134,170.00 USD | `-41.15%` | `2,255.03` |
| `Live` | `Long` | `60.50` | 112,740,000.00 USD | 0.00 USD | 177,470.00 USD | `-40.16%` | `2,933.39` |
| `Live` | `Long` | `61.50` | 112,560,000.00 USD | 0.00 USD | 228,150.00 USD | `-39.17%` | `3,709.83` |
| `Live` | `Long` | `62.50` | 112,330,000.00 USD | 0.00 USD | 217,380.00 USD | `-38.18%` | `3,478.04` |
| `Live` | `Long` | `63.50` | 112,110,000.00 USD | 0.00 USD | 376,000.00 USD | `-37.19%` | `5,921.33` |
| `Live` | `Long` | `64.50` | 111,740,000.00 USD | 0.00 USD | 75,240.00 USD | `-36.20%` | `1,166.47` |
| `Live` | `Long` | `65.50` | 111,660,000.00 USD | 0.00 USD | 11,940,000.00 USD | `-35.21%` | `182,345.10` |
| `Live` | `Long` | `66.50` | 99,720,000.00 USD | 0.00 USD | 99,120.00 USD | `-34.22%` | `1,490.55` |
| `Live` | `Long` | `67.50` | 99,620,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-33.24%` | `15,598.58` |
| `Live` | `Long` | `68.50` | 98,570,000.00 USD | 0.00 USD | 37,930,000.00 USD | `-32.25%` | `553,664.83` |
| `Live` | `Long` | `69.50` | 60,640,000.00 USD | 0.00 USD | 172,850.00 USD | `-31.26%` | `2,487.09` |
| `Live` | `Long` | `70.50` | 60,470,000.00 USD | 0.00 USD | 3,590,000.00 USD | `-30.27%` | `50,879.87` |
| `Live` | `Long` | `71.50` | 56,880,000.00 USD | 0.00 USD | 497,880.00 USD | `-29.28%` | `6,963.33` |
| `Live` | `Long` | `72.50` | 56,380,000.00 USD | 0.00 USD | 1,920,000.00 USD | `-28.29%` | `26,480.44` |
| `Live` | `Long` | `73.50` | 54,460,000.00 USD | 0.00 USD | 590,970.00 USD | `-27.30%` | `8,040.40` |
| `Live` | `Long` | `74.50` | 53,870,000.00 USD | 0.00 USD | 644,710.00 USD | `-26.31%` | `8,653.88` |
| `Live` | `Long` | `75.50` | 53,230,000.00 USD | 0.00 USD | 871,540.00 USD | `-25.32%` | `11,543.64` |
| `Live` | `Long` | `76.50` | 52,360,000.00 USD | 0.00 USD | 441,110.00 USD | `-24.33%` | `5,766.12` |
| `Live` | `Long` | `77.50` | 51,920,000.00 USD | 0.00 USD | 757,050.00 USD | `-23.34%` | `9,768.43` |
| `Live` | `Long` | `78.50` | 51,160,000.00 USD | 0.00 USD | 5,380,000.00 USD | `-22.36%` | `68,540.65` |
| `Live` | `Long` | `79.50` | 45,780,000.00 USD | 0.00 USD | 430,910.00 USD | `-21.37%` | `5,420.22` |
| `Live` | `Long` | `80.50` | 45,350,000.00 USD | 0.00 USD | 2,020,000.00 USD | `-20.38%` | `25,087.54` |
| `Live` | `Long` | `81.50` | 43,330,000.00 USD | 0.00 USD | 2,600,000.00 USD | `-19.39%` | `31,899.01` |
| `Live` | `Long` | `82.50` | 40,730,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-18.40%` | `17,173.82` |
| `Live` | `Long` | `83.50` | 39,310,000.00 USD | 0.00 USD | 721,890.00 USD | `-17.41%` | `8,645.35` |
| `Live` | `Long` | `84.50` | 38,590,000.00 USD | 0.00 USD | 610,240.00 USD | `-16.42%` | `7,221.77` |
| `Live` | `Long` | `85.50` | 37,980,000.00 USD | 0.00 USD | 956,570.00 USD | `-15.43%` | `11,187.94` |
| `Live` | `Long` | `86.50` | 37,020,000.00 USD | 0.00 USD | 882,970.00 USD | `-14.44%` | `10,207.76` |
| `Live` | `Long` | `87.50` | 36,140,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-13.45%` | `16,186.37` |
| `Live` | `Long` | `88.50` | 34,720,000.00 USD | 0.00 USD | 3,930,000.00 USD | `-12.46%` | `44,426.70` |
| `Live` | `Long` | `89.50` | 30,790,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-11.48%` | `20,893.76` |
| `Live` | `Long` | `90.50` | 28,920,000.00 USD | 0.00 USD | 426,080.00 USD | `-10.49%` | `4,708.06` |
| `Live` | `Long` | `91.50` | 28,490,000.00 USD | 0.00 USD | 3,170,000.00 USD | `-9.50%` | `34,668.72` |
| `Live` | `Long` | `92.50` | 25,320,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-8.51%` | `24,997.59` |
| `Live` | `Long` | `93.50` | 23,010,000.00 USD | 0.00 USD | 3,170,000.00 USD | `-7.52%` | `33,932.78` |
| `Live` | `Long` | `94.50` | 19,840,000.00 USD | 0.00 USD | 2,910,000.00 USD | `-6.53%` | `30,794.19` |
| `Live` | `Long` | `95.50` | 16,930,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-5.54%` | `16,934.75` |
| `Live` | `Long` | `96.50` | 15,310,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-4.55%` | `14,096.22` |
| `Live` | `Long` | `97.50` | 13,950,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-3.56%` | `25,290.68` |
| `Live` | `Long` | `98.50` | 11,480,000.00 USD | 0.00 USD | 10,960,000.00 USD | `-2.57%` | `111,319.00` |
| `Live` | `Long` | `99.50` | 519,290.00 USD | 0.00 USD | 481,350.00 USD | `-1.58%` | `4,837.73` |
| `Live` | `Long` | `100.50` | 37,930.00 USD | 0.00 USD | 37,930.00 USD | `-0.60%` | `377.44` |
| `Live` | `Short` | `101.50` | 96,850.00 USD | 96,850.00 USD | 0.00 USD | `+0.39%` | `954.19` |
| `Live` | `Short` | `102.50` | 107,970.00 USD | 11,120.00 USD | 0.00 USD | `+1.38%` | `108.53` |
| `Live` | `Short` | `103.50` | 137,030.00 USD | 29,050.00 USD | 0.00 USD | `+2.37%` | `280.71` |
| `Live` | `Short` | `104.50` | 1,330,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+3.36%` | `11,422.89` |
| `Live` | `Short` | `105.50` | 1,500,000.00 USD | 167,490.00 USD | 0.00 USD | `+4.35%` | `1,587.59` |
| `Live` | `Short` | `106.50` | 1,510,000.00 USD | 13,380.00 USD | 0.00 USD | `+5.34%` | `125.60` |
| `Live` | `Short` | `107.50` | 1,880,000.00 USD | 368,250.00 USD | 0.00 USD | `+6.33%` | `3,425.54` |
| `Live` | `Short` | `108.50` | 1,980,000.00 USD | 102,250.00 USD | 0.00 USD | `+7.32%` | `942.41` |
| `Live` | `Short` | `109.50` | 2,590,000.00 USD | 609,280.00 USD | 0.00 USD | `+8.31%` | `5,564.22` |
| `Live` | `Short` | `110.50` | 2,790,000.00 USD | 195,830.00 USD | 0.00 USD | `+9.30%` | `1,772.19` |
| `Live` | `Short` | `111.50` | 5,180,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+10.29%` | `21,434.38` |
| `Live` | `Short` | `112.50` | 5,300,000.00 USD | 125,350.00 USD | 0.00 USD | `+11.27%` | `1,114.19` |
| `Live` | `Short` | `113.50` | 5,530,000.00 USD | 224,480.00 USD | 0.00 USD | `+12.26%` | `1,977.81` |
| `Live` | `Short` | `114.50` | 5,590,000.00 USD | 62,000.00 USD | 0.00 USD | `+13.25%` | `541.48` |
| `Live` | `Short` | `115.50` | 6,530,000.00 USD | 945,940.00 USD | 0.00 USD | `+14.24%` | `8,189.93` |
| `Live` | `Short` | `116.50` | 6,690,000.00 USD | 157,330.00 USD | 0.00 USD | `+15.23%` | `1,350.46` |
| `Live` | `Short` | `117.50` | 11,290,000.00 USD | 4,600,000.00 USD | 0.00 USD | `+16.22%` | `39,166.67` |
| `Live` | `Short` | `118.50` | 12,020,000.00 USD | 725,160.00 USD | 0.00 USD | `+17.21%` | `6,119.46` |
| `Live` | `Short` | `119.50` | 12,380,000.00 USD | 358,660.00 USD | 0.00 USD | `+18.20%` | `3,001.30` |
| `Live` | `Short` | `120.50` | 12,390,000.00 USD | 7,000.00 USD | 0.00 USD | `+19.19%` | `58.05` |
| `Live` | `Short` | `121.50` | 12,500,000.00 USD | 113,860.00 USD | 0.00 USD | `+20.18%` | `937.09` |
| `Live` | `Short` | `122.50` | 12,580,000.00 USD | 82,340.00 USD | 0.00 USD | `+21.17%` | `672.17` |
| `Live` | `Short` | `123.50` | 12,600,000.00 USD | 17,790.00 USD | 0.00 USD | `+22.15%` | `144.05` |
| `Live` | `Short` | `124.50` | 12,800,000.00 USD | 204,410.00 USD | 0.00 USD | `+23.14%` | `1,641.86` |
| `Live` | `Short` | `125.50` | 13,320,000.00 USD | 512,840.00 USD | 0.00 USD | `+24.13%` | `4,086.37` |
| `Live` | `Short` | `126.50` | 25,860,000.00 USD | 12,540,000.00 USD | 0.00 USD | `+25.12%` | `99,153.38` |
| `Live` | `Short` | `127.50` | 26,630,000.00 USD | 770,400.00 USD | 0.00 USD | `+26.11%` | `6,042.37` |
| `Live` | `Short` | `128.50` | 37,130,000.00 USD | 10,500,000.00 USD | 0.00 USD | `+27.10%` | `81,695.44` |
| `Live` | `Short` | `129.50` | 37,290,000.00 USD | 164,320.00 USD | 0.00 USD | `+28.09%` | `1,268.86` |
| `Live` | `Short` | `130.50` | 37,890,000.00 USD | 602,490.00 USD | 0.00 USD | `+29.08%` | `4,616.78` |
| `Live` | `Short` | `131.50` | 37,910,000.00 USD | 18,810.00 USD | 0.00 USD | `+30.07%` | `143.01` |
| `Live` | `Short` | `132.50` | 37,980,000.00 USD | 68,510.00 USD | 0.00 USD | `+31.06%` | `517.05` |
| `Live` | `Short` | `133.50` | 39,260,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+32.05%` | `9,542.34` |
| `Live` | `Short` | `134.50` | 39,290,000.00 USD | 35,860.00 USD | 0.00 USD | `+33.03%` | `266.61` |
| `Live` | `Short` | `135.50` | 40,010,000.00 USD | 719,490.00 USD | 0.00 USD | `+34.02%` | `5,309.86` |
| `Live` | `Short` | `136.50` | 40,020,000.00 USD | 8,680.00 USD | 0.00 USD | `+35.01%` | `63.60` |
| `Live` | `Short` | `137.50` | 40,020,000.00 USD | 3,760.00 USD | 0.00 USD | `+36.00%` | `27.32` |
| `Live` | `Short` | `138.50` | 42,340,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+36.99%` | `16,733.65` |
| `Live` | `Short` | `139.50` | 43,490,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+37.98%` | `8,252.19` |
| `Live` | `Short` | `140.50` | 43,510,000.00 USD | 14,240.00 USD | 0.00 USD | `+38.97%` | `101.38` |
| `Live` | `Short` | `141.50` | 43,970,000.00 USD | 462,490.00 USD | 0.00 USD | `+39.96%` | `3,268.45` |
| `Live` | `Short` | `142.50` | 44,070,000.00 USD | 96,470.00 USD | 0.00 USD | `+40.95%` | `676.97` |
| `Live` | `Short` | `143.50` | 44,260,000.00 USD | 198,910.00 USD | 0.00 USD | `+41.94%` | `1,386.10` |
| `Live` | `Short` | `144.50` | 45,220,000.00 USD | 957,190.00 USD | 0.00 USD | `+42.93%` | `6,624.16` |
| `Live` | `Short` | `145.50` | 45,240,000.00 USD | 16,290.00 USD | 0.00 USD | `+43.91%` | `111.97` |
| `Live` | `Short` | `146.50` | 45,930,000.00 USD | 691,960.00 USD | 0.00 USD | `+44.90%` | `4,723.31` |
| `Live` | `Short` | `147.50` | 46,030,000.00 USD | 103,680.00 USD | 0.00 USD | `+45.89%` | `702.90` |
| `Live` | `Short` | `148.50` | 48,380,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+46.88%` | `15,827.51` |
| `Live` | `Short` | `149.50` | 48,400,000.00 USD | 19,740.00 USD | 0.00 USD | `+47.87%` | `132.06` |
| `Live` | `Short` | `150.50` | 48,410,000.00 USD | 5,850.00 USD | 0.00 USD | `+48.86%` | `38.87` |
| `Live` | `Short` | `151.50` | 48,430,000.00 USD | 19,740.00 USD | 0.00 USD | `+49.85%` | `130.32` |
| `Live` | `Short` | `152.50` | 50,760,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+50.84%` | `15,304.70` |
| `Live` | `Short` | `153.50` | 51,190,000.00 USD | 429,190.00 USD | 0.00 USD | `+51.83%` | `2,796.03` |
| `Live` | `Short` | `154.50` | 51,200,000.00 USD | 7,250.00 USD | 0.00 USD | `+52.82%` | `46.90` |
| `Live` | `Short` | `155.50` | 51,370,000.00 USD | 168,990.00 USD | 0.00 USD | `+53.81%` | `1,086.78` |
| `Live` | `Short` | `156.50` | 56,370,000.00 USD | 5,000,000.00 USD | 0.00 USD | `+54.79%` | `31,929.23` |
| `Live` | `Short` | `157.50` | 58,030,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+55.78%` | `10,540.87` |
| `Live` | `Short` | `158.50` | 58,150,000.00 USD | 120,580.00 USD | 0.00 USD | `+56.77%` | `760.78` |
| `Live` | `Short` | `159.50` | 58,290,000.00 USD | 148,650.00 USD | 0.00 USD | `+57.76%` | `931.95` |
| `Live` | `Short` | `160.50` | 59,110,000.00 USD | 817,810.00 USD | 0.00 USD | `+58.75%` | `5,095.36` |
| `Live` | `Short` | `161.50` | 59,410,000.00 USD | 297,730.00 USD | 0.00 USD | `+59.74%` | `1,843.51` |
| `Live` | `Short` | `162.50` | 59,420,000.00 USD | 12,910.00 USD | 0.00 USD | `+60.73%` | `79.45` |
| `Live` | `Short` | `163.50` | 59,430,000.00 USD | 3,880.00 USD | 0.00 USD | `+61.72%` | `23.71` |
| `Live` | `Short` | `164.50` | 59,690,000.00 USD | 261,230.00 USD | 0.00 USD | `+62.71%` | `1,588.02` |
| `Live` | `Short` | `165.50` | 96,240,000.00 USD | 36,550,000.00 USD | 0.00 USD | `+63.70%` | `220,873.34` |
| `Live` | `Short` | `166.50` | 97,470,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+64.69%` | `7,393.77` |
| `Live` | `Short` | `167.50` | 103,450,000.00 USD | 5,980,000.00 USD | 0.00 USD | `+65.67%` | `35,677.30` |
| `Live` | `Short` | `168.50` | 103,940,000.00 USD | 485,410.00 USD | 0.00 USD | `+66.66%` | `2,880.80` |
| `Live` | `Short` | `169.50` | 104,040,000.00 USD | 101,700.00 USD | 0.00 USD | `+67.65%` | `600.00` |
| `Live` | `Short` | `170.50` | 104,040,000.00 USD | 231.88 USD | 0.00 USD | `+68.64%` | `1.36` |
| `Live` | `Short` | `171.50` | 104,040,000.00 USD | 509.35 USD | 0.00 USD | `+69.63%` | `2.97` |
| `Live` | `Short` | `172.50` | 104,100,000.00 USD | 65,260.00 USD | 0.00 USD | `+70.62%` | `378.33` |
| `Live` | `Short` | `173.50` | 104,170,000.00 USD | 63,530.00 USD | 0.00 USD | `+71.61%` | `366.15` |
| `Live` | `Short` | `174.50` | 104,720,000.00 USD | 557,520.00 USD | 0.00 USD | `+72.60%` | `3,194.96` |
| `Live` | `Short` | `175.50` | 104,730,000.00 USD | 4,880.00 USD | 0.00 USD | `+73.59%` | `27.80` |
| `Live` | `Short` | `176.50` | 104,760,000.00 USD | 27,570.00 USD | 0.00 USD | `+74.58%` | `156.23` |
| `Live` | `Short` | `177.50` | 104,830,000.00 USD | 78,100.00 USD | 0.00 USD | `+75.57%` | `440.00` |
| `Live` | `Short` | `178.50` | 107,820,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+76.56%` | `16,710.60` |
| `Live` | `Short` | `179.50` | 107,820,000.00 USD | 829.29 USD | 0.00 USD | `+77.54%` | `4.62` |
| `Live` | `Short` | `180.50` | 107,830,000.00 USD | 13,820.00 USD | 0.00 USD | `+78.53%` | `76.54` |
| `Live` | `Short` | `181.50` | 107,840,000.00 USD | 11,650.00 USD | 0.00 USD | `+79.52%` | `64.21` |
| `Live` | `Short` | `182.50` | 108,140,000.00 USD | 297,920.00 USD | 0.00 USD | `+80.51%` | `1,632.44` |
| `Live` | `Short` | `183.50` | 108,510,000.00 USD | 372,500.00 USD | 0.00 USD | `+81.50%` | `2,030.00` |
| `Live` | `Short` | `184.50` | 108,680,000.00 USD | 165,370.00 USD | 0.00 USD | `+82.49%` | `896.30` |
| `Live` | `Short` | `185.50` | 108,890,000.00 USD | 206,840.00 USD | 0.00 USD | `+83.48%` | `1,115.02` |
| `Live` | `Short` | `186.50` | 109,660,000.00 USD | 774,320.00 USD | 0.00 USD | `+84.47%` | `4,151.86` |
| `Live` | `Short` | `187.50` | 109,700,000.00 USD | 41,020.00 USD | 0.00 USD | `+85.46%` | `218.77` |
| `Live` | `Short` | `188.50` | 109,890,000.00 USD | 187,240.00 USD | 0.00 USD | `+86.45%` | `993.33` |
| `Live` | `Short` | `189.50` | 110,240,000.00 USD | 349,140.00 USD | 0.00 USD | `+87.44%` | `1,842.41` |
| `Live` | `Short` | `190.50` | 124,120,000.00 USD | 13,880,000.00 USD | 0.00 USD | `+88.42%` | `72,853.82` |
| `Live` | `Short` | `191.50` | 124,120,000.00 USD | 321.72 USD | 0.00 USD | `+89.41%` | `1.68` |
| `Live` | `Short` | `192.50` | 124,230,000.00 USD | 109,870.00 USD | 0.00 USD | `+90.40%` | `570.74` |
| `Live` | `Short` | `193.50` | 124,370,000.00 USD | 144,570.00 USD | 0.00 USD | `+91.39%` | `747.11` |
| `Live` | `Short` | `194.50` | 124,520,000.00 USD | 148,800.00 USD | 0.00 USD | `+92.38%` | `765.03` |
| `Live` | `Short` | `195.50` | 124,580,000.00 USD | 62,580.00 USD | 0.00 USD | `+93.37%` | `320.12` |
| `Live` | `Short` | `196.50` | 124,600,000.00 USD | 15,680.00 USD | 0.00 USD | `+94.36%` | `79.79` |
| `Live` | `Short` | `197.50` | 124,840,000.00 USD | 246,140.00 USD | 0.00 USD | `+95.35%` | `1,246.30` |
| `Live` | `Short` | `198.50` | 124,930,000.00 USD | 84,450.00 USD | 0.00 USD | `+96.34%` | `425.42` |
| `Live` | `Short` | `199.50` | 124,980,000.00 USD | 53,380.00 USD | 0.00 USD | `+97.33%` | `267.58` |
| `Live` | `Short` | `200.50` | 125,300,000.00 USD | 314,450.00 USD | 0.00 USD | `+98.32%` | `1,568.35` |
| `Live` | `Short` | `201.50` | 125,310,000.00 USD | 9,970.00 USD | 0.00 USD | `+99.30%` | `49.48` |
| `Live` | `Short` | `202.50` | 129,620,000.00 USD | 4,310,000.00 USD | 0.00 USD | `+100.29%` | `21,284.01` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.50` | 12,730,000.00 USD | 0.00 USD | 15,460.00 USD | `-76.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.50` | 12,710,000.00 USD | 0.00 USD | 3,830.00 USD | `-74.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.50` | 12,710,000.00 USD | 0.00 USD | 105.20 USD | `-73.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.50` | 12,710,000.00 USD | 0.00 USD | 527.35 USD | `-69.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.50` | 12,710,000.00 USD | 0.00 USD | 829.46 USD | `-66.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.50` | 12,710,000.00 USD | 0.00 USD | 1,320.00 USD | `-65.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.50` | 12,710,000.00 USD | 0.00 USD | 199.88 USD | `-62.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.50` | 12,710,000.00 USD | 0.00 USD | 205.21 USD | `-61.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.50` | 12,710,000.00 USD | 0.00 USD | 3,620.00 USD | `-60.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.50` | 12,700,000.00 USD | 0.00 USD | 423.63 USD | `-59.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.50` | 12,700,000.00 USD | 0.00 USD | 170,330.00 USD | `-57.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.50` | 12,530,000.00 USD | 0.00 USD | 104.40 USD | `-56.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.50` | 12,530,000.00 USD | 0.00 USD | 64,090.00 USD | `-55.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.50` | 12,470,000.00 USD | 0.00 USD | 249.71 USD | `-54.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.50` | 12,470,000.00 USD | 0.00 USD | 332.50 USD | `-53.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.50` | 12,470,000.00 USD | 0.00 USD | 102.82 USD | `-52.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.50` | 12,470,000.00 USD | 0.00 USD | 5,510.00 USD | `-50.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.50` | 12,460,000.00 USD | 0.00 USD | 4,070.00 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.50` | 12,460,000.00 USD | 0.00 USD | 427.88 USD | `-48.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.50` | 12,460,000.00 USD | 0.00 USD | 26,860.00 USD | `-47.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.50` | 12,430,000.00 USD | 0.00 USD | 785.89 USD | `-46.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.50` | 12,430,000.00 USD | 0.00 USD | 210.90 USD | `-45.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.50` | 12,430,000.00 USD | 0.00 USD | 5,860.00 USD | `-44.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.50` | 12,420,000.00 USD | 0.00 USD | 6,550.00 USD | `-43.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.50` | 12,420,000.00 USD | 0.00 USD | 159.71 USD | `-42.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.50` | 12,420,000.00 USD | 0.00 USD | 10,860.00 USD | `-41.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.50` | 12,410,000.00 USD | 0.00 USD | 40,470.00 USD | `-40.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.50` | 12,370,000.00 USD | 0.00 USD | 18,990.00 USD | `-39.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.50` | 12,350,000.00 USD | 0.00 USD | 4,810.00 USD | `-38.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.50` | 12,340,000.00 USD | 0.00 USD | 13,260.00 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.50` | 12,330,000.00 USD | 0.00 USD | 129.00 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.50` | 12,330,000.00 USD | 0.00 USD | 4,650.00 USD | `-35.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.50` | 12,320,000.00 USD | 0.00 USD | 7,690.00 USD | `-34.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.50` | 12,320,000.00 USD | 0.00 USD | 607.50 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.50` | 12,320,000.00 USD | 0.00 USD | 7,360.00 USD | `-32.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.50` | 12,310,000.00 USD | 0.00 USD | 54,850.00 USD | `-31.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.50` | 12,250,000.00 USD | 0.00 USD | 50,700.00 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.50` | 12,200,000.00 USD | 0.00 USD | 1,470.00 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.50` | 12,200,000.00 USD | 0.00 USD | 120,230.00 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.50` | 12,080,000.00 USD | 0.00 USD | 139.65 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.50` | 12,080,000.00 USD | 0.00 USD | 52,170.00 USD | `-26.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.50` | 12,030,000.00 USD | 0.00 USD | 26,730.00 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.50` | 12,000,000.00 USD | 0.00 USD | 16,050.00 USD | `-24.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.50` | 11,990,000.00 USD | 0.00 USD | 14,790.00 USD | `-23.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.50` | 11,970,000.00 USD | 0.00 USD | 81,220.00 USD | `-22.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.50` | 11,890,000.00 USD | 0.00 USD | 13,780.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.50` | 11,880,000.00 USD | 0.00 USD | 118,650.00 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.50` | 11,760,000.00 USD | 0.00 USD | 91,450.00 USD | `-19.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.50` | 11,670,000.00 USD | 0.00 USD | 27,520.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.50` | 11,640,000.00 USD | 0.00 USD | 74,090.00 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.50` | 11,560,000.00 USD | 0.00 USD | 24,890.00 USD | `-16.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.50` | 11,540,000.00 USD | 0.00 USD | 171,750.00 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.50` | 11,370,000.00 USD | 0.00 USD | 16,860.00 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.50` | 11,350,000.00 USD | 0.00 USD | 233,390.00 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.50` | 11,120,000.00 USD | 0.00 USD | 281,840.00 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.50` | 10,840,000.00 USD | 0.00 USD | 69,740.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.50` | 10,770,000.00 USD | 0.00 USD | 175,260.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.50` | 10,590,000.00 USD | 0.00 USD | 435,590.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.50` | 10,150,000.00 USD | 0.00 USD | 224,950.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.50` | 9,930,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.50` | 8,860,000.00 USD | 0.00 USD | 591,380.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.50` | 8,270,000.00 USD | 0.00 USD | 976,790.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.50` | 7,290,000.00 USD | 0.00 USD | 604,550.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.50` | 6,680,000.00 USD | 0.00 USD | 491,960.00 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.50` | 6,190,000.00 USD | 0.00 USD | 3,480,000.00 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.50` | 2,710,000.00 USD | 0.00 USD | 910,510.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `100.50` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.50` | 797,300.00 USD | 797,300.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.50` | 1,600,000.00 USD | 805,020.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.50` | 1,950,000.00 USD | 348,530.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.50` | 2,690,000.00 USD | 742,710.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.50` | 3,130,000.00 USD | 438,000.00 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.50` | 3,500,000.00 USD | 364,850.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.50` | 3,710,000.00 USD | 210,000.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.50` | 4,070,000.00 USD | 359,420.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.50` | 8,370,000.00 USD | 4,300,000.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.50` | 9,750,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+9.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.50` | 9,800,000.00 USD | 54,160.00 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.50` | 10,030,000.00 USD | 222,460.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.50` | 10,310,000.00 USD | 281,630.00 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.50` | 10,340,000.00 USD | 32,520.00 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.50` | 10,460,000.00 USD | 119,540.00 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.50` | 10,510,000.00 USD | 47,920.00 USD | 0.00 USD | `+15.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.50` | 10,760,000.00 USD | 254,840.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.50` | 10,940,000.00 USD | 178,980.00 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.50` | 11,180,000.00 USD | 239,490.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.50` | 11,330,000.00 USD | 153,100.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.50` | 11,410,000.00 USD | 75,990.00 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.50` | 11,940,000.00 USD | 526,980.00 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.50` | 13,000,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.50` | 13,170,000.00 USD | 166,110.00 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.50` | 13,720,000.00 USD | 554,500.00 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.50` | 13,840,000.00 USD | 114,230.00 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.50` | 14,110,000.00 USD | 275,030.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.50` | 14,170,000.00 USD | 58,000.00 USD | 0.00 USD | `+27.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.50` | 16,830,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.50` | 16,890,000.00 USD | 54,500.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.50` | 17,060,000.00 USD | 179,050.00 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.50` | 17,090,000.00 USD | 26,010.00 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.50` | 17,100,000.00 USD | 13,090.00 USD | 0.00 USD | `+32.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.50` | 17,350,000.00 USD | 250,620.00 USD | 0.00 USD | `+33.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.50` | 17,430,000.00 USD | 74,880.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.50` | 17,430,000.00 USD | 3,770.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.50` | 17,470,000.00 USD | 34,120.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.50` | 24,230,000.00 USD | 6,760,000.00 USD | 0.00 USD | `+36.99%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `139.50` | 26,440,000.00 USD | 2,220,000.00 USD | 0.00 USD | `+37.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.50` | 26,730,000.00 USD | 286,300.00 USD | 0.00 USD | `+38.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.50` | 26,740,000.00 USD | 10,520.00 USD | 0.00 USD | `+39.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.50` | 27,080,000.00 USD | 346,440.00 USD | 0.00 USD | `+40.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.50` | 27,080,000.00 USD | 529.51 USD | 0.00 USD | `+41.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.50` | 27,350,000.00 USD | 269,670.00 USD | 0.00 USD | `+42.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.50` | 27,370,000.00 USD | 13,070.00 USD | 0.00 USD | `+43.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.50` | 27,570,000.00 USD | 198,500.00 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.50` | 27,610,000.00 USD | 46,350.00 USD | 0.00 USD | `+45.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.50` | 28,950,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.50` | 29,460,000.00 USD | 512,760.00 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.50` | 29,730,000.00 USD | 269,220.00 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.50` | 29,750,000.00 USD | 16,890.00 USD | 0.00 USD | `+49.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.50` | 29,760,000.00 USD | 12,020.00 USD | 0.00 USD | `+50.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.50` | 29,770,000.00 USD | 11,660.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.50` | 29,780,000.00 USD | 12,130.00 USD | 0.00 USD | `+52.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.50` | 29,790,000.00 USD | 13,650.00 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.50` | 29,800,000.00 USD | 2,230.00 USD | 0.00 USD | `+54.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.50` | 29,820,000.00 USD | 22,350.00 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.50` | 29,820,000.00 USD | 815.04 USD | 0.00 USD | `+57.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.50` | 30,060,000.00 USD | 242,540.00 USD | 0.00 USD | `+58.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.50` | 30,060,000.00 USD | 282.62 USD | 0.00 USD | `+59.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.50` | 30,070,000.00 USD | 5,030.00 USD | 0.00 USD | `+61.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.50` | 30,150,000.00 USD | 83,570.00 USD | 0.00 USD | `+63.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.50` | 30,150,000.00 USD | 517.81 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.50` | 30,150,000.00 USD | 2,030.00 USD | 0.00 USD | `+65.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.50` | 30,160,000.00 USD | 5,560.00 USD | 0.00 USD | `+66.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.50` | 30,160,000.00 USD | 1,410.00 USD | 0.00 USD | `+67.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.50` | 30,200,000.00 USD | 42,950.00 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.50` | 30,200,000.00 USD | 686.00 USD | 0.00 USD | `+69.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.50` | 30,240,000.00 USD | 36,070.00 USD | 0.00 USD | `+70.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.50` | 30,250,000.00 USD | 6,550.00 USD | 0.00 USD | `+71.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.50` | 30,320,000.00 USD | 74,640.00 USD | 0.00 USD | `+73.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.50` | 30,320,000.00 USD | 1,450.00 USD | 0.00 USD | `+74.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.50` | 30,330,000.00 USD | 2,140.00 USD | 0.00 USD | `+75.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.50` | 30,330,000.00 USD | 2,990.00 USD | 0.00 USD | `+76.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.50` | 30,330,000.00 USD | 262.07 USD | 0.00 USD | `+77.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.50` | 30,430,000.00 USD | 102,680.00 USD | 0.00 USD | `+78.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.50` | 30,430,000.00 USD | 2,730.00 USD | 0.00 USD | `+79.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.50` | 30,450,000.00 USD | 19,620.00 USD | 0.00 USD | `+80.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.50` | 31,000,000.00 USD | 550,500.00 USD | 0.00 USD | `+81.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.50` | 31,030,000.00 USD | 29,490.00 USD | 0.00 USD | `+83.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.50` | 31,220,000.00 USD | 191,020.00 USD | 0.00 USD | `+85.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.50` | 31,370,000.00 USD | 141,530.00 USD | 0.00 USD | `+86.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.50` | 31,410,000.00 USD | 38,960.00 USD | 0.00 USD | `+88.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.50` | 31,410,000.00 USD | 4,280.00 USD | 0.00 USD | `+92.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.50` | 31,410,000.00 USD | 1,760.00 USD | 0.00 USD | `+93.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `196.50` | 31,670,000.00 USD | 253,980.00 USD | 0.00 USD | `+94.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.50` | 31,760,000.00 USD | 94,590.00 USD | 0.00 USD | `+95.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.50` | 32,130,000.00 USD | 374,220.00 USD | 0.00 USD | `+96.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.50` | 32,160,000.00 USD | 28,310.00 USD | 0.00 USD | `+97.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `200.50` | 32,470,000.00 USD | 302,560.00 USD | 0.00 USD | `+98.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `201.50` | 32,470,000.00 USD | 398.97 USD | 0.00 USD | `+99.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `202.50` | 32,470,000.00 USD | 2,430.00 USD | 0.00 USD | `+100.29%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `89.90` | 371,170,000.00 USD | 0.00 USD | 371,170,000.00 USD | 525,310.00 USD | 459,170.00 USD | 925,200.00 USD |
| `7D` | `90.10` | 369,260,000.00 USD | 0.00 USD | 369,260,000.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD |
| `1D` | `90.30` | 180,280,000.00 USD | 0.00 USD | 180,280,000.00 USD | 362,900.00 USD | 537,500.00 USD | 506,490.00 USD |
| `7D` | `90.30` | 367,180,000.00 USD | 0.00 USD | 367,180,000.00 USD | 703,270.00 USD | 342,020.00 USD | 654,780.00 USD |
| `1D` | `90.50` | 178,870,000.00 USD | 0.00 USD | 178,870,000.00 USD | 523,240.00 USD | 399,670.00 USD | 473,640.00 USD |
| `7D` | `90.50` | 365,480,000.00 USD | 0.00 USD | 365,480,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD |
| `1D` | `90.70` | 177,470,000.00 USD | 0.00 USD | 177,470,000.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `90.70` | 362,800,000.00 USD | 0.00 USD | 362,800,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `90.90` | 176,970,000.00 USD | 0.00 USD | 176,970,000.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `90.90` | 360,350,000.00 USD | 0.00 USD | 360,350,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `91.10` | 176,870,000.00 USD | 0.00 USD | 176,870,000.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `91.10` | 357,970,000.00 USD | 0.00 USD | 357,970,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `91.30` | 176,680,000.00 USD | 0.00 USD | 176,680,000.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD |
| `7D` | `91.30` | 356,060,000.00 USD | 0.00 USD | 356,060,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `91.50` | 176,530,000.00 USD | 0.00 USD | 176,530,000.00 USD | 21,670.00 USD | 87,530.00 USD | 1,730.00 USD |
| `7D` | `91.50` | 353,560,000.00 USD | 0.00 USD | 353,560,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD |
| `1D` | `91.70` | 176,420,000.00 USD | 0.00 USD | 176,420,000.00 USD | 107,440.00 USD | 112,260.00 USD | 1,080.00 USD |
| `7D` | `91.70` | 350,650,000.00 USD | 0.00 USD | 350,650,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `91.90` | 176,200,000.00 USD | 0.00 USD | 176,200,000.00 USD | 187,160.00 USD | 63,660.00 USD | 177,950.00 USD |
| `7D` | `91.90` | 349,020,000.00 USD | 0.00 USD | 349,020,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `1D` | `92.10` | 175,770,000.00 USD | 0.00 USD | 175,770,000.00 USD | 161,220.00 USD | 124,560.00 USD | 64,070.00 USD |
| `7D` | `92.10` | 346,600,000.00 USD | 0.00 USD | 346,600,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `1D` | `92.30` | 175,420,000.00 USD | 0.00 USD | 175,420,000.00 USD | 219,340.00 USD | 97,250.00 USD | 738,010.00 USD |
| `7D` | `92.30` | 345,290,000.00 USD | 0.00 USD | 345,290,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,200,000.00 USD |
| `1D` | `92.50` | 174,370,000.00 USD | 0.00 USD | 174,370,000.00 USD | 37,670.00 USD | 53,380.00 USD | 168,480.00 USD |
| `7D` | `92.50` | 343,280,000.00 USD | 0.00 USD | 343,280,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `1D` | `92.70` | 174,110,000.00 USD | 0.00 USD | 174,110,000.00 USD | 0.00 USD | 86,970.00 USD | 168,150.00 USD |
| `7D` | `92.70` | 341,880,000.00 USD | 0.00 USD | 341,880,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `1D` | `92.90` | 173,850,000.00 USD | 0.00 USD | 173,850,000.00 USD | 100,830.00 USD | 0.00 USD | 60,580.00 USD |
| `7D` | `92.90` | 341,610,000.00 USD | 0.00 USD | 341,610,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `1D` | `93.10` | 173,690,000.00 USD | 0.00 USD | 173,690,000.00 USD | 0.00 USD | 2,580.00 USD | 115,350.00 USD |
| `7D` | `93.10` | 341,550,000.00 USD | 0.00 USD | 341,550,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |
| `1D` | `93.30` | 173,570,000.00 USD | 0.00 USD | 173,570,000.00 USD | 0.00 USD | 103,020.00 USD | 99,970.00 USD |
| `7D` | `93.30` | 341,160,000.00 USD | 0.00 USD | 341,160,000.00 USD | 55,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `93.50` | 341,050,000.00 USD | 0.00 USD | 341,050,000.00 USD | 101,820.00 USD | 335,760.00 USD | 2,240.00 USD |
| `7D` | `93.70` | 340,610,000.00 USD | 0.00 USD | 340,610,000.00 USD | 270,240.00 USD | 262,300.00 USD | 115,880.00 USD |
| `7D` | `93.90` | 339,960,000.00 USD | 0.00 USD | 339,960,000.00 USD | 236,340.00 USD | 90,940.00 USD | 214,850.00 USD |
| `7D` | `94.10` | 339,420,000.00 USD | 0.00 USD | 339,420,000.00 USD | 233,120.00 USD | 296,810.00 USD | 321,280.00 USD |
| `7D` | `94.30` | 338,570,000.00 USD | 0.00 USD | 338,570,000.00 USD | 10,610.00 USD | 0.00 USD | 44,740.00 USD |
| `7D` | `94.50` | 338,510,000.00 USD | 0.00 USD | 338,510,000.00 USD | 183,750.00 USD | 0.00 USD | 140,220.00 USD |
| `7D` | `94.90` | 338,190,000.00 USD | 0.00 USD | 338,190,000.00 USD | 297,690.00 USD | 444,840.00 USD | 18,350.00 USD |
| `1D` | `95.10` | 173,370,000.00 USD | 0.00 USD | 173,370,000.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `95.10` | 337,430,000.00 USD | 0.00 USD | 337,430,000.00 USD | 141,070.00 USD | 115,890.00 USD | 9,610.00 USD |
| `1D` | `95.30` | 173,360,000.00 USD | 0.00 USD | 173,360,000.00 USD | 18,710.00 USD | 89,760.00 USD | 6,930.00 USD |
| `7D` | `95.30` | 337,160,000.00 USD | 0.00 USD | 337,160,000.00 USD | 251,720.00 USD | 196,820.00 USD | 474,750.00 USD |
| `1D` | `95.50` | 173,240,000.00 USD | 0.00 USD | 173,240,000.00 USD | 679,320.00 USD | 458,400.00 USD | 465,470.00 USD |
| `7D` | `95.50` | 336,240,000.00 USD | 0.00 USD | 336,240,000.00 USD | 1,000,000.00 USD | 732,540.00 USD | 341,230.00 USD |
| `1D` | `95.70` | 171,640,000.00 USD | 0.00 USD | 171,640,000.00 USD | 1,490,000.00 USD | 1,130,000.00 USD | 649,920.00 USD |
| `7D` | `95.70` | 334,160,000.00 USD | 0.00 USD | 334,160,000.00 USD | 1,980,000.00 USD | 1,130,000.00 USD | 1,450,000.00 USD |
| `1D` | `95.90` | 168,370,000.00 USD | 0.00 USD | 168,370,000.00 USD | 1,150,000.00 USD | 885,010.00 USD | 1,240,000.00 USD |
| `7D` | `95.90` | 329,600,000.00 USD | 0.00 USD | 329,600,000.00 USD | 1,610,000.00 USD | 1,260,000.00 USD | 2,660,000.00 USD |
| `1D` | `96.10` | 165,100,000.00 USD | 0.00 USD | 165,100,000.00 USD | 1,430,000.00 USD | 1,420,000.00 USD | 942,310.00 USD |
| `7D` | `96.10` | 324,070,000.00 USD | 0.00 USD | 324,070,000.00 USD | 2,910,000.00 USD | 2,330,000.00 USD | 2,640,000.00 USD |
| `1D` | `96.30` | 161,310,000.00 USD | 0.00 USD | 161,310,000.00 USD | 875,730.00 USD | 1,150,000.00 USD | 1,180,000.00 USD |
| `7D` | `96.30` | 316,190,000.00 USD | 0.00 USD | 316,190,000.00 USD | 2,910,000.00 USD | 1,170,000.00 USD | 2,170,000.00 USD |
| `1D` | `96.50` | 158,110,000.00 USD | 0.00 USD | 158,110,000.00 USD | 1,370,000.00 USD | 924,880.00 USD | 1,350,000.00 USD |
| `7D` | `96.50` | 309,940,000.00 USD | 0.00 USD | 309,940,000.00 USD | 2,870,000.00 USD | 1,580,000.00 USD | 2,580,000.00 USD |
| `1D` | `96.70` | 154,470,000.00 USD | 0.00 USD | 154,470,000.00 USD | 681,660.00 USD | 858,670.00 USD | 909,580.00 USD |
| `7D` | `96.70` | 302,910,000.00 USD | 0.00 USD | 302,910,000.00 USD | 2,220,000.00 USD | 2,450,000.00 USD | 2,360,000.00 USD |
| `1D` | `96.90` | 152,020,000.00 USD | 0.00 USD | 152,020,000.00 USD | 383,880.00 USD | 290,640.00 USD | 167,820.00 USD |
| `7D` | `96.90` | 295,870,000.00 USD | 0.00 USD | 295,870,000.00 USD | 5,140,000.00 USD | 3,170,000.00 USD | 3,350,000.00 USD |
| `1D` | `97.10` | 151,170,000.00 USD | 0.00 USD | 151,170,000.00 USD | 271,410.00 USD | 113,790.00 USD | 379,350.00 USD |
| `7D` | `97.10` | 284,210,000.00 USD | 0.00 USD | 284,210,000.00 USD | 4,430,000.00 USD | 2,080,000.00 USD | 1,660,000.00 USD |
| `1D` | `97.30` | 150,410,000.00 USD | 0.00 USD | 150,410,000.00 USD | 197,550.00 USD | 378,560.00 USD | 121,680.00 USD |
| `7D` | `97.30` | 276,050,000.00 USD | 0.00 USD | 276,050,000.00 USD | 5,780,000.00 USD | 4,270,000.00 USD | 3,750,000.00 USD |
| `1D` | `97.50` | 149,710,000.00 USD | 0.00 USD | 149,710,000.00 USD | 1,460,000.00 USD | 1,060,000.00 USD | 960,650.00 USD |
| `7D` | `97.50` | 262,250,000.00 USD | 0.00 USD | 262,250,000.00 USD | 4,390,000.00 USD | 4,370,000.00 USD | 4,390,000.00 USD |
| `1D` | `97.70` | 146,220,000.00 USD | 0.00 USD | 146,220,000.00 USD | 3,200,000.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `7D` | `97.70` | 249,100,000.00 USD | 0.00 USD | 249,100,000.00 USD | 5,660,000.00 USD | 3,410,000.00 USD | 5,400,000.00 USD |
| `1D` | `97.90` | 138,930,000.00 USD | 0.00 USD | 138,930,000.00 USD | 3,030,000.00 USD | 2,300,000.00 USD | 2,740,000.00 USD |
| `7D` | `97.90` | 234,630,000.00 USD | 0.00 USD | 234,630,000.00 USD | 8,020,000.00 USD | 6,060,000.00 USD | 7,190,000.00 USD |
| `1D` | `98.10` | 130,870,000.00 USD | 0.00 USD | 130,870,000.00 USD | 3,360,000.00 USD | 3,450,000.00 USD | 2,510,000.00 USD |
| `7D` | `98.10` | 213,350,000.00 USD | 0.00 USD | 213,350,000.00 USD | 8,580,000.00 USD | 7,190,000.00 USD | 7,130,000.00 USD |
| `1D` | `98.30` | 121,550,000.00 USD | 0.00 USD | 121,550,000.00 USD | 2,760,000.00 USD | 2,960,000.00 USD | 2,690,000.00 USD |
| `7D` | `98.30` | 190,450,000.00 USD | 0.00 USD | 190,450,000.00 USD | 7,530,000.00 USD | 4,040,000.00 USD | 7,420,000.00 USD |
| `1D` | `98.50` | 113,150,000.00 USD | 0.00 USD | 113,150,000.00 USD | 6,160,000.00 USD | 3,960,000.00 USD | 6,330,000.00 USD |
| `7D` | `98.50` | 171,470,000.00 USD | 0.00 USD | 171,470,000.00 USD | 10,550,000.00 USD | 7,040,000.00 USD | 9,060,000.00 USD |
| `1D` | `98.70` | 96,710,000.00 USD | 0.00 USD | 96,710,000.00 USD | 7,440,000.00 USD | 6,270,000.00 USD | 4,920,000.00 USD |
| `7D` | `98.70` | 144,820,000.00 USD | 0.00 USD | 144,820,000.00 USD | 11,830,000.00 USD | 9,800,000.00 USD | 13,480,000.00 USD |
| `1D` | `98.90` | 78,070,000.00 USD | 0.00 USD | 78,070,000.00 USD | 5,040,000.00 USD | 4,270,000.00 USD | 5,750,000.00 USD |
| `7D` | `98.90` | 109,700,000.00 USD | 0.00 USD | 109,700,000.00 USD | 15,300,000.00 USD | 9,640,000.00 USD | 17,510,000.00 USD |
| `1D` | `99.10` | 63,020,000.00 USD | 0.00 USD | 63,020,000.00 USD | 6,070,000.00 USD | 5,760,000.00 USD | 4,720,000.00 USD |
| `7D` | `99.10` | 67,260,000.00 USD | 0.00 USD | 67,260,000.00 USD | 18,940,000.00 USD | 12,780,000.00 USD | 10,390,000.00 USD |
| `1D` | `99.30` | 46,460,000.00 USD | 0.00 USD | 46,460,000.00 USD | 3,310,000.00 USD | 4,420,000.00 USD | 4,970,000.00 USD |
| `7D` | `99.30` | 25,160,000.00 USD | 0.00 USD | 25,160,000.00 USD | 3,040,000.00 USD | 1,180,000.00 USD | 6,080,000.00 USD |
| `1D` | `99.50` | 33,760,000.00 USD | 0.00 USD | 33,760,000.00 USD | 5,190,000.00 USD | 3,860,000.00 USD | 5,240,000.00 USD |
| `7D` | `99.50` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 1,370,000.00 USD | 1,380,000.00 USD | 2,950,000.00 USD |
| `1D` | `99.70` | 19,470,000.00 USD | 0.00 USD | 19,470,000.00 USD | 2,480,000.00 USD | 3,410,000.00 USD | 3,230,000.00 USD |
| `7D` | `99.70` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 661,070.00 USD | 1,650,000.00 USD | 2,240,000.00 USD |
| `1D` | `99.90` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 1,650,000.00 USD | 1,300,000.00 USD | 1,100,000.00 USD |
| `7D` | `99.90` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 843,730.00 USD | 0.00 USD | 531,900.00 USD |
| `1D` | `100.10` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 1,290,000.00 USD | 914,930.00 USD | 1,430,000.00 USD |
| `7D` | `100.10` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 533,430.00 USD | 36,980.00 USD | 1,040,000.00 USD |
| `1D` | `100.30` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 163,250.00 USD | 167,670.00 USD | 5,240.00 USD |
| `7D` | `100.30` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 39,280.00 USD | 68,710.00 USD | 0.00 USD |
| `1D` | `100.50` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 2,320,000.00 USD |
| `7D` | `100.50` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 39,680.00 USD | 0.00 USD | 1,480,000.00 USD |
| `1D` | `100.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `100.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `100.70` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 274,280.00 USD | 970,010.00 USD | 476,700.00 USD |
| `7D` | `100.70` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 46,010.00 USD | 1,230,000.00 USD | 0.00 USD |
| `1D` | `100.90` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 953,600.00 USD | 5,230.00 USD |
| `7D` | `100.90` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 1,610,000.00 USD | 3,730,000.00 USD |
| `1D` | `101.10` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 4,870,000.00 USD | 3,090,000.00 USD | 0.00 USD |
| `7D` | `101.10` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 3,710,000.00 USD | 0.00 USD |
| `1D` | `101.30` | 19,590,000.00 USD | 19,590,000.00 USD | 0.00 USD | 2,660,000.00 USD | 3,940,000.00 USD | 2,350,000.00 USD |
| `7D` | `101.30` | 22,770,000.00 USD | 22,770,000.00 USD | 0.00 USD | 4,480,000.00 USD | 2,460,000.00 USD | 5,500,000.00 USD |
| `1D` | `101.50` | 34,430,000.00 USD | 34,430,000.00 USD | 0.00 USD | 1,940,000.00 USD | 3,350,000.00 USD | 9,540,000.00 USD |
| `7D` | `101.50` | 34,390,000.00 USD | 34,390,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 9,060,000.00 USD |
| `1D` | `101.70` | 47,750,000.00 USD | 47,750,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 8,900,000.00 USD |
| `7D` | `101.70` | 43,730,000.00 USD | 43,730,000.00 USD | 0.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD |
| `1D` | `101.90` | 52,280,000.00 USD | 52,280,000.00 USD | 0.00 USD | 1,320,000.00 USD | 142,780.00 USD | 3,070,000.00 USD |
| `7D` | `101.90` | 50,190,000.00 USD | 50,190,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 3,790,000.00 USD |
| `1D` | `102.10` | 53,900,000.00 USD | 53,900,000.00 USD | 0.00 USD | 407,760.00 USD | 439,590.00 USD | 768,500.00 USD |
| `7D` | `102.10` | 52,910,000.00 USD | 52,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,720,000.00 USD |
| `1D` | `102.30` | 58,220,000.00 USD | 58,220,000.00 USD | 0.00 USD | 799,010.00 USD | 1,180,000.00 USD | 2,350,000.00 USD |
| `7D` | `102.30` | 56,810,000.00 USD | 56,810,000.00 USD | 0.00 USD | 1,520,000.00 USD | 578,040.00 USD | 1,800,000.00 USD |
| `1D` | `102.50` | 60,200,000.00 USD | 60,200,000.00 USD | 0.00 USD | 992,380.00 USD | 292,190.00 USD | 696,950.00 USD |
| `7D` | `102.50` | 59,350,000.00 USD | 59,350,000.00 USD | 0.00 USD | 680,620.00 USD | 1,280,000.00 USD | 582,270.00 USD |
| `1D` | `102.70` | 61,660,000.00 USD | 61,660,000.00 USD | 0.00 USD | 931,170.00 USD | 524,710.00 USD | 3,170.00 USD |
| `7D` | `102.70` | 60,080,000.00 USD | 60,080,000.00 USD | 0.00 USD | 722,800.00 USD | 0.00 USD | 7,680.00 USD |
| `1D` | `102.90` | 65,600,000.00 USD | 65,600,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,770,000.00 USD | 792,760.00 USD |
| `7D` | `102.90` | 79,590,000.00 USD | 79,590,000.00 USD | 0.00 USD | 16,450,000.00 USD | 0.00 USD | 3,060,000.00 USD |
| `1D` | `103.10` | 71,770,000.00 USD | 71,770,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,800,000.00 USD | 1,590,000.00 USD |
| `7D` | `103.10` | 84,970,000.00 USD | 84,970,000.00 USD | 0.00 USD | 4,750,000.00 USD | 4,380.00 USD | 616,540.00 USD |
| `1D` | `103.30` | 76,900,000.00 USD | 76,900,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,920,000.00 USD | 815,560.00 USD |
| `7D` | `103.30` | 102,570,000.00 USD | 102,570,000.00 USD | 0.00 USD | 17,450,000.00 USD | 9,520.00 USD | 140,130.00 USD |
| `1D` | `103.50` | 89,410,000.00 USD | 89,410,000.00 USD | 0.00 USD | 4,290,000.00 USD | 2,690,000.00 USD | 5,530,000.00 USD |
| `7D` | `103.50` | 124,070,000.00 USD | 124,070,000.00 USD | 0.00 USD | 13,580,000.00 USD | 1,770,000.00 USD | 6,150,000.00 USD |
| `1D` | `103.70` | 101,330,000.00 USD | 101,330,000.00 USD | 0.00 USD | 4,210,000.00 USD | 2,380,000.00 USD | 5,340,000.00 USD |
| `7D` | `103.70` | 136,290,000.00 USD | 136,290,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.90` | 110,650,000.00 USD | 110,650,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,080,000.00 USD | 3,530,000.00 USD |
| `7D` | `103.90` | 153,550,000.00 USD | 153,550,000.00 USD | 0.00 USD | 8,600,000.00 USD | 2,630,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.10` | 119,690,000.00 USD | 119,690,000.00 USD | 0.00 USD | 3,450,000.00 USD | 2,370,000.00 USD | 3,220,000.00 USD |
| `7D` | `104.10` | 181,320,000.00 USD | 181,320,000.00 USD | 0.00 USD | 10,840,000.00 USD | 8,150,000.00 USD | 8,780,000.00 USD |
| `1D` | `104.30` | 127,680,000.00 USD | 127,680,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,140,000.00 USD | 3,140,000.00 USD |
| `7D` | `104.30` | 201,630,000.00 USD | 201,630,000.00 USD | 0.00 USD | 6,740,000.00 USD | 6,260,000.00 USD | 7,320,000.00 USD |
| `1D` | `104.50` | 135,180,000.00 USD | 135,180,000.00 USD | 0.00 USD | 2,590,000.00 USD | 2,120,000.00 USD | 2,790,000.00 USD |
| `7D` | `104.50` | 213,360,000.00 USD | 213,360,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 4,980,000.00 USD |
| `1D` | `104.70` | 145,050,000.00 USD | 145,050,000.00 USD | 0.00 USD | 2,650,000.00 USD | 2,140,000.00 USD | 5,080,000.00 USD |
| `7D` | `104.70` | 233,360,000.00 USD | 233,360,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD |
| `1D` | `104.90` | 148,020,000.00 USD | 148,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 592,030.00 USD | 1,360,000.00 USD |
| `7D` | `104.90` | 253,960,000.00 USD | 253,960,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.10` | 150,460,000.00 USD | 150,460,000.00 USD | 0.00 USD | 421,810.00 USD | 622,250.00 USD | 1,400,000.00 USD |
| `7D` | `105.10` | 267,640,000.00 USD | 267,640,000.00 USD | 0.00 USD | 5,580,000.00 USD | 5,260,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.30` | 151,400,000.00 USD | 151,400,000.00 USD | 0.00 USD | 506,770.00 USD | 2,430.00 USD | 425,580.00 USD |
| `7D` | `105.30` | 274,040,000.00 USD | 274,040,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | 1,120,000.00 USD |
| `1D` | `105.50` | 152,450,000.00 USD | 152,450,000.00 USD | 0.00 USD | 157,550.00 USD | 209,490.00 USD | 684,590.00 USD |
| `7D` | `105.50` | 293,880,000.00 USD | 293,880,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,270,000.00 USD | 7,970,000.00 USD |
| `1D` | `105.70` | 153,780,000.00 USD | 153,780,000.00 USD | 0.00 USD | 294,800.00 USD | 506,510.00 USD | 529,580.00 USD |
| `7D` | `105.70` | 308,730,000.00 USD | 308,730,000.00 USD | 0.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | 5,260,000.00 USD |
| `1D` | `105.90` | 154,800,000.00 USD | 154,800,000.00 USD | 0.00 USD | 215,940.00 USD | 666,590.00 USD | 135,010.00 USD |
| `7D` | `105.90` | 319,270,000.00 USD | 319,270,000.00 USD | 0.00 USD | 3,930,000.00 USD | 2,260,000.00 USD | 4,350,000.00 USD |
| `1D` | `106.10` | 156,310,000.00 USD | 156,310,000.00 USD | 0.00 USD | 716,050.00 USD | 529,140.00 USD | 267,330.00 USD |
| `7D` | `106.10` | 332,730,000.00 USD | 332,730,000.00 USD | 0.00 USD | 6,810,000.00 USD | 3,690,000.00 USD | 2,960,000.00 USD |
| `1D` | `106.30` | 158,050,000.00 USD | 158,050,000.00 USD | 0.00 USD | 499,810.00 USD | 619,440.00 USD | 622,260.00 USD |
| `7D` | `106.30` | 344,020,000.00 USD | 344,020,000.00 USD | 0.00 USD | 5,120,000.00 USD | 3,230,000.00 USD | 2,940,000.00 USD |
| `1D` | `106.50` | 159,730,000.00 USD | 159,730,000.00 USD | 0.00 USD | 1,010,000.00 USD | 336,210.00 USD | 333,130.00 USD |
| `7D` | `106.50` | 349,990,000.00 USD | 349,990,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,010,000.00 USD | 2,230,000.00 USD |
| `1D` | `106.70` | 162,820,000.00 USD | 162,820,000.00 USD | 0.00 USD | 890,450.00 USD | 383,670.00 USD | 1,820,000.00 USD |
| `7D` | `106.70` | 359,720,000.00 USD | 359,720,000.00 USD | 0.00 USD | 2,290,000.00 USD | 3,150,000.00 USD | 4,290,000.00 USD |
| `1D` | `106.90` | 163,880,000.00 USD | 163,880,000.00 USD | 0.00 USD | 317,210.00 USD | 150,690.00 USD | 594,370.00 USD |
| `7D` | `106.90` | 365,500,000.00 USD | 365,500,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,120,000.00 USD | 3,470,000.00 USD |
| `1D` | `107.10` | 164,730,000.00 USD | 164,730,000.00 USD | 0.00 USD | 88,570.00 USD | 254,230.00 USD | 510,390.00 USD |
| `7D` | `107.10` | 368,900,000.00 USD | 368,900,000.00 USD | 0.00 USD | 1,630,000.00 USD | 508,540.00 USD | 1,260,000.00 USD |
| `1D` | `107.30` | 165,200,000.00 USD | 165,200,000.00 USD | 0.00 USD | 252,090.00 USD | 0.00 USD | 212,790.00 USD |
| `7D` | `107.30` | 369,060,000.00 USD | 369,060,000.00 USD | 0.00 USD | 0.00 USD | 156,300.00 USD | 0.00 USD |
| `1D` | `107.50` | 165,490,000.00 USD | 165,490,000.00 USD | 0.00 USD | 0.00 USD | 6,440.00 USD | 288,380.00 USD |
| `7D` | `107.50` | 370,040,000.00 USD | 370,040,000.00 USD | 0.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD |
| `1D` | `107.70` | 166,020,000.00 USD | 166,020,000.00 USD | 0.00 USD | 94,360.00 USD | 181,310.00 USD | 249,940.00 USD |
| `7D` | `107.70` | 371,010,000.00 USD | 371,010,000.00 USD | 0.00 USD | 523,660.00 USD | 11,530.00 USD | 432,310.00 USD |
| `1D` | `107.90` | 166,150,000.00 USD | 166,150,000.00 USD | 0.00 USD | 0.00 USD | 128,660.00 USD | 0.00 USD |
| `7D` | `107.90` | 371,180,000.00 USD | 371,180,000.00 USD | 0.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.10` | 372,810,000.00 USD | 372,810,000.00 USD | 0.00 USD | 707,230.00 USD | 915,170.00 USD | 7,940.00 USD |
| `7D` | `108.30` | 375,220,000.00 USD | 375,220,000.00 USD | 0.00 USD | 1,090,000.00 USD | 697,770.00 USD | 612,150.00 USD |
| `7D` | `108.50` | 376,930,000.00 USD | 376,930,000.00 USD | 0.00 USD | 835,610.00 USD | 340,050.00 USD | 540,760.00 USD |
| `7D` | `108.70` | 379,300,000.00 USD | 379,300,000.00 USD | 0.00 USD | 575,510.00 USD | 726,100.00 USD | 1,070,000.00 USD |
| `7D` | `108.90` | 380,600,000.00 USD | 380,600,000.00 USD | 0.00 USD | 414,890.00 USD | 701,350.00 USD | 181,660.00 USD |
| `1D` | `109.10` | 166,150,000.00 USD | 166,150,000.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `109.10` | 381,680,000.00 USD | 381,680,000.00 USD | 0.00 USD | 434,330.00 USD | 185,250.00 USD | 461,880.00 USD |
| `1D` | `109.30` | 166,290,000.00 USD | 166,290,000.00 USD | 0.00 USD | 126,020.00 USD | 9,360.00 USD | 2,950.00 USD |
| `7D` | `109.30` | 382,540,000.00 USD | 382,540,000.00 USD | 0.00 USD | 486,260.00 USD | 85,680.00 USD | 286,560.00 USD |
| `1D` | `109.50` | 166,550,000.00 USD | 166,550,000.00 USD | 0.00 USD | 133,350.00 USD | 84,430.00 USD | 44,310.00 USD |
| `7D` | `109.50` | 382,780,000.00 USD | 382,780,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `1D` | `109.70` | 167,460,000.00 USD | 167,460,000.00 USD | 0.00 USD | 456,990.00 USD | 277,760.00 USD | 171,080.00 USD |
| `7D` | `109.70` | 383,960,000.00 USD | 383,960,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `1D` | `109.90` | 168,400,000.00 USD | 168,400,000.00 USD | 0.00 USD | 268,320.00 USD | 266,300.00 USD | 405,440.00 USD |
| `7D` | `109.90` | 385,450,000.00 USD | 385,450,000.00 USD | 0.00 USD | 238,580.00 USD | 447,100.00 USD | 807,700.00 USD |
| `1D` | `110.10` | 169,440,000.00 USD | 169,440,000.00 USD | 0.00 USD | 258,510.00 USD | 467,380.00 USD | 313,070.00 USD |
| `7D` | `110.10` | 387,520,000.00 USD | 387,520,000.00 USD | 0.00 USD | 674,110.00 USD | 531,910.00 USD | 866,570.00 USD |
| `1D` | `110.30` | 170,430,000.00 USD | 170,430,000.00 USD | 0.00 USD | 238,980.00 USD | 342,030.00 USD | 406,900.00 USD |
| `7D` | `110.30` | 389,220,000.00 USD | 389,220,000.00 USD | 0.00 USD | 703,270.00 USD | 342,020.00 USD | 654,780.00 USD |
| `1D` | `110.50` | 171,080,000.00 USD | 171,080,000.00 USD | 0.00 USD | 300,210.00 USD | 150,770.00 USD | 197,150.00 USD |
| `7D` | `110.50` | 389,710,000.00 USD | 389,710,000.00 USD | 0.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD |
| `1D` | `110.70` | 171,820,000.00 USD | 171,820,000.00 USD | 0.00 USD | 223,030.00 USD | 248,900.00 USD | 276,490.00 USD |
| `7D` | `110.70` | 391,910,000.00 USD | 391,910,000.00 USD | 0.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD |
| `1D` | `110.90` | 172,330,000.00 USD | 172,330,000.00 USD | 0.00 USD | 55,550.00 USD | 244,840.00 USD | 201,330.00 USD |
| `7D` | `110.90` | 394,350,000.00 USD | 394,350,000.00 USD | 0.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `111.10` | 172,430,000.00 USD | 172,430,000.00 USD | 0.00 USD | 101,980.00 USD | 1,460.00 USD | 1,400.00 USD |
| `7D` | `111.10` | 396,740,000.00 USD | 396,740,000.00 USD | 0.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `111.30` | 172,610,000.00 USD | 172,610,000.00 USD | 0.00 USD | 53,030.00 USD | 769.97 USD | 129,600.00 USD |
| `7D` | `111.30` | 398,640,000.00 USD | 398,640,000.00 USD | 0.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `111.50` | 172,760,000.00 USD | 172,760,000.00 USD | 0.00 USD | 29,300.00 USD | 77,530.00 USD | 43,130.00 USD |
| `7D` | `111.50` | 401,150,000.00 USD | 401,150,000.00 USD | 0.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `111.70` | 172,790,000.00 USD | 172,790,000.00 USD | 0.00 USD | 0.00 USD | 27,410.00 USD | 641.98 USD |
| `7D` | `111.70` | 402,290,000.00 USD | 402,290,000.00 USD | 0.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD |
| `1D` | `111.90` | 172,880,000.00 USD | 172,880,000.00 USD | 0.00 USD | 21,670.00 USD | 60,130.00 USD | 1,090.00 USD |
| `7D` | `111.90` | 404,060,000.00 USD | 404,060,000.00 USD | 0.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD |
| `1D` | `112.10` | 173,100,000.00 USD | 173,100,000.00 USD | 0.00 USD | 107,440.00 USD | 112,260.00 USD | 1,080.00 USD |
| `7D` | `112.10` | 405,690,000.00 USD | 405,690,000.00 USD | 0.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `112.30` | 173,510,000.00 USD | 173,510,000.00 USD | 0.00 USD | 178,390.00 USD | 58,870.00 USD | 174,870.00 USD |
| `7D` | `112.30` | 408,100,000.00 USD | 408,100,000.00 USD | 0.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `7D` | `112.50` | 409,420,000.00 USD | 409,420,000.00 USD | 0.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `7D` | `112.70` | 409,940,000.00 USD | 409,940,000.00 USD | 0.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD |
| `7D` | `112.90` | 411,430,000.00 USD | 411,430,000.00 USD | 0.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD |
| `7D` | `113.10` | 412,820,000.00 USD | 412,820,000.00 USD | 0.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `7D` | `113.30` | 413,100,000.00 USD | 413,100,000.00 USD | 0.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `7D` | `113.50` | 413,160,000.00 USD | 413,160,000.00 USD | 0.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `7D` | `113.70` | 413,550,000.00 USD | 413,550,000.00 USD | 0.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.24B` | Total OI Tokens: `61,934,931.8 SOL`
  * 1h OI Change: `-0.16%` | 4h OI Change: `-3.18%` | 24h OI Change: `-2.61%`
  * Exchange Breakdown: Binance=`1.09B` | Bybit=`615.05M` | OKX=`353.60M` | Hyperliquid=`568.39M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `194.12K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `61.91%` | `38.09%` | `1.63` | 36,690,000.00 USD |
| `15M` | `Binance` | `56.77%` | `43.23%` | `1.31` | 12,610,000.00 USD |
| `15M` | `OKX` | `59.02%` | `40.98%` | `1.44` | 3,360,000.00 USD |
| `15M` | `Bybit` | `55.21%` | `44.79%` | `1.23` | 4,350,000.00 USD |
| `15M` | `KuCoin` | `79.88%` | `20.12%` | `3.97` | 328,590.00 USD |
| `15M` | `Gate` | `58.03%` | `41.97%` | `1.38` | 1,930,000.00 USD |
| `15M` | `Bitget` | `62.16%` | `37.84%` | `1.64` | 1,620,000.00 USD |
| `15M` | `BingX` | `85.57%` | `14.43%` | `5.93` | 882,170.00 USD |
| `15M` | `MEXC` | `64.45%` | `35.55%` | `1.81` | 5,440,000.00 USD |
| `15M` | `Bitunix` | `76.97%` | `23.03%` | `3.34` | 2,760,000.00 USD |
| `15M` | `Hyperliquid` | `45.05%` | `54.95%` | `0.82` | 969,690.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `58.67%` | `41.33%` | `1.42` | 111,040.00 USD |
| `15M` | `Crypto.com` | `52.13%` | `47.87%` | `1.09` | 42,380.00 USD |
| `15M` | `WhiteBIT` | `98.15%` | `1.85%` | `53.05` | 1,370,000.00 USD |
| `15M` | `HTX` | `77.29%` | `22.71%` | `3.40` | 242,410.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `65.43%` | `34.57%` | `1.89` | 225,030.00 USD |
| `15M` | `Aster` | `44.46%` | `55.54%` | `0.80` | 413,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.93%` | `55.07%` | `0.82` | 53,480.00 USD |
| `15M` | `Whale Positions` | `56.77%` | `43.23%` | `1.31` | 12,610,000.00 USD |
| `15M` | `Global Accounts` | `61.91%` | `38.09%` | `1.63` | 36,690,000.00 USD |
| `1H` | `SOL` | `45.41%` | `54.59%` | `0.83` | 153,470,000.00 USD |
| `1H` | `Binance` | `41.1%` | `58.9%` | `0.70` | 54,140,000.00 USD |
| `1H` | `OKX` | `46.27%` | `53.73%` | `0.86` | 15,630,000.00 USD |
| `1H` | `Bybit` | `44.8%` | `55.2%` | `0.81` | 21,450,000.00 USD |
| `1H` | `KuCoin` | `49.07%` | `50.93%` | `0.96` | 1,770,000.00 USD |
| `1H` | `Gate` | `51.07%` | `48.93%` | `1.04` | 6,340,000.00 USD |
| `1H` | `Bitget` | `37.15%` | `62.85%` | `0.59` | 11,010,000.00 USD |
| `1H` | `BingX` | `52.24%` | `47.76%` | `1.09` | 3,020,000.00 USD |
| `1H` | `MEXC` | `51.22%` | `48.78%` | `1.05` | 17,790,000.00 USD |
| `1H` | `Bitunix` | `53.09%` | `46.91%` | `1.13` | 9,090,000.00 USD |
| `1H` | `Hyperliquid` | `30.19%` | `69.81%` | `0.43` | 3,420,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `69.73%` | `30.27%` | `2.30` | 714,850.00 USD |
| `1H` | `Crypto.com` | `51.99%` | `48.01%` | `1.08` | 205,760.00 USD |
| `1H` | `WhiteBIT` | `62.11%` | `37.89%` | `1.64` | 6,280,000.00 USD |
| `1H` | `HTX` | `73.84%` | `26.16%` | `2.82` | 269,130.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `30.69%` | `69.31%` | `0.44` | 894,460.00 USD |
| `1H` | `Aster` | `63.66%` | `36.34%` | `1.75` | 1,250,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `38.59%` | `61.41%` | `0.63` | 194,250.00 USD |
| `1H` | `Whale Positions` | `41.1%` | `58.9%` | `0.70` | 54,140,000.00 USD |
| `1H` | `Global Accounts` | `45.41%` | `54.59%` | `0.83` | 153,470,000.00 USD |
| `4H` | `SOL` | `47.09%` | `52.91%` | `0.89` | 588,440,000.00 USD |
| `4H` | `Binance` | `46.82%` | `53.18%` | `0.88` | 193,230,000.00 USD |
| `4H` | `OKX` | `47.02%` | `52.98%` | `0.89` | 59,400,000.00 USD |
| `4H` | `Bybit` | `49.96%` | `50.04%` | `1.00` | 82,620,000.00 USD |
| `4H` | `KuCoin` | `47.53%` | `52.47%` | `0.91` | 6,110,000.00 USD |
| `4H` | `Gate` | `49.11%` | `50.89%` | `0.97` | 25,470,000.00 USD |
| `4H` | `Bitget` | `49.39%` | `50.61%` | `0.98` | 48,870,000.00 USD |
| `4H` | `BingX` | `48.19%` | `51.81%` | `0.93` | 13,430,000.00 USD |
| `4H` | `MEXC` | `49.13%` | `50.87%` | `0.97` | 77,950,000.00 USD |
| `4H` | `Bitunix` | `50%` | `50%` | `1.00` | 31,820,000.00 USD |
| `4H` | `Hyperliquid` | `44.86%` | `55.14%` | `0.81` | 13,480,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.68%` | `50.32%` | `0.99` | 2,480,000.00 USD |
| `4H` | `Crypto.com` | `47.12%` | `52.88%` | `0.89` | 781,790.00 USD |
| `4H` | `WhiteBIT` | `10.26%` | `89.74%` | `0.11` | 21,830,000.00 USD |
| `4H` | `HTX` | `45.05%` | `54.95%` | `0.82` | 470,140.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.72%` | `55.28%` | `0.81` | 3,410,000.00 USD |
| `4H` | `Aster` | `42.88%` | `57.12%` | `0.75` | 6,430,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.39%` | `58.61%` | `0.71` | 638,480.00 USD |
| `4H` | `Whale Positions` | `46.82%` | `53.18%` | `0.88` | 193,230,000.00 USD |
| `4H` | `Global Accounts` | `47.09%` | `52.91%` | `0.89` | 588,440,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `101.94` | `101.88` | `101.94` | `102.02` | `101.75` | 15,546,239.68 USD | 7,009,090.38 USD | 8,537,149.31 USD | -1,528,058.93 USD | `-9.83%` | `0B / 1S` |
| `0:00 UTC` | `101.70` | `101.72` | `101.70` | `101.94` | `101.53` | 20,486,970.74 USD | 7,002,058.55 USD | 13,484,912.18 USD | -6,482,853.63 USD | `-31.64%` | `0B / 15S` |
| `5:00 UTC` | `101.65` | `101.65` | `101.65` | `101.78` | `101.53` | 12,871,901.66 USD | 6,991,731.87 USD | 5,880,169.78 USD | 1,111,562.09 USD | `+8.64%` | `1B / 2S` |
| `0:00 UTC` | `101.00` | `101.32` | `101.00` | `101.77` | `100.97` | 23,345,961.64 USD | 9,081,895.18 USD | 14,264,066.46 USD | -5,182,171.27 USD | `-22.20%` | `6B / 20S` |
| `5:00 UTC` | `100.91` | `100.89` | `100.91` | `101.13` | `100.72` | 21,682,501.47 USD | 10,212,926.11 USD | 11,469,575.36 USD | -1,256,649.25 USD | `-5.80%` | `6B / 4S` |
| `0:00 UTC` | `101.07` | `101.03` | `101.07` | `101.19` | `100.90` | 11,845,890.84 USD | 5,647,320.15 USD | 6,198,570.68 USD | -551,250.53 USD | `-4.65%` | `2B / 1S` |
| `5:00 UTC` | `100.81` | `100.98` | `100.81` | `101.18` | `100.75` | 7,681,327.85 USD | 3,539,960.94 USD | 4,141,366.91 USD | -601,405.98 USD | `-7.83%` | `5B / 12S` |
| `0:00 UTC` | `100.38` | `100.47` | `100.38` | `100.81` | `100.30` | 26,755,803.01 USD | 9,721,488.50 USD | 17,034,314.50 USD | -7,312,826.00 USD | `-27.33%` | `0B / 21S` |
| `5:00 UTC` | `100.66` | `100.58` | `100.66` | `100.78` | `100.34` | 9,618,082.62 USD | 5,517,082.05 USD | 4,101,000.56 USD | 1,416,081.49 USD | `+14.72%` | `9B / 2S` |
| `0:00 UTC` | `100.57` | `100.52` | `100.57` | `100.62` | `100.41` | 1,112,750.07 USD | 447,525.28 USD | 665,224.79 USD | -217,699.51 USD | `-19.56%` | `1B / 6S` |

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
| `5m` | 621,680.00 USD | 4,560,000.00 USD | **`ACCUMULATION`** |
| `15m` | 422,580.00 USD | 2,630,000.00 USD | **`ACCUMULATION`** |
| `30m` | -783,310.00 USD | -9,730,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -226,530.00 USD | -9,180,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -6,160,000.00 USD | -36,140,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,480,000.00 USD | -44,520,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 12,440,000.00 USD | -19,670,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 12,160,000.00 USD | -59,690,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 24,130,000.00 USD | -52,900,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 24,230,000.00 USD | -107,560,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 83,420,000.00 USD | -302,210,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 62,180,000.00 USD | -1,900,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+621.68K` | 15m=`+422.58K` | 1h=`-226.53K` | 24h=`+24.23M`
* Futures Capital Netflows: 5m=`+4.56M` | 15m=`+2.63M` | 1h=`-9.18M` | 24h=`-107.56M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `99.18` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `98.22` (Risk Distance: `0.9551` pts)
  * +2.5R Take Profit: `101.57`
  * Mathematical Lot Sizing: **`10.47 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.28` (Risk Distance: `0.9551` pts)
  * +2.5R Take Profit: `98.93`
  * Mathematical Lot Sizing: **`10.47 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`101.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
