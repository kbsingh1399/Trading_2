# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 04:38:03 IST` (`2026-10-29 23:08:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4016.88` | **Live Ask Quote**: `4016.96` | **Mid Price**: `4016.92`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4029.42` | VWAP Z-Score: `-0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.57` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.31` | Lower -3.00σ Band: `3994.52`
  * Upper +2.51σ Band: `4058.61` | Lower -2.51σ Band: `4000.22`
  * Upper +2.01σ Band: `4052.80` | Lower -2.01σ Band: `4006.04`
  * Upper +2.00σ Band: `4052.68` | Lower -2.00σ Band: `4006.16`
  * Upper +1.28σ Band: `4044.31` | Lower -1.28σ Band: `4014.53`
  * Upper +1.00σ Band: `4041.05` | Lower -1.00σ Band: `4017.79`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4020.62` | EMA-20=`4019.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4022.74` (Slope: `+0.0000`) | EMA-100=`4028.48`
  * Institutional Anchors: EMA-144=`4030.49` | EMA-200=`4030.89` (Slope: `-0.0324`) | EMA-233=`4030.57`
- **Range Boundaries**: 24H High=`4069.28` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4023.63` (Distance: `-0.15%`)
  * Point of Control (POC) = `4020.95` (Distance: `-0.09%`)
  * Value Area Low (VAL) = `4017.76` (Distance: `-0.01%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4016.38`
  * London Session (08:00-16:00 UTC): High=`4032.99` | Low=`4000.85`
  * New York Session (13:00-21:00 UTC): High=`4041.02` | Low=`3992.82`
  * Initial Balance (First Hour): IB High=`4028.97` | IB Low=`4004.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4000.85` - `4032.99`
  * Optimal Trade Entry (OTE 0.705): `4024.95`
  * Structural Invalidation Anchor (0.786): `4049.06`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4028.18` | `4028.94` | `4025.59` | `4025.59` | `29` | 115,117.17 USD | -71,794.64 USD | `-62.37%` | 2,034,906.69 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4025.54` | `4025.54` | `4020.54` | `4020.55` | `56` | 226,360.81 USD | -44,355.72 USD | `-19.60%` | 1,990,550.96 USD | `-0.92` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4020.55` | `4021.27` | `4020.54` | `4021.05` | `5` | 18,576.33 USD | 10,903.84 USD | `+58.70%` | 2,001,454.80 USD | `-0.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4021.48` | `4026.89` | `4021.28` | `4026.36` | `116` | 466,788.35 USD | 24,890.09 USD | `+5.33%` | 1,885,355.81 USD | `+0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4026.37` | `4029.17` | `4025.59` | `4025.59` | `113` | 456,921.14 USD | 49,642.38 USD | `+10.86%` | 1,934,998.19 USD | `+0.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4025.54` | `4025.54` | `4020.54` | `4021.05` | `61` | 244,937.13 USD | -33,451.88 USD | `-13.66%` | 1,901,546.31 USD | `-0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,132,085.43 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4029.17` | `4017.72` | `4025.59` | `562` | 2,260,235.02 USD | 263,421.07 USD | `+11.65%` | 1,395,506.50 USD | `+0.51` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4025.54` | `4025.54` | `4020.54` | `4021.05` | `61` | 244,937.13 USD | -33,451.88 USD | `-13.66%` | 1,362,054.62 USD | `-0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4021.05` | `2,274` | 9,152,587.79 USD | 114,907.29 USD | `+1.26%` | 1,362,054.62 USD | `-0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4021.05` | `2,274` | 9,152,587.79 USD | 114,907.29 USD | `+1.26%` | 1,362,054.62 USD | `-0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4017.50` | `5.3839` | 21,629.82 USD | 2,236,461.94 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4017.60` | `0.9334` | 3,750.03 USD | 2,214,832.12 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4017.70` | `14.0874` | 56,598.95 USD | 2,211,082.09 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4017.80` | `41.6793` | 167,459.09 USD | 2,154,483.14 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4017.90` | `12.6049` | 50,645.23 USD | 1,987,024.05 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4018.00` | `12.9397` | 51,991.71 USD | 1,936,378.83 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4018.10` | `4.9797` | 20,008.93 USD | 1,884,387.11 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4018.20` | `0.9333` | 3,750.19 USD | 1,864,378.18 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4018.30` | `59.0859` | 237,424.87 USD | 1,860,627.99 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4018.40` | `4.6660` | 18,749.85 USD | 1,623,203.12 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4018.50` | `10.0464` | 40,371.46 USD | 1,604,453.27 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4018.60` | `18.1416` | 72,903.83 USD | 1,564,081.81 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4018.70` | `5.1689` | 20,772.26 USD | 1,491,177.97 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4018.80` | `13.9826` | 56,193.27 USD | 1,470,405.72 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4019.00` | `285.7739` | 1,148,525.30 USD | 1,414,212.44 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4019.10` | `21.7037` | 87,229.34 USD | 265,687.14 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4019.20` | `0.8477` | 3,407.08 USD | 178,457.80 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4019.30` | `10.5900` | 42,564.39 USD | 175,050.72 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4019.40` | `0.0253` | 101.69 USD | 132,486.34 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `4019.50` | `32.9356` | 132,384.64 USD | 132,384.64 USD | `13 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4019.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,019.55` | `0.00%` | `-` |
| `ASK` | `4019.60` | `91.9131` | 369,453.90 USD | 369,453.90 USD | `12 orders` | `+0.00%` | `-` |
| `ASK` | `4019.70` | `9.3404` | 37,545.61 USD | 406,999.50 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4019.80` | `10.1935` | 40,975.83 USD | 447,975.33 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4019.90` | `1.0448` | 4,199.99 USD | 452,175.33 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4020.00` | `5.2842` | 21,242.48 USD | 473,417.81 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4020.10` | `78.6059` | 316,003.58 USD | 789,421.39 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4020.20` | `26.9123` | 108,192.83 USD | 897,614.22 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4020.30` | `11.0874` | 44,574.67 USD | 942,188.89 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4020.40` | `15.2851` | 61,452.22 USD | 1,003,641.11 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4020.50` | `14.4908` | 58,260.26 USD | 1,061,901.37 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `4020.60` | `4.9779` | 20,014.14 USD | 1,081,915.51 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.70` | `6.2053` | 24,949.65 USD | 1,106,865.16 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.80` | `8.7405` | 35,143.80 USD | 1,142,008.97 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.90` | `0.1094` | 439.89 USD | 1,142,448.85 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4021.00` | `16.2525` | 65,351.30 USD | 1,207,800.15 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.10` | `13.9376` | 56,044.48 USD | 1,263,844.64 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4021.20` | `9.4241` | 37,896.19 USD | 1,301,740.83 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4021.30` | `17.1230` | 68,856.72 USD | 1,370,597.55 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4021.40` | `4.1568` | 16,716.16 USD | 1,387,313.70 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4021.50` | `1.3032` | 5,240.82 USD | 1,392,554.52 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,627,668.50 USD | `6,365.38` | `4188.90` | `4026.00` | `32919.27` | 1,036,302.80 USD | `+4.04%` | `4X Cross` |
| `52` | `0x4692...164f` | `SHORT` | 25,465,120.35 USD | `6,325.01` | `4132.69` | `4026.00` | `13839.40` | 674,235.50 USD | `+2.65%` | `5X Cross` |
| `66` | `0xb83d...6e36` | `SHORT` | 23,631,627.99 USD | `5,869.90` | `4228.86` | `4026.00` | `30649.19` | 1,191,393.94 USD | `+5.04%` | `5X Cross` |
| `95` | `0xec0b...b078` | `LONG` | 19,441,662.07 USD | `4,828.91` | `4157.43` | `4026.00` | `2240.73` | -634,220.25 USD | `-3.26%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,228,299.40 USD | `3,534.02` | `4129.09` | `4026.00` | `462.61` | -363,979.46 USD | `-2.56%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,158,153.16 USD | `3,268.21` | `4228.94` | `4026.00` | `4400.12` | 662,925.97 USD | `+5.04%` | `25X Cross` |
| `176` | `0xa742...e390` | `SHORT` | 11,675,690.40 USD | `2,900.00` | `4364.92` | `4026.00` | `4235.67` | 982,585.93 USD | `+8.42%` | `20X Cross` |
| `256` | `0x3678...b209` | `LONG` | 8,857,420.00 USD | `2,200.00` | `4176.09` | `4026.00` | `2701.54` | -329,999.30 USD | `-3.73%` | `25X Cross` |
| `257` | `0x41e5...0825` | `SHORT` | 8,856,980.00 USD | `2,200.00` | `4112.20` | `4026.00` | `4331.15` | 189,874.59 USD | `+2.14%` | `20X Cross` |
| `259` | `0xfc66...ca06` | `SHORT` | 8,843,588.25 USD | `2,196.67` | `4031.28` | `4026.00` | `10393.57` | 11,833.46 USD | `+0.13%` | `3X Cross` |
| `293` | `0xacb6...efbd` | `SHORT` | 7,952,638.46 USD | `1,975.37` | `4048.55` | `4026.00` | `6502.36` | 44,753.25 USD | `+0.56%` | `6X Cross` |
| `363` | `0xc26c...b8f4` | `LONG` | 6,361,043.94 USD | `1,579.95` | `4075.62` | `4026.00` | `0.000000` | -78,253.03 USD | `-1.23%` | `1X Cross` |
| `399` | `0x12d2...f97f` | `LONG` | 5,644,081.52 USD | `1,401.94` | `4278.91` | `4026.00` | `3134.13` | -354,709.06 USD | `-6.28%` | `20X Cross` |
| `546` | `0x63da...8add` | `LONG` | 4,026,100.00 USD | `1,000.00` | `4021.46` | `4026.00` | `3564.11` | 4,639.04 USD | `+0.12%` | `25X Cross` |
| `556` | `0x354b...6425` | `LONG` | 3,953,497.74 USD | `981.97` | `4031.85` | `4026.00` | `0.000000` | -5,650.58 USD | `-0.14%` | `10X Cross` |
| `570` | `0x9aa5...58af` | `LONG` | 3,911,927.86 USD | `971.64` | `4279.98` | `4026.00` | `0.000000` | -246,681.23 USD | `-6.31%` | `20X Cross` |
| `593` | `0xf3dc...1672` | `LONG` | 3,747,267.21 USD | `930.74` | `4024.62` | `4026.00` | `3344.05` | 1,374.65 USD | `+0.04%` | `20X Cross` |
| `666` | `0x4a20...3c26` | `LONG` | 3,371,454.93 USD | `837.40` | `4599.73` | `4026.00` | `0.000000` | -480,365.45 USD | `-14.25%` | `20X Cross` |
| `813` | `0x0fac...7a0a` | `LONG` | 2,763,857.26 USD | `686.49` | `4290.34` | `4026.00` | `1524.32` | -181,401.44 USD | `-6.56%` | `25X Cross` |
| `865` | `0xd8c5...99b0` | `SHORT` | 2,586,185.06 USD | `642.35` | `4175.35` | `4026.00` | `33022.37` | 95,876.11 USD | `+3.71%` | `4X Cross` |
| `894` | `0x625e...a354` | `SHORT` | 2,496,058.00 USD | `620.00` | `4122.81` | `4026.00` | `4342.25` | 60,089.03 USD | `+2.41%` | `20X Cross` |
| `931` | `0xeae3...e8ad` | `SHORT` | 2,415,660.00 USD | `600.00` | `4104.77` | `4026.00` | `4325.27` | 47,205.11 USD | `+1.95%` | `20X Cross` |
| `933` | `0xf285...fa82` | `LONG` | 2,408,034.16 USD | `598.11` | `4146.45` | `4026.00` | `3891.24` | -71,985.39 USD | `-2.99%` | `25X Cross` |
| `955` | `0x12f7...8750` | `LONG` | 2,357,727.24 USD | `585.61` | `4082.77` | `4026.00` | `2539.70` | -33,189.74 USD | `-1.41%` | `10X Cross` |
| `1088` | `0x413c...886c` | `LONG` | 2,013,050.00 USD | `500.00` | `4010.43` | `4026.00` | `0.000000` | 7,833.77 USD | `+0.39%` | `2X Cross` |
| `1100` | `0x61ce...a62b` | `SHORT` | 2,002,998.84 USD | `497.50` | `4071.66` | `4026.00` | `4712.96` | 22,669.95 USD | `+1.13%` | `20X Cross` |
| `1104` | `0x0593...40f9` | `LONG` | 1,997,658.22 USD | `496.18` | `4024.57` | `4026.00` | `3701.73` | 754.39 USD | `+0.04%` | `10X Isolated` |
| `1179` | `0x2edd...8179` | `LONG` | 1,897,261.39 USD | `470.91` | `4164.68` | `4028.90` | `0.000000` | -63,939.93 USD | `-3.37%` | `10X Cross` |
| `1222` | `0xead5...69f2` | `LONG` | 1,826,888.60 USD | `453.78` | `4220.88` | `4026.00` | `3538.94` | -88,479.46 USD | `-4.84%` | `5X Isolated` |
| `1287` | `0x7a6d...f79c` | `SHORT` | 1,725,896.15 USD | `428.38` | `4136.09` | `4028.90` | `5759.69` | 45,918.85 USD | `+2.66%` | `10X Cross` |
| `1309` | `0x46fc...1195` | `LONG` | 1,676,435.03 USD | `416.39` | `4054.56` | `4026.00` | `2189.38` | -11,850.96 USD | `-0.71%` | `20X Cross` |
| `1368` | `0xee02...309d` | `SHORT` | 1,610,440.00 USD | `400.00` | `4438.84` | `4026.00` | `4226.89` | 165,098.60 USD | `+10.25%` | `25X Isolated` |
| `1370` | `0x6d15...d374` | `LONG` | 1,610,360.00 USD | `400.00` | `4068.25` | `4026.00` | `3841.81` | -16,940.00 USD | `-1.05%` | `25X Cross` |
| `1403` | `0x02a7...fe9f` | `SHORT` | 1,570,179.00 USD | `390.00` | `4055.02` | `4026.00` | `4306.71` | 11,280.25 USD | `+0.72%` | `25X Cross` |
| `1438` | `0x51f6...2b39` | `LONG` | 1,538,093.01 USD | `381.76` | `4233.94` | `4028.90` | `0.000000` | -78,278.63 USD | `-5.09%` | `10X Cross` |
| `1444` | `0x7e77...b8d2` | `SHORT` | 1,529,918.00 USD | `380.00` | `4131.92` | `4026.00` | `4293.51` | 40,211.64 USD | `+2.63%` | `20X Cross` |
| `1457` | `0x72c2...9b37` | `LONG` | 1,502,263.93 USD | `373.13` | `4000.98` | `4026.00` | `3778.05` | 9,370.41 USD | `+0.62%` | `13X Isolated` |
| `1501` | `0xaa44...b844` | `LONG` | 1,449,396.00 USD | `360.00` | `4043.10` | `4026.00` | `2820.95` | -6,121.63 USD | `-0.42%` | `4X Cross` |
| `1502` | `0x781e...96b7` | `SHORT` | 1,448,844.82 USD | `359.61` | `4364.97` | `4028.90` | `13591.40` | 120,856.11 USD | `+8.34%` | `10X Cross` |
| `1625` | `0xa41f...d50a` | `LONG` | 1,324,368.52 USD | `328.96` | `4468.89` | `4026.00` | `3833.19` | -145,729.33 USD | `-11.00%` | `15X Cross` |
| `1657` | `0xbf5a...88ba` | `SHORT` | 1,278,910.39 USD | `317.65` | `4091.80` | `4026.00` | `9874.78` | 20,872.64 USD | `+1.63%` | `20X Cross` |
| `1689` | `0xff31...ff6c` | `SHORT` | 1,248,091.00 USD | `310.00` | `4372.43` | `4026.00` | `4789.18` | 107,364.38 USD | `+8.60%` | `10X Isolated` |
| `1699` | `0xada6...6f88` | `LONG` | 1,240,442.62 USD | `308.10` | `4166.46` | `4026.00` | `1937.12` | -43,246.40 USD | `-3.49%` | `5X Cross` |
| `1872` | `0x50e2...d770` | `LONG` | 1,088,526.19 USD | `270.37` | `4243.58` | `4026.00` | `2562.10` | -58,800.27 USD | `-5.40%` | `20X Cross` |
| `1887` | `0x4c92...4f17` | `SHORT` | 1,073,843.41 USD | `266.72` | `4260.98` | `4026.00` | `6518.25` | 62,648.83 USD | `+5.83%` | `20X Cross` |
| `1944` | `0xd346...c4f3` | `LONG` | 1,027,355.24 USD | `255.17` | `4188.66` | `4026.00` | `3310.43` | -41,481.27 USD | `-4.04%` | `5X Isolated` |
| `1990` | `0x1581...463b` | `LONG` | 1,006,475.00 USD | `250.00` | `4003.77` | `4026.00` | `3555.39` | 5,531.41 USD | `+0.55%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.96` (Vol: 346,900.00 USD, Dist: `+2.03%`) | Long MP=`3936.30` (Vol: 356,200.00 USD, Dist: `--2.30%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.70%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.29%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.69%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.28%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.04%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.63%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,280,000.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.90` | 3,860,000.00 USD | 3,860,000.00 USD | 37,670.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,060,000.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 3,820,000.00 USD | 3,820,000.00 USD | 67,080.00 USD | 0.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 16,000,000.00 USD | 16,000,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.10` | 3,740,000.00 USD | 3,740,000.00 USD | 35,590.00 USD | 0.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,900,000.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.20` | 3,700,000.00 USD | 3,700,000.00 USD | 31,790.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,720,000.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.30` | 3,660,000.00 USD | 3,660,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,610,000.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.40` | 3,630,000.00 USD | 3,630,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,470,000.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.50` | 3,590,000.00 USD | 3,590,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.60` | 3,580,000.00 USD | 3,580,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,370,000.00 USD | 15,370,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.70` | 3,570,000.00 USD | 3,570,000.00 USD | 14,200.00 USD | 0.00 USD | 1,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,350,000.00 USD | 15,350,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.80` | 3,550,000.00 USD | 3,550,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,320,000.00 USD | 15,320,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,290,000.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,260,000.00 USD | 15,260,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,250,000.00 USD | 15,250,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,890,000.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,400,000.00 USD | 14,400,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,870,000.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.60` | 3,550,000.00 USD | 3,550,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,540,000.00 USD | 13,540,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.70` | 3,540,000.00 USD | 3,540,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,240,000.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.80` | 3,450,000.00 USD | 3,450,000.00 USD | 127,460.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,950,000.00 USD | 12,950,000.00 USD | 183,740.00 USD | 0.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.90` | 3,300,000.00 USD | 3,300,000.00 USD | 207,510.00 USD | 0.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,700,000.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.00` | 3,070,000.00 USD | 3,070,000.00 USD | 144,700.00 USD | 0.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,160,000.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.10` | 2,900,000.00 USD | 2,900,000.00 USD | 126,020.00 USD | 0.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,740,000.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.20` | 2,760,000.00 USD | 2,760,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,190,000.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.30` | 2,660,000.00 USD | 2,660,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,850,000.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.40` | 2,530,000.00 USD | 2,530,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,710,000.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.50` | 2,490,000.00 USD | 2,490,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,600,000.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.60` | 2,470,000.00 USD | 2,470,000.00 USD | 66,940.00 USD | 0.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,480,000.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.70` | 2,390,000.00 USD | 2,390,000.00 USD | 11,950.00 USD | 0.00 USD | 133.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,360,000.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.80` | 2,380,000.00 USD | 2,380,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,280,000.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,180,000.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,160,000.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,430,000.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,490,000.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,600,000.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 2,360,000.00 USD | 2,360,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,760,000.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.70` | 2,300,000.00 USD | 2,300,000.00 USD | 177,090.00 USD | 0.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,290,000.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.80` | 2,110,000.00 USD | 2,110,000.00 USD | 305,210.00 USD | 0.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,630,000.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.90` | 1,750,000.00 USD | 1,750,000.00 USD | 347,350.00 USD | 0.00 USD | 54,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 123,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.00` | 1,350,000.00 USD | 1,350,000.00 USD | 346,950.00 USD | 0.00 USD | 38,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.10` | 965,830.00 USD | 965,830.00 USD | 181,840.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.20` | 754,530.00 USD | 754,530.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.30` | 464,400.00 USD | 464,400.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 308,770.00 USD | 308,770.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.50` | 258,690.00 USD | 258,690.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.60` | 164,090.00 USD | 164,090.00 USD | 97,640.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.70` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.80` | 19,950.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.50` | 29,250.00 USD | 29,250.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.70` | 512,670.00 USD | 512,670.00 USD | 255,730.00 USD | 0.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 990,060.00 USD | 990,060.00 USD | 428,840.00 USD | 0.00 USD | 48,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 506,510.00 USD | 0.00 USD | 106,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.90` | 1,310,000.00 USD | 1,310,000.00 USD | 278,400.00 USD | 0.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.00` | 1,570,000.00 USD | 1,570,000.00 USD | 229,730.00 USD | 0.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.10` | 1,770,000.00 USD | 1,770,000.00 USD | 185,530.00 USD | 0.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.20` | 2,010,000.00 USD | 2,010,000.00 USD | 207,400.00 USD | 0.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.30` | 2,100,000.00 USD | 2,100,000.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.40` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.50` | 2,250,000.00 USD | 2,250,000.00 USD | 127,000.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 2,330,000.00 USD | 2,330,000.00 USD | 71,850.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.70` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.80` | 2,360,000.00 USD | 2,360,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.50` | 2,420,000.00 USD | 2,420,000.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.60` | 2,520,000.00 USD | 2,520,000.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.70` | 2,680,000.00 USD | 2,680,000.00 USD | 131,510.00 USD | 0.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 249,690.00 USD | 0.00 USD | 62,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.80` | 2,890,000.00 USD | 2,890,000.00 USD | 190,610.00 USD | 0.00 USD | 27,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,470,000.00 USD | 13,470,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.90` | 3,060,000.00 USD | 3,060,000.00 USD | 150,560.00 USD | 0.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,790,000.00 USD | 13,790,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.00` | 3,170,000.00 USD | 3,170,000.00 USD | 90,920.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,230,000.00 USD | 14,230,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.10` | 3,290,000.00 USD | 3,290,000.00 USD | 122,050.00 USD | 0.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,570,000.00 USD | 14,570,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.20` | 3,380,000.00 USD | 3,380,000.00 USD | 65,640.00 USD | 0.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.30` | 3,420,000.00 USD | 3,420,000.00 USD | 22,630.00 USD | 0.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.40` | 3,440,000.00 USD | 3,440,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,930,000.00 USD | 14,930,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.50` | 3,500,000.00 USD | 3,500,000.00 USD | 47,950.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.60` | 3,530,000.00 USD | 3,530,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,140,000.00 USD | 15,140,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.70` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.80` | 3,550,000.00 USD | 3,550,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,600,000.00 USD | 15,600,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,800,000.00 USD | 15,800,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.30` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 674.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,930,000.00 USD | 15,930,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.40` | 3,580,000.00 USD | 3,580,000.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.50` | 3,600,000.00 USD | 3,600,000.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.60` | 3,640,000.00 USD | 3,640,000.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.70` | 3,710,000.00 USD | 3,710,000.00 USD | 59,900.00 USD | 0.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.20` | 3,730,000.00 USD | 3,730,000.00 USD | 16,560.00 USD | 0.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,530,000.00 USD | 16,530,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.90` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 37,670.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3619.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3623.00` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 67,080.00 USD | 0.00 USD | 10,850.00 USD |
| `7D` | `3623.90` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.10` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 35,590.00 USD | 0.00 USD | 5,730.00 USD |
| `7D` | `3628.10` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.20` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 31,790.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3632.30` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.30` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.40` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3640.70` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.50` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.60` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3649.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.70` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 14,200.00 USD | 0.00 USD | 1,120.00 USD |
| `7D` | `3653.30` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.80` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.60` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `3854.90` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.70` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3860.80` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 127,460.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `3863.30` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 183,740.00 USD | 0.00 USD | 71,710.00 USD |
| `1D` | `3864.90` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 207,510.00 USD | 0.00 USD | 25,460.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3869.00` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 144,700.00 USD | 0.00 USD | 21,610.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3873.10` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 126,020.00 USD | 0.00 USD | 17,270.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3877.20` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3880.10` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3881.30` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD |
| `7D` | `3884.30` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3885.40` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `3888.50` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.50` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `3892.70` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.60` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 66,940.00 USD | 0.00 USD | 5,880.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.70` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 11,950.00 USD | 0.00 USD | 133.60 USD |
| `7D` | `3901.10` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.80` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.60` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.70` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 177,090.00 USD | 0.00 USD | 7,390.00 USD |
| `7D` | `3938.90` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.80` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 305,210.00 USD | 0.00 USD | 52,850.00 USD |
| `7D` | `3943.10` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD |
| `1D` | `3946.90` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 347,350.00 USD | 0.00 USD | 54,250.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 123,890.00 USD |
| `1D` | `3951.00` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 346,950.00 USD | 0.00 USD | 38,390.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3955.10` | 965,830.00 USD | 0.00 USD | 965,830.00 USD | 181,840.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.20` | 754,530.00 USD | 0.00 USD | 754,530.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.30` | 464,400.00 USD | 0.00 USD | 464,400.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.40` | 308,770.00 USD | 0.00 USD | 308,770.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.50` | 258,690.00 USD | 0.00 USD | 258,690.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.60` | 164,090.00 USD | 0.00 USD | 164,090.00 USD | 97,640.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.70` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.80` | 19,950.00 USD | 0.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4024.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4025.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4094.50` | 29,250.00 USD | 29,250.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 0.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `1D` | `4102.70` | 512,670.00 USD | 512,670.00 USD | 0.00 USD | 255,730.00 USD | 0.00 USD | 48,490.00 USD |
| `7D` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD |
| `1D` | `4106.80` | 990,060.00 USD | 990,060.00 USD | 0.00 USD | 428,840.00 USD | 0.00 USD | 48,550.00 USD |
| `7D` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 106,200.00 USD |
| `1D` | `4110.90` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 278,400.00 USD | 0.00 USD | 37,810.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4115.00` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 229,730.00 USD | 0.00 USD | 34,530.00 USD |
| `7D` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4119.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 185,530.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4123.20` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 207,400.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.30` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD |
| `7D` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.40` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.50` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 127,000.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.60` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 71,850.00 USD | 0.00 USD | 5,440.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.70` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.80` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.50` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.60` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD |
| `1D` | `4184.70` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 131,510.00 USD | 0.00 USD | 25,770.00 USD |
| `7D` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 62,050.00 USD |
| `1D` | `4188.80` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 190,610.00 USD | 0.00 USD | 27,100.00 USD |
| `7D` | `4190.90` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.90` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 150,560.00 USD | 0.00 USD | 18,220.00 USD |
| `7D` | `4195.10` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4197.00` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 90,920.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4199.30` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4201.10` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 122,050.00 USD | 0.00 USD | 4,310.00 USD |
| `7D` | `4203.50` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4205.20` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 65,640.00 USD | 0.00 USD | 23,090.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4209.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,280.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4213.40` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `4216.10` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.50` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 47,950.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.60` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `4224.50` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.70` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.80` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4414.30` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 674.96 USD |
| `7D` | `4417.70` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4418.40` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.50` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4426.60` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4430.70` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 59,900.00 USD | 0.00 USD | 8,160.00 USD |
| `1D` | `4433.20` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 16,560.00 USD | 0.00 USD | 3,720.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.55M` | Total OI Tokens: `68,157.7 PAXG`
  * 1h OI Change: `-0.07%` | 4h OI Change: `+0.01%` | 24h OI Change: `+0.05%`
  * Exchange Breakdown: Binance=`107.29M` | Bybit=`20.08M` | OKX=`-` | Hyperliquid=`24.66M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.37K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `34.05%` | `65.95%` | `0.52` | 2,560,000.00 USD |
| `15M` | `Binance` | `52.01%` | `47.99%` | `1.08` | 324,030.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `54.75%` | `45.25%` | `1.21` | 121,090.00 USD |
| `15M` | `KuCoin` | `4.25%` | `95.75%` | `0.04` | 4,260.00 USD |
| `15M` | `Gate` | `34.07%` | `65.93%` | `0.52` | 180,100.00 USD |
| `15M` | `Bitget` | `53%` | `47%` | `1.13` | 110,800.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `27.81%` | `72.19%` | `0.39` | 1,580,000.00 USD |
| `15M` | `Bitunix` | `27.97%` | `72.03%` | `0.39` | 50,360.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.01%` | `53.99%` | `0.85` | 127,730.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 51,230.00 USD |
| `15M` | `HTX` | `46.74%` | `53.26%` | `0.88` | 1,790.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `86.94%` | `13.06%` | `6.66` | 1,730.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `52.01%` | `47.99%` | `1.08` | 324,030.00 USD |
| `15M` | `Global Accounts` | `34.05%` | `65.95%` | `0.52` | 2,560,000.00 USD |
| `1H` | `PAXG` | `41.04%` | `58.96%` | `0.70` | 6,500,000.00 USD |
| `1H` | `Binance` | `49.76%` | `50.24%` | `0.99` | 1,150,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `44.65%` | `55.35%` | `0.81` | 639,560.00 USD |
| `1H` | `KuCoin` | `43.55%` | `56.45%` | `0.77` | 32,260.00 USD |
| `1H` | `Gate` | `43.28%` | `56.72%` | `0.76` | 529,030.00 USD |
| `1H` | `Bitget` | `35.49%` | `64.51%` | `0.55` | 492,680.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `38.48%` | `61.52%` | `0.63` | 2,680,000.00 USD |
| `1H` | `Bitunix` | `43.72%` | `56.28%` | `0.78` | 156,960.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `39.78%` | `60.22%` | `0.66` | 585,800.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.79%` | `78.21%` | `0.28` | 217,800.00 USD |
| `1H` | `HTX` | `48.24%` | `51.76%` | `0.93` | 4,190.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `94.26%` | `5.74%` | `16.42` | 9,730.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `49.76%` | `50.24%` | `0.99` | 1,150,000.00 USD |
| `1H` | `Global Accounts` | `41.04%` | `58.96%` | `0.70` | 6,500,000.00 USD |
| `4H` | `PAXG` | `45.26%` | `54.74%` | `0.83` | 58,840,000.00 USD |
| `4H` | `Binance` | `53.48%` | `46.52%` | `1.15` | 6,640,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.2%` | `45.8%` | `1.18` | 5,700,000.00 USD |
| `4H` | `KuCoin` | `25.31%` | `74.69%` | `0.34` | 318,400.00 USD |
| `4H` | `Gate` | `49.4%` | `50.6%` | `0.98` | 2,830,000.00 USD |
| `4H` | `Bitget` | `54.28%` | `45.72%` | `1.19` | 2,060,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `40.06%` | `59.94%` | `0.67` | 32,030,000.00 USD |
| `4H` | `Bitunix` | `45.88%` | `54.12%` | `0.85` | 3,400,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.83%` | `41.17%` | `1.43` | 4,760,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `15.65%` | `84.35%` | `0.19` | 988,870.00 USD |
| `4H` | `HTX` | `41.44%` | `58.56%` | `0.71` | 12,910.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.97%` | `59.03%` | `0.69` | 97,170.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.48%` | `46.52%` | `1.15` | 6,640,000.00 USD |
| `4H` | `Global Accounts` | `45.26%` | `54.74%` | `0.83` | 58,840,000.00 USD |


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
| `5m` | -60,610.00 USD | -25,580.00 USD | **`DISTRIBUTION`** |
| `15m` | -19,020.00 USD | -126,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 305,820.00 USD | -17,320.00 USD | **`ACCUMULATION`** |
| `1h` | 265,130.00 USD | 47,840.00 USD | **`ACCUMULATION`** |
| `2h` | -966,550.00 USD | 207,210.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,070,000.00 USD | -155,460.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,700,000.00 USD | 291,310.00 USD | **`DISTRIBUTION`** |
| `8h` | -924,400.00 USD | 471,910.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,310,000.00 USD | 1,560,000.00 USD | **`ACCUMULATION`** |
| `24h` | -839,440.00 USD | 2,070,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,990,000.00 USD | -8,220,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,860,000.00 USD | -71,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-60.61K` | 15m=`-19.02K` | 1h=`+265.13K` | 24h=`-839.44K`
* Futures Capital Netflows: 5m=`-25.58K` | 15m=`-126.00K` | 1h=`+47.84K` | 24h=`+2.07M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4017.76` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.76` (Risk Distance: `8.00` pts)
  * +2.5R Take Profit: `4037.77`
  * Mathematical Lot Sizing: **`1.24 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4023.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4031.63` (Risk Distance: `8.00` pts)
  * +2.5R Take Profit: `4003.62`
  * Mathematical Lot Sizing: **`1.24 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4049.06`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
