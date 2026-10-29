# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 01:23:52 IST` (`2026-10-29 19:53:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4020.28` | **Live Ask Quote**: `4020.36` | **Mid Price**: `4020.32`
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
  * Session VWAP: `4029.81` | VWAP Z-Score: `-0.95` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.92` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.51` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4065.60` | Lower -3.00σ Band: `3994.01`
  * Upper +2.51σ Band: `4059.76` | Lower -2.51σ Band: `3999.86`
  * Upper +2.01σ Band: `4053.79` | Lower -2.01σ Band: `4005.82`
  * Upper +2.00σ Band: `4053.67` | Lower -2.00σ Band: `4005.94`
  * Upper +1.28σ Band: `4045.08` | Lower -1.28σ Band: `4014.53`
  * Upper +1.00σ Band: `4041.74` | Lower -1.00σ Band: `4017.87`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4014.11` | EMA-20=`4016.39` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4022.96` (Slope: `+0.0000`) | EMA-100=`4029.77`
  * Institutional Anchors: EMA-144=`4031.53` | EMA-200=`4031.64` (Slope: `-0.0572`) | EMA-233=`4030.82`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.53` (Distance: `-0.50%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.18%`)
  * Value Area Low (VAL) = `4016.67` (Distance: `+0.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.72` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4004.24` - `4036.40`
  * Optimal Trade Entry (OTE 0.705): `4028.36`
  * Structural Invalidation Anchor (0.786): `4052.48`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4020.84` | `4021.99` | `4019.80` | `4020.77` | `29` | 114,678.87 USD | 20,363.17 USD | `+17.76%` | 1,273,901.56 USD | `-0.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4020.77` | `4023.61` | `4020.76` | `4022.61` | `80` | 320,566.79 USD | -183,285.47 USD | `-57.18%` | 1,090,616.09 USD | `-1.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4022.82` | `4023.32` | `4022.19` | `4022.50` | `8` | 31,370.47 USD | 313.02 USD | `+1.00%` | 1,090,929.12 USD | `-0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4017.56` | `4018.64` | `4014.71` | `4015.27` | `224` | 899,445.34 USD | -718,002.67 USD | `-79.83%` | 1,091,901.63 USD | `-2.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4015.26` | `4021.41` | `4014.71` | `4020.84` | `71` | 284,291.04 USD | 161,636.76 USD | `+56.86%` | 1,253,538.39 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4020.84` | `4023.61` | `4019.80` | `4022.50` | `116` | 466,616.13 USD | -162,609.28 USD | `-34.85%` | 1,090,929.12 USD | `-0.65` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 1,017,172.68 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4017.97` | `4011.01` | `4017.56` | `511` | 2,050,996.96 USD | 1,105,382.66 USD | `+53.89%` | 2,122,555.33 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4017.56` | `4023.61` | `4014.71` | `4022.50` | `411` | 1,650,352.51 USD | -718,975.19 USD | `-43.56%` | 1,403,580.15 USD | `-1.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4022.50` | `2,421` | 9,731,392.61 USD | 1,026,529.87 USD | `+10.55%` | 1,403,580.15 USD | `+1.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4022.50` | `2,421` | 9,731,392.61 USD | 1,026,529.87 USD | `+10.55%` | 1,403,580.15 USD | `+1.42` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4019.40` | `33.0648` | 132,900.66 USD | 1,235,758.00 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `4019.50` | `2.5574` | 10,279.47 USD | 1,102,857.35 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4019.60` | `0.0547` | 219.87 USD | 1,092,577.88 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4019.70` | `8.1324` | 32,689.81 USD | 1,092,358.00 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4019.80` | `0.4869` | 1,957.24 USD | 1,059,668.20 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4019.90` | `76.0861` | 305,858.51 USD | 1,057,710.96 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4020.00` | `39.0897` | 157,140.59 USD | 751,852.44 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4020.10` | `9.9436` | 39,974.27 USD | 594,711.85 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4020.20` | `5.4755` | 22,012.61 USD | 554,737.58 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4020.30` | `14.8923` | 59,871.51 USD | 532,724.98 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4020.40` | `0.5765` | 2,317.76 USD | 472,853.46 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4020.50` | `54.1285` | 217,623.63 USD | 470,535.70 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4020.70` | `2.2610` | 9,090.80 USD | 252,912.07 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4020.80` | `8.4031` | 33,787.18 USD | 243,821.27 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4020.90` | `7.5318` | 30,284.61 USD | 210,034.08 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4021.00` | `14.4804` | 58,225.69 USD | 179,749.47 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4021.10` | `0.2486` | 999.65 USD | 121,523.78 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4021.20` | `1.5896` | 6,392.10 USD | 120,524.13 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4021.30` | `24.8671` | 99,998.07 USD | 114,132.03 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4021.50` | `3.5146` | 14,133.96 USD | 14,133.96 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4021.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,021.55` | `0.00%` | `-` |
| `ASK` | `4021.60` | `16.1339` | 64,884.09 USD | 64,884.09 USD | `10 orders` | `+0.00%` | `-` |
| `ASK` | `4021.70` | `25.5611` | 102,799.08 USD | 167,683.17 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `4021.80` | `19.2053` | 77,239.88 USD | 244,923.04 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4021.90` | `11.4384` | 46,004.10 USD | 290,927.14 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4022.00` | `14.4259` | 58,020.97 USD | 348,948.11 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4022.10` | `18.0323` | 72,527.71 USD | 421,475.83 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4022.20` | `10.2449` | 41,207.04 USD | 462,682.87 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4022.30` | `4.9073` | 19,738.63 USD | 482,421.50 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4022.40` | `8.2925` | 33,355.75 USD | 515,777.25 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4022.50` | `8.4659` | 34,054.08 USD | 549,831.33 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4022.60` | `8.8080` | 35,431.06 USD | 585,262.39 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4022.70` | `48.6791` | 195,821.42 USD | 781,083.81 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4022.80` | `13.5346` | 54,446.99 USD | 835,530.80 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4022.90` | `1.3597` | 5,469.94 USD | 841,000.73 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4023.00` | `9.2148` | 37,071.14 USD | 878,071.88 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4023.10` | `9.6855` | 38,965.74 USD | 917,037.61 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4023.20` | `9.8917` | 39,796.29 USD | 956,833.90 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4023.30` | `16.9931` | 68,368.34 USD | 1,025,202.24 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4023.40` | `0.4395` | 1,768.28 USD | 1,026,970.52 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4023.50` | `3.1183` | 12,546.48 USD | 1,039,517.00 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,616,630.94 USD | `6,372.61` | `4191.43` | `4019.80` | `29365.52` | 1,093,787.66 USD | `+4.27%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,369,462.69 USD | `6,311.13` | `4133.84` | `4019.80` | `13316.03` | 719,765.19 USD | `+2.84%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,980,291.96 USD | `5,717.06` | `4234.49` | `4019.80` | `27627.75` | 1,228,583.26 USD | `+5.35%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,414,137.30 USD | `4,828.91` | `4157.43` | `4019.80` | `2087.89` | -661,745.01 USD | `-3.41%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,145,255.73 USD | `3,518.90` | `4129.56` | `4019.80` | `301.08` | -386,238.85 USD | `-2.73%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,137,890.24 USD | `3,268.21` | `4228.94` | `4019.80` | `4410.05` | 683,188.89 USD | `+5.20%` | `25X Cross` |
| `178` | `0xa742...e390` | `SHORT` | 11,657,420.40 USD | `2,900.00` | `4364.92` | `4019.80` | `4235.62` | 1,000,855.93 USD | `+8.59%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,843,560.00 USD | `2,200.00` | `4176.09` | `4019.80` | `2490.92` | -343,859.30 USD | `-3.89%` | `25X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,843,120.00 USD | `2,200.00` | `4112.20` | `4019.80` | `4331.10` | 203,734.59 USD | `+2.30%` | `20X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,986,898.81 USD | `1,986.89` | `4032.86` | `4019.80` | `24049.47` | 25,967.36 USD | `+0.33%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,941,773.93 USD | `1,975.37` | `4048.55` | `4019.80` | `6492.70` | 55,617.78 USD | `+0.70%` | `6X Cross` |
| `378` | `0xc26c...b8f4` | `LONG` | 6,351,090.25 USD | `1,579.95` | `4075.62` | `4019.80` | `0.000000` | -88,206.72 USD | `-1.39%` | `1X Cross` |
| `419` | `0x12d2...f97f` | `LONG` | 5,636,370.83 USD | `1,401.94` | `4278.91` | `4019.80` | `2513.15` | -362,419.75 USD | `-6.43%` | `20X Cross` |
| `575` | `0x63da...8add` | `LONG` | 4,019,800.00 USD | `1,000.00` | `4021.46` | `4019.80` | `3564.06` | -1,660.96 USD | `-0.04%` | `25X Cross` |
| `595` | `0x9aa5...58af` | `LONG` | 3,906,389.50 USD | `971.64` | `4279.98` | `4019.80` | `0.000000` | -252,219.59 USD | `-6.46%` | `20X Cross` |
| `624` | `0xf3dc...1672` | `LONG` | 3,741,403.53 USD | `930.74` | `4024.62` | `4019.80` | `3337.54` | -4,489.04 USD | `-0.12%` | `20X Cross` |
| `689` | `0x4a20...3c26` | `LONG` | 3,366,263.05 USD | `837.40` | `4599.73` | `4019.80` | `0.000000` | -485,557.33 USD | `-14.42%` | `20X Cross` |
| `703` | `0x354b...6425` | `LONG` | 3,299,768.60 USD | `820.88` | `4033.57` | `4019.80` | `0.000000` | -11,305.39 USD | `-0.34%` | `10X Cross` |
| `843` | `0x0fac...7a0a` | `LONG` | 2,759,532.40 USD | `686.49` | `4290.34` | `4019.80` | `1336.92` | -185,726.30 USD | `-6.73%` | `25X Cross` |
| `884` | `0xd8c5...99b0` | `SHORT` | 2,582,138.23 USD | `642.35` | `4175.35` | `4019.80` | `32055.51` | 99,922.95 USD | `+3.87%` | `4X Cross` |
| `919` | `0x625e...a354` | `SHORT` | 2,492,152.00 USD | `620.00` | `4122.81` | `4019.80` | `4342.20` | 63,995.03 USD | `+2.57%` | `20X Cross` |
| `946` | `0xeae3...e8ad` | `SHORT` | 2,411,940.00 USD | `600.00` | `4104.77` | `4019.80` | `4325.22` | 50,925.11 USD | `+2.11%` | `20X Cross` |
| `947` | `0xf285...fa82` | `LONG` | 2,404,744.58 USD | `598.11` | `4146.45` | `4019.80` | `3891.19` | -75,274.97 USD | `-3.13%` | `25X Cross` |
| `964` | `0x12f7...8750` | `LONG` | 2,354,037.89 USD | `585.61` | `4082.77` | `4019.80` | `2167.83` | -36,879.09 USD | `-1.57%` | `10X Cross` |
| `1122` | `0x413c...886c` | `LONG` | 2,009,950.00 USD | `500.00` | `4010.43` | `4019.80` | `0.000000` | 4,733.77 USD | `+0.24%` | `2X Cross` |
| `1138` | `0x61ce...a62b` | `SHORT` | 1,999,914.32 USD | `497.50` | `4071.66` | `4019.80` | `4692.34` | 25,754.47 USD | `+1.29%` | `20X Cross` |
| `1143` | `0x0593...40f9` | `LONG` | 1,994,532.30 USD | `496.18` | `4024.57` | `4019.80` | `3701.68` | -2,371.52 USD | `-0.12%` | `10X Isolated` |
| `1262` | `0x2edd...8179` | `LONG` | 1,824,496.28 USD | `453.58` | `4169.95` | `4022.70` | `0.000000` | -66,927.84 USD | `-3.67%` | `10X Cross` |
| `1263` | `0xead5...69f2` | `LONG` | 1,824,029.76 USD | `453.78` | `4220.88` | `4019.80` | `3538.89` | -91,338.29 USD | `-5.01%` | `5X Isolated` |
| `1322` | `0x7a6d...f79c` | `SHORT` | 1,723,240.20 USD | `428.38` | `4136.09` | `4022.70` | `5890.65` | 48,574.80 USD | `+2.82%` | `10X Cross` |
| `1389` | `0x46fc...1195` | `LONG` | 1,636,173.16 USD | `407.03` | `4055.53` | `4019.80` | `1975.24` | -14,546.65 USD | `-0.89%` | `20X Cross` |
| `1424` | `0xee02...309d` | `SHORT` | 1,607,920.00 USD | `400.00` | `4438.84` | `4019.80` | `4226.84` | 167,618.60 USD | `+10.42%` | `25X Isolated` |
| `1425` | `0x6d15...d374` | `LONG` | 1,607,840.00 USD | `400.00` | `4068.25` | `4019.80` | `3841.76` | -19,460.00 USD | `-1.21%` | `25X Cross` |
| `1451` | `0x02a7...fe9f` | `SHORT` | 1,567,722.00 USD | `390.00` | `4055.02` | `4019.80` | `4306.66` | 13,737.25 USD | `+0.88%` | `25X Cross` |
| `1484` | `0x51f6...2b39` | `LONG` | 1,530,466.89 USD | `380.49` | `4234.66` | `4022.70` | `0.000000` | -80,761.18 USD | `-5.28%` | `10X Cross` |
| `1487` | `0x7e77...b8d2` | `SHORT` | 1,527,524.00 USD | `380.00` | `4131.92` | `4019.80` | `4293.46` | 42,605.64 USD | `+2.79%` | `20X Cross` |
| `1509` | `0x72c2...9b37` | `LONG` | 1,499,950.51 USD | `373.13` | `4000.98` | `4019.80` | `3777.99` | 7,057.00 USD | `+0.47%` | `13X Isolated` |
| `1545` | `0xaa44...b844` | `LONG` | 1,447,380.00 USD | `360.00` | `4043.10` | `4019.80` | `2803.21` | -8,137.63 USD | `-0.56%` | `4X Cross` |
| `1546` | `0x781e...96b7` | `SHORT` | 1,446,577.51 USD | `359.55` | `4365.03` | `4022.70` | `12773.30` | 122,869.97 USD | `+8.49%` | `10X Cross` |
| `1657` | `0xa41f...d50a` | `LONG` | 1,322,559.23 USD | `328.96` | `4468.89` | `4019.80` | `3833.14` | -147,538.63 USD | `-11.16%` | `15X Cross` |
| `1684` | `0x49e9...e1d0` | `SHORT` | 1,300,635.63 USD | `323.56` | `4025.23` | `4019.80` | `28417.33` | 1,757.06 USD | `+0.14%` | `4X Cross` |
| `1712` | `0xada6...6f88` | `LONG` | 1,283,455.98 USD | `319.28` | `4166.46` | `4019.80` | `1877.85` | -46,794.53 USD | `-3.65%` | `5X Cross` |
| `1718` | `0xbf5a...88ba` | `SHORT` | 1,277,099.76 USD | `317.65` | `4091.80` | `4019.80` | `10491.78` | 22,683.27 USD | `+1.78%` | `20X Cross` |
| `1738` | `0xff31...ff6c` | `SHORT` | 1,246,138.00 USD | `310.00` | `4372.43` | `4019.80` | `4789.13` | 109,317.38 USD | `+8.77%` | `10X Isolated` |
| `1905` | `0x50e2...d770` | `LONG` | 1,086,822.87 USD | `270.37` | `4243.58` | `4019.80` | `2562.05` | -60,503.59 USD | `-5.57%` | `20X Cross` |
| `1918` | `0x4c92...4f17` | `SHORT` | 1,072,189.74 USD | `266.72` | `4260.98` | `4019.80` | `6522.83` | 64,302.50 USD | `+6.00%` | `20X Cross` |
| `1988` | `0xd346...c4f3` | `LONG` | 1,025,747.64 USD | `255.17` | `4188.66` | `4019.80` | `3310.37` | -43,088.87 USD | `-4.20%` | `5X Isolated` |
| `2024` | `0xe47f...758c` | `LONG` | 1,004,975.00 USD | `250.00` | `4020.00` | `4019.80` | `3774.29` | -25.00 USD | `-0.00%` | `20X Cross` |
| `2025` | `0x1581...463b` | `LONG` | 1,004,900.00 USD | `250.00` | `4003.77` | `4019.80` | `3504.59` | 3,956.41 USD | `+0.39%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.86%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.14%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.86%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.14%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.14%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--1.08%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.35%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.72%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.20` | 16,450,000.00 USD | 16,450,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.70` | 3,620,000.00 USD | 3,620,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,370,000.00 USD | 16,370,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.80` | 3,620,000.00 USD | 3,620,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,230,000.00 USD | 16,230,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3620.90` | 3,590,000.00 USD | 3,590,000.00 USD | 30,600.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,170,000.00 USD | 16,170,000.00 USD | 86,210.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.00` | 3,550,000.00 USD | 3,550,000.00 USD | 40,950.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,060,000.00 USD | 16,060,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.10` | 3,500,000.00 USD | 3,500,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,870,000.00 USD | 15,870,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.20` | 3,470,000.00 USD | 3,470,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,740,000.00 USD | 15,740,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.30` | 3,440,000.00 USD | 3,440,000.00 USD | 49,080.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,610,000.00 USD | 15,610,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3641.40` | 3,380,000.00 USD | 3,380,000.00 USD | 13,660.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.50` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,550,000.00 USD | 15,550,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3649.60` | 3,360,000.00 USD | 3,360,000.00 USD | 23,000.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,510,000.00 USD | 15,510,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3653.70` | 3,340,000.00 USD | 3,340,000.00 USD | 19,450.00 USD | 0.00 USD | 977.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,490,000.00 USD | 15,490,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3657.80` | 3,320,000.00 USD | 3,320,000.00 USD | 5,110.00 USD | 0.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,430,000.00 USD | 15,430,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3661.90` | 3,310,000.00 USD | 3,310,000.00 USD | 2,940.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,420,000.00 USD | 15,420,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3666.00` | 3,300,000.00 USD | 3,300,000.00 USD | 6,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,400,000.00 USD | 15,400,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3670.10` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,390,000.00 USD | 15,390,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 14,970,000.00 USD | 14,970,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,450,000.00 USD | 14,450,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,920,000.00 USD | 13,920,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.60` | 3,290,000.00 USD | 3,290,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,640,000.00 USD | 13,640,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.70` | 3,250,000.00 USD | 3,250,000.00 USD | 68,860.00 USD | 0.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,210,000.00 USD | 13,210,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.80` | 3,180,000.00 USD | 3,180,000.00 USD | 92,460.00 USD | 0.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,030,000.00 USD | 13,030,000.00 USD | 289,880.00 USD | 0.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.90` | 3,080,000.00 USD | 3,080,000.00 USD | 147,900.00 USD | 0.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,680,000.00 USD | 12,680,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.00` | 2,910,000.00 USD | 2,910,000.00 USD | 110,190.00 USD | 0.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,030,000.00 USD | 12,030,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.10` | 2,770,000.00 USD | 2,770,000.00 USD | 88,450.00 USD | 0.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,650,000.00 USD | 11,650,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.20` | 2,680,000.00 USD | 2,680,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,070,000.00 USD | 11,070,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.30` | 2,520,000.00 USD | 2,520,000.00 USD | 47,790.00 USD | 0.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,850,000.00 USD | 10,850,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.40` | 2,450,000.00 USD | 2,450,000.00 USD | 15,370.00 USD | 0.00 USD | 9,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,760,000.00 USD | 10,760,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.50` | 2,430,000.00 USD | 2,430,000.00 USD | 61,290.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,630,000.00 USD | 10,630,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3895.60` | 2,360,000.00 USD | 2,360,000.00 USD | 44,820.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,500,000.00 USD | 10,500,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3899.70` | 2,310,000.00 USD | 2,310,000.00 USD | 34,730.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,380,000.00 USD | 10,380,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.80` | 2,270,000.00 USD | 2,270,000.00 USD | 35,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.90` | 2,230,000.00 USD | 2,230,000.00 USD | 20,800.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,330,000.00 USD | 10,330,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,280,000.00 USD | 10,280,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3916.10` | 2,210,000.00 USD | 2,210,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,260,000.00 USD | 10,260,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,890,000.00 USD | 9,890,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,110,000.00 USD | 9,110,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,120,000.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3932.50` | 2,200,000.00 USD | 2,200,000.00 USD | 5,620.00 USD | 0.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,010,000.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.60` | 2,190,000.00 USD | 2,190,000.00 USD | 153,970.00 USD | 0.00 USD | 9,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,510,000.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.70` | 2,020,000.00 USD | 2,020,000.00 USD | 128,480.00 USD | 0.00 USD | 13,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,790,000.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.80` | 1,880,000.00 USD | 1,880,000.00 USD | 292,410.00 USD | 0.00 USD | 26,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,360,000.00 USD | 5,360,000.00 USD | 605,870.00 USD | 0.00 USD | 137,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3948.90` | 1,560,000.00 USD | 1,560,000.00 USD | 202,600.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.00` | 1,320,000.00 USD | 1,320,000.00 USD | 238,960.00 USD | 0.00 USD | 33,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.10` | 1,050,000.00 USD | 1,050,000.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.20` | 858,660.00 USD | 858,660.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.30` | 567,700.00 USD | 567,700.00 USD | 61,120.00 USD | 0.00 USD | 27,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.40` | 478,680.00 USD | 478,680.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.50` | 460,300.00 USD | 460,300.00 USD | 150,360.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3977.60` | 303,340.00 USD | 303,340.00 USD | 85,770.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.70` | 210,360.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3985.80` | 138,980.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3989.90` | 67,140.00 USD | 67,140.00 USD | 41,610.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3998.10` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4092.40` | 5,620.00 USD | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4096.50` | 143,550.00 USD | 143,550.00 USD | 125,060.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.60` | 238,120.00 USD | 238,120.00 USD | 85,770.00 USD | 0.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.70` | 445,060.00 USD | 445,060.00 USD | 193,530.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,350,000.00 USD | 5,350,000.00 USD | 606,780.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.80` | 785,020.00 USD | 785,020.00 USD | 292,970.00 USD | 0.00 USD | 46,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,440,000.00 USD | 6,440,000.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.90` | 1,040,000.00 USD | 1,040,000.00 USD | 214,610.00 USD | 0.00 USD | 41,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.00` | 1,230,000.00 USD | 1,230,000.00 USD | 166,650.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,220,000.00 USD | 8,220,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.10` | 1,520,000.00 USD | 1,520,000.00 USD | 277,540.00 USD | 0.00 USD | 14,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,940,000.00 USD | 8,940,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.20` | 1,670,000.00 USD | 1,670,000.00 USD | 106,180.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,190,000.00 USD | 9,190,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.30` | 1,720,000.00 USD | 1,720,000.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,390,000.00 USD | 9,390,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.40` | 1,820,000.00 USD | 1,820,000.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,620,000.00 USD | 9,620,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.50` | 1,950,000.00 USD | 1,950,000.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,870,000.00 USD | 9,870,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.60` | 2,030,000.00 USD | 2,030,000.00 USD | 65,150.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,040,000.00 USD | 10,040,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.70` | 2,090,000.00 USD | 2,090,000.00 USD | 54,840.00 USD | 0.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,140,000.00 USD | 10,140,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.80` | 2,140,000.00 USD | 2,140,000.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,230,000.00 USD | 10,230,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.90` | 2,180,000.00 USD | 2,180,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,610,000.00 USD | 10,610,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.00` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,040,000.00 USD | 11,040,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.10` | 2,200,000.00 USD | 2,200,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,460,000.00 USD | 11,460,000.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,900,000.00 USD | 11,900,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.40` | 2,210,000.00 USD | 2,210,000.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,140,000.00 USD | 12,140,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.50` | 2,300,000.00 USD | 2,300,000.00 USD | 84,040.00 USD | 0.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,480,000.00 USD | 12,480,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.60` | 2,370,000.00 USD | 2,370,000.00 USD | 60,250.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,650,000.00 USD | 12,650,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.70` | 2,520,000.00 USD | 2,520,000.00 USD | 140,480.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 13,000,000.00 USD | 13,000,000.00 USD | 292,190.00 USD | 0.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.80` | 2,640,000.00 USD | 2,640,000.00 USD | 96,720.00 USD | 0.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,640,000.00 USD | 13,640,000.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.90` | 2,770,000.00 USD | 2,770,000.00 USD | 119,480.00 USD | 0.00 USD | 15,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 13,980,000.00 USD | 13,980,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.00` | 2,840,000.00 USD | 2,840,000.00 USD | 63,390.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,490,000.00 USD | 14,490,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.10` | 3,000,000.00 USD | 3,000,000.00 USD | 133,090.00 USD | 0.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,740,000.00 USD | 14,740,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4207.20` | 3,040,000.00 USD | 3,040,000.00 USD | 33,970.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,870,000.00 USD | 14,870,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4211.30` | 3,060,000.00 USD | 3,060,000.00 USD | 10,950.00 USD | 0.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 14,980,000.00 USD | 14,980,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4215.40` | 3,120,000.00 USD | 3,120,000.00 USD | 57,500.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,090,000.00 USD | 15,090,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.50` | 3,180,000.00 USD | 3,180,000.00 USD | 47,060.00 USD | 0.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,200,000.00 USD | 15,200,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.60` | 3,220,000.00 USD | 3,220,000.00 USD | 31,440.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,290,000.00 USD | 15,290,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.70` | 3,260,000.00 USD | 3,260,000.00 USD | 36,150.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,340,000.00 USD | 15,340,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4231.80` | 3,270,000.00 USD | 3,270,000.00 USD | 8,950.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,380,000.00 USD | 15,380,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4235.90` | 3,280,000.00 USD | 3,280,000.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,400,000.00 USD | 15,400,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4240.00` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4244.10` | 3,290,000.00 USD | 3,290,000.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,540,000.00 USD | 15,540,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,670,000.00 USD | 15,670,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,810,000.00 USD | 15,810,000.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,920,000.00 USD | 15,920,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 15,990,000.00 USD | 15,990,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.30` | 3,310,000.00 USD | 3,310,000.00 USD | 8,150.00 USD | 0.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,100,000.00 USD | 16,100,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.40` | 3,330,000.00 USD | 3,330,000.00 USD | 24,480.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,140,000.00 USD | 16,140,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4424.50` | 3,360,000.00 USD | 3,360,000.00 USD | 23,020.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.30` | 3,390,000.00 USD | 3,390,000.00 USD | 29,160.00 USD | 0.00 USD | 929.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,220,000.00 USD | 16,220,000.00 USD | 65,320.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,390,000.00 USD | 16,390,000.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,500,000.00 USD | 16,500,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,630,000.00 USD | 16,630,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,710,000.00 USD | 16,710,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,750,000.00 USD | 16,750,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.70` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `3615.50` | 16,370,000.00 USD | 0.00 USD | 16,370,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.80` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD |
| `7D` | `3619.80` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3620.90` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 30,600.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `3624.10` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 86,210.00 USD | 0.00 USD | 21,190.00 USD |
| `1D` | `3625.00` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 40,950.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `3628.40` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.10` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD |
| `7D` | `3632.70` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3633.20` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.30` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 49,080.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `3641.30` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3641.40` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 13,660.00 USD | 0.00 USD | 4,800.00 USD |
| `1D` | `3645.50` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `3645.60` | 15,550,000.00 USD | 0.00 USD | 15,550,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3649.60` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 23,000.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3649.90` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3653.70` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 19,450.00 USD | 0.00 USD | 977.78 USD |
| `7D` | `3654.20` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3657.80` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 5,110.00 USD | 0.00 USD | 4,100.00 USD |
| `7D` | `3658.50` | 15,430,000.00 USD | 0.00 USD | 15,430,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3661.90` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 2,940.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3666.00` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 6,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3667.10` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3670.10` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD |
| `7D` | `3852.00` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3854.60` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `3856.30` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3858.70` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 68,860.00 USD | 0.00 USD | 4,400.00 USD |
| `7D` | `3860.60` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3862.80` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 92,460.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `3864.90` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 289,880.00 USD | 0.00 USD | 59,280.00 USD |
| `1D` | `3866.90` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 147,900.00 USD | 0.00 USD | 22,530.00 USD |
| `7D` | `3869.20` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3871.00` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 110,190.00 USD | 0.00 USD | 21,730.00 USD |
| `7D` | `3873.50` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3875.10` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 88,450.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3877.80` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3879.20` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD |
| `7D` | `3882.10` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3883.30` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 47,790.00 USD | 0.00 USD | 20,480.00 USD |
| `7D` | `3886.40` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3887.40` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 15,370.00 USD | 0.00 USD | 9,900.00 USD |
| `7D` | `3890.70` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3891.50` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 61,290.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3895.00` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3895.60` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 44,820.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `3899.30` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3899.70` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 34,730.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `3903.60` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3903.80` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 35,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3907.90` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 20,800.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3916.10` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `1D` | `3932.50` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 5,620.00 USD | 0.00 USD | 4,300.00 USD |
| `7D` | `3933.70` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3936.60` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 153,970.00 USD | 0.00 USD | 9,520.00 USD |
| `7D` | `3938.00` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3940.70` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 128,480.00 USD | 0.00 USD | 13,700.00 USD |
| `7D` | `3942.30` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.80` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 292,410.00 USD | 0.00 USD | 26,330.00 USD |
| `7D` | `3946.60` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 605,870.00 USD | 0.00 USD | 137,820.00 USD |
| `1D` | `3948.90` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 202,600.00 USD | 0.00 USD | 42,040.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3953.00` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 238,960.00 USD | 0.00 USD | 33,540.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3957.10` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3961.20` | 858,660.00 USD | 0.00 USD | 858,660.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.30` | 567,700.00 USD | 0.00 USD | 567,700.00 USD | 61,120.00 USD | 0.00 USD | 27,900.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.40` | 478,680.00 USD | 0.00 USD | 478,680.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.50` | 460,300.00 USD | 0.00 USD | 460,300.00 USD | 150,360.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3977.60` | 303,340.00 USD | 0.00 USD | 303,340.00 USD | 85,770.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3981.70` | 210,360.00 USD | 0.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3985.80` | 138,980.00 USD | 0.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 4,620.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3989.90` | 67,140.00 USD | 0.00 USD | 67,140.00 USD | 41,610.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3998.10` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4023.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4023.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD |
| `1D` | `4092.40` | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4096.50` | 143,550.00 USD | 143,550.00 USD | 0.00 USD | 125,060.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4100.60` | 238,120.00 USD | 238,120.00 USD | 0.00 USD | 85,770.00 USD | 0.00 USD | 8,800.00 USD |
| `7D` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4104.70` | 445,060.00 USD | 445,060.00 USD | 0.00 USD | 193,530.00 USD | 0.00 USD | 13,400.00 USD |
| `7D` | `4105.70` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 606,780.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4108.80` | 785,020.00 USD | 785,020.00 USD | 0.00 USD | 292,970.00 USD | 0.00 USD | 46,990.00 USD |
| `7D` | `4110.00` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4112.90` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 214,610.00 USD | 0.00 USD | 41,550.00 USD |
| `7D` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4117.00` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 166,650.00 USD | 0.00 USD | 19,550.00 USD |
| `7D` | `4118.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4121.10` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 277,540.00 USD | 0.00 USD | 14,500.00 USD |
| `7D` | `4122.90` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4125.20` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 106,180.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `4127.20` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4129.30` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `4131.50` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.40` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `4135.80` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.50` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.60` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 15,250.00 USD |
| `7D` | `4144.40` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4145.70` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 54,840.00 USD | 0.00 USD | 7,170.00 USD |
| `7D` | `4148.70` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4153.90` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.00` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `1D` | `4174.40` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `4174.50` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4178.50` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 2,660.00 USD |
| `7D` | `4178.80` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4182.60` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 60,250.00 USD | 0.00 USD | 8,050.00 USD |
| `7D` | `4183.10` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4186.70` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 140,480.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `4187.40` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 292,190.00 USD | 0.00 USD | 53,390.00 USD |
| `1D` | `4190.80` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 96,720.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `4191.70` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4194.90` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 119,480.00 USD | 0.00 USD | 15,450.00 USD |
| `7D` | `4196.00` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4199.00` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 63,390.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4200.30` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4203.10` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 133,090.00 USD | 0.00 USD | 19,190.00 USD |
| `7D` | `4204.60` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4207.20` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 33,970.00 USD | 0.00 USD | 13,590.00 USD |
| `7D` | `4208.90` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4211.30` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 10,950.00 USD | 0.00 USD | 7,620.00 USD |
| `7D` | `4213.20` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4215.40` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 57,500.00 USD | 0.00 USD | 5,020.00 USD |
| `7D` | `4217.50` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4219.50` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 47,060.00 USD | 0.00 USD | 4,850.00 USD |
| `7D` | `4221.80` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4223.60` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 31,440.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `4226.10` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4227.70` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 36,150.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `4230.40` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4231.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4234.70` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `1D` | `4235.90` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4239.00` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4240.00` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `4244.10` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4389.50` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `7D` | `4415.30` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4416.30` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | 2,080.00 USD |
| `7D` | `4419.60` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4420.40` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 24,480.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `4423.90` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4424.50` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 23,020.00 USD | 0.00 USD | 2,060.00 USD |
| `1D` | `4427.30` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 29,160.00 USD | 0.00 USD | 929.32 USD |
| `7D` | `4428.20` | 16,220,000.00 USD | 16,220,000.00 USD | 0.00 USD | 65,320.00 USD | 0.00 USD | 18,160.00 USD |
| `7D` | `4432.50` | 16,390,000.00 USD | 16,390,000.00 USD | 0.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD |
| `7D` | `4436.80` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,630,000.00 USD | 16,630,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.60M` | Total OI Tokens: `68,246.8 PAXG`
  * 1h OI Change: `+0.15%` | 4h OI Change: `-0.15%` | 24h OI Change: `+0.07%`
  * Exchange Breakdown: Binance=`107.13M` | Bybit=`20.01M` | OKX=`-` | Hyperliquid=`25.11M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.36K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `43.80%` | `56.20%` | `0.78` | 749,300.00 USD |
| `15M` | `Binance` | `33.24%` | `66.76%` | `0.50` | 480,970.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `77.77%` | `22.23%` | `3.50` | 9,010.00 USD |
| `15M` | `KuCoin` | `46.68%` | `53.32%` | `0.88` | 37,830.00 USD |
| `15M` | `Gate` | `60.56%` | `39.44%` | `1.54` | 8,440.00 USD |
| `15M` | `Bitget` | `52.44%` | `47.56%` | `1.10` | 92,370.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `54.18%` | `45.82%` | `1.18` | 2,310.00 USD |
| `15M` | `Bitunix` | `71.44%` | `28.56%` | `2.50` | 10,230.00 USD |
| `15M` | `Hyperliquid` | `96.06%` | `3.94%` | `24.38` | 14,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `71.73%` | `28.27%` | `2.54` | 89,860.00 USD |
| `15M` | `HTX` | `81.49%` | `18.51%` | `4.40` | 1,460.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 68.36 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 201.09 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `81.57%` | `18.43%` | `4.43` | 1,630.00 USD |
| `15M` | `Whale Positions` | `33.24%` | `66.76%` | `0.50` | 480,970.00 USD |
| `15M` | `Global Accounts` | `43.80%` | `56.20%` | `0.78` | 749,300.00 USD |
| `1H` | `PAXG` | `51.59%` | `48.41%` | `1.07` | 3,430,000.00 USD |
| `1H` | `Binance` | `41.72%` | `58.28%` | `0.72` | 2,190,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `59.87%` | `40.13%` | `1.49` | 52,600.00 USD |
| `1H` | `KuCoin` | `54.49%` | `45.51%` | `1.20` | 54,180.00 USD |
| `1H` | `Gate` | `74%` | `26%` | `2.85` | 48,460.00 USD |
| `1H` | `Bitget` | `59.69%` | `40.31%` | `1.48` | 434,330.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `69.62%` | `30.38%` | `2.29` | 30,810.00 USD |
| `1H` | `Bitunix` | `43.88%` | `56.12%` | `0.78` | 55,740.00 USD |
| `1H` | `Hyperliquid` | `98.57%` | `1.43%` | `68.93` | 168,770.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `73.26%` | `26.74%` | `2.74` | 366,620.00 USD |
| `1H` | `HTX` | `71.83%` | `28.17%` | `2.55` | 5,110.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `69.02%` | `30.98%` | `2.23` | 10,780.00 USD |
| `1H` | `Aster` | `100%` | `0%` | `1.00` | 446.17 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.5%` | `31.5%` | `2.17` | 8,420.00 USD |
| `1H` | `Whale Positions` | `41.72%` | `58.28%` | `0.72` | 2,190,000.00 USD |
| `1H` | `Global Accounts` | `51.59%` | `48.41%` | `1.07` | 3,430,000.00 USD |
| `4H` | `PAXG` | `52.32%` | `47.68%` | `1.10` | 51,710,000.00 USD |
| `4H` | `Binance` | `53.83%` | `46.17%` | `1.17` | 4,530,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.71%` | `50.29%` | `0.99` | 4,880,000.00 USD |
| `4H` | `KuCoin` | `50.16%` | `49.84%` | `1.01` | 316,190.00 USD |
| `4H` | `Gate` | `52.48%` | `47.52%` | `1.10` | 1,800,000.00 USD |
| `4H` | `Bitget` | `44.43%` | `55.57%` | `0.80` | 1,760,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `54.29%` | `45.71%` | `1.19` | 31,070,000.00 USD |
| `4H` | `Bitunix` | `61.56%` | `38.44%` | `1.60` | 1,640,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.32%` | `48.68%` | `1.05` | 4,270,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `13.45%` | `86.55%` | `0.16` | 1,310,000.00 USD |
| `4H` | `HTX` | `64.45%` | `35.55%` | `1.81` | 12,800.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.59%` | `56.41%` | `0.77` | 126,210.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.83%` | `46.17%` | `1.17` | 4,530,000.00 USD |
| `4H` | `Global Accounts` | `52.32%` | `47.68%` | `1.10` | 51,710,000.00 USD |


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
| `5m` | -14,270.00 USD | -220,190.00 USD | **`DISTRIBUTION`** |
| `15m` | -30,560.00 USD | -109,770.00 USD | **`DISTRIBUTION`** |
| `30m` | 37,350.00 USD | 19,860.00 USD | **`ACCUMULATION`** |
| `1h` | -118,670.00 USD | -337,390.00 USD | **`DISTRIBUTION`** |
| `2h` | -326,570.00 USD | 132,440.00 USD | **`DISTRIBUTION`** |
| `4h` | 302,490.00 USD | 909,370.00 USD | **`ACCUMULATION`** |
| `6h` | 181,880.00 USD | 504,600.00 USD | **`ACCUMULATION`** |
| `8h` | -166,030.00 USD | 1,390,000.00 USD | **`ACCUMULATION`** |
| `12h` | -279,510.00 USD | 910,710.00 USD | **`ACCUMULATION`** |
| `24h` | -374,570.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,260,000.00 USD | -7,620,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,700,000.00 USD | -71,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-14.27K` | 15m=`-30.56K` | 1h=`-118.67K` | 24h=`-374.57K`
* Futures Capital Netflows: 5m=`-220.19K` | 15m=`-109.77K` | 1h=`-337.39K` | 24h=`+1.14M`
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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4016.67` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4008.25` (Risk Distance: `8.42` pts)
  * +2.5R Take Profit: `4037.72`
  * Mathematical Lot Sizing: **`1.18 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4048.95` (Risk Distance: `8.42` pts)
  * +2.5R Take Profit: `4019.48`
  * Mathematical Lot Sizing: **`1.18 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4052.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
