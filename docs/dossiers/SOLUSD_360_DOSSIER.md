# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `100.91` | **Live Ask Quote**: `101.16` | **Mid Price**: `101.03`
- **Spread Points**: `25.00` | **Spread BPS**: `24.74 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `100.42` | VWAP Z-Score: `+0.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5101` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.68` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.07` | Lower -3.00σ Band: `97.78`
  * Upper +2.51σ Band: `102.64` | Lower -2.51σ Band: `98.21`
  * Upper +2.01σ Band: `102.20` | Lower -2.01σ Band: `98.65`
  * Upper +2.00σ Band: `102.19` | Lower -2.00σ Band: `98.66`
  * Upper +1.28σ Band: `101.55` | Lower -1.28σ Band: `99.30`
  * Upper +1.00σ Band: `101.31` | Lower -1.00σ Band: `99.54`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`101.32` | EMA-20=`101.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.87` (Slope: `+0.0000`) | EMA-100=`100.84`
  * Institutional Anchors: EMA-144=`100.85` | EMA-200=`100.79` (Slope: `+0.1144`) | EMA-233=`100.72`
- **Range Boundaries**: 24H High=`103.63` | 24H Low=`98.95` | Weekly High=`103.63` | Weekly Low=`98.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.35` (Distance: `-0.28%`)
  * Point of Control (POC) = `99.92` (Distance: `+1.15%`)
  * Value Area Low (VAL) = `99.04` (Distance: `+2.04%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `100.63` - `101.44`
  * Optimal Trade Entry (OTE 0.705): `101.24`
  * Structural Invalidation Anchor (0.786): `101.84`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.83` | `101.06` | `100.80` | `101.06` | `36,820` | 3,716,926.13 USD | 1,239,537.15 USD | `+33.35%` | -65,171,409.08 USD | `+1.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.06` | `101.12` | `100.96` | `101.08` | `47,323` | 4,781,341.43 USD | -242,663.57 USD | `-5.08%` | -65,414,072.65 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `101.08` | `101.14` | `101.08` | `101.14` | `4,095` | 414,117.29 USD | 93,772.62 USD | `+22.64%` | -65,320,300.03 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.62` | `101.76` | `100.97` | `101.02` | `230,432` | 23,345,961.64 USD | -5,182,171.27 USD | `-22.20%` | -65,722,352.40 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `101.01` | `101.13` | `100.71` | `101.06` | `214,916` | 21,682,501.47 USD | -1,256,649.25 USD | `-5.80%` | -66,979,001.65 USD | `-0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `101.06` | `101.17` | `100.96` | `101.17` | `52,089` | 5,263,270.54 USD | -90,709.57 USD | `-1.72%` | -67,069,711.22 USD | `+0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `102.66` | `103.16` | `101.75` | `101.86` | `1,100,013` | 112,591,915.90 USD | -12,028,545.03 USD | `-10.68%` | -51,660,705.06 USD | `-1.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `101.87` | `101.93` | `100.71` | `101.06` | `773,410` | 78,387,335.50 USD | -11,810,112.06 USD | `-15.07%` | -63,470,817.13 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.06` | `101.14` | `100.96` | `101.14` | `51,418` | 5,195,458.72 USD | -148,890.95 USD | `-2.87%` | -63,619,708.08 USD | `+0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.71` | `101.16` | `1,925,430` | 196,234,169.34 USD | -23,937,709.13 USD | `-12.20%` | -67,806,352.35 USD | `-0.91` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.37` | `102.50` | `99.16` | `99.64` | `3,450,297` | 345,810,531.49 USD | -35,022,306.76 USD | `-10.13%` | -43,673,756.58 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -38,017,362.01 USD | `+1.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.71` | `101.16` | `1,925,430` | 196,234,169.34 USD | -23,937,709.13 USD | `-12.20%` | -67,806,352.35 USD | `-0.91` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`101.03`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `100.99` | `2010.4300` | 203,033.33 USD | 6,197,649.93 USD | `9 orders` | `-0.19%` | `-` |
| `BID` | `101.00` | `1686.4800` | 170,334.48 USD | 5,994,616.61 USD | `12 orders` | `-0.18%` | `-` |
| `BID` | `101.01` | `3283.0800` | 331,623.91 USD | 5,824,282.13 USD | `7 orders` | `-0.17%` | `-` |
| `BID` | `101.02` | `4133.7100` | 417,587.38 USD | 5,492,658.21 USD | `9 orders` | `-0.16%` | `-` |
| `BID` | `101.03` | `3548.9900` | 358,554.46 USD | 5,075,070.83 USD | `8 orders` | `-0.15%` | `-` |
| `BID` | `101.04` | `1462.7300` | 147,794.24 USD | 4,716,516.37 USD | `9 orders` | `-0.14%` | `-` |
| `BID` | `101.05` | `2829.9500` | 285,966.45 USD | 4,568,722.13 USD | `9 orders` | `-0.13%` | `-` |
| `BID` | `101.06` | `4059.2600` | 410,228.82 USD | 4,282,755.68 USD | `21 orders` | `-0.12%` | `-` |
| `BID` | `101.07` | `6833.4500` | 690,656.79 USD | 3,872,526.87 USD | `17 orders` | `-0.11%` | `-` |
| `BID` | `101.08` | `1698.3000` | 171,664.16 USD | 3,181,870.08 USD | `16 orders` | `-0.10%` | `-` |
| `BID` | `101.09` | `2367.7200` | 239,352.81 USD | 3,010,205.91 USD | `12 orders` | `-0.09%` | `-` |
| `BID` | `101.10` | `3123.5600` | 315,791.92 USD | 2,770,853.10 USD | `16 orders` | `-0.08%` | `-` |
| `BID` | `101.11` | `2301.2100` | 232,675.34 USD | 2,455,061.18 USD | `14 orders` | `-0.07%` | `-` |
| `BID` | `101.12` | `5207.7300` | 526,605.66 USD | 2,222,385.84 USD | `22 orders` | `-0.06%` | `-` |
| `BID` | `101.13` | `4097.7600` | 414,406.47 USD | 1,695,780.18 USD | `27 orders` | `-0.05%` | `-` |
| `BID` | `101.14` | `1921.3000` | 194,320.28 USD | 1,281,373.71 USD | `21 orders` | `-0.04%` | `-` |
| `BID` | `101.15` | `3282.0000` | 331,974.30 USD | 1,087,053.43 USD | `24 orders` | `-0.03%` | `-` |
| `BID` | `101.16` | `1570.5900` | 158,880.88 USD | 755,079.13 USD | `20 orders` | `-0.02%` | `-` |
| `BID` | `101.17` | `2109.2700` | 213,394.85 USD | 596,198.25 USD | `24 orders` | `-0.01%` | `-` |
| `BID` | `101.18` | `3783.3900` | 382,803.40 USD | 382,803.40 USD | `32 orders` | `-0.00%` | `-` |
| `ASK` | `101.19` | `0.6400` | 64.76 USD | 64.76 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `101.19` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 101.19` | `0.00%` | `-` |
| `ASK` | `101.20` | `11.9400` | 1,208.33 USD | 1,273.09 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `101.21` | `439.9000` | 44,522.28 USD | 45,795.37 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `101.22` | `1193.1300` | 120,768.62 USD | 166,563.99 USD | `22 orders` | `+0.03%` | `-` |
| `ASK` | `101.23` | `3031.3100` | 306,859.51 USD | 473,423.50 USD | `21 orders` | `+0.04%` | `-` |
| `ASK` | `101.24` | `1916.7600` | 194,052.78 USD | 667,476.28 USD | `25 orders` | `+0.05%` | `-` |
| `ASK` | `101.25` | `3598.9000` | 364,388.62 USD | 1,031,864.91 USD | `31 orders` | `+0.06%` | `-` |
| `ASK` | `101.26` | `2139.0400` | 216,599.19 USD | 1,248,464.10 USD | `20 orders` | `+0.07%` | `-` |
| `ASK` | `101.27` | `5784.3300` | 585,779.10 USD | 1,834,243.20 USD | `19 orders` | `+0.08%` | `-` |
| `ASK` | `101.28` | `2035.2000` | 206,125.06 USD | 2,040,368.25 USD | `18 orders` | `+0.09%` | `-` |
| `ASK` | `101.29` | `3625.6300` | 367,240.06 USD | 2,407,608.31 USD | `18 orders` | `+0.10%` | `-` |
| `ASK` | `101.30` | `655.3100` | 66,382.90 USD | 2,473,991.22 USD | `10 orders` | `+0.11%` | `-` |
| `ASK` | `101.31` | `4254.0700` | 430,979.83 USD | 2,904,971.05 USD | `14 orders` | `+0.12%` | `-` |
| `ASK` | `101.32` | `4359.2100` | 441,675.16 USD | 3,346,646.21 USD | `15 orders` | `+0.13%` | `-` |
| `ASK` | `101.33` | `3005.7700` | 304,574.67 USD | 3,651,220.88 USD | `14 orders` | `+0.14%` | `-` |
| `ASK` | `101.34` | `441.8800` | 44,780.12 USD | 3,696,001.00 USD | `10 orders` | `+0.15%` | `-` |
| `ASK` | `101.35` | `3941.5800` | 399,479.13 USD | 4,095,480.13 USD | `11 orders` | `+0.16%` | `-` |
| `ASK` | `101.36` | `735.7200` | 74,572.58 USD | 4,170,052.71 USD | `7 orders` | `+0.17%` | `-` |
| `ASK` | `101.37` | `4082.8300` | 413,876.48 USD | 4,583,929.19 USD | `10 orders` | `+0.18%` | `-` |
| `ASK` | `101.38` | `7543.8200` | 764,792.47 USD | 5,348,721.66 USD | `13 orders` | `+0.19%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 72,924,231.09 USD | `721,165.26` | `94.33` | `101.14` | `315.70` | -4,893,340.68 USD | `-6.71%` | `7X Cross` |
| `21` | `0x9c6a...a4ed` | `LONG` | 55,624,867.21 USD | `550,087.69` | `80.86` | `101.14` | `68.17` | 11,145,880.82 USD | `+20.04%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 26,226,070.76 USD | `259,300.02` | `91.42` | `101.14` | `605.71` | -2,520,937.74 USD | `-9.61%` | `5X Cross` |
| `78` | `0x3dc9...54b0` | `SHORT` | 22,251,215.22 USD | `220,000.19` | `105.90` | `101.14` | `165.16` | 1,047,892.06 USD | `+4.71%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 19,159,459.20 USD | `189,472.50` | `115.21` | `101.14` | `34.67` | -2,669,556.06 USD | `-13.93%` | `20X Cross` |
| `111` | `0x4a20...3c26` | `LONG` | 18,207,000.00 USD | `180,000.00` | `106.43` | `101.14` | `65.51` | -951,278.71 USD | `-5.22%` | `20X Cross` |
| `135` | `0xecb6...2b00` | `SHORT` | 15,073,092.95 USD | `149,073.53` | `102.73` | `101.14` | `292.82` | 241,950.57 USD | `+1.61%` | `20X Cross` |
| `227` | `0xc63a...a3cd` | `LONG` | 10,115,000.00 USD | `100,000.00` | `112.22` | `101.14` | `0.000000` | -1,107,108.97 USD | `-10.95%` | `20X Cross` |
| `231` | `0x7a5a...0394` | `SHORT` | 10,033,087.72 USD | `99,190.19` | `100.92` | `101.14` | `127.43` | -22,878.33 USD | `-0.23%` | `10X Cross` |
| `242` | `0x13da...08be` | `LONG` | 9,681,196.98 USD | `95,711.29` | `100.55` | `101.14` | `98.09` | 57,456.31 USD | `+0.59%` | `20X Isolated` |
| `264` | `0xb581...6f4f` | `LONG` | 9,100,800.00 USD | `90,000.00` | `114.59` | `101.14` | `0.000000` | -1,212,492.29 USD | `-13.32%` | `3X Cross` |
| `288` | `0x645b...87b8` | `SHORT` | 8,454,166.92 USD | `83,605.29` | `103.91` | `101.14` | `332.15` | 232,962.24 USD | `+2.76%` | `20X Cross` |
| `293` | `0xdb3a...cf3b` | `LONG` | 8,279,307.55 USD | `81,851.78` | `106.04` | `101.14` | `46.49` | -400,439.31 USD | `-4.84%` | `4X Cross` |
| `314` | `0xe927...98ef` | `LONG` | 7,887,360.00 USD | `78,000.00` | `96.34` | `101.14` | `38.44` | 373,218.52 USD | `+4.73%` | `3X Cross` |
| `324` | `0xca49...53c8` | `SHORT` | 7,479,379.97 USD | `73,943.45` | `110.70` | `101.14` | `272.97` | 706,242.29 USD | `+9.44%` | `20X Cross` |
| `327` | `0x8ae4...3d60` | `LONG` | 7,298,846.66 USD | `72,180.05` | `111.72` | `101.14` | `1.55` | -765,313.58 USD | `-10.49%` | `10X Cross` |
| `331` | `0xa0b7...6165` | `SHORT` | 7,184,011.75 USD | `71,044.42` | `107.87` | `101.14` | `190.90` | 479,455.45 USD | `+6.67%` | `2X Cross` |
| `348` | `0xf517...c032` | `SHORT` | 6,855,798.31 USD | `67,778.53` | `84.64` | `101.14` | `231.16` | -1,118,767.15 USD | `-16.32%` | `20X Cross` |
| `475` | `0x7e23...5a5a` | `LONG` | 4,911,907.01 USD | `48,564.56` | `105.17` | `101.14` | `78.11` | -195,662.15 USD | `-3.98%` | `5X Isolated` |
| `568` | `0x2e2b...2fab` | `LONG` | 4,045,672.00 USD | `40,000.00` | `119.55` | `101.14` | `53.52` | -736,363.64 USD | `-18.20%` | `10X Cross` |
| `576` | `0x7fda...17d1` | `SHORT` | 4,009,281.05 USD | `39,651.96` | `103.77` | `101.14` | `1071.15` | 105,320.47 USD | `+2.63%` | `20X Cross` |
| `593` | `0xf899...88db` | `SHORT` | 3,901,843.62 USD | `38,586.27` | `87.86` | `101.14` | `117.02` | -511,468.43 USD | `-13.11%` | `20X Cross` |
| `612` | `0x9946...0852` | `SHORT` | 3,821,932.52 USD | `37,784.80` | `112.11` | `101.14` | `128.39` | 414,294.80 USD | `+10.84%` | `20X Cross` |
| `637` | `0x27b8...12fc` | `LONG` | 3,649,349.87 USD | `36,085.73` | `110.86` | `101.14` | `14.07` | -350,995.38 USD | `-9.62%` | `10X Cross` |
| `642` | `0x9c16...4a6f` | `SHORT` | 3,619,061.02 USD | `35,779.15` | `90.45` | `101.14` | `128.56` | -382,955.99 USD | `-10.58%` | `20X Cross` |
| `647` | `0x3440...32c5` | `SHORT` | 3,593,770.49 USD | `35,529.12` | `95.02` | `101.14` | `167.49` | -217,749.06 USD | `-6.06%` | `20X Cross` |
| `715` | `0x96a7...79df` | `LONG` | 3,235,840.00 USD | `32,000.00` | `74.39` | `101.14` | `0.000000` | 855,434.15 USD | `+26.44%` | `20X Cross` |
| `733` | `0x023a...2355` | `SHORT` | 3,188,205.52 USD | `31,519.58` | `101.48` | `101.14` | `363.35` | 10,358.60 USD | `+0.32%` | `20X Cross` |
| `759` | `0xbe19...8bd1` | `SHORT` | 3,080,188.44 USD | `30,451.69` | `97.62` | `101.14` | `732.08` | -107,641.81 USD | `-3.49%` | `3X Cross` |
| `767` | `0x482b...cae4` | `SHORT` | 3,065,906.06 USD | `30,310.49` | `88.03` | `101.14` | `157.11` | -397,657.78 USD | `-12.97%` | `20X Cross` |
| `781` | `0x610b...b613` | `LONG` | 2,996,604.24 USD | `29,634.14` | `101.23` | `101.14` | `70.38` | -3,395.11 USD | `-0.11%` | `3X Isolated` |
| `790` | `0x45d2...4029` | `SHORT` | 2,955,603.00 USD | `29,220.00` | `93.28` | `101.14` | `1347.60` | -229,827.02 USD | `-7.78%` | `20X Cross` |
| `802` | `0xa61c...66b9` | `LONG` | 2,922,021.20 USD | `28,888.00` | `104.39` | `101.14` | `0.000000` | -93,542.92 USD | `-3.20%` | `5X Cross` |
| `841` | `0xfc66...ca06` | `SHORT` | 2,771,286.46 USD | `27,397.79` | `102.30` | `101.14` | `1376.13` | 31,496.77 USD | `+1.14%` | `20X Cross` |
| `842` | `0x458d...ab3b` | `LONG` | 2,769,174.23 USD | `27,385.03` | `117.17` | `101.14` | `81.07` | -439,488.28 USD | `-15.87%` | `3X Isolated` |
| `876` | `0xfc27...9d9d` | `SHORT` | 2,609,018.59 USD | `25,793.56` | `102.76` | `101.14` | `654.88` | 41,469.20 USD | `+1.59%` | `20X Cross` |
| `904` | `0x051c...693c` | `LONG` | 2,542,126.46 USD | `25,139.70` | `89.76` | `101.14` | `22.45` | 285,565.14 USD | `+11.23%` | `20X Cross` |
| `935` | `0x638f...f5f0` | `LONG` | 2,427,600.00 USD | `24,000.00` | `136.71` | `101.14` | `42.26` | -853,368.54 USD | `-35.15%` | `20X Cross` |
| `1001` | `0x7178...0854` | `LONG` | 2,280,451.03 USD | `22,545.24` | `110.94` | `101.14` | `30.56` | -220,693.45 USD | `-9.68%` | `10X Cross` |
| `1021` | `0x739c...cfb2` | `LONG` | 2,225,119.60 USD | `22,000.00` | `91.95` | `101.14` | `72.97` | 202,212.29 USD | `+9.09%` | `20X Cross` |
| `1031` | `0x69cc...14fd` | `SHORT` | 2,195,113.81 USD | `21,701.57` | `99.01` | `101.14` | `457.98` | -46,461.06 USD | `-2.12%` | `20X Cross` |
| `1052` | `0xb90d...870c` | `SHORT` | 2,136,124.93 USD | `21,120.10` | `102.00` | `101.14` | `111.91` | 18,199.84 USD | `+0.85%` | `20X Cross` |
| `1093` | `0x7737...bf66` | `SHORT` | 2,061,847.67 USD | `20,384.06` | `102.94` | `101.14` | `1000.26` | 36,494.22 USD | `+1.77%` | `10X Cross` |
| `1104` | `0xea00...a918` | `LONG` | 2,025,130.91 USD | `20,022.69` | `66.09` | `101.14` | `0.000000` | 701,822.31 USD | `+34.66%` | `20X Cross` |
| `1106` | `0x251f...6e5d` | `LONG` | 2,023,000.00 USD | `20,000.00` | `101.15` | `101.14` | `45.35` | -97.77 USD | `-0.00%` | `20X Cross` |
| `1108` | `0x3fc5...c0c1` | `SHORT` | 2,022,836.00 USD | `20,000.00` | `98.28` | `101.14` | `202.32` | -57,276.16 USD | `-2.83%` | `20X Cross` |
| `1109` | `0xdf60...d3c7` | `LONG` | 2,022,836.00 USD | `20,000.00` | `120.12` | `101.14` | `94.00` | -379,572.53 USD | `-18.76%` | `7X Isolated` |
| `1110` | `0x5986...89d9` | `LONG` | 2,022,600.00 USD | `20,000.00` | `101.84` | `101.14` | `45.37` | -14,197.53 USD | `-0.70%` | `20X Cross` |
| `1111` | `0xbfc7...80b4` | `SHORT` | 2,022,400.00 USD | `20,000.00` | `85.98` | `101.14` | `319.64` | -302,865.50 USD | `-14.98%` | `20X Cross` |
| `1131` | `0xb322...d51f` | `LONG` | 2,000,223.04 USD | `19,774.82` | `102.98` | `101.14` | `56.10` | -36,248.36 USD | `-1.81%` | `20X Cross` |
| `1140` | `0x34e6...8d74` | `LONG` | 1,991,448.28 USD | `19,688.07` | `101.19` | `101.14` | `53.20` | -715.52 USD | `-0.04%` | `20X Cross` |
| `1163` | `0x936c...bb0f` | `SHORT` | 1,966,135.49 USD | `19,437.82` | `105.65` | `101.14` | `635.52` | 87,378.89 USD | `+4.44%` | `20X Cross` |
| `1164` | `0x7160...d47c` | `LONG` | 1,965,759.22 USD | `19,434.10` | `105.03` | `101.14` | `80.17` | -75,462.08 USD | `-3.84%` | `20X Cross` |
| `1189` | `0xe097...d0fe` | `LONG` | 1,921,420.11 USD | `18,995.75` | `109.71` | `101.14` | `0.000000` | -162,576.78 USD | `-8.46%` | `20X Cross` |
| `1280` | `0xe98b...8cd5` | `SHORT` | 1,782,026.64 USD | `17,622.89` | `187.95` | `101.14` | `260.15` | 1,530,194.09 USD | `+85.87%` | `20X Cross` |
| `1289` | `0xdf95...7d72` | `SHORT` | 1,764,399.91 USD | `17,443.40` | `104.70` | `101.14` | `2198.74` | 61,863.75 USD | `+3.51%` | `20X Cross` |
| `1319` | `0xee2b...d67e` | `LONG` | 1,715,826.67 USD | `16,963.19` | `119.86` | `101.14` | `19.92` | -317,444.97 USD | `-18.50%` | `4X Cross` |
| `1323` | `0x123d...3bff` | `LONG` | 1,711,160.46 USD | `16,918.43` | `89.53` | `101.14` | `0.000000` | 196,373.98 USD | `+11.48%` | `10X Cross` |
| `1352` | `0x7277...0b98` | `SHORT` | 1,679,404.58 USD | `16,603.11` | `101.18` | `101.14` | `178.64` | 523.63 USD | `+0.03%` | `20X Cross` |
| `1436` | `0x73d7...8be1` | `LONG` | 1,584,914.29 USD | `15,668.95` | `106.60` | `101.14` | `70.09` | -85,426.67 USD | `-5.39%` | `20X Cross` |
| `1449` | `0xc74a...ab93` | `LONG` | 1,571,083.24 USD | `15,536.82` | `64.06` | `101.14` | `54.88` | 575,854.40 USD | `+36.65%` | `5X Isolated` |
| `1493` | `0xc7d1...51af` | `SHORT` | 1,516,800.00 USD | `15,000.00` | `105.79` | `101.14` | `138.76` | 70,075.00 USD | `+4.62%` | `20X Cross` |
| `1524` | `0xffb2...5ed6` | `LONG` | 1,466,649.54 USD | `14,504.05` | `117.89` | `101.14` | `89.77` | -243,255.18 USD | `-16.59%` | `20X Cross` |
| `1554` | `0x0d6a...ca57` | `LONG` | 1,436,886.15 USD | `14,206.65` | `110.41` | `101.14` | `91.59` | -131,704.20 USD | `-9.17%` | `5X Isolated` |
| `1831` | `0x2482...0e55` | `LONG` | 1,149,373.39 USD | `11,363.98` | `122.03` | `101.14` | `94.24` | -237,328.53 USD | `-20.65%` | `20X Isolated` |
| `1848` | `0xe105...6a47` | `LONG` | 1,133,390.81 USD | `11,205.05` | `107.11` | `101.14` | `92.18` | -66,766.25 USD | `-5.89%` | `20X Cross` |
| `1862` | `0x45db...86eb` | `LONG` | 1,122,543.00 USD | `11,100.00` | `110.69` | `101.14` | `67.96` | -106,138.90 USD | `-9.46%` | `5X Cross` |
| `1889` | `0x1d04...7c43` | `LONG` | 1,093,285.17 USD | `10,811.76` | `111.55` | `101.14` | `18.72` | -112,776.32 USD | `-10.32%` | `6X Cross` |
| `2005` | `0x0daf...47e0` | `SHORT` | 1,011,200.00 USD | `10,000.00` | `99.07` | `101.14` | `249.11` | -20,487.78 USD | `-2.03%` | `5X Cross` |

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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.65` (Vol: 2,900,000.00 USD, Dist: `+2.61%`) | Long MP=`98.78` (Vol: 4,200,000.00 USD, Dist: `--2.21%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+3.04%`) | Long MP=`98.78` (Vol: 4,300,000.00 USD, Dist: `--2.21%`)
  * 3D Horizon: Short MP=`104.03` (Vol: 4,200,000.00 USD, Dist: `+2.99%`) | Long MP=`99.07` (Vol: 5,900,000.00 USD, Dist: `--1.92%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+3.00%`) | Long MP=`98.63` (Vol: 8,800,000.00 USD, Dist: `--2.36%`)
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
| `7D` | `Long Liquidation` | `89.60` | 371,410,000.00 USD | 371,410,000.00 USD | 700,630.00 USD | 276,340.00 USD | 577,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 369,860,000.00 USD | 369,860,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 368,870,000.00 USD | 368,870,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 367,150,000.00 USD | 367,150,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 365,150,000.00 USD | 365,150,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.50` | 1,800,000.00 USD | 29,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 190,070,000.00 USD | 190,070,000.00 USD | 441,060.00 USD | 495,490.00 USD | 561,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.60` | 363,750,000.00 USD | 363,750,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.80` | 188,580,000.00 USD | 188,580,000.00 USD | 91,100.00 USD | 101,660.00 USD | 319.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 360,630,000.00 USD | 360,630,000.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.00` | 188,380,000.00 USD | 188,380,000.00 USD | 53,030.00 USD | 882.42 USD | 75,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 357,660,000.00 USD | 357,660,000.00 USD | 1,180,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.20` | 188,250,000.00 USD | 188,250,000.00 USD | 27,610.00 USD | 2,670.00 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 355,610,000.00 USD | 355,610,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.40` | 188,220,000.00 USD | 188,220,000.00 USD | 133,210.00 USD | 195,720.00 USD | 248,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 353,280,000.00 USD | 353,280,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.50` | 4,240,000.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 187,650,000.00 USD | 187,650,000.00 USD | 31,510.00 USD | 192,290.00 USD | 73,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 349,960,000.00 USD | 349,960,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.80` | 187,350,000.00 USD | 187,350,000.00 USD | 369,020.00 USD | 218,430.00 USD | 123,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 348,340,000.00 USD | 348,340,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.00` | 186,640,000.00 USD | 186,640,000.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 346,130,000.00 USD | 346,130,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.20` | 186,170,000.00 USD | 186,170,000.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 344,400,000.00 USD | 344,400,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.40` | 185,720,000.00 USD | 185,720,000.00 USD | 151,210.00 USD | 110,310.00 USD | 782,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 343,540,000.00 USD | 343,540,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.50` | 1,190,000.00 USD | 23,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 184,680,000.00 USD | 184,680,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 341,620,000.00 USD | 341,620,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.80` | 184,430,000.00 USD | 184,430,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 340,540,000.00 USD | 340,540,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.00` | 184,270,000.00 USD | 184,270,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 340,320,000.00 USD | 340,320,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.20` | 184,110,000.00 USD | 184,110,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 339,930,000.00 USD | 339,930,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.40` | 183,900,000.00 USD | 183,900,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 339,820,000.00 USD | 339,820,000.00 USD | 80,500.00 USD | 115,240.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.50` | 3,140,000.00 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 339,620,000.00 USD | 339,620,000.00 USD | 238,200.00 USD | 343,740.00 USD | 114,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 338,920,000.00 USD | 338,920,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 338,250,000.00 USD | 338,250,000.00 USD | 78,790.00 USD | 153,680.00 USD | 134,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 337,880,000.00 USD | 337,880,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 337,220,000.00 USD | 337,220,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,910,000.00 USD | 19,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 336,930,000.00 USD | 336,930,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 336,850,000.00 USD | 336,850,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 336,820,000.00 USD | 336,820,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.20` | 183,850,000.00 USD | 183,850,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 335,860,000.00 USD | 335,860,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.40` | 183,830,000.00 USD | 183,830,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 335,470,000.00 USD | 335,470,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.50` | 1,800,000.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 183,310,000.00 USD | 183,310,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 333,950,000.00 USD | 333,950,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.80` | 180,750,000.00 USD | 180,750,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 329,910,000.00 USD | 329,910,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.00` | 176,920,000.00 USD | 176,920,000.00 USD | 1,200,000.00 USD | 1,170,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 325,670,000.00 USD | 325,670,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.20` | 173,330,000.00 USD | 173,330,000.00 USD | 1,060,000.00 USD | 1,190,000.00 USD | 693,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 319,230,000.00 USD | 319,230,000.00 USD | 2,940,000.00 USD | 1,970,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.40` | 170,380,000.00 USD | 170,380,000.00 USD | 862,370.00 USD | 983,090.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 312,340,000.00 USD | 312,340,000.00 USD | 2,950,000.00 USD | 643,110.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.50` | 1,410,000.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.60` | 167,430,000.00 USD | 167,430,000.00 USD | 994,840.00 USD | 756,910.00 USD | 933,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 306,370,000.00 USD | 306,370,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.80` | 164,750,000.00 USD | 164,750,000.00 USD | 307,030.00 USD | 737,250.00 USD | 729,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 298,270,000.00 USD | 298,270,000.00 USD | 3,000,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.00` | 162,970,000.00 USD | 162,970,000.00 USD | 277,090.00 USD | 40,420.00 USD | 52,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.00` | 289,530,000.00 USD | 289,530,000.00 USD | 5,460,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.20` | 162,600,000.00 USD | 162,600,000.00 USD | 298,320.00 USD | 11,630.00 USD | 277,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.20` | 279,500,000.00 USD | 279,500,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.40` | 162,020,000.00 USD | 162,020,000.00 USD | 1,110,000.00 USD | 916,790.00 USD | 567,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.40` | 265,940,000.00 USD | 265,940,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.50` | 1,830,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.60` | 159,430,000.00 USD | 159,430,000.00 USD | 2,200,000.00 USD | 1,940,000.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.60` | 255,530,000.00 USD | 255,530,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.80` | 153,110,000.00 USD | 153,110,000.00 USD | 3,880,000.00 USD | 3,190,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.80` | 240,180,000.00 USD | 240,180,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.00` | 143,870,000.00 USD | 143,870,000.00 USD | 3,680,000.00 USD | 3,010,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.00` | 226,720,000.00 USD | 226,720,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.20` | 133,980,000.00 USD | 133,980,000.00 USD | 3,040,000.00 USD | 2,880,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.20` | 202,050,000.00 USD | 202,050,000.00 USD | 7,790,000.00 USD | 6,660,000.00 USD | 5,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.40` | 126,030,000.00 USD | 126,030,000.00 USD | 3,740,000.00 USD | 3,150,000.00 USD | 3,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.40` | 181,920,000.00 USD | 181,920,000.00 USD | 9,460,000.00 USD | 2,950,000.00 USD | 9,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.50` | 11,050,000.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.60` | 115,690,000.00 USD | 115,690,000.00 USD | 6,200,000.00 USD | 4,440,000.00 USD | 6,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.60` | 159,880,000.00 USD | 159,880,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.80` | 98,290,000.00 USD | 98,290,000.00 USD | 7,300,000.00 USD | 6,980,000.00 USD | 5,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.80` | 124,390,000.00 USD | 124,390,000.00 USD | 12,600,000.00 USD | 9,880,000.00 USD | 13,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.00` | 78,960,000.00 USD | 78,960,000.00 USD | 4,990,000.00 USD | 4,620,000.00 USD | 5,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.00` | 88,840,000.00 USD | 88,840,000.00 USD | 14,180,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.20` | 64,120,000.00 USD | 64,120,000.00 USD | 4,490,000.00 USD | 4,640,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.20` | 47,260,000.00 USD | 47,260,000.00 USD | 12,590,000.00 USD | 6,970,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.40` | 51,500,000.00 USD | 51,500,000.00 USD | 3,410,000.00 USD | 4,060,000.00 USD | 4,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.40` | 22,310,000.00 USD | 22,310,000.00 USD | 2,300,000.00 USD | 599,290.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.50` | 448,020.00 USD | 554,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `99.60` | 39,160,000.00 USD | 39,160,000.00 USD | 3,330,000.00 USD | 2,990,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.60` | 12,720,000.00 USD | 12,720,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.80` | 29,870,000.00 USD | 29,870,000.00 USD | 1,490,000.00 USD | 2,600,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.80` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.00` | 22,630,000.00 USD | 22,630,000.00 USD | 2,110,000.00 USD | 937,930.00 USD | 662,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.00` | 5,490,000.00 USD | 5,490,000.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.20` | 18,920,000.00 USD | 18,920,000.00 USD | 234,170.00 USD | 341,570.00 USD | 431,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.40` | 17,910,000.00 USD | 17,910,000.00 USD | 718,910.00 USD | 877,160.00 USD | 438,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.40` | 4,070,000.00 USD | 4,070,000.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `100.50` | 106,160.00 USD | 106,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `100.60` | 15,870,000.00 USD | 15,870,000.00 USD | 1,200,000.00 USD | 251,930.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.60` | 2,750,000.00 USD | 2,750,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `100.80` | 11,630,000.00 USD | 11,630,000.00 USD | 274,280.00 USD | 802,330.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `100.80` | 981,100.00 USD | 981,100.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `101.00` | 10,550,000.00 USD | 10,550,000.00 USD | 6,610,000.00 USD | 953,600.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 19,160,000.00 USD | 19,160,000.00 USD | 0.00 USD | 4,560,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.20` | 14,800,000.00 USD | 14,800,000.00 USD | 2,650,000.00 USD | 7,010,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 30,510,000.00 USD | 30,510,000.00 USD | 2,190,000.00 USD | 3,220,000.00 USD | 5,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.40` | 16,100,000.00 USD | 16,100,000.00 USD | 692,280.00 USD | 609,630.00 USD | 1,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 41,010,000.00 USD | 41,010,000.00 USD | 3,020,000.00 USD | 0.00 USD | 7,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.60` | 35,850,000.00 USD | 35,850,000.00 USD | 4,420,000.00 USD | 2,220,000.00 USD | 13,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 50,860,000.00 USD | 50,860,000.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.80` | 42,420,000.00 USD | 42,420,000.00 USD | 212,730.00 USD | 142,780.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 60,210,000.00 USD | 60,210,000.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 44,250,000.00 USD | 44,250,000.00 USD | 1,110,000.00 USD | 147,120.00 USD | 574,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 62,880,000.00 USD | 62,880,000.00 USD | 843,730.00 USD | 0.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 47,180,000.00 USD | 47,180,000.00 USD | 998,960.00 USD | 1,160,000.00 USD | 764,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 65,120,000.00 USD | 65,120,000.00 USD | 369,280.00 USD | 578,040.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.40` | 48,760,000.00 USD | 48,760,000.00 USD | 0.00 USD | 0.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 68,140,000.00 USD | 68,140,000.00 USD | 1,150,000.00 USD | 299,640.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.60` | 48,990,000.00 USD | 48,990,000.00 USD | 194,440.00 USD | 26,340.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 70,560,000.00 USD | 70,560,000.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.80` | 52,790,000.00 USD | 52,790,000.00 USD | 1,370,000.00 USD | 1,870,000.00 USD | 563,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 78,440,000.00 USD | 78,440,000.00 USD | 7,600,000.00 USD | 0.00 USD | 277,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.00` | 56,710,000.00 USD | 56,710,000.00 USD | 2,540,000.00 USD | 1,280,000.00 USD | 104,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 92,860,000.00 USD | 92,860,000.00 USD | 11,590,000.00 USD | 0.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.20` | 62,390,000.00 USD | 62,390,000.00 USD | 1,740,000.00 USD | 2,390,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 106,630,000.00 USD | 106,630,000.00 USD | 13,650,000.00 USD | 4,380.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.40` | 69,670,000.00 USD | 69,670,000.00 USD | 3,970,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 121,630,000.00 USD | 121,630,000.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.50` | 70,910.00 USD | 70,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 84,180,000.00 USD | 84,180,000.00 USD | 4,360,000.00 USD | 2,110,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 140,020,000.00 USD | 140,020,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.80` | 93,700,000.00 USD | 93,700,000.00 USD | 3,390,000.00 USD | 2,690,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 152,370,000.00 USD | 152,370,000.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.00` | 106,070,000.00 USD | 106,070,000.00 USD | 4,020,000.00 USD | 3,820,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 180,780,000.00 USD | 180,780,000.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.20` | 115,100,000.00 USD | 115,100,000.00 USD | 3,440,000.00 USD | 2,450,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 200,870,000.00 USD | 200,870,000.00 USD | 7,510,000.00 USD | 6,900,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.40` | 123,260,000.00 USD | 123,260,000.00 USD | 3,160,000.00 USD | 1,660,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 217,010,000.00 USD | 217,010,000.00 USD | 4,800,000.00 USD | 3,700,000.00 USD | 7,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.50` | 1,440,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 131,580,000.00 USD | 131,580,000.00 USD | 2,260,000.00 USD | 2,030,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 234,570,000.00 USD | 234,570,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.80` | 137,870,000.00 USD | 137,870,000.00 USD | 1,610,000.00 USD | 1,620,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 251,700,000.00 USD | 251,700,000.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.00` | 140,200,000.00 USD | 140,200,000.00 USD | 675,360.00 USD | 680,650.00 USD | 980,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 268,780,000.00 USD | 268,780,000.00 USD | 5,680,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.20` | 141,350,000.00 USD | 141,350,000.00 USD | 462,990.00 USD | 4,110.00 USD | 679,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 281,230,000.00 USD | 281,230,000.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.40` | 142,470,000.00 USD | 142,470,000.00 USD | 312,780.00 USD | 7,520.00 USD | 803,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 293,880,000.00 USD | 293,880,000.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.50` | 193,620.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 145,010,000.00 USD | 145,010,000.00 USD | 558,220.00 USD | 913,400.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 311,350,000.00 USD | 311,350,000.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 146,820,000.00 USD | 146,820,000.00 USD | 480,230.00 USD | 783,480.00 USD | 552,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 322,570,000.00 USD | 322,570,000.00 USD | 3,560,000.00 USD | 3,300,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.00` | 148,410,000.00 USD | 148,410,000.00 USD | 460,610.00 USD | 552,510.00 USD | 576,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 334,170,000.00 USD | 334,170,000.00 USD | 4,740,000.00 USD | 3,150,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.20` | 151,110,000.00 USD | 151,110,000.00 USD | 1,280,000.00 USD | 675,100.00 USD | 740,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 348,670,000.00 USD | 348,670,000.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.40` | 153,170,000.00 USD | 153,170,000.00 USD | 918,780.00 USD | 500,580.00 USD | 640,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 357,180,000.00 USD | 357,180,000.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.50` | 27,960.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 155,920,000.00 USD | 155,920,000.00 USD | 957,870.00 USD | 536,470.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 366,390,000.00 USD | 366,390,000.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 157,920,000.00 USD | 157,920,000.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 372,270,000.00 USD | 372,270,000.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.00` | 158,900,000.00 USD | 158,900,000.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 377,830,000.00 USD | 377,830,000.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.20` | 159,290,000.00 USD | 159,290,000.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 379,550,000.00 USD | 379,550,000.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.40` | 159,760,000.00 USD | 159,760,000.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 380,530,000.00 USD | 380,530,000.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.50` | 367,260.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 160,250,000.00 USD | 160,250,000.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.60` | 380,900,000.00 USD | 380,900,000.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.80` | 160,560,000.00 USD | 160,560,000.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 381,910,000.00 USD | 381,910,000.00 USD | 499,750.00 USD | 149,980.00 USD | 357,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.00` | 382,540,000.00 USD | 382,540,000.00 USD | 293,270.00 USD | 252,740.00 USD | 82,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.20` | 384,950,000.00 USD | 384,950,000.00 USD | 966,370.00 USD | 938,650.00 USD | 503,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.40` | 387,440,000.00 USD | 387,440,000.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.50` | 105,510.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 388,860,000.00 USD | 388,860,000.00 USD | 401,600.00 USD | 515,740.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.80` | 391,540,000.00 USD | 391,540,000.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.00` | 160,570,000.00 USD | 160,570,000.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.00` | 392,080,000.00 USD | 392,080,000.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.20` | 160,580,000.00 USD | 160,580,000.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.20` | 393,300,000.00 USD | 393,300,000.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.40` | 160,710,000.00 USD | 160,710,000.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.40` | 393,630,000.00 USD | 393,630,000.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.50` | 1,850,000.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.60` | 161,370,000.00 USD | 161,370,000.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.60` | 394,700,000.00 USD | 394,700,000.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.80` | 162,390,000.00 USD | 162,390,000.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.80` | 395,680,000.00 USD | 395,680,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.00` | 163,460,000.00 USD | 163,460,000.00 USD | 213,690.00 USD | 401,420.00 USD | 453,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.00` | 397,400,000.00 USD | 397,400,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.20` | 164,330,000.00 USD | 164,330,000.00 USD | 228,950.00 USD | 389,380.00 USD | 250,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.20` | 399,400,000.00 USD | 399,400,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.40` | 165,220,000.00 USD | 165,220,000.00 USD | 277,830.00 USD | 269,600.00 USD | 337,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.40` | 400,800,000.00 USD | 400,800,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.50` | 195,170.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.60` | 165,640,000.00 USD | 165,640,000.00 USD | 110,850.00 USD | 71,980.00 USD | 239,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.60` | 401,910,000.00 USD | 401,910,000.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.80` | 166,320,000.00 USD | 166,320,000.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.80` | 403,920,000.00 USD | 403,920,000.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.00` | 166,520,000.00 USD | 166,520,000.00 USD | 91,100.00 USD | 101,660.00 USD | 319.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.00` | 406,890,000.00 USD | 406,890,000.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.20` | 166,650,000.00 USD | 166,650,000.00 USD | 53,030.00 USD | 882.42 USD | 75,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.20` | 408,940,000.00 USD | 408,940,000.00 USD | 1,180,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.40` | 166,680,000.00 USD | 166,680,000.00 USD | 27,610.00 USD | 2,670.00 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.40` | 411,270,000.00 USD | 411,270,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.50` | 2,450,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `111.60` | 167,020,000.00 USD | 167,020,000.00 USD | 6,590.00 USD | 147,570.00 USD | 184,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.60` | 412,230,000.00 USD | 412,230,000.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.80` | 167,250,000.00 USD | 167,250,000.00 USD | 126,620.00 USD | 48,150.00 USD | 64,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.80` | 414,590,000.00 USD | 414,590,000.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.00` | 167,550,000.00 USD | 167,550,000.00 USD | 31,510.00 USD | 192,290.00 USD | 73,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.00` | 416,220,000.00 USD | 416,220,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.20` | 168,260,000.00 USD | 168,260,000.00 USD | 369,020.00 USD | 218,430.00 USD | 123,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.20` | 418,420,000.00 USD | 418,420,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.40` | 168,730,000.00 USD | 168,730,000.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.40` | 420,160,000.00 USD | 420,160,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.50` | 223,220.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `112.60` | 169,180,000.00 USD | 169,180,000.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.60` | 421,020,000.00 USD | 421,020,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `112.80` | 169,620,000.00 USD | 169,620,000.00 USD | 16,000.00 USD | 63,410.00 USD | 364,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.80` | 421,890,000.00 USD | 421,890,000.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.00` | 170,220,000.00 USD | 170,220,000.00 USD | 135,210.00 USD | 46,900.00 USD | 418,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.00` | 422,930,000.00 USD | 422,930,000.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.20` | 170,470,000.00 USD | 170,470,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.20` | 424,010,000.00 USD | 424,010,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.40` | 170,630,000.00 USD | 170,630,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.40` | 424,230,000.00 USD | 424,230,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.50` | 54,920.00 USD | 6,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `113.60` | 170,790,000.00 USD | 170,790,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.60` | 424,630,000.00 USD | 424,630,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `113.70` | 170,850,000.00 USD | 170,850,000.00 USD | 0.00 USD | 0.00 USD | 55,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.80` | 424,630,000.00 USD | 424,630,000.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `89.60` | 373,310,000.00 USD | 0.00 USD | 373,310,000.00 USD | 700,630.00 USD | 276,340.00 USD | 577,220.00 USD |
| `7D` | `89.80` | 371,760,000.00 USD | 0.00 USD | 371,760,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `7D` | `90.00` | 370,770,000.00 USD | 0.00 USD | 370,770,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `7D` | `90.20` | 369,050,000.00 USD | 0.00 USD | 369,050,000.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD |
| `7D` | `90.40` | 367,050,000.00 USD | 0.00 USD | 367,050,000.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `90.60` | 180,640,000.00 USD | 0.00 USD | 180,640,000.00 USD | 441,060.00 USD | 495,490.00 USD | 561,930.00 USD |
| `7D` | `90.60` | 365,650,000.00 USD | 0.00 USD | 365,650,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD |
| `1D` | `90.80` | 179,140,000.00 USD | 0.00 USD | 179,140,000.00 USD | 100,370.00 USD | 101,660.00 USD | 1,520.00 USD |
| `7D` | `90.80` | 362,530,000.00 USD | 0.00 USD | 362,530,000.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `91.00` | 178,940,000.00 USD | 0.00 USD | 178,940,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `91.00` | 359,560,000.00 USD | 0.00 USD | 359,560,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `91.20` | 178,750,000.00 USD | 0.00 USD | 178,750,000.00 USD | 27,610.00 USD | 2,670.00 USD | 307.73 USD |
| `7D` | `91.20` | 357,500,000.00 USD | 0.00 USD | 357,500,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `91.40` | 178,720,000.00 USD | 0.00 USD | 178,720,000.00 USD | 68,610.00 USD | 195,720.00 USD | 185,130.00 USD |
| `7D` | `91.40` | 355,170,000.00 USD | 0.00 USD | 355,170,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `91.60` | 178,270,000.00 USD | 0.00 USD | 178,270,000.00 USD | 25,530.00 USD | 162,380.00 USD | 1,680.00 USD |
| `7D` | `91.60` | 351,850,000.00 USD | 0.00 USD | 351,850,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `91.80` | 178,080,000.00 USD | 0.00 USD | 178,080,000.00 USD | 369,020.00 USD | 180,040.00 USD | 67,090.00 USD |
| `7D` | `91.80` | 350,230,000.00 USD | 0.00 USD | 350,230,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 177,460,000.00 USD | 0.00 USD | 177,460,000.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD |
| `7D` | `92.00` | 348,020,000.00 USD | 0.00 USD | 348,020,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `92.20` | 177,000,000.00 USD | 0.00 USD | 177,000,000.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD |
| `7D` | `92.20` | 346,290,000.00 USD | 0.00 USD | 346,290,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `92.40` | 176,550,000.00 USD | 0.00 USD | 176,550,000.00 USD | 151,210.00 USD | 110,310.00 USD | 782,700.00 USD |
| `7D` | `92.40` | 345,430,000.00 USD | 0.00 USD | 345,430,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD |
| `1D` | `92.60` | 175,510,000.00 USD | 0.00 USD | 175,510,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD |
| `7D` | `92.60` | 343,510,000.00 USD | 0.00 USD | 343,510,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `92.80` | 175,250,000.00 USD | 0.00 USD | 175,250,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD |
| `7D` | `92.80` | 342,430,000.00 USD | 0.00 USD | 342,430,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `1D` | `93.00` | 175,100,000.00 USD | 0.00 USD | 175,100,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD |
| `7D` | `93.00` | 342,210,000.00 USD | 0.00 USD | 342,210,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `1D` | `93.20` | 174,930,000.00 USD | 0.00 USD | 174,930,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD |
| `7D` | `93.20` | 341,820,000.00 USD | 0.00 USD | 341,820,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `1D` | `93.40` | 174,720,000.00 USD | 0.00 USD | 174,720,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD |
| `7D` | `93.40` | 341,710,000.00 USD | 0.00 USD | 341,710,000.00 USD | 80,500.00 USD | 115,240.00 USD | 2,890.00 USD |
| `7D` | `93.60` | 341,510,000.00 USD | 0.00 USD | 341,510,000.00 USD | 238,200.00 USD | 343,740.00 USD | 114,860.00 USD |
| `7D` | `93.80` | 340,810,000.00 USD | 0.00 USD | 340,810,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD |
| `7D` | `94.00` | 340,140,000.00 USD | 0.00 USD | 340,140,000.00 USD | 78,790.00 USD | 153,680.00 USD | 134,360.00 USD |
| `7D` | `94.20` | 339,770,000.00 USD | 0.00 USD | 339,770,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD |
| `7D` | `94.40` | 339,110,000.00 USD | 0.00 USD | 339,110,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD |
| `7D` | `94.60` | 338,820,000.00 USD | 0.00 USD | 338,820,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `94.80` | 338,740,000.00 USD | 0.00 USD | 338,740,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD |
| `7D` | `95.00` | 338,710,000.00 USD | 0.00 USD | 338,710,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD |
| `1D` | `95.20` | 174,670,000.00 USD | 0.00 USD | 174,670,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD |
| `7D` | `95.20` | 337,750,000.00 USD | 0.00 USD | 337,750,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD |
| `1D` | `95.40` | 174,650,000.00 USD | 0.00 USD | 174,650,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD |
| `7D` | `95.40` | 337,360,000.00 USD | 0.00 USD | 337,360,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD |
| `1D` | `95.60` | 174,140,000.00 USD | 0.00 USD | 174,140,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD |
| `7D` | `95.60` | 335,840,000.00 USD | 0.00 USD | 335,840,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD |
| `1D` | `95.80` | 171,570,000.00 USD | 0.00 USD | 171,570,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD |
| `7D` | `95.80` | 331,800,000.00 USD | 0.00 USD | 331,800,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD |
| `1D` | `96.00` | 167,750,000.00 USD | 0.00 USD | 167,750,000.00 USD | 1,200,000.00 USD | 1,170,000.00 USD | 1,230,000.00 USD |
| `7D` | `96.00` | 327,560,000.00 USD | 0.00 USD | 327,560,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD |
| `1D` | `96.20` | 164,150,000.00 USD | 0.00 USD | 164,150,000.00 USD | 1,060,000.00 USD | 1,190,000.00 USD | 693,510.00 USD |
| `7D` | `96.20` | 321,120,000.00 USD | 0.00 USD | 321,120,000.00 USD | 2,940,000.00 USD | 1,970,000.00 USD | 1,990,000.00 USD |
| `1D` | `96.40` | 161,210,000.00 USD | 0.00 USD | 161,210,000.00 USD | 862,370.00 USD | 983,090.00 USD | 1,100,000.00 USD |
| `7D` | `96.40` | 314,230,000.00 USD | 0.00 USD | 314,230,000.00 USD | 2,950,000.00 USD | 643,110.00 USD | 2,370,000.00 USD |
| `1D` | `96.60` | 158,260,000.00 USD | 0.00 USD | 158,260,000.00 USD | 994,840.00 USD | 756,910.00 USD | 933,760.00 USD |
| `7D` | `96.60` | 308,260,000.00 USD | 0.00 USD | 308,260,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD |
| `1D` | `96.80` | 155,580,000.00 USD | 0.00 USD | 155,580,000.00 USD | 307,030.00 USD | 737,250.00 USD | 729,790.00 USD |
| `7D` | `96.80` | 300,160,000.00 USD | 0.00 USD | 300,160,000.00 USD | 3,000,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD |
| `1D` | `97.00` | 153,800,000.00 USD | 0.00 USD | 153,800,000.00 USD | 310,450.00 USD | 114,330.00 USD | 110,200.00 USD |
| `7D` | `97.00` | 291,420,000.00 USD | 0.00 USD | 291,420,000.00 USD | 5,480,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD |
| `1D` | `97.20` | 153,270,000.00 USD | 0.00 USD | 153,270,000.00 USD | 350,270.00 USD | 11,630.00 USD | 413,200.00 USD |
| `7D` | `97.20` | 281,360,000.00 USD | 0.00 USD | 281,360,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD |
| `1D` | `97.40` | 152,490,000.00 USD | 0.00 USD | 152,490,000.00 USD | 1,050,000.00 USD | 916,790.00 USD | 503,240.00 USD |
| `7D` | `97.40` | 267,550,000.00 USD | 0.00 USD | 267,550,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD |
| `1D` | `97.60` | 150,020,000.00 USD | 0.00 USD | 150,020,000.00 USD | 2,070,000.00 USD | 1,870,000.00 USD | 1,920,000.00 USD |
| `7D` | `97.60` | 257,130,000.00 USD | 0.00 USD | 257,130,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD |
| `1D` | `97.80` | 144,160,000.00 USD | 0.00 USD | 144,160,000.00 USD | 3,830,000.00 USD | 3,090,000.00 USD | 1,960,000.00 USD |
| `7D` | `97.80` | 241,790,000.00 USD | 0.00 USD | 241,790,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD |
| `1D` | `98.00` | 135,280,000.00 USD | 0.00 USD | 135,280,000.00 USD | 3,680,000.00 USD | 3,010,000.00 USD | 3,190,000.00 USD |
| `7D` | `98.00` | 228,330,000.00 USD | 0.00 USD | 228,330,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,710,000.00 USD |
| `1D` | `98.20` | 125,400,000.00 USD | 0.00 USD | 125,400,000.00 USD | 3,040,000.00 USD | 2,880,000.00 USD | 2,030,000.00 USD |
| `7D` | `98.20` | 203,650,000.00 USD | 0.00 USD | 203,650,000.00 USD | 7,790,000.00 USD | 6,660,000.00 USD | 5,670,000.00 USD |
| `1D` | `98.40` | 117,450,000.00 USD | 0.00 USD | 117,450,000.00 USD | 3,740,000.00 USD | 3,150,000.00 USD | 3,460,000.00 USD |
| `7D` | `98.40` | 183,530,000.00 USD | 0.00 USD | 183,530,000.00 USD | 9,460,000.00 USD | 2,950,000.00 USD | 9,620,000.00 USD |
| `1D` | `98.60` | 107,100,000.00 USD | 0.00 USD | 107,100,000.00 USD | 6,200,000.00 USD | 4,440,000.00 USD | 6,740,000.00 USD |
| `7D` | `98.60` | 161,490,000.00 USD | 0.00 USD | 161,490,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD |
| `1D` | `98.80` | 89,710,000.00 USD | 0.00 USD | 89,710,000.00 USD | 7,300,000.00 USD | 6,980,000.00 USD | 5,060,000.00 USD |
| `7D` | `98.80` | 126,000,000.00 USD | 0.00 USD | 126,000,000.00 USD | 12,600,000.00 USD | 9,880,000.00 USD | 13,080,000.00 USD |
| `1D` | `99.00` | 70,380,000.00 USD | 0.00 USD | 70,380,000.00 USD | 5,060,000.00 USD | 4,770,000.00 USD | 5,340,000.00 USD |
| `7D` | `99.00` | 90,440,000.00 USD | 0.00 USD | 90,440,000.00 USD | 14,230,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD |
| `1D` | `99.20` | 55,210,000.00 USD | 0.00 USD | 55,210,000.00 USD | 4,590,000.00 USD | 4,640,000.00 USD | 3,770,000.00 USD |
| `7D` | `99.20` | 48,820,000.00 USD | 0.00 USD | 48,820,000.00 USD | 12,590,000.00 USD | 6,970,000.00 USD | 5,910,000.00 USD |
| `1D` | `99.40` | 42,210,000.00 USD | 0.00 USD | 42,210,000.00 USD | 3,410,000.00 USD | 4,060,000.00 USD | 4,870,000.00 USD |
| `7D` | `99.40` | 23,350,000.00 USD | 0.00 USD | 23,350,000.00 USD | 2,300,000.00 USD | 599,290.00 USD | 6,690,000.00 USD |
| `1D` | `99.60` | 29,870,000.00 USD | 0.00 USD | 29,870,000.00 USD | 3,330,000.00 USD | 2,990,000.00 USD | 2,970,000.00 USD |
| `7D` | `99.60` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD |
| `1D` | `99.80` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 1,490,000.00 USD | 2,600,000.00 USD | 3,150,000.00 USD |
| `7D` | `99.80` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD |
| `1D` | `100.00` | 13,340,000.00 USD | 0.00 USD | 13,340,000.00 USD | 2,110,000.00 USD | 1,230,000.00 USD | 882,050.00 USD |
| `7D` | `100.00` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD |
| `1D` | `100.20` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 441,980.00 USD | 341,570.00 USD | 972,450.00 USD |
| `7D` | `100.20` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD |
| `1D` | `100.40` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 718,910.00 USD | 877,160.00 USD | 438,820.00 USD |
| `7D` | `100.40` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 78,970.00 USD | 68,710.00 USD | 1,170,000.00 USD |
| `1D` | `100.60` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 1,200,000.00 USD | 251,930.00 USD | 2,790,000.00 USD |
| `7D` | `100.60` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD |
| `1D` | `100.80` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 274,280.00 USD | 802,330.00 USD | 4,380.00 USD |
| `7D` | `100.80` | 981,100.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD |
| `1D` | `101.00` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 6,610,000.00 USD | 953,600.00 USD | 5,230.00 USD |
| `1D` | `101.00` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 6,610,000.00 USD | 953,600.00 USD | 5,230.00 USD |
| `7D` | `101.00` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 0.00 USD | 4,560,000.00 USD | 3,730,000.00 USD |
| `7D` | `101.00` | 16,580,000.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 4,560,000.00 USD | 3,730,000.00 USD |
| `1D` | `101.20` | 27,860,000.00 USD | 27,860,000.00 USD | 0.00 USD | 2,650,000.00 USD | 7,010,000.00 USD | 3,050,000.00 USD |
| `7D` | `101.20` | 24,440,000.00 USD | 24,440,000.00 USD | 0.00 USD | 2,190,000.00 USD | 3,220,000.00 USD | 2,450,000.00 USD |
| `1D` | `101.40` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 692,280.00 USD | 609,630.00 USD | 1,690.00 USD |
| `7D` | `101.40` | 34,950,000.00 USD | 34,950,000.00 USD | 0.00 USD | 3,020,000.00 USD | 0.00 USD | 7,490,000.00 USD |
| `1D` | `101.60` | 48,920,000.00 USD | 48,920,000.00 USD | 0.00 USD | 4,420,000.00 USD | 2,220,000.00 USD | 13,110,000.00 USD |
| `7D` | `101.60` | 44,800,000.00 USD | 44,800,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD |
| `1D` | `101.80` | 55,490,000.00 USD | 55,490,000.00 USD | 0.00 USD | 212,730.00 USD | 142,780.00 USD | 6,210,000.00 USD |
| `7D` | `101.80` | 54,150,000.00 USD | 54,150,000.00 USD | 0.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD |
| `1D` | `102.00` | 57,830,000.00 USD | 57,830,000.00 USD | 0.00 USD | 1,110,000.00 USD | 439,590.00 USD | 793,500.00 USD |
| `7D` | `102.00` | 56,820,000.00 USD | 56,820,000.00 USD | 0.00 USD | 843,730.00 USD | 0.00 USD | 1,830,000.00 USD |
| `1D` | `102.20` | 61,510,000.00 USD | 61,510,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,160,000.00 USD | 1,300,000.00 USD |
| `7D` | `102.20` | 60,090,000.00 USD | 60,090,000.00 USD | 0.00 USD | 369,280.00 USD | 578,040.00 USD | 2,320,000.00 USD |
| `1D` | `102.40` | 63,090,000.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,590,000.00 USD |
| `7D` | `102.40` | 63,120,000.00 USD | 63,120,000.00 USD | 0.00 USD | 1,150,000.00 USD | 299,640.00 USD | 1,580,000.00 USD |
| `1D` | `102.60` | 63,320,000.00 USD | 63,320,000.00 USD | 0.00 USD | 194,440.00 USD | 26,340.00 USD | 8,280.00 USD |
| `7D` | `102.60` | 65,540,000.00 USD | 65,540,000.00 USD | 0.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD |
| `1D` | `102.80` | 67,120,000.00 USD | 67,120,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,870,000.00 USD | 563,120.00 USD |
| `7D` | `102.80` | 73,410,000.00 USD | 73,410,000.00 USD | 0.00 USD | 7,600,000.00 USD | 0.00 USD | 277,920.00 USD |
| `1D` | `103.00` | 71,370,000.00 USD | 71,370,000.00 USD | 0.00 USD | 2,600,000.00 USD | 1,430,000.00 USD | 220,410.00 USD |
| `7D` | `103.00` | 87,890,000.00 USD | 87,890,000.00 USD | 0.00 USD | 11,640,000.00 USD | 0.00 USD | 2,830,000.00 USD |
| `1D` | `103.20` | 77,430,000.00 USD | 77,430,000.00 USD | 0.00 USD | 1,840,000.00 USD | 2,390,000.00 USD | 1,820,000.00 USD |
| `7D` | `103.20` | 102,170,000.00 USD | 102,170,000.00 USD | 0.00 USD | 13,650,000.00 USD | 4,380.00 USD | 631,060.00 USD |
| `1D` | `103.40` | 84,710,000.00 USD | 84,710,000.00 USD | 0.00 USD | 3,970,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD |
| `7D` | `103.40` | 117,180,000.00 USD | 117,180,000.00 USD | 0.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD |
| `1D` | `103.60` | 99,110,000.00 USD | 99,110,000.00 USD | 0.00 USD | 4,260,000.00 USD | 2,110,000.00 USD | 8,040,000.00 USD |
| `7D` | `103.60` | 135,570,000.00 USD | 135,570,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 108,600,000.00 USD | 108,600,000.00 USD | 0.00 USD | 3,360,000.00 USD | 2,690,000.00 USD | 3,430,000.00 USD |
| `7D` | `103.80` | 147,910,000.00 USD | 147,910,000.00 USD | 0.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 120,400,000.00 USD | 120,400,000.00 USD | 0.00 USD | 3,920,000.00 USD | 3,630,000.00 USD | 4,250,000.00 USD |
| `7D` | `104.00` | 176,330,000.00 USD | 176,330,000.00 USD | 0.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD |
| `1D` | `104.20` | 129,430,000.00 USD | 129,430,000.00 USD | 0.00 USD | 3,440,000.00 USD | 2,450,000.00 USD | 3,140,000.00 USD |
| `7D` | `104.20` | 196,420,000.00 USD | 196,420,000.00 USD | 0.00 USD | 7,510,000.00 USD | 6,900,000.00 USD | 5,680,000.00 USD |
| `1D` | `104.40` | 137,590,000.00 USD | 137,590,000.00 USD | 0.00 USD | 3,160,000.00 USD | 1,660,000.00 USD | 3,340,000.00 USD |
| `7D` | `104.40` | 212,550,000.00 USD | 212,550,000.00 USD | 0.00 USD | 4,800,000.00 USD | 3,700,000.00 USD | 7,640,000.00 USD |
| `1D` | `104.60` | 145,900,000.00 USD | 145,900,000.00 USD | 0.00 USD | 2,260,000.00 USD | 2,030,000.00 USD | 4,030,000.00 USD |
| `7D` | `104.60` | 230,120,000.00 USD | 230,120,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD |
| `1D` | `104.80` | 152,190,000.00 USD | 152,190,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,620,000.00 USD | 3,060,000.00 USD |
| `7D` | `104.80` | 247,250,000.00 USD | 247,250,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD |
| `1D` | `105.00` | 154,690,000.00 USD | 154,690,000.00 USD | 0.00 USD | 708,730.00 USD | 754,560.00 USD | 1,040,000.00 USD |
| `7D` | `105.00` | 264,350,000.00 USD | 264,350,000.00 USD | 0.00 USD | 5,700,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 156,030,000.00 USD | 156,030,000.00 USD | 0.00 USD | 514,940.00 USD | 4,110.00 USD | 814,780.00 USD |
| `7D` | `105.20` | 277,060,000.00 USD | 277,060,000.00 USD | 0.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.40` | 157,150,000.00 USD | 157,150,000.00 USD | 0.00 USD | 312,780.00 USD | 7,520.00 USD | 803,640.00 USD |
| `7D` | `105.40` | 289,710,000.00 USD | 289,710,000.00 USD | 0.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 5,240,000.00 USD |
| `1D` | `105.60` | 159,570,000.00 USD | 159,570,000.00 USD | 0.00 USD | 507,390.00 USD | 913,400.00 USD | 995,740.00 USD |
| `7D` | `105.60` | 307,180,000.00 USD | 307,180,000.00 USD | 0.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD |
| `1D` | `105.80` | 160,920,000.00 USD | 160,920,000.00 USD | 0.00 USD | 354,630.00 USD | 708,710.00 USD | 287,640.00 USD |
| `7D` | `105.80` | 318,150,000.00 USD | 318,150,000.00 USD | 0.00 USD | 3,560,000.00 USD | 3,200,000.00 USD | 4,210,000.00 USD |
| `1D` | `106.00` | 162,150,000.00 USD | 162,150,000.00 USD | 0.00 USD | 408,900.00 USD | 456,530.00 USD | 362,090.00 USD |
| `7D` | `106.00` | 329,750,000.00 USD | 329,750,000.00 USD | 0.00 USD | 4,740,000.00 USD | 3,150,000.00 USD | 3,710,000.00 USD |
| `1D` | `106.20` | 164,840,000.00 USD | 164,840,000.00 USD | 0.00 USD | 1,280,000.00 USD | 675,100.00 USD | 740,340.00 USD |
| `7D` | `106.20` | 344,250,000.00 USD | 344,250,000.00 USD | 0.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,970,000.00 USD |
| `1D` | `106.40` | 166,900,000.00 USD | 166,900,000.00 USD | 0.00 USD | 918,780.00 USD | 500,580.00 USD | 640,280.00 USD |
| `7D` | `106.40` | 352,760,000.00 USD | 352,760,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 2,250,000.00 USD |
| `1D` | `106.60` | 169,660,000.00 USD | 169,660,000.00 USD | 0.00 USD | 957,870.00 USD | 536,470.00 USD | 1,260,000.00 USD |
| `7D` | `106.60` | 361,960,000.00 USD | 361,960,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD |
| `1D` | `106.80` | 171,660,000.00 USD | 171,660,000.00 USD | 0.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD |
| `7D` | `106.80` | 367,850,000.00 USD | 367,850,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD |
| `1D` | `107.00` | 172,640,000.00 USD | 172,640,000.00 USD | 0.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD |
| `7D` | `107.00` | 373,410,000.00 USD | 373,410,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD |
| `1D` | `107.20` | 173,020,000.00 USD | 173,020,000.00 USD | 0.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD |
| `7D` | `107.20` | 375,130,000.00 USD | 375,130,000.00 USD | 0.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD |
| `1D` | `107.40` | 173,500,000.00 USD | 173,500,000.00 USD | 0.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD |
| `7D` | `107.40` | 376,110,000.00 USD | 376,110,000.00 USD | 0.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD |
| `1D` | `107.60` | 173,990,000.00 USD | 173,990,000.00 USD | 0.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD |
| `7D` | `107.60` | 376,480,000.00 USD | 376,480,000.00 USD | 0.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD |
| `1D` | `107.80` | 174,300,000.00 USD | 174,300,000.00 USD | 0.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD |
| `7D` | `107.80` | 377,360,000.00 USD | 377,360,000.00 USD | 0.00 USD | 499,750.00 USD | 100,420.00 USD | 281,400.00 USD |
| `7D` | `108.00` | 377,990,000.00 USD | 377,990,000.00 USD | 0.00 USD | 293,270.00 USD | 252,740.00 USD | 82,880.00 USD |
| `7D` | `108.20` | 380,400,000.00 USD | 380,400,000.00 USD | 0.00 USD | 966,370.00 USD | 938,650.00 USD | 503,200.00 USD |
| `7D` | `108.40` | 382,890,000.00 USD | 382,890,000.00 USD | 0.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD |
| `7D` | `108.60` | 384,310,000.00 USD | 384,310,000.00 USD | 0.00 USD | 401,600.00 USD | 515,740.00 USD | 505,810.00 USD |
| `7D` | `108.80` | 386,990,000.00 USD | 386,990,000.00 USD | 0.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD |
| `1D` | `109.00` | 174,300,000.00 USD | 174,300,000.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `109.00` | 387,530,000.00 USD | 387,530,000.00 USD | 0.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD |
| `1D` | `109.20` | 174,320,000.00 USD | 174,320,000.00 USD | 0.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD |
| `7D` | `109.20` | 388,750,000.00 USD | 388,750,000.00 USD | 0.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD |
| `1D` | `109.40` | 174,440,000.00 USD | 174,440,000.00 USD | 0.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD |
| `7D` | `109.40` | 389,090,000.00 USD | 389,090,000.00 USD | 0.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD |
| `1D` | `109.60` | 175,100,000.00 USD | 175,100,000.00 USD | 0.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD |
| `7D` | `109.60` | 390,150,000.00 USD | 390,150,000.00 USD | 0.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD |
| `1D` | `109.80` | 176,130,000.00 USD | 176,130,000.00 USD | 0.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD |
| `7D` | `109.80` | 391,130,000.00 USD | 391,130,000.00 USD | 0.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `1D` | `110.00` | 177,200,000.00 USD | 177,200,000.00 USD | 0.00 USD | 213,690.00 USD | 401,420.00 USD | 453,270.00 USD |
| `7D` | `110.00` | 392,850,000.00 USD | 392,850,000.00 USD | 0.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `1D` | `110.20` | 178,070,000.00 USD | 178,070,000.00 USD | 0.00 USD | 228,950.00 USD | 389,380.00 USD | 250,700.00 USD |
| `7D` | `110.20` | 394,860,000.00 USD | 394,860,000.00 USD | 0.00 USD | 851,120.00 USD | 573,800.00 USD | 577,690.00 USD |
| `1D` | `110.40` | 178,950,000.00 USD | 178,950,000.00 USD | 0.00 USD | 277,830.00 USD | 269,600.00 USD | 337,940.00 USD |
| `7D` | `110.40` | 396,250,000.00 USD | 396,250,000.00 USD | 0.00 USD | 673,280.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `110.60` | 179,370,000.00 USD | 179,370,000.00 USD | 0.00 USD | 110,850.00 USD | 71,980.00 USD | 239,910.00 USD |
| `7D` | `110.60` | 397,360,000.00 USD | 397,360,000.00 USD | 0.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD |
| `1D` | `110.80` | 180,060,000.00 USD | 180,060,000.00 USD | 0.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD |
| `7D` | `110.80` | 399,370,000.00 USD | 399,370,000.00 USD | 0.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD |
| `1D` | `111.00` | 180,260,000.00 USD | 180,260,000.00 USD | 0.00 USD | 100,370.00 USD | 101,660.00 USD | 1,520.00 USD |
| `7D` | `111.00` | 402,340,000.00 USD | 402,340,000.00 USD | 0.00 USD | 1,200,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `111.20` | 180,450,000.00 USD | 180,450,000.00 USD | 0.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `111.20` | 404,400,000.00 USD | 404,400,000.00 USD | 0.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `111.40` | 180,480,000.00 USD | 180,480,000.00 USD | 0.00 USD | 27,610.00 USD | 2,670.00 USD | 307.73 USD |
| `7D` | `111.40` | 406,730,000.00 USD | 406,730,000.00 USD | 0.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `111.60` | 180,820,000.00 USD | 180,820,000.00 USD | 0.00 USD | 6,590.00 USD | 147,570.00 USD | 184,010.00 USD |
| `7D` | `111.60` | 407,690,000.00 USD | 407,690,000.00 USD | 0.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD |
| `1D` | `111.80` | 180,930,000.00 USD | 180,930,000.00 USD | 0.00 USD | 62,020.00 USD | 48,150.00 USD | 1,130.00 USD |
| `7D` | `111.80` | 410,050,000.00 USD | 410,050,000.00 USD | 0.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD |
| `1D` | `112.00` | 181,120,000.00 USD | 181,120,000.00 USD | 0.00 USD | 25,530.00 USD | 162,380.00 USD | 1,680.00 USD |
| `7D` | `112.00` | 411,680,000.00 USD | 411,680,000.00 USD | 0.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `112.20` | 181,740,000.00 USD | 181,740,000.00 USD | 0.00 USD | 369,020.00 USD | 180,040.00 USD | 67,090.00 USD |
| `7D` | `112.20` | 413,880,000.00 USD | 413,880,000.00 USD | 0.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `112.40` | 182,200,000.00 USD | 182,200,000.00 USD | 0.00 USD | 142,430.00 USD | 121,090.00 USD | 200,830.00 USD |
| `7D` | `112.40` | 415,620,000.00 USD | 415,620,000.00 USD | 0.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `112.60` | 182,650,000.00 USD | 182,650,000.00 USD | 0.00 USD | 215,200.00 USD | 41,930.00 USD | 191,690.00 USD |
| `7D` | `112.60` | 416,480,000.00 USD | 416,480,000.00 USD | 0.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `112.80` | 183,090,000.00 USD | 183,090,000.00 USD | 0.00 USD | 16,000.00 USD | 63,410.00 USD | 364,110.00 USD |
| `7D` | `112.80` | 417,350,000.00 USD | 417,350,000.00 USD | 0.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD |
| `1D` | `113.00` | 183,690,000.00 USD | 183,690,000.00 USD | 0.00 USD | 135,210.00 USD | 46,900.00 USD | 418,590.00 USD |
| `7D` | `113.00` | 418,390,000.00 USD | 418,390,000.00 USD | 0.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD |
| `1D` | `113.20` | 183,950,000.00 USD | 183,950,000.00 USD | 0.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD |
| `7D` | `113.20` | 419,470,000.00 USD | 419,470,000.00 USD | 0.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `113.40` | 184,100,000.00 USD | 184,100,000.00 USD | 0.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD |
| `7D` | `113.40` | 419,690,000.00 USD | 419,690,000.00 USD | 0.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `1D` | `113.50` | 184,210,000.00 USD | 184,210,000.00 USD | 0.00 USD | 45,270.00 USD | 0.00 USD | 60,580.00 USD |
| `7D` | `113.60` | 420,090,000.00 USD | 420,090,000.00 USD | 0.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.80` | 420,090,000.00 USD | 420,090,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `BALANCED` | 1,620.00 USD | 0.00 USD | 1,620.00 USD | -1,620.00 USD | `1` | `2026-10-29 18:05:00 UTC - 2026-10-29 18:10:00 UTC` |
| `15m` | `BALANCED` | 1,620.00 USD | 0.00 USD | 1,620.00 USD | -1,620.00 USD | `1` | `2026-10-29 18:00:00 UTC - 2026-10-29 18:15:00 UTC` |
| `1h` | `BALANCED` | 1,620.00 USD | 0.00 USD | 1,620.00 USD | -1,620.00 USD | `1` | `2026-10-29 18:00:00 UTC - 2026-10-29 19:00:00 UTC` |
| `4h` | `BALANCED` | 1,620.00 USD | 0.00 USD | 1,620.00 USD | -1,620.00 USD | `1` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.27B` | Total OI Tokens: `61,999,215.1 SOL`
  * 1h OI Change: `-0.61%` | 4h OI Change: `-3.22%` | 24h OI Change: `-2.41%`
  * Exchange Breakdown: Binance=`1.10B` | Bybit=`618.50M` | OKX=`355.76M` | Hyperliquid=`569.88M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `195.27K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0074%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `50.83%` | `49.17%` | `1.03` | 55,440,000.00 USD |
