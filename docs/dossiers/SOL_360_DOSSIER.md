# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 09:49:26 IST` (`2026-10-30 04:19:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `97.08` | **Live Ask Quote**: `97.31` | **Mid Price**: `97.19`
- **Spread Points**: `23.00` | **Spread BPS**: `23.66 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `94.45` | VWAP Z-Score: `+2.30` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.8741` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `97.71` | Lower -3.00σ Band: `91.18`
  * Upper +2.51σ Band: `97.18` | Lower -2.51σ Band: `91.72`
  * Upper +2.01σ Band: `96.63` | Lower -2.01σ Band: `92.26`
  * Upper +2.00σ Band: `96.62` | Lower -2.00σ Band: `92.27`
  * Upper +1.28σ Band: `95.84` | Lower -1.28σ Band: `93.05`
  * Upper +1.00σ Band: `95.54` | Lower -1.00σ Band: `93.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`95.87` | EMA-20=`95.69` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`96.93` (Slope: `+0.0000`) | EMA-100=`98.28`
  * Institutional Anchors: EMA-144=`98.88` | EMA-200=`99.32` (Slope: `-0.5306`) | EMA-233=`99.57`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `97.54` (Distance: `-0.39%`)
  * Point of Control (POC) = `96.54` (Distance: `+0.64%`)
  * Value Area Low (VAL) = `94.31` (Distance: `+3.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.86` | Weekly POC=`100.92` | Weekly VAL=`99.59`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`97.58` | Low=`96.81`
  * New York Session (13:00-21:00 UTC): High=`97.78` | Low=`96.61`
  * Initial Balance (First Hour): IB High=`97.49` | IB Low=`96.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.81` - `97.58`
  * Optimal Trade Entry (OTE 0.705): `97.39`
  * Structural Invalidation Anchor (0.786): `97.97`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `96.61` | `96.83` | `96.42` | `96.76` | `151,691` | 14,655,257.31 USD | -1,452,197.90 USD | `-9.91%` | -193,641,167.89 USD | `-1.75` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `96.75` | `96.99` | `96.73` | `96.97` | `91,785` | 8,889,898.56 USD | -207,792.04 USD | `-2.34%` | -193,848,959.93 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `96.97` | `97.23` | `96.88` | `97.15` | `110,052` | 10,679,162.67 USD | 1,690,875.11 USD | `+15.83%` | -192,158,084.82 USD | `+0.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `95.60` | `96.22` | `95.47` | `96.14` | `155,206` | 14,869,396.80 USD | 2,961,535.05 USD | `+19.92%` | -195,165,077.00 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `96.14` | `96.99` | `96.09` | `96.97` | `377,426` | 36,449,738.16 USD | 1,028,112.62 USD | `+2.82%` | -194,136,964.38 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `96.97` | `97.23` | `96.88` | `97.15` | `110,052` | 10,679,162.67 USD | 1,690,875.11 USD | `+15.83%` | -192,446,089.27 USD | `+0.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `94.83` | `94.95` | `93.09` | `93.94` | `1,523,328` | 143,343,122.66 USD | -9,061,130.68 USD | `-6.32%` | -208,016,721.32 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `93.94` | `95.50` | `93.46` | `95.37` | `1,008,098` | 95,532,788.00 USD | 7,630,937.68 USD | `+7.99%` | -200,385,783.64 USD | `+0.97` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `95.37` | `97.23` | `95.32` | `97.16` | `893,088` | 85,970,664.27 USD | 7,969,758.65 USD | `+9.27%` | -192,416,024.99 USD | `+0.95` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -32,437,669.41 USD | `-1.68` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -148,311,095.06 USD | `-1.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.15` | `7,623,611` | 719,378,777.10 USD | -44,134,994.21 USD | `-6.14%` | -192,446,089.27 USD | `-0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | 1,363,040.70 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -194,886.64 USD | `-0.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -32,437,669.41 USD | `-1.68` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -148,311,095.06 USD | `-1.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.15` | `7,623,611` | 719,378,777.10 USD | -44,134,994.21 USD | `-6.14%` | -192,446,089.27 USD | `-0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`97.19`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `97.29` | `235.8200` | 22,943.40 USD | 512,741.46 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `97.29` | `2606.7500` | 253,613.31 USD | 766,354.77 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `97.30` | `144.6000` | 14,069.87 USD | 299,185.51 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.30` | `205.5400` | 19,999.25 USD | 319,184.76 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.30` | `250.0000` | 24,325.00 USD | 343,509.76 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.30` | `146.4600` | 14,250.12 USD | 357,759.88 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `97.30` | `106.4600` | 10,358.13 USD | 368,118.01 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `97.30` | `1250.6300` | 121,680.05 USD | 489,798.06 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `97.31` | `0.1200` | 11.68 USD | 152,487.49 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.31` | `1051.6600` | 102,341.24 USD | 254,828.73 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.31` | `1.9700` | 191.71 USD | 255,020.44 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.31` | `154.6800` | 15,052.07 USD | 270,072.50 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.31` | `144.5900` | 14,070.05 USD | 284,142.55 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.31` | `10.0000` | 973.09 USD | 285,115.64 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.32` | `195.7900` | 19,055.07 USD | 132,380.49 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `97.32` | `47.1000` | 4,583.82 USD | 136,964.31 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.32` | `0.5100` | 49.63 USD | 137,013.94 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.32` | `145.8800` | 14,196.75 USD | 151,210.69 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.32` | `13.0000` | 1,265.12 USD | 152,475.81 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `97.33` | `10.0000` | 973.35 USD | 96,742.28 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.33` | `415.8100` | 40,471.62 USD | 95,768.93 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `97.33` | `568.1600` | 55,297.31 USD | 55,297.31 USD | `7 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `97.33` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 97.33` | `0.00%` | `-` |
| `BID` | `97.33` | `1164.3900` | 113,325.42 USD | 113,325.42 USD | `5 orders` | `-0.00%` | `-` |
| `ASK` | `97.34` | `90.7800` | 8,836.98 USD | 210,220.64 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.34` | `90.7800` | 8,836.89 USD | 201,383.66 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.34` | `90.7800` | 8,836.80 USD | 192,546.77 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.34` | `90.7800` | 8,836.71 USD | 183,709.98 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.34` | `410.3800` | 39,946.80 USD | 174,873.27 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `97.34` | `187.0800` | 18,210.37 USD | 134,926.47 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `97.34` | `90.7800` | 8,836.43 USD | 116,716.10 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.34` | `90.7800` | 8,836.34 USD | 107,879.67 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.34` | `23.6400` | 2,301.05 USD | 99,043.32 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.35` | `299.9200` | 29,198.11 USD | 332,186.15 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.35` | `198.5100` | 19,325.35 USD | 302,988.04 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.35` | `246.6600` | 24,012.60 USD | 283,662.70 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `97.35` | `90.7600` | 8,835.49 USD | 259,650.10 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.35` | `136.9800` | 13,334.87 USD | 250,814.61 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.35` | `90.7600` | 8,835.30 USD | 237,479.75 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.35` | `98.4800` | 9,586.73 USD | 228,644.44 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.35` | `90.7800` | 8,837.07 USD | 219,057.71 USD | `1 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:47:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0x5b5d...c060` | `SHORT` | 67,364,937.22 USD | `696,120.13` | `94.33` | `96.79` | `335.09` | -1,696,671.00 USD | `-2.52%` | `7X Cross` |
| `20` | `0x9c6a...a4ed` | `LONG` | 53,249,588.57 USD | `550,087.69` | `80.86` | `96.79` | `68.19` | 8,770,602.18 USD | `+16.47%` | `20X Cross` |
| `51` | `0xb83d...6e36` | `SHORT` | 25,117,096.44 USD | `259,300.02` | `91.42` | `96.79` | `626.77` | -1,411,963.42 USD | `-5.62%` | `5X Cross` |
| `80` | `0x3dc9...54b0` | `SHORT` | 21,297,998.39 USD | `220,000.19` | `105.90` | `96.79` | `176.06` | 2,001,108.88 USD | `+9.40%` | `20X Cross` |
| `111` | `0x9c89...600e` | `LONG` | 18,341,885.36 USD | `189,472.50` | `115.21` | `96.79` | `35.05` | -3,487,129.90 USD | `-19.01%` | `20X Cross` |
| `117` | `0x4a20...3c26` | `LONG` | 17,417,880.00 USD | `180,000.00` | `106.43` | `96.79` | `69.71` | -1,740,398.71 USD | `-9.99%` | `20X Cross` |
| `153` | `0xecb6...2b00` | `SHORT` | 13,298,081.56 USD | `137,388.23` | `101.37` | `96.79` | `289.89` | 628,569.39 USD | `+4.73%` | `20X Cross` |
| `224` | `0xb581...6f4f` | `LONG` | 9,677,000.00 USD | `100,000.00` | `112.81` | `96.79` | `0.000000` | -1,603,709.14 USD | `-16.57%` | `3X Cross` |
| `225` | `0xc63a...a3cd` | `LONG` | 9,676,500.00 USD | `100,000.00` | `112.22` | `96.79` | `0.000000` | -1,545,608.97 USD | `-15.97%` | `20X Cross` |
| `290` | `0x645b...87b8` | `SHORT` | 8,022,117.09 USD | `82,879.96` | `103.90` | `96.79` | `361.37` | 589,353.14 USD | `+7.35%` | `20X Cross` |
| `295` | `0xdb3a...cf3b` | `LONG` | 7,928,572.67 USD | `81,851.78` | `106.04` | `96.79` | `45.10` | -751,174.19 USD | `-9.47%` | `4X Cross` |
| `304` | `0x7a5a...0394` | `SHORT` | 7,777,989.27 USD | `80,357.77` | `99.29` | `96.79` | `122.56` | 200,418.01 USD | `+2.58%` | `10X Cross` |
| `312` | `0xe927...98ef` | `LONG` | 7,551,102.00 USD | `78,000.00` | `96.34` | `96.79` | `38.45` | 36,960.52 USD | `+0.49%` | `3X Cross` |
| `325` | `0xca49...53c8` | `SHORT` | 7,154,324.56 USD | `73,943.45` | `110.70` | `96.79` | `302.68` | 1,031,297.70 USD | `+14.42%` | `20X Cross` |
| `327` | `0x8ae4...3d60` | `LONG` | 6,998,938.55 USD | `72,180.05` | `111.72` | `96.79` | `12.06` | -1,065,221.69 USD | `-15.22%` | `10X Cross` |
| `332` | `0xa0b7...6165` | `SHORT` | 6,875,110.61 USD | `71,044.42` | `107.87` | `96.79` | `190.91` | 788,356.59 USD | `+11.47%` | `2X Cross` |
| `348` | `0xf517...c032` | `SHORT` | 6,565,570.64 USD | `67,778.53` | `84.64` | `96.79` | `221.82` | -828,539.48 USD | `-12.62%` | `20X Cross` |
| `401` | `0x7fda...17d1` | `SHORT` | 5,500,282.83 USD | `56,825.80` | `100.55` | `96.79` | `774.07` | 213,483.94 USD | `+3.88%` | `20X Cross` |
| `466` | `0x7e23...5a5a` | `LONG` | 4,702,263.52 USD | `48,564.56` | `105.17` | `96.79` | `57.00` | -405,305.64 USD | `-8.62%` | `5X Isolated` |
| `566` | `0xf899...88db` | `SHORT` | 3,940,247.14 USD | `40,716.81` | `88.40` | `96.79` | `117.52` | -340,974.27 USD | `-8.65%` | `20X Cross` |
| `583` | `0x2e2b...2fab` | `LONG` | 3,872,360.00 USD | `40,000.00` | `119.55` | `96.79` | `59.48` | -909,675.64 USD | `-23.49%` | `10X Cross` |
| `615` | `0x9c16...4a6f` | `SHORT` | 3,657,342.52 USD | `37,796.13` | `90.79` | `96.79` | `118.51` | -225,991.80 USD | `-6.18%` | `20X Cross` |
| `636` | `0x27b8...12fc` | `LONG` | 3,493,062.58 USD | `36,085.73` | `110.86` | `96.79` | `24.12` | -507,282.68 USD | `-14.52%` | `10X Cross` |
| `652` | `0x3440...32c5` | `SHORT` | 3,404,200.77 USD | `35,170.27` | `95.02` | `96.79` | `163.32` | -62,277.72 USD | `-1.83%` | `20X Cross` |
| `669` | `0xa61c...66b9` | `LONG` | 3,330,617.46 USD | `34,410.76` | `102.78` | `96.79` | `0.000000` | -206,134.88 USD | `-6.19%` | `5X Cross` |
| `697` | `0x9946...0852` | `SHORT` | 3,196,110.56 USD | `33,020.40` | `112.11` | `96.79` | `147.02` | 505,755.60 USD | `+15.82%` | `20X Cross` |
| `731` | `0x96a7...79df` | `LONG` | 3,097,280.00 USD | `32,000.00` | `74.39` | `96.79` | `0.000000` | 716,874.15 USD | `+23.15%` | `20X Cross` |
| `768` | `0xfc27...9d9d` | `SHORT` | 2,951,347.79 USD | `30,491.65` | `100.40` | `96.79` | `710.36` | 109,880.74 USD | `+3.72%` | `20X Cross` |
| `769` | `0x023a...2355` | `SHORT` | 2,947,712.99 USD | `30,462.28` | `101.18` | `96.79` | `268.84` | 134,334.11 USD | `+4.56%` | `20X Cross` |
| `770` | `0xbe19...8bd1` | `SHORT` | 2,946,688.23 USD | `30,451.69` | `97.62` | `96.79` | `762.22` | 25,858.40 USD | `+0.88%` | `3X Cross` |
| `777` | `0x482b...cae4` | `SHORT` | 2,933,024.88 USD | `30,310.49` | `88.03` | `96.79` | `153.09` | -264,776.59 USD | `-9.03%` | `20X Cross` |
| `786` | `0x610b...b613` | `LONG` | 2,868,436.58 USD | `29,634.14` | `101.23` | `96.79` | `70.40` | -131,562.77 USD | `-4.59%` | `3X Isolated` |
| `802` | `0x45d2...4029` | `SHORT` | 2,827,502.52 USD | `29,220.00` | `93.28` | `96.79` | `1583.91` | -101,726.54 USD | `-3.60%` | `20X Cross` |
| `838` | `0xb644...7d51` | `LONG` | 2,691,876.50 USD | `27,810.94` | `100.64` | `96.79` | `84.79` | -107,037.33 USD | `-3.98%` | `20X Cross` |
| `851` | `0x458d...ab3b` | `LONG` | 2,650,597.05 USD | `27,385.03` | `117.17` | `96.79` | `81.08` | -558,065.46 USD | `-21.05%` | `3X Isolated` |
| `921` | `0x051c...693c` | `LONG` | 2,433,271.56 USD | `25,139.70` | `89.76` | `96.79` | `44.05` | 176,710.23 USD | `+7.26%` | `20X Cross` |
| `955` | `0x638f...f5f0` | `LONG` | 2,322,384.00 USD | `24,000.00` | `136.71` | `96.79` | `51.09` | -958,584.54 USD | `-41.28%` | `20X Cross` |
| `1005` | `0x7178...0854` | `LONG` | 2,182,491.96 USD | `22,545.24` | `110.94` | `96.79` | `39.87` | -318,652.52 USD | `-14.60%` | `10X Cross` |
| `1020` | `0x739c...cfb2` | `LONG` | 2,129,798.00 USD | `22,000.00` | `91.95` | `96.79` | `75.16` | 106,890.69 USD | `+5.02%` | `20X Cross` |
| `1028` | `0x69cc...14fd` | `SHORT` | 2,100,538.36 USD | `21,701.57` | `99.01` | `96.79` | `469.66` | 48,114.39 USD | `+2.29%` | `20X Cross` |
| `1109` | `0x7737...bf66` | `SHORT` | 1,972,606.25 USD | `20,384.06` | `102.94` | `96.79` | `934.94` | 125,735.64 USD | `+6.37%` | `10X Cross` |
| `1138` | `0xea00...a918` | `LONG` | 1,938,376.60 USD | `20,022.69` | `66.09` | `96.79` | `0.000000` | 615,068.00 USD | `+31.73%` | `20X Cross` |
| `1140` | `0x251f...6e5d` | `LONG` | 1,937,360.00 USD | `20,000.00` | `101.15` | `96.79` | `71.26` | -85,737.77 USD | `-4.43%` | `20X Cross` |
| `1143` | `0xbfc7...80b4` | `SHORT` | 1,935,320.00 USD | `20,000.00` | `85.98` | `96.79` | `185.38` | -215,785.50 USD | `-11.15%` | `20X Cross` |
| `1144` | `0x3fc5...c0c1` | `SHORT` | 1,935,320.00 USD | `20,000.00` | `98.28` | `96.79` | `186.37` | 30,239.84 USD | `+1.56%` | `20X Cross` |
| `1162` | `0x936c...bb0f` | `SHORT` | 1,903,321.76 USD | `19,664.04` | `105.57` | `96.79` | `517.75` | 172,640.42 USD | `+9.07%` | `20X Cross` |
| `1174` | `0x7160...d47c` | `LONG` | 1,882,542.40 USD | `19,434.10` | `105.03` | `96.79` | `75.60` | -158,678.89 USD | `-8.43%` | `20X Cross` |
| `1204` | `0xe097...d0fe` | `LONG` | 1,838,218.73 USD | `18,995.75` | `109.71` | `96.79` | `0.000000` | -245,778.16 USD | `-13.37%` | `20X Cross` |
| `1271` | `0xdf95...7d72` | `SHORT` | 1,722,684.46 USD | `17,802.58` | `104.53` | `96.79` | `2306.62` | 138,272.40 USD | `+8.03%` | `20X Cross` |
| `1279` | `0xe98b...8cd5` | `SHORT` | 1,705,754.77 USD | `17,622.89` | `187.95` | `96.79` | `262.63` | 1,606,465.95 USD | `+94.18%` | `20X Cross` |
| `1308` | `0x5323...b23c` | `LONG` | 1,651,409.52 USD | `17,066.01` | `94.75` | `96.79` | `0.000000` | 34,466.13 USD | `+2.09%` | `5X Cross` |
| `1316` | `0xee2b...d67e` | `LONG` | 1,643,190.29 USD | `16,963.19` | `119.86` | `96.79` | `34.38` | -390,081.35 USD | `-23.74%` | `4X Cross` |
| `1320` | `0x123d...3bff` | `LONG` | 1,637,333.94 USD | `16,920.55` | `89.54` | `96.79` | `0.000000` | 122,340.19 USD | `+7.47%` | `10X Cross` |
| `1353` | `0x7277...0b98` | `SHORT` | 1,598,361.14 USD | `16,513.36` | `100.07` | `96.79` | `182.11` | 54,175.74 USD | `+3.39%` | `20X Cross` |
| `1431` | `0x73d7...8be1` | `LONG` | 1,516,205.95 USD | `15,668.95` | `106.60` | `96.79` | `49.60` | -154,135.02 USD | `-10.17%` | `20X Cross` |
| `1445` | `0xc74a...ab93` | `LONG` | 1,503,529.15 USD | `15,536.82` | `64.06` | `96.79` | `54.89` | 508,300.31 USD | `+33.81%` | `5X Isolated` |
| `1477` | `0xb322...d51f` | `LONG` | 1,453,002.56 USD | `14,999.82` | `102.98` | `96.79` | `44.04` | -91,724.74 USD | `-6.31%` | `20X Cross` |
| `1481` | `0x5f10...d49d` | `LONG` | 1,451,490.00 USD | `15,000.00` | `96.35` | `96.79` | `71.84` | 6,188.84 USD | `+0.43%` | `20X Cross` |
| `1531` | `0xffb2...5ed6` | `LONG` | 1,403,556.92 USD | `14,504.05` | `117.89` | `96.79` | `84.62` | -306,347.79 USD | `-21.83%` | `20X Cross` |
| `1560` | `0x0d6a...ca57` | `LONG` | 1,375,331.58 USD | `14,206.65` | `110.41` | `96.79` | `91.60` | -193,258.78 USD | `-14.05%` | `5X Isolated` |
| `1578` | `0x8d0c...e17b` | `SHORT` | 1,347,187.13 USD | `13,897.41` | `96.42` | `96.79` | `103.56` | -7,203.75 USD | `-0.53%` | `10X Cross` |
| `1666` | `0x2577...4897` | `LONG` | 1,260,844.53 USD | `13,026.33` | `95.59` | `96.79` | `0.000000` | 15,685.38 USD | `+1.24%` | `15X Cross` |
| `1770` | `0x2814...9b08` | `LONG` | 1,167,151.37 USD | `12,061.71` | `96.37` | `96.79` | `93.93` | 4,812.62 USD | `+0.41%` | `20X Isolated` |
| `1845` | `0x7808...6e70` | `SHORT` | 1,111,719.89 USD | `11,488.27` | `97.15` | `96.79` | `152.00` | 4,342.33 USD | `+0.39%` | `10X Cross` |
| `1858` | `0x2482...0e55` | `LONG` | 1,100,771.92 USD | `11,363.98` | `122.03` | `96.79` | `88.84` | -285,930.00 USD | `-25.98%` | `20X Isolated` |
| `1883` | `0x45db...86eb` | `LONG` | 1,073,869.50 USD | `11,100.00` | `110.69` | `96.79` | `69.16` | -154,812.40 USD | `-14.42%` | `5X Cross` |
| `1914` | `0x1d04...7c43` | `LONG` | 1,046,275.64 USD | `10,811.76` | `111.55` | `96.79` | `17.22` | -159,785.85 USD | `-15.27%` | `6X Cross` |
| `1939` | `0x34e6...8d74` | `LONG` | 1,032,593.83 USD | `10,671.15` | `101.19` | `96.79` | `15.56` | -47,180.81 USD | `-4.57%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `102.31` | 26,049.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 26.05K USD at 102.3100 USD [API] | `2026-10-28 23:50:13` |
| `ANNOUNCEMENT` | `INFO` | `102.43` | 21,806.32 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 21.81K USD at 102.4300 USD [API] | `2026-10-29 00:01:28` |
| `ANNOUNCEMENT` | `INFO` | `100.85` | 1,933.29 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.93K USD at 100.8500 USD [API] | `2026-10-29 01:39:01` |
| `ANNOUNCEMENT` | `INFO` | `100.85` | 2,058.35 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.06K USD at 100.8500 USD [API] | `2026-10-29 01:39:01` |
| `ANNOUNCEMENT` | `INFO` | `100.85` | 188.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.19K USD at 100.8500 USD [API] | `2026-10-29 01:39:01` |
| `ANNOUNCEMENT` | `INFO` | `100.85` | 2,396.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.40K USD at 100.8500 USD [API] | `2026-10-29 01:39:01` |
| `ANNOUNCEMENT` | `INFO` | `100.95` | 99,246.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 99.25K USD at 100.9500 USD [API] | `2026-10-29 01:39:20` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 82.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.08K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 1,958.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.96K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 1,258.86 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.26K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 1,062.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.06K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 2,738.62 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.74K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 2,985.75 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.99K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 5,003.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.00K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.87` | 4,019.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.02K USD at 100.8700 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.88` | 4,887.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.89K USD at 100.8800 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.89` | 5,325.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.33K USD at 100.8900 USD [API] | `2026-10-29 01:39:05` |
| `ANNOUNCEMENT` | `INFO` | `100.86` | 5,727.84 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.73K USD at 100.8600 USD [API] | `2026-10-29 01:39:01` |
| `ANNOUNCEMENT` | `INFO` | `98.43` | 64,053.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 64.05K USD at 98.4280 USD [API] | `2026-08-25 12:03:14` |
| `ANNOUNCEMENT` | `INFO` | `100.14` | 66,006.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 66.01K USD at 100.1400 USD [API] | `2026-10-29 01:50:28` |
| `ANNOUNCEMENT` | `INFO` | `100.13` | 20,000.97 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 100.1300 USD [API] | `2026-10-29 01:50:28` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 3,231.72 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.23K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 18.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 20,695.42 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 20.70K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 1,496.86 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.50K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 10.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 12.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 481.66 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.48K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 350.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.35K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 95.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 830.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.83K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 295.54 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.30K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.80` | 41.74 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.04K USD at 112.8000 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 1,640.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 1,128.10 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.13K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 1,128.10 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.13K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 599.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.60K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 33,998.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 34.00K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 7,029.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.03K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 7,173.59 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.17K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 5,967.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.97K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `112.81` | 4,934.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.93K USD at 112.8100 USD [API] | `2026-10-08 12:11:14` |
| `ANNOUNCEMENT` | `INFO` | `124.84` | 4,908.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 4.91K USD at 124.8400 USD [API] | `2026-09-27 08:15:43` |
| `ANNOUNCEMENT` | `INFO` | `124.84` | 1,381.98 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.38K USD at 124.8400 USD [API] | `2026-09-27 08:15:43` |
| `ANNOUNCEMENT` | `INFO` | `124.84` | 2,614.15 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.61K USD at 124.8400 USD [API] | `2026-09-27 08:15:43` |
| `ANNOUNCEMENT` | `INFO` | `99.14` | 19,362.82 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 19.36K USD at 99.1440 USD [API] | `2026-09-01 18:28:02` |
| `ANNOUNCEMENT` | `INFO` | `70.56` | 76,012.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 76.01K USD at 70.5600 USD [API] | `2026-08-01 18:49:57` |
| `ANNOUNCEMENT` | `INFO` | `70.56` | 23,148.24 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 23.15K USD at 70.5610 USD [API] | `2026-08-01 18:49:57` |
| `ANNOUNCEMENT` | `INFO` | `70.56` | 2,288.33 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.29K USD at 70.5620 USD [API] | `2026-08-01 18:49:57` |
| `ANNOUNCEMENT` | `INFO` | `70.56` | 126.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.13K USD at 70.5620 USD [API] | `2026-08-01 18:49:57` |
| `ANNOUNCEMENT` | `INFO` | `70.56` | 1,047.86 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.05K USD at 70.5630 USD [API] | `2026-08-01 18:49:57` |
| `ANNOUNCEMENT` | `INFO` | `70.56` | 25,653.82 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 25.65K USD at 70.5570 USD [API] | `2026-08-01 18:49:55` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 1,169.25 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.17K USD at 74.0500 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0500 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0500 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0500 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0500 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.88 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0500 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 8,835.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 8.84K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 4,010.60 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.01K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 4,010.60 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.01K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,776.91 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.78K USD at 74.0510 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `74.05` | 2,100.86 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.10K USD at 74.0520 USD [API] | `2026-07-24 13:53:52` |
| `ANNOUNCEMENT` | `INFO` | `73.77` | 686.83 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.69K USD at 73.7730 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.77` | 1,229.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.23K USD at 73.7730 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.77` | 60,056.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 60.06K USD at 73.7730 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.77` | 1,328.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.33K USD at 73.7740 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.77` | 56.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.06K USD at 73.7740 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.78` | 30,029.05 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 30.03K USD at 73.7760 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.78` | 1,328.74 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.33K USD at 73.7780 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.78` | 368.89 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.37K USD at 73.7780 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `73.78` | 1,795.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.80K USD at 73.7780 USD [API] | `2026-07-17 13:06:53` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 10,484.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 10.48K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 2,999.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.00K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 4,999.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.00K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 60.20 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.06K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 2,836.69 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.84K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 2,836.69 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.84K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `79.22` | 7,959.52 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 7.96K USD at 79.2150 USD [API] | `2026-07-06 13:04:18` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 28,936.89 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 28.94K USD at 65.3380 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 1,636.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 65.3380 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 13,158.82 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 13.16K USD at 65.3400 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 17,550.32 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 17.55K USD at 65.3400 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 662.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.66K USD at 65.3400 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 998.43 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.00K USD at 65.3420 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 2,670.57 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.67K USD at 65.3430 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 1,103.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.10K USD at 65.3430 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 1,636.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 65.3430 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.34` | 173.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.17K USD at 65.3440 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.35` | 6,895.96 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.90K USD at 65.3460 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.35` | 1,636.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 65.3460 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.35` | 2,015.95 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.02K USD at 65.3470 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.35` | 1,636.36 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 65.3500 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.35` | 1,636.44 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.64K USD at 65.3530 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.36` | 16.99 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 65.3570 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.36` | 12,878.99 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 12.88K USD at 65.3590 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.36` | 20.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 65.3600 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.36` | 12.42 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 65.3600 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `65.36` | 408.52 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.41K USD at 65.3630 USD [API] | `2026-06-24 17:20:52` |
| `ANNOUNCEMENT` | `INFO` | `69.90` | 68,665.13 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 68.67K USD at 69.8960 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.90` | 20.27 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 69.8960 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.90` | 1,498.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.50K USD at 69.8990 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.90` | 20.27 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 69.9000 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.91` | 699.06 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.70K USD at 69.9060 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.91` | 20.27 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 69.9060 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.91` | 999.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.00K USD at 69.9080 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.91` | 426.44 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.43K USD at 69.9090 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.91` | 666.24 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.67K USD at 69.9100 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.91` | 270.56 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.27K USD at 69.9110 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.92` | 1,396.90 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.40K USD at 69.9150 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.92` | 999.83 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.00K USD at 69.9180 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.92` | 426.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.43K USD at 69.9180 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.92` | 3,126.21 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.13K USD at 69.9220 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.92` | 5,335.75 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 5.34K USD at 69.9220 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.93` | 399.31 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.40K USD at 69.9310 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `69.93` | 101.40 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.10K USD at 69.9310 USD [API] | `2026-06-23 06:21:15` |
| `ANNOUNCEMENT` | `INFO` | `99.88` | 2,402.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.40K USD at 99.8820 USD [API] | `2026-10-29 01:49:11` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`99.59` (Vol: 4,500,000.00 USD, Dist: `+2.65%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--4.99%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 4,700,000.00 USD, Dist: `+4.23%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--5.01%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 4,700,000.00 USD, Dist: `+4.23%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--5.01%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+7.23%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--5.06%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.45` | 18,080.00 USD | 125,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.15` | 1,720.00 USD | 125,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 734.06 USD | 125,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 125,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.75` | 604.86 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.85` | 325.89 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 699.85 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.25` | 403.75 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,830.00 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 900.90 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 11,030.00 USD | 125,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.15` | 5,110.00 USD | 125,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 132.98 USD | 125,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.75` | 112.61 USD | 125,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.85` | 1,140.00 USD | 125,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 22,260.00 USD | 125,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 243.31 USD | 125,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 2,550.00 USD | 125,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 849,820.00 USD | 125,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 242.65 USD | 124,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 242.79 USD | 124,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.95` | 8,840.00 USD | 124,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 1,120.00 USD | 124,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 1,210.00 USD | 124,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.35` | 249.34 USD | 124,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.45` | 1,180.00 USD | 124,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 4,590.00 USD | 124,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,550.00 USD | 124,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 124,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 22,290.00 USD | 124,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 3,210.00 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 152,940.00 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 102.60 USD | 124,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.75` | 80,250.00 USD | 124,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.85` | 2,070.00 USD | 124,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 10,840.00 USD | 124,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.25` | 166.22 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 686.25 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 152.08 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 79,480.00 USD | 124,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 414.78 USD | 124,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 124,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 1,220.00 USD | 124,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 124,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 1,150.00 USD | 124,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 2,610.00 USD | 124,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 15,220.00 USD | 124,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 12,390.00 USD | 124,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 201,280.00 USD | 124,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 394.14 USD | 124,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 4,460.00 USD | 124,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 47,340.00 USD | 124,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.25` | 4,210.00 USD | 123,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 1,340.00 USD | 123,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 123,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 46,430.00 USD | 123,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 753.32 USD | 123,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 621.00 USD | 123,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 47,200.00 USD | 123,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 7,370.00 USD | 123,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 3,920.00 USD | 123,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 2,390.00 USD | 123,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 15,990.00 USD | 123,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.55` | 4,430.00 USD | 123,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 1,010.00 USD | 123,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 5,540.00 USD | 123,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 6,590.00 USD | 123,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.45` | 179.96 USD | 123,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 570,810.00 USD | 123,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 496.46 USD | 123,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 768.63 USD | 123,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 228.77 USD | 123,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 74,420.00 USD | 123,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 290.78 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 6,640,000.00 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 17,810.00 USD | 116,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.35` | 1,720.00 USD | 116,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 39,390.00 USD | 116,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.55` | 2,840.00 USD | 116,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 7,060.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 557.94 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 14,170.00 USD | 116,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 116,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 6,560.00 USD | 116,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,410.00 USD | 116,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,410.00 USD | 116,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 247.39 USD | 116,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 4,870.00 USD | 116,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 913.51 USD | 116,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 116,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 38,980.00 USD | 116,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 371.50 USD | 116,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 106,530.00 USD | 116,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 20,860.00 USD | 116,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 1,160.00 USD | 116,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 53,040.00 USD | 116,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 45,300.00 USD | 116,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 4,160.00 USD | 116,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 331,760.00 USD | 116,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 192,160.00 USD | 115,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 115,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 151.89 USD | 112,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 736.64 USD | 112,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 112,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 18,420.00 USD | 112,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,960.00 USD | 112,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 890,790.00 USD | 112,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 10,620.00 USD | 111,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,720.00 USD | 111,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 111,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 111,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.95` | 1,740.00 USD | 111,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 3,460.00 USD | 111,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 5,270.00 USD | 111,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 111,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 2,020.00 USD | 111,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 12,130.00 USD | 111,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 5,160.00 USD | 111,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 52,030.00 USD | 111,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 2,770.00 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 142.10 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 17,840.00 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 1,070.00 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 592.13 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 130.88 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 588.26 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,020.00 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 50,900.00 USD | 111,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 470.12 USD | 111,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 10,060.00 USD | 111,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 2,680.00 USD | 111,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 198.62 USD | 111,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 1,040.00 USD | 111,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 8,230.00 USD | 111,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 106.88 USD | 111,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,360.00 USD | 111,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 5,480.00 USD | 111,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,090,000.00 USD | 111,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 25,640.00 USD | 110,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 2,390.00 USD | 110,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 2,000.00 USD | 110,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 1,970.00 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 69,090.00 USD | 110,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 110,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 11,220.00 USD | 110,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 672,280.00 USD | 110,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,110.00 USD | 109,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 2,380.00 USD | 109,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 16,440.00 USD | 109,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 17,870.00 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 729.13 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 109,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 794.74 USD | 109,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 6,510.00 USD | 109,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 3,700,000.00 USD | 109,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 105,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 39,460.00 USD | 105,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 45,920.00 USD | 105,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 8,630.00 USD | 105,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 319.09 USD | 105,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 105,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 105,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 27,460.00 USD | 105,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 281.83 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 4,620.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 334.39 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 229.90 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 824.95 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 522.76 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 374.00 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 1,480.00 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,090.00 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 641.24 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 3,220.00 USD | 105,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 130.21 USD | 105,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 977.00 USD | 105,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 10,330.00 USD | 105,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 102,470.00 USD | 105,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 58,470.00 USD | 105,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 2,930.00 USD | 105,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 17,510.00 USD | 105,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 6,300.00 USD | 105,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,550.00 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 5,280.00 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 3,910.00 USD | 105,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,530.00 USD | 105,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 9,850.00 USD | 105,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 1,860.00 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 14,680.00 USD | 105,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 8,240.00 USD | 105,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,400.00 USD | 105,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,010.00 USD | 105,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 105,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 1,060.00 USD | 105,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 15,300.00 USD | 105,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 889.42 USD | 105,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 13,570.00 USD | 105,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 100.50 USD | 105,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 512.96 USD | 105,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 20,850.00 USD | 105,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,450.00 USD | 105,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 8,390.00 USD | 105,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 7,860.00 USD | 105,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 2,410.00 USD | 105,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 3,820.00 USD | 105,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 1,220,000.00 USD | 105,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 995.78 USD | 104,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,470.00 USD | 104,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 19,710.00 USD | 103,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 6,570.00 USD | 103,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 2,680.00 USD | 103,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 3,410.00 USD | 103,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 1,950.00 USD | 103,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 10,640.00 USD | 103,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 7,110.00 USD | 103,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 140,560.00 USD | 103,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 7,490.00 USD | 103,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 103,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 43,020.00 USD | 103,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 473,690.00 USD | 103,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 31,030.00 USD | 103,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 99,630.00 USD | 103,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 13,810.00 USD | 103,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,030.00 USD | 103,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 157,790.00 USD | 103,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 13,210.00 USD | 102,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 3,120.00 USD | 102,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,770.00 USD | 102,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 102,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 2,210.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 17,520.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 3,820.00 USD | 102,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,560.00 USD | 102,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,400.00 USD | 102,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,000.00 USD | 102,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 43,790.00 USD | 102,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 717.84 USD | 102,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 102,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,990.00 USD | 102,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 58,760.00 USD | 102,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 1,430.00 USD | 102,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 102,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 19,150.00 USD | 102,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 31,690.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 753.04 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 60,580.00 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 2,070.00 USD | 102,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 24,000.00 USD | 102,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 858,930.00 USD | 102,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 101,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 552.70 USD | 101,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 101,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 101,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 5,620.00 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 5,200.00 USD | 101,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 152,840.00 USD | 101,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 91,560.00 USD | 101,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 3,370.00 USD | 101,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,050.00 USD | 101,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 5,640.00 USD | 101,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 50,650.00 USD | 101,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 13,300.00 USD | 101,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 13,200.00 USD | 101,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 13,140.00 USD | 101,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 4,730.00 USD | 101,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,190.00 USD | 101,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 101,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 1,670.00 USD | 101,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 14,320.00 USD | 101,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 2,770,000.00 USD | 101,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 29,170.00 USD | 98,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 26,940.00 USD | 98,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 8,330.00 USD | 98,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 98,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 35,760.00 USD | 98,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 13,030.00 USD | 98,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 30,770.00 USD | 98,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 22,650.00 USD | 98,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 1,730.00 USD | 98,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 15,270.00 USD | 98,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 155,370.00 USD | 98,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 9,870.00 USD | 97,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 4,670.00 USD | 97,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 7,040.00 USD | 97,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 2,970.00 USD | 97,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 2,350,000.00 USD | 97,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 1,900.00 USD | 95,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 95,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 16,160.00 USD | 95,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 22,080.00 USD | 95,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 4,760.00 USD | 95,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 376.83 USD | 95,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,320.00 USD | 95,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,230.00 USD | 95,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 8,610.00 USD | 95,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 3,640.00 USD | 95,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 20,570.00 USD | 95,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 3,830.00 USD | 95,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 37,750.00 USD | 95,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 43,240.00 USD | 95,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 35,140.00 USD | 95,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 499.47 USD | 95,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 32,290.00 USD | 95,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 69,320.00 USD | 95,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 2,760.00 USD | 95,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 95,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,300.00 USD | 95,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,860.00 USD | 95,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 56,410.00 USD | 95,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 21,180.00 USD | 95,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 5,900.00 USD | 95,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 5,260.00 USD | 95,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 10,280.00 USD | 95,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 26,450.00 USD | 95,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 18,770.00 USD | 95,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 20,520.00 USD | 95,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 16,580.00 USD | 95,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 5,500.00 USD | 95,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 8,720.00 USD | 95,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 9,000.00 USD | 95,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 45,390.00 USD | 95,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 8,720.00 USD | 94,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 16,180.00 USD | 94,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 22,050.00 USD | 94,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 227,580.00 USD | 94,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,230.00 USD | 94,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 20,770.00 USD | 94,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,460.00 USD | 94,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 2,990.00 USD | 94,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 44,200.00 USD | 94,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 89,390.00 USD | 94,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 18,290.00 USD | 94,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.35` | 63,290.00 USD | 94,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 291.24 USD | 94,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 94,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 575.40 USD | 94,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 32,540.00 USD | 94,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 40,980.00 USD | 94,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 2,280.00 USD | 94,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.05` | 434.90 USD | 94,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 101,470.00 USD | 94,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 4,320.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 8,960.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 2,220.00 USD | 94,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 94,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 32,680.00 USD | 94,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 250,430.00 USD | 94,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 17,690.00 USD | 93,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 15,120.00 USD | 93,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 55,730.00 USD | 93,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 3,130.00 USD | 93,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 50,820.00 USD | 93,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 59,910.00 USD | 93,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,070.00 USD | 93,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 1,300.00 USD | 93,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 62,250.00 USD | 93,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 4,840.00 USD | 93,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 14,930.00 USD | 93,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 13,850.00 USD | 93,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 13,450.00 USD | 93,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 59,860.00 USD | 93,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 13,170.00 USD | 93,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 5,930.00 USD | 93,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 1,910.00 USD | 93,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 1,770.00 USD | 93,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 37,010.00 USD | 93,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 358,860.00 USD | 93,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 248.83 USD | 93,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 1,230.00 USD | 93,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 21,630.00 USD | 93,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 53,490.00 USD | 93,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 141,830.00 USD | 93,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 11,530.00 USD | 92,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 4,670.00 USD | 92,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 10,300.00 USD | 92,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 92,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 25,920.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 3,530.00 USD | 55,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 443,120.00 USD | 55,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 5,370.00 USD | 54,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 44,390.00 USD | 54,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 149,630.00 USD | 54,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 3,240.00 USD | 54,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 49,010.00 USD | 54,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 795,950.00 USD | 54,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 10,190.00 USD | 53,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 225,210.00 USD | 53,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 12,520,000.00 USD | 53,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 26,200.00 USD | 41,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 5,150.00 USD | 41,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 1,610,000.00 USD | 41,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 24,140.00 USD | 39,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 39,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 682.99 USD | 39,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 3,670.00 USD | 39,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 72,890.00 USD | 39,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,140,000.00 USD | 39,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 115,160.00 USD | 37,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 10,270.00 USD | 37,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 42,480.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 10,000.00 USD | 37,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 17,910.00 USD | 37,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 4,430.00 USD | 37,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 59,200.00 USD | 37,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 70,840.00 USD | 36,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 2,040.00 USD | 36,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 1,120,000.00 USD | 36,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 31,640.00 USD | 35,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 76,050.00 USD | 35,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 894.91 USD | 35,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 28,130.00 USD | 35,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 13,960.00 USD | 35,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 12,710.00 USD | 35,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 21,780.00 USD | 35,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 131,360.00 USD | 35,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 269,280.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 28,860.00 USD | 35,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 1,840.00 USD | 35,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 16,340.00 USD | 35,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 33,720.00 USD | 35,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,940.00 USD | 35,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 186,830.00 USD | 35,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 7,580.00 USD | 34,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 8,160.00 USD | 34,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 24,730.00 USD | 34,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 28,470.00 USD | 34,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 3,330.00 USD | 34,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 13,390.00 USD | 34,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 15,210.00 USD | 34,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 38,120.00 USD | 34,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 84,720.00 USD | 34,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 15,410.00 USD | 34,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,420.00 USD | 34,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 34,460.00 USD | 34,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,430.00 USD | 34,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 50,970.00 USD | 34,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 37,750.00 USD | 34,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 26,740.00 USD | 34,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 6,260.00 USD | 34,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 102,100.00 USD | 34,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 1,690,000.00 USD | 34,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 31,860.00 USD | 32,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 1,190,000.00 USD | 32,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 41,500.00 USD | 31,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 3,150.00 USD | 31,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 1,470,000.00 USD | 31,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 15,140.00 USD | 29,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 275,550.00 USD | 29,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 28,520.00 USD | 29,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 141,300.00 USD | 29,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 50,260.00 USD | 29,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 7,370.00 USD | 29,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 27,920.00 USD | 29,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 9,680.00 USD | 29,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 5,990.00 USD | 29,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 5,790.00 USD | 29,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 31,790.00 USD | 29,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 23,200.00 USD | 29,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 40,570.00 USD | 29,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 57,460.00 USD | 29,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 5,060.00 USD | 29,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 176,890.00 USD | 29,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 28,980.00 USD | 29,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 172,800.00 USD | 28,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 82,020.00 USD | 28,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 27,870.00 USD | 28,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 49,120.00 USD | 28,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 49,970.00 USD | 28,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 13,260.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.65` | 29,320.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 186,270.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 193,010.00 USD | 28,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 8,370.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 27,710.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 63,910.00 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 39,070.00 USD | 28,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 51,020.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 26,080.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,740.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,860.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 60,550.00 USD | 27,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 63,030.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 1,740.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 16,760.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 608,630.00 USD | 27,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 47,670.00 USD | 27,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 30,350.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 16,910.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 645.15 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 15,720.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 15,190.00 USD | 27,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 42,690.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 5,600.00 USD | 27,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 37,880.00 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 40,470.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 59,920.00 USD | 26,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 104,600.00 USD | 26,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 10,320.00 USD | 26,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 11,150.00 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 47,310.00 USD | 26,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 19,370.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 458,770.00 USD | 26,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 26,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 26,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 132,270.00 USD | 23,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 23,460.00 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 60,780.00 USD | 23,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 70,230.00 USD | 23,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 65,060.00 USD | 23,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 15,400.00 USD | 23,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 23,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 44,330.00 USD | 23,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 68,660.00 USD | 23,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,440.00 USD | 23,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 805,410.00 USD | 23,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 24,700.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 159,740.00 USD | 22,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 209,090.00 USD | 22,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 30,900.00 USD | 22,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 104,620.00 USD | 22,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 1,150,000.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 49,530.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 19,450.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 129,140.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 5,900.00 USD | 20,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 156,460.00 USD | 20,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 321,100.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.45` | 30,830.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 14,120.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.65` | 225,710.00 USD | 20,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 98,260.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.85` | 203,740.00 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 30,940.00 USD | 19,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 125,390.00 USD | 19,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 66,120.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.25` | 67,160.00 USD | 19,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,630.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.45` | 85,770.00 USD | 19,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 4,610.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 102,150.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 2,410,000.00 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 94,840.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 1,250,000.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 14,870.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 5,940.00 USD | 15,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.25` | 571,570.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,000.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.45` | 46,070.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 23,080.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.65` | 42,860.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 9,830.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.85` | 85,650.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 738,410.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 256,680.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 60,740.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.25` | 44,050.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.30` | 101,970,000.00 USD | 101,970,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.35` | 182,490.00 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.45` | 108,330.00 USD | 13,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.50` | 101,810,000.00 USD | 101,810,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.55` | 28,140.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.60` | 80,880,000.00 USD | 80,880,000.00 USD | 0.00 USD | 306,270.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.65` | 225,720.00 USD | 13,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 37,350.00 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.80` | 80,570,000.00 USD | 80,570,000.00 USD | 0.00 USD | 69,010.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 78,930.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.90` | 101,810,000.00 USD | 101,810,000.00 USD | 226,670.00 USD | 138,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 154,360.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.00` | 80,490,000.00 USD | 80,490,000.00 USD | 156,460.00 USD | 243,720.00 USD | 107,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 53,710.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.10` | 101,440,000.00 USD | 101,440,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 68,830.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.20` | 79,980,000.00 USD | 79,980,000.00 USD | 54,890.00 USD | 79,810.00 USD | 221,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 50,440.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.30` | 101,440,000.00 USD | 101,440,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 76,460.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.40` | 79,630,000.00 USD | 79,630,000.00 USD | 8,750.00 USD | 95,800.00 USD | 40,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 149,740.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.50` | 100,950,000.00 USD | 100,950,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 202,390.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.60` | 79,480,000.00 USD | 79,480,000.00 USD | 10,160.00 USD | 50,950.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 176,180.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.70` | 100,900,000.00 USD | 100,900,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 28,310.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.80` | 79,420,000.00 USD | 79,420,000.00 USD | 22,290.00 USD | 112,630.00 USD | 716,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 69,500.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.90` | 100,190,000.00 USD | 100,190,000.00 USD | 0.00 USD | 295,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 6,600.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.00` | 78,570,000.00 USD | 78,570,000.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 153,760.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 22,010.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.25` | 49,740.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 109,890.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.45` | 71,730.00 USD | 11,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 248,900.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.60` | 78,080,000.00 USD | 78,080,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.65` | 82,420.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.70` | 99,890,000.00 USD | 99,890,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 157,190.00 USD | 10,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 78,070,000.00 USD | 78,070,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,090,000.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.90` | 99,670,000.00 USD | 99,670,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 44,030.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 77,180,000.00 USD | 77,180,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 41,130.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.10` | 99,650,000.00 USD | 99,650,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 142,610.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 76,950,000.00 USD | 76,950,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 51,890.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.30` | 98,430,000.00 USD | 98,430,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 29,850.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 76,680,000.00 USD | 76,680,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 450,050.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.50` | 98,400,000.00 USD | 98,400,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 52,760.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 76,310,000.00 USD | 76,310,000.00 USD | 557,950.00 USD | 163,120.00 USD | 317,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 91,070.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.70` | 97,610,000.00 USD | 97,610,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 125,990.00 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 75,270,000.00 USD | 75,270,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 50,640.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.90` | 96,190,000.00 USD | 96,190,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 78,510.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 74,160,000.00 USD | 74,160,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 26,110.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.10` | 94,390,000.00 USD | 94,390,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 65,220.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 72,810,000.00 USD | 72,810,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 28,440.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.30` | 92,020,000.00 USD | 92,020,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 54,540.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 71,490,000.00 USD | 71,490,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 41,980.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.50` | 89,940,000.00 USD | 89,940,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 20,810.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 70,130,000.00 USD | 70,130,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 133,420.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.70` | 87,260,000.00 USD | 87,260,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 87,870.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 68,990,000.00 USD | 68,990,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 973,350.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.90` | 84,810,000.00 USD | 84,810,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 16,500.00 USD | 7,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 68,780,000.00 USD | 68,780,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 435,550.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.10` | 82,430,000.00 USD | 82,430,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 296,830.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 68,590,000.00 USD | 68,590,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 25,100.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.30` | 80,520,000.00 USD | 80,520,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 52,180.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 68,560,000.00 USD | 68,560,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 375,760.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.50` | 78,020,000.00 USD | 78,020,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,240,000.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 68,390,000.00 USD | 68,390,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,460,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.70` | 75,100,000.00 USD | 75,100,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 334,680.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 68,270,000.00 USD | 68,270,000.00 USD | 250,490.00 USD | 103,030.00 USD | 525,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 248,720.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.90` | 73,470,000.00 USD | 73,470,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 86,480.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 67,390,000.00 USD | 67,390,000.00 USD | 38,300.00 USD | 274,720.00 USD | 87,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 116,220.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.10` | 71,060,000.00 USD | 71,060,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 167,540.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 66,990,000.00 USD | 66,990,000.00 USD | 63,310.00 USD | 149,590.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 233,470.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.30` | 69,360,000.00 USD | 69,360,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 339,860.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 66,740,000.00 USD | 66,740,000.00 USD | 117,460.00 USD | 824,620.00 USD | 877,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 109,370.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.50` | 67,000,000.00 USD | 67,000,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.60` | 64,920,000.00 USD | 64,920,000.00 USD | 377,000.00 USD | 345,060.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 174,900.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.70` | 65,240,000.00 USD | 65,240,000.00 USD | 718,400.00 USD | 377,890.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 5,170.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 64,190,000.00 USD | 64,190,000.00 USD | 26,180.00 USD | 866,290.00 USD | 435,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 11,850.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.90` | 64,070,000.00 USD | 64,070,000.00 USD | 0.00 USD | 729,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 3,780.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.00` | 62,860,000.00 USD | 62,860,000.00 USD | 276,830.00 USD | 262,440.00 USD | 552,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 25,790.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.10` | 63,340,000.00 USD | 63,340,000.00 USD | 31,020.00 USD | 630,650.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 4,950.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.20` | 61,770,000.00 USD | 61,770,000.00 USD | 32,310.00 USD | 398,190.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 38,840.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.30` | 61,680,000.00 USD | 61,680,000.00 USD | 145,070.00 USD | 66,280.00 USD | 468,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 13,820.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.40` | 61,240,000.00 USD | 61,240,000.00 USD | 57,590.00 USD | 433,830.00 USD | 141,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 13,880.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.50` | 61,000,000.00 USD | 61,000,000.00 USD | 93,960.00 USD | 1,260,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 29,480.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.60` | 60,610,000.00 USD | 60,610,000.00 USD | 64,480.00 USD | 472,950.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 2,050.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.70` | 58,200,000.00 USD | 58,200,000.00 USD | 270,240.00 USD | 954,120.00 USD | 120,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 9,050.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.80` | 58,280,000.00 USD | 58,280,000.00 USD | 63,080.00 USD | 1,320,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.90` | 56,850,000.00 USD | 56,850,000.00 USD | 168,420.00 USD | 56,340.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,130,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.00` | 55,130,000.00 USD | 55,130,000.00 USD | 60,590.00 USD | 86,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 9,740.00 USD | 137,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.10` | 56,610,000.00 USD | 56,610,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 45,570.00 USD | 127,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.20` | 54,980,000.00 USD | 54,980,000.00 USD | 0.00 USD | 691,260.00 USD | 702,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 1,860.00 USD | 82,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.30` | 55,030,000.00 USD | 55,030,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 51,340.00 USD | 80,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.40` | 53,590,000.00 USD | 53,590,000.00 USD | 46,210.00 USD | 1,130,000.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 2,430.00 USD | 28,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.50` | 54,310,000.00 USD | 54,310,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 24,250.00 USD | 26,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 52,390,000.00 USD | 52,390,000.00 USD | 827,670.00 USD | 605,060.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.70` | 53,220,000.00 USD | 53,220,000.00 USD | 1,690,000.00 USD | 656,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `94.80` | 48,880,000.00 USD | 48,880,000.00 USD | 762,670.00 USD | 3,070,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 136.58 USD | 2,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.90` | 50,870,000.00 USD | 50,870,000.00 USD | 1,100,000.00 USD | 3,570,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.00` | 43,330,000.00 USD | 43,330,000.00 USD | 1,070,000.00 USD | 1,240,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.10` | 46,200,000.00 USD | 46,200,000.00 USD | 198,380.00 USD | 1,270,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.20` | 39,900,000.00 USD | 39,900,000.00 USD | 99,290.00 USD | 4,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.30` | 41,960,000.00 USD | 41,960,000.00 USD | 678,330.00 USD | 445,310.00 USD | 838,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.40` | 34,140,000.00 USD | 34,140,000.00 USD | 378,280.00 USD | 1,650,000.00 USD | 294,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.50` | 40,000,000.00 USD | 40,000,000.00 USD | 1,200,000.00 USD | 3,810,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.60` | 31,820,000.00 USD | 31,820,000.00 USD | 2,740,000.00 USD | 2,900,000.00 USD | 4,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.70` | 32,110,000.00 USD | 32,110,000.00 USD | 4,060,000.00 USD | 4,060,000.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.80` | 21,610,000.00 USD | 21,610,000.00 USD | 2,310,000.00 USD | 1,930,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.90` | 23,990,000.00 USD | 23,990,000.00 USD | 2,130,000.00 USD | 877,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.95` | 990.20 USD | 2,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.00` | 14,460,000.00 USD | 14,460,000.00 USD | 2,070,000.00 USD | 1,880,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.10` | 20,980,000.00 USD | 20,980,000.00 USD | 3,460,000.00 USD | 2,050,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.15` | 432.68 USD | 1,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.20` | 8,970,000.00 USD | 8,970,000.00 USD | 1,350,000.00 USD | 847,400.00 USD | 498,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.30` | 10,950,000.00 USD | 10,950,000.00 USD | 1,030,000.00 USD | 2,320,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.40` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 2,050,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.50` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.55` | 2,880.00 USD | 2,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.60` | 747,550.00 USD | 747,550.00 USD | 0.00 USD | 747,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `96.80` | 4,300.00 USD | 4,300.00 USD | 0.00 USD | 4,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.85` | 676.01 USD | 676.01 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.00` | 808,780.00 USD | 808,780.00 USD | 804,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.05` | 203,110.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.20` | 1,100,000.00 USD | 1,100,000.00 USD | 286,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.25` | 48,730.00 USD | 254,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.30` | 5,720,000.00 USD | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.35` | 1,580.00 USD | 256,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.40` | 1,790,000.00 USD | 1,790,000.00 USD | 690,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.45` | 850.74 USD | 257,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `97.50` | 12,360,000.00 USD | 12,360,000.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.55` | 45,780.00 USD | 302,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.60` | 9,330,000.00 USD | 9,330,000.00 USD | 5,180,000.00 USD | 1,410,000.00 USD | 956,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.70` | 22,260,000.00 USD | 22,260,000.00 USD | 7,320,000.00 USD | 2,580,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.75` | 166.17 USD | 303,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.80` | 17,230,000.00 USD | 17,230,000.00 USD | 5,710,000.00 USD | 724,660.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.90` | 48,690,000.00 USD | 48,690,000.00 USD | 11,920,000.00 USD | 6,740,000.00 USD | 7,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.95` | 746.38 USD | 303,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.00` | 32,370,000.00 USD | 32,370,000.00 USD | 6,540,000.00 USD | 2,650,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.05` | 487.31 USD | 304,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.10` | 83,590,000.00 USD | 83,590,000.00 USD | 9,820,000.00 USD | 9,540,000.00 USD | 15,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.15` | 4,780.00 USD | 309,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.20` | 43,310,000.00 USD | 43,310,000.00 USD | 4,120,000.00 USD | 3,690,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.25` | 4,050.00 USD | 313,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.30` | 100,170,000.00 USD | 100,170,000.00 USD | 43,030.00 USD | 6,830,000.00 USD | 9,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.35` | 151.46 USD | 313,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.40` | 56,830,000.00 USD | 56,830,000.00 USD | 2,330,000.00 USD | 2,640,000.00 USD | 8,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.50` | 106,830,000.00 USD | 106,830,000.00 USD | 1,130,000.00 USD | 5,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 319,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.60` | 66,250,000.00 USD | 66,250,000.00 USD | 52,360.00 USD | 3,510,000.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 328,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.70` | 108,170,000.00 USD | 108,170,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.75` | 1,150.00 USD | 330,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.80` | 73,890,000.00 USD | 73,890,000.00 USD | 553,660.00 USD | 3,030,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.90` | 110,710,000.00 USD | 110,710,000.00 USD | 57,310.00 USD | 1,040,000.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 331,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.00` | 75,260,000.00 USD | 75,260,000.00 USD | 64,620.00 USD | 1,100,000.00 USD | 202,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 23,060.00 USD | 354,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.10` | 111,850,000.00 USD | 111,850,000.00 USD | 179,190.00 USD | 124,230.00 USD | 838,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 128,100.00 USD | 482,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 80,110,000.00 USD | 80,110,000.00 USD | 115,180.00 USD | 867,660.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 3,900.00 USD | 486,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.30` | 116,980,000.00 USD | 116,980,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 29,310.00 USD | 515,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 84,960,000.00 USD | 84,960,000.00 USD | 2,860,000.00 USD | 509,170.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 2,120.00 USD | 517,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.50` | 120,720,000.00 USD | 120,720,000.00 USD | 2,240,000.00 USD | 1,480,000.00 USD | 16,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 60,330.00 USD | 577,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 98,960,000.00 USD | 98,960,000.00 USD | 1,520,000.00 USD | 5,710,000.00 USD | 6,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 79,990.00 USD | 657,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.70` | 122,730,000.00 USD | 122,730,000.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 1,040.00 USD | 658,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 111,860,000.00 USD | 111,860,000.00 USD | 2,250,000.00 USD | 3,870,000.00 USD | 6,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 3,040.00 USD | 662,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.90` | 129,880,000.00 USD | 129,880,000.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 1,250.00 USD | 663,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.00` | 117,340,000.00 USD | 117,340,000.00 USD | 2,080,000.00 USD | 1,770,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 1,550.00 USD | 664,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.10` | 133,270,000.00 USD | 133,270,000.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 11,860.00 USD | 676,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 118,200,000.00 USD | 118,200,000.00 USD | 23,110.00 USD | 838,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 7,170.00 USD | 683,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.30` | 136,120,000.00 USD | 136,120,000.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.40` | 121,990,000.00 USD | 121,990,000.00 USD | 377,000.00 USD | 771,420.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.50` | 143,320,000.00 USD | 143,320,000.00 USD | 2,550,000.00 USD | 337,850.00 USD | 4,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 969.30 USD | 684,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 132,120,000.00 USD | 132,120,000.00 USD | 1,990,000.00 USD | 1,650,000.00 USD | 6,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.70` | 145,350,000.00 USD | 145,350,000.00 USD | 133,340.00 USD | 1,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 11,950.00 USD | 696,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.80` | 137,280,000.00 USD | 137,280,000.00 USD | 1,780,000.00 USD | 1,750,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 10,090.00 USD | 706,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.90` | 158,450,000.00 USD | 158,450,000.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.00` | 148,680,000.00 USD | 148,680,000.00 USD | 7,810,000.00 USD | 2,650,000.00 USD | 935,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 320.33 USD | 707,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.10` | 168,220,000.00 USD | 168,220,000.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 23,800.00 USD | 730,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.20` | 164,990,000.00 USD | 164,990,000.00 USD | 5,230,000.00 USD | 6,870,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 731,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.30` | 188,780,000.00 USD | 188,780,000.00 USD | 7,310,000.00 USD | 4,280,000.00 USD | 8,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.35` | 1,330.00 USD | 733,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.40` | 174,900,000.00 USD | 174,900,000.00 USD | 3,450,000.00 USD | 2,420,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 733,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.50` | 204,050,000.00 USD | 204,050,000.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 3,440.00 USD | 736,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 195,710,000.00 USD | 195,710,000.00 USD | 4,700,000.00 USD | 3,450,000.00 USD | 12,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 2,640.00 USD | 739,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.70` | 213,400,000.00 USD | 213,400,000.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.80` | 202,000,000.00 USD | 202,000,000.00 USD | 483,810.00 USD | 381,190.00 USD | 5,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.90` | 221,400,000.00 USD | 221,400,000.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 206,400,000.00 USD | 206,400,000.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 8,550.00 USD | 747,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.10` | 226,050,000.00 USD | 226,050,000.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.15` | 120.54 USD | 747,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.20` | 213,230,000.00 USD | 213,230,000.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 749,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.30` | 232,100,000.00 USD | 232,100,000.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.35` | 9,980.00 USD | 759,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.40` | 217,810,000.00 USD | 217,810,000.00 USD | 1,430,000.00 USD | 579,100.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.45` | 826.77 USD | 759,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.50` | 235,750,000.00 USD | 235,750,000.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.60` | 220,450,000.00 USD | 220,450,000.00 USD | 978,360.00 USD | 625,050.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,500.00 USD | 761,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.70` | 236,520,000.00 USD | 236,520,000.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 944.27 USD | 762,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.80` | 224,910,000.00 USD | 224,910,000.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.90` | 257,810,000.00 USD | 257,810,000.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 3,080.00 USD | 765,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 230,170,000.00 USD | 230,170,000.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 3,380.00 USD | 768,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.10` | 264,020,000.00 USD | 264,020,000.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 779,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 233,770,000.00 USD | 233,770,000.00 USD | 585,300.00 USD | 1,180,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 1,310.00 USD | 781,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.30` | 281,590,000.00 USD | 281,590,000.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 2,820.00 USD | 783,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 238,710,000.00 USD | 238,710,000.00 USD | 2,140,000.00 USD | 1,620,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 787,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.50` | 304,000,000.00 USD | 304,000,000.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.55` | 1,440,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 249,270,000.00 USD | 249,270,000.00 USD | 3,310,000.00 USD | 1,240,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 870.66 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.70` | 316,220,000.00 USD | 316,220,000.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,580.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 256,070,000.00 USD | 256,070,000.00 USD | 2,280,000.00 USD | 2,510,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 14,290.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.90` | 334,250,000.00 USD | 334,250,000.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.00` | 265,620,000.00 USD | 265,620,000.00 USD | 3,550,000.00 USD | 2,790,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 545.22 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.10` | 362,980,000.00 USD | 362,980,000.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,060.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 271,350,000.00 USD | 271,350,000.00 USD | 2,070,000.00 USD | 1,830,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.30` | 384,360,000.00 USD | 384,360,000.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.40` | 277,250,000.00 USD | 277,250,000.00 USD | 2,370,000.00 USD | 1,780,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 10,760.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.50` | 396,360,000.00 USD | 396,360,000.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 11,230.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 282,170,000.00 USD | 282,170,000.00 USD | 1,430,000.00 USD | 963,940.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 521.16 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.70` | 416,360,000.00 USD | 416,360,000.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 285,970,000.00 USD | 285,970,000.00 USD | 948,860.00 USD | 905,680.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.90` | 436,970,000.00 USD | 436,970,000.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 125,660.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 287,160,000.00 USD | 287,160,000.00 USD | 487,580.00 USD | 351,350.00 USD | 350,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.10` | 450,180,000.00 USD | 450,180,000.00 USD | 5,580,000.00 USD | 4,800,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.15` | 746.57 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.20` | 288,420,000.00 USD | 288,420,000.00 USD | 237,100.00 USD | 4,110.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 1,040.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.30` | 455,170,000.00 USD | 455,170,000.00 USD | 2,740,000.00 USD | 1,820,000.00 USD | 428,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 1,050.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 288,590,000.00 USD | 288,590,000.00 USD | 84,970.00 USD | 88,270.00 USD | 769.33 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 527,250.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.50` | 474,680,000.00 USD | 474,680,000.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 289,170,000.00 USD | 289,170,000.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.70` | 488,850,000.00 USD | 488,850,000.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 289,920,000.00 USD | 289,920,000.00 USD | 132,310.00 USD | 591,910.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 91,370.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.90` | 498,740,000.00 USD | 498,740,000.00 USD | 3,680,000.00 USD | 1,870,000.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 291,040,000.00 USD | 291,040,000.00 USD | 377,210.00 USD | 525,540.00 USD | 226,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.10` | 510,880,000.00 USD | 510,880,000.00 USD | 6,090,000.00 USD | 3,080,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.20` | 292,380,000.00 USD | 292,380,000.00 USD | 620,980.00 USD | 344,210.00 USD | 367,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.30` | 520,860,000.00 USD | 520,860,000.00 USD | 4,770,000.00 USD | 2,990,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 252,220.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.40` | 293,290,000.00 USD | 293,290,000.00 USD | 233,950.00 USD | 449,760.00 USD | 233,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 32,940.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.50` | 526,100,000.00 USD | 526,100,000.00 USD | 1,700,000.00 USD | 1,650,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.60` | 295,110,000.00 USD | 295,110,000.00 USD | 445,430.00 USD | 321,480.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 11,590.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.70` | 535,720,000.00 USD | 535,720,000.00 USD | 2,280,000.00 USD | 2,870,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.75` | 249.79 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.80` | 296,260,000.00 USD | 296,260,000.00 USD | 319,360.00 USD | 179,630.00 USD | 649,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 479,130.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.90` | 541,550,000.00 USD | 541,550,000.00 USD | 1,220,000.00 USD | 1,150,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 398,430.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 296,630,000.00 USD | 296,630,000.00 USD | 98,730.00 USD | 169,460.00 USD | 95,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 20,180.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.10` | 545,650,000.00 USD | 545,650,000.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.20` | 297,110,000.00 USD | 297,110,000.00 USD | 0.00 USD | 49,040.00 USD | 436,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 34,950.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.30` | 546,100,000.00 USD | 546,100,000.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 297,720,000.00 USD | 297,720,000.00 USD | 22,290.00 USD | 63,590.00 USD | 523,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.50` | 547,090,000.00 USD | 547,090,000.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 298,210,000.00 USD | 298,210,000.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.65` | 1,820.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.70` | 548,060,000.00 USD | 548,060,000.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,340.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.90` | 548,230,000.00 USD | 548,230,000.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.10` | 548,830,000.00 USD | 548,830,000.00 USD | 249,450.00 USD | 347,250.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.30` | 550,990,000.00 USD | 550,990,000.00 USD | 964,640.00 USD | 578,980.00 USD | 612,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,660.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.45` | 111,070.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.50` | 552,020,000.00 USD | 552,020,000.00 USD | 867,380.00 USD | 155,140.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.55` | 17,460.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.70` | 554,260,000.00 USD | 554,260,000.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 150,780.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.90` | 556,310,000.00 USD | 556,310,000.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.05` | 318.43 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.10` | 557,390,000.00 USD | 557,390,000.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.30` | 558,550,000.00 USD | 558,550,000.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.35` | 10,490.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 342.58 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.50` | 558,790,000.00 USD | 558,790,000.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.55` | 356.04 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 44,880.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.70` | 559,980,000.00 USD | 559,980,000.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.75` | 3,240.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 653.61 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.90` | 561,780,000.00 USD | 561,780,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.95` | 3,510.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.05` | 12,220.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.10` | 564,150,000.00 USD | 564,150,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.30` | 566,230,000.00 USD | 566,230,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.35` | 158.90 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,580.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.50` | 566,710,000.00 USD | 566,710,000.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 257,120.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.70` | 568,910,000.00 USD | 568,910,000.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.75` | 575.90 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 1,090.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `110.90` | 571,360,000.00 USD | 571,360,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.95` | 5,040.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.10` | 573,740,000.00 USD | 573,740,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.30` | 575,640,000.00 USD | 575,640,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.50` | 578,150,000.00 USD | 578,150,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.70` | 579,290,000.00 USD | 579,290,000.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.90` | 581,060,000.00 USD | 581,060,000.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.10` | 582,690,000.00 USD | 582,690,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.15` | 291.59 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.30` | 585,110,000.00 USD | 585,110,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.35` | 1,910.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.50` | 586,420,000.00 USD | 586,420,000.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.70` | 586,940,000.00 USD | 586,940,000.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.90` | 588,430,000.00 USD | 588,430,000.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.10` | 589,830,000.00 USD | 589,830,000.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 1,350.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.30` | 590,100,000.00 USD | 590,100,000.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.45` | 2,160.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.50` | 590,160,000.00 USD | 590,160,000.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.65` | 105,510.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.70` | 590,550,000.00 USD | 590,550,000.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.75` | 303.71 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.90` | 590,600,000.00 USD | 590,600,000.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.95` | 22,000.00 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 22,870.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.10` | 590,660,000.00 USD | 590,660,000.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `114.30` | 590,890,000.00 USD | 590,890,000.00 USD | 93,960.00 USD | 135,190.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `114.40` | 591,220,000.00 USD | 591,220,000.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,310.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.75` | 1,470.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 5,850.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 879,040.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 57,760.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 1,720.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 89,950.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.25` | 16,600.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 11,840.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.45` | 4,780,000.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 4,300.00 USD | 12,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 10,360.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 353.85 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.05` | 28,100.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.35` | 4,470,000.00 USD | 16,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 1,110.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.05` | 1,440.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.15` | 2,350.00 USD | 16,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 16,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 621,120.00 USD | 17,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.45` | 861,240.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 27,920.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 13,070.00 USD | 18,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.05` | 95,660.00 USD | 18,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 3,440.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 145.74 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 316.20 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 18,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.65` | 16,190.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 2,330.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 18,030.00 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.85` | 245.70 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.95` | 10,810,000.00 USD | 29,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.05` | 33,370.00 USD | 29,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,850.00 USD | 29,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 8,630.00 USD | 29,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.55` | 124,410.00 USD | 29,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 29,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 29,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 29,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 114.40 USD | 29,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 29,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 29,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 18,200.00 USD | 29,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 2,800.00 USD | 29,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 46,540.00 USD | 29,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 29,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 590.87 USD | 29,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 36,630.00 USD | 29,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 851.91 USD | 29,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 4,600.00 USD | 29,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 29,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 1,250.00 USD | 29,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 8,420.00 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 188.26 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 117.60 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.55` | 318.91 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 31,130.00 USD | 29,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.75` | 6,420.00 USD | 29,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 4,260.00 USD | 29,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 29,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.25` | 162.88 USD | 29,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 16,190.00 USD | 29,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 720.51 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 266,410.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 30,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.15` | 6,740.00 USD | 30,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 30,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 30,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 42,690.00 USD | 30,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 55,570.00 USD | 30,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,780.00 USD | 30,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 699,390.00 USD | 31,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 1,130.00 USD | 31,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 36,480.00 USD | 31,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 31,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.95` | 68,950.00 USD | 31,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 13,200.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 145.99 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 3,570.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 503,960.00 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.35` | 855.09 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 31,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 5,430.00 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 106.88 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 11,940.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 79,190.00 USD | 31,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 103.78 USD | 31,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 31,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 31,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 31,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 2,110.00 USD | 31,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 31,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 32,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.55` | 168,190.00 USD | 32,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.05` | 8,490.00 USD | 32,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.65` | 48,790.00 USD | 32,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.75` | 8,270.00 USD | 32,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 32,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 15,120.00 USD | 32,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 32,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 32,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 34,240.00 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 809.19 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.25` | 488.61 USD | 32,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.55` | 4,120.00 USD | 32,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.65` | 40,630.00 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.75` | 698.39 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.85` | 647.90 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 19,770.00 USD | 32,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 44,270.00 USD | 32,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 47,280.00 USD | 32,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 9,620.00 USD | 32,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 32,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.05` | 13,180.00 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 253.80 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 8,990.00 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 1,820.00 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 32,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 12,850.00 USD | 32,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 702.75 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 8,780.00 USD | 32,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.75` | 627.75 USD | 32,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 69,260.00 USD | 32,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 3,080.00 USD | 32,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 32,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 32,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 1,080,000.00 USD | 33,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 111.90 USD | 33,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 2,460.00 USD | 33,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.85` | 866,960.00 USD | 34,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.35` | 23,090.00 USD | 34,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 34,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.55` | 2,440.00 USD | 34,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 34,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,330.00 USD | 34,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 34,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.75` | 596,560.00 USD | 35,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.85` | 89,820.00 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 35,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.35` | 23,340.00 USD | 35,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 35,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 2,360.00 USD | 35,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 28,990.00 USD | 35,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.55` | 1,340.00 USD | 35,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 8,050.00 USD | 35,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 104,150.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 2,770.00 USD | 35,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,480.00 USD | 35,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.45` | 4,970,000.00 USD | 40,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.75` | 1,400.00 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.85` | 547.75 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,070.00 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 2,290.00 USD | 41,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 41,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 41,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 41,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 2,290.00 USD | 41,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 443,190.00 USD | 41,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.75` | 277.77 USD | 41,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 300.14 USD | 41,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.95` | 108,230.00 USD | 41,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 102.22 USD | 41,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 78,690.00 USD | 41,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 163.29 USD | 41,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 864,710.00 USD | 42,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 21,850.00 USD | 42,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 93,700.00 USD | 42,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 160,350.00 USD | 43,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.35` | 1,390,000.00 USD | 44,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 44,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 44,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 123,320.00 USD | 44,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 44,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.85` | 346.96 USD | 44,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.95` | 19,710.00 USD | 44,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.05` | 29,300.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 3,180.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.35` | 2,780.00 USD | 44,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 44,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.55` | 1,140.00 USD | 44,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 44,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 1,110,000.00 USD | 45,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 200.97 USD | 45,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 331,180.00 USD | 46,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 4,070.00 USD | 46,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 423,220.00 USD | 46,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 46,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 45,670.00 USD | 46,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 20,200.00 USD | 46,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 46,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 46,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.05` | 223.37 USD | 46,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 46,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 4,680,000.00 USD | 51,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,600.00 USD | 51,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.55` | 465.20 USD | 51,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 1,240.00 USD | 51,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.85` | 1,500.00 USD | 51,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 51,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.65` | 118.29 USD | 51,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.05` | 308.98 USD | 51,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 7,810.00 USD | 51,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.25` | 27,390.00 USD | 51,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 51,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 4,900.00 USD | 51,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.85` | 327.82 USD | 51,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.05` | 18,390.00 USD | 51,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 159,270.00 USD | 51,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.35` | 2,950.00 USD | 51,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 51,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 51,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.95` | 298.53 USD | 51,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.05` | 237,080.00 USD | 51,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.45` | 80,030.00 USD | 51,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.55` | 1,820,000.00 USD | 53,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 474,780.00 USD | 54,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.25` | 40,450.00 USD | 54,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.35` | 101,490.00 USD | 54,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 54,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 39,490.00 USD | 54,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.05` | 497.76 USD | 54,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 55,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 55,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.45` | 320,900.00 USD | 55,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.75` | 227,000.00 USD | 55,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 55,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 55,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.45` | 106,980.00 USD | 55,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 55,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 55,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.65` | 5,720,000.00 USD | 61,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.95` | 1,350.00 USD | 61,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.65` | 1,040.00 USD | 61,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 61,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 223,350.00 USD | 61,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.55` | 6,590.00 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.25` | 17,080.00 USD | 61,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.85` | 620.28 USD | 61,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 996.90 USD | 61,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 61,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.55` | 149.90 USD | 61,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 68,630.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.85` | 3,440.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 23,890.00 USD | 61,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 122.68 USD | 61,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 61,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 62,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.85` | 3,260.00 USD | 62,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.65` | 180,130.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.45` | 279.54 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.85` | 1,180.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.05` | 20,480.00 USD | 62,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 62,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.95` | 28,000.00 USD | 62,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.55` | 204.79 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 62,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 324,200.00 USD | 63,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 63,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 63,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.85` | 38,470,000.00 USD | 101,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.25` | 203,090.00 USD | 101,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 119.31 USD | 101,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 653.79 USD | 101,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.95` | 1,300.00 USD | 101,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.15` | 105,690.00 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.45` | 36,930.00 USD | 102,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.05` | 25,600.00 USD | 102,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.25` | 709.00 USD | 102,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.45` | 266,180.00 USD | 102,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.55` | 2,810.00 USD | 102,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 637.76 USD | 102,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.75` | 3,680.00 USD | 102,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 102,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.15` | 2,940,000.00 USD | 105,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.25` | 2,060.00 USD | 105,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.55` | 142,840.00 USD | 105,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.95` | 1,040,000.00 USD | 106,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.15` | 338.59 USD | 106,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.65` | 4,490.00 USD | 106,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.75` | 154.59 USD | 106,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.05` | 50,020.00 USD | 106,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.45` | 116,590.00 USD | 106,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 3,970.00 USD | 106,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.65` | 3,610,000.00 USD | 110,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.75` | 9,490.00 USD | 110,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.15` | 18,120.00 USD | 110,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 1,620.00 USD | 110,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 5,140.00 USD | 110,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.55` | 73,020.00 USD | 110,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.35` | 3,670,000.00 USD | 114,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 114,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 114,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.05` | 797.57 USD | 114,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 8,410.00 USD | 114,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 114,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 12,160.00 USD | 114,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 137.38 USD | 114,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.75` | 390.07 USD | 114,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.85` | 247.18 USD | 114,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.95` | 53,420.00 USD | 114,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.75` | 2,800.00 USD | 114,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 114,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.95` | 4,110.00 USD | 114,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.35` | 1,010.00 USD | 114,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.55` | 232.56 USD | 114,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 114,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.15` | 29,130.00 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.45` | 256.29 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 2,270.00 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 114,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 114,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 114,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 118.08 USD | 114,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 128,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.15` | 382,300.00 USD | 128,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.25` | 2,510.00 USD | 128,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.45` | 62,820.00 USD | 128,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.75` | 5,430.00 USD | 128,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 128,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.75` | 192.75 USD | 128,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 128,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.35` | 9,380.00 USD | 128,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 125,590,000.00 USD | 0.00 USD | 18,080.00 USD | `-79.92%` | `929.70` |
| `Live` | `Long` | `20.15` | 125,570,000.00 USD | 0.00 USD | 1,720.00 USD | `-79.20%` | `85.12` |
| `Live` | `Long` | `20.25` | 125,570,000.00 USD | 0.00 USD | 734.06 USD | `-79.10%` | `36.25` |
| `Live` | `Long` | `20.55` | 125,570,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.79%` | `233.31` |
| `Live` | `Long` | `20.75` | 125,560,000.00 USD | 0.00 USD | 604.86 USD | `-78.58%` | `29.15` |
| `Live` | `Long` | `20.85` | 125,560,000.00 USD | 0.00 USD | 325.89 USD | `-78.48%` | `15.63` |
| `Live` | `Long` | `21.15` | 125,560,000.00 USD | 0.00 USD | 699.85 USD | `-78.17%` | `33.09` |
| `Live` | `Long` | `21.25` | 125,560,000.00 USD | 0.00 USD | 403.75 USD | `-78.07%` | `19.00` |
| `Live` | `Long` | `21.35` | 125,560,000.00 USD | 0.00 USD | 1,830.00 USD | `-77.96%` | `85.69` |
| `Live` | `Long` | `21.45` | 125,560,000.00 USD | 0.00 USD | 900.90 USD | `-77.86%` | `42.00` |
| `Live` | `Long` | `21.75` | 125,560,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.55%` | `212.70` |
| `Live` | `Long` | `22.05` | 125,560,000.00 USD | 0.00 USD | 11,030.00 USD | `-77.24%` | `500.00` |
| `Live` | `Long` | `22.15` | 125,540,000.00 USD | 0.00 USD | 5,110.00 USD | `-77.14%` | `230.92` |
| `Live` | `Long` | `22.35` | 125,540,000.00 USD | 0.00 USD | 132.98 USD | `-76.93%` | `5.95` |
| `Live` | `Long` | `22.75` | 125,540,000.00 USD | 0.00 USD | 112.61 USD | `-76.52%` | `4.95` |
| `Live` | `Long` | `22.85` | 125,540,000.00 USD | 0.00 USD | 1,140.00 USD | `-76.42%` | `50.00` |
| `Live` | `Long` | `22.95` | 125,540,000.00 USD | 0.00 USD | 22,260.00 USD | `-76.31%` | `969.95` |
| `Live` | `Long` | `23.15` | 125,520,000.00 USD | 0.00 USD | 243.31 USD | `-76.11%` | `10.51` |
| `Live` | `Long` | `23.45` | 125,520,000.00 USD | 0.00 USD | 2,550.00 USD | `-75.80%` | `108.86` |
| `Live` | `Long` | `23.55` | 125,510,000.00 USD | 0.00 USD | 849,820.00 USD | `-75.69%` | `36,085.73` |
| `Live` | `Long` | `23.65` | 124,660,000.00 USD | 0.00 USD | 242.65 USD | `-75.59%` | `10.26` |
| `Live` | `Long` | `23.85` | 124,660,000.00 USD | 0.00 USD | 242.79 USD | `-75.38%` | `10.18` |
| `Live` | `Long` | `23.95` | 124,660,000.00 USD | 0.00 USD | 8,840.00 USD | `-75.28%` | `369.00` |
| `Live` | `Long` | `24.05` | 124,650,000.00 USD | 0.00 USD | 1,120.00 USD | `-75.18%` | `46.58` |
| `Live` | `Long` | `24.15` | 124,650,000.00 USD | 0.00 USD | 1,210.00 USD | `-75.07%` | `50.00` |
| `Live` | `Long` | `24.35` | 124,650,000.00 USD | 0.00 USD | 249.34 USD | `-74.87%` | `10.24` |
| `Live` | `Long` | `24.45` | 124,650,000.00 USD | 0.00 USD | 1,180.00 USD | `-74.76%` | `48.08` |
| `Live` | `Long` | `24.85` | 124,650,000.00 USD | 0.00 USD | 4,590.00 USD | `-74.35%` | `184.67` |
| `Live` | `Long` | `25.05` | 124,650,000.00 USD | 0.00 USD | 1,550.00 USD | `-74.14%` | `62.00` |
| `Live` | `Long` | `25.15` | 124,640,000.00 USD | 0.00 USD | 2,010.00 USD | `-74.04%` | `80.00` |
| `Live` | `Long` | `25.45` | 124,640,000.00 USD | 0.00 USD | 22,290.00 USD | `-73.73%` | `875.84` |
| `Live` | `Long` | `25.95` | 124,620,000.00 USD | 0.00 USD | 3,210.00 USD | `-73.22%` | `123.60` |
| `Live` | `Long` | `26.25` | 124,620,000.00 USD | 0.00 USD | 136.24 USD | `-72.91%` | `5.19` |
| `Live` | `Long` | `26.35` | 124,620,000.00 USD | 0.00 USD | 152,940.00 USD | `-72.80%` | `5,804.28` |
| `Live` | `Long` | `26.65` | 124,460,000.00 USD | 0.00 USD | 102.60 USD | `-72.49%` | `3.85` |
| `Live` | `Long` | `26.75` | 124,460,000.00 USD | 0.00 USD | 80,250.00 USD | `-72.39%` | `3,000.00` |
| `Live` | `Long` | `26.85` | 124,380,000.00 USD | 0.00 USD | 2,070.00 USD | `-72.29%` | `77.00` |
| `Live` | `Long` | `26.95` | 124,380,000.00 USD | 0.00 USD | 10,840.00 USD | `-72.18%` | `402.05` |
| `Live` | `Long` | `27.25` | 124,370,000.00 USD | 0.00 USD | 166.22 USD | `-71.87%` | `6.10` |
| `Live` | `Long` | `27.35` | 124,370,000.00 USD | 0.00 USD | 332.30 USD | `-71.77%` | `12.15` |
| `Live` | `Long` | `27.45` | 124,370,000.00 USD | 0.00 USD | 686.25 USD | `-71.67%` | `25.00` |
| `Live` | `Long` | `27.55` | 124,370,000.00 USD | 0.00 USD | 152.08 USD | `-71.56%` | `5.52` |
| `Live` | `Long` | `27.85` | 124,370,000.00 USD | 0.00 USD | 79,480.00 USD | `-71.25%` | `2,854.02` |
| `Live` | `Long` | `27.95` | 124,290,000.00 USD | 0.00 USD | 414.78 USD | `-71.15%` | `14.84` |
| `Live` | `Long` | `28.05` | 124,290,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.05%` | `97.63` |
| `Live` | `Long` | `28.25` | 124,290,000.00 USD | 0.00 USD | 1,220.00 USD | `-70.84%` | `43.06` |
| `Live` | `Long` | `28.35` | 124,280,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.74%` | `218.55` |
| `Live` | `Long` | `28.45` | 124,280,000.00 USD | 0.00 USD | 1,150.00 USD | `-70.64%` | `40.37` |
| `Live` | `Long` | `28.95` | 124,280,000.00 USD | 0.00 USD | 2,610.00 USD | `-70.12%` | `90.00` |
| `Live` | `Long` | `29.05` | 124,270,000.00 USD | 0.00 USD | 15,220.00 USD | `-70.02%` | `523.99` |
| `Live` | `Long` | `29.15` | 124,260,000.00 USD | 0.00 USD | 12,390.00 USD | `-69.91%` | `425.17` |
| `Live` | `Long` | `29.35` | 124,250,000.00 USD | 0.00 USD | 201,280.00 USD | `-69.71%` | `6,857.87` |
| `Live` | `Long` | `29.95` | 124,050,000.00 USD | 0.00 USD | 394.14 USD | `-69.09%` | `13.16` |
| `Live` | `Long` | `30.05` | 124,050,000.00 USD | 0.00 USD | 4,460.00 USD | `-68.98%` | `148.37` |
| `Live` | `Long` | `30.15` | 124,040,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.88%` | `1,570.00` |
| `Live` | `Long` | `30.25` | 123,990,000.00 USD | 0.00 USD | 4,210.00 USD | `-68.78%` | `139.06` |
| `Live` | `Long` | `30.55` | 123,990,000.00 USD | 0.00 USD | 1,340.00 USD | `-68.47%` | `43.76` |
| `Live` | `Long` | `30.65` | 123,990,000.00 USD | 0.00 USD | 233.86 USD | `-68.36%` | `7.63` |
| `Live` | `Long` | `30.85` | 123,990,000.00 USD | 0.00 USD | 46,430.00 USD | `-68.16%` | `1,505.11` |
| `Live` | `Long` | `30.95` | 123,940,000.00 USD | 0.00 USD | 753.32 USD | `-68.05%` | `24.34` |
| `Live` | `Long` | `31.05` | 123,940,000.00 USD | 0.00 USD | 621.00 USD | `-67.95%` | `20.00` |
| `Live` | `Long` | `31.15` | 123,940,000.00 USD | 0.00 USD | 47,200.00 USD | `-67.85%` | `1,515.26` |
| `Live` | `Long` | `31.35` | 123,890,000.00 USD | 0.00 USD | 7,370.00 USD | `-67.64%` | `235.00` |
| `Live` | `Long` | `31.45` | 123,890,000.00 USD | 0.00 USD | 3,920.00 USD | `-67.54%` | `124.52` |
| `Live` | `Long` | `31.55` | 123,880,000.00 USD | 0.00 USD | 2,390.00 USD | `-67.44%` | `75.83` |
| `Live` | `Long` | `31.65` | 123,880,000.00 USD | 0.00 USD | 15,990.00 USD | `-67.33%` | `505.14` |
| `Live` | `Long` | `32.55` | 123,860,000.00 USD | 0.00 USD | 4,430.00 USD | `-66.40%` | `136.10` |
| `Live` | `Long` | `32.65` | 123,860,000.00 USD | 0.00 USD | 1,010.00 USD | `-66.30%` | `30.95` |
| `Live` | `Long` | `32.85` | 123,860,000.00 USD | 0.00 USD | 5,540.00 USD | `-66.09%` | `168.50` |
| `Live` | `Long` | `33.25` | 123,850,000.00 USD | 0.00 USD | 6,590.00 USD | `-65.68%` | `198.28` |
| `Live` | `Long` | `33.45` | 123,850,000.00 USD | 0.00 USD | 179.96 USD | `-65.47%` | `5.38` |
| `Live` | `Long` | `33.65` | 123,850,000.00 USD | 0.00 USD | 570,810.00 USD | `-65.27%` | `16,963.19` |
| `Live` | `Long` | `33.75` | 123,270,000.00 USD | 0.00 USD | 496.46 USD | `-65.16%` | `14.71` |
| `Live` | `Long` | `33.95` | 123,270,000.00 USD | 0.00 USD | 768.63 USD | `-64.96%` | `22.64` |
| `Live` | `Long` | `34.35` | 123,270,000.00 USD | 0.00 USD | 228.77 USD | `-64.55%` | `6.66` |
| `Live` | `Long` | `34.55` | 123,270,000.00 USD | 0.00 USD | 74,420.00 USD | `-64.34%` | `2,154.01` |
| `Live` | `Long` | `34.65` | 123,200,000.00 USD | 0.00 USD | 486.14 USD | `-64.24%` | `14.03` |
| `Live` | `Long` | `34.95` | 123,200,000.00 USD | 0.00 USD | 290.78 USD | `-63.93%` | `8.32` |
| `Live` | `Long` | `35.05` | 123,200,000.00 USD | 0.00 USD | 6,640,000.00 USD | `-63.82%` | `189,484.12` |
| `Live` | `Long` | `35.15` | 116,560,000.00 USD | 0.00 USD | 17,810.00 USD | `-63.72%` | `506.61` |
| `Live` | `Long` | `35.35` | 116,540,000.00 USD | 0.00 USD | 1,720.00 USD | `-63.51%` | `48.60` |
| `Live` | `Long` | `35.45` | 116,540,000.00 USD | 0.00 USD | 39,390.00 USD | `-63.41%` | `1,111.14` |
| `Live` | `Long` | `35.55` | 116,500,000.00 USD | 0.00 USD | 2,840.00 USD | `-63.31%` | `80.00` |
| `Live` | `Long` | `35.75` | 116,490,000.00 USD | 0.00 USD | 7,060.00 USD | `-63.10%` | `197.54` |
| `Live` | `Long` | `35.95` | 116,490,000.00 USD | 0.00 USD | 557.94 USD | `-62.89%` | `15.52` |
| `Live` | `Long` | `36.05` | 116,490,000.00 USD | 0.00 USD | 14,170.00 USD | `-62.79%` | `393.00` |
| `Live` | `Long` | `36.15` | 116,470,000.00 USD | 0.00 USD | 531.41 USD | `-62.69%` | `14.70` |
| `Live` | `Long` | `36.25` | 116,470,000.00 USD | 0.00 USD | 6,560.00 USD | `-62.58%` | `180.87` |
| `Live` | `Long` | `36.35` | 116,470,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.48%` | `121.32` |
| `Live` | `Long` | `36.45` | 116,460,000.00 USD | 0.00 USD | 2,410.00 USD | `-62.38%` | `66.24` |
| `Live` | `Long` | `36.65` | 116,460,000.00 USD | 0.00 USD | 247.39 USD | `-62.17%` | `6.75` |
| `Live` | `Long` | `36.75` | 116,460,000.00 USD | 0.00 USD | 4,870.00 USD | `-62.07%` | `132.42` |
| `Live` | `Long` | `36.85` | 116,450,000.00 USD | 0.00 USD | 913.51 USD | `-61.97%` | `24.79` |
| `Live` | `Long` | `36.95` | 116,450,000.00 USD | 0.00 USD | 1,660.00 USD | `-61.86%` | `45.00` |
| `Live` | `Long` | `37.05` | 116,450,000.00 USD | 0.00 USD | 38,980.00 USD | `-61.76%` | `1,052.17` |
| `Live` | `Long` | `37.15` | 116,410,000.00 USD | 0.00 USD | 371.50 USD | `-61.66%` | `10.00` |
| `Live` | `Long` | `37.25` | 116,410,000.00 USD | 0.00 USD | 106,530.00 USD | `-61.55%` | `2,859.94` |
| `Live` | `Long` | `37.35` | 116,310,000.00 USD | 0.00 USD | 20,860.00 USD | `-61.45%` | `558.43` |
| `Live` | `Long` | `37.55` | 116,280,000.00 USD | 0.00 USD | 1,160.00 USD | `-61.24%` | `31.00` |
| `Live` | `Long` | `37.65` | 116,280,000.00 USD | 0.00 USD | 53,040.00 USD | `-61.14%` | `1,408.71` |
| `Live` | `Long` | `37.75` | 116,230,000.00 USD | 0.00 USD | 45,300.00 USD | `-61.04%` | `1,200.00` |
| `Live` | `Long` | `37.95` | 116,190,000.00 USD | 0.00 USD | 4,160.00 USD | `-60.83%` | `109.49` |
| `Live` | `Long` | `38.05` | 116,180,000.00 USD | 0.00 USD | 331,760.00 USD | `-60.73%` | `8,719.08` |
| `Live` | `Long` | `38.35` | 115,850,000.00 USD | 0.00 USD | 192,160.00 USD | `-60.42%` | `5,010.78` |
| `Live` | `Long` | `38.45` | 115,660,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.31%` | `78,017.19` |
| `Live` | `Long` | `38.55` | 112,660,000.00 USD | 0.00 USD | 151.89 USD | `-60.21%` | `3.94` |
| `Live` | `Long` | `38.75` | 112,660,000.00 USD | 0.00 USD | 736.64 USD | `-60.00%` | `19.01` |
| `Live` | `Long` | `38.85` | 112,660,000.00 USD | 0.00 USD | 4,270.00 USD | `-59.90%` | `109.96` |
| `Live` | `Long` | `38.95` | 112,650,000.00 USD | 0.00 USD | 18,420.00 USD | `-59.80%` | `472.98` |
| `Live` | `Long` | `39.05` | 112,630,000.00 USD | 0.00 USD | 50,960.00 USD | `-59.69%` | `1,305.06` |
| `Live` | `Long` | `39.35` | 112,580,000.00 USD | 0.00 USD | 890,790.00 USD | `-59.38%` | `22,637.73` |
| `Live` | `Long` | `39.45` | 111,690,000.00 USD | 0.00 USD | 10,620.00 USD | `-59.28%` | `269.19` |
| `Live` | `Long` | `39.65` | 111,680,000.00 USD | 0.00 USD | 5,720.00 USD | `-59.08%` | `144.25` |
| `Live` | `Long` | `39.75` | 111,680,000.00 USD | 0.00 USD | 159.00 USD | `-58.97%` | `4.00` |
| `Live` | `Long` | `39.85` | 111,680,000.00 USD | 0.00 USD | 1,270.00 USD | `-58.87%` | `31.86` |
| `Live` | `Long` | `39.95` | 111,670,000.00 USD | 0.00 USD | 1,740.00 USD | `-58.77%` | `43.67` |
| `Live` | `Long` | `40.05` | 111,670,000.00 USD | 0.00 USD | 3,460.00 USD | `-58.66%` | `86.41` |
| `Live` | `Long` | `40.15` | 111,670,000.00 USD | 0.00 USD | 5,270.00 USD | `-58.56%` | `131.29` |
| `Live` | `Long` | `40.25` | 111,660,000.00 USD | 0.00 USD | 632.73 USD | `-58.46%` | `15.72` |
| `Live` | `Long` | `40.35` | 111,660,000.00 USD | 0.00 USD | 2,020.00 USD | `-58.35%` | `50.00` |
| `Live` | `Long` | `40.45` | 111,660,000.00 USD | 0.00 USD | 12,130.00 USD | `-58.25%` | `300.00` |
| `Live` | `Long` | `40.55` | 111,650,000.00 USD | 0.00 USD | 5,160.00 USD | `-58.15%` | `127.35` |
| `Live` | `Long` | `40.65` | 111,640,000.00 USD | 0.00 USD | 52,030.00 USD | `-58.04%` | `1,280.00` |
| `Live` | `Long` | `40.85` | 111,590,000.00 USD | 0.00 USD | 2,770.00 USD | `-57.84%` | `67.92` |
| `Live` | `Long` | `40.95` | 111,590,000.00 USD | 0.00 USD | 142.10 USD | `-57.73%` | `3.47` |
| `Live` | `Long` | `41.05` | 111,590,000.00 USD | 0.00 USD | 17,840.00 USD | `-57.63%` | `434.51` |
| `Live` | `Long` | `41.15` | 111,570,000.00 USD | 0.00 USD | 1,070.00 USD | `-57.53%` | `26.08` |
| `Live` | `Long` | `41.25` | 111,570,000.00 USD | 0.00 USD | 368.36 USD | `-57.42%` | `8.93` |
| `Live` | `Long` | `41.35` | 111,570,000.00 USD | 0.00 USD | 592.13 USD | `-57.32%` | `14.32` |
| `Live` | `Long` | `41.55` | 111,570,000.00 USD | 0.00 USD | 130.88 USD | `-57.11%` | `3.15` |
| `Live` | `Long` | `41.65` | 111,570,000.00 USD | 0.00 USD | 770.11 USD | `-57.01%` | `18.49` |
| `Live` | `Long` | `41.75` | 111,570,000.00 USD | 0.00 USD | 588.26 USD | `-56.91%` | `14.09` |
| `Live` | `Long` | `41.85` | 111,570,000.00 USD | 0.00 USD | 1,020.00 USD | `-56.80%` | `24.39` |
| `Live` | `Long` | `41.95` | 111,570,000.00 USD | 0.00 USD | 50,900.00 USD | `-56.70%` | `1,213.34` |
| `Live` | `Long` | `42.05` | 111,520,000.00 USD | 0.00 USD | 470.12 USD | `-56.60%` | `11.18` |
| `Live` | `Long` | `42.15` | 111,520,000.00 USD | 0.00 USD | 10,060.00 USD | `-56.49%` | `238.58` |
| `Live` | `Long` | `42.25` | 111,510,000.00 USD | 0.00 USD | 2,680.00 USD | `-56.39%` | `63.46` |
| `Live` | `Long` | `42.35` | 111,500,000.00 USD | 0.00 USD | 198.62 USD | `-56.29%` | `4.69` |
| `Live` | `Long` | `42.55` | 111,500,000.00 USD | 0.00 USD | 1,040.00 USD | `-56.08%` | `24.53` |
| `Live` | `Long` | `42.65` | 111,500,000.00 USD | 0.00 USD | 8,230.00 USD | `-55.98%` | `193.00` |
| `Live` | `Long` | `42.75` | 111,490,000.00 USD | 0.00 USD | 106.88 USD | `-55.88%` | `2.50` |
| `Live` | `Long` | `42.85` | 111,490,000.00 USD | 0.00 USD | 44,360.00 USD | `-55.77%` | `1,035.19` |
| `Live` | `Long` | `42.95` | 111,450,000.00 USD | 0.00 USD | 5,480.00 USD | `-55.67%` | `127.66` |
| `Live` | `Long` | `43.25` | 111,440,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-55.36%` | `25,164.70` |
| `Live` | `Long` | `43.35` | 110,350,000.00 USD | 0.00 USD | 25,640.00 USD | `-55.26%` | `591.40` |
| `Live` | `Long` | `43.45` | 110,330,000.00 USD | 0.00 USD | 2,390.00 USD | `-55.15%` | `55.07` |
| `Live` | `Long` | `43.65` | 110,330,000.00 USD | 0.00 USD | 2,000.00 USD | `-54.95%` | `45.92` |
| `Live` | `Long` | `43.75` | 110,320,000.00 USD | 0.00 USD | 1,970.00 USD | `-54.84%` | `45.06` |
| `Live` | `Long` | `43.85` | 110,320,000.00 USD | 0.00 USD | 69,090.00 USD | `-54.74%` | `1,575.58` |
| `Live` | `Long` | `43.95` | 110,250,000.00 USD | 0.00 USD | 242.16 USD | `-54.64%` | `5.51` |
| `Live` | `Long` | `44.05` | 110,250,000.00 USD | 0.00 USD | 11,220.00 USD | `-54.53%` | `254.69` |
| `Live` | `Long` | `44.15` | 110,240,000.00 USD | 0.00 USD | 672,280.00 USD | `-54.43%` | `15,227.10` |
| `Live` | `Long` | `44.25` | 109,570,000.00 USD | 0.00 USD | 6,110.00 USD | `-54.33%` | `138.09` |
| `Live` | `Long` | `44.35` | 109,560,000.00 USD | 0.00 USD | 2,380.00 USD | `-54.22%` | `53.68` |
| `Live` | `Long` | `44.45` | 109,560,000.00 USD | 0.00 USD | 16,440.00 USD | `-54.12%` | `369.90` |
| `Live` | `Long` | `44.55` | 109,540,000.00 USD | 0.00 USD | 17,870.00 USD | `-54.02%` | `401.03` |
| `Live` | `Long` | `44.65` | 109,530,000.00 USD | 0.00 USD | 729.13 USD | `-53.91%` | `16.33` |
| `Live` | `Long` | `44.75` | 109,530,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.81%` | `39.98` |
| `Live` | `Long` | `44.85` | 109,520,000.00 USD | 0.00 USD | 794.74 USD | `-53.71%` | `17.72` |
| `Live` | `Long` | `44.95` | 109,520,000.00 USD | 0.00 USD | 6,510.00 USD | `-53.60%` | `144.85` |
| `Live` | `Long` | `45.05` | 109,520,000.00 USD | 0.00 USD | 3,700,000.00 USD | `-53.50%` | `82,065.43` |
| `Live` | `Long` | `45.15` | 105,820,000.00 USD | 0.00 USD | 179.70 USD | `-53.40%` | `3.98` |
| `Live` | `Long` | `45.35` | 105,820,000.00 USD | 0.00 USD | 39,460.00 USD | `-53.19%` | `870.15` |
| `Live` | `Long` | `45.45` | 105,780,000.00 USD | 0.00 USD | 45,920.00 USD | `-53.09%` | `1,010.35` |
| `Live` | `Long` | `45.55` | 105,730,000.00 USD | 0.00 USD | 8,630.00 USD | `-52.99%` | `189.38` |
| `Live` | `Long` | `45.65` | 105,730,000.00 USD | 0.00 USD | 319.09 USD | `-52.88%` | `6.99` |
| `Live` | `Long` | `45.75` | 105,730,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.78%` | `206.46` |
| `Live` | `Long` | `45.85` | 105,720,000.00 USD | 0.00 USD | 458.50 USD | `-52.68%` | `10.00` |
| `Live` | `Long` | `45.95` | 105,720,000.00 USD | 0.00 USD | 27,460.00 USD | `-52.57%` | `597.64` |
| `Live` | `Long` | `46.05` | 105,690,000.00 USD | 0.00 USD | 281.83 USD | `-52.47%` | `6.12` |
| `Live` | `Long` | `46.15` | 105,690,000.00 USD | 0.00 USD | 4,620.00 USD | `-52.37%` | `100.00` |
| `Live` | `Long` | `46.25` | 105,680,000.00 USD | 0.00 USD | 334.39 USD | `-52.26%` | `7.23` |
| `Live` | `Long` | `46.35` | 105,680,000.00 USD | 0.00 USD | 229.90 USD | `-52.16%` | `4.96` |
| `Live` | `Long` | `46.45` | 105,680,000.00 USD | 0.00 USD | 824.95 USD | `-52.06%` | `17.76` |
| `Live` | `Long` | `46.55` | 105,680,000.00 USD | 0.00 USD | 522.76 USD | `-51.95%` | `11.23` |
| `Live` | `Long` | `46.65` | 105,680,000.00 USD | 0.00 USD | 542.07 USD | `-51.85%` | `11.62` |
| `Live` | `Long` | `46.75` | 105,680,000.00 USD | 0.00 USD | 374.00 USD | `-51.75%` | `8.00` |
| `Live` | `Long` | `46.85` | 105,680,000.00 USD | 0.00 USD | 1,480.00 USD | `-51.64%` | `31.61` |
| `Live` | `Long` | `46.95` | 105,680,000.00 USD | 0.00 USD | 2,090.00 USD | `-51.54%` | `44.48` |
| `Live` | `Long` | `47.15` | 105,680,000.00 USD | 0.00 USD | 641.24 USD | `-51.33%` | `13.60` |
| `Live` | `Long` | `47.25` | 105,680,000.00 USD | 0.00 USD | 3,220.00 USD | `-51.23%` | `68.21` |
| `Live` | `Long` | `47.35` | 105,670,000.00 USD | 0.00 USD | 130.21 USD | `-51.13%` | `2.75` |
| `Live` | `Long` | `47.45` | 105,670,000.00 USD | 0.00 USD | 977.00 USD | `-51.02%` | `20.59` |
| `Live` | `Long` | `47.55` | 105,670,000.00 USD | 0.00 USD | 10,330.00 USD | `-50.92%` | `217.28` |
| `Live` | `Long` | `47.65` | 105,660,000.00 USD | 0.00 USD | 102,470.00 USD | `-50.82%` | `2,150.48` |
| `Live` | `Long` | `47.75` | 105,560,000.00 USD | 0.00 USD | 58,470.00 USD | `-50.71%` | `1,224.41` |
| `Live` | `Long` | `47.95` | 105,500,000.00 USD | 0.00 USD | 2,930.00 USD | `-50.51%` | `61.09` |
| `Live` | `Long` | `48.05` | 105,500,000.00 USD | 0.00 USD | 17,510.00 USD | `-50.41%` | `364.39` |
| `Live` | `Long` | `48.15` | 105,480,000.00 USD | 0.00 USD | 6,300.00 USD | `-50.30%` | `130.93` |
| `Live` | `Long` | `48.25` | 105,470,000.00 USD | 0.00 USD | 2,550.00 USD | `-50.20%` | `52.82` |
| `Live` | `Long` | `48.35` | 105,470,000.00 USD | 0.00 USD | 5,280.00 USD | `-50.10%` | `109.21` |
| `Live` | `Long` | `48.45` | 105,470,000.00 USD | 0.00 USD | 3,910.00 USD | `-49.99%` | `80.67` |
| `Live` | `Long` | `48.55` | 105,460,000.00 USD | 0.00 USD | 97,530.00 USD | `-49.89%` | `2,008.83` |
| `Live` | `Long` | `48.65` | 105,360,000.00 USD | 0.00 USD | 9,850.00 USD | `-49.79%` | `202.42` |
| `Live` | `Long` | `48.75` | 105,350,000.00 USD | 0.00 USD | 1,860.00 USD | `-49.68%` | `38.17` |
| `Live` | `Long` | `48.85` | 105,350,000.00 USD | 0.00 USD | 14,680.00 USD | `-49.58%` | `300.45` |
| `Live` | `Long` | `48.95` | 105,340,000.00 USD | 0.00 USD | 8,240.00 USD | `-49.48%` | `168.30` |
| `Live` | `Long` | `49.05` | 105,330,000.00 USD | 0.00 USD | 1,400.00 USD | `-49.37%` | `28.61` |
| `Live` | `Long` | `49.15` | 105,330,000.00 USD | 0.00 USD | 5,010.00 USD | `-49.27%` | `102.01` |
| `Live` | `Long` | `49.25` | 105,320,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.17%` | `430.30` |
| `Live` | `Long` | `49.35` | 105,300,000.00 USD | 0.00 USD | 1,060.00 USD | `-49.06%` | `21.50` |
| `Live` | `Long` | `49.45` | 105,300,000.00 USD | 0.00 USD | 15,300.00 USD | `-48.96%` | `309.37` |
| `Live` | `Long` | `49.55` | 105,290,000.00 USD | 0.00 USD | 889.42 USD | `-48.86%` | `17.95` |
| `Live` | `Long` | `49.65` | 105,290,000.00 USD | 0.00 USD | 13,570.00 USD | `-48.75%` | `273.34` |
| `Live` | `Long` | `49.75` | 105,270,000.00 USD | 0.00 USD | 100.50 USD | `-48.65%` | `2.02` |
| `Live` | `Long` | `49.85` | 105,270,000.00 USD | 0.00 USD | 512.96 USD | `-48.55%` | `10.29` |
| `Live` | `Long` | `49.95` | 105,270,000.00 USD | 0.00 USD | 20,850.00 USD | `-48.44%` | `417.37` |
| `Live` | `Long` | `50.05` | 105,250,000.00 USD | 0.00 USD | 9,450.00 USD | `-48.34%` | `188.80` |
| `Live` | `Long` | `50.15` | 105,240,000.00 USD | 0.00 USD | 8,390.00 USD | `-48.24%` | `167.32` |
| `Live` | `Long` | `50.25` | 105,230,000.00 USD | 0.00 USD | 7,860.00 USD | `-48.13%` | `156.35` |
| `Live` | `Long` | `50.35` | 105,220,000.00 USD | 0.00 USD | 2,410.00 USD | `-48.03%` | `47.91` |
| `Live` | `Long` | `50.45` | 105,220,000.00 USD | 0.00 USD | 3,820.00 USD | `-47.93%` | `75.77` |
| `Live` | `Long` | `50.55` | 105,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | `-47.82%` | `24,047.47` |
| `Live` | `Long` | `50.65` | 104,000,000.00 USD | 0.00 USD | 995.78 USD | `-47.72%` | `19.66` |
| `Live` | `Long` | `50.75` | 104,000,000.00 USD | 0.00 USD | 12,470.00 USD | `-47.62%` | `245.66` |
| `Live` | `Long` | `50.85` | 103,990,000.00 USD | 0.00 USD | 19,710.00 USD | `-47.52%` | `387.64` |
| `Live` | `Long` | `50.95` | 103,970,000.00 USD | 0.00 USD | 6,570.00 USD | `-47.41%` | `129.02` |
| `Live` | `Long` | `51.05` | 103,960,000.00 USD | 0.00 USD | 2,680.00 USD | `-47.31%` | `52.57` |
| `Live` | `Long` | `51.15` | 103,960,000.00 USD | 0.00 USD | 3,410.00 USD | `-47.21%` | `66.63` |
| `Live` | `Long` | `51.25` | 103,960,000.00 USD | 0.00 USD | 1,950.00 USD | `-47.10%` | `38.05` |
| `Live` | `Long` | `51.35` | 103,950,000.00 USD | 0.00 USD | 10,640.00 USD | `-47.00%` | `207.26` |
| `Live` | `Long` | `51.45` | 103,940,000.00 USD | 0.00 USD | 7,110.00 USD | `-46.90%` | `138.18` |
| `Live` | `Long` | `51.55` | 103,940,000.00 USD | 0.00 USD | 140,560.00 USD | `-46.79%` | `2,726.69` |
| `Live` | `Long` | `51.65` | 103,800,000.00 USD | 0.00 USD | 7,490.00 USD | `-46.69%` | `145.07` |
| `Live` | `Long` | `51.75` | 103,790,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.59%` | `478.71` |
| `Live` | `Long` | `51.85` | 103,760,000.00 USD | 0.00 USD | 43,020.00 USD | `-46.48%` | `829.67` |
| `Live` | `Long` | `51.95` | 103,720,000.00 USD | 0.00 USD | 473,690.00 USD | `-46.38%` | `9,118.13` |
| `Live` | `Long` | `52.05` | 103,250,000.00 USD | 0.00 USD | 31,030.00 USD | `-46.28%` | `596.12` |
| `Live` | `Long` | `52.15` | 103,220,000.00 USD | 0.00 USD | 99,630.00 USD | `-46.17%` | `1,910.43` |
| `Live` | `Long` | `52.25` | 103,120,000.00 USD | 0.00 USD | 13,810.00 USD | `-46.07%` | `264.40` |
| `Live` | `Long` | `52.35` | 103,100,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.97%` | `19.66` |
| `Live` | `Long` | `52.45` | 103,100,000.00 USD | 0.00 USD | 157,790.00 USD | `-45.86%` | `3,008.41` |
| `Live` | `Long` | `52.55` | 102,940,000.00 USD | 0.00 USD | 13,210.00 USD | `-45.76%` | `251.45` |
| `Live` | `Long` | `52.65` | 102,930,000.00 USD | 0.00 USD | 3,120.00 USD | `-45.66%` | `59.23` |
| `Live` | `Long` | `52.75` | 102,930,000.00 USD | 0.00 USD | 30,770.00 USD | `-45.55%` | `583.33` |
| `Live` | `Long` | `52.85` | 102,900,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.45%` | `177.38` |
| `Live` | `Long` | `52.95` | 102,890,000.00 USD | 0.00 USD | 2,210.00 USD | `-45.35%` | `41.82` |
| `Live` | `Long` | `53.05` | 102,890,000.00 USD | 0.00 USD | 17,520.00 USD | `-45.24%` | `330.33` |
| `Live` | `Long` | `53.15` | 102,870,000.00 USD | 0.00 USD | 3,820.00 USD | `-45.14%` | `71.91` |
| `Live` | `Long` | `53.25` | 102,860,000.00 USD | 0.00 USD | 24,560.00 USD | `-45.04%` | `461.23` |
| `Live` | `Long` | `53.35` | 102,840,000.00 USD | 0.00 USD | 2,400.00 USD | `-44.93%` | `44.91` |
| `Live` | `Long` | `53.45` | 102,840,000.00 USD | 0.00 USD | 34,000.00 USD | `-44.83%` | `636.19` |
| `Live` | `Long` | `53.55` | 102,800,000.00 USD | 0.00 USD | 43,790.00 USD | `-44.73%` | `817.76` |
| `Live` | `Long` | `53.65` | 102,760,000.00 USD | 0.00 USD | 717.84 USD | `-44.63%` | `13.38` |
| `Live` | `Long` | `53.75` | 102,760,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.52%` | `67.00` |
| `Live` | `Long` | `53.85` | 102,760,000.00 USD | 0.00 USD | 19,990.00 USD | `-44.42%` | `371.18` |
| `Live` | `Long` | `53.95` | 102,740,000.00 USD | 0.00 USD | 58,760.00 USD | `-44.32%` | `1,089.22` |
| `Live` | `Long` | `54.05` | 102,680,000.00 USD | 0.00 USD | 1,430.00 USD | `-44.21%` | `26.49` |
| `Live` | `Long` | `54.15` | 102,670,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.11%` | `270.39` |
| `Live` | `Long` | `54.25` | 102,660,000.00 USD | 0.00 USD | 19,150.00 USD | `-44.01%` | `352.97` |
| `Live` | `Long` | `54.35` | 102,640,000.00 USD | 0.00 USD | 31,690.00 USD | `-43.90%` | `583.05` |
| `Live` | `Long` | `54.45` | 102,610,000.00 USD | 0.00 USD | 753.04 USD | `-43.80%` | `13.83` |
| `Live` | `Long` | `54.55` | 102,610,000.00 USD | 0.00 USD | 60,580.00 USD | `-43.70%` | `1,110.45` |
| `Live` | `Long` | `54.65` | 102,550,000.00 USD | 0.00 USD | 2,070.00 USD | `-43.59%` | `37.91` |
| `Live` | `Long` | `54.75` | 102,550,000.00 USD | 0.00 USD | 24,000.00 USD | `-43.49%` | `438.41` |
| `Live` | `Long` | `54.85` | 102,520,000.00 USD | 0.00 USD | 858,930.00 USD | `-43.39%` | `15,659.66` |
| `Live` | `Long` | `54.95` | 101,660,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.28%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 101,520,000.00 USD | 0.00 USD | 552.70 USD | `-43.18%` | `10.04` |
| `Live` | `Long` | `55.25` | 101,520,000.00 USD | 0.00 USD | 2,010.00 USD | `-42.97%` | `36.31` |
| `Live` | `Long` | `55.35` | 101,520,000.00 USD | 0.00 USD | 9,920.00 USD | `-42.87%` | `179.16` |
| `Live` | `Long` | `55.45` | 101,510,000.00 USD | 0.00 USD | 5,620.00 USD | `-42.77%` | `101.35` |
| `Live` | `Long` | `55.55` | 101,500,000.00 USD | 0.00 USD | 5,200.00 USD | `-42.66%` | `93.64` |
| `Live` | `Long` | `55.65` | 101,500,000.00 USD | 0.00 USD | 152,840.00 USD | `-42.56%` | `2,746.50` |
| `Live` | `Long` | `55.75` | 101,340,000.00 USD | 0.00 USD | 91,560.00 USD | `-42.46%` | `1,642.37` |
| `Live` | `Long` | `55.85` | 101,250,000.00 USD | 0.00 USD | 3,370.00 USD | `-42.35%` | `60.34` |
| `Live` | `Long` | `55.95` | 101,250,000.00 USD | 0.00 USD | 7,050.00 USD | `-42.25%` | `125.95` |
| `Live` | `Long` | `56.05` | 101,240,000.00 USD | 0.00 USD | 5,640.00 USD | `-42.15%` | `100.70` |
| `Live` | `Long` | `56.15` | 101,240,000.00 USD | 0.00 USD | 50,650.00 USD | `-42.04%` | `902.06` |
| `Live` | `Long` | `56.25` | 101,190,000.00 USD | 0.00 USD | 13,300.00 USD | `-41.94%` | `236.52` |
| `Live` | `Long` | `56.35` | 101,170,000.00 USD | 0.00 USD | 13,200.00 USD | `-41.84%` | `234.22` |
| `Live` | `Long` | `56.45` | 101,160,000.00 USD | 0.00 USD | 13,140.00 USD | `-41.74%` | `232.85` |
| `Live` | `Long` | `56.55` | 101,150,000.00 USD | 0.00 USD | 4,730.00 USD | `-41.63%` | `83.63` |
| `Live` | `Long` | `56.65` | 101,140,000.00 USD | 0.00 USD | 3,190.00 USD | `-41.53%` | `56.32` |
| `Live` | `Long` | `56.75` | 101,140,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.43%` | `165.87` |
| `Live` | `Long` | `56.85` | 101,130,000.00 USD | 0.00 USD | 1,670.00 USD | `-41.32%` | `29.30` |
| `Live` | `Long` | `56.95` | 101,130,000.00 USD | 0.00 USD | 14,320.00 USD | `-41.22%` | `251.38` |
| `Live` | `Long` | `57.05` | 101,110,000.00 USD | 0.00 USD | 2,770,000.00 USD | `-41.12%` | `48,627.98` |
| `Live` | `Long` | `57.15` | 98,340,000.00 USD | 0.00 USD | 29,170.00 USD | `-41.01%` | `510.36` |
| `Live` | `Long` | `57.25` | 98,310,000.00 USD | 0.00 USD | 26,940.00 USD | `-40.91%` | `470.50` |
| `Live` | `Long` | `57.35` | 98,280,000.00 USD | 0.00 USD | 8,330.00 USD | `-40.81%` | `145.17` |
| `Live` | `Long` | `57.45` | 98,270,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.70%` | `334.25` |
| `Live` | `Long` | `57.55` | 98,260,000.00 USD | 0.00 USD | 35,760.00 USD | `-40.60%` | `621.29` |
| `Live` | `Long` | `57.65` | 98,220,000.00 USD | 0.00 USD | 13,030.00 USD | `-40.50%` | `226.05` |
| `Live` | `Long` | `57.75` | 98,210,000.00 USD | 0.00 USD | 30,770.00 USD | `-40.39%` | `532.87` |
| `Live` | `Long` | `57.85` | 98,180,000.00 USD | 0.00 USD | 22,650.00 USD | `-40.29%` | `391.54` |
| `Live` | `Long` | `57.95` | 98,150,000.00 USD | 0.00 USD | 1,730.00 USD | `-40.19%` | `29.88` |
| `Live` | `Long` | `58.05` | 98,150,000.00 USD | 0.00 USD | 15,270.00 USD | `-40.08%` | `263.04` |
| `Live` | `Long` | `58.15` | 98,140,000.00 USD | 0.00 USD | 155,370.00 USD | `-39.98%` | `2,671.87` |
| `Live` | `Long` | `58.25` | 97,980,000.00 USD | 0.00 USD | 9,870.00 USD | `-39.88%` | `169.44` |
| `Live` | `Long` | `58.35` | 97,970,000.00 USD | 0.00 USD | 4,670.00 USD | `-39.77%` | `80.09` |
| `Live` | `Long` | `58.45` | 97,970,000.00 USD | 0.00 USD | 7,040.00 USD | `-39.67%` | `120.36` |
| `Live` | `Long` | `58.55` | 97,960,000.00 USD | 0.00 USD | 2,970.00 USD | `-39.57%` | `50.81` |
| `Live` | `Long` | `58.65` | 97,960,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-39.46%` | `40,107.13` |
| `Live` | `Long` | `58.75` | 95,600,000.00 USD | 0.00 USD | 1,900.00 USD | `-39.36%` | `32.37` |
| `Live` | `Long` | `58.85` | 95,600,000.00 USD | 0.00 USD | 6,130.00 USD | `-39.26%` | `104.08` |
| `Live` | `Long` | `58.95` | 95,600,000.00 USD | 0.00 USD | 16,160.00 USD | `-39.15%` | `274.15` |
| `Live` | `Long` | `59.05` | 95,580,000.00 USD | 0.00 USD | 22,080.00 USD | `-39.05%` | `373.97` |
| `Live` | `Long` | `59.15` | 95,560,000.00 USD | 0.00 USD | 4,760.00 USD | `-38.95%` | `80.44` |
| `Live` | `Long` | `59.25` | 95,550,000.00 USD | 0.00 USD | 376.83 USD | `-38.85%` | `6.36` |
| `Live` | `Long` | `59.35` | 95,550,000.00 USD | 0.00 USD | 28,320.00 USD | `-38.74%` | `477.21` |
| `Live` | `Long` | `59.45` | 95,520,000.00 USD | 0.00 USD | 4,230.00 USD | `-38.64%` | `71.12` |
| `Live` | `Long` | `59.55` | 95,520,000.00 USD | 0.00 USD | 8,610.00 USD | `-38.54%` | `144.57` |
| `Live` | `Long` | `59.65` | 95,510,000.00 USD | 0.00 USD | 3,640.00 USD | `-38.43%` | `61.07` |
| `Live` | `Long` | `59.75` | 95,510,000.00 USD | 0.00 USD | 20,570.00 USD | `-38.33%` | `344.35` |
| `Live` | `Long` | `59.85` | 95,490,000.00 USD | 0.00 USD | 3,830.00 USD | `-38.23%` | `63.91` |
| `Live` | `Long` | `59.95` | 95,480,000.00 USD | 0.00 USD | 37,750.00 USD | `-38.12%` | `629.77` |
| `Live` | `Long` | `60.05` | 95,450,000.00 USD | 0.00 USD | 43,240.00 USD | `-38.02%` | `720.00` |
| `Live` | `Long` | `60.15` | 95,400,000.00 USD | 0.00 USD | 35,140.00 USD | `-37.92%` | `584.16` |
| `Live` | `Long` | `60.25` | 95,370,000.00 USD | 0.00 USD | 499.47 USD | `-37.81%` | `8.29` |
| `Live` | `Long` | `60.35` | 95,370,000.00 USD | 0.00 USD | 32,290.00 USD | `-37.71%` | `535.10` |
| `Live` | `Long` | `60.45` | 95,330,000.00 USD | 0.00 USD | 69,320.00 USD | `-37.61%` | `1,146.68` |
| `Live` | `Long` | `60.55` | 95,270,000.00 USD | 0.00 USD | 2,760.00 USD | `-37.50%` | `45.51` |
| `Live` | `Long` | `60.65` | 95,260,000.00 USD | 0.00 USD | 711.42 USD | `-37.40%` | `11.73` |
| `Live` | `Long` | `60.75` | 95,260,000.00 USD | 0.00 USD | 5,300.00 USD | `-37.30%` | `87.26` |
| `Live` | `Long` | `60.85` | 95,260,000.00 USD | 0.00 USD | 28,860.00 USD | `-37.19%` | `474.33` |
| `Live` | `Long` | `60.95` | 95,230,000.00 USD | 0.00 USD | 56,410.00 USD | `-37.09%` | `925.59` |
| `Live` | `Long` | `61.05` | 95,170,000.00 USD | 0.00 USD | 21,180.00 USD | `-36.99%` | `346.93` |
| `Live` | `Long` | `61.15` | 95,150,000.00 USD | 0.00 USD | 5,900.00 USD | `-36.88%` | `96.47` |
| `Live` | `Long` | `61.25` | 95,140,000.00 USD | 0.00 USD | 5,260.00 USD | `-36.78%` | `85.83` |
| `Live` | `Long` | `61.35` | 95,140,000.00 USD | 0.00 USD | 10,280.00 USD | `-36.68%` | `167.54` |
| `Live` | `Long` | `61.45` | 95,130,000.00 USD | 0.00 USD | 26,450.00 USD | `-36.57%` | `430.48` |
| `Live` | `Long` | `61.55` | 95,100,000.00 USD | 0.00 USD | 18,770.00 USD | `-36.47%` | `305.01` |
| `Live` | `Long` | `61.65` | 95,080,000.00 USD | 0.00 USD | 20,520.00 USD | `-36.37%` | `332.83` |
| `Live` | `Long` | `61.75` | 95,060,000.00 USD | 0.00 USD | 16,580.00 USD | `-36.26%` | `268.54` |
| `Live` | `Long` | `61.85` | 95,050,000.00 USD | 0.00 USD | 5,500.00 USD | `-36.16%` | `88.89` |
| `Live` | `Long` | `61.95` | 95,040,000.00 USD | 0.00 USD | 8,720.00 USD | `-36.06%` | `140.73` |
| `Live` | `Long` | `62.05` | 95,030,000.00 USD | 0.00 USD | 9,000.00 USD | `-35.95%` | `145.05` |
| `Live` | `Long` | `62.15` | 95,020,000.00 USD | 0.00 USD | 45,390.00 USD | `-35.85%` | `730.34` |
| `Live` | `Long` | `62.25` | 94,980,000.00 USD | 0.00 USD | 8,720.00 USD | `-35.75%` | `140.13` |
| `Live` | `Long` | `62.35` | 94,970,000.00 USD | 0.00 USD | 16,180.00 USD | `-35.65%` | `259.49` |
| `Live` | `Long` | `62.45` | 94,950,000.00 USD | 0.00 USD | 22,050.00 USD | `-35.54%` | `353.15` |
| `Live` | `Long` | `62.55` | 94,930,000.00 USD | 0.00 USD | 227,580.00 USD | `-35.44%` | `3,638.40` |
| `Live` | `Long` | `62.65` | 94,700,000.00 USD | 0.00 USD | 2,230.00 USD | `-35.34%` | `35.62` |
| `Live` | `Long` | `62.75` | 94,700,000.00 USD | 0.00 USD | 20,770.00 USD | `-35.23%` | `331.05` |
| `Live` | `Long` | `62.85` | 94,680,000.00 USD | 0.00 USD | 31,460.00 USD | `-35.13%` | `500.54` |
| `Live` | `Long` | `62.95` | 94,650,000.00 USD | 0.00 USD | 2,990.00 USD | `-35.03%` | `47.46` |
| `Live` | `Long` | `63.05` | 94,650,000.00 USD | 0.00 USD | 44,200.00 USD | `-34.92%` | `701.10` |
| `Live` | `Long` | `63.15` | 94,600,000.00 USD | 0.00 USD | 89,390.00 USD | `-34.82%` | `1,415.47` |
| `Live` | `Long` | `63.25` | 94,510,000.00 USD | 0.00 USD | 18,290.00 USD | `-34.72%` | `289.21` |
| `Live` | `Long` | `63.35` | 94,490,000.00 USD | 0.00 USD | 63,290.00 USD | `-34.61%` | `999.06` |
| `Live` | `Long` | `63.45` | 94,430,000.00 USD | 0.00 USD | 291.24 USD | `-34.51%` | `4.59` |
| `Live` | `Long` | `63.55` | 94,430,000.00 USD | 0.00 USD | 49,290.00 USD | `-34.41%` | `775.56` |
| `Live` | `Long` | `63.65` | 94,380,000.00 USD | 0.00 USD | 575.40 USD | `-34.30%` | `9.04` |
| `Live` | `Long` | `63.75` | 94,380,000.00 USD | 0.00 USD | 32,540.00 USD | `-34.20%` | `510.36` |
| `Live` | `Long` | `63.85` | 94,350,000.00 USD | 0.00 USD | 40,980.00 USD | `-34.10%` | `641.89` |
| `Live` | `Long` | `63.95` | 94,310,000.00 USD | 0.00 USD | 2,280.00 USD | `-33.99%` | `35.70` |
| `Live` | `Long` | `64.05` | 94,300,000.00 USD | 0.00 USD | 434.90 USD | `-33.89%` | `6.79` |
| `Live` | `Long` | `64.25` | 94,300,000.00 USD | 0.00 USD | 101,470.00 USD | `-33.68%` | `1,579.27` |
| `Live` | `Long` | `64.35` | 94,200,000.00 USD | 0.00 USD | 875.16 USD | `-33.58%` | `13.60` |
| `Live` | `Long` | `64.45` | 94,200,000.00 USD | 0.00 USD | 4,320.00 USD | `-33.48%` | `67.00` |
| `Live` | `Long` | `64.55` | 94,200,000.00 USD | 0.00 USD | 8,960.00 USD | `-33.37%` | `138.79` |
| `Live` | `Long` | `64.65` | 94,190,000.00 USD | 0.00 USD | 2,220.00 USD | `-33.27%` | `34.28` |
| `Live` | `Long` | `64.85` | 94,190,000.00 USD | 0.00 USD | 396.23 USD | `-33.06%` | `6.11` |
| `Live` | `Long` | `64.95` | 94,190,000.00 USD | 0.00 USD | 32,680.00 USD | `-32.96%` | `503.23` |
| `Live` | `Long` | `65.05` | 94,150,000.00 USD | 0.00 USD | 250,430.00 USD | `-32.86%` | `3,849.85` |
| `Live` | `Long` | `65.15` | 93,900,000.00 USD | 0.00 USD | 17,690.00 USD | `-32.76%` | `271.47` |
| `Live` | `Long` | `65.25` | 93,880,000.00 USD | 0.00 USD | 15,120.00 USD | `-32.65%` | `231.74` |
| `Live` | `Long` | `65.35` | 93,870,000.00 USD | 0.00 USD | 55,730.00 USD | `-32.55%` | `852.79` |
| `Live` | `Long` | `65.45` | 93,810,000.00 USD | 0.00 USD | 3,130.00 USD | `-32.45%` | `47.89` |
| `Live` | `Long` | `65.55` | 93,810,000.00 USD | 0.00 USD | 50,820.00 USD | `-32.34%` | `775.31` |
| `Live` | `Long` | `65.65` | 93,760,000.00 USD | 0.00 USD | 59,910.00 USD | `-32.24%` | `912.62` |
| `Live` | `Long` | `65.75` | 93,700,000.00 USD | 0.00 USD | 5,070.00 USD | `-32.14%` | `77.05` |
| `Live` | `Long` | `65.85` | 93,700,000.00 USD | 0.00 USD | 1,300.00 USD | `-32.03%` | `19.81` |
| `Live` | `Long` | `65.95` | 93,690,000.00 USD | 0.00 USD | 62,250.00 USD | `-31.93%` | `943.96` |
| `Live` | `Long` | `66.05` | 93,630,000.00 USD | 0.00 USD | 4,840.00 USD | `-31.83%` | `73.25` |
| `Live` | `Long` | `66.25` | 93,630,000.00 USD | 0.00 USD | 14,930.00 USD | `-31.62%` | `225.38` |
| `Live` | `Long` | `66.35` | 93,610,000.00 USD | 0.00 USD | 13,850.00 USD | `-31.52%` | `208.80` |
| `Live` | `Long` | `66.45` | 93,600,000.00 USD | 0.00 USD | 13,450.00 USD | `-31.41%` | `202.43` |
| `Live` | `Long` | `66.55` | 93,580,000.00 USD | 0.00 USD | 59,860.00 USD | `-31.31%` | `899.44` |
| `Live` | `Long` | `66.65` | 93,520,000.00 USD | 0.00 USD | 13,170.00 USD | `-31.21%` | `197.56` |
| `Live` | `Long` | `66.75` | 93,510,000.00 USD | 0.00 USD | 5,930.00 USD | `-31.10%` | `88.77` |
| `Live` | `Long` | `66.85` | 93,510,000.00 USD | 0.00 USD | 1,910.00 USD | `-31.00%` | `28.53` |
| `Live` | `Long` | `66.95` | 93,500,000.00 USD | 0.00 USD | 1,770.00 USD | `-30.90%` | `26.44` |
| `Live` | `Long` | `67.05` | 93,500,000.00 USD | 0.00 USD | 37,010.00 USD | `-30.79%` | `552.01` |
| `Live` | `Long` | `67.15` | 93,460,000.00 USD | 0.00 USD | 358,860.00 USD | `-30.69%` | `5,344.10` |
| `Live` | `Long` | `67.25` | 93,110,000.00 USD | 0.00 USD | 248.83 USD | `-30.59%` | `3.70` |
| `Live` | `Long` | `67.35` | 93,110,000.00 USD | 0.00 USD | 1,230.00 USD | `-30.48%` | `18.27` |
| `Live` | `Long` | `67.45` | 93,100,000.00 USD | 0.00 USD | 21,630.00 USD | `-30.38%` | `320.66` |
| `Live` | `Long` | `67.55` | 93,080,000.00 USD | 0.00 USD | 53,490.00 USD | `-30.28%` | `791.93` |
| `Live` | `Long` | `67.65` | 93,030,000.00 USD | 0.00 USD | 141,830.00 USD | `-30.17%` | `2,096.57` |
| `Live` | `Long` | `67.75` | 92,890,000.00 USD | 0.00 USD | 11,530.00 USD | `-30.07%` | `170.21` |
| `Live` | `Long` | `67.85` | 92,880,000.00 USD | 0.00 USD | 4,670.00 USD | `-29.97%` | `68.85` |
| `Live` | `Long` | `68.05` | 92,870,000.00 USD | 0.00 USD | 10,300.00 USD | `-29.76%` | `151.41` |
| `Live` | `Long` | `68.15` | 92,860,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.66%` | `550,131.92` |
| `Live` | `Long` | `68.25` | 55,370,000.00 USD | 0.00 USD | 25,920.00 USD | `-29.56%` | `379.72` |
| `Live` | `Long` | `68.35` | 55,340,000.00 USD | 0.00 USD | 3,530.00 USD | `-29.45%` | `51.60` |
| `Live` | `Long` | `68.45` | 55,340,000.00 USD | 0.00 USD | 443,120.00 USD | `-29.35%` | `6,473.68` |
| `Live` | `Long` | `68.55` | 54,900,000.00 USD | 0.00 USD | 5,370.00 USD | `-29.25%` | `78.39` |
| `Live` | `Long` | `68.65` | 54,890,000.00 USD | 0.00 USD | 44,390.00 USD | `-29.14%` | `646.56` |
| `Live` | `Long` | `68.75` | 54,850,000.00 USD | 0.00 USD | 149,630.00 USD | `-29.04%` | `2,176.49` |
| `Live` | `Long` | `68.85` | 54,700,000.00 USD | 0.00 USD | 3,240.00 USD | `-28.94%` | `47.11` |
| `Live` | `Long` | `68.95` | 54,690,000.00 USD | 0.00 USD | 49,010.00 USD | `-28.83%` | `710.81` |
| `Live` | `Long` | `69.05` | 54,650,000.00 USD | 0.00 USD | 795,950.00 USD | `-28.73%` | `11,527.15` |
| `Live` | `Long` | `69.15` | 53,850,000.00 USD | 0.00 USD | 10,190.00 USD | `-28.63%` | `147.31` |
| `Live` | `Long` | `69.25` | 53,840,000.00 USD | 0.00 USD | 225,210.00 USD | `-28.52%` | `3,252.20` |
| `Live` | `Long` | `69.45` | 53,610,000.00 USD | 0.00 USD | 12,520,000.00 USD | `-28.32%` | `180,278.77` |
| `Live` | `Long` | `69.55` | 41,090,000.00 USD | 0.00 USD | 26,200.00 USD | `-28.21%` | `376.73` |
| `Live` | `Long` | `69.65` | 41,070,000.00 USD | 0.00 USD | 5,150.00 USD | `-28.11%` | `74.00` |
| `Live` | `Long` | `69.75` | 41,060,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-28.01%` | `23,041.83` |
| `Live` | `Long` | `69.85` | 39,460,000.00 USD | 0.00 USD | 24,140.00 USD | `-27.90%` | `345.61` |
| `Live` | `Long` | `69.95` | 39,430,000.00 USD | 0.00 USD | 8,800.00 USD | `-27.80%` | `125.81` |
| `Live` | `Long` | `70.05` | 39,420,000.00 USD | 0.00 USD | 682.99 USD | `-27.70%` | `9.75` |
| `Live` | `Long` | `70.15` | 39,420,000.00 USD | 0.00 USD | 3,670.00 USD | `-27.59%` | `52.27` |
| `Live` | `Long` | `70.25` | 39,420,000.00 USD | 0.00 USD | 72,890.00 USD | `-27.49%` | `1,037.54` |
| `Live` | `Long` | `70.35` | 39,340,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-27.39%` | `30,411.76` |
| `Live` | `Long` | `70.45` | 37,210,000.00 USD | 0.00 USD | 115,160.00 USD | `-27.28%` | `1,634.62` |
| `Live` | `Long` | `70.55` | 37,090,000.00 USD | 0.00 USD | 10,270.00 USD | `-27.18%` | `145.63` |
| `Live` | `Long` | `70.65` | 37,080,000.00 USD | 0.00 USD | 42,480.00 USD | `-27.08%` | `601.27` |
| `Live` | `Long` | `70.75` | 37,040,000.00 USD | 0.00 USD | 10,000.00 USD | `-26.98%` | `141.31` |
| `Live` | `Long` | `70.85` | 37,030,000.00 USD | 0.00 USD | 17,910.00 USD | `-26.87%` | `252.72` |
| `Live` | `Long` | `70.95` | 37,010,000.00 USD | 0.00 USD | 4,430.00 USD | `-26.77%` | `62.38` |
| `Live` | `Long` | `71.05` | 37,010,000.00 USD | 0.00 USD | 59,200.00 USD | `-26.67%` | `833.26` |
| `Live` | `Long` | `71.15` | 36,950,000.00 USD | 0.00 USD | 70,840.00 USD | `-26.56%` | `995.63` |
| `Live` | `Long` | `71.25` | 36,880,000.00 USD | 0.00 USD | 2,040.00 USD | `-26.46%` | `28.61` |
| `Live` | `Long` | `71.35` | 36,870,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-26.36%` | `15,651.38` |
| `Live` | `Long` | `71.45` | 35,760,000.00 USD | 0.00 USD | 31,640.00 USD | `-26.25%` | `442.82` |
| `Live` | `Long` | `71.55` | 35,720,000.00 USD | 0.00 USD | 76,050.00 USD | `-26.15%` | `1,062.87` |
| `Live` | `Long` | `71.65` | 35,650,000.00 USD | 0.00 USD | 894.91 USD | `-26.05%` | `12.49` |
| `Live` | `Long` | `71.75` | 35,650,000.00 USD | 0.00 USD | 28,130.00 USD | `-25.94%` | `392.08` |
| `Live` | `Long` | `71.85` | 35,620,000.00 USD | 0.00 USD | 13,960.00 USD | `-25.84%` | `194.24` |
| `Live` | `Long` | `71.95` | 35,610,000.00 USD | 0.00 USD | 12,710.00 USD | `-25.74%` | `176.62` |
| `Live` | `Long` | `72.05` | 35,590,000.00 USD | 0.00 USD | 21,780.00 USD | `-25.63%` | `302.26` |
| `Live` | `Long` | `72.15` | 35,570,000.00 USD | 0.00 USD | 131,360.00 USD | `-25.53%` | `1,820.66` |
| `Live` | `Long` | `72.25` | 35,440,000.00 USD | 0.00 USD | 269,280.00 USD | `-25.43%` | `3,727.07` |
| `Live` | `Long` | `72.35` | 35,170,000.00 USD | 0.00 USD | 28,860.00 USD | `-25.32%` | `398.85` |
| `Live` | `Long` | `72.45` | 35,140,000.00 USD | 0.00 USD | 1,840.00 USD | `-25.22%` | `25.36` |
| `Live` | `Long` | `72.55` | 35,140,000.00 USD | 0.00 USD | 16,340.00 USD | `-25.12%` | `225.23` |
| `Live` | `Long` | `72.65` | 35,120,000.00 USD | 0.00 USD | 33,720.00 USD | `-25.01%` | `464.15` |
| `Live` | `Long` | `72.75` | 35,090,000.00 USD | 0.00 USD | 3,940.00 USD | `-24.91%` | `54.10` |
| `Live` | `Long` | `72.85` | 35,090,000.00 USD | 0.00 USD | 186,830.00 USD | `-24.81%` | `2,564.61` |
| `Live` | `Long` | `72.95` | 34,900,000.00 USD | 0.00 USD | 7,580.00 USD | `-24.70%` | `103.91` |
| `Live` | `Long` | `73.05` | 34,890,000.00 USD | 0.00 USD | 8,160.00 USD | `-24.60%` | `111.69` |
| `Live` | `Long` | `73.15` | 34,880,000.00 USD | 0.00 USD | 24,730.00 USD | `-24.50%` | `338.01` |
| `Live` | `Long` | `73.25` | 34,860,000.00 USD | 0.00 USD | 28,470.00 USD | `-24.39%` | `388.71` |
| `Live` | `Long` | `73.35` | 34,830,000.00 USD | 0.00 USD | 3,330.00 USD | `-24.29%` | `45.42` |
| `Live` | `Long` | `73.45` | 34,830,000.00 USD | 0.00 USD | 13,390.00 USD | `-24.19%` | `182.24` |
| `Live` | `Long` | `73.55` | 34,810,000.00 USD | 0.00 USD | 15,210.00 USD | `-24.09%` | `206.81` |
| `Live` | `Long` | `73.65` | 34,800,000.00 USD | 0.00 USD | 38,120.00 USD | `-23.98%` | `517.59` |
| `Live` | `Long` | `73.75` | 34,760,000.00 USD | 0.00 USD | 84,720.00 USD | `-23.88%` | `1,148.75` |
| `Live` | `Long` | `73.85` | 34,680,000.00 USD | 0.00 USD | 15,410.00 USD | `-23.78%` | `208.63` |
| `Live` | `Long` | `73.95` | 34,660,000.00 USD | 0.00 USD | 40,420.00 USD | `-23.67%` | `546.60` |
| `Live` | `Long` | `74.05` | 34,620,000.00 USD | 0.00 USD | 34,460.00 USD | `-23.57%` | `465.34` |
| `Live` | `Long` | `74.15` | 34,590,000.00 USD | 0.00 USD | 21,430.00 USD | `-23.47%` | `289.03` |
| `Live` | `Long` | `74.25` | 34,560,000.00 USD | 0.00 USD | 50,970.00 USD | `-23.36%` | `686.47` |
| `Live` | `Long` | `74.35` | 34,510,000.00 USD | 0.00 USD | 37,750.00 USD | `-23.26%` | `507.69` |
| `Live` | `Long` | `74.45` | 34,470,000.00 USD | 0.00 USD | 26,740.00 USD | `-23.16%` | `359.12` |
| `Live` | `Long` | `74.55` | 34,450,000.00 USD | 0.00 USD | 6,260.00 USD | `-23.05%` | `84.00` |
| `Live` | `Long` | `74.65` | 34,440,000.00 USD | 0.00 USD | 102,100.00 USD | `-22.95%` | `1,367.69` |
| `Live` | `Long` | `74.75` | 34,340,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-22.85%` | `22,645.24` |
| `Live` | `Long` | `74.85` | 32,650,000.00 USD | 0.00 USD | 31,860.00 USD | `-22.74%` | `425.64` |
| `Live` | `Long` | `74.95` | 32,620,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-22.64%` | `15,907.90` |
| `Live` | `Long` | `75.05` | 31,420,000.00 USD | 0.00 USD | 41,500.00 USD | `-22.54%` | `552.96` |
| `Live` | `Long` | `75.15` | 31,380,000.00 USD | 0.00 USD | 3,150.00 USD | `-22.43%` | `41.94` |
| `Live` | `Long` | `75.25` | 31,380,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-22.33%` | `19,560.43` |
| `Live` | `Long` | `75.35` | 29,910,000.00 USD | 0.00 USD | 15,140.00 USD | `-22.23%` | `200.99` |
| `Live` | `Long` | `75.45` | 29,890,000.00 USD | 0.00 USD | 275,550.00 USD | `-22.12%` | `3,652.13` |
| `Live` | `Long` | `75.55` | 29,620,000.00 USD | 0.00 USD | 28,520.00 USD | `-22.02%` | `377.53` |
| `Live` | `Long` | `75.65` | 29,590,000.00 USD | 0.00 USD | 141,300.00 USD | `-21.92%` | `1,867.79` |
| `Live` | `Long` | `75.75` | 29,450,000.00 USD | 0.00 USD | 50,260.00 USD | `-21.81%` | `663.51` |
| `Live` | `Long` | `75.85` | 29,400,000.00 USD | 0.00 USD | 7,370.00 USD | `-21.71%` | `97.11` |
| `Live` | `Long` | `75.95` | 29,390,000.00 USD | 0.00 USD | 27,920.00 USD | `-21.61%` | `367.58` |
| `Live` | `Long` | `76.05` | 29,360,000.00 USD | 0.00 USD | 9,680.00 USD | `-21.50%` | `127.31` |
| `Live` | `Long` | `76.15` | 29,350,000.00 USD | 0.00 USD | 5,990.00 USD | `-21.40%` | `78.71` |
| `Live` | `Long` | `76.25` | 29,340,000.00 USD | 0.00 USD | 5,790.00 USD | `-21.30%` | `75.98` |
| `Live` | `Long` | `76.35` | 29,340,000.00 USD | 0.00 USD | 31,790.00 USD | `-21.20%` | `416.36` |
| `Live` | `Long` | `76.45` | 29,310,000.00 USD | 0.00 USD | 23,200.00 USD | `-21.09%` | `303.41` |
| `Live` | `Long` | `76.55` | 29,280,000.00 USD | 0.00 USD | 40,570.00 USD | `-20.99%` | `529.97` |
| `Live` | `Long` | `76.65` | 29,240,000.00 USD | 0.00 USD | 57,460.00 USD | `-20.89%` | `749.66` |
| `Live` | `Long` | `76.75` | 29,190,000.00 USD | 0.00 USD | 5,060.00 USD | `-20.78%` | `65.89` |
| `Live` | `Long` | `76.85` | 29,180,000.00 USD | 0.00 USD | 176,890.00 USD | `-20.68%` | `2,301.81` |
| `Live` | `Long` | `76.95` | 29,000,000.00 USD | 0.00 USD | 28,980.00 USD | `-20.58%` | `376.65` |
| `Live` | `Long` | `77.05` | 28,970,000.00 USD | 0.00 USD | 172,800.00 USD | `-20.47%` | `2,242.66` |
| `Live` | `Long` | `77.15` | 28,800,000.00 USD | 0.00 USD | 82,020.00 USD | `-20.37%` | `1,063.08` |
| `Live` | `Long` | `77.25` | 28,720,000.00 USD | 0.00 USD | 27,870.00 USD | `-20.27%` | `360.84` |
| `Live` | `Long` | `77.35` | 28,690,000.00 USD | 0.00 USD | 49,120.00 USD | `-20.16%` | `634.99` |
| `Live` | `Long` | `77.45` | 28,640,000.00 USD | 0.00 USD | 49,970.00 USD | `-20.06%` | `645.13` |
| `Live` | `Long` | `77.55` | 28,590,000.00 USD | 0.00 USD | 13,260.00 USD | `-19.96%` | `171.01` |
| `Live` | `Long` | `77.65` | 28,580,000.00 USD | 0.00 USD | 29,320.00 USD | `-19.85%` | `377.54` |
| `Live` | `Long` | `77.75` | 28,550,000.00 USD | 0.00 USD | 186,270.00 USD | `-19.75%` | `2,395.73` |
| `Live` | `Long` | `77.85` | 28,360,000.00 USD | 0.00 USD | 193,010.00 USD | `-19.65%` | `2,479.22` |
| `Live` | `Long` | `77.95` | 28,170,000.00 USD | 0.00 USD | 8,370.00 USD | `-19.54%` | `107.32` |
| `Live` | `Long` | `78.05` | 28,160,000.00 USD | 0.00 USD | 27,710.00 USD | `-19.44%` | `355.03` |
| `Live` | `Long` | `78.15` | 28,140,000.00 USD | 0.00 USD | 63,910.00 USD | `-19.34%` | `817.85` |
| `Live` | `Long` | `78.25` | 28,070,000.00 USD | 0.00 USD | 39,070.00 USD | `-19.23%` | `499.28` |
| `Live` | `Long` | `78.35` | 28,030,000.00 USD | 0.00 USD | 51,020.00 USD | `-19.13%` | `651.21` |
| `Live` | `Long` | `78.45` | 27,980,000.00 USD | 0.00 USD | 26,080.00 USD | `-19.03%` | `332.40` |
| `Live` | `Long` | `78.55` | 27,960,000.00 USD | 0.00 USD | 5,740.00 USD | `-18.92%` | `73.09` |
| `Live` | `Long` | `78.65` | 27,950,000.00 USD | 0.00 USD | 32,860.00 USD | `-18.82%` | `417.75` |
| `Live` | `Long` | `78.75` | 27,920,000.00 USD | 0.00 USD | 60,550.00 USD | `-18.72%` | `768.88` |
| `Live` | `Long` | `78.85` | 27,860,000.00 USD | 0.00 USD | 63,030.00 USD | `-18.61%` | `799.40` |
| `Live` | `Long` | `78.95` | 27,790,000.00 USD | 0.00 USD | 1,740.00 USD | `-18.51%` | `22.05` |
| `Live` | `Long` | `79.05` | 27,790,000.00 USD | 0.00 USD | 16,760.00 USD | `-18.41%` | `212.06` |
| `Live` | `Long` | `79.15` | 27,770,000.00 USD | 0.00 USD | 608,630.00 USD | `-18.31%` | `7,689.61` |
| `Live` | `Long` | `79.25` | 27,170,000.00 USD | 0.00 USD | 47,670.00 USD | `-18.20%` | `601.53` |
| `Live` | `Long` | `79.35` | 27,120,000.00 USD | 0.00 USD | 30,350.00 USD | `-18.10%` | `382.43` |
| `Live` | `Long` | `79.45` | 27,090,000.00 USD | 0.00 USD | 16,910.00 USD | `-18.00%` | `212.86` |
| `Live` | `Long` | `79.55` | 27,070,000.00 USD | 0.00 USD | 645.15 USD | `-17.89%` | `8.11` |
| `Live` | `Long` | `79.65` | 27,070,000.00 USD | 0.00 USD | 15,720.00 USD | `-17.79%` | `197.39` |
| `Live` | `Long` | `79.75` | 27,050,000.00 USD | 0.00 USD | 15,190.00 USD | `-17.69%` | `190.42` |
| `Live` | `Long` | `79.85` | 27,040,000.00 USD | 0.00 USD | 42,690.00 USD | `-17.58%` | `534.68` |
| `Live` | `Long` | `79.95` | 27,000,000.00 USD | 0.00 USD | 5,600.00 USD | `-17.48%` | `70.00` |
| `Live` | `Long` | `80.05` | 26,990,000.00 USD | 0.00 USD | 37,880.00 USD | `-17.38%` | `473.18` |
| `Live` | `Long` | `80.15` | 26,950,000.00 USD | 0.00 USD | 40,470.00 USD | `-17.27%` | `504.87` |
| `Live` | `Long` | `80.25` | 26,910,000.00 USD | 0.00 USD | 59,920.00 USD | `-17.17%` | `746.64` |
| `Live` | `Long` | `80.35` | 26,850,000.00 USD | 0.00 USD | 104,600.00 USD | `-17.07%` | `1,301.82` |
| `Live` | `Long` | `80.45` | 26,750,000.00 USD | 0.00 USD | 10,320.00 USD | `-16.96%` | `128.34` |
| `Live` | `Long` | `80.55` | 26,740,000.00 USD | 0.00 USD | 11,150.00 USD | `-16.86%` | `138.38` |
| `Live` | `Long` | `80.65` | 26,730,000.00 USD | 0.00 USD | 47,310.00 USD | `-16.76%` | `586.60` |
| `Live` | `Long` | `80.75` | 26,680,000.00 USD | 0.00 USD | 19,370.00 USD | `-16.65%` | `239.86` |
| `Live` | `Long` | `80.85` | 26,660,000.00 USD | 0.00 USD | 458,770.00 USD | `-16.55%` | `5,674.33` |
| `Live` | `Long` | `80.95` | 26,200,000.00 USD | 0.00 USD | 10,620.00 USD | `-16.45%` | `131.18` |
| `Live` | `Long` | `81.05` | 26,190,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-16.34%` | `27,492.63` |
| `Live` | `Long` | `81.15` | 23,960,000.00 USD | 0.00 USD | 132,270.00 USD | `-16.24%` | `1,629.98` |
| `Live` | `Long` | `81.25` | 23,830,000.00 USD | 0.00 USD | 23,460.00 USD | `-16.14%` | `288.80` |
| `Live` | `Long` | `81.35` | 23,810,000.00 USD | 0.00 USD | 60,780.00 USD | `-16.03%` | `747.20` |
| `Live` | `Long` | `81.45` | 23,750,000.00 USD | 0.00 USD | 70,230.00 USD | `-15.93%` | `862.29` |
| `Live` | `Long` | `81.55` | 23,680,000.00 USD | 0.00 USD | 65,060.00 USD | `-15.83%` | `797.81` |
| `Live` | `Long` | `81.65` | 23,610,000.00 USD | 0.00 USD | 15,400.00 USD | `-15.72%` | `188.66` |
| `Live` | `Long` | `81.75` | 23,600,000.00 USD | 0.00 USD | 18,650.00 USD | `-15.62%` | `228.11` |
| `Live` | `Long` | `81.85` | 23,580,000.00 USD | 0.00 USD | 44,330.00 USD | `-15.52%` | `541.62` |
| `Live` | `Long` | `81.95` | 23,530,000.00 USD | 0.00 USD | 68,660.00 USD | `-15.42%` | `837.80` |
| `Live` | `Long` | `82.05` | 23,460,000.00 USD | 0.00 USD | 117,440.00 USD | `-15.31%` | `1,431.29` |
| `Live` | `Long` | `82.15` | 23,350,000.00 USD | 0.00 USD | 805,410.00 USD | `-15.21%` | `9,804.12` |
| `Live` | `Long` | `82.25` | 22,540,000.00 USD | 0.00 USD | 24,700.00 USD | `-15.11%` | `300.35` |
| `Live` | `Long` | `82.35` | 22,520,000.00 USD | 0.00 USD | 159,740.00 USD | `-15.00%` | `1,939.77` |
| `Live` | `Long` | `82.45` | 22,360,000.00 USD | 0.00 USD | 209,090.00 USD | `-14.90%` | `2,535.94` |
| `Live` | `Long` | `82.55` | 22,150,000.00 USD | 0.00 USD | 30,900.00 USD | `-14.80%` | `374.28` |
| `Live` | `Long` | `82.65` | 22,120,000.00 USD | 0.00 USD | 104,620.00 USD | `-14.69%` | `1,265.84` |
| `Live` | `Long` | `82.75` | 22,010,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-14.59%` | `13,924.70` |
| `Live` | `Long` | `82.85` | 20,860,000.00 USD | 0.00 USD | 49,530.00 USD | `-14.49%` | `597.78` |
| `Live` | `Long` | `82.95` | 20,810,000.00 USD | 0.00 USD | 19,450.00 USD | `-14.38%` | `234.47` |
| `Live` | `Long` | `83.05` | 20,790,000.00 USD | 0.00 USD | 129,140.00 USD | `-14.28%` | `1,554.97` |
| `Live` | `Long` | `83.15` | 20,660,000.00 USD | 0.00 USD | 5,900.00 USD | `-14.18%` | `70.95` |
| `Live` | `Long` | `83.25` | 20,660,000.00 USD | 0.00 USD | 156,460.00 USD | `-14.07%` | `1,879.38` |
| `Live` | `Long` | `83.35` | 20,500,000.00 USD | 0.00 USD | 321,100.00 USD | `-13.97%` | `3,852.48` |
| `Live` | `Long` | `83.45` | 20,180,000.00 USD | 0.00 USD | 30,830.00 USD | `-13.87%` | `369.42` |
| `Live` | `Long` | `83.55` | 20,150,000.00 USD | 0.00 USD | 14,120.00 USD | `-13.76%` | `169.01` |
| `Live` | `Long` | `83.65` | 20,130,000.00 USD | 0.00 USD | 225,710.00 USD | `-13.66%` | `2,698.21` |
| `Live` | `Long` | `83.75` | 19,910,000.00 USD | 0.00 USD | 98,260.00 USD | `-13.56%` | `1,173.25` |
| `Live` | `Long` | `83.85` | 19,810,000.00 USD | 0.00 USD | 203,740.00 USD | `-13.45%` | `2,429.84` |
| `Live` | `Long` | `83.95` | 19,610,000.00 USD | 0.00 USD | 30,940.00 USD | `-13.35%` | `368.54` |
| `Live` | `Long` | `84.05` | 19,570,000.00 USD | 0.00 USD | 125,390.00 USD | `-13.25%` | `1,491.89` |
| `Live` | `Long` | `84.15` | 19,450,000.00 USD | 0.00 USD | 66,120.00 USD | `-13.14%` | `785.76` |
| `Live` | `Long` | `84.25` | 19,380,000.00 USD | 0.00 USD | 67,160.00 USD | `-13.04%` | `797.21` |
| `Live` | `Long` | `84.35` | 19,320,000.00 USD | 0.00 USD | 25,630.00 USD | `-12.94%` | `303.84` |
| `Live` | `Long` | `84.45` | 19,290,000.00 USD | 0.00 USD | 85,770.00 USD | `-12.83%` | `1,015.66` |
| `Live` | `Long` | `84.55` | 19,200,000.00 USD | 0.00 USD | 4,610.00 USD | `-12.73%` | `54.53` |
| `Live` | `Long` | `84.65` | 19,200,000.00 USD | 0.00 USD | 102,150.00 USD | `-12.63%` | `1,206.79` |
| `Live` | `Long` | `84.75` | 19,100,000.00 USD | 0.00 USD | 2,410,000.00 USD | `-12.53%` | `28,488.58` |
| `Live` | `Long` | `84.85` | 16,680,000.00 USD | 0.00 USD | 94,840.00 USD | `-12.42%` | `1,117.68` |
| `Live` | `Long` | `84.95` | 16,590,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-12.32%` | `14,770.37` |
| `Live` | `Long` | `85.05` | 15,330,000.00 USD | 0.00 USD | 14,870.00 USD | `-12.22%` | `174.81` |
| `Live` | `Long` | `85.15` | 15,320,000.00 USD | 0.00 USD | 5,940.00 USD | `-12.11%` | `69.80` |
| `Live` | `Long` | `85.25` | 15,310,000.00 USD | 0.00 USD | 571,570.00 USD | `-12.01%` | `6,704.67` |
| `Live` | `Long` | `85.35` | 14,740,000.00 USD | 0.00 USD | 21,000.00 USD | `-11.91%` | `246.09` |
| `Live` | `Long` | `85.45` | 14,720,000.00 USD | 0.00 USD | 46,070.00 USD | `-11.80%` | `539.18` |
| `Live` | `Long` | `85.55` | 14,670,000.00 USD | 0.00 USD | 23,080.00 USD | `-11.70%` | `269.84` |
| `Live` | `Long` | `85.65` | 14,650,000.00 USD | 0.00 USD | 42,860.00 USD | `-11.60%` | `500.36` |
| `Live` | `Long` | `85.75` | 14,610,000.00 USD | 0.00 USD | 9,830.00 USD | `-11.49%` | `114.66` |
| `Live` | `Long` | `85.85` | 14,600,000.00 USD | 0.00 USD | 85,650.00 USD | `-11.39%` | `997.67` |
| `Live` | `Long` | `85.95` | 14,510,000.00 USD | 0.00 USD | 738,410.00 USD | `-11.29%` | `8,591.21` |
| `Live` | `Long` | `86.05` | 13,770,000.00 USD | 0.00 USD | 256,680.00 USD | `-11.18%` | `2,982.96` |
| `Live` | `Long` | `86.15` | 13,520,000.00 USD | 0.00 USD | 60,740.00 USD | `-11.08%` | `705.04` |
| `Live` | `Long` | `86.25` | 13,460,000.00 USD | 0.00 USD | 44,050.00 USD | `-10.98%` | `510.72` |
| `Live` | `Long` | `86.35` | 13,410,000.00 USD | 0.00 USD | 182,490.00 USD | `-10.87%` | `2,113.43` |
| `Live` | `Long` | `86.45` | 13,230,000.00 USD | 0.00 USD | 108,330.00 USD | `-10.77%` | `1,253.13` |
| `Live` | `Long` | `86.55` | 13,120,000.00 USD | 0.00 USD | 28,140.00 USD | `-10.67%` | `325.09` |
| `Live` | `Long` | `86.65` | 13,090,000.00 USD | 0.00 USD | 225,720.00 USD | `-10.56%` | `2,604.91` |
| `Live` | `Long` | `86.75` | 12,870,000.00 USD | 0.00 USD | 37,350.00 USD | `-10.46%` | `430.52` |
| `Live` | `Long` | `86.85` | 12,830,000.00 USD | 0.00 USD | 78,930.00 USD | `-10.36%` | `908.76` |
| `Live` | `Long` | `86.95` | 12,750,000.00 USD | 0.00 USD | 154,360.00 USD | `-10.25%` | `1,775.26` |
| `Live` | `Long` | `87.05` | 12,600,000.00 USD | 0.00 USD | 53,710.00 USD | `-10.15%` | `617.04` |
| `Live` | `Long` | `87.15` | 12,540,000.00 USD | 0.00 USD | 68,830.00 USD | `-10.05%` | `789.82` |
| `Live` | `Long` | `87.25` | 12,470,000.00 USD | 0.00 USD | 50,440.00 USD | `-9.94%` | `578.15` |
| `Live` | `Long` | `87.35` | 12,420,000.00 USD | 0.00 USD | 76,460.00 USD | `-9.84%` | `875.35` |
| `Live` | `Long` | `87.45` | 12,350,000.00 USD | 0.00 USD | 149,740.00 USD | `-9.74%` | `1,712.27` |
| `Live` | `Long` | `87.55` | 12,200,000.00 USD | 0.00 USD | 202,390.00 USD | `-9.64%` | `2,311.67` |
| `Live` | `Long` | `87.65` | 12,000,000.00 USD | 0.00 USD | 176,180.00 USD | `-9.53%` | `2,010.06` |
| `Live` | `Long` | `87.75` | 11,820,000.00 USD | 0.00 USD | 28,310.00 USD | `-9.43%` | `322.66` |
| `Live` | `Long` | `87.85` | 11,790,000.00 USD | 0.00 USD | 69,500.00 USD | `-9.33%` | `791.12` |
| `Live` | `Long` | `87.95` | 11,720,000.00 USD | 0.00 USD | 6,600.00 USD | `-9.22%` | `75.02` |
| `Live` | `Long` | `88.05` | 11,720,000.00 USD | 0.00 USD | 153,760.00 USD | `-9.12%` | `1,746.26` |
| `Live` | `Long` | `88.15` | 11,560,000.00 USD | 0.00 USD | 22,010.00 USD | `-9.02%` | `249.71` |
| `Live` | `Long` | `88.25` | 11,540,000.00 USD | 0.00 USD | 49,740.00 USD | `-8.91%` | `563.61` |
| `Live` | `Long` | `88.35` | 11,490,000.00 USD | 0.00 USD | 109,890.00 USD | `-8.81%` | `1,243.85` |
| `Live` | `Long` | `88.45` | 11,380,000.00 USD | 0.00 USD | 71,730.00 USD | `-8.71%` | `811.02` |
| `Live` | `Long` | `88.55` | 11,310,000.00 USD | 0.00 USD | 248,900.00 USD | `-8.60%` | `2,810.79` |
| `Live` | `Long` | `88.65` | 11,060,000.00 USD | 0.00 USD | 82,420.00 USD | `-8.50%` | `929.76` |
| `Live` | `Long` | `88.75` | 10,980,000.00 USD | 0.00 USD | 157,190.00 USD | `-8.40%` | `1,771.17` |
| `Live` | `Long` | `88.85` | 10,820,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-8.29%` | `12,214.12` |
| `Live` | `Long` | `88.95` | 9,730,000.00 USD | 0.00 USD | 44,030.00 USD | `-8.19%` | `494.99` |
| `Live` | `Long` | `89.05` | 9,690,000.00 USD | 0.00 USD | 41,130.00 USD | `-8.09%` | `461.88` |
| `Live` | `Long` | `89.15` | 9,650,000.00 USD | 0.00 USD | 142,610.00 USD | `-7.98%` | `1,599.65` |
| `Live` | `Long` | `89.25` | 9,510,000.00 USD | 0.00 USD | 51,890.00 USD | `-7.88%` | `581.40` |
| `Live` | `Long` | `89.35` | 9,450,000.00 USD | 0.00 USD | 29,850.00 USD | `-7.78%` | `334.04` |
| `Live` | `Long` | `89.45` | 9,420,000.00 USD | 0.00 USD | 450,050.00 USD | `-7.67%` | `5,031.26` |
| `Live` | `Long` | `89.55` | 8,970,000.00 USD | 0.00 USD | 52,760.00 USD | `-7.57%` | `589.13` |
| `Live` | `Long` | `89.65` | 8,920,000.00 USD | 0.00 USD | 91,070.00 USD | `-7.47%` | `1,015.85` |
| `Live` | `Long` | `89.75` | 8,830,000.00 USD | 0.00 USD | 125,990.00 USD | `-7.36%` | `1,403.81` |
| `Live` | `Long` | `89.85` | 8,700,000.00 USD | 0.00 USD | 50,640.00 USD | `-7.26%` | `563.62` |
| `Live` | `Long` | `89.95` | 8,650,000.00 USD | 0.00 USD | 78,510.00 USD | `-7.16%` | `872.79` |
| `Live` | `Long` | `90.05` | 8,580,000.00 USD | 0.00 USD | 26,110.00 USD | `-7.05%` | `289.90` |
| `Live` | `Long` | `90.15` | 8,550,000.00 USD | 0.00 USD | 65,220.00 USD | `-6.95%` | `723.43` |
| `Live` | `Long` | `90.25` | 8,480,000.00 USD | 0.00 USD | 28,440.00 USD | `-6.85%` | `315.11` |
| `Live` | `Long` | `90.35` | 8,460,000.00 USD | 0.00 USD | 54,540.00 USD | `-6.75%` | `603.69` |
| `Live` | `Long` | `90.45` | 8,400,000.00 USD | 0.00 USD | 41,980.00 USD | `-6.64%` | `464.08` |
| `Live` | `Long` | `90.55` | 8,360,000.00 USD | 0.00 USD | 20,810.00 USD | `-6.54%` | `229.87` |
| `Live` | `Long` | `90.65` | 8,340,000.00 USD | 0.00 USD | 133,420.00 USD | `-6.44%` | `1,471.79` |
| `Live` | `Long` | `90.75` | 8,210,000.00 USD | 0.00 USD | 87,870.00 USD | `-6.33%` | `968.28` |
| `Live` | `Long` | `90.85` | 8,120,000.00 USD | 0.00 USD | 973,350.00 USD | `-6.23%` | `10,713.86` |
| `Live` | `Long` | `90.95` | 7,140,000.00 USD | 0.00 USD | 16,500.00 USD | `-6.13%` | `181.43` |
| `Live` | `Long` | `91.05` | 7,130,000.00 USD | 0.00 USD | 435,550.00 USD | `-6.02%` | `4,783.59` |
| `Live` | `Long` | `91.15` | 6,690,000.00 USD | 0.00 USD | 296,830.00 USD | `-5.92%` | `3,256.51` |
| `Live` | `Long` | `91.25` | 6,400,000.00 USD | 0.00 USD | 25,100.00 USD | `-5.82%` | `275.06` |
| `Live` | `Long` | `91.35` | 6,370,000.00 USD | 0.00 USD | 52,180.00 USD | `-5.71%` | `571.23` |
| `Live` | `Long` | `91.45` | 6,320,000.00 USD | 0.00 USD | 375,760.00 USD | `-5.61%` | `4,108.96` |
| `Live` | `Long` | `91.55` | 5,940,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-5.51%` | `13,551.90` |
| `Live` | `Long` | `91.65` | 4,700,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-5.40%` | `15,939.62` |
| `Live` | `Long` | `91.75` | 3,240,000.00 USD | 0.00 USD | 334,680.00 USD | `-5.30%` | `3,647.73` |
| `Live` | `Long` | `91.85` | 2,910,000.00 USD | 0.00 USD | 248,720.00 USD | `-5.20%` | `2,707.90` |
| `Live` | `Long` | `91.95` | 2,660,000.00 USD | 0.00 USD | 86,480.00 USD | `-5.09%` | `940.47` |
| `Live` | `Long` | `92.05` | 2,570,000.00 USD | 0.00 USD | 116,220.00 USD | `-4.99%` | `1,262.59` |
| `Live` | `Long` | `92.15` | 2,450,000.00 USD | 0.00 USD | 167,540.00 USD | `-4.89%` | `1,818.08` |
| `Live` | `Long` | `92.25` | 2,290,000.00 USD | 0.00 USD | 233,470.00 USD | `-4.78%` | `2,530.88` |
| `Live` | `Long` | `92.35` | 2,050,000.00 USD | 0.00 USD | 339,860.00 USD | `-4.68%` | `3,680.14` |
| `Live` | `Long` | `92.45` | 1,710,000.00 USD | 0.00 USD | 109,370.00 USD | `-4.58%` | `1,183.05` |
| `Live` | `Long` | `92.65` | 1,600,000.00 USD | 0.00 USD | 174,900.00 USD | `-4.37%` | `1,887.79` |
| `Live` | `Long` | `92.75` | 1,430,000.00 USD | 0.00 USD | 5,170.00 USD | `-4.27%` | `55.73` |
| `Live` | `Long` | `92.85` | 1,420,000.00 USD | 0.00 USD | 11,850.00 USD | `-4.16%` | `127.59` |
| `Live` | `Long` | `92.95` | 1,410,000.00 USD | 0.00 USD | 3,780.00 USD | `-4.06%` | `40.66` |
| `Live` | `Long` | `93.05` | 1,410,000.00 USD | 0.00 USD | 25,790.00 USD | `-3.96%` | `277.19` |
| `Live` | `Long` | `93.15` | 1,380,000.00 USD | 0.00 USD | 4,950.00 USD | `-3.86%` | `53.10` |
| `Live` | `Long` | `93.25` | 1,380,000.00 USD | 0.00 USD | 38,840.00 USD | `-3.75%` | `416.49` |
| `Live` | `Long` | `93.35` | 1,340,000.00 USD | 0.00 USD | 13,820.00 USD | `-3.65%` | `148.07` |
| `Live` | `Long` | `93.45` | 1,330,000.00 USD | 0.00 USD | 13,880.00 USD | `-3.55%` | `148.50` |
| `Live` | `Long` | `93.55` | 1,310,000.00 USD | 0.00 USD | 29,480.00 USD | `-3.44%` | `315.13` |
| `Live` | `Long` | `93.65` | 1,280,000.00 USD | 0.00 USD | 2,050.00 USD | `-3.34%` | `21.94` |
| `Live` | `Long` | `93.75` | 1,280,000.00 USD | 0.00 USD | 9,050.00 USD | `-3.24%` | `96.49` |
| `Live` | `Long` | `93.95` | 1,270,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-3.03%` | `12,061.71` |
| `Live` | `Long` | `94.05` | 137,430.00 USD | 0.00 USD | 9,740.00 USD | `-2.93%` | `103.59` |
| `Live` | `Long` | `94.15` | 127,690.00 USD | 0.00 USD | 45,570.00 USD | `-2.82%` | `484.05` |
| `Live` | `Long` | `94.25` | 82,120.00 USD | 0.00 USD | 1,860.00 USD | `-2.72%` | `19.73` |
| `Live` | `Long` | `94.35` | 80,260.00 USD | 0.00 USD | 51,340.00 USD | `-2.62%` | `544.14` |
| `Live` | `Long` | `94.45` | 28,920.00 USD | 0.00 USD | 2,430.00 USD | `-2.51%` | `25.74` |
| `Live` | `Long` | `94.55` | 26,480.00 USD | 0.00 USD | 24,250.00 USD | `-2.41%` | `256.47` |
| `Live` | `Long` | `94.85` | 2,240.00 USD | 0.00 USD | 136.58 USD | `-2.10%` | `1.44` |
| `Live` | `Long` | `95.95` | 2,100.00 USD | 0.00 USD | 990.20 USD | `-0.97%` | `10.32` |
| `Live` | `Long` | `96.15` | 1,110.00 USD | 0.00 USD | 432.68 USD | `-0.76%` | `4.50` |
| `Live` | `Short` | `96.55` | 2,880.00 USD | 2,880.00 USD | 0.00 USD | `-0.35%` | `29.88` |
| `Live` | `Long` | `96.85` | 676.01 USD | 0.00 USD | 676.01 USD | `-0.04%` | `6.98` |
| `Live` | `Short` | `97.05` | 205,990.00 USD | 203,110.00 USD | 0.00 USD | `+0.17%` | `2,092.83` |
| `Live` | `Short` | `97.25` | 254,730.00 USD | 48,730.00 USD | 0.00 USD | `+0.38%` | `501.11` |
| `Live` | `Short` | `97.35` | 256,310.00 USD | 1,580.00 USD | 0.00 USD | `+0.48%` | `16.25` |
| `Live` | `Short` | `97.45` | 257,160.00 USD | 850.74 USD | 0.00 USD | `+0.58%` | `8.73` |
| `Live` | `Short` | `97.55` | 302,940.00 USD | 45,780.00 USD | 0.00 USD | `+0.69%` | `469.34` |
| `Live` | `Short` | `97.75` | 303,110.00 USD | 166.17 USD | 0.00 USD | `+0.89%` | `1.70` |
| `Live` | `Short` | `97.95` | 303,860.00 USD | 746.38 USD | 0.00 USD | `+1.10%` | `7.62` |
| `Live` | `Short` | `98.05` | 304,340.00 USD | 487.31 USD | 0.00 USD | `+1.20%` | `4.97` |
| `Live` | `Short` | `98.15` | 309,120.00 USD | 4,780.00 USD | 0.00 USD | `+1.31%` | `48.66` |
| `Live` | `Short` | `98.25` | 313,170.00 USD | 4,050.00 USD | 0.00 USD | `+1.41%` | `41.18` |
| `Live` | `Short` | `98.35` | 313,320.00 USD | 151.46 USD | 0.00 USD | `+1.51%` | `1.54` |
| `Live` | `Short` | `98.55` | 319,250.00 USD | 5,930.00 USD | 0.00 USD | `+1.72%` | `60.17` |
| `Live` | `Short` | `98.65` | 328,980.00 USD | 9,740.00 USD | 0.00 USD | `+1.82%` | `98.70` |
| `Live` | `Short` | `98.75` | 330,130.00 USD | 1,150.00 USD | 0.00 USD | `+1.92%` | `11.60` |
| `Live` | `Short` | `98.95` | 331,150.00 USD | 1,020.00 USD | 0.00 USD | `+2.13%` | `10.28` |
| `Live` | `Short` | `99.05` | 354,210.00 USD | 23,060.00 USD | 0.00 USD | `+2.23%` | `232.80` |
| `Live` | `Short` | `99.15` | 482,300.00 USD | 128,100.00 USD | 0.00 USD | `+2.34%` | `1,291.96` |
| `Live` | `Short` | `99.25` | 486,200.00 USD | 3,900.00 USD | 0.00 USD | `+2.44%` | `39.26` |
| `Live` | `Short` | `99.35` | 515,510.00 USD | 29,310.00 USD | 0.00 USD | `+2.54%` | `294.98` |
| `Live` | `Short` | `99.45` | 517,620.00 USD | 2,120.00 USD | 0.00 USD | `+2.65%` | `21.28` |
| `Live` | `Short` | `99.55` | 577,950.00 USD | 60,330.00 USD | 0.00 USD | `+2.75%` | `606.03` |
| `Live` | `Short` | `99.65` | 657,940.00 USD | 79,990.00 USD | 0.00 USD | `+2.85%` | `802.69` |
| `Live` | `Short` | `99.75` | 658,980.00 USD | 1,040.00 USD | 0.00 USD | `+2.96%` | `10.40` |
| `Live` | `Short` | `99.85` | 662,020.00 USD | 3,040.00 USD | 0.00 USD | `+3.06%` | `30.49` |
| `Live` | `Short` | `99.95` | 663,270.00 USD | 1,250.00 USD | 0.00 USD | `+3.16%` | `12.48` |
| `Live` | `Short` | `100.05` | 664,820.00 USD | 1,550.00 USD | 0.00 USD | `+3.27%` | `15.51` |
| `Live` | `Short` | `100.15` | 676,680.00 USD | 11,860.00 USD | 0.00 USD | `+3.37%` | `118.40` |
| `Live` | `Short` | `100.25` | 683,850.00 USD | 7,170.00 USD | 0.00 USD | `+3.47%` | `71.51` |
| `Live` | `Short` | `100.55` | 684,820.00 USD | 969.30 USD | 0.00 USD | `+3.78%` | `9.64` |
| `Live` | `Short` | `100.75` | 696,770.00 USD | 11,950.00 USD | 0.00 USD | `+3.99%` | `118.63` |
| `Live` | `Short` | `100.85` | 706,850.00 USD | 10,090.00 USD | 0.00 USD | `+4.09%` | `100.00` |
| `Live` | `Short` | `101.05` | 707,170.00 USD | 320.33 USD | 0.00 USD | `+4.30%` | `3.17` |
| `Live` | `Short` | `101.15` | 730,970.00 USD | 23,800.00 USD | 0.00 USD | `+4.40%` | `235.27` |
| `Live` | `Short` | `101.25` | 731,740.00 USD | 769.50 USD | 0.00 USD | `+4.51%` | `7.60` |
| `Live` | `Short` | `101.35` | 733,070.00 USD | 1,330.00 USD | 0.00 USD | `+4.61%` | `13.09` |
| `Live` | `Short` | `101.45` | 733,190.00 USD | 118.70 USD | 0.00 USD | `+4.71%` | `1.17` |
| `Live` | `Short` | `101.55` | 736,630.00 USD | 3,440.00 USD | 0.00 USD | `+4.81%` | `33.91` |
| `Live` | `Short` | `101.65` | 739,280.00 USD | 2,640.00 USD | 0.00 USD | `+4.92%` | `26.02` |
| `Live` | `Short` | `102.05` | 747,830.00 USD | 8,550.00 USD | 0.00 USD | `+5.33%` | `83.80` |
| `Live` | `Short` | `102.15` | 747,950.00 USD | 120.54 USD | 0.00 USD | `+5.43%` | `1.18` |
| `Live` | `Short` | `102.25` | 749,120.00 USD | 1,170.00 USD | 0.00 USD | `+5.54%` | `11.44` |
| `Live` | `Short` | `102.35` | 759,100.00 USD | 9,980.00 USD | 0.00 USD | `+5.64%` | `97.50` |
| `Live` | `Short` | `102.45` | 759,920.00 USD | 826.77 USD | 0.00 USD | `+5.74%` | `8.07` |
| `Live` | `Short` | `102.65` | 761,430.00 USD | 1,500.00 USD | 0.00 USD | `+5.95%` | `14.63` |
| `Live` | `Short` | `102.75` | 762,370.00 USD | 944.27 USD | 0.00 USD | `+6.05%` | `9.19` |
| `Live` | `Short` | `102.95` | 765,450.00 USD | 3,080.00 USD | 0.00 USD | `+6.26%` | `29.92` |
| `Live` | `Short` | `103.05` | 768,830.00 USD | 3,380.00 USD | 0.00 USD | `+6.36%` | `32.80` |
| `Live` | `Short` | `103.15` | 779,830.00 USD | 11,000.00 USD | 0.00 USD | `+6.47%` | `106.62` |
| `Live` | `Short` | `103.25` | 781,140.00 USD | 1,310.00 USD | 0.00 USD | `+6.57%` | `12.68` |
| `Live` | `Short` | `103.35` | 783,950.00 USD | 2,820.00 USD | 0.00 USD | `+6.67%` | `27.25` |
| `Live` | `Short` | `103.45` | 787,260.00 USD | 3,300.00 USD | 0.00 USD | `+6.78%` | `31.94` |
| `Live` | `Short` | `103.55` | 2,230,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+6.88%` | `13,897.41` |
| `Live` | `Short` | `103.65` | 2,230,000.00 USD | 870.66 USD | 0.00 USD | `+6.98%` | `8.40` |
| `Live` | `Short` | `103.75` | 2,490,000.00 USD | 261,580.00 USD | 0.00 USD | `+7.09%` | `2,521.25` |
| `Live` | `Short` | `103.85` | 2,500,000.00 USD | 14,290.00 USD | 0.00 USD | `+7.19%` | `137.64` |
| `Live` | `Short` | `104.05` | 2,500,000.00 USD | 545.22 USD | 0.00 USD | `+7.40%` | `5.24` |
| `Live` | `Short` | `104.15` | 2,500,000.00 USD | 1,060.00 USD | 0.00 USD | `+7.50%` | `10.20` |
| `Live` | `Short` | `104.45` | 2,520,000.00 USD | 10,760.00 USD | 0.00 USD | `+7.81%` | `102.98` |
| `Live` | `Short` | `104.55` | 2,530,000.00 USD | 11,230.00 USD | 0.00 USD | `+7.91%` | `107.43` |
| `Live` | `Short` | `104.65` | 2,530,000.00 USD | 521.16 USD | 0.00 USD | `+8.01%` | `4.98` |
| `Live` | `Short` | `104.75` | 2,530,000.00 USD | 199.02 USD | 0.00 USD | `+8.12%` | `1.90` |
| `Live` | `Short` | `104.95` | 2,650,000.00 USD | 125,660.00 USD | 0.00 USD | `+8.32%` | `1,197.29` |
| `Live` | `Short` | `105.15` | 2,650,000.00 USD | 746.57 USD | 0.00 USD | `+8.53%` | `7.10` |
| `Live` | `Short` | `105.25` | 2,650,000.00 USD | 1,040.00 USD | 0.00 USD | `+8.63%` | `9.84` |
| `Live` | `Short` | `105.35` | 2,660,000.00 USD | 1,050.00 USD | 0.00 USD | `+8.74%` | `10.00` |
| `Live` | `Short` | `105.45` | 3,180,000.00 USD | 527,250.00 USD | 0.00 USD | `+8.84%` | `5,000.00` |
| `Live` | `Short` | `105.55` | 3,190,000.00 USD | 4,180.00 USD | 0.00 USD | `+8.94%` | `39.61` |
| `Live` | `Short` | `105.85` | 3,280,000.00 USD | 91,370.00 USD | 0.00 USD | `+9.25%` | `863.23` |
| `Live` | `Short` | `105.95` | 3,280,000.00 USD | 592.26 USD | 0.00 USD | `+9.36%` | `5.59` |
| `Live` | `Short` | `106.05` | 3,310,000.00 USD | 33,380.00 USD | 0.00 USD | `+9.46%` | `314.77` |
| `Live` | `Short` | `106.35` | 3,560,000.00 USD | 252,220.00 USD | 0.00 USD | `+9.77%` | `2,371.56` |
| `Live` | `Short` | `106.45` | 3,600,000.00 USD | 32,940.00 USD | 0.00 USD | `+9.87%` | `309.43` |
| `Live` | `Short` | `106.65` | 3,610,000.00 USD | 11,590.00 USD | 0.00 USD | `+10.08%` | `108.68` |
| `Live` | `Short` | `106.75` | 3,610,000.00 USD | 249.79 USD | 0.00 USD | `+10.18%` | `2.34` |
| `Live` | `Short` | `106.85` | 4,090,000.00 USD | 479,130.00 USD | 0.00 USD | `+10.29%` | `4,484.15` |
| `Live` | `Short` | `106.95` | 4,490,000.00 USD | 398,430.00 USD | 0.00 USD | `+10.39%` | `3,725.40` |
| `Live` | `Short` | `107.05` | 4,510,000.00 USD | 20,180.00 USD | 0.00 USD | `+10.49%` | `188.54` |
| `Live` | `Short` | `107.25` | 4,540,000.00 USD | 34,950.00 USD | 0.00 USD | `+10.70%` | `325.92` |
| `Live` | `Short` | `107.35` | 4,540,000.00 USD | 766.48 USD | 0.00 USD | `+10.80%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,580,000.00 USD | 32,580.00 USD | 0.00 USD | `+10.90%` | `303.18` |
| `Live` | `Short` | `107.55` | 4,580,000.00 USD | 221.55 USD | 0.00 USD | `+11.01%` | `2.06` |
| `Live` | `Short` | `107.65` | 4,580,000.00 USD | 1,820.00 USD | 0.00 USD | `+11.11%` | `16.87` |
| `Live` | `Short` | `107.85` | 4,720,000.00 USD | 143,340.00 USD | 0.00 USD | `+11.32%` | `1,329.08` |
| `Live` | `Short` | `108.05` | 4,720,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.52%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,720,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.63%` | `10.66` |
| `Live` | `Short` | `108.35` | 4,730,000.00 USD | 3,660.00 USD | 0.00 USD | `+11.83%` | `33.80` |
| `Live` | `Short` | `108.45` | 4,840,000.00 USD | 111,070.00 USD | 0.00 USD | `+11.94%` | `1,024.14` |
| `Live` | `Short` | `108.55` | 4,860,000.00 USD | 17,460.00 USD | 0.00 USD | `+12.04%` | `160.83` |
| `Live` | `Short` | `108.65` | 4,860,000.00 USD | 5,050.00 USD | 0.00 USD | `+12.14%` | `46.45` |
| `Live` | `Short` | `108.85` | 5,010,000.00 USD | 150,780.00 USD | 0.00 USD | `+12.35%` | `1,385.19` |
| `Live` | `Short` | `108.95` | 5,010,000.00 USD | 3,170.00 USD | 0.00 USD | `+12.45%` | `29.10` |
| `Live` | `Short` | `109.05` | 5,010,000.00 USD | 318.43 USD | 0.00 USD | `+12.56%` | `2.92` |
| `Live` | `Short` | `109.35` | 5,030,000.00 USD | 10,490.00 USD | 0.00 USD | `+12.87%` | `95.96` |
| `Live` | `Short` | `109.45` | 5,030,000.00 USD | 342.58 USD | 0.00 USD | `+12.97%` | `3.13` |
| `Live` | `Short` | `109.55` | 5,030,000.00 USD | 356.04 USD | 0.00 USD | `+13.07%` | `3.25` |
| `Live` | `Short` | `109.65` | 5,070,000.00 USD | 44,880.00 USD | 0.00 USD | `+13.18%` | `409.28` |
| `Live` | `Short` | `109.75` | 5,070,000.00 USD | 3,240.00 USD | 0.00 USD | `+13.28%` | `29.50` |
| `Live` | `Short` | `109.85` | 5,070,000.00 USD | 653.61 USD | 0.00 USD | `+13.38%` | `5.95` |
| `Live` | `Short` | `109.95` | 5,080,000.00 USD | 3,510.00 USD | 0.00 USD | `+13.49%` | `31.88` |
| `Live` | `Short` | `110.05` | 5,090,000.00 USD | 12,220.00 USD | 0.00 USD | `+13.59%` | `111.01` |
| `Live` | `Short` | `110.15` | 5,090,000.00 USD | 194.97 USD | 0.00 USD | `+13.69%` | `1.77` |
| `Live` | `Short` | `110.35` | 5,090,000.00 USD | 158.90 USD | 0.00 USD | `+13.90%` | `1.44` |
| `Live` | `Short` | `110.45` | 5,230,000.00 USD | 143,580.00 USD | 0.00 USD | `+14.00%` | `1,299.91` |
| `Live` | `Short` | `110.55` | 5,230,000.00 USD | 203.41 USD | 0.00 USD | `+14.10%` | `1.84` |
| `Live` | `Short` | `110.65` | 5,490,000.00 USD | 257,120.00 USD | 0.00 USD | `+14.21%` | `2,323.72` |
| `Live` | `Short` | `110.75` | 5,490,000.00 USD | 575.90 USD | 0.00 USD | `+14.31%` | `5.20` |
| `Live` | `Short` | `110.85` | 5,490,000.00 USD | 1,090.00 USD | 0.00 USD | `+14.41%` | `9.87` |
| `Live` | `Short` | `110.95` | 5,500,000.00 USD | 5,040.00 USD | 0.00 USD | `+14.52%` | `45.39` |
| `Live` | `Short` | `111.15` | 5,500,000.00 USD | 1,710.00 USD | 0.00 USD | `+14.72%` | `15.37` |
| `Live` | `Short` | `111.35` | 5,500,000.00 USD | 390.84 USD | 0.00 USD | `+14.93%` | `3.51` |
| `Live` | `Short` | `111.45` | 5,500,000.00 USD | 841.45 USD | 0.00 USD | `+15.03%` | `7.55` |
| `Live` | `Short` | `111.75` | 5,500,000.00 USD | 169.86 USD | 0.00 USD | `+15.34%` | `1.52` |
| `Live` | `Short` | `111.85` | 5,520,000.00 USD | 15,880.00 USD | 0.00 USD | `+15.45%` | `141.95` |
| `Live` | `Short` | `111.95` | 5,520,000.00 USD | 223.90 USD | 0.00 USD | `+15.55%` | `2.00` |
| `Live` | `Short` | `112.15` | 5,520,000.00 USD | 291.59 USD | 0.00 USD | `+15.76%` | `2.60` |
| `Live` | `Short` | `112.35` | 5,520,000.00 USD | 1,910.00 USD | 0.00 USD | `+15.96%` | `17.00` |
| `Live` | `Short` | `112.45` | 5,530,000.00 USD | 5,670.00 USD | 0.00 USD | `+16.07%` | `50.42` |
| `Live` | `Short` | `112.55` | 5,530,000.00 USD | 844.13 USD | 0.00 USD | `+16.17%` | `7.50` |
| `Live` | `Short` | `112.65` | 5,530,000.00 USD | 707.44 USD | 0.00 USD | `+16.27%` | `6.28` |
| `Live` | `Short` | `112.75` | 5,650,000.00 USD | 118,640.00 USD | 0.00 USD | `+16.38%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 5,750,000.00 USD | 108,760.00 USD | 0.00 USD | `+16.48%` | `963.76` |
| `Live` | `Short` | `113.05` | 5,750,000.00 USD | 406.98 USD | 0.00 USD | `+16.68%` | `3.60` |
| `Live` | `Short` | `113.15` | 5,760,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.79%` | `84.51` |
| `Live` | `Short` | `113.25` | 5,770,000.00 USD | 1,350.00 USD | 0.00 USD | `+16.89%` | `11.95` |
| `Live` | `Short` | `113.45` | 5,770,000.00 USD | 2,160.00 USD | 0.00 USD | `+17.10%` | `19.07` |
| `Live` | `Short` | `113.65` | 5,870,000.00 USD | 105,510.00 USD | 0.00 USD | `+17.30%` | `928.37` |
| `Live` | `Short` | `113.75` | 5,870,000.00 USD | 303.71 USD | 0.00 USD | `+17.41%` | `2.67` |
| `Live` | `Short` | `113.95` | 5,900,000.00 USD | 22,000.00 USD | 0.00 USD | `+17.61%` | `193.09` |
| `Live` | `Short` | `114.05` | 5,920,000.00 USD | 22,870.00 USD | 0.00 USD | `+17.72%` | `200.55` |
| `Live` | `Short` | `114.25` | 5,920,000.00 USD | 2,150.00 USD | 0.00 USD | `+17.92%` | `18.80` |
| `Live` | `Short` | `114.45` | 5,920,000.00 USD | 3,310.00 USD | 0.00 USD | `+18.13%` | `28.93` |
| `Live` | `Short` | `114.75` | 5,930,000.00 USD | 1,470.00 USD | 0.00 USD | `+18.44%` | `12.80` |
| `Live` | `Short` | `115.05` | 6,500,000.00 USD | 569,550.00 USD | 0.00 USD | `+18.75%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 6,500,000.00 USD | 1,100.00 USD | 0.00 USD | `+18.85%` | `9.52` |
| `Live` | `Short` | `115.35` | 6,500,000.00 USD | 5,850.00 USD | 0.00 USD | `+19.06%` | `50.73` |
| `Live` | `Short` | `115.45` | 7,380,000.00 USD | 879,040.00 USD | 0.00 USD | `+19.16%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 7,440,000.00 USD | 57,760.00 USD | 0.00 USD | `+19.27%` | `499.87` |
| `Live` | `Short` | `115.75` | 7,440,000.00 USD | 160.89 USD | 0.00 USD | `+19.47%` | `1.39` |
| `Live` | `Short` | `115.85` | 7,440,000.00 USD | 289.62 USD | 0.00 USD | `+19.57%` | `2.50` |
| `Live` | `Short` | `116.05` | 7,440,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.78%` | `38.34` |
| `Live` | `Short` | `116.25` | 7,440,000.00 USD | 180.19 USD | 0.00 USD | `+19.99%` | `1.55` |
| `Live` | `Short` | `116.35` | 7,450,000.00 USD | 4,960.00 USD | 0.00 USD | `+20.09%` | `42.60` |
| `Live` | `Short` | `116.55` | 7,450,000.00 USD | 2,040.00 USD | 0.00 USD | `+20.30%` | `17.52` |
| `Live` | `Short` | `116.65` | 7,450,000.00 USD | 113.15 USD | 0.00 USD | `+20.40%` | `0.97` |
| `Live` | `Short` | `116.85` | 7,450,000.00 USD | 1,720.00 USD | 0.00 USD | `+20.61%` | `14.72` |
| `Live` | `Short` | `117.05` | 7,450,000.00 USD | 156.85 USD | 0.00 USD | `+20.81%` | `1.34` |
| `Live` | `Short` | `117.15` | 7,540,000.00 USD | 89,950.00 USD | 0.00 USD | `+20.92%` | `767.80` |
| `Live` | `Short` | `117.25` | 7,560,000.00 USD | 16,600.00 USD | 0.00 USD | `+21.02%` | `141.58` |
| `Live` | `Short` | `117.35` | 7,570,000.00 USD | 11,840.00 USD | 0.00 USD | `+21.12%` | `100.91` |
| `Live` | `Short` | `117.45` | 12,350,000.00 USD | 4,780,000.00 USD | 0.00 USD | `+21.23%` | `40,716.81` |
| `Live` | `Short` | `117.55` | 12,360,000.00 USD | 4,300.00 USD | 0.00 USD | `+21.33%` | `36.60` |
| `Live` | `Short` | `117.75` | 12,370,000.00 USD | 10,360.00 USD | 0.00 USD | `+21.54%` | `87.98` |
| `Live` | `Short` | `117.95` | 12,370,000.00 USD | 353.85 USD | 0.00 USD | `+21.74%` | `3.00` |
| `Live` | `Short` | `118.05` | 12,400,000.00 USD | 28,100.00 USD | 0.00 USD | `+21.85%` | `238.04` |
| `Live` | `Short` | `118.35` | 16,870,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+22.16%` | `37,796.13` |
| `Live` | `Short` | `118.45` | 16,900,000.00 USD | 30,080.00 USD | 0.00 USD | `+22.26%` | `253.91` |
| `Live` | `Short` | `118.55` | 16,900,000.00 USD | 1,110.00 USD | 0.00 USD | `+22.36%` | `9.38` |
| `Live` | `Short` | `118.75` | 16,900,000.00 USD | 309.94 USD | 0.00 USD | `+22.57%` | `2.61` |
| `Live` | `Short` | `119.05` | 16,900,000.00 USD | 1,440.00 USD | 0.00 USD | `+22.88%` | `12.11` |
| `Live` | `Short` | `119.15` | 16,910,000.00 USD | 2,350.00 USD | 0.00 USD | `+22.98%` | `19.76` |
| `Live` | `Short` | `119.25` | 16,910,000.00 USD | 240.88 USD | 0.00 USD | `+23.08%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,530,000.00 USD | 621,120.00 USD | 0.00 USD | `+23.19%` | `5,204.19` |
| `Live` | `Short` | `119.45` | 18,390,000.00 USD | 861,240.00 USD | 0.00 USD | `+23.29%` | `7,210.07` |
| `Live` | `Short` | `119.55` | 18,420,000.00 USD | 27,920.00 USD | 0.00 USD | `+23.39%` | `233.55` |
| `Live` | `Short` | `119.75` | 18,420,000.00 USD | 261.06 USD | 0.00 USD | `+23.60%` | `2.18` |
| `Live` | `Short` | `119.85` | 18,430,000.00 USD | 13,070.00 USD | 0.00 USD | `+23.70%` | `109.05` |
| `Live` | `Short` | `120.05` | 18,520,000.00 USD | 95,660.00 USD | 0.00 USD | `+23.91%` | `796.83` |
| `Live` | `Short` | `120.15` | 18,530,000.00 USD | 3,440.00 USD | 0.00 USD | `+24.01%` | `28.60` |
| `Live` | `Short` | `120.45` | 18,530,000.00 USD | 145.74 USD | 0.00 USD | `+24.32%` | `1.21` |
| `Live` | `Short` | `120.55` | 18,530,000.00 USD | 1,190.00 USD | 0.00 USD | `+24.43%` | `9.86` |
| `Live` | `Short` | `120.95` | 18,540,000.00 USD | 13,290.00 USD | 0.00 USD | `+24.84%` | `109.91` |
| `Live` | `Short` | `121.15` | 18,540,000.00 USD | 316.20 USD | 0.00 USD | `+25.05%` | `2.61` |
| `Live` | `Short` | `121.55` | 18,550,000.00 USD | 5,940.00 USD | 0.00 USD | `+25.46%` | `48.87` |
| `Live` | `Short` | `121.65` | 18,570,000.00 USD | 16,190.00 USD | 0.00 USD | `+25.56%` | `133.08` |
| `Live` | `Short` | `121.75` | 18,570,000.00 USD | 105.92 USD | 0.00 USD | `+25.66%` | `0.87` |
| `Live` | `Short` | `122.05` | 18,620,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.97%` | `460.06` |
| `Live` | `Short` | `122.15` | 18,620,000.00 USD | 169.79 USD | 0.00 USD | `+26.08%` | `1.39` |
| `Live` | `Short` | `122.25` | 18,620,000.00 USD | 2,330.00 USD | 0.00 USD | `+26.18%` | `19.10` |
| `Live` | `Short` | `122.45` | 18,640,000.00 USD | 18,030.00 USD | 0.00 USD | `+26.39%` | `147.22` |
| `Live` | `Short` | `122.65` | 18,640,000.00 USD | 116.52 USD | 0.00 USD | `+26.59%` | `0.95` |
| `Live` | `Short` | `122.85` | 18,640,000.00 USD | 245.70 USD | 0.00 USD | `+26.80%` | `2.00` |
| `Live` | `Short` | `122.95` | 29,450,000.00 USD | 10,810,000.00 USD | 0.00 USD | `+26.90%` | `87,902.63` |
| `Live` | `Short` | `123.05` | 29,480,000.00 USD | 33,370.00 USD | 0.00 USD | `+27.01%` | `271.23` |
| `Live` | `Short` | `123.35` | 29,490,000.00 USD | 2,850.00 USD | 0.00 USD | `+27.32%` | `23.14` |
| `Live` | `Short` | `123.45` | 29,490,000.00 USD | 8,630.00 USD | 0.00 USD | `+27.42%` | `69.92` |
| `Live` | `Short` | `123.55` | 29,620,000.00 USD | 124,410.00 USD | 0.00 USD | `+27.52%` | `1,006.96` |
| `Live` | `Short` | `124.05` | 29,620,000.00 USD | 586.76 USD | 0.00 USD | `+28.04%` | `4.73` |
| `Live` | `Short` | `124.15` | 29,620,000.00 USD | 121.67 USD | 0.00 USD | `+28.14%` | `0.98` |
| `Live` | `Short` | `124.25` | 29,640,000.00 USD | 23,360.00 USD | 0.00 USD | `+28.24%` | `188.01` |
| `Live` | `Short` | `124.35` | 29,640,000.00 USD | 114.40 USD | 0.00 USD | `+28.35%` | `0.92` |
| `Live` | `Short` | `124.55` | 29,650,000.00 USD | 3,080.00 USD | 0.00 USD | `+28.55%` | `24.76` |
| `Live` | `Short` | `124.65` | 29,650,000.00 USD | 675.60 USD | 0.00 USD | `+28.66%` | `5.42` |
| `Live` | `Short` | `124.75` | 29,670,000.00 USD | 18,200.00 USD | 0.00 USD | `+28.76%` | `145.90` |
| `Live` | `Short` | `124.95` | 29,670,000.00 USD | 2,800.00 USD | 0.00 USD | `+28.97%` | `22.41` |
| `Live` | `Short` | `125.05` | 29,710,000.00 USD | 46,540.00 USD | 0.00 USD | `+29.07%` | `372.17` |
| `Live` | `Short` | `125.35` | 29,720,000.00 USD | 5,320.00 USD | 0.00 USD | `+29.38%` | `42.44` |
| `Live` | `Short` | `125.45` | 29,720,000.00 USD | 590.87 USD | 0.00 USD | `+29.48%` | `4.71` |
| `Live` | `Short` | `125.55` | 29,760,000.00 USD | 36,630.00 USD | 0.00 USD | `+29.59%` | `291.76` |
| `Live` | `Short` | `125.65` | 29,760,000.00 USD | 851.91 USD | 0.00 USD | `+29.69%` | `6.78` |
| `Live` | `Short` | `125.75` | 29,760,000.00 USD | 4,600.00 USD | 0.00 USD | `+29.79%` | `36.61` |
| `Live` | `Short` | `125.95` | 29,760,000.00 USD | 110.84 USD | 0.00 USD | `+30.00%` | `0.88` |
| `Live` | `Short` | `126.05` | 29,760,000.00 USD | 1,250.00 USD | 0.00 USD | `+30.10%` | `9.90` |
| `Live` | `Short` | `126.15` | 29,770,000.00 USD | 8,420.00 USD | 0.00 USD | `+30.21%` | `66.73` |
| `Live` | `Short` | `126.35` | 29,770,000.00 USD | 188.26 USD | 0.00 USD | `+30.41%` | `1.49` |
| `Live` | `Short` | `126.45` | 29,770,000.00 USD | 117.60 USD | 0.00 USD | `+30.52%` | `0.93` |
| `Live` | `Short` | `126.55` | 29,770,000.00 USD | 318.91 USD | 0.00 USD | `+30.62%` | `2.52` |
| `Live` | `Short` | `126.65` | 29,800,000.00 USD | 31,130.00 USD | 0.00 USD | `+30.72%` | `245.77` |
| `Live` | `Short` | `126.75` | 29,810,000.00 USD | 6,420.00 USD | 0.00 USD | `+30.83%` | `50.69` |
| `Live` | `Short` | `126.85` | 29,810,000.00 USD | 4,260.00 USD | 0.00 USD | `+30.93%` | `33.56` |
| `Live` | `Short` | `127.05` | 29,820,000.00 USD | 2,030.00 USD | 0.00 USD | `+31.13%` | `16.01` |
| `Live` | `Short` | `127.25` | 29,820,000.00 USD | 162.88 USD | 0.00 USD | `+31.34%` | `1.28` |
| `Live` | `Short` | `127.35` | 29,830,000.00 USD | 16,190.00 USD | 0.00 USD | `+31.44%` | `127.13` |
| `Live` | `Short` | `127.65` | 29,840,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.75%` | `37.89` |
| `Live` | `Short` | `127.75` | 29,840,000.00 USD | 720.51 USD | 0.00 USD | `+31.86%` | `5.64` |
| `Live` | `Short` | `127.85` | 29,840,000.00 USD | 388.66 USD | 0.00 USD | `+31.96%` | `3.04` |
| `Live` | `Short` | `127.95` | 30,110,000.00 USD | 266,410.00 USD | 0.00 USD | `+32.06%` | `2,082.13` |
| `Live` | `Short` | `128.05` | 30,220,000.00 USD | 116,190.00 USD | 0.00 USD | `+32.17%` | `907.38` |
| `Live` | `Short` | `128.15` | 30,230,000.00 USD | 6,740.00 USD | 0.00 USD | `+32.27%` | `52.61` |
| `Live` | `Short` | `128.35` | 30,230,000.00 USD | 195.09 USD | 0.00 USD | `+32.48%` | `1.52` |
| `Live` | `Short` | `128.65` | 30,230,000.00 USD | 788.62 USD | 0.00 USD | `+32.79%` | `6.13` |
| `Live` | `Short` | `128.75` | 30,250,000.00 USD | 18,730.00 USD | 0.00 USD | `+32.89%` | `145.45` |
| `Live` | `Short` | `128.85` | 30,290,000.00 USD | 42,690.00 USD | 0.00 USD | `+32.99%` | `331.32` |
| `Live` | `Short` | `129.15` | 30,350,000.00 USD | 55,570.00 USD | 0.00 USD | `+33.30%` | `430.25` |
| `Live` | `Short` | `129.25` | 30,380,000.00 USD | 32,780.00 USD | 0.00 USD | `+33.41%` | `253.64` |
| `Live` | `Short` | `129.35` | 31,080,000.00 USD | 699,390.00 USD | 0.00 USD | `+33.51%` | `5,406.93` |
| `Live` | `Short` | `129.55` | 31,080,000.00 USD | 1,130.00 USD | 0.00 USD | `+33.72%` | `8.70` |
| `Live` | `Short` | `129.75` | 31,120,000.00 USD | 36,480.00 USD | 0.00 USD | `+33.92%` | `281.19` |
| `Live` | `Short` | `129.85` | 31,120,000.00 USD | 490.83 USD | 0.00 USD | `+34.02%` | `3.78` |
| `Live` | `Short` | `129.95` | 31,190,000.00 USD | 68,950.00 USD | 0.00 USD | `+34.13%` | `530.61` |
| `Live` | `Short` | `130.25` | 31,200,000.00 USD | 13,200.00 USD | 0.00 USD | `+34.44%` | `101.38` |
| `Live` | `Short` | `130.35` | 31,200,000.00 USD | 145.99 USD | 0.00 USD | `+34.54%` | `1.12` |
| `Live` | `Short` | `130.65` | 31,200,000.00 USD | 3,570.00 USD | 0.00 USD | `+34.85%` | `27.29` |
| `Live` | `Short` | `130.85` | 31,710,000.00 USD | 503,960.00 USD | 0.00 USD | `+35.06%` | `3,851.40` |
| `Live` | `Short` | `130.95` | 31,710,000.00 USD | 2,070.00 USD | 0.00 USD | `+35.16%` | `15.84` |
| `Live` | `Short` | `131.05` | 31,710,000.00 USD | 188.71 USD | 0.00 USD | `+35.26%` | `1.44` |
| `Live` | `Short` | `131.25` | 31,710,000.00 USD | 1,560.00 USD | 0.00 USD | `+35.47%` | `11.87` |
| `Live` | `Short` | `131.35` | 31,710,000.00 USD | 855.09 USD | 0.00 USD | `+35.57%` | `6.51` |
| `Live` | `Short` | `131.45` | 31,710,000.00 USD | 219.52 USD | 0.00 USD | `+35.68%` | `1.67` |
| `Live` | `Short` | `131.85` | 31,720,000.00 USD | 5,430.00 USD | 0.00 USD | `+36.09%` | `41.20` |
| `Live` | `Short` | `131.95` | 31,720,000.00 USD | 106.88 USD | 0.00 USD | `+36.19%` | `0.81` |
| `Live` | `Short` | `132.05` | 31,730,000.00 USD | 11,940.00 USD | 0.00 USD | `+36.30%` | `90.43` |
| `Live` | `Short` | `132.15` | 31,730,000.00 USD | 325.09 USD | 0.00 USD | `+36.40%` | `2.46` |
| `Live` | `Short` | `132.55` | 31,740,000.00 USD | 8,730.00 USD | 0.00 USD | `+36.81%` | `65.85` |
| `Live` | `Short` | `132.65` | 31,740,000.00 USD | 240.10 USD | 0.00 USD | `+36.91%` | `1.81` |
| `Live` | `Short` | `132.85` | 31,820,000.00 USD | 79,190.00 USD | 0.00 USD | `+37.12%` | `596.06` |
| `Live` | `Short` | `133.05` | 31,820,000.00 USD | 103.78 USD | 0.00 USD | `+37.33%` | `0.78` |
| `Live` | `Short` | `133.15` | 31,830,000.00 USD | 8,440.00 USD | 0.00 USD | `+37.43%` | `63.42` |
| `Live` | `Short` | `133.65` | 31,830,000.00 USD | 156.37 USD | 0.00 USD | `+37.95%` | `1.17` |
| `Live` | `Short` | `133.75` | 31,980,000.00 USD | 151,200.00 USD | 0.00 USD | `+38.05%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 31,980,000.00 USD | 2,110.00 USD | 0.00 USD | `+38.26%` | `15.73` |
| `Live` | `Short` | `134.05` | 31,990,000.00 USD | 12,620.00 USD | 0.00 USD | `+38.36%` | `94.18` |
| `Live` | `Short` | `134.25` | 32,000,000.00 USD | 11,590.00 USD | 0.00 USD | `+38.57%` | `86.32` |
| `Live` | `Short` | `134.55` | 32,170,000.00 USD | 168,190.00 USD | 0.00 USD | `+38.88%` | `1,250.00` |
| `Live` | `Short` | `135.05` | 32,180,000.00 USD | 8,490.00 USD | 0.00 USD | `+39.39%` | `62.87` |
| `Live` | `Short` | `135.65` | 32,230,000.00 USD | 48,790.00 USD | 0.00 USD | `+40.01%` | `359.64` |
| `Live` | `Short` | `135.75` | 32,240,000.00 USD | 8,270.00 USD | 0.00 USD | `+40.11%` | `60.91` |
| `Live` | `Short` | `135.85` | 32,240,000.00 USD | 3,250.00 USD | 0.00 USD | `+40.22%` | `23.94` |
| `Live` | `Short` | `135.95` | 32,260,000.00 USD | 15,120.00 USD | 0.00 USD | `+40.32%` | `111.21` |
| `Live` | `Short` | `136.55` | 32,260,000.00 USD | 136.55 USD | 0.00 USD | `+40.94%` | `1.00` |
| `Live` | `Short` | `136.65` | 32,260,000.00 USD | 1,110.00 USD | 0.00 USD | `+41.04%` | `8.14` |
| `Live` | `Short` | `136.95` | 32,290,000.00 USD | 34,240.00 USD | 0.00 USD | `+41.35%` | `250.00` |
| `Live` | `Short` | `137.05` | 32,290,000.00 USD | 836.00 USD | 0.00 USD | `+41.46%` | `6.10` |
| `Live` | `Short` | `137.15` | 32,290,000.00 USD | 809.19 USD | 0.00 USD | `+41.56%` | `5.90` |
| `Live` | `Short` | `137.25` | 32,290,000.00 USD | 488.61 USD | 0.00 USD | `+41.66%` | `3.56` |
| `Live` | `Short` | `137.55` | 32,300,000.00 USD | 4,120.00 USD | 0.00 USD | `+41.97%` | `29.93` |
| `Live` | `Short` | `137.65` | 32,340,000.00 USD | 40,630.00 USD | 0.00 USD | `+42.08%` | `295.19` |
| `Live` | `Short` | `137.75` | 32,340,000.00 USD | 698.39 USD | 0.00 USD | `+42.18%` | `5.07` |
| `Live` | `Short` | `137.85` | 32,340,000.00 USD | 647.90 USD | 0.00 USD | `+42.28%` | `4.70` |
| `Live` | `Short` | `138.05` | 32,360,000.00 USD | 19,770.00 USD | 0.00 USD | `+42.49%` | `143.21` |
| `Live` | `Short` | `138.15` | 32,400,000.00 USD | 44,270.00 USD | 0.00 USD | `+42.59%` | `320.42` |
| `Live` | `Short` | `138.25` | 32,450,000.00 USD | 47,280.00 USD | 0.00 USD | `+42.69%` | `341.98` |
| `Live` | `Short` | `138.45` | 32,460,000.00 USD | 9,620.00 USD | 0.00 USD | `+42.90%` | `69.47` |
| `Live` | `Short` | `138.75` | 32,460,000.00 USD | 2,360.00 USD | 0.00 USD | `+43.21%` | `17.04` |
| `Live` | `Short` | `139.05` | 32,480,000.00 USD | 13,180.00 USD | 0.00 USD | `+43.52%` | `94.76` |
| `Live` | `Short` | `139.15` | 32,480,000.00 USD | 552.43 USD | 0.00 USD | `+43.62%` | `3.97` |
| `Live` | `Short` | `139.45` | 32,480,000.00 USD | 253.80 USD | 0.00 USD | `+43.93%` | `1.82` |
| `Live` | `Short` | `139.55` | 32,480,000.00 USD | 494.01 USD | 0.00 USD | `+44.04%` | `3.54` |
| `Live` | `Short` | `139.65` | 32,490,000.00 USD | 8,990.00 USD | 0.00 USD | `+44.14%` | `64.35` |
| `Live` | `Short` | `139.75` | 32,490,000.00 USD | 1,820.00 USD | 0.00 USD | `+44.24%` | `13.00` |
| `Live` | `Short` | `139.95` | 32,490,000.00 USD | 394.66 USD | 0.00 USD | `+44.45%` | `2.82` |
| `Live` | `Short` | `140.05` | 32,500,000.00 USD | 12,850.00 USD | 0.00 USD | `+44.55%` | `91.74` |
| `Live` | `Short` | `140.45` | 32,510,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.97%` | `34.66` |
| `Live` | `Short` | `140.55` | 32,510,000.00 USD | 702.75 USD | 0.00 USD | `+45.07%` | `5.00` |
| `Live` | `Short` | `140.65` | 32,520,000.00 USD | 8,780.00 USD | 0.00 USD | `+45.17%` | `62.42` |
| `Live` | `Short` | `140.75` | 32,520,000.00 USD | 627.75 USD | 0.00 USD | `+45.28%` | `4.46` |
| `Live` | `Short` | `140.95` | 32,590,000.00 USD | 69,260.00 USD | 0.00 USD | `+45.48%` | `491.40` |
| `Live` | `Short` | `141.05` | 32,590,000.00 USD | 3,080.00 USD | 0.00 USD | `+45.58%` | `21.83` |
| `Live` | `Short` | `141.35` | 32,590,000.00 USD | 210.61 USD | 0.00 USD | `+45.89%` | `1.49` |
| `Live` | `Short` | `141.45` | 32,840,000.00 USD | 247,540.00 USD | 0.00 USD | `+46.00%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 33,910,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+46.10%` | `7,611.25` |
| `Live` | `Short` | `141.65` | 33,910,000.00 USD | 111.90 USD | 0.00 USD | `+46.20%` | `0.79` |
| `Live` | `Short` | `141.75` | 33,920,000.00 USD | 2,460.00 USD | 0.00 USD | `+46.31%` | `17.33` |
| `Live` | `Short` | `141.85` | 34,780,000.00 USD | 866,960.00 USD | 0.00 USD | `+46.41%` | `6,111.83` |
| `Live` | `Short` | `142.35` | 34,810,000.00 USD | 23,090.00 USD | 0.00 USD | `+46.93%` | `162.19` |
| `Live` | `Short` | `142.45` | 34,810,000.00 USD | 151.00 USD | 0.00 USD | `+47.03%` | `1.06` |
| `Live` | `Short` | `142.55` | 34,810,000.00 USD | 2,440.00 USD | 0.00 USD | `+47.13%` | `17.10` |
| `Live` | `Short` | `142.75` | 34,810,000.00 USD | 368.30 USD | 0.00 USD | `+47.34%` | `2.58` |
| `Live` | `Short` | `143.15` | 34,810,000.00 USD | 1,330.00 USD | 0.00 USD | `+47.75%` | `9.31` |
| `Live` | `Short` | `143.35` | 34,830,000.00 USD | 22,260.00 USD | 0.00 USD | `+47.96%` | `155.27` |
| `Live` | `Short` | `143.75` | 35,430,000.00 USD | 596,560.00 USD | 0.00 USD | `+48.37%` | `4,150.00` |
| `Live` | `Short` | `143.85` | 35,520,000.00 USD | 89,820.00 USD | 0.00 USD | `+48.47%` | `624.42` |
| `Live` | `Short` | `144.05` | 35,520,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.68%` | `26.00` |
| `Live` | `Short` | `144.35` | 35,550,000.00 USD | 23,340.00 USD | 0.00 USD | `+48.99%` | `161.66` |
| `Live` | `Short` | `144.65` | 35,550,000.00 USD | 1,240.00 USD | 0.00 USD | `+49.30%` | `8.60` |
| `Live` | `Short` | `145.15` | 35,550,000.00 USD | 2,360.00 USD | 0.00 USD | `+49.82%` | `16.29` |
| `Live` | `Short` | `145.45` | 35,580,000.00 USD | 28,990.00 USD | 0.00 USD | `+50.13%` | `199.30` |
| `Live` | `Short` | `145.55` | 35,580,000.00 USD | 1,340.00 USD | 0.00 USD | `+50.23%` | `9.22` |
| `Live` | `Short` | `145.85` | 35,590,000.00 USD | 8,050.00 USD | 0.00 USD | `+50.54%` | `55.18` |
| `Live` | `Short` | `146.15` | 35,690,000.00 USD | 104,150.00 USD | 0.00 USD | `+50.85%` | `712.63` |
| `Live` | `Short` | `146.25` | 35,700,000.00 USD | 2,770.00 USD | 0.00 USD | `+50.95%` | `18.95` |
| `Live` | `Short` | `146.35` | 35,700,000.00 USD | 7,480.00 USD | 0.00 USD | `+51.06%` | `51.10` |
| `Live` | `Short` | `146.45` | 40,670,000.00 USD | 4,970,000.00 USD | 0.00 USD | `+51.16%` | `33,908.21` |
| `Live` | `Short` | `146.65` | 41,260,000.00 USD | 587,730.00 USD | 0.00 USD | `+51.37%` | `4,007.68` |
| `Live` | `Short` | `146.75` | 41,260,000.00 USD | 1,400.00 USD | 0.00 USD | `+51.47%` | `9.57` |
| `Live` | `Short` | `146.85` | 41,260,000.00 USD | 547.75 USD | 0.00 USD | `+51.57%` | `3.73` |
| `Live` | `Short` | `146.95` | 41,260,000.00 USD | 3,070.00 USD | 0.00 USD | `+51.67%` | `20.88` |
| `Live` | `Short` | `147.05` | 41,260,000.00 USD | 2,290.00 USD | 0.00 USD | `+51.78%` | `15.54` |
| `Live` | `Short` | `147.15` | 41,270,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.88%` | `11.75` |
| `Live` | `Short` | `147.35` | 41,270,000.00 USD | 169.45 USD | 0.00 USD | `+52.09%` | `1.15` |
| `Live` | `Short` | `147.45` | 41,270,000.00 USD | 204.96 USD | 0.00 USD | `+52.19%` | `1.39` |
| `Live` | `Short` | `147.55` | 41,270,000.00 USD | 2,290.00 USD | 0.00 USD | `+52.29%` | `15.53` |
| `Live` | `Short` | `147.65` | 41,710,000.00 USD | 443,190.00 USD | 0.00 USD | `+52.40%` | `3,001.61` |
| `Live` | `Short` | `147.75` | 41,710,000.00 USD | 277.77 USD | 0.00 USD | `+52.50%` | `1.88` |
| `Live` | `Short` | `147.85` | 41,710,000.00 USD | 300.14 USD | 0.00 USD | `+52.60%` | `2.03` |
| `Live` | `Short` | `147.95` | 41,820,000.00 USD | 108,230.00 USD | 0.00 USD | `+52.71%` | `731.56` |
| `Live` | `Short` | `148.15` | 41,820,000.00 USD | 102.22 USD | 0.00 USD | `+52.91%` | `0.69` |
| `Live` | `Short` | `148.35` | 41,900,000.00 USD | 78,690.00 USD | 0.00 USD | `+53.12%` | `530.42` |
| `Live` | `Short` | `148.45` | 41,900,000.00 USD | 163.29 USD | 0.00 USD | `+53.22%` | `1.10` |
| `Live` | `Short` | `148.55` | 42,760,000.00 USD | 864,710.00 USD | 0.00 USD | `+53.33%` | `5,821.00` |
| `Live` | `Short` | `148.65` | 42,790,000.00 USD | 21,850.00 USD | 0.00 USD | `+53.43%` | `147.00` |
| `Live` | `Short` | `148.75` | 42,880,000.00 USD | 93,700.00 USD | 0.00 USD | `+53.53%` | `629.91` |
| `Live` | `Short` | `149.05` | 43,040,000.00 USD | 160,350.00 USD | 0.00 USD | `+53.84%` | `1,075.79` |
| `Live` | `Short` | `149.35` | 44,430,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+54.15%` | `9,289.83` |
| `Live` | `Short` | `149.55` | 44,430,000.00 USD | 116.65 USD | 0.00 USD | `+54.36%` | `0.78` |
| `Live` | `Short` | `149.65` | 44,440,000.00 USD | 16,030.00 USD | 0.00 USD | `+54.46%` | `107.15` |
| `Live` | `Short` | `149.95` | 44,570,000.00 USD | 123,320.00 USD | 0.00 USD | `+54.77%` | `822.40` |
| `Live` | `Short` | `150.05` | 44,570,000.00 USD | 2,930.00 USD | 0.00 USD | `+54.87%` | `19.54` |
| `Live` | `Short` | `150.85` | 44,570,000.00 USD | 346.96 USD | 0.00 USD | `+55.70%` | `2.30` |
| `Live` | `Short` | `150.95` | 44,590,000.00 USD | 19,710.00 USD | 0.00 USD | `+55.80%` | `130.55` |
| `Live` | `Short` | `151.05` | 44,620,000.00 USD | 29,300.00 USD | 0.00 USD | `+55.91%` | `194.00` |
| `Live` | `Short` | `151.15` | 44,620,000.00 USD | 3,180.00 USD | 0.00 USD | `+56.01%` | `21.05` |
| `Live` | `Short` | `151.35` | 44,620,000.00 USD | 2,780.00 USD | 0.00 USD | `+56.22%` | `18.37` |
| `Live` | `Short` | `151.45` | 44,630,000.00 USD | 8,830.00 USD | 0.00 USD | `+56.32%` | `58.32` |
| `Live` | `Short` | `151.55` | 44,630,000.00 USD | 1,140.00 USD | 0.00 USD | `+56.42%` | `7.50` |
| `Live` | `Short` | `151.95` | 44,640,000.00 USD | 1,920.00 USD | 0.00 USD | `+56.84%` | `12.64` |
| `Live` | `Short` | `152.05` | 45,740,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+56.94%` | `7,271.63` |
| `Live` | `Short` | `152.25` | 45,740,000.00 USD | 200.97 USD | 0.00 USD | `+57.15%` | `1.32` |
| `Live` | `Short` | `152.35` | 46,070,000.00 USD | 331,180.00 USD | 0.00 USD | `+57.25%` | `2,173.78` |
| `Live` | `Short` | `152.45` | 46,080,000.00 USD | 4,070.00 USD | 0.00 USD | `+57.35%` | `26.70` |
| `Live` | `Short` | `152.55` | 46,500,000.00 USD | 423,220.00 USD | 0.00 USD | `+57.45%` | `2,774.28` |
| `Live` | `Short` | `152.75` | 46,500,000.00 USD | 1,570.00 USD | 0.00 USD | `+57.66%` | `10.30` |
| `Live` | `Short` | `153.15` | 46,550,000.00 USD | 45,670.00 USD | 0.00 USD | `+58.07%` | `298.21` |
| `Live` | `Short` | `153.25` | 46,570,000.00 USD | 20,200.00 USD | 0.00 USD | `+58.18%` | `131.84` |
| `Live` | `Short` | `153.35` | 46,570,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.28%` | `15.00` |
| `Live` | `Short` | `153.65` | 46,580,000.00 USD | 8,340.00 USD | 0.00 USD | `+58.59%` | `54.29` |
| `Live` | `Short` | `154.05` | 46,580,000.00 USD | 223.37 USD | 0.00 USD | `+59.00%` | `1.45` |
| `Live` | `Short` | `154.15` | 46,580,000.00 USD | 292.89 USD | 0.00 USD | `+59.11%` | `1.90` |
| `Live` | `Short` | `154.25` | 51,260,000.00 USD | 4,680,000.00 USD | 0.00 USD | `+59.21%` | `30,325.69` |
| `Live` | `Short` | `154.45` | 51,260,000.00 USD | 4,600.00 USD | 0.00 USD | `+59.42%` | `29.80` |
| `Live` | `Short` | `154.55` | 51,260,000.00 USD | 465.20 USD | 0.00 USD | `+59.52%` | `3.01` |
| `Live` | `Short` | `154.75` | 51,260,000.00 USD | 1,240.00 USD | 0.00 USD | `+59.73%` | `8.00` |
| `Live` | `Short` | `154.85` | 51,270,000.00 USD | 1,500.00 USD | 0.00 USD | `+59.83%` | `9.68` |
| `Live` | `Short` | `155.55` | 51,270,000.00 USD | 267.55 USD | 0.00 USD | `+60.55%` | `1.72` |
| `Live` | `Short` | `155.65` | 51,270,000.00 USD | 118.29 USD | 0.00 USD | `+60.65%` | `0.76` |
| `Live` | `Short` | `156.05` | 51,270,000.00 USD | 308.98 USD | 0.00 USD | `+61.07%` | `1.98` |
| `Live` | `Short` | `156.15` | 51,270,000.00 USD | 7,810.00 USD | 0.00 USD | `+61.17%` | `50.00` |
| `Live` | `Short` | `156.25` | 51,300,000.00 USD | 27,390.00 USD | 0.00 USD | `+61.27%` | `175.30` |
| `Live` | `Short` | `156.35` | 51,300,000.00 USD | 197.00 USD | 0.00 USD | `+61.38%` | `1.26` |
| `Live` | `Short` | `156.45` | 51,310,000.00 USD | 4,900.00 USD | 0.00 USD | `+61.48%` | `31.29` |
| `Live` | `Short` | `156.85` | 51,310,000.00 USD | 327.82 USD | 0.00 USD | `+61.89%` | `2.09` |
| `Live` | `Short` | `157.05` | 51,320,000.00 USD | 18,390.00 USD | 0.00 USD | `+62.10%` | `117.09` |
| `Live` | `Short` | `157.15` | 51,480,000.00 USD | 159,270.00 USD | 0.00 USD | `+62.20%` | `1,013.50` |
| `Live` | `Short` | `157.35` | 51,490,000.00 USD | 2,950.00 USD | 0.00 USD | `+62.41%` | `18.73` |
| `Live` | `Short` | `157.65` | 51,490,000.00 USD | 654.25 USD | 0.00 USD | `+62.72%` | `4.15` |
| `Live` | `Short` | `157.75` | 51,580,000.00 USD | 92,600.00 USD | 0.00 USD | `+62.82%` | `587.00` |
| `Live` | `Short` | `157.95` | 51,580,000.00 USD | 298.53 USD | 0.00 USD | `+63.03%` | `1.89` |
| `Live` | `Short` | `158.05` | 51,820,000.00 USD | 237,080.00 USD | 0.00 USD | `+63.13%` | `1,500.00` |
| `Live` | `Short` | `158.45` | 51,900,000.00 USD | 80,030.00 USD | 0.00 USD | `+63.54%` | `505.07` |
| `Live` | `Short` | `158.55` | 53,720,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+63.65%` | `11,488.27` |
| `Live` | `Short` | `159.05` | 54,190,000.00 USD | 474,780.00 USD | 0.00 USD | `+64.16%` | `2,985.11` |
| `Live` | `Short` | `159.25` | 54,230,000.00 USD | 40,450.00 USD | 0.00 USD | `+64.37%` | `253.99` |
| `Live` | `Short` | `159.35` | 54,340,000.00 USD | 101,490.00 USD | 0.00 USD | `+64.47%` | `636.89` |
| `Live` | `Short` | `159.65` | 54,340,000.00 USD | 1,760.00 USD | 0.00 USD | `+64.78%` | `11.01` |
| `Live` | `Short` | `159.85` | 54,380,000.00 USD | 39,490.00 USD | 0.00 USD | `+64.99%` | `247.07` |
| `Live` | `Short` | `160.05` | 54,380,000.00 USD | 497.76 USD | 0.00 USD | `+65.20%` | `3.11` |
| `Live` | `Short` | `160.15` | 55,060,000.00 USD | 683,000.00 USD | 0.00 USD | `+65.30%` | `4,264.75` |
| `Live` | `Short` | `160.35` | 55,060,000.00 USD | 655.83 USD | 0.00 USD | `+65.51%` | `4.09` |
| `Live` | `Short` | `160.45` | 55,380,000.00 USD | 320,900.00 USD | 0.00 USD | `+65.61%` | `2,000.00` |
| `Live` | `Short` | `160.75` | 55,610,000.00 USD | 227,000.00 USD | 0.00 USD | `+65.92%` | `1,412.13` |
| `Live` | `Short` | `161.05` | 55,610,000.00 USD | 2,240.00 USD | 0.00 USD | `+66.23%` | `13.93` |
| `Live` | `Short` | `161.35` | 55,610,000.00 USD | 1,530.00 USD | 0.00 USD | `+66.54%` | `9.51` |
| `Live` | `Short` | `161.45` | 55,720,000.00 USD | 106,980.00 USD | 0.00 USD | `+66.64%` | `662.62` |
| `Live` | `Short` | `161.55` | 55,720,000.00 USD | 410.34 USD | 0.00 USD | `+66.74%` | `2.54` |
| `Live` | `Short` | `161.95` | 55,870,000.00 USD | 144,610.00 USD | 0.00 USD | `+67.16%` | `892.95` |
| `Live` | `Short` | `162.65` | 61,590,000.00 USD | 5,720,000.00 USD | 0.00 USD | `+67.88%` | `35,170.27` |
| `Live` | `Short` | `162.95` | 61,590,000.00 USD | 1,350.00 USD | 0.00 USD | `+68.19%` | `8.29` |
| `Live` | `Short` | `163.65` | 61,590,000.00 USD | 1,040.00 USD | 0.00 USD | `+68.91%` | `6.38` |
| `Live` | `Short` | `163.85` | 61,590,000.00 USD | 786.48 USD | 0.00 USD | `+69.12%` | `4.80` |
| `Live` | `Short` | `163.95` | 61,810,000.00 USD | 223,350.00 USD | 0.00 USD | `+69.22%` | `1,362.30` |
| `Live` | `Short` | `164.55` | 61,820,000.00 USD | 6,590.00 USD | 0.00 USD | `+69.84%` | `40.03` |
| `Live` | `Short` | `165.15` | 61,820,000.00 USD | 198.18 USD | 0.00 USD | `+70.46%` | `1.20` |
| `Live` | `Short` | `165.25` | 61,840,000.00 USD | 17,080.00 USD | 0.00 USD | `+70.56%` | `103.36` |
| `Live` | `Short` | `165.85` | 61,840,000.00 USD | 620.28 USD | 0.00 USD | `+71.18%` | `3.74` |
| `Live` | `Short` | `166.15` | 61,840,000.00 USD | 996.90 USD | 0.00 USD | `+71.49%` | `6.00` |
| `Live` | `Short` | `166.25` | 61,850,000.00 USD | 14,070.00 USD | 0.00 USD | `+71.60%` | `84.61` |
| `Live` | `Short` | `166.55` | 61,850,000.00 USD | 149.90 USD | 0.00 USD | `+71.90%` | `0.90` |
| `Live` | `Short` | `166.65` | 61,920,000.00 USD | 68,630.00 USD | 0.00 USD | `+72.01%` | `411.80` |
| `Live` | `Short` | `166.85` | 61,920,000.00 USD | 3,440.00 USD | 0.00 USD | `+72.21%` | `20.63` |
| `Live` | `Short` | `167.65` | 61,920,000.00 USD | 115.68 USD | 0.00 USD | `+73.04%` | `0.69` |
| `Live` | `Short` | `167.75` | 61,950,000.00 USD | 23,890.00 USD | 0.00 USD | `+73.14%` | `142.40` |
| `Live` | `Short` | `168.05` | 61,950,000.00 USD | 122.68 USD | 0.00 USD | `+73.45%` | `0.73` |
| `Live` | `Short` | `168.35` | 61,970,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.76%` | `117.24` |
| `Live` | `Short` | `168.65` | 62,290,000.00 USD | 325,850.00 USD | 0.00 USD | `+74.07%` | `1,932.10` |
| `Live` | `Short` | `168.85` | 62,300,000.00 USD | 3,260.00 USD | 0.00 USD | `+74.28%` | `19.33` |
| `Live` | `Short` | `169.65` | 62,480,000.00 USD | 180,130.00 USD | 0.00 USD | `+75.10%` | `1,061.79` |
| `Live` | `Short` | `170.45` | 62,480,000.00 USD | 279.54 USD | 0.00 USD | `+75.93%` | `1.64` |
| `Live` | `Short` | `171.45` | 62,480,000.00 USD | 111.44 USD | 0.00 USD | `+76.96%` | `0.65` |
| `Live` | `Short` | `171.85` | 62,480,000.00 USD | 1,180.00 USD | 0.00 USD | `+77.38%` | `6.88` |
| `Live` | `Short` | `172.05` | 62,500,000.00 USD | 20,480.00 USD | 0.00 USD | `+77.58%` | `119.02` |
| `Live` | `Short` | `172.45` | 62,550,000.00 USD | 51,730.00 USD | 0.00 USD | `+77.99%` | `300.00` |
| `Live` | `Short` | `172.95` | 62,580,000.00 USD | 28,000.00 USD | 0.00 USD | `+78.51%` | `161.92` |
| `Live` | `Short` | `173.45` | 62,600,000.00 USD | 16,540.00 USD | 0.00 USD | `+79.03%` | `95.36` |
| `Live` | `Short` | `173.55` | 62,600,000.00 USD | 204.79 USD | 0.00 USD | `+79.13%` | `1.18` |
| `Live` | `Short` | `173.85` | 62,600,000.00 USD | 695.40 USD | 0.00 USD | `+79.44%` | `4.00` |
| `Live` | `Short` | `174.15` | 62,700,000.00 USD | 104,490.00 USD | 0.00 USD | `+79.75%` | `600.00` |
| `Live` | `Short` | `174.25` | 63,020,000.00 USD | 324,200.00 USD | 0.00 USD | `+79.85%` | `1,860.52` |
| `Live` | `Short` | `174.35` | 63,230,000.00 USD | 205,490.00 USD | 0.00 USD | `+79.96%` | `1,178.60` |
| `Live` | `Short` | `174.75` | 63,230,000.00 USD | 146.79 USD | 0.00 USD | `+80.37%` | `0.84` |
| `Live` | `Short` | `174.85` | 101,700,000.00 USD | 38,470,000.00 USD | 0.00 USD | `+80.47%` | `220,000.19` |
| `Live` | `Short` | `175.25` | 101,900,000.00 USD | 203,090.00 USD | 0.00 USD | `+80.88%` | `1,158.88` |
| `Live` | `Short` | `175.45` | 101,900,000.00 USD | 119.31 USD | 0.00 USD | `+81.09%` | `0.68` |
| `Live` | `Short` | `175.75` | 101,900,000.00 USD | 653.79 USD | 0.00 USD | `+81.40%` | `3.72` |
| `Live` | `Short` | `175.95` | 101,900,000.00 USD | 1,300.00 USD | 0.00 USD | `+81.61%` | `7.37` |
| `Live` | `Short` | `176.15` | 102,010,000.00 USD | 105,690.00 USD | 0.00 USD | `+81.81%` | `600.00` |
| `Live` | `Short` | `176.25` | 102,010,000.00 USD | 625.69 USD | 0.00 USD | `+81.92%` | `3.55` |
| `Live` | `Short` | `176.45` | 102,050,000.00 USD | 36,930.00 USD | 0.00 USD | `+82.12%` | `209.30` |
| `Live` | `Short` | `177.05` | 102,070,000.00 USD | 25,600.00 USD | 0.00 USD | `+82.74%` | `144.60` |
| `Live` | `Short` | `177.25` | 102,070,000.00 USD | 709.00 USD | 0.00 USD | `+82.95%` | `4.00` |
| `Live` | `Short` | `177.45` | 102,340,000.00 USD | 266,180.00 USD | 0.00 USD | `+83.16%` | `1,500.00` |
| `Live` | `Short` | `177.55` | 102,340,000.00 USD | 2,810.00 USD | 0.00 USD | `+83.26%` | `15.84` |
| `Live` | `Short` | `177.65` | 102,340,000.00 USD | 637.76 USD | 0.00 USD | `+83.36%` | `3.59` |
| `Live` | `Short` | `177.75` | 102,350,000.00 USD | 3,680.00 USD | 0.00 USD | `+83.46%` | `20.70` |
| `Live` | `Short` | `177.95` | 102,420,000.00 USD | 78,300.00 USD | 0.00 USD | `+83.67%` | `440.00` |
| `Live` | `Short` | `178.15` | 105,370,000.00 USD | 2,940,000.00 USD | 0.00 USD | `+83.88%` | `16,513.36` |
| `Live` | `Short` | `178.25` | 105,370,000.00 USD | 2,060.00 USD | 0.00 USD | `+83.98%` | `11.53` |
| `Live` | `Short` | `178.55` | 105,510,000.00 USD | 142,840.00 USD | 0.00 USD | `+84.29%` | `800.00` |
| `Live` | `Short` | `178.95` | 106,550,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+84.70%` | `5,800.00` |
| `Live` | `Short` | `179.15` | 106,550,000.00 USD | 338.59 USD | 0.00 USD | `+84.91%` | `1.89` |
| `Live` | `Short` | `179.65` | 106,550,000.00 USD | 4,490.00 USD | 0.00 USD | `+85.43%` | `25.00` |
| `Live` | `Short` | `179.75` | 106,550,000.00 USD | 154.59 USD | 0.00 USD | `+85.53%` | `0.86` |
| `Live` | `Short` | `180.05` | 106,600,000.00 USD | 50,020.00 USD | 0.00 USD | `+85.84%` | `277.83` |
| `Live` | `Short` | `180.45` | 106,720,000.00 USD | 116,590.00 USD | 0.00 USD | `+86.25%` | `646.12` |
| `Live` | `Short` | `180.55` | 106,720,000.00 USD | 3,970.00 USD | 0.00 USD | `+86.35%` | `22.01` |
| `Live` | `Short` | `180.65` | 110,340,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+86.46%` | `20,000.00` |
| `Live` | `Short` | `180.75` | 110,350,000.00 USD | 9,490.00 USD | 0.00 USD | `+86.56%` | `52.53` |
| `Live` | `Short` | `181.15` | 110,360,000.00 USD | 18,120.00 USD | 0.00 USD | `+86.97%` | `100.00` |
| `Live` | `Short` | `181.55` | 110,370,000.00 USD | 1,620.00 USD | 0.00 USD | `+87.39%` | `8.92` |
| `Live` | `Short` | `182.15` | 110,370,000.00 USD | 5,140.00 USD | 0.00 USD | `+88.01%` | `28.20` |
| `Live` | `Short` | `182.55` | 110,440,000.00 USD | 73,020.00 USD | 0.00 USD | `+88.42%` | `400.00` |
| `Live` | `Short` | `183.35` | 114,110,000.00 USD | 3,670,000.00 USD | 0.00 USD | `+89.24%` | `20,000.00` |
| `Live` | `Short` | `184.25` | 114,110,000.00 USD | 1,680.00 USD | 0.00 USD | `+90.17%` | `9.12` |
| `Live` | `Short` | `184.95` | 114,280,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.90%` | `893.35` |
| `Live` | `Short` | `185.05` | 114,280,000.00 USD | 797.57 USD | 0.00 USD | `+91.00%` | `4.31` |
| `Live` | `Short` | `185.25` | 114,290,000.00 USD | 8,410.00 USD | 0.00 USD | `+91.21%` | `45.41` |
| `Live` | `Short` | `185.45` | 114,290,000.00 USD | 2,770.00 USD | 0.00 USD | `+91.41%` | `14.94` |
| `Live` | `Short` | `185.55` | 114,300,000.00 USD | 12,160.00 USD | 0.00 USD | `+91.52%` | `65.56` |
| `Live` | `Short` | `185.65` | 114,300,000.00 USD | 137.38 USD | 0.00 USD | `+91.62%` | `0.74` |
| `Live` | `Short` | `185.75` | 114,300,000.00 USD | 390.07 USD | 0.00 USD | `+91.72%` | `2.10` |
| `Live` | `Short` | `185.85` | 114,300,000.00 USD | 247.18 USD | 0.00 USD | `+91.83%` | `1.33` |
| `Live` | `Short` | `185.95` | 114,360,000.00 USD | 53,420.00 USD | 0.00 USD | `+91.93%` | `287.30` |
| `Live` | `Short` | `186.75` | 114,360,000.00 USD | 2,800.00 USD | 0.00 USD | `+92.75%` | `15.00` |
| `Live` | `Short` | `186.85` | 114,360,000.00 USD | 2,190.00 USD | 0.00 USD | `+92.86%` | `11.72` |
| `Live` | `Short` | `186.95` | 114,370,000.00 USD | 4,110.00 USD | 0.00 USD | `+92.96%` | `22.01` |
| `Live` | `Short` | `187.35` | 114,370,000.00 USD | 1,010.00 USD | 0.00 USD | `+93.37%` | `5.41` |
| `Live` | `Short` | `187.55` | 114,370,000.00 USD | 232.56 USD | 0.00 USD | `+93.58%` | `1.24` |
| `Live` | `Short` | `187.85` | 114,370,000.00 USD | 1,560.00 USD | 0.00 USD | `+93.89%` | `8.32` |
| `Live` | `Short` | `188.15` | 114,400,000.00 USD | 29,130.00 USD | 0.00 USD | `+94.20%` | `154.84` |
| `Live` | `Short` | `188.45` | 114,400,000.00 USD | 256.29 USD | 0.00 USD | `+94.51%` | `1.36` |
| `Live` | `Short` | `188.55` | 114,400,000.00 USD | 231.92 USD | 0.00 USD | `+94.61%` | `1.23` |
| `Live` | `Short` | `188.95` | 114,400,000.00 USD | 1,450.00 USD | 0.00 USD | `+95.03%` | `7.69` |
| `Live` | `Short` | `189.25` | 114,400,000.00 USD | 2,270.00 USD | 0.00 USD | `+95.33%` | `11.98` |
| `Live` | `Short` | `189.85` | 114,400,000.00 USD | 189.85 USD | 0.00 USD | `+95.95%` | `1.00` |
| `Live` | `Short` | `189.95` | 114,690,000.00 USD | 284,930.00 USD | 0.00 USD | `+96.06%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 114,690,000.00 USD | 148.32 USD | 0.00 USD | `+96.26%` | `0.78` |
| `Live` | `Short` | `190.45` | 114,690,000.00 USD | 118.08 USD | 0.00 USD | `+96.57%` | `0.62` |
| `Live` | `Short` | `190.95` | 128,250,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+97.09%` | `71,045.04` |
| `Live` | `Short` | `191.15` | 128,640,000.00 USD | 382,300.00 USD | 0.00 USD | `+97.30%` | `2,000.00` |
| `Live` | `Short` | `191.25` | 128,640,000.00 USD | 2,510.00 USD | 0.00 USD | `+97.40%` | `13.11` |
| `Live` | `Short` | `191.45` | 128,700,000.00 USD | 62,820.00 USD | 0.00 USD | `+97.61%` | `328.11` |
| `Live` | `Short` | `191.75` | 128,710,000.00 USD | 5,430.00 USD | 0.00 USD | `+97.92%` | `28.34` |
| `Live` | `Short` | `191.95` | 128,710,000.00 USD | 322.48 USD | 0.00 USD | `+98.12%` | `1.68` |
| `Live` | `Short` | `192.75` | 128,710,000.00 USD | 192.75 USD | 0.00 USD | `+98.95%` | `1.00` |
| `Live` | `Short` | `193.55` | 128,820,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.77%` | `592.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,070,000.00 USD | 0.00 USD | 13,940.00 USD | `-76.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,060,000.00 USD | 0.00 USD | 499.56 USD | `-68.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 10,060,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,060,000.00 USD | 0.00 USD | 818.32 USD | `-65.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,060,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 10,060,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 10,050,000.00 USD | 0.00 USD | 434.85 USD | `-62.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 10,050,000.00 USD | 0.00 USD | 267.87 USD | `-60.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.65` | 10,050,000.00 USD | 0.00 USD | 206.00 USD | `-60.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 10,050,000.00 USD | 0.00 USD | 208.14 USD | `-59.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,050,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,050,000.00 USD | 0.00 USD | 157.01 USD | `-58.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,050,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 10,050,000.00 USD | 0.00 USD | 120.66 USD | `-56.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 10,050,000.00 USD | 0.00 USD | 121.81 USD | `-56.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,050,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 9,880,000.00 USD | 0.00 USD | 105.00 USD | `-54.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 9,880,000.00 USD | 0.00 USD | 59,730.00 USD | `-53.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 9,820,000.00 USD | 0.00 USD | 251.05 USD | `-51.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 9,820,000.00 USD | 0.00 USD | 143.25 USD | `-50.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 9,820,000.00 USD | 0.00 USD | 191.40 USD | `-50.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 9,820,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 9,770,000.00 USD | 0.00 USD | 664.65 USD | `-49.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 9,770,000.00 USD | 0.00 USD | 103.35 USD | `-49.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 9,770,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 9,760,000.00 USD | 0.00 USD | 107.03 USD | `-48.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 9,760,000.00 USD | 0.00 USD | 102.62 USD | `-47.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 9,760,000.00 USD | 0.00 USD | 134.28 USD | `-47.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 9,760,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 9,760,000.00 USD | 0.00 USD | 102.74 USD | `-46.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 9,760,000.00 USD | 0.00 USD | 126.12 USD | `-45.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 9,760,000.00 USD | 0.00 USD | 200.15 USD | `-45.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 9,760,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 9,730,000.00 USD | 0.00 USD | 1,660.00 USD | `-44.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 9,730,000.00 USD | 0.00 USD | 641.57 USD | `-44.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 9,730,000.00 USD | 0.00 USD | 139.87 USD | `-43.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 9,730,000.00 USD | 0.00 USD | 209.19 USD | `-43.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 9,730,000.00 USD | 0.00 USD | 894.56 USD | `-42.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 9,730,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 9,720,000.00 USD | 0.00 USD | 6,960.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 9,720,000.00 USD | 0.00 USD | 265.53 USD | `-40.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 9,720,000.00 USD | 0.00 USD | 158.48 USD | `-40.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 9,720,000.00 USD | 0.00 USD | 3,820.00 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 9,710,000.00 USD | 0.00 USD | 428.72 USD | `-39.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 9,710,000.00 USD | 0.00 USD | 295.25 USD | `-39.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 9,710,000.00 USD | 0.00 USD | 200.01 USD | `-38.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 9,710,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 9,710,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 9,700,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 9,670,000.00 USD | 0.00 USD | 2,820.00 USD | `-37.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 9,660,000.00 USD | 0.00 USD | 488.63 USD | `-37.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 9,660,000.00 USD | 0.00 USD | 258.90 USD | `-37.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 9,660,000.00 USD | 0.00 USD | 206.13 USD | `-37.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 9,660,000.00 USD | 0.00 USD | 724.78 USD | `-37.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 9,660,000.00 USD | 0.00 USD | 14,350.00 USD | `-36.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 9,650,000.00 USD | 0.00 USD | 142.33 USD | `-36.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 9,650,000.00 USD | 0.00 USD | 100.78 USD | `-36.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 9,650,000.00 USD | 0.00 USD | 243.74 USD | `-36.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 9,650,000.00 USD | 0.00 USD | 6,720.00 USD | `-35.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 9,640,000.00 USD | 0.00 USD | 136.98 USD | `-35.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 9,640,000.00 USD | 0.00 USD | 9,990.00 USD | `-34.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 9,630,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 9,630,000.00 USD | 0.00 USD | 222.55 USD | `-33.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 9,630,000.00 USD | 0.00 USD | 163.19 USD | `-33.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 9,630,000.00 USD | 0.00 USD | 129.70 USD | `-33.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 9,630,000.00 USD | 0.00 USD | 2,440.00 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 9,620,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 9,620,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 9,620,000.00 USD | 0.00 USD | 9,140.00 USD | `-31.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 9,610,000.00 USD | 0.00 USD | 541.72 USD | `-31.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 9,610,000.00 USD | 0.00 USD | 335.25 USD | `-30.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 9,610,000.00 USD | 0.00 USD | 268.60 USD | `-30.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 9,610,000.00 USD | 0.00 USD | 195.30 USD | `-29.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 9,610,000.00 USD | 0.00 USD | 7,600.00 USD | `-29.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 9,600,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 9,600,000.00 USD | 0.00 USD | 359.04 USD | `-29.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 9,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 9,590,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 9,580,000.00 USD | 0.00 USD | 172.18 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 9,580,000.00 USD | 0.00 USD | 668.96 USD | `-28.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 9,580,000.00 USD | 0.00 USD | 107.96 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 9,580,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 9,540,000.00 USD | 0.00 USD | 365.32 USD | `-27.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 9,540,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 9,540,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 9,490,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 9,490,000.00 USD | 0.00 USD | 562.80 USD | `-27.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 9,490,000.00 USD | 0.00 USD | 681.51 USD | `-27.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 9,490,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 9,480,000.00 USD | 0.00 USD | 2,790.00 USD | `-26.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 9,480,000.00 USD | 0.00 USD | 265.02 USD | `-26.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 9,480,000.00 USD | 0.00 USD | 32,440.00 USD | `-26.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 9,450,000.00 USD | 0.00 USD | 289.37 USD | `-26.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.55` | 9,450,000.00 USD | 0.00 USD | 1,170.00 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 9,450,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 9,440,000.00 USD | 0.00 USD | 235.34 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 9,440,000.00 USD | 0.00 USD | 2,300.00 USD | `-25.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 9,440,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 9,420,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 9,410,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 9,340,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 9,330,000.00 USD | 0.00 USD | 733.50 USD | `-24.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 9,330,000.00 USD | 0.00 USD | 139.56 USD | `-24.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 9,330,000.00 USD | 0.00 USD | 510.95 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 9,330,000.00 USD | 0.00 USD | 414.31 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 9,330,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 9,330,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 9,320,000.00 USD | 0.00 USD | 1,820.00 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 9,320,000.00 USD | 0.00 USD | 28,050.00 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 9,290,000.00 USD | 0.00 USD | 30,040.00 USD | `-22.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 9,260,000.00 USD | 0.00 USD | 153.71 USD | `-22.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 9,260,000.00 USD | 0.00 USD | 163.73 USD | `-22.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,260,000.00 USD | 0.00 USD | 2,220.00 USD | `-21.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,260,000.00 USD | 0.00 USD | 277.98 USD | `-21.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,260,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,250,000.00 USD | 0.00 USD | 254.34 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,250,000.00 USD | 0.00 USD | 486.47 USD | `-21.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 9,250,000.00 USD | 0.00 USD | 358.84 USD | `-21.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,250,000.00 USD | 0.00 USD | 4,340.00 USD | `-20.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,240,000.00 USD | 0.00 USD | 536.55 USD | `-20.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,240,000.00 USD | 0.00 USD | 251.74 USD | `-20.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,240,000.00 USD | 0.00 USD | 2,160.00 USD | `-20.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,240,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 9,230,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,230,000.00 USD | 0.00 USD | 155.12 USD | `-19.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,230,000.00 USD | 0.00 USD | 56,850.00 USD | `-19.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,180,000.00 USD | 0.00 USD | 738.52 USD | `-19.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,170,000.00 USD | 0.00 USD | 18,590.00 USD | `-18.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 9,160,000.00 USD | 0.00 USD | 116.40 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 9,160,000.00 USD | 0.00 USD | 379.58 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,160,000.00 USD | 0.00 USD | 5,300.00 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,150,000.00 USD | 0.00 USD | 201.04 USD | `-18.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,150,000.00 USD | 0.00 USD | 2,140.00 USD | `-18.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,150,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,140,000.00 USD | 0.00 USD | 238.95 USD | `-17.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 9,140,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 9,140,000.00 USD | 0.00 USD | 289.06 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,140,000.00 USD | 0.00 USD | 808.29 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,140,000.00 USD | 0.00 USD | 37,100.00 USD | `-17.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 9,100,000.00 USD | 0.00 USD | 8,360.00 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 9,090,000.00 USD | 0.00 USD | 359.97 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 9,090,000.00 USD | 0.00 USD | 8,770.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 9,080,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 9,080,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 9,080,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 9,060,000.00 USD | 0.00 USD | 341.19 USD | `-16.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,060,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 9,060,000.00 USD | 0.00 USD | 959.56 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,060,000.00 USD | 0.00 USD | 5,830.00 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 9,050,000.00 USD | 0.00 USD | 572.48 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,050,000.00 USD | 0.00 USD | 806.70 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 9,050,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 9,050,000.00 USD | 0.00 USD | 818.50 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,050,000.00 USD | 0.00 USD | 70,900.00 USD | `-15.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 8,980,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 8,970,000.00 USD | 0.00 USD | 684.31 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 8,970,000.00 USD | 0.00 USD | 486.92 USD | `-15.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 8,970,000.00 USD | 0.00 USD | 386.22 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 8,970,000.00 USD | 0.00 USD | 3,190.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 8,970,000.00 USD | 0.00 USD | 267,390.00 USD | `-14.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 8,700,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 8,700,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 8,700,000.00 USD | 0.00 USD | 945.63 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 8,690,000.00 USD | 0.00 USD | 310,300.00 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 8,380,000.00 USD | 0.00 USD | 239.47 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 8,380,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 8,370,000.00 USD | 0.00 USD | 168.57 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 8,370,000.00 USD | 0.00 USD | 107,330.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 8,260,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 8,260,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 8,260,000.00 USD | 0.00 USD | 4,550.00 USD | `-13.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 8,250,000.00 USD | 0.00 USD | 33,500.00 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 8,220,000.00 USD | 0.00 USD | 25,220.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 8,190,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 8,190,000.00 USD | 0.00 USD | 965.26 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 8,190,000.00 USD | 0.00 USD | 651.04 USD | `-12.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 8,190,000.00 USD | 0.00 USD | 858.35 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 8,190,000.00 USD | 0.00 USD | 306.80 USD | `-12.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 8,190,000.00 USD | 0.00 USD | 137.62 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 8,190,000.00 USD | 0.00 USD | 236,040.00 USD | `-12.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 7,950,000.00 USD | 0.00 USD | 1,290.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 7,950,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 7,950,000.00 USD | 0.00 USD | 39,110.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 7,910,000.00 USD | 0.00 USD | 120.48 USD | `-11.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 7,910,000.00 USD | 0.00 USD | 105.23 USD | `-11.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 7,910,000.00 USD | 0.00 USD | 310.05 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 7,910,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 7,910,000.00 USD | 0.00 USD | 360.57 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 7,910,000.00 USD | 0.00 USD | 731.43 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 7,910,000.00 USD | 0.00 USD | 13,340.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 7,890,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 7,890,000.00 USD | 0.00 USD | 163.88 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 7,890,000.00 USD | 0.00 USD | 4,080.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 7,890,000.00 USD | 0.00 USD | 1,550.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 7,880,000.00 USD | 0.00 USD | 417.17 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 7,880,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 7,660,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 7,660,000.00 USD | 0.00 USD | 788.60 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 7,660,000.00 USD | 0.00 USD | 132.16 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 7,660,000.00 USD | 0.00 USD | 280,590.00 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,380,000.00 USD | 0.00 USD | 23,550.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,360,000.00 USD | 0.00 USD | 8,200.00 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,350,000.00 USD | 0.00 USD | 127.53 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,350,000.00 USD | 0.00 USD | 730.21 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,350,000.00 USD | 0.00 USD | 7,840.00 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,340,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,340,000.00 USD | 0.00 USD | 131.78 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,340,000.00 USD | 0.00 USD | 104,230.00 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,230,000.00 USD | 0.00 USD | 125,980.00 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 7,110,000.00 USD | 0.00 USD | 2,470.00 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 7,100,000.00 USD | 0.00 USD | 3,070.00 USD | `-8.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 7,100,000.00 USD | 0.00 USD | 38,020.00 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 7,060,000.00 USD | 0.00 USD | 1,100.00 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 7,060,000.00 USD | 0.00 USD | 32,280.00 USD | `-8.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 7,030,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 7,000,000.00 USD | 0.00 USD | 53,390.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 6,950,000.00 USD | 0.00 USD | 91,430.00 USD | `-8.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 6,860,000.00 USD | 0.00 USD | 141.43 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 6,860,000.00 USD | 0.00 USD | 18,290.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 6,840,000.00 USD | 0.00 USD | 6,840.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 6,830,000.00 USD | 0.00 USD | 1,340.00 USD | `-7.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 6,830,000.00 USD | 0.00 USD | 4,360.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 6,830,000.00 USD | 0.00 USD | 5,280.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 6,820,000.00 USD | 0.00 USD | 644.76 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 6,820,000.00 USD | 0.00 USD | 297.64 USD | `-7.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 6,820,000.00 USD | 0.00 USD | 262.97 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 6,820,000.00 USD | 0.00 USD | 17,650.00 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 6,800,000.00 USD | 0.00 USD | 89,440.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 6,710,000.00 USD | 0.00 USD | 2,370,000.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 4,340,000.00 USD | 0.00 USD | 1,250.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 4,340,000.00 USD | 0.00 USD | 12,170.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 4,330,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 4,320,000.00 USD | 0.00 USD | 13,500.00 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 4,310,000.00 USD | 0.00 USD | 75,820.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 4,230,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 4,230,000.00 USD | 0.00 USD | 6,580.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 4,220,000.00 USD | 0.00 USD | 15,580.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 4,210,000.00 USD | 0.00 USD | 642,030.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 3,560,000.00 USD | 0.00 USD | 1,240.00 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 3,560,000.00 USD | 0.00 USD | 6,310.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 3,560,000.00 USD | 0.00 USD | 17,720.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 3,540,000.00 USD | 0.00 USD | 1,800.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 3,540,000.00 USD | 0.00 USD | 451,280.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 3,090,000.00 USD | 0.00 USD | 44,430.00 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 3,040,000.00 USD | 0.00 USD | 5,710.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 3,040,000.00 USD | 0.00 USD | 42,300.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 2,990,000.00 USD | 0.00 USD | 32,120.00 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 2,960,000.00 USD | 0.00 USD | 341,040.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 2,620,000.00 USD | 0.00 USD | 49,960.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 2,570,000.00 USD | 0.00 USD | 2,170.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 2,570,000.00 USD | 0.00 USD | 912,240.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 1,660,000.00 USD | 0.00 USD | 10,200.00 USD | `-4.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 1,650,000.00 USD | 0.00 USD | 17,280.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,630,000.00 USD | 0.00 USD | 51,600.00 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,580,000.00 USD | 0.00 USD | 2,020.00 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,570,000.00 USD | 0.00 USD | 32,500.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,540,000.00 USD | 0.00 USD | 21,710.00 USD | `-4.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,520,000.00 USD | 0.00 USD | 23,030.00 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,500,000.00 USD | 0.00 USD | 136,280.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,360,000.00 USD | 0.00 USD | 50,820.00 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,310,000.00 USD | 0.00 USD | 3,350.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,310,000.00 USD | 0.00 USD | 1,830.00 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,310,000.00 USD | 0.00 USD | 1,510.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,300,000.00 USD | 0.00 USD | 8,670.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,300,000.00 USD | 0.00 USD | 2,340.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,290,000.00 USD | 0.00 USD | 1,570.00 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,290,000.00 USD | 0.00 USD | 3,800.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,290,000.00 USD | 0.00 USD | 401,480.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 885,930.00 USD | 0.00 USD | 15,780.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 870,140.00 USD | 0.00 USD | 7,420.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 862,720.00 USD | 0.00 USD | 2,030.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 860,690.00 USD | 0.00 USD | 53,810.00 USD | `-2.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 806,880.00 USD | 0.00 USD | 10,380.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 796,500.00 USD | 0.00 USD | 12,970.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 783,530.00 USD | 0.00 USD | 20,190.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 763,340.00 USD | 0.00 USD | 9,990.00 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 753,350.00 USD | 0.00 USD | 8,370.00 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 744,980.00 USD | 0.00 USD | 2,980.00 USD | `-1.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 742,000.00 USD | 0.00 USD | 42,510.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 699,490.00 USD | 0.00 USD | 1,470.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 698,010.00 USD | 0.00 USD | 4,370.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 693,650.00 USD | 0.00 USD | 198,270.00 USD | `-1.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 495,370.00 USD | 0.00 USD | 155,200.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 340,180.00 USD | 0.00 USD | 14,790.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 325,390.00 USD | 0.00 USD | 12,880.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 312,510.00 USD | 0.00 USD | 27,520.00 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 284,990.00 USD | 0.00 USD | 8,990.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 276,000.00 USD | 0.00 USD | 19,840.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 256,160.00 USD | 0.00 USD | 1,550.00 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 254,610.00 USD | 0.00 USD | 189,760.00 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 64,840.00 USD | 0.00 USD | 43,540.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 21,300.00 USD | 0.00 USD | 515.04 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 20,780.00 USD | 0.00 USD | 11,410.00 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 9,370.00 USD | 0.00 USD | 1,000.00 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 8,370.00 USD | 0.00 USD | 4,690.00 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 3,670.00 USD | 0.00 USD | 3,670.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.95` | 21,960.00 USD | 21,960.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.05` | 1,400,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.15` | 1,400,000.00 USD | 129.21 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 1,400,000.00 USD | 1,860.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 1,410,000.00 USD | 8,150.00 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 1,440,000.00 USD | 27,330.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 1,450,000.00 USD | 16,490.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 1,460,000.00 USD | 6,510.00 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 1,470,000.00 USD | 5,820.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 1,470,000.00 USD | 2,010.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 1,470,000.00 USD | 996.15 USD | 0.00 USD | `+1.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,930,000.00 USD | 459,820.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 1,930,000.00 USD | 1,260.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 1,940,000.00 USD | 10,780.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 1,950,000.00 USD | 6,420.00 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 2,020,000.00 USD | 71,460.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 2,040,000.00 USD | 19,270.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 2,040,000.00 USD | 600.78 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 2,110,000.00 USD | 75,340.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 2,120,000.00 USD | 5,190.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 2,120,000.00 USD | 4,980.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 2,300,000.00 USD | 172,550.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 2,310,000.00 USD | 11,260.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 2,310,000.00 USD | 191.55 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 2,340,000.00 USD | 27,840.00 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 2,350,000.00 USD | 12,800.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 2,350,000.00 USD | 5,260.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 2,370,000.00 USD | 12,170.00 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 2,370,000.00 USD | 829.92 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 2,370,000.00 USD | 3,980.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 2,410,000.00 USD | 40,120.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 3,800,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 3,810,000.00 USD | 9,920.00 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 3,820,000.00 USD | 4,920.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 3,820,000.00 USD | 266.93 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 3,820,000.00 USD | 2,410.00 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 3,820,000.00 USD | 2,490.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 3,850,000.00 USD | 22,050.00 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 3,850,000.00 USD | 826.15 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 3,850,000.00 USD | 1,540.00 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 3,860,000.00 USD | 9,530.00 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 3,890,000.00 USD | 36,140.00 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 3,900,000.00 USD | 4,670.00 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 3,910,000.00 USD | 7,110.00 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 3,920,000.00 USD | 11,250.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 3,920,000.00 USD | 1,990.00 USD | 0.00 USD | `+4.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 4,290,000.00 USD | 374,470.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 4,290,000.00 USD | 762.38 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 4,300,000.00 USD | 417.17 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 4,300,000.00 USD | 2,210.00 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 4,310,000.00 USD | 7,640.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 5,370,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 5,370,000.00 USD | 2,450.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 5,380,000.00 USD | 7,120.00 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 5,380,000.00 USD | 4,930.00 USD | 0.00 USD | `+5.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 5,390,000.00 USD | 7,280.00 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 5,400,000.00 USD | 11,660.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 5,670,000.00 USD | 265,320.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 5,670,000.00 USD | 1,280.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 5,670,000.00 USD | 4,390.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 5,680,000.00 USD | 5,370.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 5,710,000.00 USD | 35,600.00 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 5,720,000.00 USD | 2,010.00 USD | 0.00 USD | `+6.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 5,780,000.00 USD | 64,080.00 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 5,790,000.00 USD | 4,260.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 5,790,000.00 USD | 3,860.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 5,800,000.00 USD | 6,440.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 5,800,000.00 USD | 2,660.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 5,800,000.00 USD | 611.09 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 6,020,000.00 USD | 218,150.00 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 6,070,000.00 USD | 54,180.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 6,090,000.00 USD | 21,390.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 6,090,000.00 USD | 1,720.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 6,090,000.00 USD | 519.17 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 6,090,000.00 USD | 146.09 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 6,190,000.00 USD | 94,960.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 6,220,000.00 USD | 26,540.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 6,220,000.00 USD | 2,650.00 USD | 0.00 USD | `+8.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 6,220,000.00 USD | 1,900.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 6,230,000.00 USD | 5,900.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 6,250,000.00 USD | 26,100.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 6,300,000.00 USD | 44,180.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 6,330,000.00 USD | 31,990.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 6,330,000.00 USD | 1,010.00 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 6,330,000.00 USD | 1,090.00 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 6,330,000.00 USD | 266.79 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 6,330,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 6,340,000.00 USD | 235.60 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 6,340,000.00 USD | 549.90 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 6,350,000.00 USD | 10,600.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 6,350,000.00 USD | 206.60 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 6,370,000.00 USD | 19,890.00 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 6,370,000.00 USD | 7,080.00 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 6,370,000.00 USD | 758.62 USD | 0.00 USD | `+9.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 6,380,000.00 USD | 7,980.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 6,410,000.00 USD | 26,170.00 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 6,420,000.00 USD | 6,950.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 6,420,000.00 USD | 355.14 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 6,530,000.00 USD | 110,530.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 6,530,000.00 USD | 1,400.00 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 6,530,000.00 USD | 725.12 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 6,670,000.00 USD | 142,930.00 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 6,670,000.00 USD | 1,200.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 6,690,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 6,690,000.00 USD | 698.85 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 6,700,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 6,750,000.00 USD | 52,130.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 6,820,000.00 USD | 65,380.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 6,820,000.00 USD | 536.60 USD | 0.00 USD | `+11.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 6,830,000.00 USD | 11,350.00 USD | 0.00 USD | `+11.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 6,840,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 6,920,000.00 USD | 83,710.00 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 6,990,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 7,000,000.00 USD | 7,140.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 7,000,000.00 USD | 2,580.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 7,010,000.00 USD | 5,430.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 7,010,000.00 USD | 666.02 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 7,010,000.00 USD | 1,030.00 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 7,010,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 7,100,000.00 USD | 92,840.00 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 7,180,000.00 USD | 72,930.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 7,190,000.00 USD | 8,620.00 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 10,790,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 10,820,000.00 USD | 25,320.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 10,820,000.00 USD | 5,880.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 10,830,000.00 USD | 1,070.00 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 10,830,000.00 USD | 5,410.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 10,830,000.00 USD | 1,370.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 10,830,000.00 USD | 1,430.00 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 10,830,000.00 USD | 357.34 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 11,370,000.00 USD | 539,620.00 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 11,380,000.00 USD | 1,030.00 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 11,380,000.00 USD | 3,230.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 11,380,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 11,380,000.00 USD | 1,580.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 11,390,000.00 USD | 10,280.00 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 11,390,000.00 USD | 3,030.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 11,410,000.00 USD | 17,740.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 11,490,000.00 USD | 74,410.00 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 11,560,000.00 USD | 71,520.00 USD | 0.00 USD | `+14.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 11,560,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 11,570,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 11,570,000.00 USD | 585.11 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 11,570,000.00 USD | 852.24 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 11,590,000.00 USD | 22,910.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 11,590,000.00 USD | 2,420.00 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 11,590,000.00 USD | 2,330.00 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 11,610,000.00 USD | 17,800.00 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 11,660,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 11,670,000.00 USD | 4,960.00 USD | 0.00 USD | `+15.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 11,670,000.00 USD | 6,270.00 USD | 0.00 USD | `+15.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 11,670,000.00 USD | 843.38 USD | 0.00 USD | `+16.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 11,710,000.00 USD | 36,280.00 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 11,720,000.00 USD | 6,150.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 11,720,000.00 USD | 586.82 USD | 0.00 USD | `+16.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 11,800,000.00 USD | 78,560.00 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 11,800,000.00 USD | 473.38 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 11,830,000.00 USD | 35,070.00 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 11,830,000.00 USD | 655.74 USD | 0.00 USD | `+17.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 11,840,000.00 USD | 4,470.00 USD | 0.00 USD | `+17.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 11,840,000.00 USD | 395.50 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 11,840,000.00 USD | 257.07 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 11,840,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 11,840,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 11,860,000.00 USD | 11,410.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 11,860,000.00 USD | 907.14 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 11,860,000.00 USD | 740.99 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 11,860,000.00 USD | 343.35 USD | 0.00 USD | `+18.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 11,860,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 11,860,000.00 USD | 105.48 USD | 0.00 USD | `+18.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 11,860,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 11,860,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 11,940,000.00 USD | 79,820.00 USD | 0.00 USD | `+18.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 11,940,000.00 USD | 309.14 USD | 0.00 USD | `+19.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 11,940,000.00 USD | 346.35 USD | 0.00 USD | `+19.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 11,950,000.00 USD | 2,440.00 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 11,950,000.00 USD | 121.54 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 11,950,000.00 USD | 579.25 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 11,950,000.00 USD | 6,180.00 USD | 0.00 USD | `+19.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 11,950,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 11,960,000.00 USD | 1,920.00 USD | 0.00 USD | `+19.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 11,960,000.00 USD | 2,870.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 11,970,000.00 USD | 10,810.00 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 11,970,000.00 USD | 1,100.00 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 11,970,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 11,970,000.00 USD | 234.87 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 11,990,000.00 USD | 12,860.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 11,990,000.00 USD | 3,740.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 11,990,000.00 USD | 584.58 USD | 0.00 USD | `+20.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 11,990,000.00 USD | 1,740.00 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 12,000,000.00 USD | 2,330.00 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 12,110,000.00 USD | 118,690.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 12,220,000.00 USD | 106,330.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 12,230,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 12,280,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 12,350,000.00 USD | 70,920.00 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 12,360,000.00 USD | 3,980.00 USD | 0.00 USD | `+21.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 12,360,000.00 USD | 4,460.00 USD | 0.00 USD | `+22.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 12,360,000.00 USD | 127.82 USD | 0.00 USD | `+22.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 12,360,000.00 USD | 707.15 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 12,360,000.00 USD | 1,260.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 12,370,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 12,370,000.00 USD | 403.75 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 12,380,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 12,430,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 12,490,000.00 USD | 65,030.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 12,500,000.00 USD | 8,120.00 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 12,500,000.00 USD | 1,850.00 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 12,500,000.00 USD | 4,150.00 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 12,510,000.00 USD | 3,580.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 12,510,000.00 USD | 615.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 12,630,000.00 USD | 125,500.00 USD | 0.00 USD | `+23.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 12,670,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 12,670,000.00 USD | 458.21 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 12,850,000.00 USD | 180,350.00 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 12,850,000.00 USD | 414.52 USD | 0.00 USD | `+24.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 12,860,000.00 USD | 3,210.00 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 12,860,000.00 USD | 7,850.00 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 12,860,000.00 USD | 184.29 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 12,870,000.00 USD | 904.13 USD | 0.00 USD | `+24.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 12,870,000.00 USD | 191.83 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 12,870,000.00 USD | 2,150.00 USD | 0.00 USD | `+24.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 12,870,000.00 USD | 663.47 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 12,890,000.00 USD | 20,810.00 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 12,890,000.00 USD | 122.36 USD | 0.00 USD | `+25.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 12,900,000.00 USD | 11,200.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 12,910,000.00 USD | 11,570.00 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 12,920,000.00 USD | 7,860.00 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 12,920,000.00 USD | 2,070.00 USD | 0.00 USD | `+25.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 12,920,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 12,930,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 13,010,000.00 USD | 80,260.00 USD | 0.00 USD | `+25.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 13,200,000.00 USD | 194,050.00 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 13,200,000.00 USD | 1,000.00 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 13,440,000.00 USD | 234,430.00 USD | 0.00 USD | `+26.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 13,490,000.00 USD | 52,330.00 USD | 0.00 USD | `+26.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 13,490,000.00 USD | 3,060.00 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 13,500,000.00 USD | 7,020.00 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 13,510,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 13,510,000.00 USD | 235.68 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 13,510,000.00 USD | 3,850.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 13,530,000.00 USD | 16,430.00 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 14,540,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 14,540,000.00 USD | 252.46 USD | 0.00 USD | `+27.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 14,550,000.00 USD | 7,710.00 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 14,550,000.00 USD | 6,790.00 USD | 0.00 USD | `+27.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 14,560,000.00 USD | 2,670.00 USD | 0.00 USD | `+27.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 14,560,000.00 USD | 632.58 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 14,570,000.00 USD | 15,370.00 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 14,580,000.00 USD | 5,530.00 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 14,600,000.00 USD | 18,470.00 USD | 0.00 USD | `+27.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 14,610,000.00 USD | 11,030.00 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 14,610,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 14,610,000.00 USD | 151.59 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 14,610,000.00 USD | 4,240.00 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 14,620,000.00 USD | 1,370.00 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 14,620,000.00 USD | 9,270.00 USD | 0.00 USD | `+28.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 14,630,000.00 USD | 6,610.00 USD | 0.00 USD | `+28.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 14,630,000.00 USD | 596.78 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 14,640,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 15,190,000.00 USD | 546,780.00 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 15,190,000.00 USD | 603.22 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 15,190,000.00 USD | 311.87 USD | 0.00 USD | `+29.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 15,200,000.00 USD | 6,780.00 USD | 0.00 USD | `+29.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 15,200,000.00 USD | 993.56 USD | 0.00 USD | `+29.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 15,210,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 15,210,000.00 USD | 471.94 USD | 0.00 USD | `+29.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 15,210,000.00 USD | 209.08 USD | 0.00 USD | `+30.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 15,370,000.00 USD | 151,060.00 USD | 0.00 USD | `+30.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 15,370,000.00 USD | 189.23 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 15,370,000.00 USD | 187.15 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 15,370,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 15,380,000.00 USD | 7,460.00 USD | 0.00 USD | `+30.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 15,570,000.00 USD | 190,580.00 USD | 0.00 USD | `+31.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 15,570,000.00 USD | 534.87 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 15,570,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 15,580,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 15,580,000.00 USD | 362.81 USD | 0.00 USD | `+31.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 15,640,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 15,640,000.00 USD | 482.37 USD | 0.00 USD | `+32.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 15,640,000.00 USD | 3,700.00 USD | 0.00 USD | `+32.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 15,650,000.00 USD | 3,010.00 USD | 0.00 USD | `+32.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 15,650,000.00 USD | 191.09 USD | 0.00 USD | `+32.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 15,690,000.00 USD | 41,130.00 USD | 0.00 USD | `+32.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 15,700,000.00 USD | 12,600.00 USD | 0.00 USD | `+33.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 15,750,000.00 USD | 50,720.00 USD | 0.00 USD | `+33.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 15,750,000.00 USD | 229.89 USD | 0.00 USD | `+33.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 15,770,000.00 USD | 15,330.00 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 15,770,000.00 USD | 401.29 USD | 0.00 USD | `+33.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 15,770,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 15,770,000.00 USD | 152.99 USD | 0.00 USD | `+33.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 15,770,000.00 USD | 153.10 USD | 0.00 USD | `+33.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 15,770,000.00 USD | 116.87 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 15,820,000.00 USD | 50,760.00 USD | 0.00 USD | `+34.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 15,820,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 15,820,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 15,820,000.00 USD | 192.06 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 15,830,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 15,830,000.00 USD | 2,620.00 USD | 0.00 USD | `+35.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 15,840,000.00 USD | 10,140.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 15,850,000.00 USD | 6,000.00 USD | 0.00 USD | `+35.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 15,850,000.00 USD | 5,950.00 USD | 0.00 USD | `+35.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 15,860,000.00 USD | 8,820.00 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 15,860,000.00 USD | 135.39 USD | 0.00 USD | `+35.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 16,020,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 16,020,000.00 USD | 144.93 USD | 0.00 USD | `+35.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 16,040,000.00 USD | 12,390.00 USD | 0.00 USD | `+36.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 16,040,000.00 USD | 397.95 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 16,040,000.00 USD | 9,310.00 USD | 0.00 USD | `+37.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 16,050,000.00 USD | 3,910.00 USD | 0.00 USD | `+37.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 16,050,000.00 USD | 267.43 USD | 0.00 USD | `+37.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 16,050,000.00 USD | 509.96 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 16,050,000.00 USD | 191.88 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 16,050,000.00 USD | 237.36 USD | 0.00 USD | `+37.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 16,050,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 16,050,000.00 USD | 192.46 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 16,050,000.00 USD | 112.35 USD | 0.00 USD | `+38.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 16,060,000.00 USD | 4,490.00 USD | 0.00 USD | `+38.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 16,110,000.00 USD | 54,080.00 USD | 0.00 USD | `+38.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 16,110,000.00 USD | 331.60 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 16,380,000.00 USD | 270,270.00 USD | 0.00 USD | `+38.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 16,380,000.00 USD | 668.86 USD | 0.00 USD | `+39.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 16,500,000.00 USD | 116,220.00 USD | 0.00 USD | `+39.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 16,510,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 16,510,000.00 USD | 1,890.00 USD | 0.00 USD | `+40.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 16,510,000.00 USD | 192.25 USD | 0.00 USD | `+40.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 16,510,000.00 USD | 465.29 USD | 0.00 USD | `+40.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 16,510,000.00 USD | 389.17 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 16,510,000.00 USD | 826.57 USD | 0.00 USD | `+41.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 16,510,000.00 USD | 231.61 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 16,510,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 16,520,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 16,540,000.00 USD | 26,260.00 USD | 0.00 USD | `+42.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 16,540,000.00 USD | 133.62 USD | 0.00 USD | `+42.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 16,560,000.00 USD | 18,910.00 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 16,560,000.00 USD | 692.25 USD | 0.00 USD | `+42.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 16,560,000.00 USD | 406.24 USD | 0.00 USD | `+43.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 23,310,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+43.31%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 23,310,000.00 USD | 826.75 USD | 0.00 USD | `+43.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 25,500,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 25,500,000.00 USD | 5,920.00 USD | 0.00 USD | `+44.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 25,630,000.00 USD | 128,430.00 USD | 0.00 USD | `+44.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 25,640,000.00 USD | 12,120.00 USD | 0.00 USD | `+44.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 25,740,000.00 USD | 98,400.00 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 25,740,000.00 USD | 990.88 USD | 0.00 USD | `+45.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 25,760,000.00 USD | 11,640.00 USD | 0.00 USD | `+45.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 25,760,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 25,760,000.00 USD | 796.07 USD | 0.00 USD | `+46.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 25,760,000.00 USD | 826.73 USD | 0.00 USD | `+46.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 25,760,000.00 USD | 278.56 USD | 0.00 USD | `+47.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 26,090,000.00 USD | 329,100.00 USD | 0.00 USD | `+47.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 26,170,000.00 USD | 72,610.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 26,180,000.00 USD | 16,980.00 USD | 0.00 USD | `+47.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 26,180,000.00 USD | 528.96 USD | 0.00 USD | `+47.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 26,190,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 26,190,000.00 USD | 415.44 USD | 0.00 USD | `+48.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 26,470,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 26,480,000.00 USD | 7,260.00 USD | 0.00 USD | `+49.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 26,480,000.00 USD | 791.78 USD | 0.00 USD | `+49.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 26,520,000.00 USD | 36,040.00 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 26,520,000.00 USD | 209.16 USD | 0.00 USD | `+49.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 26,520,000.00 USD | 698.64 USD | 0.00 USD | `+50.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 26,710,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 26,710,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 26,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 26,710,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 26,750,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 26,750,000.00 USD | 844.89 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 26,760,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 26,760,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 28,100,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 28,100,000.00 USD | 1,370.00 USD | 0.00 USD | `+53.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 28,100,000.00 USD | 4,760.00 USD | 0.00 USD | `+53.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 28,100,000.00 USD | 549.99 USD | 0.00 USD | `+53.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 28,610,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 28,870,000.00 USD | 254,780.00 USD | 0.00 USD | `+54.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 28,870,000.00 USD | 1,200.00 USD | 0.00 USD | `+55.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 28,870,000.00 USD | 178.92 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 28,870,000.00 USD | 1,360.00 USD | 0.00 USD | `+55.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 28,890,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 28,890,000.00 USD | 2,000.00 USD | 0.00 USD | `+56.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 28,890,000.00 USD | 411.94 USD | 0.00 USD | `+56.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 28,900,000.00 USD | 10,620.00 USD | 0.00 USD | `+58.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 28,900,000.00 USD | 1,020.00 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 28,910,000.00 USD | 12,000.00 USD | 0.00 USD | `+59.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 28,910,000.00 USD | 113.04 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 28,910,000.00 USD | 1,830.00 USD | 0.00 USD | `+60.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 28,940,000.00 USD | 22,680.00 USD | 0.00 USD | `+60.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 28,950,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 28,960,000.00 USD | 2,230.00 USD | 0.00 USD | `+61.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 28,960,000.00 USD | 6,640.00 USD | 0.00 USD | `+63.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 28,980,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 28,980,000.00 USD | 692.30 USD | 0.00 USD | `+64.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 28,990,000.00 USD | 5,620.00 USD | 0.00 USD | `+65.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 29,070,000.00 USD | 89,040.00 USD | 0.00 USD | `+65.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 29,070,000.00 USD | 281.84 USD | 0.00 USD | `+66.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 29,080,000.00 USD | 4,080.00 USD | 0.00 USD | `+68.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 29,160,000.00 USD | 82,530.00 USD | 0.00 USD | `+70.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 29,160,000.00 USD | 823.94 USD | 0.00 USD | `+70.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 29,160,000.00 USD | 211.39 USD | 0.00 USD | `+71.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 29,160,000.00 USD | 307.19 USD | 0.00 USD | `+72.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 29,160,000.00 USD | 593.03 USD | 0.00 USD | `+72.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 29,160,000.00 USD | 1,440.00 USD | 0.00 USD | `+73.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 29,170,000.00 USD | 5,720.00 USD | 0.00 USD | `+73.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 29,170,000.00 USD | 495.09 USD | 0.00 USD | `+75.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 29,170,000.00 USD | 912.63 USD | 0.00 USD | `+75.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 29,220,000.00 USD | 43,480.00 USD | 0.00 USD | `+75.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 29,220,000.00 USD | 686.20 USD | 0.00 USD | `+77.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 29,250,000.00 USD | 35,280.00 USD | 0.00 USD | `+77.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 29,250,000.00 USD | 703.60 USD | 0.00 USD | `+77.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 29,260,000.00 USD | 3,160.00 USD | 0.00 USD | `+78.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 29,260,000.00 USD | 1,430.00 USD | 0.00 USD | `+80.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 29,310,000.00 USD | 52,520.00 USD | 0.00 USD | `+80.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 29,330,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 29,330,000.00 USD | 1,450.00 USD | 0.00 USD | `+82.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 29,330,000.00 USD | 885.25 USD | 0.00 USD | `+82.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 29,340,000.00 USD | 2,990.00 USD | 0.00 USD | `+84.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 29,340,000.00 USD | 261.56 USD | 0.00 USD | `+84.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 29,420,000.00 USD | 80,290.00 USD | 0.00 USD | `+85.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 29,420,000.00 USD | 2,520.00 USD | 0.00 USD | `+86.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 29,420,000.00 USD | 349.34 USD | 0.00 USD | `+87.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 29,440,000.00 USD | 19,620.00 USD | 0.00 USD | `+88.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 29,990,000.00 USD | 550,350.00 USD | 0.00 USD | `+89.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 30,020,000.00 USD | 29,610.00 USD | 0.00 USD | `+91.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 30,180,000.00 USD | 165,580.00 USD | 0.00 USD | `+93.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 30,330,000.00 USD | 141,190.00 USD | 0.00 USD | `+94.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 30,360,000.00 USD | 35,880.00 USD | 0.00 USD | `+96.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 30,360,000.00 USD | 744.27 USD | 0.00 USD | `+96.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 30,370,000.00 USD | 7,750.00 USD | 0.00 USD | `+96.78%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `86.30` | 101,970,000.00 USD | 0.00 USD | 101,970,000.00 USD | 0.00 USD | 149,300.00 USD | 4,140.00 USD |
| `7D` | `86.50` | 101,810,000.00 USD | 0.00 USD | 101,810,000.00 USD | 0.00 USD | 0.00 USD | 4,340.00 USD |
| `1D` | `86.60` | 80,880,000.00 USD | 0.00 USD | 80,880,000.00 USD | 0.00 USD | 306,270.00 USD | 3,100.00 USD |
| `1D` | `86.80` | 80,570,000.00 USD | 0.00 USD | 80,570,000.00 USD | 0.00 USD | 69,010.00 USD | 4,330.00 USD |
| `7D` | `86.90` | 101,810,000.00 USD | 0.00 USD | 101,810,000.00 USD | 226,670.00 USD | 138,700.00 USD | 0.00 USD |
| `1D` | `87.00` | 80,490,000.00 USD | 0.00 USD | 80,490,000.00 USD | 156,460.00 USD | 243,720.00 USD | 107,550.00 USD |
| `7D` | `87.10` | 101,440,000.00 USD | 0.00 USD | 101,440,000.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD |
| `1D` | `87.20` | 79,980,000.00 USD | 0.00 USD | 79,980,000.00 USD | 54,890.00 USD | 79,810.00 USD | 221,100.00 USD |
| `7D` | `87.30` | 101,440,000.00 USD | 0.00 USD | 101,440,000.00 USD | 0.00 USD | 204,790.00 USD | 288,100.00 USD |
| `1D` | `87.40` | 79,630,000.00 USD | 0.00 USD | 79,630,000.00 USD | 8,750.00 USD | 95,800.00 USD | 40,280.00 USD |
| `7D` | `87.50` | 100,950,000.00 USD | 0.00 USD | 100,950,000.00 USD | 24,350.00 USD | 24,850.00 USD | 0.00 USD |
| `1D` | `87.60` | 79,480,000.00 USD | 0.00 USD | 79,480,000.00 USD | 10,160.00 USD | 50,950.00 USD | 5,580.00 USD |
| `7D` | `87.70` | 100,900,000.00 USD | 0.00 USD | 100,900,000.00 USD | 0.00 USD | 290,940.00 USD | 415,730.00 USD |
| `1D` | `87.80` | 79,420,000.00 USD | 0.00 USD | 79,420,000.00 USD | 22,290.00 USD | 112,630.00 USD | 716,950.00 USD |
| `7D` | `87.90` | 100,190,000.00 USD | 0.00 USD | 100,190,000.00 USD | 0.00 USD | 295,390.00 USD | 0.00 USD |
| `1D` | `88.00` | 78,570,000.00 USD | 0.00 USD | 78,570,000.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD |
| `1D` | `88.60` | 78,080,000.00 USD | 0.00 USD | 78,080,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD |
| `7D` | `88.70` | 99,890,000.00 USD | 0.00 USD | 99,890,000.00 USD | 224,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.80` | 78,070,000.00 USD | 0.00 USD | 78,070,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD |
| `7D` | `88.90` | 99,670,000.00 USD | 0.00 USD | 99,670,000.00 USD | 17,470.00 USD | 3,730.00 USD | 3,570.00 USD |
| `1D` | `89.00` | 77,180,000.00 USD | 0.00 USD | 77,180,000.00 USD | 8,600.00 USD | 2,360.00 USD | 217,430.00 USD |
| `7D` | `89.10` | 99,650,000.00 USD | 0.00 USD | 99,650,000.00 USD | 350,210.00 USD | 291,000.00 USD | 576,850.00 USD |
| `1D` | `89.20` | 76,950,000.00 USD | 0.00 USD | 76,950,000.00 USD | 166,240.00 USD | 99,310.00 USD | 1,410.00 USD |
| `7D` | `89.30` | 98,430,000.00 USD | 0.00 USD | 98,430,000.00 USD | 14,870.00 USD | 7,630.00 USD | 3,920.00 USD |
| `1D` | `89.40` | 76,680,000.00 USD | 0.00 USD | 76,680,000.00 USD | 12,630.00 USD | 93,010.00 USD | 265,240.00 USD |
| `7D` | `89.50` | 98,400,000.00 USD | 0.00 USD | 98,400,000.00 USD | 184,930.00 USD | 91,380.00 USD | 512,480.00 USD |
| `1D` | `89.60` | 76,310,000.00 USD | 0.00 USD | 76,310,000.00 USD | 557,950.00 USD | 163,120.00 USD | 317,090.00 USD |
| `7D` | `89.70` | 97,610,000.00 USD | 0.00 USD | 97,610,000.00 USD | 780,700.00 USD | 190,280.00 USD | 450,090.00 USD |
| `1D` | `89.80` | 75,270,000.00 USD | 0.00 USD | 75,270,000.00 USD | 532,910.00 USD | 381,520.00 USD | 197,340.00 USD |
| `7D` | `89.90` | 96,190,000.00 USD | 0.00 USD | 96,190,000.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `1D` | `90.00` | 74,160,000.00 USD | 0.00 USD | 74,160,000.00 USD | 412,230.00 USD | 479,230.00 USD | 454,010.00 USD |
| `7D` | `90.10` | 94,390,000.00 USD | 0.00 USD | 94,390,000.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `1D` | `90.20` | 72,810,000.00 USD | 0.00 USD | 72,810,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `90.30` | 92,020,000.00 USD | 0.00 USD | 92,020,000.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `1D` | `90.40` | 71,490,000.00 USD | 0.00 USD | 71,490,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `90.50` | 89,940,000.00 USD | 0.00 USD | 89,940,000.00 USD | 1,040,000.00 USD | 785,340.00 USD | 860,530.00 USD |
| `1D` | `90.60` | 70,130,000.00 USD | 0.00 USD | 70,130,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD |
| `7D` | `90.70` | 87,260,000.00 USD | 0.00 USD | 87,260,000.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `1D` | `90.80` | 68,990,000.00 USD | 0.00 USD | 68,990,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `90.90` | 84,810,000.00 USD | 0.00 USD | 84,810,000.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `1D` | `91.00` | 68,780,000.00 USD | 0.00 USD | 68,780,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `91.10` | 82,430,000.00 USD | 0.00 USD | 82,430,000.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `1D` | `91.20` | 68,590,000.00 USD | 0.00 USD | 68,590,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD |
| `7D` | `91.30` | 80,520,000.00 USD | 0.00 USD | 80,520,000.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `1D` | `91.40` | 68,560,000.00 USD | 0.00 USD | 68,560,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD |
| `7D` | `91.50` | 78,020,000.00 USD | 0.00 USD | 78,020,000.00 USD | 705,000.00 USD | 963,570.00 USD | 1,240,000.00 USD |
| `1D` | `91.60` | 68,390,000.00 USD | 0.00 USD | 68,390,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD |
| `7D` | `91.70` | 75,100,000.00 USD | 0.00 USD | 75,100,000.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `1D` | `91.80` | 68,270,000.00 USD | 0.00 USD | 68,270,000.00 USD | 250,490.00 USD | 103,030.00 USD | 525,270.00 USD |
| `7D` | `91.90` | 73,470,000.00 USD | 0.00 USD | 73,470,000.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `1D` | `92.00` | 67,390,000.00 USD | 0.00 USD | 67,390,000.00 USD | 38,300.00 USD | 274,720.00 USD | 87,940.00 USD |
| `7D` | `92.10` | 71,060,000.00 USD | 0.00 USD | 71,060,000.00 USD | 494,450.00 USD | 947,560.00 USD | 258,190.00 USD |
| `1D` | `92.20` | 66,990,000.00 USD | 0.00 USD | 66,990,000.00 USD | 63,310.00 USD | 149,590.00 USD | 32,130.00 USD |
| `7D` | `92.30` | 69,360,000.00 USD | 0.00 USD | 69,360,000.00 USD | 375,130.00 USD | 436,950.00 USD | 1,540,000.00 USD |
| `1D` | `92.40` | 66,740,000.00 USD | 0.00 USD | 66,740,000.00 USD | 117,460.00 USD | 824,620.00 USD | 877,000.00 USD |
| `7D` | `92.50` | 67,000,000.00 USD | 0.00 USD | 67,000,000.00 USD | 259,870.00 USD | 570,240.00 USD | 935,930.00 USD |
| `1D` | `92.60` | 64,920,000.00 USD | 0.00 USD | 64,920,000.00 USD | 377,000.00 USD | 345,060.00 USD | 10,820.00 USD |
| `7D` | `92.70` | 65,240,000.00 USD | 0.00 USD | 65,240,000.00 USD | 718,400.00 USD | 377,890.00 USD | 70,750.00 USD |
| `1D` | `92.80` | 64,190,000.00 USD | 0.00 USD | 64,190,000.00 USD | 26,180.00 USD | 866,290.00 USD | 435,270.00 USD |
| `7D` | `92.90` | 64,070,000.00 USD | 0.00 USD | 64,070,000.00 USD | 0.00 USD | 729,620.00 USD | 0.00 USD |
| `1D` | `93.00` | 62,860,000.00 USD | 0.00 USD | 62,860,000.00 USD | 276,830.00 USD | 262,440.00 USD | 552,740.00 USD |
| `7D` | `93.10` | 63,340,000.00 USD | 0.00 USD | 63,340,000.00 USD | 31,020.00 USD | 630,650.00 USD | 1,000,000.00 USD |
| `1D` | `93.20` | 61,770,000.00 USD | 0.00 USD | 61,770,000.00 USD | 32,310.00 USD | 398,190.00 USD | 100,690.00 USD |
| `7D` | `93.30` | 61,680,000.00 USD | 0.00 USD | 61,680,000.00 USD | 145,070.00 USD | 66,280.00 USD | 468,690.00 USD |
| `1D` | `93.40` | 61,240,000.00 USD | 0.00 USD | 61,240,000.00 USD | 57,590.00 USD | 433,830.00 USD | 141,640.00 USD |
| `7D` | `93.50` | 61,000,000.00 USD | 0.00 USD | 61,000,000.00 USD | 93,960.00 USD | 1,260,000.00 USD | 1,450,000.00 USD |
| `1D` | `93.60` | 60,610,000.00 USD | 0.00 USD | 60,610,000.00 USD | 64,480.00 USD | 472,950.00 USD | 1,790,000.00 USD |
| `7D` | `93.70` | 58,200,000.00 USD | 0.00 USD | 58,200,000.00 USD | 270,240.00 USD | 954,120.00 USD | 120,980.00 USD |
| `1D` | `93.80` | 58,280,000.00 USD | 0.00 USD | 58,280,000.00 USD | 63,080.00 USD | 1,320,000.00 USD | 1,770,000.00 USD |
| `7D` | `93.90` | 56,850,000.00 USD | 0.00 USD | 56,850,000.00 USD | 168,420.00 USD | 56,340.00 USD | 23,050.00 USD |
| `1D` | `94.00` | 55,130,000.00 USD | 0.00 USD | 55,130,000.00 USD | 60,590.00 USD | 86,320.00 USD | 0.00 USD |
| `7D` | `94.10` | 56,610,000.00 USD | 0.00 USD | 56,610,000.00 USD | 233,120.00 USD | 999,200.00 USD | 342,970.00 USD |
| `1D` | `94.20` | 54,980,000.00 USD | 0.00 USD | 54,980,000.00 USD | 0.00 USD | 691,260.00 USD | 702,910.00 USD |
| `7D` | `94.30` | 55,030,000.00 USD | 0.00 USD | 55,030,000.00 USD | 10,610.00 USD | 0.00 USD | 711,670.00 USD |
| `1D` | `94.40` | 53,590,000.00 USD | 0.00 USD | 53,590,000.00 USD | 46,210.00 USD | 1,130,000.00 USD | 15,520.00 USD |
| `7D` | `94.50` | 54,310,000.00 USD | 0.00 USD | 54,310,000.00 USD | 245,400.00 USD | 698,220.00 USD | 140,220.00 USD |
| `1D` | `94.60` | 52,390,000.00 USD | 0.00 USD | 52,390,000.00 USD | 827,670.00 USD | 605,060.00 USD | 2,080,000.00 USD |
| `7D` | `94.70` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,690,000.00 USD | 656,870.00 USD | 0.00 USD |
| `1D` | `94.80` | 48,880,000.00 USD | 0.00 USD | 48,880,000.00 USD | 762,670.00 USD | 3,070,000.00 USD | 1,710,000.00 USD |
| `7D` | `94.90` | 50,870,000.00 USD | 0.00 USD | 50,870,000.00 USD | 1,100,000.00 USD | 3,570,000.00 USD | 0.00 USD |
| `1D` | `95.00` | 43,330,000.00 USD | 0.00 USD | 43,330,000.00 USD | 1,070,000.00 USD | 1,240,000.00 USD | 1,110,000.00 USD |
| `7D` | `95.10` | 46,200,000.00 USD | 0.00 USD | 46,200,000.00 USD | 198,380.00 USD | 1,270,000.00 USD | 2,770,000.00 USD |
| `1D` | `95.20` | 39,900,000.00 USD | 0.00 USD | 39,900,000.00 USD | 99,290.00 USD | 4,070,000.00 USD | 1,600,000.00 USD |
| `7D` | `95.30` | 41,960,000.00 USD | 0.00 USD | 41,960,000.00 USD | 678,330.00 USD | 445,310.00 USD | 838,770.00 USD |
| `1D` | `95.40` | 34,140,000.00 USD | 0.00 USD | 34,140,000.00 USD | 378,280.00 USD | 1,650,000.00 USD | 294,280.00 USD |
| `7D` | `95.50` | 40,000,000.00 USD | 0.00 USD | 40,000,000.00 USD | 1,200,000.00 USD | 3,810,000.00 USD | 2,880,000.00 USD |
| `1D` | `95.60` | 31,820,000.00 USD | 0.00 USD | 31,820,000.00 USD | 2,740,000.00 USD | 2,900,000.00 USD | 4,570,000.00 USD |
| `7D` | `95.70` | 32,110,000.00 USD | 0.00 USD | 32,110,000.00 USD | 4,060,000.00 USD | 4,060,000.00 USD | 10,200.00 USD |
| `1D` | `95.80` | 21,610,000.00 USD | 0.00 USD | 21,610,000.00 USD | 2,310,000.00 USD | 1,930,000.00 USD | 2,910,000.00 USD |
| `7D` | `95.90` | 23,990,000.00 USD | 0.00 USD | 23,990,000.00 USD | 2,130,000.00 USD | 877,200.00 USD | 0.00 USD |
| `1D` | `96.00` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 2,070,000.00 USD | 1,880,000.00 USD | 1,540,000.00 USD |
| `7D` | `96.10` | 20,980,000.00 USD | 0.00 USD | 20,980,000.00 USD | 3,460,000.00 USD | 2,050,000.00 USD | 4,520,000.00 USD |
| `1D` | `96.20` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 1,350,000.00 USD | 847,400.00 USD | 498,740.00 USD |
| `7D` | `96.30` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 1,030,000.00 USD | 2,320,000.00 USD | 5,630,000.00 USD |
| `1D` | `96.40` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 0.00 USD | 2,050,000.00 USD | 3,480,000.00 USD |
| `7D` | `96.50` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD |
| `1D` | `96.60` | 747,550.00 USD | 0.00 USD | 747,550.00 USD | 0.00 USD | 747,550.00 USD | 0.00 USD |
| `7D` | `96.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `96.80` | 4,300.00 USD | 4,300.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 0.00 USD |
| `1D` | `97.00` | 808,780.00 USD | 808,780.00 USD | 0.00 USD | 804,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.20` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 286,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.30` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.40` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 690,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.50` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.60` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 5,180,000.00 USD | 1,410,000.00 USD | 956,940.00 USD |
| `7D` | `97.70` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 7,320,000.00 USD | 2,580,000.00 USD | 0.00 USD |
| `1D` | `97.80` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 5,710,000.00 USD | 724,660.00 USD | 1,470,000.00 USD |
| `7D` | `97.90` | 48,690,000.00 USD | 48,690,000.00 USD | 0.00 USD | 11,920,000.00 USD | 6,740,000.00 USD | 7,770,000.00 USD |
| `1D` | `98.00` | 32,370,000.00 USD | 32,370,000.00 USD | 0.00 USD | 6,540,000.00 USD | 2,650,000.00 USD | 5,940,000.00 USD |
| `7D` | `98.10` | 83,590,000.00 USD | 83,590,000.00 USD | 0.00 USD | 9,820,000.00 USD | 9,540,000.00 USD | 15,550,000.00 USD |
| `1D` | `98.20` | 43,310,000.00 USD | 43,310,000.00 USD | 0.00 USD | 4,120,000.00 USD | 3,690,000.00 USD | 3,140,000.00 USD |
| `7D` | `98.30` | 100,170,000.00 USD | 100,170,000.00 USD | 0.00 USD | 43,030.00 USD | 6,830,000.00 USD | 9,700,000.00 USD |
| `1D` | `98.40` | 56,830,000.00 USD | 56,830,000.00 USD | 0.00 USD | 2,330,000.00 USD | 2,640,000.00 USD | 8,550,000.00 USD |
| `7D` | `98.50` | 106,830,000.00 USD | 106,830,000.00 USD | 0.00 USD | 1,130,000.00 USD | 5,530,000.00 USD | 0.00 USD |
| `1D` | `98.60` | 66,250,000.00 USD | 66,250,000.00 USD | 0.00 USD | 52,360.00 USD | 3,510,000.00 USD | 5,860,000.00 USD |
| `7D` | `98.70` | 108,170,000.00 USD | 108,170,000.00 USD | 0.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD |
| `1D` | `98.80` | 73,890,000.00 USD | 73,890,000.00 USD | 0.00 USD | 553,660.00 USD | 3,030,000.00 USD | 4,050,000.00 USD |
| `7D` | `98.90` | 110,710,000.00 USD | 110,710,000.00 USD | 0.00 USD | 57,310.00 USD | 1,040,000.00 USD | 1,440,000.00 USD |
| `1D` | `99.00` | 75,260,000.00 USD | 75,260,000.00 USD | 0.00 USD | 64,620.00 USD | 1,100,000.00 USD | 202,560.00 USD |
| `7D` | `99.10` | 111,850,000.00 USD | 111,850,000.00 USD | 0.00 USD | 179,190.00 USD | 124,230.00 USD | 838,770.00 USD |
| `1D` | `99.20` | 80,110,000.00 USD | 80,110,000.00 USD | 0.00 USD | 115,180.00 USD | 867,660.00 USD | 3,870,000.00 USD |
| `7D` | `99.30` | 116,980,000.00 USD | 116,980,000.00 USD | 0.00 USD | 0.00 USD | 2,230,000.00 USD | 2,890,000.00 USD |
| `1D` | `99.40` | 84,960,000.00 USD | 84,960,000.00 USD | 0.00 USD | 2,860,000.00 USD | 509,170.00 USD | 1,480,000.00 USD |
| `7D` | `99.50` | 120,720,000.00 USD | 120,720,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,480,000.00 USD | 16,920.00 USD |
| `1D` | `99.60` | 98,960,000.00 USD | 98,960,000.00 USD | 0.00 USD | 1,520,000.00 USD | 5,710,000.00 USD | 6,770,000.00 USD |
| `7D` | `99.70` | 122,730,000.00 USD | 122,730,000.00 USD | 0.00 USD | 0.00 USD | 2,000,000.00 USD | 12,550.00 USD |
| `1D` | `99.80` | 111,860,000.00 USD | 111,860,000.00 USD | 0.00 USD | 2,250,000.00 USD | 3,870,000.00 USD | 6,780,000.00 USD |
| `7D` | `99.90` | 129,880,000.00 USD | 129,880,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,110,000.00 USD | 3,190,000.00 USD |
| `1D` | `100.00` | 117,340,000.00 USD | 117,340,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,770,000.00 USD | 1,630,000.00 USD |
| `7D` | `100.10` | 133,270,000.00 USD | 133,270,000.00 USD | 0.00 USD | 48,160.00 USD | 477,660.00 USD | 2,870,000.00 USD |
| `1D` | `100.20` | 118,200,000.00 USD | 118,200,000.00 USD | 0.00 USD | 23,110.00 USD | 838,950.00 USD | 0.00 USD |
| `7D` | `100.30` | 136,120,000.00 USD | 136,120,000.00 USD | 0.00 USD | 883,050.00 USD | 855,480.00 USD | 1,110,000.00 USD |
| `1D` | `100.40` | 121,990,000.00 USD | 121,990,000.00 USD | 0.00 USD | 377,000.00 USD | 771,420.00 USD | 2,640,000.00 USD |
| `7D` | `100.50` | 143,320,000.00 USD | 143,320,000.00 USD | 0.00 USD | 2,550,000.00 USD | 337,850.00 USD | 4,310,000.00 USD |
| `1D` | `100.60` | 132,120,000.00 USD | 132,120,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,650,000.00 USD | 6,490,000.00 USD |
| `7D` | `100.70` | 145,350,000.00 USD | 145,350,000.00 USD | 0.00 USD | 133,340.00 USD | 1,900,000.00 USD | 0.00 USD |
| `1D` | `100.80` | 137,280,000.00 USD | 137,280,000.00 USD | 0.00 USD | 1,780,000.00 USD | 1,750,000.00 USD | 1,630,000.00 USD |
| `7D` | `100.90` | 158,450,000.00 USD | 158,450,000.00 USD | 0.00 USD | 3,480,000.00 USD | 3,730,000.00 USD | 5,890,000.00 USD |
| `1D` | `101.00` | 148,680,000.00 USD | 148,680,000.00 USD | 0.00 USD | 7,810,000.00 USD | 2,650,000.00 USD | 935,430.00 USD |
| `7D` | `101.10` | 168,220,000.00 USD | 168,220,000.00 USD | 0.00 USD | 3,020,000.00 USD | 3,990,000.00 USD | 2,760,000.00 USD |
| `1D` | `101.20` | 164,990,000.00 USD | 164,990,000.00 USD | 0.00 USD | 5,230,000.00 USD | 6,870,000.00 USD | 4,220,000.00 USD |
| `7D` | `101.30` | 188,780,000.00 USD | 188,780,000.00 USD | 0.00 USD | 7,310,000.00 USD | 4,280,000.00 USD | 8,980,000.00 USD |
| `1D` | `101.40` | 174,900,000.00 USD | 174,900,000.00 USD | 0.00 USD | 3,450,000.00 USD | 2,420,000.00 USD | 4,030,000.00 USD |
| `7D` | `101.50` | 204,050,000.00 USD | 204,050,000.00 USD | 0.00 USD | 2,950,000.00 USD | 738,480.00 USD | 11,580,000.00 USD |
| `1D` | `101.60` | 195,710,000.00 USD | 195,710,000.00 USD | 0.00 USD | 4,700,000.00 USD | 3,450,000.00 USD | 12,660,000.00 USD |
| `7D` | `101.70` | 213,400,000.00 USD | 213,400,000.00 USD | 0.00 USD | 2,950,000.00 USD | 453,970.00 USD | 5,940,000.00 USD |
| `1D` | `101.80` | 202,000,000.00 USD | 202,000,000.00 USD | 0.00 USD | 483,810.00 USD | 381,190.00 USD | 5,430,000.00 USD |
| `7D` | `101.90` | 221,400,000.00 USD | 221,400,000.00 USD | 0.00 USD | 3,710,000.00 USD | 503,680.00 USD | 3,790,000.00 USD |
| `1D` | `102.00` | 206,400,000.00 USD | 206,400,000.00 USD | 0.00 USD | 2,230,000.00 USD | 873,740.00 USD | 1,290,000.00 USD |
| `7D` | `102.10` | 226,050,000.00 USD | 226,050,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 3,180,000.00 USD |
| `1D` | `102.20` | 213,230,000.00 USD | 213,230,000.00 USD | 0.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD |
| `7D` | `102.30` | 232,100,000.00 USD | 232,100,000.00 USD | 0.00 USD | 2,700,000.00 USD | 807,930.00 USD | 2,540,000.00 USD |
| `1D` | `102.40` | 217,810,000.00 USD | 217,810,000.00 USD | 0.00 USD | 1,430,000.00 USD | 579,100.00 USD | 2,570,000.00 USD |
| `7D` | `102.50` | 235,750,000.00 USD | 235,750,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `102.60` | 220,450,000.00 USD | 220,450,000.00 USD | 0.00 USD | 978,360.00 USD | 625,050.00 USD | 1,040,000.00 USD |
| `7D` | `102.70` | 236,520,000.00 USD | 236,520,000.00 USD | 0.00 USD | 766,460.00 USD | 0.00 USD | 7,680.00 USD |
| `1D` | `102.80` | 224,910,000.00 USD | 224,910,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,920,000.00 USD | 1,100,000.00 USD |
| `7D` | `102.90` | 257,810,000.00 USD | 257,810,000.00 USD | 0.00 USD | 17,210,000.00 USD | 294,050.00 USD | 3,780,000.00 USD |
| `1D` | `103.00` | 230,170,000.00 USD | 230,170,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,640,000.00 USD | 498,100.00 USD |
| `7D` | `103.10` | 264,020,000.00 USD | 264,020,000.00 USD | 0.00 USD | 4,750,000.00 USD | 114,550.00 USD | 1,340,000.00 USD |
| `1D` | `103.20` | 233,770,000.00 USD | 233,770,000.00 USD | 0.00 USD | 585,300.00 USD | 1,180,000.00 USD | 1,830,000.00 USD |
| `7D` | `103.30` | 281,590,000.00 USD | 281,590,000.00 USD | 0.00 USD | 17,020,000.00 USD | 133,780.00 USD | 417,110.00 USD |
| `1D` | `103.40` | 238,710,000.00 USD | 238,710,000.00 USD | 0.00 USD | 2,140,000.00 USD | 1,620,000.00 USD | 1,170,000.00 USD |
| `7D` | `103.50` | 304,000,000.00 USD | 304,000,000.00 USD | 0.00 USD | 13,780,000.00 USD | 1,770,000.00 USD | 6,860,000.00 USD |
| `1D` | `103.60` | 249,270,000.00 USD | 249,270,000.00 USD | 0.00 USD | 3,310,000.00 USD | 1,240,000.00 USD | 6,000,000.00 USD |
| `7D` | `103.70` | 316,220,000.00 USD | 316,220,000.00 USD | 0.00 USD | 8,190,000.00 USD | 1,320,000.00 USD | 2,710,000.00 USD |
| `1D` | `103.80` | 256,070,000.00 USD | 256,070,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,510,000.00 USD | 2,010,000.00 USD |
| `7D` | `103.90` | 334,250,000.00 USD | 334,250,000.00 USD | 0.00 USD | 9,120,000.00 USD | 2,880,000.00 USD | 6,040,000.00 USD |
| `1D` | `104.00` | 265,620,000.00 USD | 265,620,000.00 USD | 0.00 USD | 3,550,000.00 USD | 2,790,000.00 USD | 3,220,000.00 USD |
| `7D` | `104.10` | 362,980,000.00 USD | 362,980,000.00 USD | 0.00 USD | 11,570,000.00 USD | 8,150,000.00 USD | 9,010,000.00 USD |
| `1D` | `104.20` | 271,350,000.00 USD | 271,350,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,830,000.00 USD | 1,830,000.00 USD |
| `7D` | `104.30` | 384,360,000.00 USD | 384,360,000.00 USD | 0.00 USD | 7,320,000.00 USD | 6,370,000.00 USD | 7,690,000.00 USD |
| `1D` | `104.40` | 277,250,000.00 USD | 277,250,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,780,000.00 USD | 1,750,000.00 USD |
| `7D` | `104.50` | 396,360,000.00 USD | 396,360,000.00 USD | 0.00 USD | 4,410,000.00 USD | 2,340,000.00 USD | 5,260,000.00 USD |
| `1D` | `104.60` | 282,170,000.00 USD | 282,170,000.00 USD | 0.00 USD | 1,430,000.00 USD | 963,940.00 USD | 2,530,000.00 USD |
| `7D` | `104.70` | 416,360,000.00 USD | 416,360,000.00 USD | 0.00 USD | 6,680,000.00 USD | 4,660,000.00 USD | 8,670,000.00 USD |
| `1D` | `104.80` | 285,970,000.00 USD | 285,970,000.00 USD | 0.00 USD | 948,860.00 USD | 905,680.00 USD | 1,950,000.00 USD |
| `7D` | `104.90` | 436,970,000.00 USD | 436,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 5,090,000.00 USD | 9,550,000.00 USD |
| `1D` | `105.00` | 287,160,000.00 USD | 287,160,000.00 USD | 0.00 USD | 487,580.00 USD | 351,350.00 USD | 350,200.00 USD |
| `7D` | `105.10` | 450,180,000.00 USD | 450,180,000.00 USD | 0.00 USD | 5,580,000.00 USD | 4,800,000.00 USD | 2,830,000.00 USD |
| `1D` | `105.20` | 288,420,000.00 USD | 288,420,000.00 USD | 0.00 USD | 237,100.00 USD | 4,110.00 USD | 1,020,000.00 USD |
| `7D` | `105.30` | 455,170,000.00 USD | 455,170,000.00 USD | 0.00 USD | 2,740,000.00 USD | 1,820,000.00 USD | 428,740.00 USD |
| `1D` | `105.40` | 288,590,000.00 USD | 288,590,000.00 USD | 0.00 USD | 84,970.00 USD | 88,270.00 USD | 769.33 USD |
| `7D` | `105.50` | 474,680,000.00 USD | 474,680,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,170,000.00 USD | 7,740,000.00 USD |
| `1D` | `105.60` | 289,170,000.00 USD | 289,170,000.00 USD | 0.00 USD | 178,510.00 USD | 263,160.00 USD | 135,560.00 USD |
| `7D` | `105.70` | 488,850,000.00 USD | 488,850,000.00 USD | 0.00 USD | 4,560,000.00 USD | 4,340,000.00 USD | 5,270,000.00 USD |
| `1D` | `105.80` | 289,920,000.00 USD | 289,920,000.00 USD | 0.00 USD | 132,310.00 USD | 591,910.00 USD | 22,350.00 USD |
| `7D` | `105.90` | 498,740,000.00 USD | 498,740,000.00 USD | 0.00 USD | 3,680,000.00 USD | 1,870,000.00 USD | 4,340,000.00 USD |
| `1D` | `106.00` | 291,040,000.00 USD | 291,040,000.00 USD | 0.00 USD | 377,210.00 USD | 525,540.00 USD | 226,180.00 USD |
| `7D` | `106.10` | 510,880,000.00 USD | 510,880,000.00 USD | 0.00 USD | 6,090,000.00 USD | 3,080,000.00 USD | 2,960,000.00 USD |
| `1D` | `106.20` | 292,380,000.00 USD | 292,380,000.00 USD | 0.00 USD | 620,980.00 USD | 344,210.00 USD | 367,070.00 USD |
| `7D` | `106.30` | 520,860,000.00 USD | 520,860,000.00 USD | 0.00 USD | 4,770,000.00 USD | 2,990,000.00 USD | 2,230,000.00 USD |
| `1D` | `106.40` | 293,290,000.00 USD | 293,290,000.00 USD | 0.00 USD | 233,950.00 USD | 449,760.00 USD | 233,150.00 USD |
| `7D` | `106.50` | 526,100,000.00 USD | 526,100,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,650,000.00 USD | 1,890,000.00 USD |
| `1D` | `106.60` | 295,110,000.00 USD | 295,110,000.00 USD | 0.00 USD | 445,430.00 USD | 321,480.00 USD | 1,050,000.00 USD |
| `7D` | `106.70` | 535,720,000.00 USD | 535,720,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,870,000.00 USD | 4,470,000.00 USD |
| `1D` | `106.80` | 296,260,000.00 USD | 296,260,000.00 USD | 0.00 USD | 319,360.00 USD | 179,630.00 USD | 649,600.00 USD |
| `7D` | `106.90` | 541,550,000.00 USD | 541,550,000.00 USD | 0.00 USD | 1,220,000.00 USD | 1,150,000.00 USD | 3,470,000.00 USD |
| `1D` | `107.00` | 296,630,000.00 USD | 296,630,000.00 USD | 0.00 USD | 98,730.00 USD | 169,460.00 USD | 95,590.00 USD |
| `7D` | `107.10` | 545,650,000.00 USD | 545,650,000.00 USD | 0.00 USD | 1,630,000.00 USD | 799,480.00 USD | 1,680,000.00 USD |
| `1D` | `107.20` | 297,110,000.00 USD | 297,110,000.00 USD | 0.00 USD | 0.00 USD | 49,040.00 USD | 436,040.00 USD |
| `7D` | `107.30` | 546,100,000.00 USD | 546,100,000.00 USD | 0.00 USD | 0.00 USD | 451,690.00 USD | 0.00 USD |
| `1D` | `107.40` | 297,720,000.00 USD | 297,720,000.00 USD | 0.00 USD | 22,290.00 USD | 63,590.00 USD | 523,690.00 USD |
| `7D` | `107.50` | 547,090,000.00 USD | 547,090,000.00 USD | 0.00 USD | 5,920.00 USD | 274,890.00 USD | 703,710.00 USD |
| `1D` | `107.60` | 298,210,000.00 USD | 298,210,000.00 USD | 0.00 USD | 0.00 USD | 194,840.00 USD | 294,900.00 USD |
| `7D` | `107.70` | 548,060,000.00 USD | 548,060,000.00 USD | 0.00 USD | 523,660.00 USD | 10,400.00 USD | 432,310.00 USD |
| `7D` | `107.90` | 548,230,000.00 USD | 548,230,000.00 USD | 0.00 USD | 173,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.10` | 548,830,000.00 USD | 548,830,000.00 USD | 0.00 USD | 249,450.00 USD | 347,250.00 USD | 5,590.00 USD |
| `7D` | `108.30` | 550,990,000.00 USD | 550,990,000.00 USD | 0.00 USD | 964,640.00 USD | 578,980.00 USD | 612,150.00 USD |
| `7D` | `108.50` | 552,020,000.00 USD | 552,020,000.00 USD | 0.00 USD | 867,380.00 USD | 155,140.00 USD | 9,530.00 USD |
| `7D` | `108.70` | 554,260,000.00 USD | 554,260,000.00 USD | 0.00 USD | 578,660.00 USD | 655,690.00 USD | 1,010,000.00 USD |
| `7D` | `108.90` | 556,310,000.00 USD | 556,310,000.00 USD | 0.00 USD | 646,020.00 USD | 644,300.00 USD | 754,740.00 USD |
| `7D` | `109.10` | 557,390,000.00 USD | 557,390,000.00 USD | 0.00 USD | 434,330.00 USD | 185,250.00 USD | 464,140.00 USD |
| `7D` | `109.30` | 558,550,000.00 USD | 558,550,000.00 USD | 0.00 USD | 503,000.00 USD | 91,380.00 USD | 569,620.00 USD |
| `7D` | `109.50` | 558,790,000.00 USD | 558,790,000.00 USD | 0.00 USD | 230,320.00 USD | 4,290.00 USD | 5,670.00 USD |
| `7D` | `109.70` | 559,980,000.00 USD | 559,980,000.00 USD | 0.00 USD | 550,380.00 USD | 185,990.00 USD | 444,420.00 USD |
| `7D` | `109.90` | 561,780,000.00 USD | 561,780,000.00 USD | 0.00 USD | 446,430.00 USD | 547,840.00 USD | 807,700.00 USD |
| `7D` | `110.10` | 564,150,000.00 USD | 564,150,000.00 USD | 0.00 USD | 967,200.00 USD | 531,910.00 USD | 868,690.00 USD |
| `7D` | `110.30` | 566,230,000.00 USD | 566,230,000.00 USD | 0.00 USD | 936,750.00 USD | 342,020.00 USD | 802,010.00 USD |
| `7D` | `110.50` | 566,710,000.00 USD | 566,710,000.00 USD | 0.00 USD | 246,210.00 USD | 10,300.00 USD | 225,600.00 USD |
| `7D` | `110.70` | 568,910,000.00 USD | 568,910,000.00 USD | 0.00 USD | 793,510.00 USD | 775,040.00 USD | 634,930.00 USD |
| `7D` | `110.90` | 571,360,000.00 USD | 571,360,000.00 USD | 0.00 USD | 742,490.00 USD | 681,670.00 USD | 1,020,000.00 USD |
| `7D` | `111.10` | 573,740,000.00 USD | 573,740,000.00 USD | 0.00 USD | 1,350,000.00 USD | 451,220.00 USD | 577,690.00 USD |
| `7D` | `111.30` | 575,640,000.00 USD | 575,640,000.00 USD | 0.00 USD | 1,020,000.00 USD | 517,490.00 USD | 367,640.00 USD |
| `7D` | `111.50` | 578,150,000.00 USD | 578,150,000.00 USD | 0.00 USD | 1,080,000.00 USD | 810,610.00 USD | 617,520.00 USD |
| `7D` | `111.70` | 579,290,000.00 USD | 579,290,000.00 USD | 0.00 USD | 415,950.00 USD | 302,250.00 USD | 423,800.00 USD |
| `7D` | `111.90` | 581,060,000.00 USD | 581,060,000.00 USD | 0.00 USD | 289,050.00 USD | 661,320.00 USD | 819,760.00 USD |
| `7D` | `112.10` | 582,690,000.00 USD | 582,690,000.00 USD | 0.00 USD | 538,680.00 USD | 310,570.00 USD | 781,330.00 USD |
| `7D` | `112.30` | 585,110,000.00 USD | 585,110,000.00 USD | 0.00 USD | 1,020,000.00 USD | 654,890.00 USD | 738,680.00 USD |
| `7D` | `112.50` | 586,420,000.00 USD | 586,420,000.00 USD | 0.00 USD | 494,450.00 USD | 568,250.00 USD | 247,840.00 USD |
| `7D` | `112.70` | 586,940,000.00 USD | 586,940,000.00 USD | 0.00 USD | 82,570.00 USD | 149,860.00 USD | 290,870.00 USD |
| `7D` | `112.90` | 588,430,000.00 USD | 588,430,000.00 USD | 0.00 USD | 292,560.00 USD | 287,090.00 USD | 907,370.00 USD |
| `7D` | `113.10` | 589,830,000.00 USD | 589,830,000.00 USD | 0.00 USD | 238,350.00 USD | 223,480.00 USD | 935,930.00 USD |
| `7D` | `113.30` | 590,100,000.00 USD | 590,100,000.00 USD | 0.00 USD | 151,730.00 USD | 49,460.00 USD | 70,750.00 USD |
| `7D` | `113.50` | 590,160,000.00 USD | 590,160,000.00 USD | 0.00 USD | 0.00 USD | 60,220.00 USD | 0.00 USD |
| `7D` | `113.70` | 590,550,000.00 USD | 590,550,000.00 USD | 0.00 USD | 2,370.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.90` | 590,600,000.00 USD | 590,600,000.00 USD | 0.00 USD | 52,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `114.10` | 590,660,000.00 USD | 590,660,000.00 USD | 0.00 USD | 3,370.00 USD | 4,160.00 USD | 49,310.00 USD |
| `7D` | `114.30` | 590,890,000.00 USD | 590,890,000.00 USD | 0.00 USD | 93,960.00 USD | 135,190.00 USD | 1,290.00 USD |
| `7D` | `114.40` | 591,220,000.00 USD | 591,220,000.00 USD | 0.00 USD | 132,060.00 USD | 82,030.00 USD | 113,160.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.67B` | Total OI Tokens: `58,631,305.2 SOL`
  * 1h OI Change: `-2.66%` | 4h OI Change: `-4.29%` | 24h OI Change: `-9.68%`
  * Exchange Breakdown: Binance=`981.00M` | Bybit=`624.03M` | OKX=`385.25M` | Hyperliquid=`530.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-130.65K` | Last 24h: `286.77K` | Last 3d: `1.17M` | Last 7d: `2.35M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0062%` | **USDT OKX** | `-0.0218%` |
| **USDT Bybit** | `-0.0192%` | **USDT KuCoin** | `-0.0037%` |
| **USDT MEXC** | `0.0061%` | **USDT BingX** | `0.0063%` |
| **USDT Gate** | `-0.0113%` | **USDT Bitget** | `-0.0058%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `56.78%` | `43.22%` | `1.31` | 44,790,000.00 USD |
| `15M` | `Binance` | `52.68%` | `47.32%` | `1.11` | 14,390,000.00 USD |
| `15M` | `OKX` | `58.35%` | `41.65%` | `1.40` | 4,750,000.00 USD |
| `15M` | `Bybit` | `66.93%` | `33.07%` | `2.02` | 7,750,000.00 USD |
| `15M` | `KuCoin` | `44.07%` | `55.93%` | `0.79` | 454,400.00 USD |
| `15M` | `Gate` | `57.61%` | `42.39%` | `1.36` | 1,660,000.00 USD |
| `15M` | `Bitget` | `58.45%` | `41.55%` | `1.41` | 3,330,000.00 USD |
| `15M` | `BingX` | `38.43%` | `61.57%` | `0.62` | 652,950.00 USD |
| `15M` | `MEXC` | `53.58%` | `46.42%` | `1.15` | 7,820,000.00 USD |
| `15M` | `Bitunix` | `48.97%` | `51.03%` | `0.96` | 1,510,000.00 USD |
| `15M` | `Hyperliquid` | `46.58%` | `53.42%` | `0.87` | 1,260,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `63.54%` | `36.46%` | `1.74` | 98,630.00 USD |
| `15M` | `Crypto.com` | `73.3%` | `26.7%` | `2.75` | 81,660.00 USD |
| `15M` | `WhiteBIT` | `98.45%` | `1.55%` | `63.52` | 699,720.00 USD |
| `15M` | `HTX` | `45.41%` | `54.59%` | `0.83` | 34,550.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `65.06%` | `34.94%` | `1.86` | 285,060.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `64.27%` | `35.73%` | `1.80` | 21,490.00 USD |
| `15M` | `Whale Positions` | `52.68%` | `47.32%` | `1.11` | 14,390,000.00 USD |
| `15M` | `Global Accounts` | `56.78%` | `43.22%` | `1.31` | 44,790,000.00 USD |
| `1H` | `SOL` | `58.70%` | `41.30%` | `1.42` | 164,180,000.00 USD |
| `1H` | `Binance` | `55.29%` | `44.71%` | `1.24` | 55,710,000.00 USD |
| `1H` | `OKX` | `60.97%` | `39.03%` | `1.56` | 17,420,000.00 USD |
| `1H` | `Bybit` | `64.64%` | `35.36%` | `1.83` | 25,540,000.00 USD |
| `1H` | `KuCoin` | `44.15%` | `55.85%` | `0.79` | 1,470,000.00 USD |
| `1H` | `Gate` | `56.97%` | `43.03%` | `1.32` | 7,630,000.00 USD |
| `1H` | `Bitget` | `55.28%` | `44.72%` | `1.24` | 10,220,000.00 USD |
| `1H` | `BingX` | `50.45%` | `49.55%` | `1.02` | 2,460,000.00 USD |
| `1H` | `MEXC` | `54.89%` | `45.11%` | `1.22` | 27,450,000.00 USD |
| `1H` | `Bitunix` | `53.88%` | `46.12%` | `1.17` | 5,040,000.00 USD |
| `1H` | `Hyperliquid` | `74.95%` | `25.05%` | `2.99` | 6,890,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `66.36%` | `33.64%` | `1.97` | 443,710.00 USD |
| `1H` | `Crypto.com` | `61.89%` | `38.11%` | `1.62` | 327,080.00 USD |
| `1H` | `WhiteBIT` | `99.08%` | `0.92%` | `107.70` | 2,430,000.00 USD |
| `1H` | `HTX` | `50.82%` | `49.18%` | `1.03` | 123,150.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `8.78%` | `91.22%` | `0.10` | 1,250.00 USD |
| `1H` | `Aster` | `64.8%` | `35.2%` | `1.84` | 844,480.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.61%` | `52.39%` | `0.91` | 187,870.00 USD |
| `1H` | `Whale Positions` | `55.29%` | `44.71%` | `1.24` | 55,710,000.00 USD |
| `1H` | `Global Accounts` | `58.70%` | `41.30%` | `1.42` | 164,180,000.00 USD |
| `4H` | `SOL` | `49.24%` | `50.76%` | `0.97` | 1,130,000,000.00 USD |
| `4H` | `Binance` | `49.46%` | `50.54%` | `0.98` | 409,550,000.00 USD |
| `4H` | `OKX` | `47.49%` | `52.51%` | `0.90` | 153,140,000.00 USD |
| `4H` | `Bybit` | `48.88%` | `51.12%` | `0.96` | 198,640,000.00 USD |
| `4H` | `KuCoin` | `51.62%` | `48.38%` | `1.07` | 12,480,000.00 USD |
| `4H` | `Gate` | `49.83%` | `50.17%` | `0.99` | 28,380,000.00 USD |
| `4H` | `Bitget` | `50.33%` | `49.67%` | `1.01` | 74,780,000.00 USD |
| `4H` | `BingX` | `47.94%` | `52.06%` | `0.92` | 14,770,000.00 USD |
| `4H` | `MEXC` | `49.66%` | `50.34%` | `0.99` | 111,290,000.00 USD |
| `4H` | `Bitunix` | `51.29%` | `48.71%` | `1.05` | 38,720,000.00 USD |
| `4H` | `Hyperliquid` | `39.06%` | `60.94%` | `0.64` | 51,110,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `59.89%` | `40.11%` | `1.49` | 5,010,000.00 USD |
| `4H` | `Crypto.com` | `43.21%` | `56.79%` | `0.76` | 1,590,000.00 USD |
| `4H` | `WhiteBIT` | `84.98%` | `15.02%` | `5.66` | 13,580,000.00 USD |
| `4H` | `HTX` | `50.96%` | `49.04%` | `1.04` | 1,210,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.81%` | `60.19%` | `0.66` | 4,140,000.00 USD |
| `4H` | `Aster` | `50.3%` | `49.7%` | `1.01` | 8,250,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `55.97%` | `44.03%` | `1.27` | 4,230,000.00 USD |
| `4H` | `Whale Positions` | `49.46%` | `50.54%` | `0.98` | 409,550,000.00 USD |
| `4H` | `Global Accounts` | `49.24%` | `50.76%` | `0.97` | 1,130,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `93.93` | `93.83` | `93.93` | `94.05` | `93.60` | 22,849,238.70 USD | 10,297,736.10 USD | 12,551,502.59 USD | -2,253,766.49 USD | `-9.86%` | `1B / 6S` |
| `0:00 UTC` | `93.50` | `93.91` | `93.50` | `94.47` | `93.47` | 26,611,059.43 USD | 14,151,528.23 USD | 12,459,531.20 USD | 1,691,997.02 USD | `+6.36%` | `19B / 9S` |
| `5:00 UTC` | `95.05` | `94.92` | `95.05` | `95.34` | `94.41` | 30,078,337.49 USD | 16,853,479.29 USD | 13,224,858.20 USD | 3,628,621.09 USD | `+12.06%` | `22B / 6S` |
| `0:00 UTC` | `95.25` | `95.27` | `95.25` | `95.50` | `94.95` | 22,651,518.02 USD | 12,099,960.73 USD | 10,551,557.30 USD | 1,548,403.43 USD | `+6.84%` | `6B / 3S` |
| `5:00 UTC` | `95.22` | `95.22` | `95.22` | `95.45` | `95.02` | 16,191,873.06 USD | 8,476,894.60 USD | 7,714,978.47 USD | 761,916.13 USD | `+4.71%` | `2B / 4S` |
| `0:00 UTC` | `95.75` | `95.74` | `95.75` | `96.00` | `95.32` | 23,940,668.21 USD | 13,099,919.90 USD | 10,840,748.31 USD | 2,259,171.60 USD | `+9.44%` | `14B / 3S` |
| `5:00 UTC` | `95.98` | `95.81` | `95.98` | `96.22` | `95.47` | 14,869,396.80 USD | 8,915,465.93 USD | 5,953,930.88 USD | 2,961,535.05 USD | `+19.92%` | `15B / 4S` |
| `0:00 UTC` | `96.60` | `96.58` | `96.60` | `97.00` | `96.09` | 36,449,738.16 USD | 18,738,925.39 USD | 17,710,812.77 USD | 1,028,112.62 USD | `+2.82%` | `16B / 6S` |
| `5:00 UTC` | `97.05` | `97.07` | `97.05` | `97.23` | `96.88` | 23,273,914.74 USD | 12,919,268.61 USD | 10,354,646.13 USD | 2,564,622.48 USD | `+11.02%` | `2B / 3S` |
| `0:00 UTC` | `97.00` | `96.92` | `97.00` | `97.20` | `96.72` | 27,802,788.20 USD | 15,482,618.69 USD | 12,320,169.51 USD | 3,162,449.19 USD | `+11.37%` | `4B / 6S` |

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
| `5m` | 1,080,000.00 USD | 5,750,000.00 USD | **`ACCUMULATION`** |
| `15m` | 2,110,000.00 USD | 9,830,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,630,000.00 USD | 12,030,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,750,000.00 USD | 30,030,000.00 USD | **`ACCUMULATION`** |
| `2h` | 4,560,000.00 USD | 52,330,000.00 USD | **`ACCUMULATION`** |
| `4h` | 7,350,000.00 USD | -16,290,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -16,940,000.00 USD | -52,200,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -59,220,000.00 USD | -339,740,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -68,110,000.00 USD | -397,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -36,760,000.00 USD | -388,740,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 27,070,000.00 USD | -656,690,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -5,040,000.00 USD | -2,180,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.08M` | 15m=`+2.11M` | 1h=`+2.75M` | 24h=`-36.76M`
* Futures Capital Netflows: 5m=`+5.75M` | 15m=`+9.83M` | 1h=`+30.03M` | 24h=`-388.74M`
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
  * `2026-10-30 09:09:49 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:41:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:43:49 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `94.31` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `92.92` (Risk Distance: `1.39` pts)
  * +2.5R Take Profit: `97.79`
  * Mathematical Lot Sizing: **`7.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `97.54` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `98.93` (Risk Distance: `1.39` pts)
  * +2.5R Take Profit: `94.06`
  * Mathematical Lot Sizing: **`7.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.97`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
