# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 03:40:27 IST` (`2026-10-29 22:10:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4021.82` | **Live Ask Quote**: `4022.01` | **Mid Price**: `4021.91`
- **Spread Points**: `19.00` | **Spread BPS**: `0.47 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4021.91` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.05` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4050.07` | Lower -3.00σ Band: `3993.76`
  * Upper +2.51σ Band: `4044.04` | Lower -2.51σ Band: `3999.79`
  * Upper +2.01σ Band: `4038.81` | Lower -2.01σ Band: `4005.02`
  * Upper +2.00σ Band: `4038.00` | Lower -2.00σ Band: `4005.83`
  * Upper +1.28σ Band: `4033.18` | Lower -1.28σ Band: `4010.65`
  * Upper +1.00σ Band: `4029.96` | Lower -1.00σ Band: `4013.87`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4021.91` | EMA-20=`4021.91` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4021.91` (Slope: `+0.0000`) | EMA-100=`4021.91`
  * Institutional Anchors: EMA-144=`4021.91` | EMA-200=`4021.91` (Slope: `+0.0000`) | EMA-233=`4021.91`
- **Range Boundaries**: 24H High=`4062.13` | 24H Low=`3981.70` | Weekly High=`4102.35` | Weekly Low=`3941.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4026.47` (Distance: `-0.11%`)
  * Point of Control (POC) = `4020.79` (Distance: `+0.03%`)
  * Value Area Low (VAL) = `4020.79` (Distance: `+0.03%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4020.76`
  * London Session (08:00-16:00 UTC): High=`4038.00` | Low=`4005.83`
  * New York Session (13:00-21:00 UTC): High=`4046.05` | Low=`3997.78`
  * Initial Balance (First Hour): IB High=`4033.98` | IB Low=`4009.85`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4005.83` - `4038.00`
  * Optimal Trade Entry (OTE 0.705): `4029.96`
  * Structural Invalidation Anchor (0.786): `4054.09`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4019.19` | `4019.19` | `4018.12` | `4018.13` | `14` | 56,243.32 USD | -33,941.51 USD | `-60.35%` | 1,742,861.15 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4018.12` | `4025.28` | `4017.72` | `4023.22` | `183` | 736,299.98 USD | 112,498.88 USD | `+15.28%` | 1,855,360.02 USD | `+1.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4023.28` | `4023.28` | `4022.23` | `4022.55` | `2` | 7,321.09 USD | 1,777.64 USD | `+24.28%` | 1,857,137.66 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4019.11` | `4023.84` | `4019.11` | `4020.01` | `192` | 774,028.49 USD | 279,522.24 USD | `+36.11%` | 1,874,455.68 USD | `+0.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4020.01` | `4020.01` | `4018.12` | `4018.13` | `44` | 175,174.25 USD | -58,319.99 USD | `-33.29%` | 1,816,135.69 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4018.12` | `4025.28` | `4017.72` | `4022.55` | `185` | 743,621.07 USD | 114,276.52 USD | `+15.37%` | 1,930,412.20 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,839,422.95 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,963,502.96 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4025.28` | `4017.72` | `4023.43` | `198` | 795,786.18 USD | 166,441.63 USD | `+20.92%` | 2,129,944.58 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4022.55` | `1,837` | 7,391,036.71 USD | -785.38 USD | `-0.01%` | 1,246,361.94 USD | `-0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4022.55` | `1,837` | 7,391,036.71 USD | -785.38 USD | `-0.01%` | 1,246,361.94 USD | `-0.36` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID` | `4020.70` | `10.2985` | 41,407.18 USD | 974,088.62 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4020.80` | `13.4662` | 54,144.90 USD | 932,681.45 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `4020.90` | `2.6101` | 10,494.95 USD | 878,536.55 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4021.00` | `25.2512` | 101,535.08 USD | 868,041.60 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4021.10` | `10.6513` | 42,829.94 USD | 766,506.52 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4021.20` | `9.0534` | 36,405.53 USD | 723,676.58 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4021.30` | `7.3018` | 29,362.73 USD | 687,271.05 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4021.40` | `16.5636` | 66,608.86 USD | 657,908.32 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.50` | `5.5335` | 22,252.97 USD | 591,299.46 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4021.60` | `12.9150` | 51,938.96 USD | 569,046.49 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.70` | `4.2257` | 16,994.50 USD | 517,107.52 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.80` | `7.5906` | 30,527.88 USD | 500,113.03 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4021.90` | `2.6101` | 10,497.56 USD | 469,585.15 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4022.00` | `25.5734` | 102,856.21 USD | 459,087.59 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `4022.10` | `11.0496` | 44,442.60 USD | 356,231.38 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4022.20` | `19.4281` | 78,143.70 USD | 311,788.78 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4022.30` | `2.3005` | 9,253.30 USD | 233,645.08 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4022.40` | `14.1624` | 56,966.84 USD | 224,391.77 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4022.50` | `5.2203` | 20,998.66 USD | 167,424.94 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4022.70` | `36.4000` | 146,426.28 USD | 146,426.28 USD | `9 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4022.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,022.75` | `0.00%` | `-` |
| `ASK` | `4022.80` | `23.3504` | 93,933.99 USD | 93,933.99 USD | `14 orders` | `+0.00%` | `-` |
| `ASK` | `4022.90` | `3.9771` | 15,999.48 USD | 109,933.46 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `4023.10` | `3.7284` | 14,999.73 USD | 124,933.19 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4023.20` | `5.2203` | 21,002.31 USD | 145,935.50 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4023.30` | `9.4222` | 37,908.34 USD | 183,843.84 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4023.40` | `0.4729` | 1,902.67 USD | 185,746.50 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4023.50` | `3.7280` | 14,999.61 USD | 200,746.11 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4023.60` | `10.9952` | 44,240.29 USD | 244,986.40 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4023.90` | `10.2540` | 41,261.07 USD | 286,247.47 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4024.00` | `9.1222` | 36,707.73 USD | 322,955.20 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4024.10` | `0.3721` | 1,497.37 USD | 324,452.57 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4024.20` | `5.9379` | 23,895.30 USD | 348,347.87 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.40` | `17.8473` | 71,824.67 USD | 420,172.54 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `4024.60` | `3.2949` | 13,260.65 USD | 433,433.20 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4024.70` | `7.8377` | 31,544.39 USD | 464,977.59 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4024.80` | `3.2429` | 13,052.02 USD | 478,029.61 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4024.90` | `14.2339` | 57,290.02 USD | 535,319.64 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4025.00` | `2.9814` | 12,000.13 USD | 547,319.77 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `4025.10` | `5.2203` | 21,012.23 USD | 568,332.00 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `4025.20` | `12.5742` | 50,613.67 USD | 618,945.67 USD | `3 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,598,387.73 USD | `6,365.38` | `4188.90` | `4022.50` | `33053.66` | 1,065,583.56 USD | `+4.16%` | `4X Cross` |
| `52` | `0x4692...164f` | `SHORT` | 25,495,222.05 USD | `6,338.15` | `4132.76` | `4022.50` | `13716.86` | 698,844.91 USD | `+2.74%` | `5X Cross` |
| `67` | `0xb83d...6e36` | `SHORT` | 23,615,779.27 USD | `5,869.90` | `4228.86` | `4022.50` | `30214.74` | 1,207,242.67 USD | `+5.11%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,419,931.99 USD | `4,828.91` | `4157.43` | `4022.50` | `2262.52` | -655,950.33 USD | `-3.38%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,209,014.74 USD | `3,533.26` | `4129.11` | `4022.50` | `415.75` | -380,234.42 USD | `-2.68%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,143,119.38 USD | `3,268.21` | `4228.94` | `4022.50` | `4397.00` | 677,959.75 USD | `+5.16%` | `25X Cross` |
| `177` | `0xa742...e390` | `SHORT` | 11,667,280.40 USD | `2,900.00` | `4364.92` | `4022.50` | `4235.67` | 990,995.93 USD | `+8.49%` | `20X Cross` |
| `261` | `0xfc66...ca06` | `SHORT` | 8,992,137.65 USD | `2,235.07` | `4031.28` | `4022.50` | `12613.28` | 18,074.99 USD | `+0.20%` | `3X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,847,740.00 USD | `2,200.00` | `4176.09` | `4022.50` | `2641.03` | -339,679.30 USD | `-3.84%` | `25X Cross` |
| `266` | `0x41e5...0825` | `SHORT` | 8,841,800.00 USD | `2,200.00` | `4112.20` | `4022.50` | `4331.15` | 205,054.59 USD | `+2.32%` | `20X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,947,304.96 USD | `1,975.37` | `4048.55` | `4022.50` | `6496.26` | 50,086.75 USD | `+0.63%` | `6X Cross` |
| `370` | `0xc26c...b8f4` | `LONG` | 6,353,776.16 USD | `1,579.95` | `4075.62` | `4022.50` | `0.000000` | -85,520.81 USD | `-1.35%` | `1X Cross` |
| `403` | `0x12d2...f97f` | `LONG` | 5,640,296.27 USD | `1,401.94` | `4278.91` | `4022.50` | `3106.24` | -358,494.31 USD | `-6.36%` | `20X Cross` |
| `552` | `0x63da...8add` | `LONG` | 4,021,500.00 USD | `1,000.00` | `4021.46` | `4022.50` | `3564.11` | 39.04 USD | `+0.00%` | `25X Cross` |
| `563` | `0x354b...6425` | `LONG` | 3,973,167.26 USD | `987.74` | `4031.85` | `4022.50` | `0.000000` | -9,240.08 USD | `-0.23%` | `10X Cross` |
| `581` | `0x9aa5...58af` | `LONG` | 3,909,110.09 USD | `971.64` | `4279.98` | `4022.50` | `0.000000` | -249,498.99 USD | `-6.38%` | `20X Cross` |
| `608` | `0xf3dc...1672` | `LONG` | 3,743,078.86 USD | `930.74` | `4024.62` | `4022.50` | `3337.59` | -2,813.70 USD | `-0.08%` | `20X Cross` |
| `686` | `0x4a20...3c26` | `LONG` | 3,367,770.37 USD | `837.40` | `4599.73` | `4022.50` | `0.000000` | -484,050.01 USD | `-14.37%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,760,630.78 USD | `686.49` | `4290.34` | `4022.50` | `1415.13` | -184,627.92 USD | `-6.69%` | `25X Cross` |
| `879` | `0xd8c5...99b0` | `SHORT` | 2,583,744.11 USD | `642.35` | `4175.35` | `4022.50` | `32727.74` | 98,317.06 USD | `+3.81%` | `4X Cross` |
| `913` | `0x625e...a354` | `SHORT` | 2,494,260.00 USD | `620.00` | `4122.81` | `4022.50` | `4342.25` | 61,887.03 USD | `+2.48%` | `20X Cross` |
| `942` | `0xeae3...e8ad` | `SHORT` | 2,412,900.00 USD | `600.00` | `4104.77` | `4022.50` | `4325.27` | 49,965.11 USD | `+2.07%` | `20X Cross` |
| `947` | `0xf285...fa82` | `LONG` | 2,405,342.69 USD | `598.11` | `4146.45` | `4022.50` | `3891.24` | -74,676.86 USD | `-3.10%` | `25X Cross` |
| `963` | `0x12f7...8750` | `LONG` | 2,355,033.43 USD | `585.61` | `4082.77` | `4022.50` | `2549.82` | -35,883.55 USD | `-1.52%` | `10X Cross` |
| `1108` | `0x413c...886c` | `LONG` | 2,010,800.00 USD | `500.00` | `4010.43` | `4022.50` | `0.000000` | 5,583.77 USD | `+0.28%` | `2X Cross` |
| `1116` | `0x61ce...a62b` | `SHORT` | 2,000,809.83 USD | `497.50` | `4071.66` | `4022.50` | `4714.83` | 24,858.97 USD | `+1.24%` | `20X Cross` |
| `1119` | `0x0593...40f9` | `LONG` | 1,995,772.75 USD | `496.18` | `4024.57` | `4022.50` | `3701.73` | -1,131.08 USD | `-0.06%` | `10X Isolated` |
| `1197` | `0x2edd...8179` | `LONG` | 1,892,222.62 USD | `470.91` | `4164.68` | `4022.86` | `0.000000` | -68,978.70 USD | `-3.65%` | `10X Cross` |
| `1242` | `0xead5...69f2` | `LONG` | 1,825,799.52 USD | `453.78` | `4220.88` | `4022.50` | `3538.94` | -89,568.54 USD | `-4.91%` | `5X Isolated` |
| `1307` | `0x7a6d...f79c` | `SHORT` | 1,723,111.69 USD | `428.38` | `4136.09` | `4022.86` | `5836.47` | 48,703.32 USD | `+2.83%` | `10X Cross` |
| `1350` | `0x46fc...1195` | `LONG` | 1,651,517.49 USD | `410.66` | `4055.10` | `4022.50` | `2118.55` | -13,759.00 USD | `-0.83%` | `20X Cross` |
| `1388` | `0xee02...309d` | `SHORT` | 1,608,600.00 USD | `400.00` | `4438.84` | `4022.50` | `4226.89` | 166,938.60 USD | `+10.38%` | `25X Isolated` |
| `1389` | `0x6d15...d374` | `LONG` | 1,607,600.00 USD | `400.00` | `4068.25` | `4022.50` | `3841.81` | -19,700.00 USD | `-1.23%` | `25X Cross` |
| `1430` | `0x02a7...fe9f` | `SHORT` | 1,568,385.00 USD | `390.00` | `4055.02` | `4022.50` | `4306.71` | 13,074.25 USD | `+0.83%` | `25X Cross` |
| `1461` | `0x51f6...2b39` | `LONG` | 1,532,075.85 USD | `380.89` | `4234.43` | `4022.86` | `0.000000` | -80,760.00 USD | `-5.27%` | `10X Cross` |
| `1467` | `0x7e77...b8d2` | `SHORT` | 1,528,170.00 USD | `380.00` | `4131.92` | `4022.50` | `4293.51` | 41,959.64 USD | `+2.75%` | `20X Cross` |
| `1482` | `0x72c2...9b37` | `LONG` | 1,500,920.65 USD | `373.13` | `4000.98` | `4022.50` | `3778.05` | 8,027.14 USD | `+0.53%` | `13X Isolated` |
| `1531` | `0xaa44...b844` | `LONG` | 1,447,776.00 USD | `360.00` | `4043.10` | `4022.50` | `2803.27` | -7,741.63 USD | `-0.53%` | `4X Cross` |
| `1533` | `0x781e...96b7` | `SHORT` | 1,446,579.25 USD | `359.61` | `4364.97` | `4022.86` | `13609.02` | 123,121.67 USD | `+8.51%` | `10X Cross` |
| `1644` | `0xa41f...d50a` | `LONG` | 1,323,480.32 USD | `328.96` | `4468.89` | `4022.50` | `3833.19` | -146,617.53 USD | `-11.08%` | `15X Cross` |
| `1677` | `0xbf5a...88ba` | `SHORT` | 1,277,480.95 USD | `317.65` | `4091.80` | `4022.50` | `9909.64` | 22,302.09 USD | `+1.75%` | `20X Cross` |
| `1715` | `0xff31...ff6c` | `SHORT` | 1,246,913.00 USD | `310.00` | `4372.43` | `4022.50` | `4789.18` | 108,542.38 USD | `+8.70%` | `10X Isolated` |
| `1724` | `0xada6...6f88` | `LONG` | 1,239,333.46 USD | `308.10` | `4166.46` | `4022.50` | `1891.56` | -44,355.56 USD | `-3.58%` | `5X Cross` |
| `1746` | `0x5238...54e5` | `LONG` | 1,206,960.00 USD | `300.00` | `4023.33` | `4022.50` | `3833.96` | -39.31 USD | `-0.00%` | `15X Isolated` |
| `1888` | `0x50e2...d770` | `LONG` | 1,087,336.57 USD | `270.37` | `4243.58` | `4022.50` | `2562.10` | -59,989.89 USD | `-5.52%` | `20X Cross` |
| `1905` | `0x4c92...4f17` | `SHORT` | 1,072,616.49 USD | `266.72` | `4260.98` | `4022.50` | `6514.71` | 63,875.75 USD | `+5.96%` | `20X Cross` |
| `1966` | `0xd346...c4f3` | `LONG` | 1,026,181.44 USD | `255.17` | `4188.66` | `4022.50` | `3310.43` | -42,655.07 USD | `-4.16%` | `5X Isolated` |
| `2017` | `0x1581...463b` | `LONG` | 1,004,750.00 USD | `250.00` | `4003.77` | `4022.50` | `3549.87` | 3,806.41 USD | `+0.38%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.85` (Vol: 274,500.00 USD, Dist: `+2.26%`) | Long MP=`3937.39` (Vol: 356,200.00 USD, Dist: `--2.04%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.96%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.05%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.94%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.04%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.29%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,270,000.00 USD | 16,270,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,200,000.00 USD | 16,200,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 3,950,000.00 USD | 3,950,000.00 USD | 34,120.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,060,000.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 3,910,000.00 USD | 3,910,000.00 USD | 67,500.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 15,990,000.00 USD | 15,990,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 3,830,000.00 USD | 3,830,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,900,000.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 3,790,000.00 USD | 3,790,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,710,000.00 USD | 15,710,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.60` | 3,750,000.00 USD | 3,750,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,600,000.00 USD | 15,600,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.80` | 3,700,000.00 USD | 3,700,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,470,000.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3644.00` | 3,680,000.00 USD | 3,680,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,400,000.00 USD | 15,400,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3648.20` | 3,670,000.00 USD | 3,670,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,360,000.00 USD | 15,360,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3652.40` | 3,650,000.00 USD | 3,650,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,340,000.00 USD | 15,340,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3656.60` | 3,630,000.00 USD | 3,630,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,310,000.00 USD | 15,310,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.80` | 3,620,000.00 USD | 3,620,000.00 USD | 2,210.00 USD | 0.00 USD | 330.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,280,000.00 USD | 15,280,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,250,000.00 USD | 15,250,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,240,000.00 USD | 15,240,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,880,000.00 USD | 14,880,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,390,000.00 USD | 14,390,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,860,000.00 USD | 13,860,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.00` | 3,620,000.00 USD | 3,620,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,530,000.00 USD | 13,530,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.20` | 3,580,000.00 USD | 3,580,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,230,000.00 USD | 13,230,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.40` | 3,500,000.00 USD | 3,500,000.00 USD | 152,270.00 USD | 0.00 USD | 24,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,940,000.00 USD | 12,940,000.00 USD | 183,740.00 USD | 0.00 USD | 69,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.60` | 3,320,000.00 USD | 3,320,000.00 USD | 193,320.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,690,000.00 USD | 12,690,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.80` | 3,100,000.00 USD | 3,100,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,150,000.00 USD | 12,150,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.00` | 2,930,000.00 USD | 2,930,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,730,000.00 USD | 11,730,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.20` | 2,820,000.00 USD | 2,820,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,190,000.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.40` | 2,670,000.00 USD | 2,670,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,850,000.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.60` | 2,600,000.00 USD | 2,600,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,710,000.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.80` | 2,580,000.00 USD | 2,580,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,600,000.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3896.00` | 2,500,000.00 USD | 2,500,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,470,000.00 USD | 10,470,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3900.20` | 2,450,000.00 USD | 2,450,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,360,000.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3904.40` | 2,430,000.00 USD | 2,430,000.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,270,000.00 USD | 10,270,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3908.60` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 825.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,180,000.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,160,000.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,430,000.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,480,000.00 USD | 8,480,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,590,000.00 USD | 7,590,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.80` | 2,410,000.00 USD | 2,410,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,750,000.00 USD | 6,750,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.00` | 2,380,000.00 USD | 2,380,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,290,000.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.20` | 2,200,000.00 USD | 2,200,000.00 USD | 296,180.00 USD | 0.00 USD | 46,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,630,000.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,860,000.00 USD | 1,860,000.00 USD | 360,890.00 USD | 0.00 USD | 45,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.60` | 1,450,000.00 USD | 1,450,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.80` | 1,050,000.00 USD | 1,050,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.00` | 840,110.00 USD | 840,110.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 551,680.00 USD | 551,680.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 392,900.00 USD | 392,900.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.60` | 342,820.00 USD | 342,820.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.80` | 248,220.00 USD | 248,220.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3980.00` | 115,260.00 USD | 115,260.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3984.20` | 47,840.00 USD | 47,840.00 USD | 44,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3988.40` | 3,760.00 USD | 3,760.00 USD | 2,110.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.80` | 433,190.00 USD | 433,190.00 USD | 224,550.00 USD | 0.00 USD | 25,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.00` | 899,580.00 USD | 899,580.00 USD | 408,710.00 USD | 0.00 USD | 57,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 506,510.00 USD | 0.00 USD | 101,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.20` | 1,200,000.00 USD | 1,200,000.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,690,000.00 USD | 6,690,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.40` | 1,500,000.00 USD | 1,500,000.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,680,000.00 USD | 1,680,000.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.80` | 1,970,000.00 USD | 1,970,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.00` | 2,060,000.00 USD | 2,060,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.20` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,330,000.00 USD | 9,330,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.40` | 2,230,000.00 USD | 2,230,000.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,560,000.00 USD | 9,560,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 2,330,000.00 USD | 2,330,000.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,770,000.00 USD | 9,770,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 2,370,000.00 USD | 2,370,000.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,940,000.00 USD | 9,940,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.00` | 2,410,000.00 USD | 2,410,000.00 USD | 36,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,040,000.00 USD | 10,040,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4152.20` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,130,000.00 USD | 10,130,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,510,000.00 USD | 10,510,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,940,000.00 USD | 10,940,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.20` | 2,420,000.00 USD | 2,420,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,930,000.00 USD | 11,930,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.40` | 2,500,000.00 USD | 2,500,000.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.60` | 2,620,000.00 USD | 2,620,000.00 USD | 108,350.00 USD | 0.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.80` | 2,780,000.00 USD | 2,780,000.00 USD | 142,450.00 USD | 0.00 USD | 22,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 249,690.00 USD | 0.00 USD | 59,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.00` | 2,960,000.00 USD | 2,960,000.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,460,000.00 USD | 13,460,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.20` | 3,140,000.00 USD | 3,140,000.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,780,000.00 USD | 13,780,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.40` | 3,210,000.00 USD | 3,210,000.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,220,000.00 USD | 14,220,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.60` | 3,360,000.00 USD | 3,360,000.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,560,000.00 USD | 14,560,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.80` | 3,420,000.00 USD | 3,420,000.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,700,000.00 USD | 14,700,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4211.00` | 3,450,000.00 USD | 3,450,000.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,810,000.00 USD | 14,810,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4215.20` | 3,500,000.00 USD | 3,500,000.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,920,000.00 USD | 14,920,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.40` | 3,560,000.00 USD | 3,560,000.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.60` | 3,590,000.00 USD | 3,590,000.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,130,000.00 USD | 15,130,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.80` | 3,610,000.00 USD | 3,610,000.00 USD | 22,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4232.00` | 3,620,000.00 USD | 3,620,000.00 USD | 1,060.00 USD | 0.00 USD | 825.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,230,000.00 USD | 15,230,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,330,000.00 USD | 15,330,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,590,000.00 USD | 15,590,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,730,000.00 USD | 15,730,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,790,000.00 USD | 15,790,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.80` | 3,630,000.00 USD | 3,630,000.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,920,000.00 USD | 15,920,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.00` | 3,660,000.00 USD | 3,660,000.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,970,000.00 USD | 15,970,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4425.20` | 3,700,000.00 USD | 3,700,000.00 USD | 35,180.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4429.40` | 3,760,000.00 USD | 3,760,000.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.60` | 3,800,000.00 USD | 3,800,000.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4437.80` | 3,840,000.00 USD | 3,840,000.00 USD | 24,810.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.40` | 3,840,000.00 USD | 3,840,000.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,370,000.00 USD | 16,370,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
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
| `7D` | `3611.30` | 16,270,000.00 USD | 0.00 USD | 16,270,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.80` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 34,120.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3619.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3623.00` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 67,500.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `3623.90` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.20` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `3628.10` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.40` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3632.30` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.60` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `3636.50` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.80` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD |
| `7D` | `3640.70` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3644.00` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `3644.90` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3648.20` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `3649.10` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3652.40` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `3653.30` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3656.60` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `3660.80` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3661.70` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3854.00` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `3854.90` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3858.20` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD |
| `7D` | `3859.10` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3862.40` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 152,270.00 USD | 0.00 USD | 25,610.00 USD |
| `7D` | `3863.30` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 183,740.00 USD | 0.00 USD | 69,400.00 USD |
| `1D` | `3866.60` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 196,590.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `3867.50` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3870.80` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD |
| `7D` | `3871.70` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3875.00` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD |
| `7D` | `3875.90` | 11,730,000.00 USD | 0.00 USD | 11,730,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3879.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD |
| `7D` | `3880.10` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3883.40` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD |
| `7D` | `3884.30` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3887.60` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD |
| `7D` | `3888.50` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3891.80` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3892.70` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3896.00` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `3896.90` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3900.20` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3901.10` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3904.40` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3905.30` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3933.80` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.00` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `3938.90` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.20` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 296,180.00 USD | 0.00 USD | 48,490.00 USD |
| `7D` | `3943.10` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD |
| `1D` | `3946.40` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 367,420.00 USD | 0.00 USD | 45,790.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD |
| `1D` | `3950.60` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.80` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.00` | 838,460.00 USD | 0.00 USD | 838,460.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.20` | 550,030.00 USD | 0.00 USD | 550,030.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.40` | 391,250.00 USD | 0.00 USD | 391,250.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.60` | 341,160.00 USD | 0.00 USD | 341,160.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.80` | 246,570.00 USD | 0.00 USD | 246,570.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3980.00` | 113,600.00 USD | 0.00 USD | 113,600.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3984.20` | 46,190.00 USD | 0.00 USD | 46,190.00 USD | 44,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `1D` | `3988.40` | 2,110.00 USD | 0.00 USD | 2,110.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4023.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 0.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4101.80` | 435,100.00 USD | 435,100.00 USD | 0.00 USD | 224,550.00 USD | 0.00 USD | 27,220.00 USD |
| `7D` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD |
| `1D` | `4106.00` | 908,010.00 USD | 908,010.00 USD | 0.00 USD | 415,230.00 USD | 0.00 USD | 57,680.00 USD |
| `7D` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 101,580.00 USD |
| `1D` | `4110.20` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `4111.10` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.40` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD |
| `7D` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD |
| `7D` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.00` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.20` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4132.10` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.40` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.60` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4140.50` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.80` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4148.00` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 36,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `1D` | `4173.20` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `4174.10` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4177.40` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4181.60` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 108,350.00 USD | 0.00 USD | 12,810.00 USD |
| `7D` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD |
| `1D` | `4185.80` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 145,720.00 USD | 0.00 USD | 22,750.00 USD |
| `7D` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 59,740.00 USD |
| `1D` | `4190.00` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD |
| `7D` | `4190.90` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4194.20` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4195.10` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4198.40` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD |
| `7D` | `4199.30` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4202.60` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD |
| `7D` | `4203.50` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4206.80` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD |
| `7D` | `4207.70` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4211.00` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD |
| `7D` | `4211.90` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4215.20` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD |
| `7D` | `4216.10` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4219.40` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD |
| `7D` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4223.60` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4224.50` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4227.80` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 22,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4232.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4416.80` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `4417.70` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4421.00` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4421.90` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4425.20` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 35,180.00 USD | 0.00 USD | 7,060.00 USD |
| `7D` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4429.40` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.60` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `4436.20` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 18,160.00 USD | 0.00 USD | 3,210.00 USD |
| `7D` | `4438.70` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
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
  * Total Open Interest: `274.92M` | Total OI Tokens: `68,322.9 PAXG`
  * 1h OI Change: `+0.07%` | 4h OI Change: `+0.35%` | 24h OI Change: `+0.22%`
  * Exchange Breakdown: Binance=`107.31M` | Bybit=`20.03M` | OKX=`-` | Hyperliquid=`24.64M`
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
| `15M` | `PAXG` | `46.21%` | `53.79%` | `0.86` | 3,810,000.00 USD |
| `15M` | `Binance` | `50.7%` | `49.3%` | `1.03` | 570,960.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `41.8%` | `58.2%` | `0.72` | 507,000.00 USD |
| `15M` | `KuCoin` | `12.96%` | `87.04%` | `0.15` | 49,570.00 USD |
| `15M` | `Gate` | `31.84%` | `68.16%` | `0.47` | 208,220.00 USD |
| `15M` | `Bitget` | `56.42%` | `43.58%` | `1.29` | 312,610.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `43.57%` | `56.43%` | `0.77` | 1,240,000.00 USD |
| `15M` | `Bitunix` | `38.07%` | `61.93%` | `0.61` | 444,880.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `67.86%` | `32.14%` | `2.11` | 439,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.57%` | `99.43%` | `0.01` | 33,840.00 USD |
| `15M` | `HTX` | `30.11%` | `69.89%` | `0.43` | 626.43 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `73.24%` | `26.76%` | `2.74` | 1,820.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `50.7%` | `49.3%` | `1.03` | 570,960.00 USD |
| `15M` | `Global Accounts` | `46.21%` | `53.79%` | `0.86` | 3,810,000.00 USD |
| `1H` | `PAXG` | `53.09%` | `46.91%` | `1.13` | 9,490,000.00 USD |
| `1H` | `Binance` | `59.62%` | `40.38%` | `1.48` | 1,860,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `54.8%` | `45.2%` | `1.21` | 1,510,000.00 USD |
| `1H` | `KuCoin` | `27.72%` | `72.28%` | `0.38` | 88,520.00 USD |
| `1H` | `Gate` | `38.71%` | `61.29%` | `0.63` | 434,110.00 USD |
| `1H` | `Bitget` | `61.51%` | `38.49%` | `1.60` | 472,980.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `51.58%` | `48.42%` | `1.07` | 2,390,000.00 USD |
| `1H` | `Bitunix` | `43.39%` | `56.61%` | `0.77` | 1,610,000.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `68.98%` | `31.02%` | `2.22` | 968,660.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.75%` | `94.25%` | `0.06` | 133,090.00 USD |
| `1H` | `HTX` | `51.26%` | `48.74%` | `1.05` | 2,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.86%` | `50.14%` | `0.99` | 11,920.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `59.62%` | `40.38%` | `1.48` | 1,860,000.00 USD |
| `1H` | `Global Accounts` | `53.09%` | `46.91%` | `1.13` | 9,490,000.00 USD |
| `4H` | `PAXG` | `46.50%` | `53.50%` | `0.87` | 61,950,000.00 USD |
| `4H` | `Binance` | `54.9%` | `45.1%` | `1.22` | 6,300,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `53.45%` | `46.55%` | `1.15` | 6,030,000.00 USD |
| `4H` | `KuCoin` | `23.63%` | `76.37%` | `0.31` | 304,550.00 USD |
| `4H` | `Gate` | `51.73%` | `48.27%` | `1.07` | 2,680,000.00 USD |
| `4H` | `Bitget` | `58.95%` | `41.05%` | `1.44` | 1,980,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `41.76%` | `58.24%` | `0.72` | 34,930,000.00 USD |
| `4H` | `Bitunix` | `48.77%` | `51.23%` | `0.95` | 3,630,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `59.46%` | `40.54%` | `1.47` | 4,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `14.96%` | `85.04%` | `0.18` | 1,020,000.00 USD |
| `4H` | `HTX` | `33.37%` | `66.63%` | `0.50` | 10,960.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.48%` | `64.52%` | `0.55` | 102,350.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.9%` | `45.1%` | `1.22` | 6,300,000.00 USD |
| `4H` | `Global Accounts` | `46.50%` | `53.50%` | `0.87` | 61,950,000.00 USD |


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
| `5m` | -111,570.00 USD | 279,940.00 USD | **`ACCUMULATION`** |
| `15m` | -155,140.00 USD | 196,260.00 USD | **`ACCUMULATION`** |
| `30m` | -578,210.00 USD | 406,110.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,190,000.00 USD | 344,050.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,300,000.00 USD | 157,310.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,720,000.00 USD | 563,220.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,330,000.00 USD | 938,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,140,000.00 USD | 1,030,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,570,000.00 USD | 1,410,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,130,000.00 USD | 1,980,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,370,000.00 USD | -7,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,070,000.00 USD | -71,020,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-111.57K` | 15m=`-155.14K` | 1h=`-1.19M` | 24h=`-1.13M`
* Futures Capital Netflows: 5m=`+279.94K` | 15m=`+196.26K` | 1h=`+344.05K` | 24h=`+1.98M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4020.79` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4008.44` (Risk Distance: `12.35` pts)
  * +2.5R Take Profit: `4051.67`
  * Mathematical Lot Sizing: **`0.80 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4026.47` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4038.82` (Risk Distance: `12.35` pts)
  * +2.5R Take Profit: `3995.59`
  * Mathematical Lot Sizing: **`0.80 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4054.09`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
