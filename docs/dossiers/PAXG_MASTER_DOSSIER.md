# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 15:21:06 IST` (`2026-10-30 09:51:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3988.45` | **Live Ask Quote**: `3988.54` | **Mid Price**: `3988.49`
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
  * Session VWAP: `3996.59` | VWAP Z-Score: `-0.70` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.98` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.60` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4025.68` | Lower -3.00σ Band: `3967.50`
  * Upper +2.51σ Band: `4020.93` | Lower -2.51σ Band: `3972.26`
  * Upper +2.01σ Band: `4016.08` | Lower -2.01σ Band: `3977.10`
  * Upper +2.00σ Band: `4015.99` | Lower -2.00σ Band: `3977.20`
  * Upper +1.28σ Band: `4009.01` | Lower -1.28σ Band: `3984.18`
  * Upper +1.00σ Band: `4006.29` | Lower -1.00σ Band: `3986.90`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3989.20` | EMA-20=`3990.55` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3998.70` (Slope: `+0.0000`) | EMA-100=`4009.27`
  * Institutional Anchors: EMA-144=`4015.12` | EMA-200=`4019.88` (Slope: `-0.1059`) | EMA-233=`4022.87`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4007.93` (Distance: `-0.50%`)
  * Point of Control (POC) = `3990.50` (Distance: `-0.07%`)
  * Value Area Low (VAL) = `3982.85` (Distance: `+0.13%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4052.58` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`4012.43` | Low=`3964.56`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3972.54` - `4004.45`
  * Optimal Trade Entry (OTE 0.705): `3996.47`
  * Structural Invalidation Anchor (0.786): `4020.40`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3993.85` | `3994.86` | `3993.00` | `3993.77` | `27` | 108,357.74 USD | 58,258.63 USD | `+53.77%` | 79,597.08 USD | `+0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `3993.76` | `3994.24` | `3992.51` | `3992.52` | `10` | 41,356.39 USD | -19,055.52 USD | `-46.08%` | 60,541.56 USD | `-0.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3992.52` | `3993.01` | `3992.49` | `3992.49` | `2` | 8,975.38 USD | -6,779.43 USD | `-75.53%` | 53,762.14 USD | `-0.28` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `3995.01` | `3998.34` | `3993.52` | `3994.62` | `106` | 425,108.34 USD | 85,150.86 USD | `+20.03%` | -42,802.78 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3994.41` | `3995.82` | `3993.00` | `3993.77` | `82` | 329,508.51 USD | 94,767.85 USD | `+28.76%` | 51,965.07 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3993.76` | `3994.24` | `3992.49` | `3992.49` | `13` | 50,331.78 USD | -25,834.95 USD | `-51.33%` | 26,130.12 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `3992.27` | `3994.60` | `3973.63` | `3981.69` | `1,798` | 7,168,194.57 USD | -1,074,302.54 USD | `-14.99%` | -629,444.62 USD | `-2.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3981.68` | `4002.39` | `3979.22` | `4001.26` | `1,541` | 6,150,835.88 USD | 541,833.50 USD | `+8.81%` | -87,611.12 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4001.22` | `4002.41` | `3992.49` | `3992.49` | `399` | 1,593,054.93 USD | 113,741.24 USD | `+7.14%` | 26,130.12 USD | `+0.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3992.49` | `1,940` | 7,743,890.81 USD | 655,574.74 USD | `+8.47%` | 76,608.51 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3992.49` | `1,940` | 7,743,890.81 USD | 655,574.74 USD | `+8.47%` | 76,608.51 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `3987.40` | `3.0847` | 12,299.93 USD | 1,157,049.86 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `3987.60` | `14.2889` | 56,978.42 USD | 1,144,749.93 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `3987.70` | `8.6225` | 34,383.94 USD | 1,087,771.51 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `3987.80` | `13.5629` | 54,086.13 USD | 1,053,387.57 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `3987.90` | `83.5973` | 333,377.67 USD | 999,301.44 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `3988.00` | `7.8924` | 31,474.89 USD | 665,923.76 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3988.10` | `5.3849` | 21,475.52 USD | 634,448.87 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3988.20` | `3.8538` | 15,369.73 USD | 612,973.35 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3988.30` | `11.6160` | 46,328.09 USD | 597,603.63 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3988.40` | `0.0620` | 247.28 USD | 551,275.53 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3988.50` | `51.5878` | 205,757.94 USD | 551,028.25 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3988.60` | `9.4359` | 37,636.03 USD | 345,270.31 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3988.70` | `14.1156` | 56,302.89 USD | 307,634.28 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3988.80` | `8.1181` | 32,381.48 USD | 251,331.39 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `3988.90` | `16.5170` | 65,884.66 USD | 218,949.91 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3989.00` | `34.9684` | 139,488.95 USD | 153,065.25 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3989.20` | `2.7967` | 11,156.60 USD | 13,576.30 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3989.30` | `0.3226` | 1,286.95 USD | 2,419.71 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3989.40` | `0.0041` | 16.36 USD | 1,132.76 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3990.00` | `0.2798` | 1,116.40 USD | 1,116.40 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3990.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,990.05` | `0.00%` | `-` |
| `ASK` | `3990.10` | `93.4597` | 372,913.55 USD | 372,913.55 USD | `23 orders` | `+0.00%` | `-` |
| `ASK` | `3990.20` | `8.6031` | 34,328.09 USD | 407,241.64 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `3990.30` | `7.5179` | 29,998.68 USD | 437,240.31 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3990.40` | `12.1140` | 48,339.71 USD | 485,580.02 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3990.50` | `18.1523` | 72,436.75 USD | 558,016.77 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3990.60` | `29.3311` | 117,048.69 USD | 675,065.46 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3990.70` | `14.8272` | 59,170.91 USD | 734,236.37 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3990.80` | `23.5985` | 94,176.89 USD | 828,413.26 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3990.90` | `15.3171` | 61,129.01 USD | 889,542.28 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3991.00` | `1.0974` | 4,379.72 USD | 893,922.00 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `3991.10` | `11.3476` | 45,289.41 USD | 939,211.41 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3991.20` | `9.1102` | 36,360.63 USD | 975,572.04 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3991.30` | `7.5171` | 30,003.00 USD | 1,005,575.04 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `3991.40` | `67.0878` | 267,774.24 USD | 1,273,349.28 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3991.50` | `14.3935` | 57,451.66 USD | 1,330,800.94 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3991.60` | `17.4464` | 69,639.05 USD | 1,400,439.99 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3991.70` | `7.1960` | 28,724.27 USD | 1,429,164.26 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3991.80` | `14.7208` | 58,762.49 USD | 1,487,926.75 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3991.90` | `12.1386` | 48,456.08 USD | 1,536,382.83 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `3992.00` | `86.9806` | 347,226.56 USD | 1,883,609.38 USD | `5 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,902,185.55 USD | `6,489.82` | `4185.46` | `3990.80` | `27920.13` | 1,260,765.46 USD | `+4.87%` | `4X Cross` |
| `48` | `0x4692...164f` | `SHORT` | 25,224,698.69 USD | `6,320.24` | `4127.37` | `3990.80` | `14118.28` | 861,303.78 USD | `+3.41%` | `5X Cross` |
| `62` | `0xb83d...6e36` | `SHORT` | 23,426,768.51 USD | `5,869.90` | `4228.86` | `3990.80` | `24468.80` | 1,396,253.43 USD | `+5.96%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,272,650.33 USD | `4,828.91` | `4157.43` | `3990.80` | `2291.01` | -803,231.99 USD | `-4.17%` | `25X Cross` |
| `141` | `0x645b...87b8` | `LONG` | 14,151,696.82 USD | `3,545.72` | `4127.81` | `3990.80` | `642.00` | -484,410.13 USD | `-3.42%` | `3X Cross` |
| `155` | `0x7a6d...f79c` | `SHORT` | 13,043,112.06 USD | `3,268.21` | `4228.94` | `3990.80` | `4378.49` | 777,967.07 USD | `+5.96%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,175,448.60 USD | `2,800.02` | `4364.62` | `3990.80` | `4212.81` | 1,045,595.53 USD | `+9.36%` | `20X Cross` |
| `260` | `0x3678...b209` | `LONG` | 8,780,640.00 USD | `2,200.00` | `4176.09` | `3990.80` | `2697.57` | -406,779.30 USD | `-4.63%` | `25X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,780,200.00 USD | `2,200.00` | `4112.20` | `3990.80` | `4287.16` | 266,654.59 USD | `+3.04%` | `20X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,883,895.62 USD | `1,975.37` | `4048.55` | `3990.80` | `6651.26` | 113,496.10 USD | `+1.44%` | `6X Cross` |
| `363` | `0xc26c...b8f4` | `LONG` | 6,305,271.64 USD | `1,579.95` | `4075.62` | `3990.80` | `0.000000` | -134,025.33 USD | `-2.13%` | `1X Cross` |
| `556` | `0x63da...8add` | `LONG` | 3,991,200.00 USD | `1,000.00` | `4021.46` | `3990.80` | `3564.70` | -30,260.96 USD | `-0.76%` | `25X Cross` |
| `568` | `0xf3dc...1672` | `LONG` | 3,928,421.22 USD | `984.27` | `4018.39` | `3990.80` | `2819.93` | -26,765.48 USD | `-0.68%` | `20X Cross` |
| `584` | `0x9aa5...58af` | `LONG` | 3,870,133.77 USD | `969.74` | `4279.98` | `3990.80` | `0.000000` | -280,333.08 USD | `-7.24%` | `20X Cross` |
| `674` | `0x4a20...3c26` | `LONG` | 3,342,229.68 USD | `837.40` | `4599.73` | `3990.80` | `0.000000` | -509,590.70 USD | `-15.25%` | `20X Cross` |
| `785` | `0x9c06...0560` | `LONG` | 2,901,410.02 USD | `726.95` | `4002.36` | `3990.80` | `0.000000` | -8,119.23 USD | `-0.28%` | `25X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,739,898.93 USD | `686.49` | `4290.34` | `3990.80` | `1461.91` | -205,359.77 USD | `-7.50%` | `25X Cross` |
| `881` | `0x354b...6425` | `LONG` | 2,522,009.22 USD | `631.91` | `4004.93` | `3990.80` | `0.000000` | -8,742.33 USD | `-0.35%` | `10X Cross` |
| `900` | `0x625e...a354` | `SHORT` | 2,474,420.00 USD | `620.00` | `4122.81` | `3990.80` | `4279.57` | 81,727.03 USD | `+3.30%` | `20X Cross` |
| `926` | `0xeae3...e8ad` | `SHORT` | 2,394,720.00 USD | `600.00` | `4104.77` | `3990.80` | `4268.65` | 68,145.11 USD | `+2.85%` | `20X Cross` |
| `927` | `0xf285...fa82` | `LONG` | 2,387,160.27 USD | `598.11` | `4146.45` | `3990.80` | `3891.83` | -92,859.28 USD | `-3.89%` | `25X Cross` |
| `935` | `0xd8c5...99b0` | `SHORT` | 2,372,308.15 USD | `594.35` | `4175.35` | `3990.80` | `35404.68` | 109,335.88 USD | `+4.61%` | `4X Cross` |
| `940` | `0x12f7...8750` | `LONG` | 2,337,289.43 USD | `585.61` | `4082.77` | `3990.80` | `2756.48` | -53,627.55 USD | `-2.29%` | `10X Cross` |
| `985` | `0x413c...886c` | `LONG` | 2,232,958.26 USD | `559.47` | `4007.05` | `3990.80` | `0.000000` | -8,868.95 USD | `-0.40%` | `2X Cross` |
| `1095` | `0x61ce...a62b` | `SHORT` | 1,985,635.97 USD | `497.50` | `4071.66` | `3990.80` | `4724.78` | 40,032.82 USD | `+2.02%` | `20X Cross` |
| `1173` | `0x2edd...8179` | `LONG` | 1,874,082.71 USD | `469.26` | `4164.68` | `3993.50` | `0.000000` | -80,226.06 USD | `-4.28%` | `10X Cross` |
| `1219` | `0xead5...69f2` | `LONG` | 1,811,096.92 USD | `453.78` | `4220.88` | `3990.80` | `3539.53` | -104,271.14 USD | `-5.76%` | `5X Isolated` |
| `1274` | `0x7a6d...f79c` | `SHORT` | 1,710,823.64 USD | `428.38` | `4136.09` | `3993.50` | `5404.66` | 60,991.37 USD | `+3.57%` | `10X Cross` |
| `1319` | `0x46fc...1195` | `LONG` | 1,637,594.39 USD | `410.28` | `4052.34` | `3990.80` | `2145.75` | -25,005.03 USD | `-1.53%` | `20X Cross` |
| `1343` | `0xee02...309d` | `SHORT` | 1,596,480.00 USD | `400.00` | `4438.84` | `3990.80` | `4202.95` | 179,058.60 USD | `+11.22%` | `25X Isolated` |
| `1344` | `0x6d15...d374` | `LONG` | 1,596,400.00 USD | `400.00` | `4068.25` | `3990.80` | `3842.40` | -30,900.00 USD | `-1.94%` | `25X Cross` |
| `1367` | `0x51f6...2b39` | `LONG` | 1,563,336.23 USD | `391.48` | `4228.25` | `3993.50` | `503.21` | -91,939.46 USD | `-5.88%` | `10X Cross` |
| `1377` | `0x02a7...fe9f` | `SHORT` | 1,556,568.00 USD | `390.00` | `4055.02` | `3990.80` | `4307.27` | 24,891.25 USD | `+1.60%` | `25X Cross` |
| `1430` | `0x7e77...b8d2` | `SHORT` | 1,516,732.00 USD | `380.00` | `4131.92` | `3990.80` | `4294.08` | 53,397.64 USD | `+3.52%` | `20X Cross` |
| `1455` | `0x72c2...9b37` | `LONG` | 1,489,241.64 USD | `373.13` | `4000.98` | `3990.80` | `3778.64` | -3,651.87 USD | `-0.25%` | `13X Isolated` |
| `1467` | `0x781e...96b7` | `SHORT` | 1,461,124.23 USD | `365.84` | `4358.71` | `3993.50` | `12872.72` | 133,483.42 USD | `+9.14%` | `10X Cross` |
| `1489` | `0xaa44...b844` | `LONG` | 1,436,832.00 USD | `360.00` | `4043.10` | `3990.80` | `2817.67` | -18,685.63 USD | `-1.30%` | `4X Cross` |
| `1609` | `0xa41f...d50a` | `LONG` | 1,312,920.64 USD | `328.96` | `4468.89` | `3990.80` | `3802.76` | -157,177.21 USD | `-11.97%` | `15X Cross` |
| `1661` | `0xbf5a...88ba` | `SHORT` | 1,267,824.24 USD | `317.65` | `4091.80` | `3990.80` | `9930.24` | 31,958.80 USD | `+2.52%` | `20X Cross` |
| `1703` | `0xff31...ff6c` | `SHORT` | 1,237,272.00 USD | `310.00` | `4372.43` | `3990.80` | `4789.75` | 118,183.38 USD | `+9.55%` | `10X Isolated` |
| `1728` | `0xada6...6f88` | `LONG` | 1,211,195.49 USD | `303.47` | `4166.46` | `3990.80` | `1793.69` | -53,186.96 USD | `-4.39%` | `5X Cross` |
| `1886` | `0x50e2...d770` | `LONG` | 1,079,090.37 USD | `270.37` | `4243.58` | `3990.80` | `2562.69` | -68,236.09 USD | `-6.32%` | `20X Cross` |
| `1897` | `0x4c92...4f17` | `SHORT` | 1,064,534.86 USD | `266.72` | `4260.98` | `3990.80` | `6498.13` | 71,957.38 USD | `+6.76%` | `20X Cross` |
| `1966` | `0xd346...c4f3` | `LONG` | 1,018,398.64 USD | `255.17` | `4188.66` | `3990.80` | `3311.02` | -50,437.87 USD | `-4.95%` | `5X Isolated` |

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
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.57%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.40%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+2.95%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.42%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+2.95%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--1.11%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.32%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.66%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `Long Liquidation` | `3581.80` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3584.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3586.00` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.80` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3590.20` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.10` | 15,070,000.00 USD | 15,070,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3594.40` | 5,490,000.00 USD | 5,490,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.40` | 15,060,000.00 USD | 15,060,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.60` | 5,450,000.00 USD | 5,450,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.70` | 14,940,000.00 USD | 14,940,000.00 USD | 175,610.00 USD | 0.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.80` | 5,420,000.00 USD | 5,420,000.00 USD | 36,990.00 USD | 0.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.00` | 14,700,000.00 USD | 14,700,000.00 USD | 134,320.00 USD | 0.00 USD | 53,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3607.00` | 5,330,000.00 USD | 5,330,000.00 USD | 48,270.00 USD | 0.00 USD | 14,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.30` | 14,510,000.00 USD | 14,510,000.00 USD | 83,580.00 USD | 0.00 USD | 21,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.20` | 5,270,000.00 USD | 5,270,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.60` | 14,410,000.00 USD | 14,410,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.40` | 5,240,000.00 USD | 5,240,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3618.90` | 14,300,000.00 USD | 14,300,000.00 USD | 40,780.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.60` | 5,200,000.00 USD | 5,200,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.20` | 14,250,000.00 USD | 14,250,000.00 USD | 59,230.00 USD | 0.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.80` | 5,140,000.00 USD | 5,140,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.50` | 14,170,000.00 USD | 14,170,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.00` | 5,070,000.00 USD | 5,070,000.00 USD | 26,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3631.80` | 14,070,000.00 USD | 14,070,000.00 USD | 60,720.00 USD | 0.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.20` | 5,040,000.00 USD | 5,040,000.00 USD | 10,830.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.10` | 14,000,000.00 USD | 14,000,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.40` | 5,030,000.00 USD | 5,030,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.40` | 13,970,000.00 USD | 13,970,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.70` | 13,910,000.00 USD | 13,910,000.00 USD | 17,720.00 USD | 0.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.00` | 13,880,000.00 USD | 13,880,000.00 USD | 24,860.00 USD | 0.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 13,850,000.00 USD | 13,850,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.60` | 13,820,000.00 USD | 13,820,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.90` | 13,790,000.00 USD | 13,790,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.20` | 13,760,000.00 USD | 13,760,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3821.20` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.30` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3825.40` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3829.60` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.60` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3833.80` | 4,960,000.00 USD | 4,960,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 13,640,000.00 USD | 13,640,000.00 USD | 69,040.00 USD | 0.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3838.00` | 4,850,000.00 USD | 4,850,000.00 USD | 38,960.00 USD | 0.00 USD | 72,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.20` | 13,550,000.00 USD | 13,550,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3842.20` | 4,740,000.00 USD | 4,740,000.00 USD | 93,750.00 USD | 0.00 USD | 113,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.50` | 13,220,000.00 USD | 13,220,000.00 USD | 557,810.00 USD | 0.00 USD | 224,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3846.40` | 4,530,000.00 USD | 4,530,000.00 USD | 180,250.00 USD | 0.00 USD | 99,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.80` | 12,440,000.00 USD | 12,440,000.00 USD | 535,820.00 USD | 0.00 USD | 157,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3850.60` | 4,250,000.00 USD | 4,250,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.10` | 11,750,000.00 USD | 11,750,000.00 USD | 231,930.00 USD | 0.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.80` | 4,180,000.00 USD | 4,180,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.40` | 11,440,000.00 USD | 11,440,000.00 USD | 219,990.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.00` | 4,040,000.00 USD | 4,040,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.70` | 11,160,000.00 USD | 11,160,000.00 USD | 174,170.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.20` | 3,890,000.00 USD | 3,890,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.00` | 10,970,000.00 USD | 10,970,000.00 USD | 204,130.00 USD | 0.00 USD | 73,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.40` | 3,720,000.00 USD | 3,720,000.00 USD | 175,670.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.30` | 10,690,000.00 USD | 10,690,000.00 USD | 298,110.00 USD | 0.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.60` | 3,530,000.00 USD | 3,530,000.00 USD | 106,280.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.60` | 10,360,000.00 USD | 10,360,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.80` | 3,410,000.00 USD | 3,410,000.00 USD | 28,070.00 USD | 0.00 USD | 4,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3876.90` | 10,100,000.00 USD | 10,100,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.00` | 3,380,000.00 USD | 3,380,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.20` | 9,930,000.00 USD | 9,930,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.50` | 9,780,000.00 USD | 9,780,000.00 USD | 124,650.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3889.80` | 9,630,000.00 USD | 9,630,000.00 USD | 85,430.00 USD | 0.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.10` | 9,520,000.00 USD | 9,520,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.40` | 9,380,000.00 USD | 9,380,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.00` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3902.70` | 9,240,000.00 USD | 9,240,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.00` | 9,150,000.00 USD | 9,150,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3909.40` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.30` | 8,990,000.00 USD | 8,990,000.00 USD | 16,550.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3913.60` | 3,240,000.00 USD | 3,240,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.60` | 8,900,000.00 USD | 8,900,000.00 USD | 287,340.00 USD | 0.00 USD | 116,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3917.80` | 3,010,000.00 USD | 3,010,000.00 USD | 55,700.00 USD | 0.00 USD | 144,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3919.90` | 8,490,000.00 USD | 8,490,000.00 USD | 674,750.00 USD | 0.00 USD | 199,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.00` | 2,810,000.00 USD | 2,810,000.00 USD | 187,870.00 USD | 0.00 USD | 214,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.20` | 7,620,000.00 USD | 7,620,000.00 USD | 1,200,000.00 USD | 0.00 USD | 464,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.20` | 2,410,000.00 USD | 2,410,000.00 USD | 382,350.00 USD | 0.00 USD | 211,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.50` | 5,960,000.00 USD | 5,960,000.00 USD | 913,310.00 USD | 0.00 USD | 195,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.40` | 1,820,000.00 USD | 1,820,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3932.80` | 4,850,000.00 USD | 4,850,000.00 USD | 380,870.00 USD | 0.00 USD | 128,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 1,730,000.00 USD | 1,730,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.10` | 4,340,000.00 USD | 4,340,000.00 USD | 466,400.00 USD | 0.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.80` | 1,420,000.00 USD | 1,420,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.40` | 3,800,000.00 USD | 3,800,000.00 USD | 287,460.00 USD | 0.00 USD | 104,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.00` | 1,160,000.00 USD | 1,160,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3945.70` | 3,400,000.00 USD | 3,400,000.00 USD | 468,070.00 USD | 0.00 USD | 118,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.20` | 780,210.00 USD | 780,210.00 USD | 352,330.00 USD | 0.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.00` | 2,820,000.00 USD | 2,820,000.00 USD | 529,640.00 USD | 0.00 USD | 78,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.40` | 381,740.00 USD | 381,740.00 USD | 189,460.00 USD | 0.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.30` | 2,210,000.00 USD | 2,210,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.60` | 170,720.00 USD | 170,720.00 USD | 83,380.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.60` | 1,720,000.00 USD | 1,720,000.00 USD | 275,800.00 USD | 0.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.80` | 73,340.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.90` | 1,400,000.00 USD | 1,400,000.00 USD | 277,640.00 USD | 0.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.00` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.20` | 1,070,000.00 USD | 1,070,000.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.50` | 863,560.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.80` | 616,600.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.10` | 347,370.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.40` | 110,560.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3988.70` | 76,450.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4061.80` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.40` | 228,770.00 USD | 228,770.00 USD | 0.00 USD | 0.00 USD | 167,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4074.70` | 483,070.00 USD | 483,070.00 USD | 138,080.00 USD | 0.00 USD | 116,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4077.40` | 534,660.00 USD | 534,660.00 USD | 87,320.00 USD | 0.00 USD | 144,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.00` | 1,420,000.00 USD | 1,420,000.00 USD | 773,860.00 USD | 0.00 USD | 167,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4081.60` | 913,400.00 USD | 913,400.00 USD | 178,090.00 USD | 0.00 USD | 200,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.30` | 2,920,000.00 USD | 2,920,000.00 USD | 1,110,000.00 USD | 0.00 USD | 384,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4085.80` | 1,500,000.00 USD | 1,500,000.00 USD | 362,630.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.60` | 4,030,000.00 USD | 4,030,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.00` | 1,610,000.00 USD | 1,610,000.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4091.90` | 4,690,000.00 USD | 4,690,000.00 USD | 514,970.00 USD | 0.00 USD | 144,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.20` | 1,870,000.00 USD | 1,870,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.20` | 5,100,000.00 USD | 5,100,000.00 USD | 310,220.00 USD | 0.00 USD | 100,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.40` | 2,100,000.00 USD | 2,100,000.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.50` | 5,560,000.00 USD | 5,560,000.00 USD | 415,790.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.60` | 2,460,000.00 USD | 2,460,000.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4104.80` | 6,060,000.00 USD | 6,060,000.00 USD | 367,480.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 2,900,000.00 USD | 2,900,000.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.10` | 6,680,000.00 USD | 6,680,000.00 USD | 537,000.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.00` | 3,130,000.00 USD | 3,130,000.00 USD | 205,470.00 USD | 0.00 USD | 26,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.40` | 7,170,000.00 USD | 7,170,000.00 USD | 434,270.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.20` | 3,270,000.00 USD | 3,270,000.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4117.70` | 7,510,000.00 USD | 7,510,000.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.40` | 3,330,000.00 USD | 3,330,000.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.00` | 7,820,000.00 USD | 7,820,000.00 USD | 272,900.00 USD | 0.00 USD | 32,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.60` | 3,350,000.00 USD | 3,350,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.30` | 8,140,000.00 USD | 8,140,000.00 USD | 252,890.00 USD | 0.00 USD | 70,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.60` | 8,330,000.00 USD | 8,330,000.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4134.90` | 8,610,000.00 USD | 8,610,000.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.20` | 8,820,000.00 USD | 8,820,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.40` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.50` | 9,060,000.00 USD | 9,060,000.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.60` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.80` | 9,210,000.00 USD | 9,210,000.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.80` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.10` | 9,380,000.00 USD | 9,380,000.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.00` | 3,500,000.00 USD | 3,500,000.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.40` | 9,680,000.00 USD | 9,680,000.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4157.20` | 3,610,000.00 USD | 3,610,000.00 USD | 36,330.00 USD | 0.00 USD | 72,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.70` | 10,130,000.00 USD | 10,130,000.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4161.40` | 3,790,000.00 USD | 3,790,000.00 USD | 87,190.00 USD | 0.00 USD | 100,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.00` | 10,930,000.00 USD | 10,930,000.00 USD | 584,890.00 USD | 0.00 USD | 215,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4165.60` | 4,090,000.00 USD | 4,090,000.00 USD | 190,490.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.30` | 11,410,000.00 USD | 11,410,000.00 USD | 384,920.00 USD | 0.00 USD | 91,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4169.80` | 4,150,000.00 USD | 4,150,000.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.60` | 11,650,000.00 USD | 11,650,000.00 USD | 181,290.00 USD | 0.00 USD | 60,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.00` | 4,270,000.00 USD | 4,270,000.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4177.90` | 11,900,000.00 USD | 11,900,000.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.20` | 4,380,000.00 USD | 4,380,000.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.20` | 12,100,000.00 USD | 12,100,000.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.40` | 4,540,000.00 USD | 4,540,000.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.50` | 12,360,000.00 USD | 12,360,000.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.60` | 4,780,000.00 USD | 4,780,000.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.80` | 4,890,000.00 USD | 4,890,000.00 USD | 91,590.00 USD | 0.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.80` | 12,670,000.00 USD | 12,670,000.00 USD | 285,320.00 USD | 0.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.00` | 4,970,000.00 USD | 4,970,000.00 USD | 73,130.00 USD | 0.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 12,910,000.00 USD | 12,910,000.00 USD | 205,140.00 USD | 0.00 USD | 38,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.20` | 5,000,000.00 USD | 5,000,000.00 USD | 30,260.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.40` | 13,040,000.00 USD | 13,040,000.00 USD | 101,170.00 USD | 0.00 USD | 24,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.40` | 5,020,000.00 USD | 5,020,000.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.70` | 13,220,000.00 USD | 13,220,000.00 USD | 164,070.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.00` | 13,340,000.00 USD | 13,340,000.00 USD | 82,850.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.30` | 13,450,000.00 USD | 13,450,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.60` | 13,560,000.00 USD | 13,560,000.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.90` | 13,690,000.00 USD | 13,690,000.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.20` | 13,770,000.00 USD | 13,770,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.50` | 13,820,000.00 USD | 13,820,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4233.80` | 13,870,000.00 USD | 13,870,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.10` | 13,880,000.00 USD | 13,880,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4379.80` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.00` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4388.20` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.60` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4392.40` | 5,070,000.00 USD | 5,070,000.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.90` | 13,940,000.00 USD | 13,940,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4396.60` | 5,100,000.00 USD | 5,100,000.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.20` | 14,050,000.00 USD | 14,050,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4400.80` | 5,150,000.00 USD | 5,150,000.00 USD | 26,650.00 USD | 0.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.50` | 14,260,000.00 USD | 14,260,000.00 USD | 143,560.00 USD | 0.00 USD | 62,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4405.00` | 5,240,000.00 USD | 5,240,000.00 USD | 51,120.00 USD | 0.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4405.50` | 5,240,000.00 USD | 5,240,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.80` | 14,420,000.00 USD | 14,420,000.00 USD | 116,280.00 USD | 0.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.10` | 14,560,000.00 USD | 14,560,000.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.40` | 14,610,000.00 USD | 14,610,000.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4418.70` | 14,690,000.00 USD | 14,690,000.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.00` | 14,730,000.00 USD | 14,730,000.00 USD | 31,340.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4427.10` | 14,810,000.00 USD | 14,810,000.00 USD | 59,230.00 USD | 0.00 USD | 17,850.00 USD | `Tier 1 CEX` |

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
| `1D` | `3581.80` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3584.50` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3586.00` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3588.80` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3590.20` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `3593.10` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3594.40` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 28,070.00 USD | 0.00 USD | 13,740.00 USD |
| `7D` | `3597.40` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3598.60` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 14,150.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `3601.70` | 14,940,000.00 USD | 0.00 USD | 14,940,000.00 USD | 175,610.00 USD | 0.00 USD | 67,670.00 USD |
| `1D` | `3602.80` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 36,990.00 USD | 0.00 USD | 51,100.00 USD |
| `7D` | `3606.00` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 134,320.00 USD | 0.00 USD | 53,650.00 USD |
| `1D` | `3607.00` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 48,270.00 USD | 0.00 USD | 14,630.00 USD |
| `7D` | `3610.30` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 83,580.00 USD | 0.00 USD | 21,070.00 USD |
| `1D` | `3611.20` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 25,560.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3614.60` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3615.40` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 31,290.00 USD | 0.00 USD | 10,040.00 USD |
| `7D` | `3618.90` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 40,780.00 USD | 0.00 USD | 8,780.00 USD |
| `1D` | `3619.60` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 42,080.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `3623.20` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 59,230.00 USD | 0.00 USD | 24,620.00 USD |
| `1D` | `3623.80` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 61,240.00 USD | 0.00 USD | 8,000.00 USD |
| `7D` | `3627.50` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3628.00` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 26,230.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3631.80` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 60,720.00 USD | 0.00 USD | 6,570.00 USD |
| `1D` | `3632.20` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 10,830.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `3636.10` | 14,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD |
| `1D` | `3636.40` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3640.40` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3644.70` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 17,720.00 USD | 0.00 USD | 11,980.00 USD |
| `7D` | `3649.00` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 24,860.00 USD | 0.00 USD | 4,150.00 USD |
| `7D` | `3653.30` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.60` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.90` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.20` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3821.20` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `3825.30` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3825.40` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `1D` | `3829.60` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `3829.60` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3833.80` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 81,530.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3833.90` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 69,040.00 USD | 0.00 USD | 20,340.00 USD |
| `1D` | `3838.00` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 38,960.00 USD | 0.00 USD | 72,460.00 USD |
| `7D` | `3838.20` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD |
| `1D` | `3842.20` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 93,750.00 USD | 0.00 USD | 113,110.00 USD |
| `7D` | `3842.50` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 557,810.00 USD | 0.00 USD | 224,650.00 USD |
| `1D` | `3846.40` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 180,250.00 USD | 0.00 USD | 99,600.00 USD |
| `7D` | `3846.80` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 535,820.00 USD | 0.00 USD | 157,990.00 USD |
| `1D` | `3850.60` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 41,090.00 USD | 0.00 USD | 31,860.00 USD |
| `7D` | `3851.10` | 11,750,000.00 USD | 0.00 USD | 11,750,000.00 USD | 231,930.00 USD | 0.00 USD | 79,320.00 USD |
| `1D` | `3854.80` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 109,230.00 USD | 0.00 USD | 31,990.00 USD |
| `7D` | `3855.40` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 219,990.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3859.00` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 125,320.00 USD | 0.00 USD | 20,940.00 USD |
| `7D` | `3859.70` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 174,170.00 USD | 0.00 USD | 22,980.00 USD |
| `1D` | `3863.20` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 136,260.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3864.00` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 204,130.00 USD | 0.00 USD | 73,250.00 USD |
| `1D` | `3867.40` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 175,670.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `3868.30` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 298,110.00 USD | 0.00 USD | 32,300.00 USD |
| `1D` | `3871.60` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 106,280.00 USD | 0.00 USD | 10,390.00 USD |
| `7D` | `3872.60` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD |
| `1D` | `3875.80` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 28,070.00 USD | 0.00 USD | 4,120.00 USD |
| `7D` | `3876.90` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `3880.00` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 30,410.00 USD | 0.00 USD | 813.93 USD |
| `7D` | `3881.20` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD |
| `7D` | `3885.50` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 124,650.00 USD | 0.00 USD | 24,550.00 USD |
| `7D` | `3889.80` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 85,430.00 USD | 0.00 USD | 25,820.00 USD |
| `7D` | `3894.10` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD |
| `7D` | `3898.40` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `3901.00` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3902.70` | 9,240,000.00 USD | 0.00 USD | 9,240,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD |
| `1D` | `3905.20` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `3907.00` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD |
| `1D` | `3909.40` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `3911.30` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 16,550.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3913.60` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 163,060.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `3915.60` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 287,340.00 USD | 0.00 USD | 116,230.00 USD |
| `1D` | `3917.80` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 55,700.00 USD | 0.00 USD | 144,920.00 USD |
| `7D` | `3919.90` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 674,750.00 USD | 0.00 USD | 199,110.00 USD |
| `1D` | `3922.00` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 187,870.00 USD | 0.00 USD | 214,020.00 USD |
| `7D` | `3924.20` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 1,200,000.00 USD | 0.00 USD | 464,810.00 USD |
| `1D` | `3926.20` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 382,350.00 USD | 0.00 USD | 211,410.00 USD |
| `7D` | `3928.50` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 913,310.00 USD | 0.00 USD | 195,870.00 USD |
| `1D` | `3930.40` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD |
| `7D` | `3932.80` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 380,870.00 USD | 0.00 USD | 128,930.00 USD |
| `1D` | `3934.60` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 237,090.00 USD | 0.00 USD | 75,970.00 USD |
| `7D` | `3937.10` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 466,400.00 USD | 0.00 USD | 74,650.00 USD |
| `1D` | `3938.80` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 215,190.00 USD | 0.00 USD | 39,310.00 USD |
| `7D` | `3941.40` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 287,460.00 USD | 0.00 USD | 104,590.00 USD |
| `1D` | `3943.00` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD |
| `7D` | `3945.70` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 468,070.00 USD | 0.00 USD | 118,120.00 USD |
| `1D` | `3947.20` | 780,210.00 USD | 0.00 USD | 780,210.00 USD | 352,330.00 USD | 0.00 USD | 46,140.00 USD |
| `7D` | `3950.00` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 529,640.00 USD | 0.00 USD | 78,520.00 USD |
| `1D` | `3951.40` | 381,740.00 USD | 0.00 USD | 381,740.00 USD | 189,460.00 USD | 0.00 USD | 21,560.00 USD |
| `7D` | `3954.30` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3955.60` | 170,720.00 USD | 0.00 USD | 170,720.00 USD | 83,380.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `3958.60` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 275,800.00 USD | 0.00 USD | 38,590.00 USD |
| `1D` | `3959.80` | 73,340.00 USD | 0.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `3962.90` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 277,640.00 USD | 0.00 USD | 56,430.00 USD |
| `1D` | `3964.00` | 606.18 USD | 0.00 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3967.20` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `3971.50` | 863,560.00 USD | 0.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3975.80` | 616,600.00 USD | 0.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.10` | 347,370.00 USD | 0.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.40` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3988.70` | 76,450.00 USD | 0.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3993.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3994.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4060.60` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4061.80` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `1D` | `4069.00` | 109,160.00 USD | 109,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,900.00 USD |
| `7D` | `4070.40` | 228,770.00 USD | 228,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 167,820.00 USD |
| `1D` | `4073.20` | 302,430.00 USD | 302,430.00 USD | 0.00 USD | 131,440.00 USD | 0.00 USD | 61,830.00 USD |
| `7D` | `4074.70` | 483,070.00 USD | 483,070.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 116,230.00 USD |
| `1D` | `4077.40` | 534,660.00 USD | 534,660.00 USD | 0.00 USD | 87,320.00 USD | 0.00 USD | 144,920.00 USD |
| `7D` | `4079.00` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 773,860.00 USD | 0.00 USD | 167,100.00 USD |
| `1D` | `4081.60` | 913,400.00 USD | 913,400.00 USD | 0.00 USD | 178,090.00 USD | 0.00 USD | 200,660.00 USD |
| `7D` | `4083.30` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 384,910.00 USD |
| `1D` | `4085.80` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 362,630.00 USD | 0.00 USD | 224,770.00 USD |
| `7D` | `4087.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD |
| `1D` | `4090.00` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 70,210.00 USD | 0.00 USD | 42,390.00 USD |
| `7D` | `4091.90` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 514,970.00 USD | 0.00 USD | 144,150.00 USD |
| `1D` | `4094.20` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `4096.20` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 310,220.00 USD | 0.00 USD | 100,990.00 USD |
| `1D` | `4098.40` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 188,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `4100.50` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 415,790.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4102.60` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 281,660.00 USD | 0.00 USD | 73,890.00 USD |
| `7D` | `4104.80` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 367,480.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4106.80` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD |
| `7D` | `4109.10` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 537,000.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4111.00` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 205,470.00 USD | 0.00 USD | 26,100.00 USD |
| `7D` | `4113.40` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 434,270.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4115.20` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `4117.70` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD |
| `1D` | `4119.40` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `4122.00` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 272,900.00 USD | 0.00 USD | 32,280.00 USD |
| `1D` | `4123.60` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4126.30` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 252,890.00 USD | 0.00 USD | 70,690.00 USD |
| `7D` | `4130.60` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD |
| `7D` | `4134.90` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD |
| `7D` | `4139.20` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4140.40` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4143.50` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD |
| `1D` | `4144.60` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4147.80` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD |
| `1D` | `4148.80` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4152.10` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 116,380.00 USD | 0.00 USD | 57,380.00 USD |
| `1D` | `4153.00` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 65,720.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `4156.40` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4157.20` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 36,330.00 USD | 0.00 USD | 72,460.00 USD |
| `7D` | `4160.70` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD |
| `1D` | `4161.40` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 87,190.00 USD | 0.00 USD | 100,330.00 USD |
| `7D` | `4165.00` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 584,890.00 USD | 0.00 USD | 215,140.00 USD |
| `1D` | `4165.60` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 190,490.00 USD | 0.00 USD | 101,630.00 USD |
| `7D` | `4169.30` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 384,920.00 USD | 0.00 USD | 91,530.00 USD |
| `1D` | `4169.80` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 35,100.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `4173.60` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 181,290.00 USD | 0.00 USD | 60,200.00 USD |
| `1D` | `4174.00` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 90,290.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4177.90` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD |
| `1D` | `4178.20` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 85,070.00 USD | 0.00 USD | 19,360.00 USD |
| `7D` | `4182.20` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD |
| `1D` | `4182.40` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 136,450.00 USD | 0.00 USD | 24,010.00 USD |
| `7D` | `4186.50` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD |
| `1D` | `4186.60` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 207,850.00 USD | 0.00 USD | 34,560.00 USD |
| `1D` | `4190.80` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 91,590.00 USD | 0.00 USD | 14,650.00 USD |
| `7D` | `4190.80` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 285,320.00 USD | 0.00 USD | 24,310.00 USD |
| `1D` | `4195.00` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 73,130.00 USD | 0.00 USD | 7,830.00 USD |
| `7D` | `4195.10` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 38,220.00 USD |
| `1D` | `4199.20` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `4199.40` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 101,170.00 USD | 0.00 USD | 24,830.00 USD |
| `1D` | `4203.40` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4203.70` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 164,070.00 USD | 0.00 USD | 23,560.00 USD |
| `7D` | `4208.00` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 82,850.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.30` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.60` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD |
| `7D` | `4220.90` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD |
| `7D` | `4225.20` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.50` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4233.80` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.10` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4379.80` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD |
| `7D` | `4380.00` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4388.20` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,810.00 USD |
| `7D` | `4388.60` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4392.40` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 18,160.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4392.90` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4396.60` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 16,880.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `4397.20` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4400.80` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 26,650.00 USD | 0.00 USD | 23,970.00 USD |
| `7D` | `4401.50` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 62,400.00 USD |
| `1D` | `4405.00` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 51,120.00 USD | 0.00 USD | 39,640.00 USD |
| `1D` | `4405.50` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4405.80` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 116,280.00 USD | 0.00 USD | 48,470.00 USD |
| `7D` | `4410.10` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD |
| `7D` | `4414.40` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD |
| `7D` | `4418.70` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD |
| `7D` | `4423.00` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 31,340.00 USD | 0.00 USD | 8,780.00 USD |
| `7D` | `4427.10` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 17,850.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.77M` | Total OI Tokens: `68,797.7 PAXG`
  * 1h OI Change: `-0.07%` | 4h OI Change: `-0.39%` | 24h OI Change: `-0.11%`
  * Exchange Breakdown: Binance=`104.90M` | Bybit=`24.27M` | OKX=`-` | Hyperliquid=`24.76M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.31K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0029%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0029%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0012%` | **USDT Bitget** | `0.0050%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `46.86%` | `53.14%` | `0.88` | 651,640.00 USD |
| `15M` | `Binance` | `45.88%` | `54.12%` | `0.85` | 194,260.00 USD |
| `15M` | `OKX` | `58.57%` | `41.43%` | `1.41` | 91,580.00 USD |
| `15M` | `Bybit` | `59.97%` | `40.03%` | `1.50` | 40,620.00 USD |
| `15M` | `KuCoin` | `52.69%` | `47.31%` | `1.11` | 51,900.00 USD |
| `15M` | `Gate` | `69.88%` | `30.12%` | `2.32` | 6,640.00 USD |
| `15M` | `Bitget` | `77.73%` | `22.27%` | `3.49` | 11,780.00 USD |
| `15M` | `BingX` | `54.39%` | `45.61%` | `1.19` | 29,160.00 USD |
| `15M` | `MEXC` | `27.32%` | `72.68%` | `0.38` | 53,440.00 USD |
| `15M` | `Bitunix` | `53.08%` | `46.92%` | `1.13` | 5,460.00 USD |
| `15M` | `Hyperliquid` | `4.44%` | `95.56%` | `0.05` | 27,840.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.14%` | `51.86%` | `0.93` | 104,430.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 5.82 USD |
| `15M` | `WhiteBIT` | `43.44%` | `56.56%` | `0.77` | 26,770.00 USD |
| `15M` | `HTX` | `23.25%` | `76.75%` | `0.30` | 249.15 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 479.62 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `1.12%` | `98.88%` | `0.01` | 7,060.00 USD |
| `15M` | `Whale Positions` | `45.88%` | `54.12%` | `0.85` | 194,260.00 USD |
| `15M` | `Global Accounts` | `46.86%` | `53.14%` | `0.88` | 651,640.00 USD |
| `1H` | `PAXG` | `44.61%` | `55.39%` | `0.81` | 18,760,000.00 USD |
| `1H` | `Binance` | `49.57%` | `50.43%` | `0.98` | 6,840,000.00 USD |
| `1H` | `OKX` | `48.26%` | `51.74%` | `0.93` | 3,290,000.00 USD |
| `1H` | `Bybit` | `44.3%` | `55.7%` | `0.80` | 1,630,000.00 USD |
| `1H` | `KuCoin` | `47.91%` | `52.09%` | `0.92` | 645,090.00 USD |
| `1H` | `Gate` | `53.74%` | `46.26%` | `1.16` | 388,530.00 USD |
| `1H` | `Bitget` | `56.93%` | `43.07%` | `1.32` | 395,830.00 USD |
| `1H` | `BingX` | `10.87%` | `89.13%` | `0.12` | 784,220.00 USD |
| `1H` | `MEXC` | `62.41%` | `37.59%` | `1.66` | 158,670.00 USD |
| `1H` | `Bitunix` | `55.02%` | `44.98%` | `1.22` | 262,720.00 USD |
| `1H` | `Hyperliquid` | `57.11%` | `42.89%` | `1.33` | 62,230.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.8%` | `48.2%` | `1.07` | 2,910,000.00 USD |
| `1H` | `Crypto.com` | `0.4%` | `99.6%` | `0.00` | 3,470.00 USD |
| `1H` | `WhiteBIT` | `1.1%` | `98.9%` | `0.01` | 1,290,000.00 USD |
| `1H` | `HTX` | `47.92%` | `52.08%` | `0.92` | 20,160.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `34.55%` | `65.45%` | `0.53` | 68,150.00 USD |
| `1H` | `Aster` | `48.97%` | `51.03%` | `0.96` | 4,500.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `88.59%` | `11.41%` | `7.76` | 12,670.00 USD |
| `1H` | `Whale Positions` | `49.57%` | `50.43%` | `0.98` | 6,840,000.00 USD |
| `1H` | `Global Accounts` | `44.61%` | `55.39%` | `0.81` | 18,760,000.00 USD |
| `4H` | `PAXG` | `47.76%` | `52.24%` | `0.91` | 17,860,000.00 USD |
| `4H` | `Binance` | `49.05%` | `50.95%` | `0.96` | 6,120,000.00 USD |
| `4H` | `OKX` | `54.74%` | `45.26%` | `1.21` | 1,490,000.00 USD |
| `4H` | `Bybit` | `48.85%` | `51.15%` | `0.96` | 1,740,000.00 USD |
| `4H` | `KuCoin` | `50.02%` | `49.98%` | `1.00` | 2,140,000.00 USD |
| `4H` | `Gate` | `55.79%` | `44.21%` | `1.26` | 437,080.00 USD |
| `4H` | `Bitget` | `47.44%` | `52.56%` | `0.90` | 1,030,000.00 USD |
| `4H` | `BingX` | `27.38%` | `72.62%` | `0.38` | 1,840,000.00 USD |
| `4H` | `MEXC` | `47.22%` | `52.78%` | `0.89` | 885,240.00 USD |
| `4H` | `Bitunix` | `40.81%` | `59.19%` | `0.69` | 243,500.00 USD |
| `4H` | `Hyperliquid` | `42.41%` | `57.59%` | `0.74` | 350,250.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.86%` | `50.14%` | `0.99` | 891,900.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `67.31%` | `32.69%` | `2.06` | 557,370.00 USD |
| `4H` | `HTX` | `48.95%` | `51.05%` | `0.96` | 4,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `67.26%` | `32.74%` | `2.05` | 8,460.00 USD |
| `4H` | `Aster` | `50.82%` | `49.18%` | `1.03` | 111,260.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.64%` | `47.36%` | `1.11` | 12,310.00 USD |
| `4H` | `Whale Positions` | `49.05%` | `50.95%` | `0.96` | 6,120,000.00 USD |
| `4H` | `Global Accounts` | `47.76%` | `52.24%` | `0.91` | 17,860,000.00 USD |


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
| `5m` | -102,120.00 USD | 39,320.00 USD | **`DISTRIBUTION`** |
| `15m` | -128,390.00 USD | 56,320.00 USD | **`DISTRIBUTION`** |
| `30m` | -275,600.00 USD | 301,910.00 USD | **`ACCUMULATION`** |
| `1h` | -401,570.00 USD | 656,740.00 USD | **`ACCUMULATION`** |
| `2h` | -1,100,000.00 USD | 627,290.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,720,000.00 USD | -609,070.00 USD | **`DISTRIBUTION`** |
| `6h` | 179,090.00 USD | 355,960.00 USD | **`ACCUMULATION`** |
| `8h` | -96,860.00 USD | -101,450.00 USD | **`DISTRIBUTION`** |
| `12h` | -56,130.00 USD | -315,090.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,210,000.00 USD | 830,630.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,910,000.00 USD | -8,190,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,290,000.00 USD | -71,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-102.12K` | 15m=`-128.39K` | 1h=`-401.57K` | 24h=`-1.21M`
* Futures Capital Netflows: 5m=`+39.32K` | 15m=`+56.32K` | 1h=`+656.74K` | 24h=`+830.63K`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3973.14` (Risk Distance: `9.71` pts)
  * +2.5R Take Profit: `4007.12`
  * Mathematical Lot Sizing: **`1.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.64` (Risk Distance: `9.71` pts)
  * +2.5R Take Profit: `3983.66`
  * Mathematical Lot Sizing: **`1.02 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4020.40`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
