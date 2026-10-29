# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 00:29:18 IST` (`2026-10-29 18:59:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4011.20` | **Live Ask Quote**: `4011.29` | **Mid Price**: `4011.24`
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
  * Session VWAP: `4030.36` | VWAP Z-Score: `-1.78` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.41` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.88` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4065.57` | Lower -3.00σ Band: `3995.16`
  * Upper +2.51σ Band: `4059.82` | Lower -2.51σ Band: `4000.91`
  * Upper +2.01σ Band: `4053.95` | Lower -2.01σ Band: `4006.77`
  * Upper +2.00σ Band: `4053.83` | Lower -2.00σ Band: `4006.89`
  * Upper +1.28σ Band: `4045.38` | Lower -1.28σ Band: `4015.34`
  * Upper +1.00σ Band: `4042.10` | Lower -1.00σ Band: `4018.63`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4012.72` | EMA-20=`4017.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4024.43` (Slope: `+0.0000`) | EMA-100=`4031.08`
  * Institutional Anchors: EMA-144=`4032.51` | EMA-200=`4032.23` (Slope: `-0.0561`) | EMA-233=`4031.26`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.53` (Distance: `-0.72%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.40%`)
  * Value Area Low (VAL) = `4017.10` (Distance: `-0.15%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.72` | Weekly POC=`4015.46` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3995.20` - `4027.29`
  * Optimal Trade Entry (OTE 0.705): `4019.27`
  * Structural Invalidation Anchor (0.786): `4043.33`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4013.82` | `4014.55` | `4013.08` | `4014.55` | `18` | 72,633.51 USD | 46,920.86 USD | `+64.60%` | 1,604,832.37 USD | `+0.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4014.54` | `4016.10` | `4013.57` | `4016.09` | `68` | 274,973.34 USD | 232,222.19 USD | `+84.45%` | 1,837,054.56 USD | `+1.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4016.09` | `4017.00` | `4015.57` | `4016.98` | `44` | 178,429.41 USD | 116,509.80 USD | `+65.30%` | 1,953,564.36 USD | `+0.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4016.60` | `4016.99` | `4011.83` | `4011.89` | `126` | 503,906.61 USD | 129,664.92 USD | `+25.73%` | 1,488,168.37 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4011.89` | `4014.70` | `4011.01` | `4014.55` | `71` | 283,231.27 USD | 115,122.48 USD | `+40.65%` | 1,603,290.84 USD | `+0.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4014.54` | `4017.00` | `4013.57` | `4016.98` | `113` | 453,402.75 USD | 348,731.99 USD | `+76.91%` | 1,952,022.84 USD | `+1.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 1,062,379.10 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 852,087.28 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4017.00` | `4011.01` | `4016.98` | `492` | 1,975,844.77 USD | 1,099,935.56 USD | `+55.67%` | 1,952,022.84 USD | `+1.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4016.98` | `1,992` | 8,005,887.91 USD | 1,740,057.95 USD | `+21.73%` | 2,117,108.23 USD | `+1.84` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4016.98` | `1,992` | 8,005,887.91 USD | 1,740,057.95 USD | `+21.73%` | 2,117,108.23 USD | `+1.84` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4010.30` | `7.4808` | 30,000.25 USD | 1,625,128.94 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4010.40` | `19.8153` | 79,467.28 USD | 1,595,128.69 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `4010.50` | `15.6522` | 62,773.15 USD | 1,515,661.41 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `4010.60` | `8.9779` | 36,006.77 USD | 1,452,888.26 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4010.70` | `7.4782` | 29,992.82 USD | 1,416,881.49 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4010.80` | `6.0440` | 24,241.28 USD | 1,386,888.68 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4010.90` | `120.9249` | 485,017.68 USD | 1,362,647.40 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4011.00` | `0.7581` | 3,040.74 USD | 877,629.72 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4011.10` | `13.1675` | 52,816.16 USD | 874,588.98 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4011.20` | `0.1173` | 470.51 USD | 821,772.82 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4011.30` | `5.5989` | 22,458.87 USD | 821,302.31 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4011.40` | `58.7296` | 235,587.92 USD | 798,843.44 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4011.50` | `18.1994` | 73,006.89 USD | 563,255.52 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4011.70` | `10.0823` | 40,447.16 USD | 490,248.63 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4011.80` | `36.5456` | 146,613.64 USD | 449,801.47 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4011.90` | `1.8558` | 7,445.28 USD | 303,187.83 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4012.00` | `25.8720` | 103,798.46 USD | 295,742.55 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4012.10` | `23.9079` | 95,920.89 USD | 191,944.08 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4012.20` | `7.7261` | 30,998.66 USD | 96,023.20 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `4012.30` | `16.2063` | 65,024.54 USD | 65,024.54 USD | `9 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4012.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,012.35` | `0.00%` | `-` |
