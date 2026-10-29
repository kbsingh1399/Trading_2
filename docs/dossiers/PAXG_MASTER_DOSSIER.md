# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 22:39:55 IST` (`2026-10-29 17:09:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4017.04` | **Live Ask Quote**: `4017.13` | **Mid Price**: `4017.09`
- **Spread Points**: `9.00` | **Spread BPS**: `0.22 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4017.09` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.04` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4045.20` | Lower -3.00σ Band: `3988.97`
  * Upper +2.51σ Band: `4039.18` | Lower -2.51σ Band: `3994.99`
  * Upper +2.01σ Band: `4033.96` | Lower -2.01σ Band: `4000.21`
  * Upper +2.00σ Band: `4033.15` | Lower -2.00σ Band: `4001.02`
  * Upper +1.28σ Band: `4028.33` | Lower -1.28σ Band: `4005.84`
  * Upper +1.00σ Band: `4025.12` | Lower -1.00σ Band: `4009.05`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4017.09` | EMA-20=`4017.09` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4017.09` (Slope: `+0.0000`) | EMA-100=`4017.09`
  * Institutional Anchors: EMA-144=`4017.09` | EMA-200=`4017.09` (Slope: `+0.0000`) | EMA-233=`4017.09`
- **Range Boundaries**: 24H High=`4057.26` | 24H Low=`3976.91` | Weekly High=`4097.43` | Weekly Low=`3936.74`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.71` (Distance: `-0.58%`)
  * Point of Control (POC) = `4027.30` (Distance: `-0.25%`)
  * Value Area Low (VAL) = `4019.82` (Distance: `-0.06%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4052.42` | Weekly POC=`4016.16` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4001.02` - `4033.15`
  * Optimal Trade Entry (OTE 0.705): `4025.12`
  * Structural Invalidation Anchor (0.786): `4049.22`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4022.00` | `4022.55` | `4019.39` | `4020.48` | `136` | 548,360.60 USD | 338,803.03 USD | `+61.78%` | 907,861.52 USD | `+2.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4020.48` | `4023.30` | `4020.48` | `4023.30` | `23` | 94,039.10 USD | 82,457.94 USD | `+87.68%` | 990,319.45 USD | `+0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4023.30` | `4024.01` | `4022.15` | `4022.60` | `22` | 87,321.94 USD | -12,036.84 USD | `-13.78%` | 978,282.61 USD | `-0.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4019.60` | `4021.70` | `4017.67` | `4021.36` | `133` | 536,295.57 USD | -74,630.45 USD | `-13.92%` | 494,219.57 USD | `-0.70` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4021.36` | `4023.30` | `4019.39` | `4023.30` | `201` | 809,848.30 USD | 483,447.28 USD | `+59.70%` | 977,666.85 USD | `+2.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4023.30` | `4024.01` | `4022.15` | `4022.15` | `22` | 87,925.33 USD | -12,640.23 USD | `-14.38%` | 965,026.63 USD | `-0.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4029.13` | `4030.46` | `4023.08` | `4026.82` | `526` | 2,116,236.19 USD | -146,951.88 USD | `-6.94%` | -157,920.93 USD | `-0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 692,493.29 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4024.01` | `4022.15` | `4022.60` | `22` | 87,321.94 USD | -12,036.84 USD | `-13.78%` | 680,456.44 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4026.82` | `4016.00` | `4022.60` | `973` | 3,911,047.30 USD | 838,377.37 USD | `+21.44%` | 1,215,427.65 USD | `+1.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4026.82` | `4016.00` | `4022.60` | `973` | 3,911,047.30 USD | 838,377.37 USD | `+21.44%` | 1,215,427.65 USD | `+1.23` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4016.80` | `18.1716` | 72,991.68 USD | 1,442,953.18 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `4016.90` | `75.5847` | 303,616.18 USD | 1,369,961.49 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4017.00` | `5.5704` | 22,376.30 USD | 1,066,345.31 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4017.10` | `10.0549` | 40,391.54 USD | 1,043,969.02 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `4017.20` | `53.1602` | 213,555.16 USD | 1,003,577.48 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `4017.30` | `7.2065` | 28,950.67 USD | 790,022.32 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4017.40` | `14.7284` | 59,169.87 USD | 761,071.65 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4017.50` | `1.0120` | 4,065.71 USD | 701,901.77 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4017.60` | `49.8987` | 200,473.02 USD | 697,836.06 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4017.70` | `3.7322` | 14,994.86 USD | 497,363.05 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4017.80` | `5.9983` | 24,099.97 USD | 482,368.19 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4017.90` | `13.0825` | 52,564.18 USD | 458,268.22 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4018.20` | `22.3056` | 89,628.36 USD | 405,704.04 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `4018.30` | `26.3688` | 105,957.75 USD | 316,075.68 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4018.40` | `24.9573` | 100,288.41 USD | 210,117.93 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4018.50` | `7.8175` | 31,414.62 USD | 109,829.52 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4018.60` | `7.8376` | 31,496.18 USD | 78,414.89 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4018.70` | `8.9514` | 35,972.99 USD | 46,918.71 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4018.90` | `0.2488` | 999.90 USD | 10,945.72 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4019.00` | `2.4747` | 9,945.82 USD | 9,945.82 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4019.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,019.05` | `0.00%` | `-` |
