# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUT
**Canonical Key**: `XAUT` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4022.23` | **Live Ask Quote**: `4022.32` | **Mid Price**: `4022.28`
- **Spread Points**: `9.00` | **Spread BPS**: `0.22 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `1.00 USD` | Point Value (0.01 Lot): `0.0100 USD`
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
| `1403` | `0x46fc...1195` | `LONG` | 1,636,529.84 USD | `407.03` | `4055.53` | `4020.60` | `1868.06` | -14,180.35 USD | `-0.87%` | `20X Cross` |
| `1442` | `0xee02...309d` | `SHORT` | 1,608,280.00 USD | `400.00` | `4438.84` | `4020.60` | `4226.78` | 167,258.60 USD | `+10.40%` | `25X Isolated` |
| `1443` | `0x6d15...d374` | `LONG` | 1,608,200.00 USD | `400.00` | `4068.25` | `4020.60` | `3841.70` | -19,100.00 USD | `-1.19%` | `25X Cross` |
| `1476` | `0x02a7...fe9f` | `SHORT` | 1,568,073.00 USD | `390.00` | `4055.02` | `4020.60` | `4306.60` | 13,386.25 USD | `+0.85%` | `25X Cross` |
| `1505` | `0x7e77...b8d2` | `SHORT` | 1,527,866.00 USD | `380.00` | `4131.92` | `4020.60` | `4293.41` | 42,263.64 USD | `+2.77%` | `20X Cross` |
| `1520` | `0x72c2...9b37` | `LONG` | 1,500,249.02 USD | `373.13` | `4000.98` | `4020.60` | `3777.93` | 7,355.50 USD | `+0.49%` | `13X Isolated` |
| `1571` | `0xaa44...b844` | `LONG` | 1,446,840.00 USD | `360.00` | `4043.10` | `4020.60` | `2794.19` | -8,677.63 USD | `-0.60%` | `9X Cross` |
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
  * 24H Horizon: Short MP=`4118.06` (Vol: 271,900.00 USD, Dist: `+2.34%`) | Long MP=`3958.87` (Vol: 230,100.00 USD, Dist: `--1.61%`)
  * 48H Horizon: Short MP=`4118.06` (Vol: 350,900.00 USD, Dist: `+2.34%`) | Long MP=`3958.87` (Vol: 346,400.00 USD, Dist: `--1.61%`)
  * 3D Horizon: Short MP=`4110.46` (Vol: 300,700.00 USD, Dist: `+2.15%`) | Long MP=`3959.21` (Vol: 388,300.00 USD, Dist: `--1.60%`)
  * 7D Horizon: Short MP=`4082.49` (Vol: 552,000.00 USD, Dist: `+1.46%`) | Long MP=`3921.81` (Vol: 617,500.00 USD, Dist: `--2.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

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
| `1D` | `3610.30` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `3610.30` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `1D` | `3614.50` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 4,120.00 USD | 0.00 USD | 12,600.00 USD |
| `7D` | `3614.50` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 4,120.00 USD | 0.00 USD | 12,600.00 USD |
| `1D` | `3618.70` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 8,500.00 USD | 0.00 USD | 24,060.00 USD |
| `7D` | `3618.70` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 8,500.00 USD | 0.00 USD | 24,060.00 USD |
| `1D` | `3622.90` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3622.90` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `1D` | `3627.10` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 25,060.00 USD | 0.00 USD | 26,370.00 USD |
| `7D` | `3627.10` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 25,060.00 USD | 0.00 USD | 26,370.00 USD |
| `1D` | `3631.30` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 45,550.00 USD | 0.00 USD | 56,520.00 USD |
| `7D` | `3631.30` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 45,550.00 USD | 0.00 USD | 56,520.00 USD |
| `1D` | `3635.50` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 39,930.00 USD | 0.00 USD | 23,450.00 USD |
| `7D` | `3635.50` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 39,930.00 USD | 0.00 USD | 23,450.00 USD |
| `1D` | `3639.70` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 12,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3639.70` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 12,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3643.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 15,910.00 USD | 0.00 USD | 10,260.00 USD |
| `7D` | `3643.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 15,910.00 USD | 0.00 USD | 10,260.00 USD |
| `1D` | `3648.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `3648.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `3652.30` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 19,030.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3652.30` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 19,030.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `3656.50` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3656.50` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `1D` | `3660.70` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3660.70` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3853.90` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 11,550.00 USD | 0.00 USD | 36,200.00 USD |
| `7D` | `3853.90` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 11,550.00 USD | 0.00 USD | 36,200.00 USD |
| `1D` | `3858.10` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 18,940.00 USD | 0.00 USD | 62,010.00 USD |
| `7D` | `3858.10` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 18,940.00 USD | 0.00 USD | 62,010.00 USD |
| `1D` | `3862.30` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 72,260.00 USD | 0.00 USD | 197,090.00 USD |
| `7D` | `3862.30` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 72,260.00 USD | 0.00 USD | 197,090.00 USD |
| `1D` | `3866.50` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 56,660.00 USD | 0.00 USD | 102,470.00 USD |
| `7D` | `3866.50` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 56,660.00 USD | 0.00 USD | 102,470.00 USD |
| `1D` | `3870.70` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 122,880.00 USD | 0.00 USD | 158,470.00 USD |
| `7D` | `3870.70` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 122,880.00 USD | 0.00 USD | 158,470.00 USD |
| `1D` | `3874.90` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 133,370.00 USD | 0.00 USD | 115,860.00 USD |
| `7D` | `3874.90` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 133,370.00 USD | 0.00 USD | 115,860.00 USD |
| `1D` | `3879.10` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 68,060.00 USD | 0.00 USD | 17,870.00 USD |
| `7D` | `3879.10` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 68,060.00 USD | 0.00 USD | 17,870.00 USD |
| `1D` | `3883.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3883.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `3887.50` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 30,170.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `3887.50` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 30,170.00 USD | 0.00 USD | 32,130.00 USD |
| `1D` | `3891.70` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `7D` | `3891.70` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `1D` | `3895.90` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 41,330.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `3895.90` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 41,330.00 USD | 0.00 USD | 19,740.00 USD |
| `1D` | `3900.10` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3900.10` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `1D` | `3904.30` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3904.30` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3933.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `7D` | `3933.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `1D` | `3937.90` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 45,160.00 USD | 0.00 USD | 120,280.00 USD |
| `7D` | `3937.90` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 45,160.00 USD | 0.00 USD | 120,280.00 USD |
| `1D` | `3942.10` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 107,830.00 USD | 0.00 USD | 293,550.00 USD |
| `7D` | `3942.10` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 107,830.00 USD | 0.00 USD | 293,550.00 USD |
| `1D` | `3946.30` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 134,190.00 USD | 0.00 USD | 303,170.00 USD |
| `7D` | `3946.30` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 134,190.00 USD | 0.00 USD | 303,170.00 USD |
| `1D` | `3950.50` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 203,270.00 USD | 0.00 USD | 198,870.00 USD |
| `7D` | `3950.50` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 203,270.00 USD | 0.00 USD | 198,870.00 USD |
| `1D` | `3954.70` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 215,080.00 USD | 0.00 USD | 331,940.00 USD |
| `7D` | `3954.70` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 215,080.00 USD | 0.00 USD | 331,940.00 USD |
| `1D` | `3958.90` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 205,310.00 USD | 0.00 USD | 69,840.00 USD |
| `7D` | `3958.90` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 205,310.00 USD | 0.00 USD | 69,840.00 USD |
| `1D` | `3963.10` | 749,680.00 USD | 0.00 USD | 749,680.00 USD | 51,840.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3963.10` | 749,680.00 USD | 0.00 USD | 749,680.00 USD | 51,840.00 USD | 0.00 USD | 7,030.00 USD |
| `1D` | `3967.30` | 690,810.00 USD | 0.00 USD | 690,810.00 USD | 107,870.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3967.30` | 690,810.00 USD | 0.00 USD | 690,810.00 USD | 107,870.00 USD | 0.00 USD | 43,420.00 USD |
| `1D` | `3971.50` | 539,520.00 USD | 0.00 USD | 539,520.00 USD | 55,160.00 USD | 0.00 USD | 91,380.00 USD |
| `7D` | `3971.50` | 539,520.00 USD | 0.00 USD | 539,520.00 USD | 55,160.00 USD | 0.00 USD | 91,380.00 USD |
| `1D` | `3975.70` | 392,970.00 USD | 0.00 USD | 392,970.00 USD | 95,320.00 USD | 0.00 USD | 62,540.00 USD |
| `7D` | `3975.70` | 392,970.00 USD | 0.00 USD | 392,970.00 USD | 95,320.00 USD | 0.00 USD | 62,540.00 USD |
| `1D` | `3979.90` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `7D` | `3979.90` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `1D` | `3984.10` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `7D` | `3984.10` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `1D` | `3988.30` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3988.30` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4019.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4093.30` | 78,120.00 USD | 78,120.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `7D` | `4093.30` | 78,120.00 USD | 78,120.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `1D` | `4097.50` | 224,030.00 USD | 224,030.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 104,430.00 USD |
| `7D` | `4097.50` | 224,030.00 USD | 224,030.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 104,430.00 USD |
| `1D` | `4101.70` | 472,020.00 USD | 472,020.00 USD | 0.00 USD | 65,360.00 USD | 0.00 USD | 182,640.00 USD |
| `7D` | `4101.70` | 472,020.00 USD | 472,020.00 USD | 0.00 USD | 65,360.00 USD | 0.00 USD | 182,640.00 USD |
| `1D` | `4105.90` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 141,490.00 USD | 0.00 USD | 392,320.00 USD |
| `7D` | `4105.90` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 141,490.00 USD | 0.00 USD | 392,320.00 USD |
| `1D` | `4110.10` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 118,510.00 USD |
| `7D` | `4110.10` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 118,510.00 USD |
| `1D` | `4114.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 261,050.00 USD | 0.00 USD | 337,060.00 USD |
| `7D` | `4114.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 261,050.00 USD | 0.00 USD | 337,060.00 USD |
| `1D` | `4118.50` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 232,210.00 USD | 0.00 USD | 168,370.00 USD |
| `7D` | `4118.50` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 232,210.00 USD | 0.00 USD | 168,370.00 USD |
| `1D` | `4122.70` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 72,330.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4122.70` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 72,330.00 USD | 0.00 USD | 14,320.00 USD |
| `1D` | `4126.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4126.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `1D` | `4131.10` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 69,470.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4131.10` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 69,470.00 USD | 0.00 USD | 52,120.00 USD |
| `1D` | `4135.30` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 93,600.00 USD |
| `7D` | `4135.30` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 93,600.00 USD |
| `1D` | `4139.50` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 82,670.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4139.50` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 82,670.00 USD | 0.00 USD | 39,490.00 USD |
| `1D` | `4143.70` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4143.70` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `1D` | `4147.90` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4147.90` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4173.10` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 7,910.00 USD | 0.00 USD | 31,150.00 USD |
| `7D` | `4173.10` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 7,910.00 USD | 0.00 USD | 31,150.00 USD |
| `1D` | `4177.30` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 41,130.00 USD |
| `7D` | `4177.30` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 41,130.00 USD |
| `1D` | `4181.50` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD | 78,420.00 USD |
| `7D` | `4181.50` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD | 78,420.00 USD |
| `1D` | `4185.70` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 80,920.00 USD | 0.00 USD | 192,620.00 USD |
| `7D` | `4185.70` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 80,920.00 USD | 0.00 USD | 192,620.00 USD |
| `1D` | `4189.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 44,580.00 USD | 0.00 USD | 81,570.00 USD |
| `7D` | `4189.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 44,580.00 USD | 0.00 USD | 81,570.00 USD |
| `1D` | `4194.10` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 147,970.00 USD | 0.00 USD | 173,750.00 USD |
| `7D` | `4194.10` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 147,970.00 USD | 0.00 USD | 173,750.00 USD |
| `1D` | `4198.30` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 96,620.00 USD | 0.00 USD | 76,410.00 USD |
| `7D` | `4198.30` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 96,620.00 USD | 0.00 USD | 76,410.00 USD |
| `1D` | `4202.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 68,060.00 USD | 0.00 USD | 14,940.00 USD |
| `7D` | `4202.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 68,060.00 USD | 0.00 USD | 14,940.00 USD |
| `1D` | `4206.70` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 24,560.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4206.70` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 24,560.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `4210.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 35,690.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4210.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 35,690.00 USD | 0.00 USD | 25,640.00 USD |
| `1D` | `4215.10` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 41,760.00 USD |
| `7D` | `4215.10` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 41,760.00 USD |
| `1D` | `4219.30` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 47,660.00 USD | 0.00 USD | 31,270.00 USD |
| `7D` | `4219.30` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 47,660.00 USD | 0.00 USD | 31,270.00 USD |
| `1D` | `4223.50` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 18,880.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4223.50` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 18,880.00 USD | 0.00 USD | 29,460.00 USD |
| `1D` | `4227.70` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `7D` | `4227.70` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `1D` | `4231.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4231.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4412.50` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `4412.50` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `1D` | `4416.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 7,410.00 USD |
| `7D` | `4416.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `4420.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 12,930.00 USD |
| `7D` | `4420.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 12,930.00 USD |
| `1D` | `4425.10` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | 58,090.00 USD |
| `7D` | `4425.10` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | 58,090.00 USD |
| `1D` | `4426.80` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |
| `7D` | `4426.80` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `841.28M` | Total OI Tokens: `209,303.4 XAUT`
  * 1h OI Change: `-2.28%` | 4h OI Change: `-3.66%` | 24h OI Change: `+5.79%`
  * Exchange Breakdown: Binance=`62.47M` | Bybit=`144.64M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `147.58K` | Last 24h: `265.18K` | Last 3d: `925.43K` | Last 7d: `2.46M`
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
| `15M` | `XAUT` | `50.30%` | `49.70%` | `1.01` | 1,600,000.00 USD |
| `15M` | `Binance` | `49.74%` | `50.26%` | `0.99` | 528,370.00 USD |
| `15M` | `OKX` | `38.77%` | `61.23%` | `0.63` | 530,860.00 USD |
| `15M` | `Bybit` | `60.31%` | `39.69%` | `1.52` | 116,470.00 USD |
| `15M` | `KuCoin` | `49.48%` | `50.52%` | `0.98` | 29,200.00 USD |
| `15M` | `Gate` | `43.99%` | `56.01%` | `0.79` | 17,480.00 USD |
| `15M` | `Bitget` | `80.28%` | `19.72%` | `4.07` | 46,500.00 USD |
| `15M` | `BingX` | `68.75%` | `31.25%` | `2.20` | 66,390.00 USD |
| `15M` | `MEXC` | `58.62%` | `41.38%` | `1.42` | 61,470.00 USD |
| `15M` | `Bitunix` | `40.77%` | `59.23%` | `0.69` | 23,210.00 USD |
| `15M` | `Hyperliquid` | `59.28%` | `40.72%` | `1.46` | 13,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.09%` | `48.91%` | `1.04` | 74,770.00 USD |
| `15M` | `Crypto.com` | `0.1%` | `99.9%` | `0.00` | 985.49 USD |
| `15M` | `WhiteBIT` | `81.49%` | `18.51%` | `4.40` | 82,620.00 USD |
| `15M` | `HTX` | `95.32%` | `4.68%` | `20.37` | 110.34 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `8.63%` | `91.37%` | `0.09` | 3,780.00 USD |
| `15M` | `Aster` | `1.97%` | `98.03%` | `0.02` | 1,140.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.39%` | `61.61%` | `0.62` | 3,130.00 USD |
| `15M` | `Whale Positions` | `49.74%` | `50.26%` | `0.99` | 528,370.00 USD |
| `15M` | `Global Accounts` | `50.30%` | `49.70%` | `1.01` | 1,600,000.00 USD |
| `1H` | `XAUT` | `44.96%` | `55.04%` | `0.82` | 14,670,000.00 USD |
| `1H` | `Binance` | `41.03%` | `58.97%` | `0.70` | 4,920,000.00 USD |
| `1H` | `OKX` | `45.58%` | `54.42%` | `0.84` | 3,890,000.00 USD |
| `1H` | `Bybit` | `50.38%` | `49.62%` | `1.02` | 1,210,000.00 USD |
| `1H` | `KuCoin` | `51.58%` | `48.42%` | `1.07` | 140,730.00 USD |
| `1H` | `Gate` | `48.65%` | `51.35%` | `0.95` | 427,490.00 USD |
| `1H` | `Bitget` | `36.04%` | `63.96%` | `0.56` | 694,660.00 USD |
| `1H` | `BingX` | `59.74%` | `40.26%` | `1.48` | 455,840.00 USD |
| `1H` | `MEXC` | `34.03%` | `65.97%` | `0.52` | 1,310,000.00 USD |
| `1H` | `Bitunix` | `47.72%` | `52.28%` | `0.91` | 309,860.00 USD |
| `1H` | `Hyperliquid` | `43.61%` | `56.39%` | `0.77` | 372,160.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.84%` | `50.16%` | `0.99` | 451,750.00 USD |
| `1H` | `Crypto.com` | `46.57%` | `53.43%` | `0.87` | 7,980.00 USD |
| `1H` | `WhiteBIT` | `89.17%` | `10.83%` | `8.23` | 366,780.00 USD |
| `1H` | `HTX` | `57.47%` | `42.53%` | `1.35` | 5,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `74.95%` | `25.05%` | `2.99` | 81,580.00 USD |
| `1H` | `Aster` | `84.78%` | `15.22%` | `5.57` | 12,330.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `37.22%` | `62.78%` | `0.59` | 18,110.00 USD |
| `1H` | `Whale Positions` | `41.03%` | `58.97%` | `0.70` | 4,920,000.00 USD |
| `1H` | `Global Accounts` | `44.96%` | `55.04%` | `0.82` | 14,670,000.00 USD |
| `4H` | `XAUT` | `51.61%` | `48.39%` | `1.07` | 24,180,000.00 USD |
| `4H` | `Binance` | `50.85%` | `49.15%` | `1.03` | 8,500,000.00 USD |
| `4H` | `OKX` | `52.95%` | `47.05%` | `1.13` | 3,040,000.00 USD |
| `4H` | `Bybit` | `50.99%` | `49.01%` | `1.04` | 2,400,000.00 USD |
| `4H` | `KuCoin` | `30.31%` | `69.69%` | `0.43` | 116,560.00 USD |
| `4H` | `Gate` | `54.05%` | `45.95%` | `1.18` | 313,940.00 USD |
| `4H` | `Bitget` | `59.36%` | `40.64%` | `1.46` | 859,060.00 USD |
| `4H` | `BingX` | `38.69%` | `61.31%` | `0.63` | 2,020,000.00 USD |
| `4H` | `MEXC` | `49.81%` | `50.19%` | `0.99` | 1,530,000.00 USD |
| `4H` | `Bitunix` | `50.58%` | `49.42%` | `1.02` | 267,120.00 USD |
| `4H` | `Hyperliquid` | `82.03%` | `17.97%` | `4.56` | 328,990.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.44%` | `50.56%` | `0.98` | 4,120,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `100%` | `0.00` | 2.92 USD |
| `4H` | `WhiteBIT` | `96.03%` | `3.97%` | `24.19` | 620,590.00 USD |
| `4H` | `HTX` | `66.83%` | `33.17%` | `2.01` | 9,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.89%` | `60.11%` | `0.66` | 26,580.00 USD |
| `4H` | `Aster` | `2.6%` | `97.4%` | `0.03` | 8,870.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.7%` | `46.3%` | `1.16` | 25,880.00 USD |
| `4H` | `Whale Positions` | `50.85%` | `49.15%` | `1.03` | 8,500,000.00 USD |
| `4H` | `Global Accounts` | `51.61%` | `48.39%` | `1.07` | 24,180,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4038.45` | `4039.21` | `4038.45` | `4044.45` | `4033.95` | 27,240,137.17 USD | 11,767,150.02 USD | 15,472,987.15 USD | -3,705,837.13 USD | `-13.60%` | `1B / 8S` |
| `0:00 UTC` | `4031.85` | `4032.39` | `4031.85` | `4035.45` | `4029.75` | 19,957,078.91 USD | 8,693,953.80 USD | 11,263,125.11 USD | -2,569,171.31 USD | `-12.87%` | `0B / 1S` |
| `5:00 UTC` | `4030.35` | `4029.61` | `4030.35` | `4031.85` | `4027.35` | 28,806,935.84 USD | 12,003,806.54 USD | 16,803,129.30 USD | -4,799,322.75 USD | `-16.66%` | `0B / 1S` |
| `0:00 UTC` | `4032.75` | `4032.21` | `4032.75` | `4033.95` | `4030.35` | 24,251,255.66 USD | 11,335,444.57 USD | 12,915,811.09 USD | -1,580,366.52 USD | `-6.52%` | `0B / 2S` |
| `5:00 UTC` | `4028.85` | `4029.33` | `4028.85` | `4032.45` | `4026.75` | 27,633,720.84 USD | 14,667,923.52 USD | 12,965,797.32 USD | 1,702,126.19 USD | `+6.16%` | `3B / 0S` |
| `0:00 UTC` | `4022.85` | `4023.63` | `4022.85` | `4030.65` | `4017.75` | 50,953,409.81 USD | 20,150,897.83 USD | 30,802,511.97 USD | -10,651,614.14 USD | `-20.90%` | `3B / 16S` |
| `5:00 UTC` | `4023.45` | `4023.44` | `4023.45` | `4025.25` | `4021.65` | 20,710,982.12 USD | 10,208,497.33 USD | 10,502,484.80 USD | -293,987.47 USD | `-1.42%` | `0B / 0S` |
| `0:00 UTC` | `4020.15` | `4021.78` | `4020.15` | `4024.35` | `4019.55` | 13,323,426.37 USD | 6,724,680.36 USD | 6,598,746.01 USD | 125,934.34 USD | `+0.95%` | `2B / 0S` |
| `5:00 UTC` | `4024.95` | `4023.96` | `4024.95` | `4025.85` | `4021.05` | 10,712,179.92 USD | 5,438,050.75 USD | 5,274,129.18 USD | 163,921.57 USD | `+1.53%` | `0B / 1S` |
| `0:00 UTC` | `4029.15` | `4028.22` | `4029.15` | `4033.05` | `4024.65` | 20,514,732.34 USD | 13,525,757.60 USD | 6,988,974.74 USD | 6,536,782.86 USD | `+31.86%` | `8B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:04` | `Volume 5.0K XAU` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `4045.20` | 1,000.00 USD | 0.00 USD |
| `10-28 17:48` | `Volume 5.0K XAU` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `4068.50` | 2,200.00 USD | 0.00 USD |
| `10-28 16:57` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4052.80` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 10:56` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4041.20` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_EUR (XAUEUR.pi) Metal Auction: ROTA | `3633.06` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_GBP (XAUGBP.pi) Metal Auction: ROTA | `3040.99` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -39,730.00 USD | -39,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -11,970.00 USD | -34,240.00 USD | **`DISTRIBUTION`** |
| `30m` | -76,730.00 USD | -41,550.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,800.00 USD | -91,730.00 USD | **`DISTRIBUTION`** |
| `2h` | -93,250.00 USD | -121,380.00 USD | **`DISTRIBUTION`** |
| `4h` | -520,560.00 USD | 351,720.00 USD | **`DISTRIBUTION`** |
| `6h` | 280,770.00 USD | -152,100.00 USD | **`ACCUMULATION`** |
| `8h` | 952,450.00 USD | -199,140.00 USD | **`ACCUMULATION`** |
| `12h` | 1,850,000.00 USD | -706,700.00 USD | **`ACCUMULATION`** |
| `24h` | -577,680.00 USD | -47,130.00 USD | **`DISTRIBUTION`** |
| `1w` | -85,570,000.00 USD | -21,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -177,050,000.00 USD | -85,800,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-39.73K` | 15m=`-11.97K` | 1h=`-2.80K` | 24h=`-577.68K`
* Futures Capital Netflows: 5m=`-39.87K` | 15m=`-34.24K` | 1h=`-91.73K` | 24h=`-47.13K`
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
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4050.58` (Risk Distance: `9.87` pts)
  * +2.5R Take Profit: `4016.03`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4054.45`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