| `15M` | `Binance` | `49.64%` | `50.36%` | `0.99` | 17,210,000.00 USD |
| `15M` | `OKX` | `60.59%` | `39.41%` | `1.54` | 8,000,000.00 USD |
| `15M` | `Bybit` | `47.26%` | `52.74%` | `0.90` | 5,140,000.00 USD |
| `15M` | `KuCoin` | `80.71%` | `19.29%` | `4.18` | 388,300.00 USD |
| `15M` | `Gate` | `43.48%` | `56.52%` | `0.77` | 5,310,000.00 USD |
| `15M` | `Bitget` | `44.76%` | `55.24%` | `0.81` | 1,120,000.00 USD |
| `15M` | `BingX` | `52.87%` | `47.13%` | `1.12` | 3,380,000.00 USD |
| `15M` | `MEXC` | `52.21%` | `47.79%` | `1.09` | 6,130,000.00 USD |
| `15M` | `Bitunix` | `54.23%` | `45.77%` | `1.18` | 3,360,000.00 USD |
| `15M` | `Hyperliquid` | `58.33%` | `41.67%` | `1.40` | 2,110,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.95%` | `45.05%` | `1.22` | 464,760.00 USD |
| `15M` | `Crypto.com` | `58.07%` | `41.93%` | `1.38` | 81,640.00 USD |
| `15M` | `WhiteBIT` | `10.69%` | `89.31%` | `0.12` | 1,510,000.00 USD |
| `15M` | `HTX` | `66.04%` | `33.96%` | `1.94` | 43,090.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `75.61%` | `24.39%` | `3.10` | 557,430.00 USD |
| `15M` | `Aster` | `49.73%` | `50.27%` | `0.99` | 173,600.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `42.02%` | `57.98%` | `0.72` | 445,450.00 USD |
| `15M` | `Whale Positions` | `49.64%` | `50.36%` | `0.99` | 17,210,000.00 USD |
| `15M` | `Global Accounts` | `50.83%` | `49.17%` | `1.03` | 55,440,000.00 USD |
| `1H` | `SOL` | `44.99%` | `55.01%` | `0.82` | 265,040,000.00 USD |
| `1H` | `Binance` | `45.88%` | `54.12%` | `0.85` | 90,950,000.00 USD |
| `1H` | `OKX` | `43.84%` | `56.16%` | `0.78` | 37,070,000.00 USD |
| `1H` | `Bybit` | `40.46%` | `59.54%` | `0.68` | 23,030,000.00 USD |
| `1H` | `KuCoin` | `54.55%` | `45.45%` | `1.20` | 1,410,000.00 USD |
| `1H` | `Gate` | `49.12%` | `50.88%` | `0.97` | 23,640,000.00 USD |
| `1H` | `Bitget` | `32.71%` | `67.29%` | `0.49` | 8,070,000.00 USD |
| `1H` | `BingX` | `54.33%` | `45.67%` | `1.19` | 13,860,000.00 USD |
| `1H` | `MEXC` | `47.28%` | `52.72%` | `0.90` | 25,510,000.00 USD |
| `1H` | `Bitunix` | `49.13%` | `50.87%` | `0.97` | 16,370,000.00 USD |
| `1H` | `Hyperliquid` | `38.05%` | `61.95%` | `0.61` | 6,830,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `57.52%` | `42.48%` | `1.35` | 2,050,000.00 USD |
| `1H` | `Crypto.com` | `42.72%` | `57.28%` | `0.75` | 550,250.00 USD |
| `1H` | `WhiteBIT` | `10.49%` | `89.51%` | `0.12` | 6,850,000.00 USD |
| `1H` | `HTX` | `62.66%` | `37.34%` | `1.68` | 430,510.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `68.71%` | `31.29%` | `2.20` | 3,260,000.00 USD |
| `1H` | `Aster` | `44.49%` | `55.51%` | `0.80` | 1,820,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.56%` | `62.44%` | `0.60` | 3,360,000.00 USD |
| `1H` | `Whale Positions` | `45.88%` | `54.12%` | `0.85` | 90,950,000.00 USD |
| `1H` | `Global Accounts` | `44.99%` | `55.01%` | `0.82` | 265,040,000.00 USD |
| `4H` | `SOL` | `48.21%` | `51.79%` | `0.93` | 1,610,000,000.00 USD |
| `4H` | `Binance` | `48.86%` | `51.14%` | `0.96` | 529,340,000.00 USD |
| `4H` | `OKX` | `48.08%` | `51.92%` | `0.93` | 261,190,000.00 USD |
| `4H` | `Bybit` | `53.22%` | `46.78%` | `1.14` | 157,820,000.00 USD |
| `4H` | `KuCoin` | `56.26%` | `43.74%` | `1.29` | 10,320,000.00 USD |
| `4H` | `Gate` | `50.02%` | `49.98%` | `1.00` | 123,890,000.00 USD |
| `4H` | `Bitget` | `47.31%` | `52.69%` | `0.90` | 55,310,000.00 USD |
| `4H` | `BingX` | `41.27%` | `58.73%` | `0.70` | 72,420,000.00 USD |
| `4H` | `MEXC` | `45.51%` | `54.49%` | `0.84` | 153,850,000.00 USD |
| `4H` | `Bitunix` | `49.88%` | `50.12%` | `1.00` | 85,570,000.00 USD |
| `4H` | `Hyperliquid` | `53.26%` | `46.74%` | `1.14` | 44,230,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.86%` | `50.14%` | `0.99` | 20,940,000.00 USD |
| `4H` | `Crypto.com` | `46.91%` | `53.09%` | `0.88` | 2,580,000.00 USD |
| `4H` | `WhiteBIT` | `19.34%` | `80.66%` | `0.24` | 22,900,000.00 USD |
| `4H` | `HTX` | `56.76%` | `43.24%` | `1.31` | 2,590,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.5%` | `56.5%` | `0.77` | 35,130,000.00 USD |
| `4H` | `Aster` | `42.5%` | `57.5%` | `0.74` | 16,500,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.62%` | `47.38%` | `1.11` | 15,550,000.00 USD |
| `4H` | `Whale Positions` | `48.86%` | `51.14%` | `0.96` | 529,340,000.00 USD |
| `4H` | `Global Accounts` | `48.21%` | `51.79%` | `0.93` | 1,610,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `102.50` | `102.51` | `102.50` | `102.70` | `102.32` | 23,288,646.41 USD | 10,642,310.31 USD | 12,646,336.10 USD | -2,004,025.79 USD | `-8.61%` | `2B / 8S` |
| `0:00 UTC` | `102.63` | `102.77` | `102.63` | `103.16` | `102.38` | 44,107,518.93 USD | 20,981,384.68 USD | 23,126,134.25 USD | -2,144,749.57 USD | `-4.86%` | `8B / 10S` |
| `5:00 UTC` | `102.31` | `102.32` | `102.31` | `102.66` | `102.10` | 27,443,327.62 USD | 11,049,929.69 USD | 16,393,397.93 USD | -5,343,468.24 USD | `-19.47%` | `1B / 16S` |
| `0:00 UTC` | `102.00` | `102.00` | `102.00` | `102.22` | `101.81` | 25,493,228.16 USD | 11,241,280.68 USD | 14,251,947.48 USD | -3,010,666.79 USD | `-11.81%` | `2B / 10S` |
| `5:00 UTC` | `101.94` | `101.88` | `101.94` | `102.02` | `101.75` | 15,546,239.68 USD | 7,009,090.38 USD | 8,537,149.31 USD | -1,528,058.93 USD | `-9.83%` | `0B / 1S` |
| `0:00 UTC` | `101.70` | `101.72` | `101.70` | `101.94` | `101.53` | 20,486,970.74 USD | 7,002,058.55 USD | 13,484,912.18 USD | -6,482,853.63 USD | `-31.64%` | `0B / 15S` |
| `5:00 UTC` | `101.65` | `101.65` | `101.65` | `101.78` | `101.53` | 12,871,901.66 USD | 6,991,731.87 USD | 5,880,169.78 USD | 1,111,562.09 USD | `+8.64%` | `1B / 2S` |
| `0:00 UTC` | `101.00` | `101.32` | `101.00` | `101.77` | `100.97` | 23,345,961.64 USD | 9,081,895.18 USD | 14,264,066.46 USD | -5,182,171.27 USD | `-22.20%` | `6B / 20S` |
| `5:00 UTC` | `100.91` | `100.89` | `100.91` | `101.13` | `100.72` | 21,682,501.47 USD | 10,212,926.11 USD | 11,469,575.36 USD | -1,256,649.25 USD | `-5.80%` | `6B / 4S` |
| `0:00 UTC` | `101.07` | `101.04` | `101.07` | `101.12` | `100.97` | 3,118,864.99 USD | 1,210,410.14 USD | 1,908,454.86 USD | -698,044.72 USD | `-22.38%` | `0B / 3S` |

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
| `5m` | 228,020.00 USD | 1,090,000.00 USD | **`ACCUMULATION`** |
| `15m` | 452,830.00 USD | 2,680,000.00 USD | **`ACCUMULATION`** |
| `30m` | -2,020,000.00 USD | -11,850,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,420,000.00 USD | -15,130,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -343,690.00 USD | -49,460,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 10,250,000.00 USD | -16,550,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 14,410,000.00 USD | -24,110,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 14,350,000.00 USD | -43,090,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 24,380,000.00 USD | -45,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 32,640,000.00 USD | -112,530,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 85,280,000.00 USD | -289,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 65,610,000.00 USD | -1,880,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+228.02K` | 15m=`+452.83K` | 1h=`-3.42M` | 24h=`+32.64M`
* Futures Capital Netflows: 5m=`+1.09M` | 15m=`+2.68M` | 1h=`-15.13M` | 24h=`-112.53M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `99.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `98.05` (Risk Distance: `0.9872` pts)
  * +2.5R Take Profit: `101.51`
  * Mathematical Lot Sizing: **`10.13 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.35` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.34` (Risk Distance: `0.9872` pts)
  * +2.5R Take Profit: `98.88`
  * Mathematical Lot Sizing: **`10.13 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`101.84`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
