# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 14:35:45 IST` (`2026-10-30 09:05:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3997.25` | **Live Ask Quote**: `3997.34` | **Mid Price**: `3997.30`
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
  * Session VWAP: `3996.92` | VWAP Z-Score: `+0.03` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.51` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.70` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4026.72` | Lower -3.00σ Band: `3967.12`
  * Upper +2.51σ Band: `4021.85` | Lower -2.51σ Band: `3971.98`
  * Upper +2.01σ Band: `4016.88` | Lower -2.01σ Band: `3976.95`
  * Upper +2.00σ Band: `4016.79` | Lower -2.00σ Band: `3977.05`
  * Upper +1.28σ Band: `4009.63` | Lower -1.28σ Band: `3984.20`
  * Upper +1.00σ Band: `4006.85` | Lower -1.00σ Band: `3986.98`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3987.99` | EMA-20=`3990.56` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3999.74` (Slope: `+0.0000`) | EMA-100=`4010.41`
  * Institutional Anchors: EMA-144=`4016.11` | EMA-200=`4020.57` (Slope: `-0.1094`) | EMA-233=`4023.42`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.45` (Distance: `-0.43%`)
  * Point of Control (POC) = `4007.08` (Distance: `-0.27%`)
  * Value Area Low (VAL) = `3988.80` (Distance: `+0.18%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4052.58` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`4021.28` | Low=`3973.31`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3981.31` - `4013.28`
  * Optimal Trade Entry (OTE 0.705): `4005.29`
  * Structural Invalidation Anchor (0.786): `4029.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3998.45` | `4002.00` | `3997.01` | `4001.30` | `96` | 382,482.00 USD | -31,947.94 USD | `-8.35%` | 70,722.16 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4001.30` | `4002.39` | `3999.54` | `4001.26` | `81` | 323,317.88 USD | -113,172.60 USD | `-35.00%` | -42,450.44 USD | `-0.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4001.22` | `4002.41` | `4000.30` | `4001.42` | `23` | 92,975.88 USD | -28,857.06 USD | `-31.04%` | -71,307.50 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `3991.23` | `3993.79` | `3990.46` | `3992.75` | `276` | 1,103,245.78 USD | 289,379.88 USD | `+26.23%` | -161,153.27 USD | `+0.97` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `3992.74` | `4002.39` | `3992.40` | `4001.26` | `389` | 1,555,357.21 USD | 201,364.81 USD | `+12.95%` | 40,211.54 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4001.22` | `4002.41` | `4000.30` | `4001.42` | `23` | 92,975.88 USD | -28,857.06 USD | `-31.04%` | 11,354.48 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `3992.27` | `3994.60` | `3973.63` | `3981.69` | `1,798` | 7,168,194.57 USD | -1,074,302.54 USD | `-14.99%` | -629,444.62 USD | `-2.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3981.68` | `4002.39` | `3979.22` | `4001.26` | `1,541` | 6,150,835.88 USD | 541,833.50 USD | `+8.81%` | -87,611.12 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4001.22` | `4002.41` | `4000.30` | `4001.19` | `24` | 94,400.35 USD | -30,281.53 USD | `-32.08%` | -117,892.65 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `4001.42` | `1,564` | 6,243,811.76 USD | 512,976.44 USD | `+8.22%` | -65,989.79 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `4001.42` | `1,564` | 6,243,811.76 USD | 512,976.44 USD | `+8.22%` | -65,989.79 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `3996.20` | `5.4937` | 21,953.92 USD | 1,308,382.84 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3996.30` | `86.7910` | 346,842.87 USD | 1,286,428.92 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3996.40` | `7.5519` | 30,180.41 USD | 939,586.04 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `3996.50` | `12.6639` | 50,611.28 USD | 909,405.63 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `3996.60` | `1.5878` | 6,345.80 USD | 858,794.36 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3996.70` | `7.9699` | 31,853.30 USD | 852,448.55 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3996.80` | `9.7290` | 38,884.87 USD | 820,595.25 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3996.90` | `7.9172` | 31,644.26 USD | 781,710.39 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3997.00` | `70.5550` | 282,008.34 USD | 750,066.13 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3997.10` | `19.2040` | 76,760.31 USD | 468,057.80 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3997.20` | `5.5924` | 22,353.94 USD | 391,297.49 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3997.30` | `11.1004` | 44,371.63 USD | 368,943.55 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3997.40` | `8.1167` | 32,445.70 USD | 324,571.92 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3997.50` | `7.5030` | 29,993.24 USD | 292,126.22 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3997.60` | `12.2221` | 48,859.07 USD | 262,132.98 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `3997.70` | `32.7667` | 130,991.44 USD | 213,273.91 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3997.80` | `0.1347` | 538.50 USD | 82,282.47 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3998.00` | `1.0002` | 3,998.80 USD | 81,743.97 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3998.10` | `10.2742` | 41,077.28 USD | 77,745.17 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `3998.20` | `9.1711` | 36,667.89 USD | 36,667.89 USD | `5 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3998.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,998.25` | `0.00%` | `-` |
| `ASK` | `3998.30` | `2.5166` | 10,062.12 USD | 10,062.12 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `3998.40` | `21.4049` | 85,585.35 USD | 95,647.47 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `3998.50` | `19.2452` | 76,951.93 USD | 172,599.41 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3998.60` | `8.2004` | 32,790.12 USD | 205,389.53 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3998.70` | `61.7925` | 247,089.67 USD | 452,479.20 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3998.90` | `3.7510` | 14,999.87 USD | 467,479.07 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `3999.00` | `10.6884` | 42,742.91 USD | 510,221.98 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3999.10` | `8.3154` | 33,254.12 USD | 543,476.10 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3999.20` | `30.5797` | 122,294.34 USD | 665,770.43 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3999.30` | `22.0174` | 88,054.19 USD | 753,824.62 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3999.40` | `0.8880` | 3,551.47 USD | 757,376.09 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3999.50` | `27.1158` | 108,449.64 USD | 865,825.73 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `3999.60` | `32.9443` | 131,764.02 USD | 997,589.75 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3999.80` | `5.5931` | 22,371.28 USD | 1,019,961.03 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3999.90` | `12.2719` | 49,086.37 USD | 1,069,047.41 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4000.00` | `7.1826` | 28,730.40 USD | 1,097,777.81 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `4000.10` | `56.8933` | 227,578.89 USD | 1,325,356.70 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4000.20` | `12.1680` | 48,674.43 USD | 1,374,031.13 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4000.30` | `3.4193` | 13,678.23 USD | 1,387,709.36 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4000.40` | `7.7001` | 30,803.48 USD | 1,418,512.84 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,946,965.33 USD | `6,489.82` | `4185.46` | `3997.70` | `28909.35` | 1,215,985.68 USD | `+4.69%` | `4X Cross` |
| `48` | `0x4692...164f` | `SHORT` | 25,285,360.65 USD | `6,326.24` | `4127.42` | `3997.70` | `14047.84` | 825,751.73 USD | `+3.27%` | `5X Cross` |
| `62` | `0xb83d...6e36` | `SHORT` | 23,470,205.76 USD | `5,869.90` | `4228.86` | `3997.70` | `26522.83` | 1,352,816.17 USD | `+5.76%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,304,521.11 USD | `4,828.91` | `4157.43` | `3997.70` | `2287.52` | -771,361.20 USD | `-4.00%` | `25X Cross` |
| `141` | `0x645b...87b8` | `LONG` | 14,186,181.16 USD | `3,548.23` | `4127.81` | `3997.70` | `621.12` | -460,269.69 USD | `-3.24%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,066,643.19 USD | `3,268.21` | `4228.94` | `3997.70` | `4375.78` | 754,435.94 USD | `+5.77%` | `25X Cross` |
| `183` | `0xa742...e390` | `SHORT` | 11,194,768.76 USD | `2,800.02` | `4364.62` | `3997.70` | `4212.81` | 1,026,275.38 USD | `+9.17%` | `20X Cross` |
| `262` | `0x41e5...0825` | `SHORT` | 8,796,480.00 USD | `2,200.00` | `4112.20` | `3997.70` | `4287.16` | 250,374.59 USD | `+2.85%` | `20X Cross` |
| `263` | `0x3678...b209` | `LONG` | 8,796,260.00 USD | `2,200.00` | `4176.09` | `3997.70` | `2664.97` | -391,159.30 USD | `-4.45%` | `25X Cross` |
| `303` | `0xacb6...efbd` | `SHORT` | 7,898,118.27 USD | `1,975.37` | `4048.55` | `3997.70` | `6634.49` | 99,273.44 USD | `+1.26%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,316,805.29 USD | `1,579.95` | `4075.62` | `3997.70` | `0.000000` | -122,491.68 USD | `-1.94%` | `1X Cross` |
| `567` | `0x63da...8add` | `LONG` | 3,998,100.00 USD | `1,000.00` | `4021.46` | `3997.70` | `3564.70` | -23,360.96 USD | `-0.58%` | `25X Cross` |
| `579` | `0xf3dc...1672` | `LONG` | 3,936,590.66 USD | `984.27` | `4018.39` | `3997.70` | `2838.58` | -18,596.03 USD | `-0.47%` | `20X Cross` |
| `593` | `0x9aa5...58af` | `LONG` | 3,884,819.04 USD | `971.64` | `4279.98` | `3997.70` | `0.000000` | -273,790.04 USD | `-7.05%` | `20X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,348,175.22 USD | `837.40` | `4599.73` | `3997.70` | `0.000000` | -503,645.16 USD | `-15.04%` | `20X Cross` |
| `788` | `0x9c06...0560` | `LONG` | 2,906,425.99 USD | `726.95` | `4002.36` | `3997.70` | `0.000000` | -3,103.26 USD | `-0.11%` | `25X Cross` |
| `833` | `0x0fac...7a0a` | `LONG` | 2,744,361.08 USD | `686.49` | `4290.34` | `3997.70` | `1359.99` | -200,897.62 USD | `-7.32%` | `25X Cross` |
| `894` | `0x354b...6425` | `LONG` | 2,525,653.10 USD | `631.90` | `4004.93` | `3997.70` | `0.000000` | -5,077.28 USD | `-0.20%` | `10X Cross` |
| `908` | `0x625e...a354` | `SHORT` | 2,479,008.00 USD | `620.00` | `4122.81` | `3997.70` | `4279.57` | 77,139.03 USD | `+3.11%` | `20X Cross` |
| `933` | `0xeae3...e8ad` | `SHORT` | 2,399,700.00 USD | `600.00` | `4104.77` | `3997.70` | `4268.65` | 63,165.11 USD | `+2.63%` | `20X Cross` |
| `938` | `0xf285...fa82` | `LONG` | 2,391,347.01 USD | `598.11` | `4146.45` | `3997.70` | `3891.83` | -88,672.54 USD | `-3.71%` | `25X Cross` |
| `944` | `0xd8c5...99b0` | `SHORT` | 2,376,409.20 USD | `594.35` | `4175.35` | `3997.70` | `35393.59` | 105,234.83 USD | `+4.43%` | `4X Cross` |
| `950` | `0x12f7...8750` | `LONG` | 2,341,330.14 USD | `585.61` | `4082.77` | `3997.70` | `2690.85` | -49,586.84 USD | `-2.12%` | `10X Cross` |
| `997` | `0x413c...886c` | `LONG` | 2,237,601.86 USD | `559.47` | `4007.05` | `3997.70` | `0.000000` | -4,225.34 USD | `-0.19%` | `2X Cross` |
| `1105` | `0x61ce...a62b` | `SHORT` | 1,989,765.25 USD | `497.50` | `4071.66` | `3997.70` | `4723.29` | 35,903.54 USD | `+1.80%` | `20X Cross` |
| `1181` | `0x2edd...8179` | `LONG` | 1,877,295.25 USD | `469.26` | `4164.68` | `3999.80` | `0.000000` | -77,013.52 USD | `-4.10%` | `10X Cross` |
| `1227` | `0xead5...69f2` | `LONG` | 1,814,364.17 USD | `453.78` | `4220.88` | `3997.70` | `3539.53` | -101,003.89 USD | `-5.57%` | `5X Isolated` |
| `1293` | `0x7a6d...f79c` | `SHORT` | 1,713,607.24 USD | `428.38` | `4136.09` | `3999.80` | `5408.34` | 58,207.76 USD | `+3.40%` | `10X Cross` |
| `1310` | `0x46fc...1195` | `LONG` | 1,671,194.82 USD | `417.99` | `4052.43` | `3997.70` | `2163.61` | -22,670.42 USD | `-1.36%` | `20X Cross` |
| `1357` | `0x6d15...d374` | `LONG` | 1,599,360.00 USD | `400.00` | `4068.25` | `3997.70` | `3842.40` | -27,940.00 USD | `-1.75%` | `25X Cross` |
| `1358` | `0xee02...309d` | `SHORT` | 1,599,240.00 USD | `400.00` | `4438.84` | `3997.70` | `4202.95` | 176,298.60 USD | `+11.02%` | `25X Isolated` |
| `1381` | `0x51f6...2b39` | `LONG` | 1,566,507.22 USD | `391.48` | `4228.25` | `3999.80` | `581.45` | -88,768.47 USD | `-5.67%` | `10X Cross` |
| `1405` | `0x02a7...fe9f` | `SHORT` | 1,559,259.00 USD | `390.00` | `4055.02` | `3997.70` | `4307.27` | 22,200.25 USD | `+1.42%` | `25X Cross` |
| `1446` | `0x7e77...b8d2` | `SHORT` | 1,519,810.00 USD | `380.00` | `4131.92` | `3997.70` | `4294.08` | 50,319.64 USD | `+3.31%` | `20X Cross` |
| `1469` | `0x72c2...9b37` | `LONG` | 1,492,338.63 USD | `373.13` | `4000.98` | `3997.70` | `3778.64` | -554.88 USD | `-0.04%` | `13X Isolated` |
| `1484` | `0x781e...96b7` | `SHORT` | 1,463,924.77 USD | `365.84` | `4358.71` | `3999.80` | `12736.18` | 130,682.88 USD | `+8.93%` | `10X Cross` |
| `1504` | `0xaa44...b844` | `LONG` | 1,439,820.00 USD | `360.00` | `4043.10` | `3997.70` | `2815.53` | -15,697.63 USD | `-1.09%` | `4X Cross` |
| `1625` | `0xa41f...d50a` | `LONG` | 1,315,289.16 USD | `328.96` | `4468.89` | `3997.70` | `3802.76` | -154,808.69 USD | `-11.77%` | `15X Cross` |
| `1670` | `0xbf5a...88ba` | `SHORT` | 1,270,047.82 USD | `317.65` | `4091.80` | `3997.70` | `9962.02` | 29,735.21 USD | `+2.34%` | `20X Cross` |
| `1711` | `0xff31...ff6c` | `SHORT` | 1,239,473.00 USD | `310.00` | `4372.43` | `3997.70` | `4789.75` | 115,982.38 USD | `+9.36%` | `10X Isolated` |
| `1740` | `0xada6...6f88` | `LONG` | 1,213,714.27 USD | `303.47` | `4166.46` | `3997.70` | `1780.36` | -50,668.19 USD | `-4.17%` | `5X Cross` |
| `1895` | `0x50e2...d770` | `LONG` | 1,081,009.98 USD | `270.37` | `4243.58` | `3997.70` | `2562.69` | -66,316.49 USD | `-6.13%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,066,375.23 USD | `266.72` | `4260.98` | `3997.70` | `6500.37` | 70,117.01 USD | `+6.58%` | `20X Cross` |
| `1978` | `0xd346...c4f3` | `LONG` | 1,020,210.37 USD | `255.17` | `4188.66` | `3997.70` | `3311.02` | -48,626.14 USD | `-4.77%` | `5X Isolated` |

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
| `1D` | `Long Liquidation` | `3581.80` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3584.30` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3586.00` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.70` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3590.20` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.10` | 15,050,000.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3594.40` | 5,470,000.00 USD | 5,470,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.50` | 15,040,000.00 USD | 15,040,000.00 USD | 99,580.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.60` | 5,430,000.00 USD | 5,430,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.90` | 14,920,000.00 USD | 14,920,000.00 USD | 182,840.00 USD | 0.00 USD | 69,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.80` | 5,410,000.00 USD | 5,410,000.00 USD | 36,990.00 USD | 0.00 USD | 47,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.30` | 14,670,000.00 USD | 14,670,000.00 USD | 152,940.00 USD | 0.00 USD | 52,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3607.00` | 5,320,000.00 USD | 5,320,000.00 USD | 48,270.00 USD | 0.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.70` | 14,460,000.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.20` | 5,260,000.00 USD | 5,260,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.10` | 14,360,000.00 USD | 14,360,000.00 USD | 76,990.00 USD | 0.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.40` | 5,230,000.00 USD | 5,230,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.50` | 14,270,000.00 USD | 14,270,000.00 USD | 45,440.00 USD | 0.00 USD | 15,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.60` | 5,190,000.00 USD | 5,190,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.80` | 5,140,000.00 USD | 5,140,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 14,210,000.00 USD | 14,210,000.00 USD | 55,480.00 USD | 0.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.00` | 5,070,000.00 USD | 5,070,000.00 USD | 28,780.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.30` | 14,130,000.00 USD | 14,130,000.00 USD | 78,160.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.20` | 5,030,000.00 USD | 5,030,000.00 USD | 10,830.00 USD | 0.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 14,040,000.00 USD | 14,040,000.00 USD | 65,870.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.40` | 5,020,000.00 USD | 5,020,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.10` | 13,970,000.00 USD | 13,970,000.00 USD | 25,300.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.50` | 13,940,000.00 USD | 13,940,000.00 USD | 45,790.00 USD | 0.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.90` | 13,880,000.00 USD | 13,880,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3650.30` | 13,850,000.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.70` | 13,830,000.00 USD | 13,830,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3659.10` | 13,770,000.00 USD | 13,770,000.00 USD | 6,820.00 USD | 0.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3663.50` | 13,760,000.00 USD | 13,760,000.00 USD | 12,530.00 USD | 0.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.90` | 13,740,000.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3821.20` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3821.90` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3825.40` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3829.60` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.70` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 84,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3833.80` | 4,950,000.00 USD | 4,950,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3835.10` | 13,620,000.00 USD | 13,620,000.00 USD | 69,040.00 USD | 0.00 USD | 58,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3838.00` | 4,840,000.00 USD | 4,840,000.00 USD | 38,960.00 USD | 0.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.50` | 13,490,000.00 USD | 13,490,000.00 USD | 396,580.00 USD | 0.00 USD | 91,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3842.20` | 4,730,000.00 USD | 4,730,000.00 USD | 93,750.00 USD | 0.00 USD | 109,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.90` | 13,000,000.00 USD | 13,000,000.00 USD | 597,060.00 USD | 0.00 USD | 208,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3846.40` | 4,530,000.00 USD | 4,530,000.00 USD | 180,250.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3848.30` | 12,200,000.00 USD | 12,200,000.00 USD | 436,120.00 USD | 0.00 USD | 112,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3850.60` | 4,260,000.00 USD | 4,260,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.70` | 11,650,000.00 USD | 11,650,000.00 USD | 228,280.00 USD | 0.00 USD | 74,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.80` | 4,190,000.00 USD | 4,190,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3857.10` | 11,350,000.00 USD | 11,350,000.00 USD | 233,200.00 USD | 0.00 USD | 38,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.00` | 4,050,000.00 USD | 4,050,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3861.50` | 11,070,000.00 USD | 11,070,000.00 USD | 174,990.00 USD | 0.00 USD | 58,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.20` | 3,900,000.00 USD | 3,900,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3865.90` | 10,840,000.00 USD | 10,840,000.00 USD | 261,040.00 USD | 0.00 USD | 62,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.40` | 3,730,000.00 USD | 3,730,000.00 USD | 182,060.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3870.30` | 10,520,000.00 USD | 10,520,000.00 USD | 226,450.00 USD | 0.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.60` | 3,530,000.00 USD | 3,530,000.00 USD | 109,480.00 USD | 0.00 USD | 12,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3874.70` | 10,260,000.00 USD | 10,260,000.00 USD | 224,270.00 USD | 0.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.80` | 3,400,000.00 USD | 3,400,000.00 USD | 28,070.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.10` | 10,010,000.00 USD | 10,010,000.00 USD | 122,020.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.00` | 3,370,000.00 USD | 3,370,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3883.50` | 9,870,000.00 USD | 9,870,000.00 USD | 161,950.00 USD | 0.00 USD | 36,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3887.90` | 9,670,000.00 USD | 9,670,000.00 USD | 87,390.00 USD | 0.00 USD | 32,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.30` | 9,550,000.00 USD | 9,550,000.00 USD | 104,620.00 USD | 0.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.70` | 9,430,000.00 USD | 9,430,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.00` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 9,310,000.00 USD | 9,310,000.00 USD | 73,850.00 USD | 0.00 USD | 75,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.20` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.50` | 9,160,000.00 USD | 9,160,000.00 USD | 55,280.00 USD | 0.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3909.40` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.90` | 9,090,000.00 USD | 9,090,000.00 USD | 34,960.00 USD | 0.00 USD | 162,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3913.60` | 3,230,000.00 USD | 3,230,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 8,890,000.00 USD | 8,890,000.00 USD | 138,080.00 USD | 0.00 USD | 40,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3917.80` | 3,000,000.00 USD | 3,000,000.00 USD | 55,700.00 USD | 0.00 USD | 142,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.70` | 8,710,000.00 USD | 8,710,000.00 USD | 763,340.00 USD | 0.00 USD | 199,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.00` | 2,810,000.00 USD | 2,810,000.00 USD | 187,870.00 USD | 0.00 USD | 206,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3923.10` | 7,750,000.00 USD | 7,750,000.00 USD | 1,120,000.00 USD | 0.00 USD | 399,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.20` | 2,410,000.00 USD | 2,410,000.00 USD | 382,350.00 USD | 0.00 USD | 187,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.50` | 6,230,000.00 USD | 6,230,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.40` | 1,840,000.00 USD | 1,840,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.90` | 5,110,000.00 USD | 5,110,000.00 USD | 586,550.00 USD | 0.00 USD | 170,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 1,750,000.00 USD | 1,750,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3936.30` | 4,360,000.00 USD | 4,360,000.00 USD | 418,330.00 USD | 0.00 USD | 95,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.80` | 1,440,000.00 USD | 1,440,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.70` | 3,840,000.00 USD | 3,840,000.00 USD | 335,530.00 USD | 0.00 USD | 70,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.00` | 1,190,000.00 USD | 1,190,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3945.10` | 3,440,000.00 USD | 3,440,000.00 USD | 398,420.00 USD | 0.00 USD | 137,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.20` | 807,080.00 USD | 807,080.00 USD | 365,110.00 USD | 0.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3949.50` | 2,900,000.00 USD | 2,900,000.00 USD | 549,120.00 USD | 0.00 USD | 68,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.40` | 395,840.00 USD | 395,840.00 USD | 195,870.00 USD | 0.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.90` | 2,280,000.00 USD | 2,280,000.00 USD | 442,240.00 USD | 0.00 USD | 66,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.60` | 174,110.00 USD | 174,110.00 USD | 83,380.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.30` | 1,770,000.00 USD | 1,770,000.00 USD | 306,330.00 USD | 0.00 USD | 49,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.80` | 73,340.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.70` | 1,420,000.00 USD | 1,420,000.00 USD | 192,180.00 USD | 0.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.00` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.10` | 1,170,000.00 USD | 1,170,000.00 USD | 249,290.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.50` | 863,560.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.90` | 616,600.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.30` | 347,370.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.70` | 110,560.00 USD | 110,560.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.10` | 50,730.00 USD | 50,730.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4063.90` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4068.30` | 185,820.00 USD | 185,820.00 USD | 0.00 USD | 0.00 USD | 124,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4072.70` | 319,810.00 USD | 319,810.00 USD | 57,650.00 USD | 0.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.10` | 980,620.00 USD | 980,620.00 USD | 539,520.00 USD | 0.00 USD | 121,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4077.40` | 532,290.00 USD | 532,290.00 USD | 87,320.00 USD | 0.00 USD | 142,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.50` | 2,290,000.00 USD | 2,290,000.00 USD | 973,810.00 USD | 0.00 USD | 337,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4081.60` | 903,240.00 USD | 903,240.00 USD | 178,090.00 USD | 0.00 USD | 192,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4085.80` | 1,470,000.00 USD | 1,470,000.00 USD | 362,630.00 USD | 0.00 USD | 201,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 3,470,000.00 USD | 3,470,000.00 USD | 813,840.00 USD | 0.00 USD | 366,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.00` | 1,580,000.00 USD | 1,580,000.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.30` | 4,430,000.00 USD | 4,430,000.00 USD | 795,150.00 USD | 0.00 USD | 159,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.20` | 1,840,000.00 USD | 1,840,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.70` | 4,820,000.00 USD | 4,820,000.00 USD | 274,190.00 USD | 0.00 USD | 118,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.40` | 2,070,000.00 USD | 2,070,000.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.10` | 5,380,000.00 USD | 5,380,000.00 USD | 528,170.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.60` | 2,420,000.00 USD | 2,420,000.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 5,870,000.00 USD | 5,870,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 2,870,000.00 USD | 2,870,000.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.90` | 6,470,000.00 USD | 6,470,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.00` | 3,120,000.00 USD | 3,120,000.00 USD | 224,660.00 USD | 0.00 USD | 30,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.30` | 7,070,000.00 USD | 7,070,000.00 USD | 528,700.00 USD | 0.00 USD | 67,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.20` | 3,260,000.00 USD | 3,260,000.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.70` | 7,450,000.00 USD | 7,450,000.00 USD | 338,630.00 USD | 0.00 USD | 42,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.40` | 3,330,000.00 USD | 3,330,000.00 USD | 66,420.00 USD | 0.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4121.10` | 7,710,000.00 USD | 7,710,000.00 USD | 225,210.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.60` | 3,340,000.00 USD | 3,340,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.50` | 8,110,000.00 USD | 8,110,000.00 USD | 342,730.00 USD | 0.00 USD | 61,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.90` | 8,290,000.00 USD | 8,290,000.00 USD | 125,300.00 USD | 0.00 USD | 56,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4134.30` | 8,530,000.00 USD | 8,530,000.00 USD | 195,250.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4138.70` | 8,760,000.00 USD | 8,760,000.00 USD | 219,810.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.10` | 9,040,000.00 USD | 9,040,000.00 USD | 232,530.00 USD | 0.00 USD | 47,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.60` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.50` | 9,190,000.00 USD | 9,190,000.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.80` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4151.90` | 9,370,000.00 USD | 9,370,000.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.00` | 3,490,000.00 USD | 3,490,000.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.30` | 9,670,000.00 USD | 9,670,000.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4157.20` | 3,600,000.00 USD | 3,600,000.00 USD | 36,330.00 USD | 0.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.70` | 10,120,000.00 USD | 10,120,000.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4161.40` | 3,780,000.00 USD | 3,780,000.00 USD | 87,190.00 USD | 0.00 USD | 96,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.10` | 10,920,000.00 USD | 10,920,000.00 USD | 593,240.00 USD | 0.00 USD | 210,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4165.60` | 4,060,000.00 USD | 4,060,000.00 USD | 190,490.00 USD | 0.00 USD | 89,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.50` | 11,400,000.00 USD | 11,400,000.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4169.80` | 4,120,000.00 USD | 4,120,000.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.90` | 11,640,000.00 USD | 11,640,000.00 USD | 156,630.00 USD | 0.00 USD | 77,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.00` | 4,250,000.00 USD | 4,250,000.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.20` | 4,350,000.00 USD | 4,350,000.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 11,900,000.00 USD | 11,900,000.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.40` | 4,510,000.00 USD | 4,510,000.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.70` | 12,090,000.00 USD | 12,090,000.00 USD | 143,730.00 USD | 0.00 USD | 50,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.60` | 4,760,000.00 USD | 4,760,000.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.10` | 12,370,000.00 USD | 12,370,000.00 USD | 219,060.00 USD | 0.00 USD | 54,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.80` | 4,870,000.00 USD | 4,870,000.00 USD | 101,180.00 USD | 0.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.50` | 12,670,000.00 USD | 12,670,000.00 USD | 271,340.00 USD | 0.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.00` | 4,960,000.00 USD | 4,960,000.00 USD | 73,130.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.90` | 12,910,000.00 USD | 12,910,000.00 USD | 204,490.00 USD | 0.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.20` | 4,990,000.00 USD | 4,990,000.00 USD | 30,260.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 13,060,000.00 USD | 13,060,000.00 USD | 132,330.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.40` | 5,010,000.00 USD | 5,010,000.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.70` | 13,210,000.00 USD | 13,210,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4209.10` | 13,330,000.00 USD | 13,330,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.50` | 13,460,000.00 USD | 13,460,000.00 USD | 99,920.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.90` | 13,590,000.00 USD | 13,590,000.00 USD | 121,670.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4222.30` | 13,740,000.00 USD | 13,740,000.00 USD | 146,500.00 USD | 0.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.70` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4231.10` | 13,830,000.00 USD | 13,830,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4235.50` | 13,860,000.00 USD | 13,860,000.00 USD | 34,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4379.80` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4388.20` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4392.40` | 5,050,000.00 USD | 5,050,000.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.90` | 13,940,000.00 USD | 13,940,000.00 USD | 27,620.00 USD | 0.00 USD | 16,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4396.60` | 5,090,000.00 USD | 5,090,000.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.30` | 14,070,000.00 USD | 14,070,000.00 USD | 117,750.00 USD | 0.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4400.80` | 5,140,000.00 USD | 5,140,000.00 USD | 26,650.00 USD | 0.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.70` | 14,280,000.00 USD | 14,280,000.00 USD | 153,810.00 USD | 0.00 USD | 59,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4405.00` | 5,220,000.00 USD | 5,220,000.00 USD | 51,120.00 USD | 0.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4407.10` | 14,440,000.00 USD | 14,440,000.00 USD | 115,090.00 USD | 0.00 USD | 43,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.50` | 14,550,000.00 USD | 14,550,000.00 USD | 78,400.00 USD | 0.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.90` | 14,600,000.00 USD | 14,600,000.00 USD | 36,920.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4420.30` | 14,690,000.00 USD | 14,690,000.00 USD | 84,770.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.70` | 14,740,000.00 USD | 14,740,000.00 USD | 34,880.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4429.10` | 14,790,000.00 USD | 14,790,000.00 USD | 37,690.00 USD | 0.00 USD | 16,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4433.40` | 14,890,000.00 USD | 14,890,000.00 USD | 88,510.00 USD | 0.00 USD | 8,450.00 USD | `Tier 1 CEX` |

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
| `1D` | `3581.80` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3584.30` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3586.00` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3588.70` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3590.20` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `3593.10` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3594.40` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD |
| `7D` | `3597.50` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 99,580.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3598.60` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `3601.90` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 182,840.00 USD | 0.00 USD | 69,870.00 USD |
| `1D` | `3602.80` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 36,990.00 USD | 0.00 USD | 47,700.00 USD |
| `7D` | `3606.30` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 152,940.00 USD | 0.00 USD | 52,040.00 USD |
| `1D` | `3607.00` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 48,270.00 USD | 0.00 USD | 11,730.00 USD |
| `7D` | `3610.70` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 25,660.00 USD |
| `1D` | `3611.20` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3615.10` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 76,990.00 USD | 0.00 USD | 15,340.00 USD |
| `1D` | `3615.40` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD |
| `7D` | `3619.50` | 14,270,000.00 USD | 0.00 USD | 14,270,000.00 USD | 45,440.00 USD | 0.00 USD | 15,200.00 USD |
| `1D` | `3619.60` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3623.80` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD |
| `7D` | `3623.90` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 55,480.00 USD | 0.00 USD | 21,610.00 USD |
| `1D` | `3628.00` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 28,780.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3628.30` | 14,130,000.00 USD | 0.00 USD | 14,130,000.00 USD | 78,160.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3632.20` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 10,830.00 USD | 0.00 USD | 3,800.00 USD |
| `7D` | `3632.70` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 65,870.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3636.40` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3637.10` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 25,300.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3641.50` | 13,940,000.00 USD | 0.00 USD | 13,940,000.00 USD | 45,790.00 USD | 0.00 USD | 13,010.00 USD |
| `7D` | `3645.90` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `7D` | `3650.30` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `7D` | `3654.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `7D` | `3659.10` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 6,820.00 USD | 0.00 USD | 4,810.00 USD |
| `7D` | `3663.50` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 12,530.00 USD | 0.00 USD | 4,250.00 USD |
| `7D` | `3667.90` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3821.20` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `3821.90` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3825.40` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `1D` | `3829.60` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `3830.70` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 84,860.00 USD |
| `1D` | `3833.80` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3835.10` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 69,040.00 USD | 0.00 USD | 58,110.00 USD |
| `1D` | `3838.00` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 38,960.00 USD | 0.00 USD | 71,270.00 USD |
| `7D` | `3839.50` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 396,580.00 USD | 0.00 USD | 91,350.00 USD |
| `1D` | `3842.20` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 93,750.00 USD | 0.00 USD | 109,220.00 USD |
| `7D` | `3843.90` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 597,060.00 USD | 0.00 USD | 208,140.00 USD |
| `1D` | `3846.40` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 180,250.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `3848.30` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 436,120.00 USD | 0.00 USD | 112,720.00 USD |
| `1D` | `3850.60` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD |
| `7D` | `3852.70` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 228,280.00 USD | 0.00 USD | 74,580.00 USD |
| `1D` | `3854.80` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD |
| `7D` | `3857.10` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 233,200.00 USD | 0.00 USD | 38,880.00 USD |
| `1D` | `3859.00` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD |
| `7D` | `3861.50` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 174,990.00 USD | 0.00 USD | 58,530.00 USD |
| `1D` | `3863.20` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3865.90` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 261,040.00 USD | 0.00 USD | 62,040.00 USD |
| `1D` | `3867.40` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 182,060.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `3870.30` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 226,450.00 USD | 0.00 USD | 32,730.00 USD |
| `1D` | `3871.60` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 109,480.00 USD | 0.00 USD | 12,540.00 USD |
| `7D` | `3874.70` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 224,270.00 USD | 0.00 USD | 25,440.00 USD |
| `1D` | `3875.80` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 28,070.00 USD | 0.00 USD | 5,810.00 USD |
| `7D` | `3879.10` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 122,020.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `3880.00` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD |
| `7D` | `3883.50` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 161,950.00 USD | 0.00 USD | 36,870.00 USD |
| `7D` | `3887.90` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 87,390.00 USD | 0.00 USD | 32,570.00 USD |
| `7D` | `3892.30` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 104,620.00 USD | 0.00 USD | 12,530.00 USD |
| `7D` | `3896.70` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `3901.00` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3901.10` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 73,850.00 USD | 0.00 USD | 75,240.00 USD |
| `1D` | `3905.20` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `3905.50` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 55,280.00 USD | 0.00 USD | 15,640.00 USD |
| `1D` | `3909.40` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `3909.90` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 34,960.00 USD | 0.00 USD | 162,420.00 USD |
| `1D` | `3913.60` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `3914.30` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 138,080.00 USD | 0.00 USD | 40,680.00 USD |
| `1D` | `3917.80` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 55,700.00 USD | 0.00 USD | 142,540.00 USD |
| `7D` | `3918.70` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 763,340.00 USD | 0.00 USD | 199,970.00 USD |
| `1D` | `3922.00` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 187,870.00 USD | 0.00 USD | 206,230.00 USD |
| `7D` | `3923.10` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 1,120,000.00 USD | 0.00 USD | 399,510.00 USD |
| `1D` | `3926.20` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 382,350.00 USD | 0.00 USD | 187,710.00 USD |
| `7D` | `3927.50` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD |
| `1D` | `3930.40` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD |
| `7D` | `3931.90` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 586,550.00 USD | 0.00 USD | 170,010.00 USD |
| `1D` | `3934.60` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD |
| `7D` | `3936.30` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 418,330.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `3938.80` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD |
| `7D` | `3940.70` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 335,530.00 USD | 0.00 USD | 70,750.00 USD |
| `1D` | `3943.00` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD |
| `7D` | `3945.10` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 398,420.00 USD | 0.00 USD | 137,690.00 USD |
| `1D` | `3947.20` | 807,080.00 USD | 0.00 USD | 807,080.00 USD | 365,110.00 USD | 0.00 USD | 46,140.00 USD |
| `7D` | `3949.50` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 549,120.00 USD | 0.00 USD | 68,930.00 USD |
| `1D` | `3951.40` | 395,840.00 USD | 0.00 USD | 395,840.00 USD | 195,870.00 USD | 0.00 USD | 25,860.00 USD |
| `7D` | `3953.90` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 442,240.00 USD | 0.00 USD | 66,920.00 USD |
| `1D` | `3955.60` | 174,110.00 USD | 0.00 USD | 174,110.00 USD | 83,380.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `3958.30` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 306,330.00 USD | 0.00 USD | 49,170.00 USD |
| `1D` | `3959.80` | 73,340.00 USD | 0.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `3962.70` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 192,180.00 USD | 0.00 USD | 56,430.00 USD |
| `1D` | `3964.00` | 606.18 USD | 0.00 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3967.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 249,290.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `3971.50` | 863,560.00 USD | 0.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3975.90` | 616,600.00 USD | 0.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.30` | 347,370.00 USD | 0.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.70` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.10` | 50,730.00 USD | 0.00 USD | 50,730.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4001.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4001.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4063.90` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `4068.30` | 185,820.00 USD | 185,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 124,870.00 USD |
| `1D` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `4072.70` | 319,810.00 USD | 319,810.00 USD | 0.00 USD | 57,650.00 USD | 0.00 USD | 76,340.00 USD |
| `1D` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 0.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `4077.10` | 980,620.00 USD | 980,620.00 USD | 0.00 USD | 539,520.00 USD | 0.00 USD | 121,290.00 USD |
| `1D` | `4077.40` | 532,290.00 USD | 532,290.00 USD | 0.00 USD | 87,320.00 USD | 0.00 USD | 142,540.00 USD |
| `7D` | `4081.50` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 973,810.00 USD | 0.00 USD | 337,450.00 USD |
| `1D` | `4081.60` | 903,240.00 USD | 903,240.00 USD | 0.00 USD | 178,090.00 USD | 0.00 USD | 192,870.00 USD |
| `1D` | `4085.80` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 362,630.00 USD | 0.00 USD | 201,070.00 USD |
| `7D` | `4085.90` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 813,840.00 USD | 0.00 USD | 366,440.00 USD |
| `1D` | `4090.00` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD |
| `7D` | `4090.30` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 795,150.00 USD | 0.00 USD | 159,840.00 USD |
| `1D` | `4094.20` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `4094.70` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 274,190.00 USD | 0.00 USD | 118,990.00 USD |
| `1D` | `4098.40` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `4099.10` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 528,170.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4102.60` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD |
| `7D` | `4103.50` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4106.80` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD |
| `7D` | `4107.90` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4111.00` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 224,660.00 USD | 0.00 USD | 30,400.00 USD |
| `7D` | `4112.30` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 528,700.00 USD | 0.00 USD | 67,220.00 USD |
| `1D` | `4115.20` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `4116.70` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 338,630.00 USD | 0.00 USD | 42,660.00 USD |
| `1D` | `4119.40` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 66,420.00 USD | 0.00 USD | 5,040.00 USD |
| `7D` | `4121.10` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 225,210.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4123.60` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4125.50` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 342,730.00 USD | 0.00 USD | 61,080.00 USD |
| `7D` | `4129.90` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 125,300.00 USD | 0.00 USD | 56,200.00 USD |
| `7D` | `4134.30` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 195,250.00 USD | 0.00 USD | 39,940.00 USD |
| `7D` | `4138.70` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 219,810.00 USD | 0.00 USD | 13,380.00 USD |
| `1D` | `4140.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4143.10` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 232,530.00 USD | 0.00 USD | 47,230.00 USD |
| `1D` | `4144.60` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4147.50` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD |
| `1D` | `4148.80` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4151.90` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD |
| `1D` | `4153.00` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `4156.30` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4157.20` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 36,330.00 USD | 0.00 USD | 71,270.00 USD |
| `7D` | `4160.70` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD |
| `1D` | `4161.40` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 87,190.00 USD | 0.00 USD | 96,430.00 USD |
| `7D` | `4165.10` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 593,240.00 USD | 0.00 USD | 210,680.00 USD |
| `1D` | `4165.60` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 190,490.00 USD | 0.00 USD | 89,780.00 USD |
| `7D` | `4169.50` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD |
| `1D` | `4169.80` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `4173.90` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 77,020.00 USD |
| `1D` | `4174.00` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4178.20` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD |
| `7D` | `4178.30` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4182.40` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD |
| `7D` | `4182.70` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 50,750.00 USD |
| `1D` | `4186.60` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD |
| `7D` | `4187.10` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 54,620.00 USD |
| `1D` | `4190.80` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 101,180.00 USD | 0.00 USD | 15,740.00 USD |
| `7D` | `4191.50` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 271,340.00 USD | 0.00 USD | 33,750.00 USD |
| `1D` | `4195.00` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 73,130.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `4195.90` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 204,490.00 USD | 0.00 USD | 31,470.00 USD |
| `1D` | `4199.20` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `4200.30` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 132,330.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4203.40` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4204.70` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD |
| `7D` | `4209.10` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `7D` | `4213.50` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 99,920.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4217.90` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 121,670.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `4222.30` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 146,500.00 USD | 0.00 USD | 5,460.00 USD |
| `7D` | `4226.70` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4231.10` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `4235.50` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 34,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4379.80` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD |
| `7D` | `4380.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4388.20` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `4389.50` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,120.00 USD |
| `1D` | `4392.40` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4393.90` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 16,570.00 USD |
| `1D` | `4396.60` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `4398.30` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 117,750.00 USD | 0.00 USD | 17,130.00 USD |
| `1D` | `4400.80` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 26,650.00 USD | 0.00 USD | 22,410.00 USD |
| `7D` | `4402.70` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 153,810.00 USD | 0.00 USD | 59,890.00 USD |
| `1D` | `4405.00` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 51,120.00 USD | 0.00 USD | 34,900.00 USD |
| `7D` | `4407.10` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 115,090.00 USD | 0.00 USD | 43,280.00 USD |
| `7D` | `4411.50` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 78,400.00 USD | 0.00 USD | 24,920.00 USD |
| `7D` | `4415.90` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 15,620.00 USD |
| `7D` | `4420.30` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 84,770.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `4424.70` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 34,880.00 USD | 0.00 USD | 18,300.00 USD |
| `7D` | `4429.10` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 37,690.00 USD | 0.00 USD | 16,270.00 USD |
| `7D` | `4433.40` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 88,510.00 USD | 0.00 USD | 8,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.62M` | Total OI Tokens: `68,876.9 PAXG`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-0.21%` | 24h OI Change: `+0.13%`
  * Exchange Breakdown: Binance=`105.43M` | Bybit=`24.16M` | OKX=`-` | Hyperliquid=`24.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.81K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0016%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0015%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0177%` | **USDT Bitget** | `0.0045%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `58.06%` | `41.94%` | `1.38` | 1,260,000.00 USD |
| `15M` | `Binance` | `52.76%` | `47.24%` | `1.12` | 372,060.00 USD |
| `15M` | `OKX` | `72.89%` | `27.11%` | `2.69` | 277,520.00 USD |
| `15M` | `Bybit` | `47.43%` | `52.57%` | `0.90` | 114,820.00 USD |
| `15M` | `KuCoin` | `49.39%` | `50.61%` | `0.98` | 124,810.00 USD |
| `15M` | `Gate` | `78.29%` | `21.71%` | `3.61` | 40,530.00 USD |
| `15M` | `Bitget` | `40.53%` | `59.47%` | `0.68` | 51,070.00 USD |
| `15M` | `BingX` | `38.75%` | `61.25%` | `0.63` | 63,200.00 USD |
| `15M` | `MEXC` | `64.85%` | `35.15%` | `1.84` | 40,900.00 USD |
| `15M` | `Bitunix` | `59.84%` | `40.16%` | `1.49` | 15,530.00 USD |
| `15M` | `Hyperliquid` | `83.24%` | `16.76%` | `4.97` | 22,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.14%` | `49.86%` | `1.01` | 44,510.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `68.47%` | `31.53%` | `2.17` | 90,360.00 USD |
| `15M` | `HTX` | `80.03%` | `19.97%` | `4.01` | 0.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.2%` | `33.8%` | `1.96` | 1,840.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 13.05 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 9.95 USD |
| `15M` | `Whale Positions` | `52.76%` | `47.24%` | `1.12` | 372,060.00 USD |
| `15M` | `Global Accounts` | `58.06%` | `41.94%` | `1.38` | 1,260,000.00 USD |
| `1H` | `PAXG` | `46.24%` | `53.76%` | `0.86` | 13,410,000.00 USD |
| `1H` | `Binance` | `46.35%` | `53.65%` | `0.86` | 5,140,000.00 USD |
| `1H` | `OKX` | `48.78%` | `51.22%` | `0.95` | 1,800,000.00 USD |
| `1H` | `Bybit` | `50.1%` | `49.9%` | `1.00` | 1,750,000.00 USD |
| `1H` | `KuCoin` | `36.88%` | `63.12%` | `0.58` | 245,690.00 USD |
| `1H` | `Gate` | `45.14%` | `54.86%` | `0.82` | 378,430.00 USD |
| `1H` | `Bitget` | `40.29%` | `59.71%` | `0.67` | 922,290.00 USD |
| `1H` | `BingX` | `40.96%` | `59.04%` | `0.69` | 884,090.00 USD |
| `1H` | `MEXC` | `33.12%` | `66.88%` | `0.50` | 1,010,000.00 USD |
| `1H` | `Bitunix` | `53.27%` | `46.73%` | `1.14` | 171,730.00 USD |
| `1H` | `Hyperliquid` | `48.74%` | `51.26%` | `0.95` | 164,370.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.3%` | `50.7%` | `0.97` | 467,160.00 USD |
| `1H` | `Crypto.com` | `54.72%` | `45.28%` | `1.21` | 4,280.00 USD |
| `1H` | `WhiteBIT` | `73.12%` | `26.88%` | `2.72` | 363,610.00 USD |
| `1H` | `HTX` | `53.19%` | `46.81%` | `1.14` | 1,430.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.98%` | `55.02%` | `0.82` | 60,980.00 USD |
| `1H` | `Aster` | `46.74%` | `53.26%` | `0.88` | 9,690.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `91.17%` | `8.83%` | `10.33` | 32,290.00 USD |
| `1H` | `Whale Positions` | `46.35%` | `53.65%` | `0.86` | 5,140,000.00 USD |
| `1H` | `Global Accounts` | `46.24%` | `53.76%` | `0.86` | 13,410,000.00 USD |
| `4H` | `PAXG` | `45.38%` | `54.62%` | `0.83` | 53,150,000.00 USD |
| `4H` | `Binance` | `49.34%` | `50.66%` | `0.97` | 19,640,000.00 USD |
| `4H` | `OKX` | `43.97%` | `56.03%` | `0.78` | 8,820,000.00 USD |
| `4H` | `Bybit` | `45.69%` | `54.31%` | `0.84` | 6,500,000.00 USD |
| `4H` | `KuCoin` | `42.09%` | `57.91%` | `0.73` | 550,430.00 USD |
| `4H` | `Gate` | `44.17%` | `55.83%` | `0.79` | 1,660,000.00 USD |
| `4H` | `Bitget` | `46.55%` | `53.45%` | `0.87` | 4,170,000.00 USD |
| `4H` | `BingX` | `24.38%` | `75.62%` | `0.32` | 4,400,000.00 USD |
| `4H` | `MEXC` | `36.82%` | `63.18%` | `0.58` | 3,040,000.00 USD |
| `4H` | `Bitunix` | `49.2%` | `50.8%` | `0.97` | 772,820.00 USD |
| `4H` | `Hyperliquid` | `56.63%` | `43.37%` | `1.31` | 537,110.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.33%` | `50.67%` | `0.97` | 1,800,000.00 USD |
| `4H` | `Crypto.com` | `39.54%` | `60.46%` | `0.65` | 25,900.00 USD |
| `4H` | `WhiteBIT` | `75.86%` | `24.14%` | `3.14` | 954,670.00 USD |
| `4H` | `HTX` | `82.56%` | `17.44%` | `4.73` | 30,440.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `37.98%` | `62.02%` | `0.61` | 72,220.00 USD |
| `4H` | `Aster` | `50.76%` | `49.24%` | `1.03` | 46,610.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `80%` | `20%` | `4.00` | 130,240.00 USD |
| `4H` | `Whale Positions` | `49.34%` | `50.66%` | `0.97` | 19,640,000.00 USD |
| `4H` | `Global Accounts` | `45.38%` | `54.62%` | `0.83` | 53,150,000.00 USD |


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
| `5m` | -58,000.00 USD | -15,220.00 USD | **`DISTRIBUTION`** |
| `15m` | -52,320.00 USD | 217,750.00 USD | **`ACCUMULATION`** |
| `30m` | -162,860.00 USD | 701,390.00 USD | **`ACCUMULATION`** |
| `1h` | -220,710.00 USD | 922,300.00 USD | **`ACCUMULATION`** |
| `2h` | -1,090,000.00 USD | -168,430.00 USD | **`DISTRIBUTION`** |
| `4h` | -521,370.00 USD | -200,180.00 USD | **`DISTRIBUTION`** |
| `6h` | 313,330.00 USD | 54,740.00 USD | **`ACCUMULATION`** |
| `8h` | 305,000.00 USD | -647,530.00 USD | **`DISTRIBUTION`** |
| `12h` | -671,570.00 USD | -440,030.00 USD | **`DISTRIBUTION`** |
| `24h` | -847,250.00 USD | 719,060.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,410,000.00 USD | -8,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,920,000.00 USD | -71,310,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-58.00K` | 15m=`-52.32K` | 1h=`-220.71K` | 24h=`-847.25K`
* Futures Capital Netflows: 5m=`-15.22K` | 15m=`+217.75K` | 1h=`+922.30K` | 24h=`+719.06K`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3988.80` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3978.46` (Risk Distance: `10.34` pts)
  * +2.5R Take Profit: `4014.66`
  * Mathematical Lot Sizing: **`0.96 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.45` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4023.79` (Risk Distance: `10.34` pts)
  * +2.5R Take Profit: `3987.59`
  * Mathematical Lot Sizing: **`0.96 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4029.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