| `ASK` | `4019.10` | `10.0651` | 40,452.64 USD | 40,452.64 USD | `9 orders` | `+0.00%` | `-` |
| `ASK` | `4019.20` | `14.0951` | 56,651.03 USD | 97,103.67 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4019.30` | `3.7319` | 14,999.63 USD | 112,103.30 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4019.40` | `10.4189` | 41,877.73 USD | 153,981.02 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4019.50` | `66.3171` | 266,561.58 USD | 420,542.61 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4019.60` | `33.2924` | 133,822.13 USD | 554,364.74 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4019.70` | `10.8835` | 43,748.40 USD | 598,113.14 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4019.80` | `25.6398` | 103,066.87 USD | 701,180.01 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4019.90` | `15.6026` | 62,720.89 USD | 763,900.90 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4020.00` | `18.1882` | 73,116.56 USD | 837,017.46 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `4020.10` | `6.6583` | 26,767.03 USD | 863,784.50 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4020.20` | `19.9811` | 80,328.02 USD | 944,112.51 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4020.30` | `21.4091` | 86,071.00 USD | 1,030,183.52 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `4020.40` | `54.1799` | 217,824.87 USD | 1,248,008.39 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4020.50` | `21.4555` | 86,261.84 USD | 1,334,270.23 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4020.60` | `5.2575` | 21,138.30 USD | 1,355,408.53 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4020.70` | `7.5400` | 30,316.08 USD | 1,385,724.61 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4020.80` | `10.9526` | 44,038.21 USD | 1,429,762.82 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4020.90` | `14.5171` | 58,371.81 USD | 1,488,134.63 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4021.00` | `82.3809` | 331,253.60 USD | 1,819,388.23 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:34:53 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `56` | `0x5b5d...c060` | `SHORT` | 25,684,529.13 USD | `6,388.07` | `4191.43` | `4020.60` | `28257.20` | 1,090,692.05 USD | `+4.25%` | `4X Cross` |
| `59` | `0x4692...164f` | `SHORT` | 25,251,025.25 USD | `6,280.57` | `4135.07` | `4020.60` | `13216.99` | 719,617.22 USD | `+2.85%` | `5X Cross` |
| `79` | `0xb83d...6e36` | `SHORT` | 22,985,437.32 USD | `5,717.06` | `4234.49` | `4020.60` | `26625.92` | 1,223,437.91 USD | `+5.32%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,414,620.19 USD | `4,828.91` | `4157.43` | `4020.60` | `2046.39` | -661,262.12 USD | `-3.41%` | `25X Cross` |
| `151` | `0x645b...87b8` | `LONG` | 14,140,428.58 USD | `3,517.08` | `4129.71` | `4020.60` | `6.91` | -384,125.16 USD | `-2.72%` | `3X Cross` |
| `162` | `0x7a6d...f79c` | `SHORT` | 13,140,504.81 USD | `3,268.21` | `4228.94` | `4020.60` | `4404.01` | 680,574.32 USD | `+5.18%` | `25X Cross` |
| `186` | `0xa742...e390` | `SHORT` | 11,660,030.40 USD | `2,900.00` | `4364.92` | `4020.60` | `4235.56` | 998,245.93 USD | `+8.56%` | `20X Cross` |
| `281` | `0x3678...b209` | `LONG` | 8,845,540.00 USD | `2,200.00` | `4176.09` | `4020.60` | `2363.04` | -341,879.30 USD | `-3.86%` | `25X Cross` |
| `282` | `0x41e5...0825` | `SHORT` | 8,845,100.00 USD | `2,200.00` | `4112.20` | `4020.60` | `4331.05` | 201,754.59 USD | `+2.28%` | `20X Cross` |
| `317` | `0xfc66...ca06` | `SHORT` | 8,006,492.85 USD | `1,991.42` | `4032.86` | `4020.60` | `24626.16` | 24,632.54 USD | `+0.31%` | `3X Cross` |
| `320` | `0xacb6...efbd` | `SHORT` | 7,942,169.00 USD | `1,975.37` | `4048.55` | `4020.60` | `6467.66` | 55,222.71 USD | `+0.70%` | `6X Cross` |
| `389` | `0xc26c...b8f4` | `LONG` | 6,352,512.20 USD | `1,579.95` | `4075.62` | `4020.60` | `0.000000` | -86,784.77 USD | `-1.37%` | `1X Cross` |
| `436` | `0x12d2...f97f` | `LONG` | 5,636,651.22 USD | `1,401.94` | `4278.91` | `4020.60` | `2386.90` | -362,139.36 USD | `-6.42%` | `20X Cross` |
| `592` | `0x63da...8add` | `LONG` | 4,020,700.00 USD | `1,000.00` | `4021.46` | `4020.60` | `3564.00` | -760.96 USD | `-0.02%` | `25X Cross` |
| `614` | `0x9aa5...58af` | `LONG` | 3,906,486.66 USD | `971.64` | `4279.98` | `4020.60` | `0.000000` | -252,122.42 USD | `-6.45%` | `20X Cross` |
| `638` | `0xf3dc...1672` | `LONG` | 3,741,496.60 USD | `930.74` | `4024.62` | `4020.60` | `3337.48` | -4,395.96 USD | `-0.12%` | `20X Cross` |
| `692` | `0x354b...6425` | `LONG` | 3,419,764.53 USD | `850.58` | `4037.06` | `4020.60` | `0.000000` | -14,091.10 USD | `-0.41%` | `10X Cross` |
| `702` | `0x4a20...3c26` | `LONG` | 3,366,932.97 USD | `837.40` | `4599.73` | `4020.60` | `0.000000` | -484,887.41 USD | `-14.40%` | `20X Cross` |
| `857` | `0x0fac...7a0a` | `LONG` | 2,760,150.24 USD | `686.49` | `4290.34` | `4020.60` | `1133.10` | -185,108.46 USD | `-6.71%` | `25X Cross` |
| `884` | `0xd8c5...99b0` | `SHORT` | 2,649,435.84 USD | `658.95` | `4175.35` | `4020.60` | `31039.31` | 101,911.21 USD | `+3.85%` | `4X Cross` |
| `939` | `0x625e...a354` | `SHORT` | 2,492,710.00 USD | `620.00` | `4122.81` | `4020.60` | `4342.14` | 63,437.03 USD | `+2.54%` | `20X Cross` |
| `962` | `0xeae3...e8ad` | `SHORT` | 2,412,180.00 USD | `600.00` | `4104.77` | `4020.60` | `4325.17` | 50,685.11 USD | `+2.10%` | `20X Cross` |
| `966` | `0xf285...fa82` | `LONG` | 2,404,804.39 USD | `598.11` | `4146.45` | `4020.60` | `3891.13` | -75,215.16 USD | `-3.13%` | `25X Cross` |
| `986` | `0x12f7...8750` | `LONG` | 2,354,564.94 USD | `585.61` | `4082.77` | `4020.60` | `2091.81` | -36,352.04 USD | `-1.54%` | `10X Cross` |
| `1143` | `0x413c...886c` | `LONG` | 2,009,200.00 USD | `500.00` | `4010.43` | `4020.60` | `0.000000` | 3,983.77 USD | `+0.20%` | `2X Cross` |
| `1149` | `0x61ce...a62b` | `SHORT` | 2,000,113.32 USD | `497.50` | `4071.66` | `4020.60` | `4683.13` | 25,555.47 USD | `+1.28%` | `20X Cross` |
| `1153` | `0x0593...40f9` | `LONG` | 1,994,780.39 USD | `496.18` | `4024.57` | `4020.60` | `3701.62` | -2,123.44 USD | `-0.11%` | `10X Isolated` |
| `1278` | `0xead5...69f2` | `LONG` | 1,824,483.55 USD | `453.78` | `4220.88` | `4020.60` | `3538.83` | -90,884.51 USD | `-4.98%` | `5X Isolated` |
| `1306` | `0x2edd...8179` | `LONG` | 1,781,581.64 USD | `442.60` | `4174.40` | `4025.40` | `0.000000` | -65,989.52 USD | `-3.70%` | `10X Cross` |
| `1341` | `0x7a6d...f79c` | `SHORT` | 1,723,925.61 USD | `428.38` | `4136.09` | `4025.40` | `5777.03` | 47,889.40 USD | `+2.78%` | `10X Cross` |
| `1403` | `0x46fc...1195` | `LONG` | 1,636,529.84 USD | `407.03` | `4055.53` | `4020.60` | `1868.06` | -14,180.35 USD | `-0.87%` | `20X Cross` |
| `1442` | `0xee02...309d` | `SHORT` | 1,608,280.00 USD | `400.00` | `4438.84` | `4020.60` | `4226.78` | 167,258.60 USD | `+10.40%` | `25X Isolated` |
| `1443` | `0x6d15...d374` | `LONG` | 1,608,200.00 USD | `400.00` | `4068.25` | `4020.60` | `3841.70` | -19,100.00 USD | `-1.19%` | `25X Cross` |
| `1476` | `0x02a7...fe9f` | `SHORT` | 1,568,073.00 USD | `390.00` | `4055.02` | `4020.60` | `4306.60` | 13,386.25 USD | `+0.85%` | `25X Cross` |
| `1505` | `0x7e77...b8d2` | `SHORT` | 1,527,866.00 USD | `380.00` | `4131.92` | `4020.60` | `4293.41` | 42,263.64 USD | `+2.77%` | `20X Cross` |
| `1508` | `0x51f6...2b39` | `LONG` | 1,524,047.79 USD | `378.61` | `4235.75` | `4025.40` | `0.000000` | -79,631.44 USD | `-5.22%` | `10X Cross` |
| `1520` | `0x72c2...9b37` | `LONG` | 1,500,249.02 USD | `373.13` | `4000.98` | `4020.60` | `3777.93` | 7,355.50 USD | `+0.49%` | `13X Isolated` |
| `1571` | `0xaa44...b844` | `LONG` | 1,446,840.00 USD | `360.00` | `4043.10` | `4020.60` | `2794.19` | -8,677.63 USD | `-0.60%` | `9X Cross` |
| `1578` | `0x781e...96b7` | `SHORT` | 1,443,418.60 USD | `358.57` | `4365.97` | `4025.40` | `12102.19` | 122,090.48 USD | `+8.46%` | `10X Cross` |
| `1683` | `0xa41f...d50a` | `LONG` | 1,322,592.12 USD | `328.96` | `4468.89` | `4020.60` | `3833.08` | -147,505.73 USD | `-11.15%` | `15X Cross` |
| `1710` | `0x49e9...e1d0` | `SHORT` | 1,300,926.84 USD | `323.56` | `4025.23` | `4020.60` | `29628.70` | 1,465.86 USD | `+0.11%` | `4X Cross` |
| `1730` | `0xada6...6f88` | `LONG` | 1,283,583.69 USD | `319.28` | `4166.46` | `4020.60` | `1835.45` | -46,666.82 USD | `-3.64%` | `5X Cross` |
| `1737` | `0xbf5a...88ba` | `SHORT` | 1,277,131.53 USD | `317.65` | `4091.80` | `4020.60` | `10554.01` | 22,651.51 USD | `+1.77%` | `20X Cross` |
| `1752` | `0xff31...ff6c` | `SHORT` | 1,246,417.00 USD | `310.00` | `4372.43` | `4020.60` | `4789.07` | 109,038.38 USD | `+8.75%` | `10X Isolated` |
| `1937` | `0x50e2...d770` | `LONG` | 1,087,066.21 USD | `270.37` | `4243.58` | `4020.60` | `2561.99` | -60,260.26 USD | `-5.54%` | `20X Cross` |
| `1961` | `0x4c92...4f17` | `SHORT` | 1,072,403.11 USD | `266.72` | `4260.98` | `4020.60` | `6534.57` | 64,089.12 USD | `+5.98%` | `20X Cross` |
| `2017` | `0xd346...c4f3` | `LONG` | 1,025,977.30 USD | `255.17` | `4188.66` | `4020.60` | `3310.31` | -42,859.21 USD | `-4.18%` | `5X Isolated` |
| `2059` | `0x1581...463b` | `LONG` | 1,005,125.00 USD | `250.00` | `4003.77` | `4020.60` | `3504.53` | 4,181.41 USD | `+0.42%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.95` (Vol: 250,500.00 USD, Dist: `+1.97%`) | Long MP=`3950.54` (Vol: 316,800.00 USD, Dist: `--1.99%`)
  * 48H Horizon: Short MP=`4142.42` (Vol: 307,400.00 USD, Dist: `+2.77%`) | Long MP=`3950.54` (Vol: 316,800.00 USD, Dist: `--1.99%`)
  * 3D Horizon: Short MP=`4115.27` (Vol: 399,400.00 USD, Dist: `+2.10%`) | Long MP=`3952.40` (Vol: 407,100.00 USD, Dist: `--1.94%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.15%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.90%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3618.80` | 16,000,000.00 USD | 16,000,000.00 USD | 45,950.00 USD | 0.00 USD | 3,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.30` | 3,980,000.00 USD | 3,980,000.00 USD | 25,480.00 USD | 0.00 USD | 1,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.00` | 15,950,000.00 USD | 15,950,000.00 USD | 79,630.00 USD | 0.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.50` | 3,950,000.00 USD | 3,950,000.00 USD | 24,820.00 USD | 0.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.20` | 15,850,000.00 USD | 15,850,000.00 USD | 206,750.00 USD | 0.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.70` | 3,920,000.00 USD | 3,920,000.00 USD | 36,780.00 USD | 0.00 USD | 5,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3631.40` | 15,630,000.00 USD | 15,630,000.00 USD | 87,600.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.90` | 3,880,000.00 USD | 3,880,000.00 USD | 44,210.00 USD | 0.00 USD | 4,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3635.60` | 15,530,000.00 USD | 15,530,000.00 USD | 135,440.00 USD | 0.00 USD | 32,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.10` | 3,830,000.00 USD | 3,830,000.00 USD | 61,190.00 USD | 0.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.80` | 15,360,000.00 USD | 15,360,000.00 USD | 47,920.00 USD | 0.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.30` | 3,760,000.00 USD | 3,760,000.00 USD | 24,860.00 USD | 0.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.00` | 15,300,000.00 USD | 15,300,000.00 USD | 25,630.00 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.50` | 3,720,000.00 USD | 3,720,000.00 USD | 18,580.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3648.20` | 15,270,000.00 USD | 15,270,000.00 USD | 24,860.00 USD | 0.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.70` | 3,700,000.00 USD | 3,700,000.00 USD | 26,300.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.40` | 15,240,000.00 USD | 15,240,000.00 USD | 18,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.90` | 3,670,000.00 USD | 3,670,000.00 USD | 13,340.00 USD | 0.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.60` | 15,220,000.00 USD | 15,220,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.10` | 3,650,000.00 USD | 3,650,000.00 USD | 10,130.00 USD | 0.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.80` | 15,170,000.00 USD | 15,170,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3664.30` | 3,640,000.00 USD | 3,640,000.00 USD | 6,340.00 USD | 0.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.00` | 15,160,000.00 USD | 15,160,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 15,150,000.00 USD | 15,150,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3672.70` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.00` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3837.20` | 15,140,000.00 USD | 15,140,000.00 USD | 212,590.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.40` | 14,910,000.00 USD | 14,910,000.00 USD | 511,020.00 USD | 0.00 USD | 37,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.60` | 14,360,000.00 USD | 14,360,000.00 USD | 378,790.00 USD | 0.00 USD | 74,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,910,000.00 USD | 13,910,000.00 USD | 406,600.00 USD | 0.00 USD | 73,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.00` | 13,430,000.00 USD | 13,430,000.00 USD | 166,740.00 USD | 0.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.20` | 13,240,000.00 USD | 13,240,000.00 USD | 219,930.00 USD | 0.00 USD | 16,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.70` | 3,630,000.00 USD | 3,630,000.00 USD | 7,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.40` | 13,000,000.00 USD | 13,000,000.00 USD | 181,990.00 USD | 0.00 USD | 30,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.90` | 3,630,000.00 USD | 3,630,000.00 USD | 87,120.00 USD | 0.00 USD | 10,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3866.60` | 12,790,000.00 USD | 12,790,000.00 USD | 370,400.00 USD | 0.00 USD | 54,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.10` | 3,530,000.00 USD | 3,530,000.00 USD | 158,170.00 USD | 0.00 USD | 20,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3870.80` | 12,370,000.00 USD | 12,370,000.00 USD | 558,420.00 USD | 0.00 USD | 47,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3874.30` | 3,350,000.00 USD | 3,350,000.00 USD | 83,140.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.00` | 11,760,000.00 USD | 11,760,000.00 USD | 384,590.00 USD | 0.00 USD | 39,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3878.50` | 3,250,000.00 USD | 3,250,000.00 USD | 220,680.00 USD | 0.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.20` | 11,340,000.00 USD | 11,340,000.00 USD | 376,000.00 USD | 0.00 USD | 87,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3882.70` | 3,020,000.00 USD | 3,020,000.00 USD | 134,600.00 USD | 0.00 USD | 35,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3883.40` | 10,870,000.00 USD | 10,870,000.00 USD | 178,610.00 USD | 0.00 USD | 43,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3886.90` | 2,850,000.00 USD | 2,850,000.00 USD | 86,350.00 USD | 0.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3887.60` | 10,650,000.00 USD | 10,650,000.00 USD | 72,000.00 USD | 0.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.10` | 2,750,000.00 USD | 2,750,000.00 USD | 73,750.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3891.80` | 10,550,000.00 USD | 10,550,000.00 USD | 120,010.00 USD | 0.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3895.30` | 2,660,000.00 USD | 2,660,000.00 USD | 80,250.00 USD | 0.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.00` | 10,420,000.00 USD | 10,420,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3899.50` | 2,570,000.00 USD | 2,570,000.00 USD | 49,800.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3900.20` | 10,310,000.00 USD | 10,310,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.70` | 2,510,000.00 USD | 2,510,000.00 USD | 51,610.00 USD | 0.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3904.40` | 10,200,000.00 USD | 10,200,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.90` | 2,460,000.00 USD | 2,460,000.00 USD | 20,800.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3908.60` | 10,160,000.00 USD | 10,160,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.80` | 10,110,000.00 USD | 10,110,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3916.30` | 2,430,000.00 USD | 2,430,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.00` | 10,080,000.00 USD | 10,080,000.00 USD | 389,720.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3921.20` | 9,670,000.00 USD | 9,670,000.00 USD | 992,680.00 USD | 0.00 USD | 67,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.40` | 8,610,000.00 USD | 8,610,000.00 USD | 636,890.00 USD | 0.00 USD | 143,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.60` | 7,830,000.00 USD | 7,830,000.00 USD | 907,960.00 USD | 0.00 USD | 164,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.80` | 6,760,000.00 USD | 6,760,000.00 USD | 424,200.00 USD | 0.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,290,000.00 USD | 6,290,000.00 USD | 422,750.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3941.50` | 2,420,000.00 USD | 2,420,000.00 USD | 15,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.20` | 5,840,000.00 USD | 5,840,000.00 USD | 254,740.00 USD | 0.00 USD | 42,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3945.70` | 2,410,000.00 USD | 2,410,000.00 USD | 174,240.00 USD | 0.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.40` | 5,550,000.00 USD | 5,550,000.00 USD | 654,020.00 USD | 0.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.90` | 2,220,000.00 USD | 2,220,000.00 USD | 254,010.00 USD | 0.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.60` | 4,770,000.00 USD | 4,770,000.00 USD | 1,080,000.00 USD | 0.00 USD | 70,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.10` | 1,920,000.00 USD | 1,920,000.00 USD | 207,790.00 USD | 0.00 USD | 26,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.80` | 3,610,000.00 USD | 3,610,000.00 USD | 808,000.00 USD | 0.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.30` | 1,690,000.00 USD | 1,690,000.00 USD | 345,090.00 USD | 0.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.00` | 2,720,000.00 USD | 2,720,000.00 USD | 920,340.00 USD | 0.00 USD | 200,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.50` | 1,320,000.00 USD | 1,320,000.00 USD | 361,130.00 USD | 0.00 USD | 60,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.20` | 1,600,000.00 USD | 1,600,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.70` | 901,920.00 USD | 901,920.00 USD | 194,640.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.40` | 1,170,000.00 USD | 1,170,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3970.90` | 669,790.00 USD | 669,790.00 USD | 55,620.00 USD | 0.00 USD | 36,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.60` | 993,340.00 USD | 993,340.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.10` | 577,510.00 USD | 577,510.00 USD | 243,510.00 USD | 0.00 USD | 18,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.80` | 746,380.00 USD | 746,380.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.30` | 315,870.00 USD | 315,870.00 USD | 83,910.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.00` | 477,160.00 USD | 477,160.00 USD | 232,530.00 USD | 0.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.50` | 213,340.00 USD | 213,340.00 USD | 120,150.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.20` | 227,870.00 USD | 227,870.00 USD | 34,110.00 USD | 0.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3987.70` | 82,620.00 USD | 82,620.00 USD | 52,470.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3988.40` | 167,600.00 USD | 167,600.00 USD | 113,270.00 USD | 0.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3992.60` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3996.10` | 20,280.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4000.30` | 15,300.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4072.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4076.60` | 421,480.00 USD | 421,480.00 USD | 389,720.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4080.80` | 1,160,000.00 USD | 1,160,000.00 USD | 669,010.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.00` | 2,200,000.00 USD | 2,200,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4089.20` | 3,230,000.00 USD | 3,230,000.00 USD | 908,780.00 USD | 0.00 USD | 122,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4093.40` | 3,580,000.00 USD | 3,580,000.00 USD | 267,370.00 USD | 0.00 USD | 86,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.60` | 4,140,000.00 USD | 4,140,000.00 USD | 516,580.00 USD | 0.00 USD | 37,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.80` | 4,400,000.00 USD | 4,400,000.00 USD | 238,850.00 USD | 0.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4105.30` | 148,100.00 USD | 148,100.00 USD | 143,100.00 USD | 0.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.00` | 5,050,000.00 USD | 5,050,000.00 USD | 540,860.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4109.50` | 352,360.00 USD | 352,360.00 USD | 170,600.00 USD | 0.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.20` | 6,240,000.00 USD | 6,240,000.00 USD | 1,130,000.00 USD | 0.00 USD | 63,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4113.70` | 664,330.00 USD | 664,330.00 USD | 281,450.00 USD | 0.00 USD | 30,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.40` | 7,060,000.00 USD | 7,060,000.00 USD | 707,700.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.90` | 822,170.00 USD | 822,170.00 USD | 136,130.00 USD | 0.00 USD | 21,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,010,000.00 USD | 8,010,000.00 USD | 793,490.00 USD | 0.00 USD | 157,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.10` | 1,330,000.00 USD | 1,330,000.00 USD | 457,960.00 USD | 0.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.80` | 8,770,000.00 USD | 8,770,000.00 USD | 645,670.00 USD | 0.00 USD | 119,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.30` | 1,610,000.00 USD | 1,610,000.00 USD | 231,470.00 USD | 0.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.00` | 9,000,000.00 USD | 9,000,000.00 USD | 165,710.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.50` | 1,780,000.00 USD | 1,780,000.00 USD | 134,870.00 USD | 0.00 USD | 32,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.20` | 9,220,000.00 USD | 9,220,000.00 USD | 174,770.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4134.70` | 1,950,000.00 USD | 1,950,000.00 USD | 155,080.00 USD | 0.00 USD | 16,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.40` | 9,440,000.00 USD | 9,440,000.00 USD | 209,230.00 USD | 0.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.90` | 2,120,000.00 USD | 2,120,000.00 USD | 152,920.00 USD | 0.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.60` | 9,650,000.00 USD | 9,650,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.10` | 2,240,000.00 USD | 2,240,000.00 USD | 99,610.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.80` | 9,870,000.00 USD | 9,870,000.00 USD | 199,160.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.30` | 2,340,000.00 USD | 2,340,000.00 USD | 97,320.00 USD | 0.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.00` | 9,960,000.00 USD | 9,960,000.00 USD | 59,830.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4151.50` | 2,400,000.00 USD | 2,400,000.00 USD | 47,500.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.20` | 10,060,000.00 USD | 10,060,000.00 USD | 87,550.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.40` | 10,280,000.00 USD | 10,280,000.00 USD | 203,340.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.90` | 2,420,000.00 USD | 2,420,000.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.60` | 10,600,000.00 USD | 10,600,000.00 USD | 290,090.00 USD | 0.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4164.80` | 11,140,000.00 USD | 11,140,000.00 USD | 478,890.00 USD | 0.00 USD | 56,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.00` | 11,680,000.00 USD | 11,680,000.00 USD | 481,630.00 USD | 0.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.20` | 11,880,000.00 USD | 11,880,000.00 USD | 153,670.00 USD | 0.00 USD | 49,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4177.40` | 12,160,000.00 USD | 12,160,000.00 USD | 258,290.00 USD | 0.00 USD | 20,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4181.60` | 12,280,000.00 USD | 12,280,000.00 USD | 110,570.00 USD | 0.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.10` | 2,460,000.00 USD | 2,460,000.00 USD | 37,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.80` | 12,540,000.00 USD | 12,540,000.00 USD | 212,310.00 USD | 0.00 USD | 43,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.30` | 2,590,000.00 USD | 2,590,000.00 USD | 111,590.00 USD | 0.00 USD | 16,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.00` | 13,030,000.00 USD | 13,030,000.00 USD | 451,780.00 USD | 0.00 USD | 41,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.50` | 2,710,000.00 USD | 2,710,000.00 USD | 107,300.00 USD | 0.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4194.20` | 13,500,000.00 USD | 13,500,000.00 USD | 429,400.00 USD | 0.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.70` | 2,820,000.00 USD | 2,820,000.00 USD | 94,950.00 USD | 0.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.40` | 14,050,000.00 USD | 14,050,000.00 USD | 475,650.00 USD | 0.00 USD | 71,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.90` | 3,040,000.00 USD | 3,040,000.00 USD | 206,890.00 USD | 0.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.60` | 14,380,000.00 USD | 14,380,000.00 USD | 279,630.00 USD | 0.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.10` | 3,200,000.00 USD | 3,200,000.00 USD | 133,400.00 USD | 0.00 USD | 33,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.80` | 14,580,000.00 USD | 14,580,000.00 USD | 153,500.00 USD | 0.00 USD | 43,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4210.30` | 3,300,000.00 USD | 3,300,000.00 USD | 86,350.00 USD | 0.00 USD | 12,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,670,000.00 USD | 14,670,000.00 USD | 62,650.00 USD | 0.00 USD | 21,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4214.50` | 3,370,000.00 USD | 3,370,000.00 USD | 54,900.00 USD | 0.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.20` | 14,780,000.00 USD | 14,780,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4218.70` | 3,480,000.00 USD | 3,480,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.40` | 14,900,000.00 USD | 14,900,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4222.90` | 3,530,000.00 USD | 3,530,000.00 USD | 41,960.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.60` | 15,020,000.00 USD | 15,020,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.10` | 3,580,000.00 USD | 3,580,000.00 USD | 49,400.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4227.80` | 15,050,000.00 USD | 15,050,000.00 USD | 17,060.00 USD | 0.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4231.30` | 3,610,000.00 USD | 3,610,000.00 USD | 21,060.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.00` | 15,120,000.00 USD | 15,120,000.00 USD | 50,070.00 USD | 0.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4235.50` | 3,620,000.00 USD | 3,620,000.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.20` | 15,140,000.00 USD | 15,140,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4239.70` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4243.90` | 3,630,000.00 USD | 3,630,000.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.80` | 15,200,000.00 USD | 15,200,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.00` | 15,300,000.00 USD | 15,300,000.00 USD | 92,310.00 USD | 0.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.20` | 15,450,000.00 USD | 15,450,000.00 USD | 130,400.00 USD | 0.00 USD | 19,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.40` | 15,620,000.00 USD | 15,620,000.00 USD | 142,360.00 USD | 0.00 USD | 19,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4412.60` | 15,690,000.00 USD | 15,690,000.00 USD | 50,960.00 USD | 0.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4416.80` | 15,740,000.00 USD | 15,740,000.00 USD | 51,780.00 USD | 0.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.00` | 15,810,000.00 USD | 15,810,000.00 USD | 62,350.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4424.50` | 3,640,000.00 USD | 3,640,000.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4425.20` | 15,850,000.00 USD | 15,850,000.00 USD | 40,820.00 USD | 0.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4428.70` | 3,670,000.00 USD | 3,670,000.00 USD | 25,930.00 USD | 0.00 USD | 3,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4429.40` | 15,940,000.00 USD | 15,940,000.00 USD | 70,130.00 USD | 0.00 USD | 19,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.90` | 3,700,000.00 USD | 3,700,000.00 USD | 25,170.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4433.60` | 16,150,000.00 USD | 16,150,000.00 USD | 188,760.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4437.10` | 3,730,000.00 USD | 3,730,000.00 USD | 30,580.00 USD | 0.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4437.80` | 16,240,000.00 USD | 16,240,000.00 USD | 82,170.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4441.30` | 3,760,000.00 USD | 3,760,000.00 USD | 24,550.00 USD | 0.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.00` | 16,370,000.00 USD | 16,370,000.00 USD | 114,900.00 USD | 0.00 USD | 22,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4445.10` | 3,820,000.00 USD | 3,820,000.00 USD | 53,030.00 USD | 0.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,440,000.00 USD | 16,440,000.00 USD | 48,670.00 USD | 0.00 USD | 17,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4450.40` | 16,480,000.00 USD | 16,480,000.00 USD | 33,140.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4453.60` | 16,500,000.00 USD | 16,500,000.00 USD | 17,720.00 USD | 0.00 USD | 2,550.00 USD | `Tier 1 CEX` |

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
| `1D` | `3617.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD |
| `7D` | `3617.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD |
| `1D` | `3621.40` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `3621.40` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD |
| `1D` | `3625.60` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD |
| `7D` | `3625.60` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD |
| `1D` | `3629.80` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `3629.80` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD |
| `1D` | `3634.00` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD |
| `7D` | `3634.00` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD |
| `1D` | `3638.20` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `3638.20` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD |
| `1D` | `3642.40` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `3642.40` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD |
| `1D` | `3646.60` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD |
| `7D` | `3646.60` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD |
| `1D` | `3650.80` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `3650.80` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD |
| `1D` | `3655.00` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `3655.00` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD |
| `1D` | `3659.20` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD |
| `7D` | `3659.20` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD |
| `1D` | `3663.40` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3663.40` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `3671.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3671.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `1D` | `3860.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD |
| `7D` | `3860.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD |
| `1D` | `3865.00` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 138,500.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `3865.00` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 138,500.00 USD | 0.00 USD | 14,270.00 USD |
| `1D` | `3869.20` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 127,010.00 USD | 0.00 USD | 20,780.00 USD |
| `7D` | `3869.20` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 127,010.00 USD | 0.00 USD | 20,780.00 USD |
| `1D` | `3873.40` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD |
| `7D` | `3873.40` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD |
| `1D` | `3877.60` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `3877.60` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD |
| `1D` | `3881.80` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD |
| `7D` | `3881.80` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD |
| `1D` | `3886.00` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD |
| `7D` | `3886.00` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD |
| `1D` | `3890.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD |
| `7D` | `3890.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD |
| `1D` | `3894.40` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3894.40` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `1D` | `3898.60` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3898.60` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD |
| `1D` | `3902.80` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD |
| `7D` | `3902.80` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD |
| `1D` | `3907.00` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.00` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD |
| `1D` | `3915.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3915.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `3940.60` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD |
| `7D` | `3940.60` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD |
| `1D` | `3944.80` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD |
| `7D` | `3944.80` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD |
| `1D` | `3949.00` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 193,440.00 USD | 0.00 USD | 43,910.00 USD |
| `7D` | `3949.00` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 193,440.00 USD | 0.00 USD | 43,910.00 USD |
| `1D` | `3953.20` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD |
| `7D` | `3953.20` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD |
| `1D` | `3957.40` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD |
| `7D` | `3957.40` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD |
| `1D` | `3961.60` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD |
| `7D` | `3961.60` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD |
| `1D` | `3965.80` | 863,010.00 USD | 0.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD |
| `7D` | `3965.80` | 863,010.00 USD | 0.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD |
| `1D` | `3970.00` | 714,020.00 USD | 0.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD |
| `7D` | `3970.00` | 714,020.00 USD | 0.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD |
| `1D` | `3974.20` | 591,750.00 USD | 0.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3974.20` | 591,750.00 USD | 0.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD |
| `1D` | `3978.40` | 386,370.00 USD | 0.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD |
| `7D` | `3978.40` | 386,370.00 USD | 0.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD |
| `1D` | `3982.60` | 253,490.00 USD | 0.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD |
| `7D` | `3982.60` | 253,490.00 USD | 0.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD |
| `1D` | `3986.80` | 119,030.00 USD | 0.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3986.80` | 119,030.00 USD | 0.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD |
| `1D` | `3991.00` | 51,990.00 USD | 0.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3991.00` | 51,990.00 USD | 0.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3995.20` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `3995.20` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `3999.40` | 15,300.00 USD | 0.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3999.40` | 15,300.00 USD | 0.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4026.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4027.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 0.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 0.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD |
| `1D` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 0.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD |
| `7D` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 0.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD |
| `1D` | `4108.60` | 554,190.00 USD | 554,190.00 USD | 0.00 USD | 286,640.00 USD | 0.00 USD | 45,070.00 USD |
| `7D` | `4108.60` | 554,190.00 USD | 554,190.00 USD | 0.00 USD | 286,640.00 USD | 0.00 USD | 45,070.00 USD |
| `1D` | `4112.80` | 817,270.00 USD | 817,270.00 USD | 0.00 USD | 220,390.00 USD | 0.00 USD | 42,690.00 USD |
| `7D` | `4112.80` | 817,270.00 USD | 817,270.00 USD | 0.00 USD | 220,390.00 USD | 0.00 USD | 42,690.00 USD |
| `1D` | `4117.00` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD |
| `7D` | `4117.00` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4121.20` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD |
| `7D` | `4121.20` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD |
| `1D` | `4125.40` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD |
| `7D` | `4125.40` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD |
| `1D` | `4129.60` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4129.60` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD |
| `1D` | `4133.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD |
| `7D` | `4133.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD |
| `1D` | `4138.00` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4138.00` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD |
| `1D` | `4142.20` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4142.20` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD |
| `1D` | `4146.40` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD |
| `7D` | `4146.40` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD |
| `1D` | `4150.60` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4150.60` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD |
| `1D` | `4159.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4159.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `4163.20` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4163.20` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4180.00` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD |
| `7D` | `4180.00` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD |
| `1D` | `4184.20` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `4184.20` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD |
| `1D` | `4188.40` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 112,780.00 USD | 0.00 USD | 18,900.00 USD |
| `7D` | `4188.40` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 112,780.00 USD | 0.00 USD | 18,900.00 USD |
| `1D` | `4192.60` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 151,790.00 USD | 0.00 USD | 19,110.00 USD |
| `7D` | `4192.60` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 151,790.00 USD | 0.00 USD | 19,110.00 USD |
| `1D` | `4196.80` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD |
| `7D` | `4196.80` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD |
| `1D` | `4201.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD |
| `7D` | `4201.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD |
| `1D` | `4205.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD |
| `7D` | `4205.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD |
| `1D` | `4209.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD |
| `7D` | `4209.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD |
| `1D` | `4213.60` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD |
| `7D` | `4213.60` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD |
| `1D` | `4217.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD |
| `7D` | `4217.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD |
| `1D` | `4222.00` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD |
| `7D` | `4222.00` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD |
| `1D` | `4226.20` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD |
| `7D` | `4226.20` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD |
| `1D` | `4230.40` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `4230.40` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `4234.60` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD |
| `7D` | `4234.60` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD |
| `1D` | `4243.00` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4243.00` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `4423.60` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `4423.60` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD |
| `1D` | `4427.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD |
| `7D` | `4427.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD |
| `1D` | `4432.00` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD |
| `7D` | `4432.00` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `4434.30` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD |
| `7D` | `4434.30` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.41M` | Total OI Tokens: `68,421.2 PAXG`
  * 1h OI Change: `+0.12%` | 4h OI Change: `-0.06%` | 24h OI Change: `+0.61%`
  * Exchange Breakdown: Binance=`106.98M` | Bybit=`20.01M` | OKX=`-` | Hyperliquid=`25.79M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.12K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `38.35%` | `61.65%` | `0.62` | 1,170,000.00 USD |
| `15M` | `Binance` | `46.34%` | `53.66%` | `0.86` | 149,010.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `46.11%` | `53.89%` | `0.86` | 204,790.00 USD |
| `15M` | `KuCoin` | `74.36%` | `25.64%` | `2.90` | 3,150.00 USD |
| `15M` | `Gate` | `26.23%` | `73.77%` | `0.36` | 111,960.00 USD |
| `15M` | `Bitget` | `44.22%` | `55.78%` | `0.79` | 135,750.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `41.54%` | `58.46%` | `0.71` | 296,780.00 USD |
| `15M` | `Bitunix` | `70.59%` | `29.41%` | `2.40` | 23,490.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `36.84%` | `63.16%` | `0.58` | 139,270.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.16%` | `99.84%` | `0.00` | 100,870.00 USD |
| `15M` | `HTX` | `58.3%` | `41.7%` | `1.40` | 1,040.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 80.27 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `46.34%` | `53.66%` | `0.86` | 149,010.00 USD |
| `15M` | `Global Accounts` | `38.35%` | `61.65%` | `0.62` | 1,170,000.00 USD |
| `1H` | `PAXG` | `49.44%` | `50.56%` | `0.98` | 18,770,000.00 USD |
| `1H` | `Binance` | `52.11%` | `47.89%` | `1.09` | 1,800,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `36.29%` | `63.71%` | `0.57` | 1,350,000.00 USD |
| `1H` | `KuCoin` | `47.96%` | `52.04%` | `0.92` | 85,290.00 USD |
| `1H` | `Gate` | `45.5%` | `54.5%` | `0.83` | 552,070.00 USD |
| `1H` | `Bitget` | `41.46%` | `58.54%` | `0.71` | 559,640.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `52.03%` | `47.97%` | `1.08` | 12,300,000.00 USD |
| `1H` | `Bitunix` | `50.45%` | `49.55%` | `1.02` | 491,660.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.02%` | `45.98%` | `1.17` | 1,230,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.06%` | `99.94%` | `0.00` | 371,670.00 USD |
| `1H` | `HTX` | `50.53%` | `49.47%` | `1.02` | 3,430.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.25%` | `46.75%` | `1.14` | 35,450.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `52.11%` | `47.89%` | `1.09` | 1,800,000.00 USD |
| `1H` | `Global Accounts` | `49.44%` | `50.56%` | `0.98` | 18,770,000.00 USD |
| `4H` | `PAXG` | `48.02%` | `51.98%` | `0.92` | 100,110,000.00 USD |
| `4H` | `Binance` | `51.73%` | `48.27%` | `1.07` | 7,020,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `50.8%` | `49.2%` | `1.03` | 6,340,000.00 USD |
| `4H` | `KuCoin` | `52.17%` | `47.83%` | `1.09` | 466,440.00 USD |
| `4H` | `Gate` | `45.67%` | `54.33%` | `0.84` | 2,060,000.00 USD |
| `4H` | `Bitget` | `48.57%` | `51.43%` | `0.94` | 4,110,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `48.39%` | `51.61%` | `0.94` | 65,070,000.00 USD |
| `4H` | `Bitunix` | `50.37%` | `49.63%` | `1.01` | 3,910,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.24%` | `44.76%` | `1.23` | 7,790,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.66%` | `95.34%` | `0.05` | 3,130,000.00 USD |
| `4H` | `HTX` | `91.52%` | `8.48%` | `10.79` | 62,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.72%` | `53.28%` | `0.88` | 147,510.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `51.73%` | `48.27%` | `1.07` | 7,020,000.00 USD |
| `4H` | `Global Accounts` | `48.02%` | `51.98%` | `0.92` | 100,110,000.00 USD |


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
| `5m` | -15,410.00 USD | -8,560.00 USD | **`DISTRIBUTION`** |
| `15m` | -6,440.00 USD | 445,570.00 USD | **`ACCUMULATION`** |
| `30m` | 35,910.00 USD | 553,040.00 USD | **`ACCUMULATION`** |
| `1h` | 567,800.00 USD | 553,260.00 USD | **`ACCUMULATION`** |
| `2h` | 766,040.00 USD | 563,350.00 USD | **`ACCUMULATION`** |
| `4h` | 596,440.00 USD | 545,960.00 USD | **`ACCUMULATION`** |
| `6h` | 376,980.00 USD | 1,260,000.00 USD | **`ACCUMULATION`** |
| `8h` | 359,200.00 USD | 700,310.00 USD | **`ACCUMULATION`** |
| `12h` | 450,440.00 USD | -196,750.00 USD | **`ACCUMULATION`** |
| `24h` | 148,170.00 USD | 926,690.00 USD | **`ACCUMULATION`** |
| `1w` | -9,130,000.00 USD | -8,870,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,650,000.00 USD | -72,550,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-15.41K` | 15m=`-6.44K` | 1h=`+567.80K` | 24h=`+148.17K`
* Futures Capital Netflows: 5m=`-8.56K` | 15m=`+445.57K` | 1h=`+553.26K` | 24h=`+926.69K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4019.82` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4007.63` (Risk Distance: `12.19` pts)
  * +2.5R Take Profit: `4050.29`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4052.90` (Risk Distance: `12.19` pts)
  * +2.5R Take Profit: `4010.24`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4049.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
