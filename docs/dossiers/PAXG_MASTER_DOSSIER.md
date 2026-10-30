# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 15:05:59 IST` (`2026-10-30 09:35:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3990.81` | **Live Ask Quote**: `3990.90` | **Mid Price**: `3990.86`
- **Spread Points**: `9.00` | **Spread BPS**: `0.23 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `3996.72` | VWAP Z-Score: `-0.64` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.26` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4025.98` | Lower -3.00σ Band: `3967.47`
  * Upper +2.51σ Band: `4021.20` | Lower -2.51σ Band: `3972.25`
  * Upper +2.01σ Band: `4016.32` | Lower -2.01σ Band: `3977.13`
  * Upper +2.00σ Band: `4016.23` | Lower -2.00σ Band: `3977.22`
  * Upper +1.28σ Band: `4009.21` | Lower -1.28σ Band: `3984.24`
  * Upper +1.00σ Band: `4006.48` | Lower -1.00σ Band: `3986.97`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3989.04` | EMA-20=`3990.63` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3999.06` (Slope: `+0.0000`) | EMA-100=`4009.66`
  * Institutional Anchors: EMA-144=`4015.46` | EMA-200=`4020.13` (Slope: `-0.1075`) | EMA-233=`4023.08`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4007.93` (Distance: `-0.42%`)
  * Point of Control (POC) = `3992.63` (Distance: `-0.04%`)
  * Value Area Low (VAL) = `3982.85` (Distance: `+0.21%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4052.58` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`4014.80` | Low=`3966.91`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3974.89` - `4006.82`
  * Optimal Trade Entry (OTE 0.705): `3998.84`
  * Structural Invalidation Anchor (0.786): `4022.78`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3997.44` | `3997.44` | `3994.22` | `3994.50` | `38` | 152,137.63 USD | -15,243.45 USD | `-10.02%` | 94,521.96 USD | `-0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `3994.50` | `3995.85` | `3993.52` | `3994.62` | `21` | 84,104.95 USD | 39,363.29 USD | `+46.80%` | 133,885.24 USD | `+0.08` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `3994.41` | `3995.39` | `3994.41` | `3994.75` | `15` | 60,823.21 USD | -27,673.07 USD | `-45.50%` | 106,212.17 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4001.22` | `4002.41` | `3994.52` | `3995.01` | `197` | 788,106.31 USD | -40,342.52 USD | `-5.12%` | -55,181.95 USD | `-0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `3995.01` | `3998.34` | `3993.52` | `3994.62` | `106` | 425,108.34 USD | 85,150.86 USD | `+20.03%` | 29,968.92 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3994.41` | `3995.39` | `3994.41` | `3994.57` | `16` | 62,812.59 USD | -27,657.09 USD | `-44.03%` | 2,311.83 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `3992.27` | `3994.60` | `3973.63` | `3981.69` | `1,798` | 7,168,194.57 USD | -1,074,302.54 USD | `-14.99%` | -629,444.62 USD | `-2.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3981.68` | `4002.39` | `3979.22` | `4001.26` | `1,541` | 6,150,835.88 USD | 541,833.50 USD | `+8.81%` | -87,611.12 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4001.22` | `4002.41` | `3993.52` | `3994.75` | `319` | 1,275,040.54 USD | 18,137.95 USD | `+1.42%` | -69,473.17 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3994.75` | `1,860` | 7,424,873.74 USD | 558,968.77 USD | `+7.53%` | -19,997.46 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3994.75` | `1,860` | 7,424,873.74 USD | 558,968.77 USD | `+7.53%` | -19,997.46 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `3990.90` | `6.0833` | 24,277.84 USD | 1,362,511.12 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3991.00` | `7.5153` | 29,993.56 USD | 1,338,233.27 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3991.10` | `87.8418` | 350,585.41 USD | 1,308,239.71 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3991.20` | `11.0815` | 44,228.48 USD | 957,654.30 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3991.30` | `3.7581` | 14,999.70 USD | 913,425.82 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3991.40` | `16.8953` | 67,435.90 USD | 898,426.12 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `3991.50` | `12.2961` | 49,079.88 USD | 830,990.22 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3991.60` | `7.9666` | 31,799.48 USD | 781,910.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3991.70` | `54.1535` | 216,164.53 USD | 750,110.85 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3991.80` | `11.2709` | 44,991.18 USD | 533,946.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3991.90` | `31.5410` | 125,908.52 USD | 488,955.15 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `3992.00` | `15.8913` | 63,438.07 USD | 363,046.63 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3992.10` | `3.8018` | 15,177.17 USD | 299,608.56 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3992.20` | `7.5132` | 29,994.20 USD | 284,431.39 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3992.30` | `28.3441` | 113,158.15 USD | 254,437.20 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3992.40` | `18.7835` | 74,991.25 USD | 141,279.05 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3992.50` | `10.5172` | 41,989.92 USD | 66,287.80 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3992.60` | `5.0093` | 20,000.13 USD | 24,297.88 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3992.70` | `1.0396` | 4,150.81 USD | 4,297.75 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3992.90` | `0.0368` | 146.94 USD | 146.94 USD | `1 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3992.95` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,992.95` | `0.00%` | `-` |
| `ASK` | `3993.00` | `19.6345` | 78,400.56 USD | 78,400.56 USD | `13 orders` | `+0.00%` | `-` |
| `ASK` | `3993.20` | `17.9209` | 71,561.74 USD | 149,962.30 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3993.30` | `7.8061` | 31,172.10 USD | 181,134.40 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3993.40` | `32.2297` | 128,706.08 USD | 309,840.48 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `3993.50` | `11.6476` | 46,514.69 USD | 356,355.17 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3993.60` | `64.0462` | 255,774.90 USD | 612,130.07 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3993.70` | `5.1258` | 20,470.91 USD | 632,600.98 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3993.80` | `50.4006` | 201,289.92 USD | 833,890.90 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3993.90` | `0.0471` | 188.11 USD | 834,079.01 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `3994.00` | `37.3673` | 149,245.00 USD | 983,324.01 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3994.10` | `0.4694` | 1,874.83 USD | 985,198.84 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `3994.20` | `2.4005` | 9,588.08 USD | 994,786.91 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3994.30` | `18.9354` | 75,633.67 USD | 1,070,420.58 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3994.40` | `59.8668` | 239,131.95 USD | 1,309,552.53 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3994.50` | `8.8040` | 35,167.58 USD | 1,344,720.11 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3994.60` | `9.3049` | 37,169.35 USD | 1,381,889.46 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3994.70` | `22.1655` | 88,544.52 USD | 1,470,433.98 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `3994.80` | `16.0082` | 63,949.56 USD | 1,534,383.54 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `3994.90` | `24.6596` | 98,512.64 USD | 1,632,896.18 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `3995.00` | `7.4823` | 29,891.79 USD | 1,662,787.97 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:01:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,908,026.39 USD | `6,489.82` | `4185.46` | `3992.20` | `28145.61` | 1,254,924.62 USD | `+4.84%` | `4X Cross` |
| `48` | `0x4692...164f` | `SHORT` | 25,233,475.39 USD | `6,320.69` | `4127.37` | `3992.20` | `14127.47` | 854,413.29 USD | `+3.39%` | `5X Cross` |
| `61` | `0xb83d...6e36` | `SHORT` | 23,442,030.24 USD | `5,869.90` | `4228.86` | `3992.20` | `24588.47` | 1,380,991.69 USD | `+5.89%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,284,722.60 USD | `4,828.91` | `4157.43` | `3992.20` | `2301.76` | -791,159.72 USD | `-4.10%` | `25X Cross` |
| `141` | `0x645b...87b8` | `LONG` | 14,153,824.26 USD | `3,545.72` | `4127.81` | `3992.20` | `648.33` | -482,282.70 USD | `-3.41%` | `3X Cross` |
| `154` | `0x7a6d...f79c` | `SHORT` | 13,046,053.45 USD | `3,268.21` | `4228.94` | `3992.20` | `4380.08` | 775,025.68 USD | `+5.94%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,177,968.62 USD | `2,800.02` | `4364.62` | `3992.20` | `4212.81` | 1,043,075.51 USD | `+9.33%` | `20X Cross` |
| `260` | `0x41e5...0825` | `SHORT` | 8,785,920.00 USD | `2,200.00` | `4112.20` | `3992.20` | `4287.16` | 260,934.59 USD | `+2.97%` | `20X Cross` |
| `261` | `0x3678...b209` | `LONG` | 8,781,740.00 USD | `2,200.00` | `4176.09` | `3992.20` | `2711.12` | -405,679.30 USD | `-4.62%` | `25X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,888,834.04 USD | `1,975.37` | `4048.55` | `3992.20` | `6645.58` | 108,557.68 USD | `+1.38%` | `6X Cross` |
| `363` | `0xc26c...b8f4` | `LONG` | 6,306,851.60 USD | `1,579.95` | `4075.62` | `3992.20` | `0.000000` | -132,445.38 USD | `-2.10%` | `1X Cross` |
| `560` | `0x63da...8add` | `LONG` | 3,991,800.00 USD | `1,000.00` | `4021.46` | `3992.20` | `3564.70` | -29,660.96 USD | `-0.74%` | `25X Cross` |
| `570` | `0xf3dc...1672` | `LONG` | 3,930,094.48 USD | `984.27` | `4018.39` | `3992.20` | `2811.55` | -25,092.22 USD | `-0.64%` | `20X Cross` |
| `589` | `0x9aa5...58af` | `LONG` | 3,875,607.89 USD | `970.45` | `4279.98` | `3992.20` | `0.000000` | -277,919.57 USD | `-7.17%` | `20X Cross` |
| `674` | `0x4a20...3c26` | `LONG` | 3,342,732.12 USD | `837.40` | `4599.73` | `3992.20` | `0.000000` | -509,088.26 USD | `-15.23%` | `20X Cross` |
| `784` | `0x9c06...0560` | `LONG` | 2,902,064.28 USD | `726.95` | `4002.36` | `3992.20` | `0.000000` | -7,464.97 USD | `-0.26%` | `25X Cross` |
| `827` | `0x0fac...7a0a` | `LONG` | 2,741,546.50 USD | `686.49` | `4290.34` | `3992.20` | `1472.23` | -203,712.21 USD | `-7.43%` | `25X Cross` |
| `880` | `0x354b...6425` | `LONG` | 2,522,683.16 USD | `631.90` | `4004.93` | `3992.20` | `0.000000` | -8,047.22 USD | `-0.32%` | `10X Cross` |
| `901` | `0x625e...a354` | `SHORT` | 2,476,032.00 USD | `620.00` | `4122.81` | `3992.20` | `4279.57` | 80,115.03 USD | `+3.24%` | `20X Cross` |
| `926` | `0xeae3...e8ad` | `SHORT` | 2,395,380.00 USD | `600.00` | `4104.77` | `3992.20` | `4268.65` | 67,485.11 USD | `+2.82%` | `20X Cross` |
| `929` | `0xf285...fa82` | `LONG` | 2,388,595.72 USD | `598.11` | `4146.45` | `3992.20` | `3891.83` | -91,423.83 USD | `-3.83%` | `25X Cross` |
| `934` | `0xd8c5...99b0` | `SHORT` | 2,372,486.45 USD | `594.35` | `4175.35` | `3992.20` | `35422.12` | 109,157.58 USD | `+4.60%` | `4X Cross` |
| `941` | `0x12f7...8750` | `LONG` | 2,337,640.79 USD | `585.61` | `4082.77` | `3992.20` | `2782.97` | -53,276.19 USD | `-2.28%` | `10X Cross` |
| `987` | `0x413c...886c` | `LONG` | 2,233,797.47 USD | `559.47` | `4007.05` | `3992.20` | `0.000000` | -8,029.74 USD | `-0.36%` | `2X Cross` |
| `1101` | `0x61ce...a62b` | `SHORT` | 1,986,232.97 USD | `497.50` | `4071.66` | `3992.20` | `4727.51` | 39,435.82 USD | `+1.99%` | `20X Cross` |
| `1179` | `0x2edd...8179` | `LONG` | 1,874,710.58 USD | `469.26` | `4164.68` | `3994.20` | `0.000000` | -79,598.19 USD | `-4.25%` | `10X Cross` |
| `1222` | `0xead5...69f2` | `LONG` | 1,812,231.38 USD | `453.78` | `4220.88` | `3992.20` | `3539.53` | -103,136.68 USD | `-5.69%` | `5X Isolated` |
| `1280` | `0x7a6d...f79c` | `SHORT` | 1,711,416.94 USD | `428.38` | `4136.09` | `3994.20` | `5431.71` | 60,398.06 USD | `+3.53%` | `10X Cross` |
| `1323` | `0x46fc...1195` | `LONG` | 1,637,881.58 USD | `410.28` | `4052.34` | `3992.20` | `2155.19` | -24,717.83 USD | `-1.51%` | `20X Cross` |
| `1352` | `0x6d15...d374` | `LONG` | 1,597,440.00 USD | `400.00` | `4068.25` | `3992.20` | `3842.40` | -29,860.00 USD | `-1.87%` | `25X Cross` |
| `1353` | `0xee02...309d` | `SHORT` | 1,596,840.00 USD | `400.00` | `4438.84` | `3992.20` | `4202.95` | 178,698.60 USD | `+11.19%` | `25X Isolated` |
| `1371` | `0x51f6...2b39` | `LONG` | 1,564,236.64 USD | `391.48` | `4228.25` | `3994.20` | `500.17` | -91,039.05 USD | `-5.82%` | `10X Cross` |
| `1378` | `0x02a7...fe9f` | `SHORT` | 1,556,802.00 USD | `390.00` | `4055.02` | `3992.20` | `4307.27` | 24,657.25 USD | `+1.58%` | `25X Cross` |
| `1432` | `0x7e77...b8d2` | `SHORT` | 1,516,846.00 USD | `380.00` | `4131.92` | `3992.20` | `4294.08` | 53,283.64 USD | `+3.51%` | `20X Cross` |
| `1460` | `0x72c2...9b37` | `LONG` | 1,489,689.40 USD | `373.13` | `4000.98` | `3992.20` | `3778.64` | -3,204.11 USD | `-0.22%` | `13X Isolated` |
| `1473` | `0x781e...96b7` | `SHORT` | 1,461,327.27 USD | `365.84` | `4358.71` | `3994.20` | `13017.26` | 133,280.37 USD | `+9.12%` | `10X Cross` |
| `1497` | `0xaa44...b844` | `LONG` | 1,437,372.00 USD | `360.00` | `4043.10` | `3992.20` | `2817.87` | -18,145.63 USD | `-1.26%` | `4X Cross` |
| `1614` | `0xa41f...d50a` | `LONG` | 1,313,743.04 USD | `328.96` | `4468.89` | `3992.20` | `3802.76` | -156,354.81 USD | `-11.90%` | `15X Cross` |
| `1665` | `0xbf5a...88ba` | `SHORT` | 1,268,586.61 USD | `317.65` | `4091.80` | `3992.20` | `9927.46` | 31,196.42 USD | `+2.46%` | `20X Cross` |
| `1704` | `0xff31...ff6c` | `SHORT` | 1,237,427.00 USD | `310.00` | `4372.43` | `3992.20` | `4789.75` | 118,028.38 USD | `+9.54%` | `10X Isolated` |
| `1730` | `0xada6...6f88` | `LONG` | 1,211,711.39 USD | `303.47` | `4166.46` | `3992.20` | `1793.68` | -52,671.07 USD | `-4.35%` | `5X Cross` |
| `1894` | `0x50e2...d770` | `LONG` | 1,079,225.55 USD | `270.37` | `4243.58` | `3992.20` | `2562.69` | -68,100.91 USD | `-6.31%` | `20X Cross` |
| `1902` | `0x4c92...4f17` | `SHORT` | 1,064,694.89 USD | `266.72` | `4260.98` | `3992.20` | `6497.76` | 71,797.34 USD | `+6.74%` | `20X Cross` |
| `1973` | `0xd346...c4f3` | `LONG` | 1,018,679.33 USD | `255.17` | `4188.66` | `3992.20` | `3311.02` | -50,157.18 USD | `-4.92%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 24.02 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.02K USD at 4002.8000 USD [API] | `2026-10-23 01:55:44` |
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 19.21 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.02K USD at 4002.8000 USD [API] | `2026-10-23 01:55:38` |
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 198.54 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.20K USD at 4002.8000 USD [API] | `2026-10-23 01:55:38` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.56%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.42%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+2.94%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.44%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+2.94%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--1.12%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.31%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.67%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `Long Liquidation` | `3581.80` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3584.40` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3586.00` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.70` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3590.20` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.00` | 15,070,000.00 USD | 15,070,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3594.40` | 5,510,000.00 USD | 5,510,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.30` | 15,060,000.00 USD | 15,060,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.60` | 5,470,000.00 USD | 5,470,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.60` | 14,940,000.00 USD | 14,940,000.00 USD | 165,290.00 USD | 0.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.80` | 5,450,000.00 USD | 5,450,000.00 USD | 36,990.00 USD | 0.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3605.90` | 14,710,000.00 USD | 14,710,000.00 USD | 144,650.00 USD | 0.00 USD | 51,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3607.00` | 5,360,000.00 USD | 5,360,000.00 USD | 48,270.00 USD | 0.00 USD | 14,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.20` | 14,520,000.00 USD | 14,520,000.00 USD | 83,580.00 USD | 0.00 USD | 23,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.20` | 5,290,000.00 USD | 5,290,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.50` | 14,410,000.00 USD | 14,410,000.00 USD | 83,910.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.40` | 5,260,000.00 USD | 5,260,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3618.80` | 14,310,000.00 USD | 14,310,000.00 USD | 45,950.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.60` | 5,220,000.00 USD | 5,220,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.10` | 14,250,000.00 USD | 14,250,000.00 USD | 59,230.00 USD | 0.00 USD | 23,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.80` | 5,170,000.00 USD | 5,170,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.40` | 14,170,000.00 USD | 14,170,000.00 USD | 88,510.00 USD | 0.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.00` | 5,100,000.00 USD | 5,100,000.00 USD | 28,780.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3631.70` | 14,070,000.00 USD | 14,070,000.00 USD | 60,720.00 USD | 0.00 USD | 10,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.20` | 5,070,000.00 USD | 5,070,000.00 USD | 10,830.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.00` | 14,000,000.00 USD | 14,000,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.40` | 5,050,000.00 USD | 5,050,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.30` | 13,970,000.00 USD | 13,970,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.60` | 13,910,000.00 USD | 13,910,000.00 USD | 17,720.00 USD | 0.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3648.90` | 13,880,000.00 USD | 13,880,000.00 USD | 24,860.00 USD | 0.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.20` | 13,850,000.00 USD | 13,850,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 13,820,000.00 USD | 13,820,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.80` | 13,790,000.00 USD | 13,790,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.10` | 13,760,000.00 USD | 13,760,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3821.20` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.20` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3825.40` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.50` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 80,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3829.60` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3833.80` | 4,990,000.00 USD | 4,990,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.80` | 13,640,000.00 USD | 13,640,000.00 USD | 69,040.00 USD | 0.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3838.00` | 4,870,000.00 USD | 4,870,000.00 USD | 38,960.00 USD | 0.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 13,550,000.00 USD | 13,550,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3842.20` | 4,760,000.00 USD | 4,760,000.00 USD | 93,750.00 USD | 0.00 USD | 113,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.40` | 13,220,000.00 USD | 13,220,000.00 USD | 550,160.00 USD | 0.00 USD | 224,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3846.40` | 4,560,000.00 USD | 4,560,000.00 USD | 180,250.00 USD | 0.00 USD | 99,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.70` | 12,450,000.00 USD | 12,450,000.00 USD | 535,270.00 USD | 0.00 USD | 157,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3850.60` | 4,280,000.00 USD | 4,280,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.00` | 11,750,000.00 USD | 11,750,000.00 USD | 240,120.00 USD | 0.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.80` | 4,200,000.00 USD | 4,200,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.30` | 11,440,000.00 USD | 11,440,000.00 USD | 180,670.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.00` | 4,060,000.00 USD | 4,060,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.60` | 11,200,000.00 USD | 11,200,000.00 USD | 213,500.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.20` | 3,920,000.00 USD | 3,920,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.90` | 10,970,000.00 USD | 10,970,000.00 USD | 204,130.00 USD | 0.00 USD | 71,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.40` | 3,750,000.00 USD | 3,750,000.00 USD | 182,060.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.20` | 10,690,000.00 USD | 10,690,000.00 USD | 298,110.00 USD | 0.00 USD | 35,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.60` | 3,540,000.00 USD | 3,540,000.00 USD | 106,280.00 USD | 0.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.50` | 10,360,000.00 USD | 10,360,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.80` | 3,420,000.00 USD | 3,420,000.00 USD | 28,070.00 USD | 0.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3876.80` | 10,100,000.00 USD | 10,100,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.00` | 3,390,000.00 USD | 3,390,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.10` | 9,930,000.00 USD | 9,930,000.00 USD | 116,920.00 USD | 0.00 USD | 29,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.40` | 9,780,000.00 USD | 9,780,000.00 USD | 101,210.00 USD | 0.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3889.70` | 9,650,000.00 USD | 9,650,000.00 USD | 108,870.00 USD | 0.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.00` | 9,520,000.00 USD | 9,520,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.30` | 9,380,000.00 USD | 9,380,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.00` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3902.60` | 9,240,000.00 USD | 9,240,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.20` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3906.90` | 9,150,000.00 USD | 9,150,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3909.40` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.20` | 8,990,000.00 USD | 8,990,000.00 USD | 16,550.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3913.60` | 3,250,000.00 USD | 3,250,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.50` | 8,900,000.00 USD | 8,900,000.00 USD | 287,340.00 USD | 0.00 USD | 116,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3917.80` | 3,030,000.00 USD | 3,030,000.00 USD | 55,700.00 USD | 0.00 USD | 142,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3919.80` | 8,490,000.00 USD | 8,490,000.00 USD | 674,750.00 USD | 0.00 USD | 187,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.00` | 2,830,000.00 USD | 2,830,000.00 USD | 187,870.00 USD | 0.00 USD | 214,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.10` | 7,630,000.00 USD | 7,630,000.00 USD | 1,200,000.00 USD | 0.00 USD | 447,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.20` | 2,430,000.00 USD | 2,430,000.00 USD | 382,350.00 USD | 0.00 USD | 211,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.40` | 5,990,000.00 USD | 5,990,000.00 USD | 837,620.00 USD | 0.00 USD | 225,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.40` | 1,830,000.00 USD | 1,830,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3932.70` | 4,920,000.00 USD | 4,920,000.00 USD | 456,560.00 USD | 0.00 USD | 128,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 1,750,000.00 USD | 1,750,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.00` | 4,340,000.00 USD | 4,340,000.00 USD | 418,330.00 USD | 0.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.80` | 1,430,000.00 USD | 1,430,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.30` | 3,840,000.00 USD | 3,840,000.00 USD | 335,530.00 USD | 0.00 USD | 97,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.00` | 1,180,000.00 USD | 1,180,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3945.60` | 3,410,000.00 USD | 3,410,000.00 USD | 438,120.00 USD | 0.00 USD | 116,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.20` | 797,290.00 USD | 797,290.00 USD | 365,110.00 USD | 0.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3949.90` | 2,860,000.00 USD | 2,860,000.00 USD | 559,600.00 USD | 0.00 USD | 87,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.40` | 386,040.00 USD | 386,040.00 USD | 189,460.00 USD | 0.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.20` | 2,210,000.00 USD | 2,210,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.60` | 170,720.00 USD | 170,720.00 USD | 83,380.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.50` | 1,720,000.00 USD | 1,720,000.00 USD | 260,640.00 USD | 0.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.80` | 73,340.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.80` | 1,420,000.00 USD | 1,420,000.00 USD | 292,800.00 USD | 0.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.00` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.10` | 1,070,000.00 USD | 1,070,000.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.40` | 863,560.00 USD | 863,560.00 USD | 170,870.00 USD | 0.00 USD | 38,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.70` | 653,770.00 USD | 653,770.00 USD | 252,970.00 USD | 0.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.00` | 380,310.00 USD | 380,310.00 USD | 265,470.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.30` | 110,560.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3988.60` | 76,450.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4061.70` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.30` | 228,770.00 USD | 228,770.00 USD | 0.00 USD | 0.00 USD | 167,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4074.60` | 483,070.00 USD | 483,070.00 USD | 138,080.00 USD | 0.00 USD | 116,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4077.40` | 532,290.00 USD | 532,290.00 USD | 87,320.00 USD | 0.00 USD | 142,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4078.90` | 1,370,000.00 USD | 1,370,000.00 USD | 773,860.00 USD | 0.00 USD | 117,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4081.60` | 911,030.00 USD | 911,030.00 USD | 178,090.00 USD | 0.00 USD | 200,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.20` | 2,840,000.00 USD | 2,840,000.00 USD | 1,030,000.00 USD | 0.00 USD | 434,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4085.80` | 1,500,000.00 USD | 1,500,000.00 USD | 362,630.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.50` | 4,030,000.00 USD | 4,030,000.00 USD | 922,350.00 USD | 0.00 USD | 266,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.00` | 1,610,000.00 USD | 1,610,000.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4091.80` | 4,640,000.00 USD | 4,640,000.00 USD | 463,860.00 USD | 0.00 USD | 144,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.20` | 1,870,000.00 USD | 1,870,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.10` | 5,090,000.00 USD | 5,090,000.00 USD | 361,330.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.40` | 2,100,000.00 USD | 2,100,000.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.40` | 5,560,000.00 USD | 5,560,000.00 USD | 415,790.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.60` | 2,450,000.00 USD | 2,450,000.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4104.70` | 6,010,000.00 USD | 6,010,000.00 USD | 323,350.00 USD | 0.00 USD | 122,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 2,900,000.00 USD | 2,900,000.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.00` | 6,590,000.00 USD | 6,590,000.00 USD | 493,950.00 USD | 0.00 USD | 88,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.00` | 3,150,000.00 USD | 3,150,000.00 USD | 218,250.00 USD | 0.00 USD | 30,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.30` | 7,170,000.00 USD | 7,170,000.00 USD | 521,450.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.20` | 3,280,000.00 USD | 3,280,000.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4117.60` | 7,510,000.00 USD | 7,510,000.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.40` | 3,350,000.00 USD | 3,350,000.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4121.90` | 7,810,000.00 USD | 7,810,000.00 USD | 272,900.00 USD | 0.00 USD | 29,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.60` | 3,360,000.00 USD | 3,360,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.20` | 8,140,000.00 USD | 8,140,000.00 USD | 252,890.00 USD | 0.00 USD | 73,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.50` | 8,330,000.00 USD | 8,330,000.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4134.80` | 8,610,000.00 USD | 8,610,000.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.10` | 8,820,000.00 USD | 8,820,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.40` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.40` | 9,060,000.00 USD | 9,060,000.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.60` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.70` | 9,210,000.00 USD | 9,210,000.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.80` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.00` | 9,380,000.00 USD | 9,380,000.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.00` | 3,510,000.00 USD | 3,510,000.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.30` | 9,680,000.00 USD | 9,680,000.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4157.20` | 3,620,000.00 USD | 3,620,000.00 USD | 36,330.00 USD | 0.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.60` | 10,060,000.00 USD | 10,060,000.00 USD | 282,940.00 USD | 0.00 USD | 92,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4161.40` | 3,810,000.00 USD | 3,810,000.00 USD | 87,190.00 USD | 0.00 USD | 100,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4164.90` | 10,920,000.00 USD | 10,920,000.00 USD | 628,030.00 USD | 0.00 USD | 233,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4165.60` | 4,100,000.00 USD | 4,100,000.00 USD | 190,490.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.20` | 11,400,000.00 USD | 11,400,000.00 USD | 395,530.00 USD | 0.00 USD | 87,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4169.80` | 4,160,000.00 USD | 4,160,000.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.50` | 11,650,000.00 USD | 11,650,000.00 USD | 181,290.00 USD | 0.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.00` | 4,290,000.00 USD | 4,290,000.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4177.80` | 11,900,000.00 USD | 11,900,000.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.20` | 4,390,000.00 USD | 4,390,000.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.10` | 12,100,000.00 USD | 12,100,000.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.40` | 4,550,000.00 USD | 4,550,000.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.40` | 12,360,000.00 USD | 12,360,000.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.60` | 4,790,000.00 USD | 4,790,000.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.70` | 12,650,000.00 USD | 12,650,000.00 USD | 269,670.00 USD | 0.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.80` | 4,910,000.00 USD | 4,910,000.00 USD | 97,980.00 USD | 0.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.00` | 4,990,000.00 USD | 4,990,000.00 USD | 73,130.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.00` | 12,910,000.00 USD | 12,910,000.00 USD | 220,790.00 USD | 0.00 USD | 38,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.20` | 5,020,000.00 USD | 5,020,000.00 USD | 30,260.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 13,030,000.00 USD | 13,030,000.00 USD | 93,720.00 USD | 0.00 USD | 24,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.40` | 5,040,000.00 USD | 5,040,000.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.60` | 13,210,000.00 USD | 13,210,000.00 USD | 159,550.00 USD | 0.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.90` | 13,340,000.00 USD | 13,340,000.00 USD | 94,830.00 USD | 0.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.20` | 13,450,000.00 USD | 13,450,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.50` | 13,560,000.00 USD | 13,560,000.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.80` | 13,660,000.00 USD | 13,660,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.10` | 13,770,000.00 USD | 13,770,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.40` | 13,820,000.00 USD | 13,820,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4233.70` | 13,870,000.00 USD | 13,870,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.00` | 13,880,000.00 USD | 13,880,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4379.80` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4379.90` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4388.20` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.50` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4392.40` | 5,090,000.00 USD | 5,090,000.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.80` | 13,940,000.00 USD | 13,940,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4396.60` | 5,120,000.00 USD | 5,120,000.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.10` | 14,050,000.00 USD | 14,050,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4400.80` | 5,170,000.00 USD | 5,170,000.00 USD | 26,650.00 USD | 0.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.40` | 14,250,000.00 USD | 14,250,000.00 USD | 139,200.00 USD | 0.00 USD | 56,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4405.00` | 5,260,000.00 USD | 5,260,000.00 USD | 51,120.00 USD | 0.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4405.50` | 5,260,000.00 USD | 5,260,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.70` | 14,420,000.00 USD | 14,420,000.00 USD | 120,640.00 USD | 0.00 USD | 53,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.00` | 14,560,000.00 USD | 14,560,000.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.30` | 14,610,000.00 USD | 14,610,000.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4418.60` | 14,690,000.00 USD | 14,690,000.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4422.90` | 14,730,000.00 USD | 14,730,000.00 USD | 31,340.00 USD | 0.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4427.20` | 14,810,000.00 USD | 14,810,000.00 USD | 59,230.00 USD | 0.00 USD | 20,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 4,030.00 USD | `Tier 1 CEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `3581.80` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3584.40` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3586.00` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3588.70` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3590.20` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `3593.00` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3594.40` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD |
| `7D` | `3597.30` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3598.60` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `3601.60` | 14,940,000.00 USD | 0.00 USD | 14,940,000.00 USD | 165,290.00 USD | 0.00 USD | 67,670.00 USD |
| `1D` | `3602.80` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 36,990.00 USD | 0.00 USD | 51,100.00 USD |
| `7D` | `3605.90` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 144,650.00 USD | 0.00 USD | 51,230.00 USD |
| `1D` | `3607.00` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 48,270.00 USD | 0.00 USD | 14,630.00 USD |
| `7D` | `3610.20` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 83,580.00 USD | 0.00 USD | 23,490.00 USD |
| `1D` | `3611.20` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3614.50` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 83,910.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3615.40` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD |
| `7D` | `3618.80` | 14,310,000.00 USD | 0.00 USD | 14,310,000.00 USD | 45,950.00 USD | 0.00 USD | 8,780.00 USD |
| `1D` | `3619.60` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `3623.10` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 59,230.00 USD | 0.00 USD | 23,540.00 USD |
| `1D` | `3623.80` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD |
| `7D` | `3627.40` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 88,510.00 USD | 0.00 USD | 10,690.00 USD |
| `1D` | `3628.00` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 28,780.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3631.70` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 60,720.00 USD | 0.00 USD | 10,550.00 USD |
| `1D` | `3632.20` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 10,830.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `3636.00` | 14,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD |
| `1D` | `3636.40` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3640.30` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3644.60` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 17,720.00 USD | 0.00 USD | 10,530.00 USD |
| `7D` | `3648.90` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 24,860.00 USD | 0.00 USD | 5,600.00 USD |
| `7D` | `3653.20` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.50` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.80` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.10` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3821.20` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `3825.20` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3825.40` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `3829.50` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 80,260.00 USD |
| `1D` | `3829.60` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `1D` | `3833.80` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3833.80` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 69,040.00 USD | 0.00 USD | 21,290.00 USD |
| `1D` | `3838.00` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 38,960.00 USD | 0.00 USD | 71,270.00 USD |
| `7D` | `3838.10` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD |
| `1D` | `3842.20` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 93,750.00 USD | 0.00 USD | 113,110.00 USD |
| `7D` | `3842.40` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 550,160.00 USD | 0.00 USD | 224,650.00 USD |
| `1D` | `3846.40` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 180,250.00 USD | 0.00 USD | 99,600.00 USD |
| `7D` | `3846.70` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 535,270.00 USD | 0.00 USD | 157,990.00 USD |
| `1D` | `3850.60` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD |
| `7D` | `3851.00` | 11,750,000.00 USD | 0.00 USD | 11,750,000.00 USD | 240,120.00 USD | 0.00 USD | 79,320.00 USD |
| `1D` | `3854.80` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD |
| `7D` | `3855.30` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 180,670.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3859.00` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD |
| `7D` | `3859.60` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 213,500.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `3863.20` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3863.90` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 204,130.00 USD | 0.00 USD | 71,380.00 USD |
| `1D` | `3867.40` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 182,060.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `3868.20` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 298,110.00 USD | 0.00 USD | 35,750.00 USD |
| `1D` | `3871.60` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 106,280.00 USD | 0.00 USD | 10,390.00 USD |
| `7D` | `3872.50` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD |
| `1D` | `3875.80` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 28,070.00 USD | 0.00 USD | 4,120.00 USD |
| `7D` | `3876.80` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `3880.00` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD |
| `7D` | `3881.10` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 116,920.00 USD | 0.00 USD | 29,790.00 USD |
| `7D` | `3885.40` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 101,210.00 USD | 0.00 USD | 26,150.00 USD |
| `7D` | `3889.70` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 108,870.00 USD | 0.00 USD | 25,820.00 USD |
| `7D` | `3894.00` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD |
| `7D` | `3898.30` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `3901.00` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3902.60` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD |
| `1D` | `3905.20` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `3906.90` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD |
| `1D` | `3909.40` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `3911.20` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 16,550.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3913.60` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `3915.50` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 287,340.00 USD | 0.00 USD | 116,230.00 USD |
| `1D` | `3917.80` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 55,700.00 USD | 0.00 USD | 142,540.00 USD |
| `7D` | `3919.80` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 674,750.00 USD | 0.00 USD | 187,230.00 USD |
| `1D` | `3922.00` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 187,870.00 USD | 0.00 USD | 214,020.00 USD |
| `7D` | `3924.10` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 1,200,000.00 USD | 0.00 USD | 447,120.00 USD |
| `1D` | `3926.20` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 382,350.00 USD | 0.00 USD | 211,410.00 USD |
| `7D` | `3928.40` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 837,620.00 USD | 0.00 USD | 225,440.00 USD |
| `1D` | `3930.40` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD |
| `7D` | `3932.70` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 456,560.00 USD | 0.00 USD | 128,930.00 USD |
| `1D` | `3934.60` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD |
| `7D` | `3937.00` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 418,330.00 USD | 0.00 USD | 74,650.00 USD |
| `1D` | `3938.80` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD |
| `7D` | `3941.30` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 335,530.00 USD | 0.00 USD | 97,220.00 USD |
| `1D` | `3943.00` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD |
| `7D` | `3945.60` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 438,120.00 USD | 0.00 USD | 116,620.00 USD |
| `1D` | `3947.20` | 792,990.00 USD | 0.00 USD | 792,990.00 USD | 365,110.00 USD | 0.00 USD | 46,140.00 USD |
| `7D` | `3949.90` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 559,600.00 USD | 0.00 USD | 87,390.00 USD |
| `1D` | `3951.40` | 381,740.00 USD | 0.00 USD | 381,740.00 USD | 189,460.00 USD | 0.00 USD | 21,560.00 USD |
| `7D` | `3954.20` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3955.60` | 170,720.00 USD | 0.00 USD | 170,720.00 USD | 83,380.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `3958.50` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 260,640.00 USD | 0.00 USD | 38,590.00 USD |
| `1D` | `3959.80` | 73,340.00 USD | 0.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `3962.80` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 292,800.00 USD | 0.00 USD | 56,430.00 USD |
| `1D` | `3964.00` | 606.18 USD | 0.00 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3967.10` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `3971.40` | 863,560.00 USD | 0.00 USD | 863,560.00 USD | 170,870.00 USD | 0.00 USD | 38,920.00 USD |
| `7D` | `3975.70` | 653,770.00 USD | 0.00 USD | 653,770.00 USD | 252,970.00 USD | 0.00 USD | 20,490.00 USD |
| `7D` | `3980.00` | 380,310.00 USD | 0.00 USD | 380,310.00 USD | 265,470.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.30` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3988.60` | 76,450.00 USD | 0.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3994.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3994.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4061.70` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `1D` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `4070.30` | 228,770.00 USD | 228,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167,820.00 USD |
| `1D` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 0.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `4074.60` | 483,070.00 USD | 483,070.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 116,230.00 USD |
| `1D` | `4077.40` | 532,290.00 USD | 532,290.00 USD | 0.00 USD | 87,320.00 USD | 0.00 USD | 142,540.00 USD |
| `7D` | `4078.90` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 773,860.00 USD | 0.00 USD | 117,130.00 USD |
| `1D` | `4081.60` | 911,030.00 USD | 911,030.00 USD | 0.00 USD | 178,090.00 USD | 0.00 USD | 200,660.00 USD |
| `7D` | `4083.20` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 434,880.00 USD |
| `1D` | `4085.80` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 362,630.00 USD | 0.00 USD | 224,770.00 USD |
| `7D` | `4087.50` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 922,350.00 USD | 0.00 USD | 266,230.00 USD |
| `1D` | `4090.00` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD |
| `7D` | `4091.80` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 463,860.00 USD | 0.00 USD | 144,150.00 USD |
| `1D` | `4094.20` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `4096.10` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 361,330.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `4098.40` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `4100.40` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 415,790.00 USD | 0.00 USD | 48,960.00 USD |
| `1D` | `4102.60` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD |
| `7D` | `4104.70` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 323,350.00 USD | 0.00 USD | 122,240.00 USD |
| `1D` | `4106.80` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD |
| `7D` | `4109.00` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 493,950.00 USD | 0.00 USD | 88,940.00 USD |
| `1D` | `4111.00` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 218,250.00 USD | 0.00 USD | 26,100.00 USD |
| `7D` | `4113.30` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 521,450.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4115.20` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `4117.60` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD |
| `1D` | `4119.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `4121.90` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 272,900.00 USD | 0.00 USD | 29,230.00 USD |
| `1D` | `4123.60` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4126.20` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 252,890.00 USD | 0.00 USD | 73,740.00 USD |
| `7D` | `4130.50` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD |
| `7D` | `4134.80` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD |
| `7D` | `4139.10` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4140.40` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4143.40` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD |
| `1D` | `4144.60` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4147.70` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD |
| `1D` | `4148.80` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4152.00` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD |
| `1D` | `4153.00` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `4156.30` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4157.20` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 36,330.00 USD | 0.00 USD | 71,270.00 USD |
| `7D` | `4160.60` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 282,940.00 USD | 0.00 USD | 92,810.00 USD |
| `1D` | `4161.40` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 87,190.00 USD | 0.00 USD | 100,330.00 USD |
| `7D` | `4164.90` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 628,030.00 USD | 0.00 USD | 233,430.00 USD |
| `1D` | `4165.60` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 190,490.00 USD | 0.00 USD | 101,630.00 USD |
| `7D` | `4169.20` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 395,530.00 USD | 0.00 USD | 87,260.00 USD |
| `1D` | `4169.80` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `4173.50` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 181,290.00 USD | 0.00 USD | 64,460.00 USD |
| `1D` | `4174.00` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4177.80` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD |
| `1D` | `4178.20` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD |
| `7D` | `4182.10` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD |
| `1D` | `4182.40` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD |
| `7D` | `4186.40` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD |
| `1D` | `4186.60` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD |
| `7D` | `4190.70` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 269,670.00 USD | 0.00 USD | 24,310.00 USD |
| `1D` | `4190.80` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 97,980.00 USD | 0.00 USD | 14,650.00 USD |
| `1D` | `4195.00` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 73,130.00 USD | 0.00 USD | 7,830.00 USD |
| `7D` | `4195.00` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 220,790.00 USD | 0.00 USD | 38,220.00 USD |
| `1D` | `4199.20` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `4199.30` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 93,720.00 USD | 0.00 USD | 24,830.00 USD |
| `1D` | `4203.40` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4203.60` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 159,550.00 USD | 0.00 USD | 21,260.00 USD |
| `7D` | `4207.90` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 34,680.00 USD |
| `7D` | `4212.20` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.50` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD |
| `7D` | `4220.80` | 13,660,000.00 USD | 13,660,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `7D` | `4225.10` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.40` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4233.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.00` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4379.80` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD |
| `7D` | `4379.90` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4388.20` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `4388.50` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4392.40` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4392.80` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4396.60` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `4397.10` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4400.80` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 26,650.00 USD | 0.00 USD | 23,970.00 USD |
| `7D` | `4401.40` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 139,200.00 USD | 0.00 USD | 56,940.00 USD |
| `1D` | `4405.00` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 51,120.00 USD | 0.00 USD | 39,640.00 USD |
| `1D` | `4405.50` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4405.70` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 120,640.00 USD | 0.00 USD | 53,920.00 USD |
| `7D` | `4410.00` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD |
| `7D` | `4414.30` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD |
| `7D` | `4418.60` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD |
| `7D` | `4422.90` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 31,340.00 USD | 0.00 USD | 7,910.00 USD |
| `7D` | `4427.20` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 20,380.00 USD |
| `7D` | `4428.20` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,030.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.91M` | Total OI Tokens: `68,819.4 PAXG`
  * 1h OI Change: `-0.08%` | 4h OI Change: `-0.46%` | 24h OI Change: `-0.09%`
  * Exchange Breakdown: Binance=`104.97M` | Bybit=`24.26M` | OKX=`-` | Hyperliquid=`24.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.81K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0027%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0027%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0010%` | **USDT Bitget** | `0.0050%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `49.06%` | `50.94%` | `0.96` | 783,970.00 USD |
| `15M` | `Binance` | `53.1%` | `46.9%` | `1.13` | 401,990.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `88.25%` | `11.75%` | `7.51` | 28,420.00 USD |
| `15M` | `KuCoin` | `44.39%` | `55.61%` | `0.80` | 92,470.00 USD |
| `15M` | `Gate` | `62.37%` | `37.63%` | `1.66` | 16,080.00 USD |
| `15M` | `Bitget` | `45.73%` | `54.27%` | `0.84` | 65,530.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `21.82%` | `78.18%` | `0.28` | 6,090.00 USD |
| `15M` | `Bitunix` | `37.05%` | `62.95%` | `0.59` | 8,590.00 USD |
| `15M` | `Hyperliquid` | `81.8%` | `18.2%` | `4.49` | 14,220.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `31.96%` | `68.04%` | `0.47` | 129,270.00 USD |
| `15M` | `HTX` | `46.19%` | `53.81%` | `0.86` | 2,630.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 11,820.00 USD |
| `15M` | `Aster` | `72.4%` | `27.6%` | `2.62` | 2,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 4,860.00 USD |
| `15M` | `Whale Positions` | `53.1%` | `46.9%` | `1.13` | 401,990.00 USD |
| `15M` | `Global Accounts` | `49.06%` | `50.94%` | `0.96` | 783,970.00 USD |
| `1H` | `PAXG` | `52.64%` | `47.36%` | `1.11` | 6,250,000.00 USD |
| `1H` | `Binance` | `55.9%` | `44.1%` | `1.27` | 3,540,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `79.11%` | `20.89%` | `3.79` | 348,780.00 USD |
| `1H` | `KuCoin` | `48.16%` | `51.84%` | `0.93` | 363,950.00 USD |
| `1H` | `Gate` | `48.29%` | `51.71%` | `0.93` | 253,340.00 USD |
| `1H` | `Bitget` | `57.02%` | `42.98%` | `1.33` | 687,230.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `36.81%` | `63.19%` | `0.58` | 12,220.00 USD |
| `1H` | `Bitunix` | `53.64%` | `46.36%` | `1.16` | 84,340.00 USD |
| `1H` | `Hyperliquid` | `81.88%` | `18.12%` | `4.52` | 174,700.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.19%` | `91.81%` | `0.09` | 602,900.00 USD |
| `1H` | `HTX` | `46.23%` | `53.77%` | `0.86` | 11,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.12%` | `58.88%` | `0.70` | 72,240.00 USD |
| `1H` | `Aster` | `57.39%` | `42.61%` | `1.35` | 64,670.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `98.19%` | `1.81%` | `54.25` | 29,990.00 USD |
| `1H` | `Whale Positions` | `55.9%` | `44.1%` | `1.27` | 3,540,000.00 USD |
| `1H` | `Global Accounts` | `52.64%` | `47.36%` | `1.11` | 6,250,000.00 USD |
| `4H` | `PAXG` | `49.42%` | `50.58%` | `0.98` | 97,140,000.00 USD |
| `4H` | `Binance` | `46.17%` | `53.83%` | `0.86` | 12,670,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `53.54%` | `46.46%` | `1.15` | 8,330,000.00 USD |
| `4H` | `KuCoin` | `42.7%` | `57.3%` | `0.75` | 572,810.00 USD |
| `4H` | `Gate` | `42.29%` | `57.71%` | `0.73` | 3,410,000.00 USD |
| `4H` | `Bitget` | `46.01%` | `53.99%` | `0.85` | 5,670,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `50.95%` | `49.05%` | `1.04` | 56,740,000.00 USD |
| `4H` | `Bitunix` | `53.59%` | `46.41%` | `1.15` | 2,620,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.55%` | `47.45%` | `1.11` | 5,140,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `6.49%` | `93.51%` | `0.07` | 1,660,000.00 USD |
| `4H` | `HTX` | `49.26%` | `50.74%` | `0.97` | 57,790.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `92.47%` | `7.53%` | `12.28` | 273,940.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `46.17%` | `53.83%` | `0.86` | 12,670,000.00 USD |
| `4H` | `Global Accounts` | `49.42%` | `50.58%` | `0.98` | 97,140,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -23,180.00 USD | 40,590.00 USD | **`ACCUMULATION`** |
| `15m` | -145,490.00 USD | 85,550.00 USD | **`DISTRIBUTION`** |
| `30m` | -222,210.00 USD | 125,710.00 USD | **`DISTRIBUTION`** |
| `1h` | -390,220.00 USD | 759,810.00 USD | **`ACCUMULATION`** |
| `2h` | -1,180,000.00 USD | 613,250.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,660,000.00 USD | -559,020.00 USD | **`DISTRIBUTION`** |
| `6h` | 207,850.00 USD | 288,860.00 USD | **`ACCUMULATION`** |
| `8h` | 66,320.00 USD | -205,970.00 USD | **`DISTRIBUTION`** |
| `12h` | -274,000.00 USD | -408,460.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,110,000.00 USD | 877,620.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,810,000.00 USD | -8,270,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,200,000.00 USD | -71,230,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-23.18K` | 15m=`-145.49K` | 1h=`-390.22K` | 24h=`-1.11M`
* Futures Capital Netflows: 5m=`+40.59K` | 15m=`+85.55K` | 1h=`+759.81K` | 24h=`+877.62K`
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
  * `2026-10-30 14:41:20 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:20 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3982.85` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3972.80` (Risk Distance: `10.05` pts)
  * +2.5R Take Profit: `4007.97`
  * Mathematical Lot Sizing: **`0.99 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.98` (Risk Distance: `10.05` pts)
  * +2.5R Take Profit: `3982.81`
  * Mathematical Lot Sizing: **`0.99 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4022.78`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
