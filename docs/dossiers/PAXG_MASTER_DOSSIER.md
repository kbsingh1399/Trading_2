# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4018.36` | **Live Ask Quote**: `4018.45` | **Mid Price**: `4018.40`
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
  * Session VWAP: `4033.57` | VWAP Z-Score: `+0.23` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `9.47` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `57.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4066.21` | Lower -3.00σ Band: `4000.93`
  * Upper +2.51σ Band: `4060.88` | Lower -2.51σ Band: `4006.26`
  * Upper +2.01σ Band: `4055.44` | Lower -2.01σ Band: `4011.70`
  * Upper +2.00σ Band: `4055.33` | Lower -2.00σ Band: `4011.81`
  * Upper +1.28σ Band: `4047.50` | Lower -1.28σ Band: `4019.64`
  * Upper +1.00σ Band: `4044.45` | Lower -1.00σ Band: `4022.69`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4027.39` | EMA-20=`4027.48` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4031.92` (Slope: `+0.0000`) | EMA-100=`4036.60`
  * Institutional Anchors: EMA-144=`4036.78` | EMA-200=`4034.89` (Slope: `-0.0302`) | EMA-233=`4033.46`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4015.80` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.71` (Distance: `-0.56%`)
  * Point of Control (POC) = `4027.30` (Distance: `-0.23%`)
  * Value Area Low (VAL) = `4019.82` (Distance: `-0.05%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `4002.33` - `4034.48`
  * Optimal Trade Entry (OTE 0.705): `4026.44`
  * Structural Invalidation Anchor (0.786): `4050.55`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4022.00` | `4022.55` | `4019.39` | `4020.48` | `136` | 548,360.60 USD | 338,803.03 USD | `+61.78%` | 907,861.52 USD | `+2.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4020.48` | `4023.30` | `4020.48` | `4023.30` | `23` | 94,039.10 USD | 82,457.94 USD | `+87.68%` | 990,319.45 USD | `+0.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4023.30` | `4024.01` | `4023.30` | `4024.00` | `8` | 30,821.85 USD | 2,816.09 USD | `+9.14%` | 993,135.55 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4019.60` | `4021.70` | `4017.67` | `4021.36` | `133` | 536,295.57 USD | -74,630.45 USD | `-13.92%` | 494,219.57 USD | `-0.70` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4021.36` | `4023.30` | `4019.39` | `4023.30` | `201` | 809,848.30 USD | 483,447.28 USD | `+59.70%` | 977,666.85 USD | `+2.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4023.30` | `4024.01` | `4023.30` | `4024.00` | `8` | 30,821.85 USD | 2,816.09 USD | `+9.14%` | 980,482.95 USD | `-0.27` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4029.13` | `4030.46` | `4023.08` | `4026.82` | `526` | 2,116,236.19 USD | -146,951.88 USD | `-6.94%` | -157,920.93 USD | `-0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 692,493.29 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4024.01` | `4023.30` | `4024.00` | `8` | 30,846.00 USD | 2,791.95 USD | `+9.05%` | 695,285.24 USD | `-0.17` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4026.82` | `4016.00` | `4024.00` | `959` | 3,854,571.35 USD | 853,206.16 USD | `+22.13%` | 1,230,256.44 USD | `+1.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4026.82` | `4016.00` | `4024.00` | `959` | 3,854,571.35 USD | 853,206.16 USD | `+22.13%` | 1,230,256.44 USD | `+1.25` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4016.80` | `4.8283` | 19,394.32 USD | 1,399,110.95 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4016.90` | `26.4792` | 106,364.30 USD | 1,379,716.64 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `4017.00` | `8.5981` | 34,538.57 USD | 1,273,352.34 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4017.10` | `26.6267` | 106,962.12 USD | 1,238,813.77 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4017.20` | `14.4179` | 57,919.59 USD | 1,131,851.66 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `4017.30` | `3.2158` | 12,918.83 USD | 1,073,932.07 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4017.50` | `92.9218` | 373,313.33 USD | 1,061,013.23 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4017.60` | `14.3831` | 57,785.54 USD | 687,699.90 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4017.70` | `1.8126` | 7,282.48 USD | 629,914.36 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4017.80` | `5.9987` | 24,101.58 USD | 622,631.88 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4017.90` | `17.9836` | 72,256.31 USD | 598,530.30 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4018.10` | `49.8287` | 200,216.70 USD | 526,273.99 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4018.20` | `9.9333` | 39,913.99 USD | 326,057.29 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `4018.30` | `35.8687` | 144,131.20 USD | 286,143.31 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4018.40` | `1.0169` | 4,086.31 USD | 142,012.11 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4018.50` | `24.8830` | 99,992.34 USD | 137,925.80 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4018.60` | `2.4272` | 9,753.95 USD | 37,933.46 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4018.70` | `2.3431` | 9,416.22 USD | 28,179.52 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4018.80` | `1.0127` | 4,069.84 USD | 18,763.30 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4019.00` | `3.6560` | 14,693.46 USD | 14,693.46 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4019.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,019.05` | `0.00%` | `-` |
| `ASK` | `4019.10` | `22.8476` | 91,826.79 USD | 91,826.79 USD | `14 orders` | `+0.00%` | `-` |
| `ASK` | `4019.20` | `53.7387` | 215,986.58 USD | 307,813.37 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4019.30` | `4.6649` | 18,749.63 USD | 326,563.00 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4019.40` | `21.1175` | 84,879.68 USD | 411,442.68 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4019.50` | `18.9738` | 76,265.19 USD | 487,707.87 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4019.60` | `20.3953` | 81,980.95 USD | 569,688.82 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4019.70` | `25.0906` | 100,856.68 USD | 670,545.51 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4019.80` | `2.4272` | 9,756.86 USD | 680,302.36 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4019.90` | `26.3658` | 105,987.88 USD | 786,290.24 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `4020.00` | `4.7998` | 19,295.20 USD | 805,585.44 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4020.10` | `0.9328` | 3,749.95 USD | 809,335.39 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4020.20` | `8.7963` | 35,362.89 USD | 844,698.27 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4020.30` | `29.5358` | 118,742.78 USD | 963,441.05 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4020.40` | `15.3673` | 61,782.69 USD | 1,025,223.74 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4020.50` | `19.5897` | 78,760.39 USD | 1,103,984.13 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4020.60` | `17.6389` | 70,918.96 USD | 1,174,903.09 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4020.70` | `9.6327` | 38,730.20 USD | 1,213,633.29 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4020.80` | `14.7417` | 59,273.43 USD | 1,272,906.72 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4020.90` | `57.4760` | 231,105.25 USD | 1,504,011.97 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `4021.00` | `7.7258` | 31,065.44 USD | 1,535,077.41 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:31:36 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,699,860.51 USD | `6,388.07` | `4191.43` | `4023.00` | `26924.19` | 1,075,360.67 USD | `+4.18%` | `4X Cross` |
| `59` | `0x4692...164f` | `SHORT` | 25,298,312.02 USD | `6,287.33` | `4135.96` | `4023.00` | `13226.96` | 705,853.45 USD | `+2.79%` | `5X Cross` |
| `74` | `0xb83d...6e36` | `SHORT` | 23,003,731.91 USD | `5,717.06` | `4234.49` | `4023.00` | `24867.61` | 1,205,143.32 USD | `+5.24%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,429,106.91 USD | `4,828.91` | `4157.43` | `4023.00` | `2095.36` | -646,775.40 USD | `-3.33%` | `25X Cross` |
| `153` | `0x645b...87b8` | `LONG` | 14,156,620.26 USD | `3,518.83` | `4129.76` | `4023.00` | `0.000000` | -375,335.25 USD | `-2.65%` | `3X Cross` |
| `168` | `0x7a6d...f79c` | `SHORT` | 13,148,348.52 USD | `3,268.21` | `4228.94` | `4023.00` | `4400.10` | 672,730.61 USD | `+5.12%` | `25X Cross` |
| `189` | `0xa742...e390` | `SHORT` | 11,666,990.40 USD | `2,900.00` | `4364.92` | `4023.00` | `4235.47` | 991,285.93 USD | `+8.50%` | `20X Cross` |
| `280` | `0x41e5...0825` | `SHORT` | 8,852,140.00 USD | `2,200.00` | `4112.20` | `4023.00` | `4330.96` | 194,714.59 USD | `+2.20%` | `20X Cross` |
| `281` | `0x3678...b209` | `LONG` | 8,850,820.00 USD | `2,200.00` | `4176.09` | `4023.00` | `2640.94` | -336,599.30 USD | `-3.80%` | `25X Cross` |
| `307` | `0xfc66...ca06` | `SHORT` | 8,107,129.81 USD | `2,014.84` | `4032.86` | `4023.00` | `24517.85` | 18,474.81 USD | `+0.23%` | `3X Cross` |
| `321` | `0xacb6...efbd` | `SHORT` | 7,948,292.65 USD | `1,975.37` | `4048.55` | `4023.00` | `6486.22` | 49,099.07 USD | `+0.62%` | `6X Cross` |
| `418` | `0x12d2...f97f` | `LONG` | 5,640,716.86 USD | `1,401.94` | `4278.91` | `4023.00` | `2609.68` | -358,073.72 USD | `-6.35%` | `20X Cross` |
| `438` | `0xc26c...b8f4` | `LONG` | 5,459,370.44 USD | `1,357.01` | `4082.56` | `4023.00` | `0.000000` | -80,696.81 USD | `-1.48%` | `1X Cross` |
| `575` | `0x63da...8add` | `LONG` | 4,023,100.00 USD | `1,000.00` | `4021.46` | `4023.00` | `3563.91` | 1,639.04 USD | `+0.04%` | `25X Cross` |
| `601` | `0x9aa5...58af` | `LONG` | 3,909,401.59 USD | `971.64` | `4279.98` | `4023.00` | `0.000000` | -249,207.50 USD | `-6.37%` | `20X Cross` |
| `624` | `0xf3dc...1672` | `LONG` | 3,745,033.43 USD | `930.74` | `4024.62` | `4023.00` | `3337.38` | -859.14 USD | `-0.02%` | `20X Cross` |
| `687` | `0x4a20...3c26` | `LONG` | 3,368,942.73 USD | `837.40` | `4599.73` | `4023.00` | `0.000000` | -482,877.65 USD | `-14.33%` | `20X Cross` |
| `776` | `0x354b...6425` | `LONG` | 3,030,542.20 USD | `753.17` | `4039.90` | `4023.00` | `0.000000` | -12,202.46 USD | `-0.40%` | `10X Cross` |
| `849` | `0x0fac...7a0a` | `LONG` | 2,739,969.80 USD | `680.97` | `4292.43` | `4023.00` | `1643.43` | -183,066.96 USD | `-6.68%` | `25X Cross` |
| `850` | `0xd8c5...99b0` | `SHORT` | 2,736,666.84 USD | `680.14` | `4175.35` | `4023.00` | `30430.27` | 103,147.68 USD | `+3.77%` | `4X Cross` |
| `919` | `0x625e...a354` | `SHORT` | 2,494,694.00 USD | `620.00` | `4122.81` | `4023.00` | `4342.05` | 61,453.03 USD | `+2.46%` | `20X Cross` |
| `944` | `0xeae3...e8ad` | `SHORT` | 2,413,680.00 USD | `600.00` | `4104.77` | `4023.00` | `4325.08` | 49,185.11 USD | `+2.04%` | `20X Cross` |
| `953` | `0xf285...fa82` | `LONG` | 2,406,299.66 USD | `598.11` | `4146.45` | `4023.00` | `3891.04` | -73,719.90 USD | `-3.06%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,355,970.41 USD | `585.61` | `4082.77` | `4023.00` | `2229.86` | -34,946.57 USD | `-1.48%` | `10X Cross` |
| `1134` | `0x413c...886c` | `LONG` | 2,010,550.00 USD | `500.00` | `4010.43` | `4023.00` | `0.000000` | 5,333.77 USD | `+0.27%` | `2X Cross` |
| `1140` | `0x61ce...a62b` | `SHORT` | 2,001,804.83 USD | `497.50` | `4071.66` | `4023.00` | `4699.82` | 23,863.96 USD | `+1.19%` | `20X Cross` |
| `1144` | `0x0593...40f9` | `LONG` | 1,996,020.84 USD | `496.18` | `4024.57` | `4023.00` | `3701.53` | -882.99 USD | `-0.04%` | `10X Isolated` |
| `1258` | `0xead5...69f2` | `LONG` | 1,825,890.28 USD | `453.78` | `4220.88` | `4023.00` | `3538.74` | -89,477.78 USD | `-4.90%` | `5X Isolated` |
| `1263` | `0x2edd...8179` | `LONG` | 1,821,104.19 USD | `452.25` | `4174.40` | `4025.80` | `0.000000` | -66,754.15 USD | `-3.67%` | `10X Cross` |
| `1325` | `0x7a6d...f79c` | `SHORT` | 1,723,283.04 USD | `428.38` | `4136.09` | `4025.80` | `5917.69` | 48,531.96 USD | `+2.82%` | `10X Cross` |
| `1400` | `0x46fc...1195` | `LONG` | 1,618,281.86 USD | `402.20` | `4056.55` | `4023.00` | `1775.16` | -13,255.07 USD | `-0.82%` | `20X Cross` |
| `1412` | `0x6d15...d374` | `LONG` | 1,609,480.00 USD | `400.00` | `4068.25` | `4023.00` | `3841.61` | -17,820.00 USD | `-1.11%` | `25X Cross` |
| `1414` | `0xee02...309d` | `SHORT` | 1,609,240.00 USD | `400.00` | `4438.84` | `4023.00` | `4226.69` | 166,298.60 USD | `+10.33%` | `25X Isolated` |
| `1455` | `0x02a7...fe9f` | `SHORT` | 1,569,009.00 USD | `390.00` | `4055.02` | `4023.00` | `4306.51` | 12,450.25 USD | `+0.79%` | `25X Cross` |
| `1490` | `0x7e77...b8d2` | `SHORT` | 1,528,664.00 USD | `380.00` | `4131.92` | `4023.00` | `4293.32` | 41,465.64 USD | `+2.71%` | `20X Cross` |
| `1491` | `0x51f6...2b39` | `LONG` | 1,524,435.48 USD | `378.61` | `4235.75` | `4025.80` | `0.000000` | -79,243.75 USD | `-5.20%` | `10X Cross` |
| `1509` | `0x72c2...9b37` | `LONG` | 1,501,368.41 USD | `373.13` | `4000.98` | `4023.00` | `3777.84` | 8,474.90 USD | `+0.56%` | `13X Isolated` |
| `1548` | `0xaa44...b844` | `LONG` | 1,448,568.00 USD | `360.00` | `4043.10` | `4023.00` | `2778.18` | -6,949.63 USD | `-0.48%` | `9X Cross` |
| `1569` | `0x781e...96b7` | `SHORT` | 1,428,740.85 USD | `354.81` | `4369.58` | `4025.80` | `12576.08` | 121,621.49 USD | `+8.51%` | `10X Cross` |
| `1656` | `0xa41f...d50a` | `LONG` | 1,323,579.01 USD | `328.96` | `4468.89` | `4023.00` | `3832.98` | -146,518.84 USD | `-11.07%` | `15X Cross` |
| `1682` | `0x49e9...e1d0` | `SHORT` | 1,301,735.73 USD | `323.56` | `4025.23` | `4023.00` | `32751.74` | 656.97 USD | `+0.05%` | `4X Cross` |
| `1698` | `0xada6...6f88` | `LONG` | 1,284,669.23 USD | `319.28` | `4166.46` | `4023.00` | `1831.68` | -45,581.28 USD | `-3.55%` | `5X Cross` |
| `1709` | `0xbf5a...88ba` | `SHORT` | 1,277,989.19 USD | `317.65` | `4091.80` | `4023.00` | `10377.68` | 21,793.84 USD | `+1.71%` | `20X Cross` |
| `1744` | `0xff31...ff6c` | `SHORT` | 1,247,068.00 USD | `310.00` | `4372.43` | `4023.00` | `4788.98` | 108,387.38 USD | `+8.69%` | `10X Isolated` |
| `1922` | `0x50e2...d770` | `LONG` | 1,087,633.98 USD | `270.37` | `4243.58` | `4023.00` | `2561.89` | -59,692.48 USD | `-5.49%` | `20X Cross` |
| `1937` | `0x4c92...4f17` | `SHORT` | 1,073,043.24 USD | `266.72` | `4260.98` | `4023.00` | `6549.18` | 63,448.99 USD | `+5.91%` | `20X Cross` |
| `1998` | `0xd346...c4f3` | `LONG` | 1,026,589.71 USD | `255.17` | `4188.66` | `4023.00` | `3310.22` | -42,246.79 USD | `-4.12%` | `5X Isolated` |
| `2048` | `0x1581...463b` | `LONG` | 1,005,900.00 USD | `250.00` | `4003.77` | `4023.00` | `3504.44` | 4,956.41 USD | `+0.49%` | `15X Cross` |
| `2062` | `0x9c06...0560` | `LONG` | 1,000,372.78 USD | `248.66` | `4021.48` | `4023.00` | `0.000000` | 401.43 USD | `+0.04%` | `25X Cross` |

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
| `7D` | `3618.80` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 45,950.00 USD | 0.00 USD | 3,760.00 USD |
| `1D` | `3622.30` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 25,480.00 USD | 0.00 USD | 1,000.00 USD |
| `7D` | `3623.00` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 79,630.00 USD | 0.00 USD | 18,670.00 USD |
| `1D` | `3626.50` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 24,820.00 USD | 0.00 USD | 6,040.00 USD |
| `7D` | `3627.20` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 206,750.00 USD | 0.00 USD | 12,940.00 USD |
| `1D` | `3630.70` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 36,780.00 USD | 0.00 USD | 5,860.00 USD |
| `7D` | `3631.40` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 87,600.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `3634.90` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 44,210.00 USD | 0.00 USD | 4,020.00 USD |
| `7D` | `3635.60` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 135,440.00 USD | 0.00 USD | 32,550.00 USD |
| `1D` | `3639.10` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 61,190.00 USD | 0.00 USD | 10,220.00 USD |
| `7D` | `3639.80` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 47,920.00 USD | 0.00 USD | 8,910.00 USD |
| `1D` | `3643.30` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 24,860.00 USD | 0.00 USD | 7,950.00 USD |
| `7D` | `3644.00` | 15,300,000.00 USD | 0.00 USD | 15,300,000.00 USD | 25,630.00 USD | 0.00 USD | 10,600.00 USD |
| `1D` | `3647.50` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 18,580.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3648.20` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 24,860.00 USD | 0.00 USD | 6,570.00 USD |
| `1D` | `3651.70` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 26,300.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `3652.40` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 18,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 13,340.00 USD | 0.00 USD | 4,100.00 USD |
| `7D` | `3656.60` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `3660.10` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 10,130.00 USD | 0.00 USD | 1,600.00 USD |
| `7D` | `3660.80` | 15,170,000.00 USD | 0.00 USD | 15,170,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `1D` | `3664.30` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 6,340.00 USD | 0.00 USD | 1,580.00 USD |
| `7D` | `3665.00` | 15,160,000.00 USD | 0.00 USD | 15,160,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3672.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3833.00` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3837.20` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 212,590.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3841.40` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 511,020.00 USD | 0.00 USD | 37,200.00 USD |
| `7D` | `3845.60` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 378,790.00 USD | 0.00 USD | 74,850.00 USD |
| `7D` | `3849.80` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 406,600.00 USD | 0.00 USD | 73,620.00 USD |
| `7D` | `3854.00` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 166,740.00 USD | 0.00 USD | 20,210.00 USD |
| `7D` | `3858.20` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 219,930.00 USD | 0.00 USD | 16,570.00 USD |
| `1D` | `3861.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 7,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3862.40` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 181,990.00 USD | 0.00 USD | 30,210.00 USD |
| `1D` | `3865.90` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 87,120.00 USD | 0.00 USD | 10,460.00 USD |
| `7D` | `3866.60` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 370,400.00 USD | 0.00 USD | 54,540.00 USD |
| `1D` | `3870.10` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 158,170.00 USD | 0.00 USD | 20,070.00 USD |
| `7D` | `3870.80` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 558,420.00 USD | 0.00 USD | 47,190.00 USD |
| `1D` | `3874.30` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 83,140.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `3875.00` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 384,590.00 USD | 0.00 USD | 39,460.00 USD |
| `1D` | `3878.50` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 220,680.00 USD | 0.00 USD | 13,860.00 USD |
| `7D` | `3879.20` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 376,000.00 USD | 0.00 USD | 87,620.00 USD |
| `1D` | `3882.70` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 134,600.00 USD | 0.00 USD | 35,150.00 USD |
| `7D` | `3883.40` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 178,610.00 USD | 0.00 USD | 43,720.00 USD |
| `1D` | `3886.90` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 86,350.00 USD | 0.00 USD | 12,910.00 USD |
| `7D` | `3887.60` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 72,000.00 USD | 0.00 USD | 24,180.00 USD |
| `1D` | `3891.10` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 73,750.00 USD | 0.00 USD | 13,590.00 USD |
| `7D` | `3891.80` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 120,010.00 USD | 0.00 USD | 17,560.00 USD |
| `1D` | `3895.30` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 80,250.00 USD | 0.00 USD | 8,470.00 USD |
| `7D` | `3896.00` | 10,420,000.00 USD | 0.00 USD | 10,420,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `3899.50` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 49,800.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `3900.20` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3903.70` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 51,610.00 USD | 0.00 USD | 3,390.00 USD |
| `7D` | `3904.40` | 10,200,000.00 USD | 0.00 USD | 10,200,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `1D` | `3907.90` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 20,800.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3908.60` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `3912.80` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3916.30` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3917.00` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 389,720.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3921.20` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 992,680.00 USD | 0.00 USD | 67,550.00 USD |
| `7D` | `3925.40` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 636,890.00 USD | 0.00 USD | 143,480.00 USD |
| `7D` | `3929.60` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 907,960.00 USD | 0.00 USD | 164,280.00 USD |
| `7D` | `3933.80` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 424,200.00 USD | 0.00 USD | 40,420.00 USD |
| `7D` | `3938.00` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 422,750.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3941.50` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 15,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3942.20` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 254,740.00 USD | 0.00 USD | 42,630.00 USD |
| `1D` | `3945.70` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 174,240.00 USD | 0.00 USD | 17,620.00 USD |
| `7D` | `3946.40` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 654,020.00 USD | 0.00 USD | 126,570.00 USD |
| `1D` | `3949.90` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 254,010.00 USD | 0.00 USD | 36,250.00 USD |
| `7D` | `3950.60` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 1,080,000.00 USD | 0.00 USD | 70,830.00 USD |
| `1D` | `3954.10` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 207,790.00 USD | 0.00 USD | 26,960.00 USD |
| `7D` | `3954.80` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 808,000.00 USD | 0.00 USD | 83,480.00 USD |
| `1D` | `3958.30` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 345,090.00 USD | 0.00 USD | 21,970.00 USD |
| `7D` | `3959.00` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 920,340.00 USD | 0.00 USD | 200,680.00 USD |
| `1D` | `3962.50` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 361,130.00 USD | 0.00 USD | 60,080.00 USD |
| `7D` | `3963.20` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `3966.70` | 901,920.00 USD | 0.00 USD | 901,920.00 USD | 194,640.00 USD | 0.00 USD | 37,490.00 USD |
| `7D` | `3967.40` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `1D` | `3970.90` | 669,790.00 USD | 0.00 USD | 669,790.00 USD | 55,620.00 USD | 0.00 USD | 36,650.00 USD |
| `7D` | `3971.60` | 993,340.00 USD | 0.00 USD | 993,340.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `1D` | `3975.10` | 577,510.00 USD | 0.00 USD | 577,510.00 USD | 243,510.00 USD | 0.00 USD | 18,130.00 USD |
| `7D` | `3975.80` | 746,380.00 USD | 0.00 USD | 746,380.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD |
| `1D` | `3979.30` | 315,870.00 USD | 0.00 USD | 315,870.00 USD | 83,910.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `3980.00` | 477,160.00 USD | 0.00 USD | 477,160.00 USD | 232,530.00 USD | 0.00 USD | 16,750.00 USD |
| `1D` | `3983.50` | 213,340.00 USD | 0.00 USD | 213,340.00 USD | 120,150.00 USD | 0.00 USD | 10,580.00 USD |
| `7D` | `3984.20` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 34,110.00 USD | 0.00 USD | 26,160.00 USD |
| `1D` | `3987.70` | 82,620.00 USD | 0.00 USD | 82,620.00 USD | 52,470.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3988.40` | 167,600.00 USD | 0.00 USD | 167,600.00 USD | 113,270.00 USD | 0.00 USD | 21,240.00 USD |
| `7D` | `3992.60` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3996.10` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `4000.30` | 15,300.00 USD | 0.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4029.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4030.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4072.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4076.60` | 421,480.00 USD | 421,480.00 USD | 0.00 USD | 389,720.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `4080.80` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 669,010.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `4085.00` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `4089.20` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 908,780.00 USD | 0.00 USD | 122,920.00 USD |
| `7D` | `4093.40` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 267,370.00 USD | 0.00 USD | 86,340.00 USD |
| `7D` | `4097.60` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 516,580.00 USD | 0.00 USD | 37,450.00 USD |
| `7D` | `4101.80` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 238,850.00 USD | 0.00 USD | 26,840.00 USD |
| `1D` | `4105.30` | 148,100.00 USD | 148,100.00 USD | 0.00 USD | 143,100.00 USD | 0.00 USD | 5,010.00 USD |
| `7D` | `4106.00` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 540,860.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4109.50` | 352,360.00 USD | 352,360.00 USD | 0.00 USD | 170,600.00 USD | 0.00 USD | 33,660.00 USD |
| `7D` | `4110.20` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 63,920.00 USD |
| `1D` | `4113.70` | 664,330.00 USD | 664,330.00 USD | 0.00 USD | 281,450.00 USD | 0.00 USD | 30,510.00 USD |
| `7D` | `4114.40` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 707,700.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4117.90` | 822,170.00 USD | 822,170.00 USD | 0.00 USD | 136,130.00 USD | 0.00 USD | 21,720.00 USD |
| `7D` | `4118.60` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 793,490.00 USD | 0.00 USD | 157,720.00 USD |
| `1D` | `4122.10` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 457,960.00 USD | 0.00 USD | 47,820.00 USD |
| `7D` | `4122.80` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 119,150.00 USD |
| `1D` | `4126.30` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 231,470.00 USD | 0.00 USD | 51,440.00 USD |
| `7D` | `4127.00` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 165,710.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4130.50` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 134,870.00 USD | 0.00 USD | 32,860.00 USD |
| `7D` | `4131.20` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 174,770.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4134.70` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 155,080.00 USD | 0.00 USD | 16,200.00 USD |
| `7D` | `4135.40` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 14,640.00 USD |
| `1D` | `4138.90` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 152,920.00 USD | 0.00 USD | 15,930.00 USD |
| `7D` | `4139.60` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4143.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 99,610.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `4143.80` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.30` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 97,320.00 USD | 0.00 USD | 6,780.00 USD |
| `7D` | `4148.00` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4151.50` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4152.20` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 87,550.00 USD | 0.00 USD | 18,110.00 USD |
| `7D` | `4156.40` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 203,340.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `4159.90` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4160.60` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 290,090.00 USD | 0.00 USD | 31,340.00 USD |
| `7D` | `4164.80` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 478,890.00 USD | 0.00 USD | 56,730.00 USD |
| `7D` | `4169.00` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 481,630.00 USD | 0.00 USD | 60,700.00 USD |
| `7D` | `4173.20` | 11,880,000.00 USD | 11,880,000.00 USD | 0.00 USD | 153,670.00 USD | 0.00 USD | 49,520.00 USD |
| `7D` | `4177.40` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 258,290.00 USD | 0.00 USD | 20,630.00 USD |
| `7D` | `4181.60` | 12,280,000.00 USD | 12,280,000.00 USD | 0.00 USD | 110,570.00 USD | 0.00 USD | 11,250.00 USD |
| `1D` | `4185.10` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 37,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4185.80` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 212,310.00 USD | 0.00 USD | 43,190.00 USD |
| `1D` | `4189.30` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 111,590.00 USD | 0.00 USD | 16,010.00 USD |
| `7D` | `4190.00` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 451,780.00 USD | 0.00 USD | 41,860.00 USD |
| `1D` | `4193.50` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 107,300.00 USD | 0.00 USD | 18,580.00 USD |
| `7D` | `4194.20` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 429,400.00 USD | 0.00 USD | 41,140.00 USD |
| `1D` | `4197.70` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 94,950.00 USD | 0.00 USD | 9,740.00 USD |
| `7D` | `4198.40` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 475,650.00 USD | 0.00 USD | 71,090.00 USD |
| `1D` | `4201.90` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 206,890.00 USD | 0.00 USD | 13,130.00 USD |
| `7D` | `4202.60` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 279,630.00 USD | 0.00 USD | 55,990.00 USD |
| `1D` | `4206.10` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 133,400.00 USD | 0.00 USD | 33,320.00 USD |
| `7D` | `4206.80` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 153,500.00 USD | 0.00 USD | 43,720.00 USD |
| `1D` | `4210.30` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 86,350.00 USD | 0.00 USD | 12,840.00 USD |
| `7D` | `4211.00` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 21,770.00 USD |
| `1D` | `4214.50` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 54,900.00 USD | 0.00 USD | 15,260.00 USD |
| `7D` | `4215.20` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `1D` | `4218.70` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4219.40` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `4222.90` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 41,960.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `4223.60` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `4227.10` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 49,400.00 USD | 0.00 USD | 5,290.00 USD |
| `7D` | `4227.80` | 15,050,000.00 USD | 15,050,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 10,770.00 USD |
| `1D` | `4231.30` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 21,060.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4232.00` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 50,070.00 USD | 0.00 USD | 12,930.00 USD |
| `1D` | `4235.50` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4236.20` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4239.70` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `4243.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.80` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `7D` | `4400.00` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 92,310.00 USD | 0.00 USD | 7,150.00 USD |
| `7D` | `4404.20` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 130,400.00 USD | 0.00 USD | 19,150.00 USD |
| `7D` | `4408.40` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 142,360.00 USD | 0.00 USD | 19,620.00 USD |
| `7D` | `4412.60` | 15,690,000.00 USD | 15,690,000.00 USD | 0.00 USD | 50,960.00 USD | 0.00 USD | 19,240.00 USD |
| `7D` | `4416.80` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 2,420.00 USD |
| `7D` | `4421.00` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 62,350.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `4424.50` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 3,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4425.20` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 40,820.00 USD | 0.00 USD | 5,730.00 USD |
| `1D` | `4428.70` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 25,930.00 USD | 0.00 USD | 3,150.00 USD |
| `7D` | `4429.40` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 70,130.00 USD | 0.00 USD | 19,660.00 USD |
| `1D` | `4432.90` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 25,170.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4433.60` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 188,760.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `4437.10` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 30,580.00 USD | 0.00 USD | 3,950.00 USD |
| `7D` | `4437.80` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 82,170.00 USD | 0.00 USD | 10,330.00 USD |
| `1D` | `4441.30` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 24,550.00 USD | 0.00 USD | 3,290.00 USD |
| `7D` | `4442.00` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 114,900.00 USD | 0.00 USD | 22,150.00 USD |
| `1D` | `4445.10` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 53,030.00 USD | 0.00 USD | 5,550.00 USD |
| `7D` | `4446.20` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 48,670.00 USD | 0.00 USD | 17,810.00 USD |
| `7D` | `4450.40` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 33,140.00 USD | 0.00 USD | 9,540.00 USD |
| `7D` | `4453.60` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 17,720.00 USD | 0.00 USD | 2,550.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.70M` | Total OI Tokens: `68,477.9 PAXG`
  * 1h OI Change: `-0.04%` | 4h OI Change: `+0.08%` | 24h OI Change: `+0.46%`
  * Exchange Breakdown: Binance=`107.02M` | Bybit=`20.12M` | OKX=`-` | Hyperliquid=`25.76M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.45K` | Last 24h: `26.74K` | Last 3d: `98.64K` | Last 7d: `223.27K`
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
| `15M` | `PAXG` | `44.96%` | `55.04%` | `0.82` | 1,470,000.00 USD |
| `15M` | `Binance` | `49.52%` | `50.48%` | `0.98` | 536,290.00 USD |
| `15M` | `OKX` | `47.69%` | `52.31%` | `0.91` | 122,500.00 USD |
| `15M` | `Bybit` | `43.35%` | `56.65%` | `0.77` | 233,190.00 USD |
| `15M` | `KuCoin` | `48.36%` | `51.64%` | `0.94` | 178,060.00 USD |
| `15M` | `Gate` | `50.5%` | `49.5%` | `1.02` | 18,950.00 USD |
| `15M` | `Bitget` | `20.61%` | `79.39%` | `0.26` | 130,430.00 USD |
| `15M` | `BingX` | `41.84%` | `58.16%` | `0.72` | 37,790.00 USD |
| `15M` | `MEXC` | `39.37%` | `60.63%` | `0.65` | 34,170.00 USD |
| `15M` | `Bitunix` | `53.69%` | `46.31%` | `1.16` | 16,480.00 USD |
| `15M` | `Hyperliquid` | `43.89%` | `56.11%` | `0.78` | 6,060.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.48%` | `54.52%` | `0.83` | 62,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `68.92%` | `31.08%` | `2.22` | 66,490.00 USD |
| `15M` | `HTX` | `66.67%` | `33.33%` | `2.00` | 0.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 30,870.00 USD |
| `15M` | `Aster` | `7.99%` | `92.01%` | `0.09` | 22.18 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.27%` | `41.73%` | `1.40` | 108.10 USD |
| `15M` | `Whale Positions` | `49.52%` | `50.48%` | `0.98` | 536,290.00 USD |
| `15M` | `Global Accounts` | `44.96%` | `55.04%` | `0.82` | 1,470,000.00 USD |
| `1H` | `PAXG` | `52.18%` | `47.82%` | `1.09` | 11,250,000.00 USD |
| `1H` | `Binance` | `53.1%` | `46.9%` | `1.13` | 2,690,000.00 USD |
| `1H` | `OKX` | `49.65%` | `50.35%` | `0.99` | 1,020,000.00 USD |
| `1H` | `Bybit` | `39.39%` | `60.61%` | `0.65` | 889,930.00 USD |
| `1H` | `KuCoin` | `48.96%` | `51.04%` | `0.96` | 95,750.00 USD |
| `1H` | `Gate` | `49.33%` | `50.67%` | `0.97` | 1,700,000.00 USD |
| `1H` | `Bitget` | `45.38%` | `54.62%` | `0.83` | 193,780.00 USD |
| `1H` | `BingX` | `42.1%` | `57.9%` | `0.73` | 2,780,000.00 USD |
| `1H` | `MEXC` | `42.68%` | `57.32%` | `0.74` | 122,440.00 USD |
| `1H` | `Bitunix` | `57.06%` | `42.94%` | `1.33` | 218,930.00 USD |
| `1H` | `Hyperliquid` | `25.46%` | `74.54%` | `0.34` | 54,970.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.77%` | `49.23%` | `1.03` | 339,120.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `96.69%` | `3.31%` | `29.21` | 1,100,000.00 USD |
| `1H` | `HTX` | `67.14%` | `32.86%` | `2.04` | 27,550.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `11.91%` | `88.09%` | `0.14` | 26,300.00 USD |
| `1H` | `Aster` | `59.36%` | `40.64%` | `1.46` | 16,350.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `63.79%` | `36.21%` | `1.76` | 154.68 USD |
| `1H` | `Whale Positions` | `53.1%` | `46.9%` | `1.13` | 2,690,000.00 USD |
| `1H` | `Global Accounts` | `52.18%` | `47.82%` | `1.09` | 11,250,000.00 USD |
| `4H` | `PAXG` | `48.64%` | `51.36%` | `0.95` | 41,040,000.00 USD |
| `4H` | `Binance` | `54.63%` | `45.37%` | `1.20` | 13,490,000.00 USD |
| `4H` | `OKX` | `51.62%` | `48.38%` | `1.07` | 8,470,000.00 USD |
| `4H` | `Bybit` | `50.34%` | `49.66%` | `1.01` | 2,040,000.00 USD |
| `4H` | `KuCoin` | `50.34%` | `49.66%` | `1.01` | 2,360,000.00 USD |
| `4H` | `Gate` | `49.54%` | `50.46%` | `0.98` | 706,210.00 USD |
| `4H` | `Bitget` | `51.92%` | `48.08%` | `1.08` | 945,370.00 USD |
| `4H` | `BingX` | `45.9%` | `54.1%` | `0.85` | 1,390,000.00 USD |
| `4H` | `MEXC` | `51.39%` | `48.61%` | `1.06` | 325,960.00 USD |
| `4H` | `Bitunix` | `44.81%` | `55.19%` | `0.81` | 1,240,000.00 USD |
| `4H` | `Hyperliquid` | `79.7%` | `20.3%` | `3.93` | 444,800.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.03%` | `48.97%` | `1.04` | 6,070,000.00 USD |
| `4H` | `Crypto.com` | `55%` | `45%` | `1.22` | 55.91 USD |
| `4H` | `WhiteBIT` | `0.04%` | `99.96%` | `0.00` | 3,160,000.00 USD |
| `4H` | `HTX` | `48.11%` | `51.89%` | `0.93` | 35,940.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `96.05%` | `3.95%` | `24.32` | 291,820.00 USD |
| `4H` | `Aster` | `84.32%` | `15.68%` | `5.38` | 55,050.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.74%` | `51.26%` | `0.95` | 22,090.00 USD |
| `4H` | `Whale Positions` | `54.63%` | `45.37%` | `1.20` | 13,490,000.00 USD |
| `4H` | `Global Accounts` | `48.64%` | `51.36%` | `0.95` | 41,040,000.00 USD |


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
| `5m` | -19,770.00 USD | -33,280.00 USD | **`DISTRIBUTION`** |
| `15m` | -31,550.00 USD | 67,640.00 USD | **`ACCUMULATION`** |
| `30m` | -30,130.00 USD | -45,780.00 USD | **`DISTRIBUTION`** |
| `1h` | -178,400.00 USD | 319,420.00 USD | **`ACCUMULATION`** |
| `2h` | -301,020.00 USD | 466,160.00 USD | **`ACCUMULATION`** |
| `4h` | -457,930.00 USD | 823,280.00 USD | **`ACCUMULATION`** |
| `6h` | -564,000.00 USD | 598,440.00 USD | **`ACCUMULATION`** |
| `8h` | -478,340.00 USD | -324,140.00 USD | **`DISTRIBUTION`** |
| `12h` | -293,870.00 USD | -142,950.00 USD | **`DISTRIBUTION`** |
| `24h` | -622,470.00 USD | 111,170.00 USD | **`DISTRIBUTION`** |
| `1w` | -10,890,000.00 USD | -10,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,360,000.00 USD | -74,010,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-19.77K` | 15m=`-31.55K` | 1h=`-178.40K` | 24h=`-622.47K`
* Futures Capital Netflows: 5m=`-33.28K` | 15m=`+67.64K` | 1h=`+319.42K` | 24h=`+111.17K`
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
  * Spread-Padded Stop Loss: `4008.32` (Risk Distance: `11.50` pts)
  * +2.5R Take Profit: `4048.57`
  * Mathematical Lot Sizing: **`0.86 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4052.21` (Risk Distance: `11.50` pts)
  * +2.5R Take Profit: `4011.96`
  * Mathematical Lot Sizing: **`0.86 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4050.55`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
