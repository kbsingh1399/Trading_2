# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 22:52:02 IST` (`2026-10-29 17:22:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `56` | `0x5b5d...c060` | `SHORT` | 25,636,130.83 USD | `6,373.66` | `4191.43` | `4022.80` | `28452.07` | 1,078,670.35 USD | `+4.21%` | `4X Cross` |
| `58` | `0x4692...164f` | `SHORT` | 25,257,644.35 USD | `6,279.09` | `4135.05` | `4022.80` | `13265.21` | 706,769.63 USD | `+2.80%` | `5X Cross` |
| `78` | `0xb83d...6e36` | `SHORT` | 22,995,156.32 USD | `5,717.06` | `4234.49` | `4022.80` | `26731.74` | 1,213,718.91 USD | `+5.28%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,422,829.33 USD | `4,828.91` | `4157.43` | `4022.80` | `2052.74` | -653,052.98 USD | `-3.36%` | `25X Cross` |
| `150` | `0x645b...87b8` | `LONG` | 14,146,407.62 USD | `3,517.08` | `4129.71` | `4022.80` | `29.61` | -378,146.12 USD | `-2.67%` | `3X Cross` |
| `162` | `0x7a6d...f79c` | `SHORT` | 13,145,407.13 USD | `3,268.21` | `4228.94` | `4022.80` | `4406.34` | 675,672.00 USD | `+5.14%` | `25X Cross` |
| `185` | `0xa742...e390` | `SHORT` | 11,664,380.40 USD | `2,900.00` | `4364.92` | `4022.80` | `4235.56` | 993,895.93 USD | `+8.52%` | `20X Cross` |
| `279` | `0x41e5...0825` | `SHORT` | 8,848,840.00 USD | `2,200.00` | `4112.20` | `4022.80` | `4331.05` | 198,014.59 USD | `+2.24%` | `20X Cross` |
| `280` | `0x3678...b209` | `LONG` | 8,847,960.00 USD | `2,200.00` | `4176.09` | `4022.80` | `2401.54` | -339,459.30 USD | `-3.84%` | `25X Cross` |
| `317` | `0xfc66...ca06` | `SHORT` | 7,991,866.04 USD | `1,986.89` | `4032.86` | `4022.80` | `24728.70` | 21,000.13 USD | `+0.26%` | `3X Cross` |
| `318` | `0xacb6...efbd` | `SHORT` | 7,945,329.59 USD | `1,975.37` | `4048.55` | `4022.80` | `6482.59` | 52,062.12 USD | `+0.66%` | `6X Cross` |
| `387` | `0xc26c...b8f4` | `LONG` | 6,354,882.13 USD | `1,579.95` | `4075.62` | `4022.80` | `0.000000` | -84,414.84 USD | `-1.33%` | `1X Cross` |
| `433` | `0x12d2...f97f` | `LONG` | 5,638,894.33 USD | `1,401.94` | `4278.91` | `4022.80` | `2426.80` | -359,896.25 USD | `-6.38%` | `20X Cross` |
| `593` | `0x63da...8add` | `LONG` | 4,022,200.00 USD | `1,000.00` | `4021.46` | `4022.80` | `3564.00` | 739.04 USD | `+0.02%` | `25X Cross` |
| `613` | `0x9aa5...58af` | `LONG` | 3,908,138.45 USD | `971.64` | `4279.98` | `4022.80` | `0.000000` | -250,470.63 USD | `-6.41%` | `20X Cross` |
| `636` | `0xf3dc...1672` | `LONG` | 3,743,078.86 USD | `930.74` | `4024.62` | `4022.80` | `3337.48` | -2,813.70 USD | `-0.08%` | `20X Cross` |
| `688` | `0x354b...6425` | `LONG` | 3,431,509.47 USD | `853.08` | `4037.02` | `4022.80` | `0.000000` | -12,389.44 USD | `-0.36%` | `10X Cross` |
| `702` | `0x4a20...3c26` | `LONG` | 3,367,854.11 USD | `837.40` | `4599.73` | `4022.80` | `0.000000` | -483,966.27 USD | `-14.37%` | `20X Cross` |
| `857` | `0x0fac...7a0a` | `LONG` | 2,761,248.62 USD | `686.49` | `4290.34` | `4022.80` | `1227.89` | -184,010.09 USD | `-6.66%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,650,160.69 USD | `658.95` | `4175.35` | `4022.80` | `31154.13` | 101,186.37 USD | `+3.82%` | `4X Cross` |
| `935` | `0x625e...a354` | `SHORT` | 2,493,764.00 USD | `620.00` | `4122.81` | `4022.80` | `4342.14` | 62,383.03 USD | `+2.50%` | `20X Cross` |
| `962` | `0xeae3...e8ad` | `SHORT` | 2,413,140.00 USD | `600.00` | `4104.77` | `4022.80` | `4325.17` | 49,725.11 USD | `+2.06%` | `20X Cross` |
| `966` | `0xf285...fa82` | `LONG` | 2,405,701.55 USD | `598.11` | `4146.45` | `4022.80` | `3891.13` | -74,318.00 USD | `-3.09%` | `25X Cross` |
| `982` | `0x12f7...8750` | `LONG` | 2,355,443.36 USD | `585.61` | `4082.77` | `4022.80` | `2121.07` | -35,473.62 USD | `-1.51%` | `10X Cross` |
| `1136` | `0x413c...886c` | `LONG` | 2,010,800.00 USD | `500.00` | `4010.43` | `4022.80` | `0.000000` | 5,583.77 USD | `+0.28%` | `2X Cross` |
| `1144` | `0x61ce...a62b` | `SHORT` | 2,001,207.83 USD | `497.50` | `4071.66` | `4022.80` | `4684.06` | 24,460.96 USD | `+1.22%` | `20X Cross` |
| `1147` | `0x0593...40f9` | `LONG` | 1,995,772.75 USD | `496.18` | `4024.57` | `4022.80` | `3701.62` | -1,131.08 USD | `-0.06%` | `10X Isolated` |
| `1267` | `0xead5...69f2` | `LONG` | 1,825,209.60 USD | `453.78` | `4220.88` | `4022.80` | `3538.83` | -90,158.46 USD | `-4.94%` | `5X Isolated` |
| `1296` | `0x2edd...8179` | `LONG` | 1,782,462.84 USD | `442.60` | `4174.40` | `4027.30` | `0.000000` | -65,108.31 USD | `-3.65%` | `10X Cross` |
| `1328` | `0x7a6d...f79c` | `SHORT` | 1,725,210.75 USD | `428.38` | `4136.09` | `4027.30` | `5795.24` | 46,604.26 USD | `+2.70%` | `10X Cross` |
| `1395` | `0x46fc...1195` | `LONG` | 1,637,262.49 USD | `407.03` | `4055.53` | `4022.80` | `1895.67` | -13,447.70 USD | `-0.82%` | `20X Cross` |
| `1435` | `0x6d15...d374` | `LONG` | 1,608,880.00 USD | `400.00` | `4068.25` | `4022.80` | `3841.70` | -18,420.00 USD | `-1.14%` | `25X Cross` |
| `1436` | `0xee02...309d` | `SHORT` | 1,608,880.00 USD | `400.00` | `4438.84` | `4022.80` | `4226.78` | 166,658.60 USD | `+10.36%` | `25X Isolated` |
| `1467` | `0x02a7...fe9f` | `SHORT` | 1,568,658.00 USD | `390.00` | `4055.02` | `4022.80` | `4306.60` | 12,801.25 USD | `+0.82%` | `25X Cross` |
| `1503` | `0x7e77...b8d2` | `SHORT` | 1,528,322.00 USD | `380.00` | `4131.92` | `4022.80` | `4293.41` | 41,807.64 USD | `+2.74%` | `20X Cross` |
| `1509` | `0x51f6...2b39` | `LONG` | 1,524,759.94 USD | `378.61` | `4235.75` | `4027.30` | `0.000000` | -78,919.28 USD | `-5.18%` | `10X Cross` |
| `1521` | `0x72c2...9b37` | `LONG` | 1,500,584.84 USD | `373.13` | `4000.98` | `4022.80` | `3777.93` | 7,691.32 USD | `+0.51%` | `13X Isolated` |
| `1568` | `0xaa44...b844` | `LONG` | 1,447,776.00 USD | `360.00` | `4043.10` | `4022.80` | `2820.88` | -7,741.63 USD | `-0.53%` | `9X Cross` |
| `1570` | `0x781e...96b7` | `SHORT` | 1,445,406.02 USD | `358.90` | `4365.65` | `4027.30` | `12173.88` | 121,435.98 USD | `+8.40%` | `10X Cross` |
| `1680` | `0xa41f...d50a` | `LONG` | 1,323,151.36 USD | `328.96` | `4468.89` | `4022.80` | `3833.08` | -146,946.49 USD | `-11.11%` | `15X Cross` |
| `1709` | `0x49e9...e1d0` | `SHORT` | 1,301,412.17 USD | `323.56` | `4025.23` | `4022.80` | `29785.31` | 980.53 USD | `+0.08%` | `4X Cross` |
| `1728` | `0xada6...6f88` | `LONG` | 1,283,998.75 USD | `319.28` | `4166.46` | `4022.80` | `1850.66` | -46,251.76 USD | `-3.60%` | `5X Cross` |
| `1734` | `0xbf5a...88ba` | `SHORT` | 1,277,671.54 USD | `317.65` | `4091.80` | `4022.80` | `10535.69` | 22,111.49 USD | `+1.73%` | `20X Cross` |
| `1753` | `0xff31...ff6c` | `SHORT` | 1,246,758.00 USD | `310.00` | `4372.43` | `4022.80` | `4789.07` | 108,697.38 USD | `+8.72%` | `10X Isolated` |
| `1933` | `0x50e2...d770` | `LONG` | 1,087,363.61 USD | `270.37` | `4243.58` | `4022.80` | `2561.99` | -59,962.85 USD | `-5.51%` | `20X Cross` |
| `1955` | `0x4c92...4f17` | `SHORT` | 1,072,803.20 USD | `266.72` | `4260.98` | `4022.80` | `6533.46` | 63,689.04 USD | `+5.94%` | `20X Cross` |
| `2014` | `0xd346...c4f3` | `LONG` | 1,026,360.06 USD | `255.17` | `4188.66` | `4022.80` | `3310.31` | -42,476.45 USD | `-4.14%` | `5X Isolated` |
| `2051` | `0x1581...463b` | `LONG` | 1,005,550.00 USD | `250.00` | `4003.77` | `4022.80` | `3504.53` | 4,606.41 USD | `+0.46%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4111.52` (Vol: 316,800.00 USD, Dist: `+2.10%`) | Long MP=`3951.52` (Vol: 223,500.00 USD, Dist: `--1.87%`)
  * 48H Horizon: Short MP=`4111.52` (Vol: 316,800.00 USD, Dist: `+2.10%`) | Long MP=`3957.44` (Vol: 226,700.00 USD, Dist: `--1.72%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.05%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--1.18%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.25%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.81%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3616.10` | 16,280,000.00 USD | 16,280,000.00 USD | 94,440.00 USD | 0.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3617.20` | 4,110,000.00 USD | 4,110,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3620.30` | 16,180,000.00 USD | 16,180,000.00 USD | 52,580.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.40` | 4,100,000.00 USD | 4,100,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.50` | 16,110,000.00 USD | 16,110,000.00 USD | 95,620.00 USD | 0.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.60` | 4,070,000.00 USD | 4,070,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.70` | 15,990,000.00 USD | 15,990,000.00 USD | 223,360.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.80` | 4,020,000.00 USD | 4,020,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.90` | 15,760,000.00 USD | 15,760,000.00 USD | 90,370.00 USD | 0.00 USD | 16,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.00` | 3,970,000.00 USD | 3,970,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.10` | 15,650,000.00 USD | 15,650,000.00 USD | 93,360.00 USD | 0.00 USD | 15,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.20` | 3,940,000.00 USD | 3,940,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,540,000.00 USD | 15,540,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3642.40` | 3,870,000.00 USD | 3,870,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.50` | 15,480,000.00 USD | 15,480,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3646.60` | 3,850,000.00 USD | 3,850,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.70` | 15,450,000.00 USD | 15,450,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.80` | 3,830,000.00 USD | 3,830,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.90` | 15,430,000.00 USD | 15,430,000.00 USD | 58,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.00` | 3,790,000.00 USD | 3,790,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.10` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3659.20` | 3,770,000.00 USD | 3,770,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.30` | 15,360,000.00 USD | 15,360,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3663.40` | 3,760,000.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.50` | 15,340,000.00 USD | 15,340,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.80` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.30` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.50` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.70` | 15,330,000.00 USD | 15,330,000.00 USD | 388,830.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.90` | 14,920,000.00 USD | 14,920,000.00 USD | 446,290.00 USD | 0.00 USD | 60,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.10` | 14,410,000.00 USD | 14,410,000.00 USD | 482,900.00 USD | 0.00 USD | 75,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.30` | 13,860,000.00 USD | 13,860,000.00 USD | 256,520.00 USD | 0.00 USD | 54,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.50` | 13,550,000.00 USD | 13,550,000.00 USD | 221,780.00 USD | 0.00 USD | 23,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.70` | 13,300,000.00 USD | 13,300,000.00 USD | 159,510.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.80` | 3,750,000.00 USD | 3,750,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.90` | 13,120,000.00 USD | 13,120,000.00 USD | 260,240.00 USD | 0.00 USD | 43,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.00` | 3,690,000.00 USD | 3,690,000.00 USD | 138,500.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.10` | 12,820,000.00 USD | 12,820,000.00 USD | 599,530.00 USD | 0.00 USD | 46,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.20` | 3,530,000.00 USD | 3,530,000.00 USD | 127,010.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.30` | 12,170,000.00 USD | 12,170,000.00 USD | 412,260.00 USD | 0.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.40` | 3,390,000.00 USD | 3,390,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3876.50` | 11,710,000.00 USD | 11,710,000.00 USD | 442,350.00 USD | 0.00 USD | 68,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.60` | 3,260,000.00 USD | 3,260,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.70` | 11,200,000.00 USD | 11,200,000.00 USD | 277,230.00 USD | 0.00 USD | 37,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.80` | 3,070,000.00 USD | 3,070,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.90` | 10,880,000.00 USD | 10,880,000.00 USD | 101,210.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3886.00` | 2,920,000.00 USD | 2,920,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3889.10` | 10,750,000.00 USD | 10,750,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3890.20` | 2,830,000.00 USD | 2,830,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3893.30` | 10,640,000.00 USD | 10,640,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3894.40` | 2,760,000.00 USD | 2,760,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.50` | 10,520,000.00 USD | 10,520,000.00 USD | 176,440.00 USD | 0.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.60` | 2,660,000.00 USD | 2,660,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.70` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.80` | 2,600,000.00 USD | 2,600,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.90` | 10,330,000.00 USD | 10,330,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.00` | 2,540,000.00 USD | 2,540,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.10` | 10,240,000.00 USD | 10,240,000.00 USD | 23,110.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.40` | 2,510,000.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.50` | 10,210,000.00 USD | 10,210,000.00 USD | 770,170.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.70` | 9,410,000.00 USD | 9,410,000.00 USD | 857,100.00 USD | 0.00 USD | 116,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.90` | 8,430,000.00 USD | 8,430,000.00 USD | 992,370.00 USD | 0.00 USD | 140,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.10` | 7,300,000.00 USD | 7,300,000.00 USD | 455,760.00 USD | 0.00 USD | 122,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.30` | 6,720,000.00 USD | 6,720,000.00 USD | 368,490.00 USD | 0.00 USD | 38,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3939.50` | 6,310,000.00 USD | 6,310,000.00 USD | 456,560.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.60` | 2,500,000.00 USD | 2,500,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.70` | 5,830,000.00 USD | 5,830,000.00 USD | 435,580.00 USD | 0.00 USD | 92,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.80` | 2,400,000.00 USD | 2,400,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.90` | 5,310,000.00 USD | 5,310,000.00 USD | 1,030,000.00 USD | 0.00 USD | 99,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.00` | 2,080,000.00 USD | 2,080,000.00 USD | 193,440.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3952.10` | 4,180,000.00 USD | 4,180,000.00 USD | 855,100.00 USD | 0.00 USD | 91,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.20` | 1,840,000.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3956.30` | 3,230,000.00 USD | 3,230,000.00 USD | 1,010,000.00 USD | 0.00 USD | 120,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.40` | 1,550,000.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3960.50` | 2,100,000.00 USD | 2,100,000.00 USD | 521,420.00 USD | 0.00 USD | 71,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.60` | 1,310,000.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.70` | 1,510,000.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.80` | 863,010.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.90` | 1,090,000.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3970.00` | 714,020.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3973.10` | 874,480.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3974.20` | 591,750.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3977.30` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3978.40` | 386,370.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.50` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3982.60` | 253,490.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.70` | 219,990.00 USD | 219,990.00 USD | 59,830.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.80` | 119,030.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.90` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3991.00` | 51,990.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3994.10` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3995.20` | 20,280.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3999.40` | 15,300.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.90` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4078.10` | 733,530.00 USD | 733,530.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.30` | 1,710,000.00 USD | 1,710,000.00 USD | 874,830.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.50` | 2,630,000.00 USD | 2,630,000.00 USD | 784,820.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.70` | 3,440,000.00 USD | 3,440,000.00 USD | 674,970.00 USD | 0.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 3,800,000.00 USD | 3,800,000.00 USD | 320,740.00 USD | 0.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.10` | 4,250,000.00 USD | 4,250,000.00 USD | 422,750.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.30` | 4,710,000.00 USD | 4,710,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.50` | 5,520,000.00 USD | 5,520,000.00 USD | 676,110.00 USD | 0.00 USD | 135,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.60` | 554,190.00 USD | 554,190.00 USD | 286,640.00 USD | 0.00 USD | 45,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.70` | 6,650,000.00 USD | 6,650,000.00 USD | 1,060,000.00 USD | 0.00 USD | 69,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.80` | 818,050.00 USD | 818,050.00 USD | 220,390.00 USD | 0.00 USD | 43,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.90` | 7,460,000.00 USD | 7,460,000.00 USD | 728,730.00 USD | 0.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.00` | 1,050,000.00 USD | 1,050,000.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.10` | 8,600,000.00 USD | 8,600,000.00 USD | 1,000,000.00 USD | 0.00 USD | 140,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.20` | 1,440,000.00 USD | 1,440,000.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4124.30` | 8,920,000.00 USD | 8,920,000.00 USD | 246,290.00 USD | 0.00 USD | 66,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.40` | 1,710,000.00 USD | 1,710,000.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4128.50` | 9,210,000.00 USD | 9,210,000.00 USD | 249,290.00 USD | 0.00 USD | 49,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.60` | 1,840,000.00 USD | 1,840,000.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.70` | 9,430,000.00 USD | 9,430,000.00 USD | 170,870.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.80` | 1,980,000.00 USD | 1,980,000.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.90` | 9,680,000.00 USD | 9,680,000.00 USD | 225,430.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.00` | 2,180,000.00 USD | 2,180,000.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4141.10` | 9,980,000.00 USD | 9,980,000.00 USD | 293,010.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4142.20` | 2,290,000.00 USD | 2,290,000.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4145.30` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.40` | 2,420,000.00 USD | 2,420,000.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4149.50` | 10,110,000.00 USD | 10,110,000.00 USD | 73,610.00 USD | 0.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.60` | 2,480,000.00 USD | 2,480,000.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.70` | 10,190,000.00 USD | 10,190,000.00 USD | 73,770.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.90` | 10,590,000.00 USD | 10,590,000.00 USD | 381,150.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4162.10` | 11,050,000.00 USD | 11,050,000.00 USD | 424,360.00 USD | 0.00 USD | 42,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.20` | 2,500,000.00 USD | 2,500,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4166.30` | 11,460,000.00 USD | 11,460,000.00 USD | 338,350.00 USD | 0.00 USD | 68,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.50` | 11,890,000.00 USD | 11,890,000.00 USD | 352,860.00 USD | 0.00 USD | 73,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.70` | 12,120,000.00 USD | 12,120,000.00 USD | 212,100.00 USD | 0.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.90` | 12,320,000.00 USD | 12,320,000.00 USD | 190,420.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.00` | 2,520,000.00 USD | 2,520,000.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,500,000.00 USD | 12,500,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,600,000.00 USD | 2,600,000.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.30` | 12,880,000.00 USD | 12,880,000.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.40` | 2,730,000.00 USD | 2,730,000.00 USD | 112,780.00 USD | 0.00 USD | 18,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.50` | 13,520,000.00 USD | 13,520,000.00 USD | 598,770.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.60` | 2,900,000.00 USD | 2,900,000.00 USD | 151,790.00 USD | 0.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.70` | 13,870,000.00 USD | 13,870,000.00 USD | 304,490.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.80` | 3,000,000.00 USD | 3,000,000.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.90` | 14,420,000.00 USD | 14,420,000.00 USD | 494,670.00 USD | 0.00 USD | 62,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.00` | 3,180,000.00 USD | 3,180,000.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.10` | 14,670,000.00 USD | 14,670,000.00 USD | 208,930.00 USD | 0.00 USD | 37,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.20` | 3,330,000.00 USD | 3,330,000.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.30` | 14,800,000.00 USD | 14,800,000.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.40` | 3,420,000.00 USD | 3,420,000.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.50` | 14,890,000.00 USD | 14,890,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.60` | 3,450,000.00 USD | 3,450,000.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.70` | 15,010,000.00 USD | 15,010,000.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.80` | 3,580,000.00 USD | 3,580,000.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.90` | 15,140,000.00 USD | 15,140,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4222.00` | 3,620,000.00 USD | 3,620,000.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.10` | 15,220,000.00 USD | 15,220,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4226.20` | 3,690,000.00 USD | 3,690,000.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.30` | 15,260,000.00 USD | 15,260,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4230.40` | 3,720,000.00 USD | 3,720,000.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4233.50` | 15,310,000.00 USD | 15,310,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4234.60` | 3,740,000.00 USD | 3,740,000.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.70` | 15,330,000.00 USD | 15,330,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4243.00` | 3,750,000.00 USD | 3,750,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.10` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.30` | 15,460,000.00 USD | 15,460,000.00 USD | 123,180.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.50` | 15,590,000.00 USD | 15,590,000.00 USD | 120,190.00 USD | 0.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.70` | 15,700,000.00 USD | 15,700,000.00 USD | 87,670.00 USD | 0.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.90` | 15,850,000.00 USD | 15,850,000.00 USD | 134,060.00 USD | 0.00 USD | 22,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.10` | 15,890,000.00 USD | 15,890,000.00 USD | 22,000.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4418.30` | 15,980,000.00 USD | 15,980,000.00 USD | 84,830.00 USD | 0.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4422.50` | 16,020,000.00 USD | 16,020,000.00 USD | 31,340.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4423.60` | 3,770,000.00 USD | 3,770,000.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.70` | 16,090,000.00 USD | 16,090,000.00 USD | 63,140.00 USD | 0.00 USD | 13,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.80` | 3,820,000.00 USD | 3,820,000.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.90` | 16,230,000.00 USD | 16,230,000.00 USD | 118,300.00 USD | 0.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.00` | 3,840,000.00 USD | 3,840,000.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4434.30` | 3,870,000.00 USD | 3,870,000.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4435.10` | 16,410,000.00 USD | 16,410,000.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4439.30` | 16,480,000.00 USD | 16,480,000.00 USD | 58,000.00 USD | 0.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4443.50` | 16,610,000.00 USD | 16,610,000.00 USD | 115,690.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4447.70` | 16,640,000.00 USD | 16,640,000.00 USD | 22,690.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |

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
| `7D` | `3616.10` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 94,440.00 USD | 0.00 USD | 4,740.00 USD |
| `1D` | `3617.20` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD |
| `7D` | `3620.30` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 52,580.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3621.40` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `3624.50` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 95,620.00 USD | 0.00 USD | 23,890.00 USD |
| `1D` | `3625.60` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD |
| `7D` | `3628.70` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 223,360.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3629.80` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `3632.90` | 15,760,000.00 USD | 0.00 USD | 15,760,000.00 USD | 90,370.00 USD | 0.00 USD | 16,790.00 USD |
| `1D` | `3634.00` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD |
| `7D` | `3637.10` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 93,360.00 USD | 0.00 USD | 15,010.00 USD |
| `1D` | `3638.20` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `3641.30` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3642.40` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `3645.50` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3646.60` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD |
| `7D` | `3649.70` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.80` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `3653.90` | 15,430,000.00 USD | 0.00 USD | 15,430,000.00 USD | 58,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.00` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `3658.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `3659.20` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD |
| `7D` | `3662.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3663.40` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3666.50` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.30` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3834.50` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.70` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 388,830.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3842.90` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 446,290.00 USD | 0.00 USD | 60,030.00 USD |
| `7D` | `3847.10` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 482,900.00 USD | 0.00 USD | 75,710.00 USD |
| `7D` | `3851.30` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 256,520.00 USD | 0.00 USD | 54,050.00 USD |
| `7D` | `3855.50` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 221,780.00 USD | 0.00 USD | 23,450.00 USD |
| `7D` | `3859.70` | 13,300,000.00 USD | 0.00 USD | 13,300,000.00 USD | 159,510.00 USD | 0.00 USD | 18,270.00 USD |
| `1D` | `3860.80` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD |
| `7D` | `3863.90` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 260,240.00 USD | 0.00 USD | 43,190.00 USD |
| `1D` | `3865.00` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 138,500.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `3868.10` | 12,820,000.00 USD | 0.00 USD | 12,820,000.00 USD | 599,530.00 USD | 0.00 USD | 46,420.00 USD |
| `1D` | `3869.20` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 127,010.00 USD | 0.00 USD | 21,160.00 USD |
| `7D` | `3872.30` | 12,170,000.00 USD | 0.00 USD | 12,170,000.00 USD | 412,260.00 USD | 0.00 USD | 53,490.00 USD |
| `1D` | `3873.40` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD |
| `7D` | `3876.50` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 442,350.00 USD | 0.00 USD | 68,150.00 USD |
| `1D` | `3877.60` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `3880.70` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 277,230.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `3881.80` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD |
| `7D` | `3884.90` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 101,210.00 USD | 0.00 USD | 32,380.00 USD |
| `1D` | `3886.00` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD |
| `7D` | `3889.10` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3890.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD |
| `7D` | `3893.30` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3894.40` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3897.50` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 176,440.00 USD | 0.00 USD | 5,460.00 USD |
| `1D` | `3898.60` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3901.70` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD |
| `1D` | `3902.80` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD |
| `7D` | `3905.90` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD |
| `1D` | `3907.00` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3910.10` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 23,110.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `1D` | `3915.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3918.50` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 770,170.00 USD | 0.00 USD | 35,850.00 USD |
| `7D` | `3922.70` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 857,100.00 USD | 0.00 USD | 116,530.00 USD |
| `7D` | `3926.90` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 992,370.00 USD | 0.00 USD | 140,450.00 USD |
| `7D` | `3931.10` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 455,760.00 USD | 0.00 USD | 122,590.00 USD |
| `7D` | `3935.30` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 368,490.00 USD | 0.00 USD | 38,330.00 USD |
| `7D` | `3939.50` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 456,560.00 USD | 0.00 USD | 23,520.00 USD |
| `1D` | `3940.60` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD |
| `7D` | `3943.70` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 435,580.00 USD | 0.00 USD | 92,010.00 USD |
| `1D` | `3944.80` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD |
| `7D` | `3947.90` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 1,030,000.00 USD | 0.00 USD | 99,970.00 USD |
| `1D` | `3949.00` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 193,440.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `3952.10` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 855,100.00 USD | 0.00 USD | 91,100.00 USD |
| `1D` | `3953.20` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD |
| `7D` | `3956.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 1,010,000.00 USD | 0.00 USD | 120,760.00 USD |
| `1D` | `3957.40` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD |
| `7D` | `3960.50` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 521,420.00 USD | 0.00 USD | 71,810.00 USD |
| `1D` | `3961.60` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD |
| `7D` | `3964.70` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD |
| `1D` | `3965.80` | 863,010.00 USD | 0.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD |
| `7D` | `3968.90` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `1D` | `3970.00` | 714,020.00 USD | 0.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD |
| `7D` | `3973.10` | 874,480.00 USD | 0.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3974.20` | 591,750.00 USD | 0.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3977.30` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3978.40` | 386,370.00 USD | 0.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD |
| `7D` | `3981.50` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `3982.60` | 253,490.00 USD | 0.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD |
| `7D` | `3985.70` | 219,990.00 USD | 0.00 USD | 219,990.00 USD | 59,830.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `3986.80` | 119,030.00 USD | 0.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3989.90` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3991.00` | 51,990.00 USD | 0.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3994.10` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3995.20` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `3999.40` | 15,300.00 USD | 0.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4027.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4027.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.90` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4078.10` | 733,530.00 USD | 733,530.00 USD | 0.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4082.30` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 874,830.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `4086.50` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 784,820.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `4090.70` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 674,970.00 USD | 0.00 USD | 137,740.00 USD |
| `7D` | `4094.90` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 320,740.00 USD | 0.00 USD | 40,420.00 USD |
| `7D` | `4099.10` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 422,750.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 0.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `4103.30` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 0.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD |
| `7D` | `4107.50` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 676,110.00 USD | 0.00 USD | 135,680.00 USD |
| `1D` | `4108.60` | 554,190.00 USD | 554,190.00 USD | 0.00 USD | 286,640.00 USD | 0.00 USD | 45,070.00 USD |
| `7D` | `4111.70` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 69,590.00 USD |
| `1D` | `4112.80` | 818,050.00 USD | 818,050.00 USD | 0.00 USD | 220,390.00 USD | 0.00 USD | 43,470.00 USD |
| `7D` | `4115.90` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 728,730.00 USD | 0.00 USD | 77,320.00 USD |
| `1D` | `4117.00` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD |
| `7D` | `4120.10` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 1,000,000.00 USD | 0.00 USD | 140,330.00 USD |
| `1D` | `4121.20` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD |
| `7D` | `4124.30` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 246,290.00 USD | 0.00 USD | 66,200.00 USD |
| `1D` | `4125.40` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD |
| `7D` | `4128.50` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 249,290.00 USD | 0.00 USD | 49,090.00 USD |
| `1D` | `4129.60` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4132.70` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 170,870.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD |
| `7D` | `4136.90` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 225,430.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4138.00` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4141.10` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 293,010.00 USD | 0.00 USD | 10,910.00 USD |
| `1D` | `4142.20` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4145.30` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `1D` | `4146.40` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD |
| `7D` | `4149.50` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 28,900.00 USD |
| `1D` | `4150.60` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.70` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `4157.90` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 381,150.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4159.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4162.10` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 424,360.00 USD | 0.00 USD | 42,940.00 USD |
| `1D` | `4163.20` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4166.30` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 338,350.00 USD | 0.00 USD | 68,260.00 USD |
| `7D` | `4170.50` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 352,860.00 USD | 0.00 USD | 73,620.00 USD |
| `7D` | `4174.70` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 20,210.00 USD |
| `7D` | `4178.90` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 190,420.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4180.00` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD |
| `7D` | `4183.10` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4184.20` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `4187.30` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD |
| `1D` | `4188.40` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 112,780.00 USD | 0.00 USD | 18,900.00 USD |
| `7D` | `4191.50` | 13,520,000.00 USD | 13,520,000.00 USD | 0.00 USD | 598,770.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4192.60` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 151,790.00 USD | 0.00 USD | 19,500.00 USD |
| `7D` | `4195.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 304,490.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4196.80` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD |
| `7D` | `4199.90` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 494,670.00 USD | 0.00 USD | 62,750.00 USD |
| `1D` | `4201.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD |
| `7D` | `4204.10` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4205.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD |
| `7D` | `4208.30` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `1D` | `4209.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD |
| `7D` | `4212.50` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4213.60` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD |
| `7D` | `4216.70` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `1D` | `4217.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD |
| `7D` | `4220.90` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `4222.00` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD |
| `7D` | `4225.10` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `4226.20` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD |
| `7D` | `4229.30` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `1D` | `4230.40` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `4233.50` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `1D` | `4234.60` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD |
| `7D` | `4237.70` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4243.00` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4393.10` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4397.30` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 123,180.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4401.50` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 120,190.00 USD | 0.00 USD | 11,600.00 USD |
| `7D` | `4405.70` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 87,670.00 USD | 0.00 USD | 16,730.00 USD |
| `7D` | `4409.90` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 134,060.00 USD | 0.00 USD | 22,490.00 USD |
| `7D` | `4414.10` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 22,000.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `4418.30` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 84,830.00 USD | 0.00 USD | 4,740.00 USD |
| `7D` | `4422.50` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 31,340.00 USD | 0.00 USD | 5,700.00 USD |
| `1D` | `4423.60` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `4426.70` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 63,140.00 USD | 0.00 USD | 13,840.00 USD |
| `1D` | `4427.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD |
| `7D` | `4430.90` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 118,300.00 USD | 0.00 USD | 14,520.00 USD |
| `1D` | `4432.00` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `4434.30` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD |
| `7D` | `4435.10` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD |
| `7D` | `4439.30` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 58,000.00 USD | 0.00 USD | 9,370.00 USD |
| `7D` | `4443.50` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 115,690.00 USD | 0.00 USD | 22,430.00 USD |
| `7D` | `4447.70` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 7,320.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.55M` | Total OI Tokens: `68,415.2 PAXG`
  * 1h OI Change: `+0.34%` | 4h OI Change: `-0.10%` | 24h OI Change: `+0.68%`
  * Exchange Breakdown: Binance=`106.93M` | Bybit=`20.02M` | OKX=`-` | Hyperliquid=`25.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.78K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `38.95%` | `61.05%` | `0.64` | 3,080,000.00 USD |
| `15M` | `Binance` | `34.18%` | `65.82%` | `0.52` | 1,190,000.00 USD |
| `15M` | `OKX` | `38.95%` | `61.05%` | `0.64` | 734,170.00 USD |
| `15M` | `Bybit` | `25.05%` | `74.95%` | `0.33` | 230,250.00 USD |
| `15M` | `KuCoin` | `47.66%` | `52.34%` | `0.91` | 34,430.00 USD |
| `15M` | `Gate` | `42.95%` | `57.05%` | `0.75` | 46,940.00 USD |
| `15M` | `Bitget` | `54.62%` | `45.38%` | `1.20` | 94,830.00 USD |
| `15M` | `BingX` | `29.62%` | `70.38%` | `0.42` | 84,110.00 USD |
| `15M` | `MEXC` | `33.69%` | `66.31%` | `0.51` | 248,940.00 USD |
| `15M` | `Bitunix` | `35.8%` | `64.2%` | `0.56` | 40,090.00 USD |
| `15M` | `Hyperliquid` | `87.5%` | `12.5%` | `7.00` | 77,510.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.16%` | `49.84%` | `1.01` | 210,120.00 USD |
| `15M` | `Crypto.com` | `42.66%` | `57.34%` | `0.74` | 1,720.00 USD |
| `15M` | `WhiteBIT` | `81.08%` | `18.92%` | `4.29` | 79,160.00 USD |
| `15M` | `HTX` | `20.77%` | `79.23%` | `0.26` | 261.95 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `4.49%` | `95.51%` | `0.05` | 8,210.00 USD |
| `15M` | `Aster` | `1%` | `99%` | `0.01` | 1,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `35.21%` | `64.79%` | `0.54` | 3,420.00 USD |
| `15M` | `Whale Positions` | `34.18%` | `65.82%` | `0.52` | 1,190,000.00 USD |
| `15M` | `Global Accounts` | `38.95%` | `61.05%` | `0.64` | 3,080,000.00 USD |
| `1H` | `PAXG` | `57.89%` | `42.11%` | `1.37` | 13,120,000.00 USD |
| `1H` | `Binance` | `64.06%` | `35.94%` | `1.78` | 1,040,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `44.14%` | `55.86%` | `0.79` | 1,060,000.00 USD |
| `1H` | `KuCoin` | `45.5%` | `54.5%` | `0.83` | 52,610.00 USD |
| `1H` | `Gate` | `51.76%` | `48.24%` | `1.07` | 399,570.00 USD |
| `1H` | `Bitget` | `53.37%` | `46.63%` | `1.14` | 475,130.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `64.12%` | `35.88%` | `1.79` | 8,430,000.00 USD |
| `1H` | `Bitunix` | `65.09%` | `34.91%` | `1.86` | 339,630.00 USD |
| `1H` | `Hyperliquid` | `47.37%` | `52.63%` | `0.90` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 987,330.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `41.71%` | `58.29%` | `0.72` | 334,350.00 USD |
| `1H` | `HTX` | `40.44%` | `59.56%` | `0.68` | 3,190.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `95.63%` | `4.37%` | `21.88` | 17,900.00 USD |
| `1H` | `Aster` | `84.96%` | `15.04%` | `5.65` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `15.51%` | `84.49%` | `0.18` | 0.00 USD |
| `1H` | `Whale Positions` | `64.06%` | `35.94%` | `1.78` | 1,040,000.00 USD |
| `1H` | `Global Accounts` | `57.89%` | `42.11%` | `1.37` | 13,120,000.00 USD |
| `4H` | `PAXG` | `48.96%` | `51.04%` | `0.96` | 102,740,000.00 USD |
| `4H` | `Binance` | `52.07%` | `47.93%` | `1.09` | 7,010,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `50.61%` | `49.39%` | `1.02` | 6,400,000.00 USD |
| `4H` | `KuCoin` | `51.95%` | `48.05%` | `1.08` | 465,770.00 USD |
| `4H` | `Gate` | `45.92%` | `54.08%` | `0.85` | 2,150,000.00 USD |
| `4H` | `Bitget` | `48.51%` | `51.49%` | `0.94` | 4,040,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `49.54%` | `50.46%` | `0.98` | 67,600,000.00 USD |
| `4H` | `Bitunix` | `51.37%` | `48.63%` | `1.06` | 3,880,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.18%` | `43.82%` | `1.28` | 7,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.8%` | `95.2%` | `0.05` | 3,040,000.00 USD |
| `4H` | `HTX` | `92.14%` | `7.86%` | `11.72` | 63,040.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.76%` | `53.24%` | `0.88` | 147,800.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `52.07%` | `47.93%` | `1.09` | 7,010,000.00 USD |
| `4H` | `Global Accounts` | `48.96%` | `51.04%` | `0.96` | 102,740,000.00 USD |


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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