| `ASK` | `4012.40` | `17.7082` | 71,052.38 USD | 71,052.38 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `4012.60` | `7.4769` | 30,001.81 USD | 101,054.19 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4012.70` | `17.5546` | 70,441.34 USD | 171,495.53 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4012.80` | `18.7240` | 75,135.67 USD | 246,631.20 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4012.90` | `27.3580` | 109,784.92 USD | 356,416.12 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4013.00` | `65.6445` | 263,431.38 USD | 619,847.50 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `4013.10` | `3.3657` | 13,506.89 USD | 633,354.39 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4013.20` | `14.3683` | 57,662.86 USD | 691,017.25 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4013.30` | `11.7615` | 47,202.43 USD | 738,219.68 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `4013.40` | `20.9354` | 84,022.13 USD | 822,241.81 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4013.50` | `33.8527` | 135,867.81 USD | 958,109.62 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4013.60` | `15.6940` | 62,989.44 USD | 1,021,099.06 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4013.70` | `5.9361` | 23,825.72 USD | 1,044,924.79 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4013.80` | `12.9431` | 51,951.01 USD | 1,096,875.80 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4013.90` | `8.6539` | 34,735.89 USD | 1,131,611.69 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4014.00` | `14.7708` | 59,289.99 USD | 1,190,901.68 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4014.10` | `57.6933` | 231,586.68 USD | 1,422,488.36 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4014.20` | `6.2516` | 25,095.17 USD | 1,447,583.53 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4014.30` | `8.6614` | 34,769.46 USD | 1,482,352.99 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4014.40` | `0.4522` | 1,815.31 USD | 1,484,168.30 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,576,168.68 USD | `6,373.65` | `4191.43` | `4012.80` | `29181.84` | 1,138,580.52 USD | `+4.45%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,359,751.09 USD | `6,319.56` | `4133.88` | `4012.80` | `13294.26` | 764,591.35 USD | `+3.01%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,940,844.25 USD | `5,717.06` | `4234.49` | `4012.80` | `27494.25` | 1,268,030.97 USD | `+5.53%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,377,920.50 USD | `4,828.91` | `4157.43` | `4012.80` | `2084.98` | -697,961.82 USD | `-3.60%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,111,639.20 USD | `3,516.66` | `4129.63` | `4012.80` | `304.95` | -410,871.67 USD | `-2.91%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,114,685.93 USD | `3,268.21` | `4228.94` | `4012.80` | `4409.83` | 706,393.20 USD | `+5.39%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,637,410.40 USD | `2,900.00` | `4364.92` | `4012.80` | `4235.59` | 1,020,865.93 USD | `+8.77%` | `20X Cross` |
| `276` | `0x3678...b209` | `LONG` | 8,828,160.00 USD | `2,200.00` | `4176.09` | `4012.80` | `2451.98` | -359,259.30 USD | `-4.07%` | `25X Cross` |
| `277` | `0x41e5...0825` | `SHORT` | 8,827,940.00 USD | `2,200.00` | `4112.20` | `4012.80` | `4331.08` | 218,914.59 USD | `+2.48%` | `20X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,972,990.59 USD | `1,986.89` | `4032.86` | `4012.80` | `25065.82` | 39,875.58 USD | `+0.50%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,926,958.66 USD | `1,975.37` | `4048.55` | `4012.80` | `6499.57` | 70,433.05 USD | `+0.89%` | `6X Cross` |
| `382` | `0xc26c...b8f4` | `LONG` | 6,340,030.58 USD | `1,579.95` | `4075.62` | `4012.80` | `0.000000` | -99,266.39 USD | `-1.57%` | `1X Cross` |
| `421` | `0x12d2...f97f` | `LONG` | 5,625,856.26 USD | `1,401.94` | `4278.91` | `4012.80` | `2497.95` | -372,934.32 USD | `-6.63%` | `20X Cross` |
| `578` | `0x63da...8add` | `LONG` | 4,012,800.00 USD | `1,000.00` | `4021.46` | `4012.80` | `3564.03` | -8,660.96 USD | `-0.22%` | `25X Cross` |
| `597` | `0x9aa5...58af` | `LONG` | 3,899,102.18 USD | `971.64` | `4279.98` | `4012.80` | `0.000000` | -259,506.90 USD | `-6.66%` | `20X Cross` |
| `626` | `0xf3dc...1672` | `LONG` | 3,734,702.17 USD | `930.74` | `4024.62` | `4012.80` | `3337.51` | -11,190.39 USD | `-0.30%` | `20X Cross` |
| `690` | `0x4a20...3c26` | `LONG` | 3,360,317.52 USD | `837.40` | `4599.73` | `4012.80` | `0.000000` | -491,502.87 USD | `-14.63%` | `20X Cross` |
| `769` | `0x354b...6425` | `LONG` | 3,071,122.53 USD | `765.31` | `4035.10` | `4012.80` | `0.000000` | -16,990.45 USD | `-0.55%` | `10X Cross` |
| `849` | `0x0fac...7a0a` | `LONG` | 2,754,795.66 USD | `686.49` | `4290.34` | `4012.80` | `1248.48` | -190,463.05 USD | `-6.91%` | `25X Cross` |
| `889` | `0xd8c5...99b0` | `SHORT` | 2,577,641.74 USD | `642.35` | `4175.35` | `4012.80` | `32047.83` | 104,419.44 USD | `+4.05%` | `4X Cross` |
| `921` | `0x625e...a354` | `SHORT` | 2,487,874.00 USD | `620.00` | `4122.81` | `4012.80` | `4342.18` | 68,273.03 USD | `+2.74%` | `20X Cross` |
| `950` | `0xeae3...e8ad` | `SHORT` | 2,407,560.00 USD | `600.00` | `4104.77` | `4012.80` | `4325.20` | 55,305.11 USD | `+2.30%` | `20X Cross` |
| `952` | `0xf285...fa82` | `LONG` | 2,400,139.17 USD | `598.11` | `4146.45` | `4012.80` | `3891.17` | -79,880.39 USD | `-3.33%` | `25X Cross` |
| `969` | `0x12f7...8750` | `LONG` | 2,349,938.62 USD | `585.61` | `4082.77` | `4012.80` | `2155.86` | -40,978.36 USD | `-1.74%` | `10X Cross` |
| `1132` | `0x413c...886c` | `LONG` | 2,006,350.00 USD | `500.00` | `4010.43` | `4012.80` | `0.000000` | 1,133.77 USD | `+0.06%` | `2X Cross` |
| `1141` | `0x61ce...a62b` | `SHORT` | 1,996,282.54 USD | `497.50` | `4071.66` | `4012.80` | `4690.69` | 29,386.25 USD | `+1.47%` | `20X Cross` |
| `1147` | `0x0593...40f9` | `LONG` | 1,991,059.07 USD | `496.18` | `4024.57` | `4012.80` | `3701.65` | -5,844.76 USD | `-0.29%` | `10X Isolated` |
| `1259` | `0x2edd...8179` | `LONG` | 1,821,967.55 USD | `453.58` | `4169.95` | `4017.30` | `0.000000` | -69,456.57 USD | `-3.81%` | `10X Cross` |
| `1260` | `0xead5...69f2` | `LONG` | 1,820,989.41 USD | `453.78` | `4220.88` | `4012.80` | `3538.86` | -94,378.65 USD | `-5.18%` | `5X Isolated` |
| `1322` | `0x7a6d...f79c` | `SHORT` | 1,720,746.61 USD | `428.38` | `4136.09` | `4017.30` | `5887.73` | 51,068.40 USD | `+2.97%` | `10X Cross` |
| `1386` | `0x46fc...1195` | `LONG` | 1,633,242.56 USD | `407.03` | `4055.53` | `4012.80` | `1926.50` | -17,477.26 USD | `-1.07%` | `20X Cross` |
| `1424` | `0xee02...309d` | `SHORT` | 1,605,160.00 USD | `400.00` | `4438.84` | `4012.80` | `4226.81` | 170,378.60 USD | `+10.61%` | `25X Isolated` |
| `1425` | `0x6d15...d374` | `LONG` | 1,605,080.00 USD | `400.00` | `4068.25` | `4012.80` | `3841.73` | -22,220.00 USD | `-1.38%` | `25X Cross` |
| `1453` | `0x02a7...fe9f` | `SHORT` | 1,564,992.00 USD | `390.00` | `4055.02` | `4012.80` | `4306.63` | 16,467.25 USD | `+1.05%` | `25X Cross` |
| `1486` | `0x51f6...2b39` | `LONG` | 1,528,366.22 USD | `380.49` | `4234.66` | `4017.30` | `0.000000` | -82,861.84 USD | `-5.42%` | `10X Cross` |
| `1489` | `0x7e77...b8d2` | `SHORT` | 1,524,864.00 USD | `380.00` | `4131.92` | `4012.80` | `4293.44` | 45,265.64 USD | `+2.97%` | `20X Cross` |
| `1505` | `0x72c2...9b37` | `LONG` | 1,497,226.65 USD | `373.13` | `4000.98` | `4012.80` | `3777.97` | 4,333.14 USD | `+0.29%` | `13X Isolated` |
| `1543` | `0xaa44...b844` | `LONG` | 1,444,536.00 USD | `360.00` | `4043.10` | `4012.80` | `2818.87` | -10,981.63 USD | `-0.76%` | `9X Cross` |
| `1545` | `0x781e...96b7` | `SHORT` | 1,444,252.31 USD | `359.55` | `4365.03` | `4017.30` | `12620.70` | 125,195.18 USD | `+8.67%` | `10X Cross` |
| `1655` | `0xa41f...d50a` | `LONG` | 1,320,092.01 USD | `328.96` | `4468.89` | `4012.80` | `3833.11` | -150,005.84 USD | `-11.36%` | `15X Cross` |
| `1685` | `0x49e9...e1d0` | `SHORT` | 1,298,403.09 USD | `323.56` | `4025.23` | `4012.80` | `28135.71` | 3,989.61 USD | `+0.31%` | `4X Cross` |
| `1712` | `0xada6...6f88` | `LONG` | 1,281,125.27 USD | `319.28` | `4166.46` | `4012.80` | `1868.52` | -49,125.24 USD | `-3.83%` | `5X Cross` |
| `1718` | `0xbf5a...88ba` | `SHORT` | 1,274,717.35 USD | `317.65` | `4091.80` | `4012.80` | `10497.37` | 25,065.68 USD | `+1.97%` | `20X Cross` |
| `1734` | `0xff31...ff6c` | `SHORT` | 1,243,968.00 USD | `310.00` | `4372.43` | `4012.80` | `4789.11` | 111,487.38 USD | `+8.96%` | `10X Isolated` |
| `1900` | `0x50e2...d770` | `LONG` | 1,084,930.30 USD | `270.37` | `4243.58` | `4012.80` | `2562.02` | -62,396.16 USD | `-5.75%` | `20X Cross` |
| `1913` | `0x4c92...4f17` | `SHORT` | 1,070,296.02 USD | `266.72` | `4260.98` | `4012.80` | `6524.92` | 66,196.21 USD | `+6.18%` | `20X Cross` |
| `1989` | `0xd346...c4f3` | `LONG` | 1,023,986.94 USD | `255.17` | `4188.66` | `4012.80` | `3310.35` | -44,849.57 USD | `-4.38%` | `5X Isolated` |
| `2028` | `0x1581...463b` | `LONG` | 1,003,175.00 USD | `250.00` | `4003.77` | `4012.80` | `3504.56` | 2,231.41 USD | `+0.22%` | `15X Cross` |
| `2029` | `0xe47f...758c` | `LONG` | 1,003,175.00 USD | `250.00` | `4020.00` | `4012.80` | `3774.26` | -1,825.00 USD | `-0.18%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.01` (Vol: 250,500.00 USD, Dist: `+2.41%`) | Long MP=`3949.20` (Vol: 281,800.00 USD, Dist: `--1.59%`)
  * 48H Horizon: Short MP=`4110.01` (Vol: 250,500.00 USD, Dist: `+2.41%`) | Long MP=`3949.20` (Vol: 281,800.00 USD, Dist: `--1.59%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.39%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--0.84%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.60%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.48%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.20` | 16,560,000.00 USD | 16,560,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.30` | 3,880,000.00 USD | 3,880,000.00 USD | 2,900.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,480,000.00 USD | 16,480,000.00 USD | 121,270.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.50` | 3,880,000.00 USD | 3,880,000.00 USD | 18,530.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,350,000.00 USD | 16,350,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3620.70` | 3,860,000.00 USD | 3,860,000.00 USD | 24,000.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,290,000.00 USD | 16,290,000.00 USD | 105,540.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.90` | 3,830,000.00 USD | 3,830,000.00 USD | 43,990.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,170,000.00 USD | 16,170,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.10` | 3,780,000.00 USD | 3,780,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,970,000.00 USD | 15,970,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.30` | 3,740,000.00 USD | 3,740,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,840,000.00 USD | 15,840,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.50` | 3,720,000.00 USD | 3,720,000.00 USD | 62,140.00 USD | 0.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,710,000.00 USD | 15,710,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3641.70` | 3,650,000.00 USD | 3,650,000.00 USD | 10,510.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,650,000.00 USD | 15,650,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.90` | 3,630,000.00 USD | 3,630,000.00 USD | 14,480.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,620,000.00 USD | 15,620,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.10` | 3,610,000.00 USD | 3,610,000.00 USD | 28,880.00 USD | 0.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,600,000.00 USD | 15,600,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3654.30` | 3,580,000.00 USD | 3,580,000.00 USD | 11,860.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3658.50` | 3,560,000.00 USD | 3,560,000.00 USD | 8,050.00 USD | 0.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,540,000.00 USD | 15,540,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3662.70` | 3,550,000.00 USD | 3,550,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,530,000.00 USD | 15,530,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,510,000.00 USD | 15,510,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.10` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,500,000.00 USD | 15,500,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 15,080,000.00 USD | 15,080,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,550,000.00 USD | 14,550,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3851.70` | 3,550,000.00 USD | 3,550,000.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 14,000,000.00 USD | 14,000,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.90` | 3,540,000.00 USD | 3,540,000.00 USD | 48,970.00 USD | 0.00 USD | 6,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,710,000.00 USD | 13,710,000.00 USD | 349,400.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.10` | 3,490,000.00 USD | 3,490,000.00 USD | 50,400.00 USD | 0.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,340,000.00 USD | 13,340,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.30` | 3,430,000.00 USD | 3,430,000.00 USD | 146,200.00 USD | 0.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,150,000.00 USD | 13,150,000.00 USD | 325,660.00 USD | 0.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,270,000.00 USD | 3,270,000.00 USD | 104,800.00 USD | 0.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,770,000.00 USD | 12,770,000.00 USD | 622,200.00 USD | 0.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.70` | 3,140,000.00 USD | 3,140,000.00 USD | 126,980.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,100,000.00 USD | 12,100,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.90` | 3,000,000.00 USD | 3,000,000.00 USD | 105,540.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,720,000.00 USD | 11,720,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.10` | 2,890,000.00 USD | 2,890,000.00 USD | 145,550.00 USD | 0.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,140,000.00 USD | 11,140,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.30` | 2,710,000.00 USD | 2,710,000.00 USD | 41,920.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,920,000.00 USD | 10,920,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.50` | 2,660,000.00 USD | 2,660,000.00 USD | 36,210.00 USD | 0.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,830,000.00 USD | 10,830,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.70` | 2,610,000.00 USD | 2,610,000.00 USD | 104,820.00 USD | 0.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,700,000.00 USD | 10,700,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.90` | 2,500,000.00 USD | 2,500,000.00 USD | 41,960.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,570,000.00 USD | 10,570,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.10` | 2,450,000.00 USD | 2,450,000.00 USD | 30,100.00 USD | 0.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,450,000.00 USD | 10,450,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.30` | 2,410,000.00 USD | 2,410,000.00 USD | 34,240.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,400,000.00 USD | 10,400,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,350,000.00 USD | 10,350,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3914.70` | 2,370,000.00 USD | 2,370,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,330,000.00 USD | 10,330,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,960,000.00 USD | 9,960,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,180,000.00 USD | 9,180,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,140,000.00 USD | 8,140,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,030,000.00 USD | 7,030,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3935.70` | 2,360,000.00 USD | 2,360,000.00 USD | 103,550.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,530,000.00 USD | 6,530,000.00 USD | 604,960.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.90` | 2,250,000.00 USD | 2,250,000.00 USD | 46,950.00 USD | 0.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,890,000.00 USD | 5,890,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.10` | 2,190,000.00 USD | 2,190,000.00 USD | 235,600.00 USD | 0.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,440,000.00 USD | 5,440,000.00 USD | 676,110.00 USD | 0.00 USD | 142,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3948.30` | 1,940,000.00 USD | 1,940,000.00 USD | 249,040.00 USD | 0.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.50` | 1,640,000.00 USD | 1,640,000.00 USD | 295,830.00 USD | 0.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3956.70` | 1,310,000.00 USD | 1,310,000.00 USD | 137,160.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.90` | 1,150,000.00 USD | 1,150,000.00 USD | 378,510.00 USD | 0.00 USD | 47,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.10` | 728,170.00 USD | 728,170.00 USD | 79,800.00 USD | 0.00 USD | 35,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.30` | 612,790.00 USD | 612,790.00 USD | 51,240.00 USD | 0.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.50` | 529,650.00 USD | 529,650.00 USD | 182,860.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3977.70` | 340,180.00 USD | 340,180.00 USD | 103,850.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.90` | 229,120.00 USD | 229,120.00 USD | 67,730.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.10` | 138,980.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3990.30` | 63,870.00 USD | 63,870.00 USD | 41,610.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3998.70` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4095.30` | 68,750.00 USD | 68,750.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,320,000.00 USD | 4,320,000.00 USD | 698,790.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.50` | 170,120.00 USD | 170,120.00 USD | 94,620.00 USD | 0.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,610,000.00 USD | 4,610,000.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4103.70` | 321,830.00 USD | 321,830.00 USD | 138,670.00 USD | 0.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,390,000.00 USD | 5,390,000.00 USD | 678,320.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.90` | 596,320.00 USD | 596,320.00 USD | 234,740.00 USD | 0.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,510,000.00 USD | 6,510,000.00 USD | 1,040,000.00 USD | 0.00 USD | 73,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.10` | 937,650.00 USD | 937,650.00 USD | 303,570.00 USD | 0.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,410,000.00 USD | 7,410,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4116.30` | 1,140,000.00 USD | 1,140,000.00 USD | 173,010.00 USD | 0.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,290,000.00 USD | 8,290,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.50` | 1,440,000.00 USD | 1,440,000.00 USD | 283,380.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 9,010,000.00 USD | 9,010,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4124.70` | 1,680,000.00 USD | 1,680,000.00 USD | 187,000.00 USD | 0.00 USD | 54,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,260,000.00 USD | 9,260,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4128.90` | 1,810,000.00 USD | 1,810,000.00 USD | 106,820.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,460,000.00 USD | 9,460,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.10` | 1,900,000.00 USD | 1,900,000.00 USD | 57,990.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,690,000.00 USD | 9,690,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.30` | 2,100,000.00 USD | 2,100,000.00 USD | 192,710.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,940,000.00 USD | 9,940,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.50` | 2,190,000.00 USD | 2,190,000.00 USD | 83,910.00 USD | 0.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,110,000.00 USD | 10,110,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.70` | 2,260,000.00 USD | 2,260,000.00 USD | 54,840.00 USD | 0.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,210,000.00 USD | 10,210,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.90` | 2,310,000.00 USD | 2,310,000.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,300,000.00 USD | 10,300,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4154.10` | 2,340,000.00 USD | 2,340,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,680,000.00 USD | 10,680,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.30` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,110,000.00 USD | 11,110,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.50` | 2,360,000.00 USD | 2,360,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,560,000.00 USD | 11,560,000.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 12,000,000.00 USD | 12,000,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,240,000.00 USD | 12,240,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4175.10` | 2,400,000.00 USD | 2,400,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,530,000.00 USD | 12,530,000.00 USD | 281,520.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4179.30` | 2,430,000.00 USD | 2,430,000.00 USD | 33,170.00 USD | 0.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,710,000.00 USD | 12,710,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.50` | 2,510,000.00 USD | 2,510,000.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 13,090,000.00 USD | 13,090,000.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4187.70` | 2,650,000.00 USD | 2,650,000.00 USD | 122,010.00 USD | 0.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,740,000.00 USD | 13,740,000.00 USD | 607,230.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.90` | 2,800,000.00 USD | 2,800,000.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 14,090,000.00 USD | 14,090,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.10` | 2,920,000.00 USD | 2,920,000.00 USD | 102,820.00 USD | 0.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.30` | 3,030,000.00 USD | 3,030,000.00 USD | 102,180.00 USD | 0.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,590,000.00 USD | 14,590,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.50` | 3,200,000.00 USD | 3,200,000.00 USD | 139,240.00 USD | 0.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,850,000.00 USD | 14,850,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.70` | 3,240,000.00 USD | 3,240,000.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,970,000.00 USD | 14,970,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,300,000.00 USD | 3,300,000.00 USD | 46,160.00 USD | 0.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 15,080,000.00 USD | 15,080,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.10` | 3,380,000.00 USD | 3,380,000.00 USD | 73,870.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,200,000.00 USD | 15,200,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.30` | 3,430,000.00 USD | 3,430,000.00 USD | 48,960.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,310,000.00 USD | 15,310,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.50` | 3,480,000.00 USD | 3,480,000.00 USD | 33,860.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,390,000.00 USD | 15,390,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.70` | 3,510,000.00 USD | 3,510,000.00 USD | 33,610.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,440,000.00 USD | 15,440,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4233.90` | 3,540,000.00 USD | 3,540,000.00 USD | 20,800.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,480,000.00 USD | 15,480,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,500,000.00 USD | 15,500,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4242.30` | 3,550,000.00 USD | 3,550,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,640,000.00 USD | 15,640,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,780,000.00 USD | 15,780,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,920,000.00 USD | 15,920,000.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 16,040,000.00 USD | 16,040,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.50` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 16,100,000.00 USD | 16,100,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.70` | 3,570,000.00 USD | 3,570,000.00 USD | 17,690.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,200,000.00 USD | 16,200,000.00 USD | 90,410.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.90` | 3,580,000.00 USD | 3,580,000.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,240,000.00 USD | 16,240,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.10` | 3,620,000.00 USD | 3,620,000.00 USD | 30,000.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,340,000.00 USD | 16,340,000.00 USD | 79,630.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4431.30` | 3,650,000.00 USD | 3,650,000.00 USD | 29,610.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,510,000.00 USD | 16,510,000.00 USD | 157,240.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.70` | 3,670,000.00 USD | 3,670,000.00 USD | 18,430.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,620,000.00 USD | 16,620,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,750,000.00 USD | 16,750,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,830,000.00 USD | 16,830,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,870,000.00 USD | 16,870,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,560,000.00 USD | 0.00 USD | 16,560,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.30` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 2,900.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `3615.50` | 16,480,000.00 USD | 0.00 USD | 16,480,000.00 USD | 121,270.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.50` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 23,950.00 USD | 0.00 USD | 2,510.00 USD |
| `7D` | `3619.80` | 16,350,000.00 USD | 0.00 USD | 16,350,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3620.70` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 24,000.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `3624.10` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 105,540.00 USD | 0.00 USD | 21,190.00 USD |
| `1D` | `3624.90` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 43,990.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `3628.40` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.10` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD |
| `7D` | `3632.70` | 15,970,000.00 USD | 0.00 USD | 15,970,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3633.30` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,840,000.00 USD | 0.00 USD | 15,840,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.50` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 52,230.00 USD | 0.00 USD | 7,500.00 USD |
| `7D` | `3641.30` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3641.70` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD |
| `7D` | `3645.60` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3645.90` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 14,480.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `3649.90` | 15,620,000.00 USD | 0.00 USD | 15,620,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.10` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 28,880.00 USD | 0.00 USD | 2,300.00 USD |
| `7D` | `3654.20` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3654.30` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 11,860.00 USD | 0.00 USD | 1,900.00 USD |
| `1D` | `3658.50` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 8,050.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `3658.50` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3662.70` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3667.10` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.10` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD |
| `1D` | `3851.70` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3852.00` | 14,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3855.90` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 62,530.00 USD | 0.00 USD | 6,910.00 USD |
| `7D` | `3856.30` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 349,400.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3860.10` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 50,400.00 USD | 0.00 USD | 6,530.00 USD |
| `7D` | `3860.60` | 13,340,000.00 USD | 0.00 USD | 13,340,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3864.30` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 146,200.00 USD | 0.00 USD | 12,280.00 USD |
| `7D` | `3864.90` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 325,660.00 USD | 0.00 USD | 59,280.00 USD |
| `1D` | `3868.50` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 104,800.00 USD | 0.00 USD | 22,340.00 USD |
| `7D` | `3869.20` | 12,770,000.00 USD | 0.00 USD | 12,770,000.00 USD | 622,200.00 USD | 0.00 USD | 41,850.00 USD |
| `1D` | `3872.70` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 126,980.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3873.50` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3876.90` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 105,540.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3877.80` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3881.10` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 120,770.00 USD | 0.00 USD | 25,220.00 USD |
| `7D` | `3882.10` | 11,140,000.00 USD | 0.00 USD | 11,140,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3885.30` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3886.40` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3889.50` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 36,210.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3890.70` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3893.70` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 104,820.00 USD | 0.00 USD | 6,900.00 USD |
| `7D` | `3895.00` | 10,700,000.00 USD | 0.00 USD | 10,700,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3897.90` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 32,580.00 USD | 0.00 USD | 5,700.00 USD |
| `7D` | `3899.30` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3902.10` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 30,100.00 USD | 0.00 USD | 5,510.00 USD |
| `7D` | `3903.60` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3906.30` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 34,240.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3914.70` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3935.70` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 604,960.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3939.90` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 46,950.00 USD | 0.00 USD | 10,440.00 USD |
| `7D` | `3942.30` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.10` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 235,600.00 USD | 0.00 USD | 12,510.00 USD |
| `7D` | `3946.60` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 676,110.00 USD | 0.00 USD | 142,130.00 USD |
| `1D` | `3948.30` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 249,040.00 USD | 0.00 USD | 51,250.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3952.50` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 295,830.00 USD | 0.00 USD | 36,370.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3956.70` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 137,160.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3960.90` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 328,950.00 USD | 0.00 USD | 47,410.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.10` | 668,840.00 USD | 0.00 USD | 668,840.00 USD | 79,800.00 USD | 0.00 USD | 26,360.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.30` | 562,680.00 USD | 0.00 USD | 562,680.00 USD | 31,350.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.50` | 510,890.00 USD | 0.00 USD | 510,890.00 USD | 182,860.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3977.70` | 321,420.00 USD | 0.00 USD | 321,420.00 USD | 103,850.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3981.90` | 210,360.00 USD | 0.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3986.10` | 138,980.00 USD | 0.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3990.30` | 63,870.00 USD | 0.00 USD | 63,870.00 USD | 41,610.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3998.70` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4016.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4017.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4095.30` | 68,750.00 USD | 68,750.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 698,790.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4099.50` | 197,260.00 USD | 197,260.00 USD | 0.00 USD | 121,750.00 USD | 0.00 USD | 6,760.00 USD |
| `7D` | `4101.40` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4103.70` | 348,960.00 USD | 348,960.00 USD | 0.00 USD | 138,670.00 USD | 0.00 USD | 13,030.00 USD |
| `7D` | `4105.70` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 678,320.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4107.90` | 623,450.00 USD | 623,450.00 USD | 0.00 USD | 234,740.00 USD | 0.00 USD | 39,750.00 USD |
| `7D` | `4110.00` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 73,030.00 USD |
| `1D` | `4112.10` | 964,780.00 USD | 964,780.00 USD | 0.00 USD | 303,570.00 USD | 0.00 USD | 37,760.00 USD |
| `7D` | `4114.30` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4116.30` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 173,010.00 USD | 0.00 USD | 28,640.00 USD |
| `7D` | `4118.60` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4120.50` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 283,380.00 USD | 0.00 USD | 19,770.00 USD |
| `7D` | `4122.90` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4124.70` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | 44,940.00 USD |
| `7D` | `4127.20` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4128.90` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `4131.50` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.10` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `4135.80` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.30` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 192,710.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.50` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 11,410.00 USD |
| `7D` | `4144.40` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4145.70` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 54,840.00 USD | 0.00 USD | 11,010.00 USD |
| `7D` | `4148.70` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.90` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4154.10` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.30` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.50` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4175.10` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `4178.80` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 281,520.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4179.30` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 46,740.00 USD | 0.00 USD | 5,240.00 USD |
| `7D` | `4183.10` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4183.50` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD |
| `7D` | `4187.40` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD |
| `1D` | `4187.70` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 17,020.00 USD |
| `7D` | `4191.70` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 607,230.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4191.90` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `4196.00` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4196.10` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 102,820.00 USD | 0.00 USD | 15,140.00 USD |
| `1D` | `4200.30` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 102,180.00 USD | 0.00 USD | 8,020.00 USD |
| `7D` | `4200.30` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4204.50` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 114,460.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `4204.60` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4208.70` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `4208.90` | 14,970,000.00 USD | 14,970,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4212.90` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 36,210.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4213.20` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4217.10` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 73,870.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4217.50` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4221.30` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 48,960.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4221.80` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4225.50` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 24,480.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `4226.10` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4229.70` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 33,610.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `4230.40` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4233.90` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 20,800.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4234.70` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4242.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4389.50` | 15,500,000.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `1D` | `4414.50` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `4415.30` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4418.70` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4419.60` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 90,410.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4422.90` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `4423.90` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4427.10` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `4428.20` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 79,630.00 USD | 0.00 USD | 18,160.00 USD |
| `1D` | `4431.30` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 29,610.00 USD | 0.00 USD | 7,540.00 USD |
| `7D` | `4432.50` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 157,240.00 USD | 0.00 USD | 11,860.00 USD |
| `1D` | `4433.70` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 18,430.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `4436.80` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,870,000.00 USD | 16,870,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.56M` | Total OI Tokens: `68,337.5 PAXG`
  * 1h OI Change: `+0.40%` | 4h OI Change: `-0.51%` | 24h OI Change: `-0.07%`
  * Exchange Breakdown: Binance=`107.28M` | Bybit=`19.99M` | OKX=`-` | Hyperliquid=`25.05M`
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
| `15M` | `PAXG` | `70.95%` | `29.05%` | `2.44` | 1,860,000.00 USD |
| `15M` | `Binance` | `72.06%` | `27.94%` | `2.58` | 136,540.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `57.76%` | `42.24%` | `1.37` | 241,510.00 USD |
| `15M` | `KuCoin` | `64.56%` | `35.44%` | `1.82` | 1,980.00 USD |
| `15M` | `Gate` | `49.7%` | `50.3%` | `0.99` | 72,010.00 USD |
| `15M` | `Bitget` | `64.43%` | `35.57%` | `1.81` | 65,820.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `82.44%` | `17.56%` | `4.69` | 1,030,000.00 USD |
| `15M` | `Bitunix` | `85.7%` | `14.3%` | `5.99` | 28,680.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.76%` | `49.24%` | `1.03` | 159,700.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `40.32%` | `59.68%` | `0.68` | 111,400.00 USD |
| `15M` | `HTX` | `31.33%` | `68.67%` | `0.46` | 332.69 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 8,010.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `72.06%` | `27.94%` | `2.58` | 136,540.00 USD |
| `15M` | `Global Accounts` | `70.95%` | `29.05%` | `2.44` | 1,860,000.00 USD |
| `1H` | `PAXG` | `52.71%` | `47.29%` | `1.11` | 9,770,000.00 USD |
| `1H` | `Binance` | `52.01%` | `47.99%` | `1.08` | 3,710,000.00 USD |
| `1H` | `OKX` | `51.55%` | `48.45%` | `1.06` | 1,760,000.00 USD |
| `1H` | `Bybit` | `52.82%` | `47.18%` | `1.12` | 868,410.00 USD |
| `1H` | `KuCoin` | `51.64%` | `48.36%` | `1.07` | 113,210.00 USD |
| `1H` | `Gate` | `42.54%` | `57.46%` | `0.74` | 425,310.00 USD |
| `1H` | `Bitget` | `55.13%` | `44.87%` | `1.23` | 391,070.00 USD |
| `1H` | `BingX` | `47.72%` | `52.28%` | `0.91` | 421,220.00 USD |
| `1H` | `MEXC` | `57.72%` | `42.28%` | `1.37` | 873,730.00 USD |
| `1H` | `Bitunix` | `56.33%` | `43.67%` | `1.29` | 152,820.00 USD |
| `1H` | `Hyperliquid` | `63.89%` | `36.11%` | `1.77` | 140,750.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.33%` | `49.67%` | `1.01` | 502,440.00 USD |
| `1H` | `Crypto.com` | `46.98%` | `53.02%` | `0.89` | 7,870.00 USD |
| `1H` | `WhiteBIT` | `74.82%` | `25.18%` | `2.97` | 308,130.00 USD |
| `1H` | `HTX` | `48.14%` | `51.86%` | `0.93` | 607.65 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `18.4%` | `81.6%` | `0.23` | 50,960.00 USD |
| `1H` | `Aster` | `17.54%` | `82.46%` | `0.21` | 2,850.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.05%` | `49.95%` | `1.00` | 40,150.00 USD |
| `1H` | `Whale Positions` | `52.01%` | `47.99%` | `1.08` | 3,710,000.00 USD |
| `1H` | `Global Accounts` | `52.71%` | `47.29%` | `1.11` | 9,770,000.00 USD |
| `4H` | `PAXG` | `47.58%` | `52.42%` | `0.91` | 52,510,000.00 USD |
| `4H` | `Binance` | `45.99%` | `54.01%` | `0.85` | 19,270,000.00 USD |
| `4H` | `OKX` | `47.24%` | `52.76%` | `0.90` | 10,500,000.00 USD |
| `4H` | `Bybit` | `48.86%` | `51.14%` | `0.96` | 4,180,000.00 USD |
| `4H` | `KuCoin` | `49.95%` | `50.05%` | `1.00` | 510,210.00 USD |
| `4H` | `Gate` | `49.49%` | `50.51%` | `0.98` | 1,550,000.00 USD |
| `4H` | `Bitget` | `49.13%` | `50.87%` | `0.97` | 2,400,000.00 USD |
| `4H` | `BingX` | `34.97%` | `65.03%` | `0.54` | 2,520,000.00 USD |
| `4H` | `MEXC` | `46.36%` | `53.64%` | `0.86` | 4,700,000.00 USD |
| `4H` | `Bitunix` | `50.08%` | `49.92%` | `1.00` | 1,180,000.00 USD |
| `4H` | `Hyperliquid` | `48.6%` | `51.4%` | `0.95` | 1,510,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.51%` | `50.49%` | `0.98` | 2,490,000.00 USD |
| `4H` | `Crypto.com` | `49.61%` | `50.39%` | `0.98` | 28,160.00 USD |
| `4H` | `WhiteBIT` | `84.09%` | `15.91%` | `5.29` | 1,260,000.00 USD |
| `4H` | `HTX` | `47%` | `53%` | `0.89` | 11,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.68%` | `50.32%` | `0.99` | 164,220.00 USD |
| `4H` | `Aster` | `86.45%` | `13.55%` | `6.38` | 54,300.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.31%` | `48.69%` | `1.05` | 147,260.00 USD |
| `4H` | `Whale Positions` | `45.99%` | `54.01%` | `0.85` | 19,270,000.00 USD |
| `4H` | `Global Accounts` | `47.58%` | `52.42%` | `0.91` | 52,510,000.00 USD |


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
| `5m` | -64,930.00 USD | 116,470.00 USD | **`ACCUMULATION`** |
| `15m` | -60,050.00 USD | 400,040.00 USD | **`ACCUMULATION`** |
| `30m` | -44,230.00 USD | 494,250.00 USD | **`ACCUMULATION`** |
| `1h` | -241,090.00 USD | 1,070,000.00 USD | **`ACCUMULATION`** |
| `2h` | -495,910.00 USD | 993,680.00 USD | **`ACCUMULATION`** |
| `4h` | 283,160.00 USD | 1,470,000.00 USD | **`ACCUMULATION`** |
| `6h` | 71,460.00 USD | 1,650,000.00 USD | **`ACCUMULATION`** |
| `8h` | -100,470.00 USD | 2,150,000.00 USD | **`ACCUMULATION`** |
| `12h` | -141,420.00 USD | 1,180,000.00 USD | **`ACCUMULATION`** |
| `24h` | -288,850.00 USD | 1,960,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,570,000.00 USD | -6,970,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,250,000.00 USD | -71,590,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-64.93K` | 15m=`-60.05K` | 1h=`-241.09K` | 24h=`-288.85K`
* Futures Capital Netflows: 5m=`+116.47K` | 15m=`+400.04K` | 1h=`+1.07M` | 24h=`+1.96M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4017.10` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4008.08` (Risk Distance: `9.02` pts)
  * +2.5R Take Profit: `4039.65`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4049.55` (Risk Distance: `9.02` pts)
  * +2.5R Take Profit: `4017.98`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4043.33`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
