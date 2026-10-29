# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4022.23` | **Live Ask Quote**: `4022.32` | **Mid Price**: `4022.28`
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
  * Session VWAP: `4031.73` | VWAP Z-Score: `-1.20` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.11` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.86` | Lower -3.00σ Band: `3998.61`
  * Upper +2.51σ Band: `4059.45` | Lower -2.51σ Band: `4004.02`
  * Upper +2.01σ Band: `4053.92` | Lower -2.01σ Band: `4009.54`
  * Upper +2.00σ Band: `4053.81` | Lower -2.00σ Band: `4009.65`
  * Upper +1.28σ Band: `4045.87` | Lower -1.28σ Band: `4017.60`
  * Upper +1.00σ Band: `4042.77` | Lower -1.00σ Band: `4020.69`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4019.99` | EMA-20=`4022.90` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4028.40` (Slope: `+0.0000`) | EMA-100=`4033.93`
  * Institutional Anchors: EMA-144=`4034.66` | EMA-200=`4033.61` (Slope: `-0.0346`) | EMA-233=`4032.43`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4010.16` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.71` (Distance: `-0.47%`)
  * Point of Control (POC) = `4027.30` (Distance: `-0.14%`)
  * Value Area Low (VAL) = `4019.82` (Distance: `+0.05%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `4006.19` - `4038.36`
  * Optimal Trade Entry (OTE 0.705): `4030.32`
  * Structural Invalidation Anchor (0.786): `4054.45`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4023.30` | `4024.01` | `4022.15` | `4022.67` | `23` | 91,006.45 USD | -11,562.25 USD | `-12.70%` | 966,104.60 USD | `-0.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4022.71` | `4027.05` | `4022.71` | `4027.05` | `51` | 204,320.84 USD | 79,817.65 USD | `+39.06%` | 1,045,922.25 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4027.05` | `4029.00` | `4026.44` | `4026.45` | `67` | 269,723.43 USD | 116,882.30 USD | `+43.33%` | 1,162,804.55 USD | `+0.71` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4019.60` | `4021.70` | `4017.67` | `4021.36` | `133` | 536,295.57 USD | -74,630.45 USD | `-13.92%` | 494,219.57 USD | `-0.70` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4021.36` | `4023.30` | `4019.39` | `4023.30` | `201` | 809,848.30 USD | 483,447.28 USD | `+59.70%` | 977,666.85 USD | `+2.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4023.30` | `4029.00` | `4022.15` | `4026.45` | `140` | 565,042.67 USD | 185,129.64 USD | `+32.76%` | 1,162,796.49 USD | `+0.72` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4029.13` | `4030.46` | `4023.08` | `4026.82` | `526` | 2,116,236.19 USD | -146,951.88 USD | `-6.94%` | -157,920.93 USD | `-0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 692,493.29 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4022.15` | `4026.45` | `140` | 565,050.72 USD | 185,137.69 USD | `+32.76%` | 877,630.98 USD | `+0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4016.00` | `4026.45` | `1,091` | 4,388,772.05 USD | 1,035,547.88 USD | `+23.60%` | 1,412,598.16 USD | `+1.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4016.00` | `4026.45` | `1,091` | 4,388,772.05 USD | 1,035,547.88 USD | `+23.60%` | 1,412,598.16 USD | `+1.43` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4020.80` | `1.9419` | 7,807.99 USD | 1,590,900.30 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4020.90` | `8.1991` | 32,967.76 USD | 1,583,092.30 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4021.00` | `6.8726` | 27,634.72 USD | 1,550,124.54 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4021.10` | `10.9684` | 44,105.03 USD | 1,522,489.82 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4021.20` | `17.0225` | 68,450.88 USD | 1,478,384.79 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4021.30` | `127.8459` | 514,106.72 USD | 1,409,933.91 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4021.40` | `4.1419` | 16,656.24 USD | 895,827.19 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4021.50` | `14.9051` | 59,940.86 USD | 879,170.95 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.60` | `8.5463` | 34,369.80 USD | 819,230.09 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4021.70` | `3.8986` | 15,679.00 USD | 784,860.29 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.80` | `12.8333` | 51,612.97 USD | 769,181.29 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4022.00` | `63.1664` | 254,055.26 USD | 717,568.33 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.10` | `7.6757` | 30,872.43 USD | 463,513.07 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.20` | `41.0424` | 165,080.74 USD | 432,640.64 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.30` | `7.8028` | 31,385.20 USD | 267,559.89 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4022.40` | `17.8688` | 71,875.46 USD | 236,174.69 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4022.50` | `36.4668` | 146,687.70 USD | 164,299.23 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4022.60` | `1.3319` | 5,357.70 USD | 17,611.53 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4022.70` | `0.2485` | 999.64 USD | 12,253.83 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4022.80` | `2.7976` | 11,254.19 USD | 11,254.19 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4022.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,022.85` | `0.00%` | `-` |
| `ASK` | `4022.90` | `12.8762` | 51,799.66 USD | 51,799.66 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `4023.00` | `14.5241` | 58,430.45 USD | 110,230.12 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4023.20` | `10.5846` | 42,583.96 USD | 152,814.08 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4023.30` | `6.1798` | 24,863.19 USD | 177,677.27 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4023.40` | `27.2798` | 109,757.55 USD | 287,434.82 USD | `13 orders` | `+0.01%` | `-` |
| `ASK` | `4023.50` | `20.9442` | 84,268.99 USD | 371,703.81 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4023.60` | `51.0499` | 205,404.38 USD | 577,108.18 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4023.70` | `9.1139` | 36,671.60 USD | 613,779.78 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4023.80` | `3.2957` | 13,261.24 USD | 627,041.02 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4023.90` | `17.6041` | 70,837.14 USD | 697,878.16 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4024.00` | `70.8998` | 285,300.80 USD | 983,178.96 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `4024.10` | `12.2340` | 49,230.84 USD | 1,032,409.79 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4024.20` | `7.1793` | 28,890.94 USD | 1,061,300.73 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4024.30` | `1.9065` | 7,672.33 USD | 1,068,973.06 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4024.40` | `15.6287` | 62,896.14 USD | 1,131,869.20 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4024.50` | `7.9026` | 31,804.01 USD | 1,163,673.22 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.60` | `5.5310` | 22,260.06 USD | 1,185,933.28 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.70` | `58.5952` | 235,828.10 USD | 1,421,761.38 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4024.80` | `22.2723` | 89,641.55 USD | 1,511,402.93 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4024.90` | `8.4390` | 33,966.13 USD | 1,545,369.06 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

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
| `1D` | `Long Liquidation` | `3617.20` | 4,100,000.00 USD | 4,100,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.20` | 4,100,000.00 USD | 4,100,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.40` | 4,100,000.00 USD | 4,100,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.40` | 4,100,000.00 USD | 4,100,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.60` | 4,070,000.00 USD | 4,070,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3625.60` | 4,070,000.00 USD | 4,070,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.80` | 4,020,000.00 USD | 4,020,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3629.80` | 4,020,000.00 USD | 4,020,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.00` | 3,970,000.00 USD | 3,970,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.00` | 3,970,000.00 USD | 3,970,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.20` | 3,940,000.00 USD | 3,940,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3638.20` | 3,940,000.00 USD | 3,940,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3642.40` | 3,870,000.00 USD | 3,870,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3642.40` | 3,870,000.00 USD | 3,870,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3646.60` | 3,850,000.00 USD | 3,850,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3646.60` | 3,850,000.00 USD | 3,850,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.80` | 3,830,000.00 USD | 3,830,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3650.80` | 3,830,000.00 USD | 3,830,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.00` | 3,790,000.00 USD | 3,790,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3655.00` | 3,790,000.00 USD | 3,790,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3659.20` | 3,770,000.00 USD | 3,770,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3659.20` | 3,770,000.00 USD | 3,770,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3663.40` | 3,760,000.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3663.40` | 3,760,000.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.80` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3671.80` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.80` | 3,750,000.00 USD | 3,750,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.80` | 3,750,000.00 USD | 3,750,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.00` | 3,680,000.00 USD | 3,680,000.00 USD | 138,500.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3865.00` | 3,680,000.00 USD | 3,680,000.00 USD | 138,500.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.20` | 3,530,000.00 USD | 3,530,000.00 USD | 127,010.00 USD | 0.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 3,530,000.00 USD | 3,530,000.00 USD | 127,010.00 USD | 0.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.40` | 3,380,000.00 USD | 3,380,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.40` | 3,380,000.00 USD | 3,380,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.60` | 3,260,000.00 USD | 3,260,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.60` | 3,260,000.00 USD | 3,260,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.80` | 3,070,000.00 USD | 3,070,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.80` | 3,070,000.00 USD | 3,070,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3886.00` | 2,910,000.00 USD | 2,910,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.00` | 2,910,000.00 USD | 2,910,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3890.20` | 2,830,000.00 USD | 2,830,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.20` | 2,830,000.00 USD | 2,830,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3894.40` | 2,760,000.00 USD | 2,760,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.40` | 2,760,000.00 USD | 2,760,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.60` | 2,660,000.00 USD | 2,660,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.60` | 2,660,000.00 USD | 2,660,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.80` | 2,600,000.00 USD | 2,600,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3902.80` | 2,600,000.00 USD | 2,600,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.00` | 2,540,000.00 USD | 2,540,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.00` | 2,540,000.00 USD | 2,540,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.40` | 2,510,000.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.40` | 2,510,000.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.60` | 2,500,000.00 USD | 2,500,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.60` | 2,500,000.00 USD | 2,500,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.80` | 2,390,000.00 USD | 2,390,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.80` | 2,390,000.00 USD | 2,390,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.00` | 2,080,000.00 USD | 2,080,000.00 USD | 193,440.00 USD | 0.00 USD | 43,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3949.00` | 2,080,000.00 USD | 2,080,000.00 USD | 193,440.00 USD | 0.00 USD | 43,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.20` | 1,840,000.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.20` | 1,840,000.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.40` | 1,550,000.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.40` | 1,550,000.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.60` | 1,310,000.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,310,000.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.80` | 863,010.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.80` | 863,010.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3970.00` | 714,020.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.00` | 714,020.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3974.20` | 591,750.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.20` | 591,750.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3978.40` | 386,370.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.40` | 386,370.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3982.60` | 253,490.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3982.60` | 253,490.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.80` | 119,030.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3986.80` | 119,030.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3991.00` | 51,990.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.00` | 51,990.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3995.20` | 20,280.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3995.20` | 20,280.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3999.40` | 15,300.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3999.40` | 15,300.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.60` | 554,190.00 USD | 554,190.00 USD | 286,640.00 USD | 0.00 USD | 45,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4108.60` | 554,190.00 USD | 554,190.00 USD | 286,640.00 USD | 0.00 USD | 45,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.80` | 817,270.00 USD | 817,270.00 USD | 220,390.00 USD | 0.00 USD | 42,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.80` | 817,270.00 USD | 817,270.00 USD | 220,390.00 USD | 0.00 USD | 42,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.00` | 1,050,000.00 USD | 1,050,000.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4117.00` | 1,050,000.00 USD | 1,050,000.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.20` | 1,440,000.00 USD | 1,440,000.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4121.20` | 1,440,000.00 USD | 1,440,000.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.40` | 1,710,000.00 USD | 1,710,000.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.40` | 1,710,000.00 USD | 1,710,000.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.60` | 1,840,000.00 USD | 1,840,000.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.60` | 1,840,000.00 USD | 1,840,000.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.80` | 1,980,000.00 USD | 1,980,000.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.80` | 1,980,000.00 USD | 1,980,000.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.00` | 2,180,000.00 USD | 2,180,000.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4138.00` | 2,180,000.00 USD | 2,180,000.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4142.20` | 2,290,000.00 USD | 2,290,000.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 2,290,000.00 USD | 2,290,000.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.40` | 2,420,000.00 USD | 2,420,000.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.40` | 2,420,000.00 USD | 2,420,000.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.60` | 2,480,000.00 USD | 2,480,000.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.60` | 2,480,000.00 USD | 2,480,000.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.20` | 2,500,000.00 USD | 2,500,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.20` | 2,500,000.00 USD | 2,500,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.00` | 2,520,000.00 USD | 2,520,000.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.00` | 2,520,000.00 USD | 2,520,000.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,600,000.00 USD | 2,600,000.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4184.20` | 2,600,000.00 USD | 2,600,000.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.40` | 2,730,000.00 USD | 2,730,000.00 USD | 112,780.00 USD | 0.00 USD | 18,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4188.40` | 2,730,000.00 USD | 2,730,000.00 USD | 112,780.00 USD | 0.00 USD | 18,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.60` | 2,900,000.00 USD | 2,900,000.00 USD | 151,790.00 USD | 0.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4192.60` | 2,900,000.00 USD | 2,900,000.00 USD | 151,790.00 USD | 0.00 USD | 19,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.80` | 3,000,000.00 USD | 3,000,000.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.80` | 3,000,000.00 USD | 3,000,000.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.00` | 3,180,000.00 USD | 3,180,000.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4201.00` | 3,180,000.00 USD | 3,180,000.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.20` | 3,330,000.00 USD | 3,330,000.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4205.20` | 3,330,000.00 USD | 3,330,000.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.40` | 3,420,000.00 USD | 3,420,000.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4209.40` | 3,420,000.00 USD | 3,420,000.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.60` | 3,450,000.00 USD | 3,450,000.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.60` | 3,450,000.00 USD | 3,450,000.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.80` | 3,580,000.00 USD | 3,580,000.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.80` | 3,580,000.00 USD | 3,580,000.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4222.00` | 3,620,000.00 USD | 3,620,000.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4222.00` | 3,620,000.00 USD | 3,620,000.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4226.20` | 3,690,000.00 USD | 3,690,000.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.20` | 3,690,000.00 USD | 3,690,000.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4230.40` | 3,720,000.00 USD | 3,720,000.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 3,720,000.00 USD | 3,720,000.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4234.60` | 3,740,000.00 USD | 3,740,000.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.60` | 3,740,000.00 USD | 3,740,000.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4243.00` | 3,750,000.00 USD | 3,750,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4243.00` | 3,750,000.00 USD | 3,750,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4423.60` | 3,770,000.00 USD | 3,770,000.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.60` | 3,770,000.00 USD | 3,770,000.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.80` | 3,820,000.00 USD | 3,820,000.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4427.80` | 3,820,000.00 USD | 3,820,000.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.00` | 3,840,000.00 USD | 3,840,000.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.00` | 3,840,000.00 USD | 3,840,000.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4434.30` | 3,870,000.00 USD | 3,870,000.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.30` | 3,870,000.00 USD | 3,870,000.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD | `Tier 1 CEX` |

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
| `5m` | -28,970.00 USD | 24,100.00 USD | **`DISTRIBUTION`** |
| `15m` | -37,210.00 USD | 184,490.00 USD | **`ACCUMULATION`** |
| `30m` | -17,970.00 USD | 706,520.00 USD | **`ACCUMULATION`** |
| `1h` | 477,940.00 USD | 718,690.00 USD | **`ACCUMULATION`** |
| `2h` | 733,400.00 USD | 830,680.00 USD | **`ACCUMULATION`** |
| `4h` | 571,070.00 USD | 733,830.00 USD | **`ACCUMULATION`** |
| `6h` | 363,830.00 USD | 1,410,000.00 USD | **`ACCUMULATION`** |
| `8h` | 364,960.00 USD | 952,300.00 USD | **`ACCUMULATION`** |
| `12h` | 387,520.00 USD | 208,160.00 USD | **`ACCUMULATION`** |
| `24h` | 119,910.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,100,000.00 USD | -8,670,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,660,000.00 USD | -72,360,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-28.97K` | 15m=`-37.21K` | 1h=`+477.94K` | 24h=`+119.91K`
* Futures Capital Netflows: 5m=`+24.10K` | 15m=`+184.49K` | 1h=`+718.69K` | 24h=`+1.15M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `4009.95` (Risk Distance: `9.87` pts)
  * +2.5R Take Profit: `4044.50`
  * Mathematical Lot Sizing: **`1.01 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4050.58` (Risk Distance: `9.87` pts)
  * +2.5R Take Profit: `4016.03`
  * Mathematical Lot Sizing: **`1.01 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4054.45`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
