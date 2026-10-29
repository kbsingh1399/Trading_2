# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 00:20:14 IST` (`2026-10-29 18:50:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4009.58` | **Live Ask Quote**: `4009.67` | **Mid Price**: `4009.62`
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
  * Value Area High (VAH) = `4040.10` (Distance: `-0.76%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.44%`)
  * Value Area Low (VAL) = `4017.10` (Distance: `-0.19%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `3993.59` - `4025.66`
  * Optimal Trade Entry (OTE 0.705): `4017.64`
  * Structural Invalidation Anchor (0.786): `4041.70`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4012.90` | `4012.91` | `4011.83` | `4011.89` | `19` | 76,519.37 USD | 22,319.64 USD | `+29.17%` | 1,318,568.05 USD | `-0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4011.89` | `4013.21` | `4011.01` | `4012.13` | `15` | 58,924.50 USD | 24,236.52 USD | `+41.13%` | 1,342,804.57 USD | `-0.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4012.12` | `4012.12` | `4011.65` | `4011.65` | `4` | 15,621.53 USD | 11,481.25 USD | `+73.50%` | 1,354,285.81 USD | `-0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4011.95` | `4016.65` | `4011.95` | `4016.65` | `183` | 735,304.15 USD | 506,416.16 USD | `+68.87%` | 1,391,708.86 USD | `+2.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4016.60` | `4016.99` | `4011.83` | `4011.89` | `126` | 503,906.61 USD | 129,664.92 USD | `+25.73%` | 1,521,373.78 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4011.89` | `4013.21` | `4011.01` | `4011.65` | `19` | 74,546.02 USD | 35,717.76 USD | `+47.91%` | 1,557,091.55 USD | `-0.06` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 1,062,379.10 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 852,087.28 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4016.99` | `4011.01` | `4011.65` | `327` | 1,313,756.78 USD | 671,798.85 USD | `+51.14%` | 1,523,886.13 USD | `+1.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4011.65` | `1,827` | 7,343,799.91 USD | 1,311,921.25 USD | `+17.86%` | 1,688,971.52 USD | `+1.64` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4014.55` | `1,879` | 7,552,697.93 USD | 1,391,482.53 USD | `+18.42%` | 1,768,532.80 USD | `+1.68` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4007.50` | `145.4167` | 582,757.43 USD | 2,436,890.13 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `4007.60` | `1.6733` | 6,705.92 USD | 1,854,132.70 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4007.70` | `0.0550` | 220.42 USD | 1,847,426.78 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4007.80` | `9.3672` | 37,541.86 USD | 1,847,206.36 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4007.90` | `11.7406` | 47,055.15 USD | 1,809,664.50 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4008.00` | `31.6292` | 126,769.83 USD | 1,762,609.34 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4008.10` | `4.4682` | 17,908.99 USD | 1,635,839.51 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4008.20` | `6.9281` | 27,769.21 USD | 1,617,930.52 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4008.30` | `8.2224` | 32,957.85 USD | 1,590,161.31 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4008.40` | `1.6691` | 6,690.42 USD | 1,557,203.46 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4008.50` | `0.0498` | 199.62 USD | 1,550,513.04 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4008.60` | `2.2499` | 9,018.95 USD | 1,550,313.42 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4008.70` | `3.8912` | 15,598.65 USD | 1,541,294.47 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4008.80` | `73.9095` | 296,288.40 USD | 1,525,695.82 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `4008.90` | `25.7472` | 103,217.95 USD | 1,229,407.41 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `4009.00` | `2.2073` | 8,849.07 USD | 1,126,189.46 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4009.10` | `3.4928` | 14,002.98 USD | 1,117,340.40 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4009.20` | `30.8914` | 123,849.80 USD | 1,103,337.41 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4009.30` | `7.9011` | 31,677.88 USD | 979,487.61 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `4009.40` | `236.3969` | 947,809.73 USD | 947,809.73 USD | `35 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4009.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,009.45` | `0.00%` | `-` |
| `ASK` | `4009.50` | `42.2899` | 169,561.35 USD | 169,561.35 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `4009.60` | `13.4848` | 54,068.65 USD | 223,630.01 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `4009.70` | `1.3382` | 5,365.78 USD | 228,995.79 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4009.80` | `14.1010` | 56,542.19 USD | 285,537.98 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4010.10` | `12.9062` | 51,755.15 USD | 337,293.13 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4010.20` | `29.3112` | 117,543.77 USD | 454,836.91 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4010.30` | `4.4345` | 17,783.68 USD | 472,620.58 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4010.40` | `8.3952` | 33,668.11 USD | 506,288.69 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4010.50` | `3.7401` | 14,999.67 USD | 521,288.36 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4010.60` | `3.3839` | 13,571.47 USD | 534,859.83 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4010.70` | `9.1452` | 36,678.65 USD | 571,538.48 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4010.80` | `23.8283` | 95,570.55 USD | 667,109.03 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4010.90` | `0.1315` | 527.43 USD | 667,636.46 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4011.00` | `1.2982` | 5,207.08 USD | 672,843.54 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4011.10` | `6.0373` | 24,216.21 USD | 697,059.76 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4011.20` | `62.2887` | 249,852.43 USD | 946,912.19 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4011.30` | `4.9882` | 20,009.17 USD | 966,921.36 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4011.40` | `6.2808` | 25,194.80 USD | 992,116.16 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4011.50` | `10.9380` | 43,877.79 USD | 1,035,993.95 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4011.60` | `17.9211` | 71,892.28 USD | 1,107,886.23 USD | `5 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,552,586.18 USD | `6,373.65` | `4191.43` | `4009.00` | `29544.49` | 1,162,163.02 USD | `+4.55%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,336,264.37 USD | `6,319.69` | `4133.88` | `4009.00` | `13325.32` | 788,622.09 USD | `+3.11%` | `5X Cross` |
| `72` | `0xb83d...6e36` | `SHORT` | 22,924,836.49 USD | `5,717.06` | `4234.49` | `4009.00` | `27766.78` | 1,284,038.74 USD | `+5.60%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,359,087.76 USD | `4,828.91` | `4157.43` | `4009.00` | `2101.93` | -716,794.55 USD | `-3.70%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,098,617.55 USD | `3,516.65` | `4129.63` | `4009.00` | `312.65` | -423,883.29 USD | `-3.01%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,102,593.54 USD | `3,268.21` | `4228.94` | `4009.00` | `4409.94` | 718,485.59 USD | `+5.48%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,626,390.40 USD | `2,900.00` | `4364.92` | `4009.00` | `4235.59` | 1,031,885.93 USD | `+8.88%` | `20X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,821,780.00 USD | `2,200.00` | `4112.20` | `4009.00` | `4331.08` | 225,074.59 USD | `+2.55%` | `20X Cross` |
| `277` | `0x3678...b209` | `LONG` | 8,819,800.00 USD | `2,200.00` | `4176.09` | `4009.00` | `2455.26` | -367,619.30 USD | `-4.17%` | `25X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,964,645.65 USD | `1,986.89` | `4032.86` | `4009.00` | `25147.40` | 48,220.52 USD | `+0.61%` | `3X Cross` |
| `310` | `0xacb6...efbd` | `SHORT` | 7,920,835.02 USD | `1,975.37` | `4048.55` | `4009.00` | `6508.72` | 76,556.70 USD | `+0.97%` | `6X Cross` |
| `382` | `0xc26c...b8f4` | `LONG` | 6,334,184.76 USD | `1,579.95` | `4075.62` | `4009.00` | `0.000000` | -105,112.21 USD | `-1.66%` | `1X Cross` |
| `419` | `0x12d2...f97f` | `LONG` | 5,621,510.24 USD | `1,401.94` | `4278.91` | `4009.00` | `2549.66` | -377,280.34 USD | `-6.71%` | `20X Cross` |
| `575` | `0x63da...8add` | `LONG` | 4,009,100.00 USD | `1,000.00` | `4021.46` | `4009.00` | `3564.03` | -12,360.96 USD | `-0.31%` | `25X Cross` |
| `597` | `0x9aa5...58af` | `LONG` | 3,895,312.78 USD | `971.64` | `4279.98` | `4009.00` | `0.000000` | -263,296.31 USD | `-6.76%` | `20X Cross` |
| `624` | `0xf3dc...1672` | `LONG` | 3,732,096.09 USD | `930.74` | `4024.62` | `4009.00` | `3337.51` | -13,796.47 USD | `-0.37%` | `20X Cross` |
| `688` | `0x4a20...3c26` | `LONG` | 3,357,889.06 USD | `837.40` | `4599.73` | `4009.00` | `0.000000` | -493,931.32 USD | `-14.71%` | `20X Cross` |
| `769` | `0x354b...6425` | `LONG` | 3,067,831.69 USD | `765.31` | `4035.10` | `4009.00` | `0.000000` | -20,281.29 USD | `-0.66%` | `10X Cross` |
| `846` | `0x0fac...7a0a` | `LONG` | 2,752,187.01 USD | `686.49` | `4290.34` | `4009.00` | `1232.86` | -193,071.69 USD | `-7.02%` | `25X Cross` |
| `880` | `0xd8c5...99b0` | `SHORT` | 2,594,200.39 USD | `646.95` | `4175.35` | `4009.00` | `31919.80` | 107,042.37 USD | `+4.13%` | `4X Cross` |
| `921` | `0x625e...a354` | `SHORT` | 2,486,138.00 USD | `620.00` | `4122.81` | `4009.00` | `4342.18` | 70,009.03 USD | `+2.82%` | `20X Cross` |
| `949` | `0xeae3...e8ad` | `SHORT` | 2,405,400.00 USD | `600.00` | `4104.77` | `4009.00` | `4325.20` | 57,465.11 USD | `+2.39%` | `20X Cross` |
| `952` | `0xf285...fa82` | `LONG` | 2,397,866.36 USD | `598.11` | `4146.45` | `4009.00` | `3891.17` | -82,153.19 USD | `-3.43%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,347,771.86 USD | `585.61` | `4082.77` | `4009.00` | `2208.07` | -43,145.12 USD | `-1.84%` | `10X Cross` |
| `1129` | `0x413c...886c` | `LONG` | 2,005,000.00 USD | `500.00` | `4010.43` | `4009.00` | `0.000000` | -216.23 USD | `-0.01%` | `2X Cross` |
| `1138` | `0x61ce...a62b` | `SHORT` | 1,994,392.03 USD | `497.50` | `4071.66` | `4009.00` | `4692.09` | 31,276.76 USD | `+1.57%` | `20X Cross` |
| `1143` | `0x0593...40f9` | `LONG` | 1,989,173.59 USD | `496.18` | `4024.57` | `4009.00` | `3701.65` | -7,730.24 USD | `-0.39%` | `10X Isolated` |
| `1252` | `0x2edd...8179` | `LONG` | 1,824,958.52 USD | `454.70` | `4169.95` | `4013.40` | `0.000000` | -71,140.12 USD | `-3.90%` | `10X Cross` |
| `1253` | `0xead5...69f2` | `LONG` | 1,819,628.06 USD | `453.78` | `4220.88` | `4009.00` | `3538.86` | -95,740.00 USD | `-5.26%` | `5X Isolated` |
| `1318` | `0x7a6d...f79c` | `SHORT` | 1,719,513.31 USD | `428.38` | `4136.09` | `4013.40` | `5917.07` | 52,301.70 USD | `+3.04%` | `10X Cross` |
| `1381` | `0x46fc...1195` | `LONG` | 1,631,695.85 USD | `407.03` | `4055.53` | `4009.00` | `1931.23` | -19,023.97 USD | `-1.17%` | `20X Cross` |
| `1422` | `0x6d15...d374` | `LONG` | 1,603,960.00 USD | `400.00` | `4068.25` | `4009.00` | `3841.73` | -23,340.00 USD | `-1.46%` | `25X Cross` |
| `1423` | `0xee02...309d` | `SHORT` | 1,603,640.00 USD | `400.00` | `4438.84` | `4009.00` | `4226.81` | 171,898.60 USD | `+10.72%` | `25X Isolated` |
| `1448` | `0x02a7...fe9f` | `SHORT` | 1,563,549.00 USD | `390.00` | `4055.02` | `4009.00` | `4306.63` | 17,910.25 USD | `+1.15%` | `25X Cross` |
| `1482` | `0x51f6...2b39` | `LONG` | 1,527,346.90 USD | `380.49` | `4234.66` | `4013.40` | `0.000000` | -83,881.16 USD | `-5.49%` | `10X Cross` |
| `1487` | `0x7e77...b8d2` | `SHORT` | 1,523,420.00 USD | `380.00` | `4131.92` | `4009.00` | `4293.44` | 46,709.64 USD | `+3.07%` | `20X Cross` |
| `1504` | `0x72c2...9b37` | `LONG` | 1,495,808.76 USD | `373.13` | `4000.98` | `4009.00` | `3777.97` | 2,915.24 USD | `+0.19%` | `13X Isolated` |
| `1541` | `0xaa44...b844` | `LONG` | 1,443,168.00 USD | `360.00` | `4043.10` | `4009.00` | `2818.92` | -12,349.63 USD | `-0.86%` | `9X Cross` |
| `1543` | `0x781e...96b7` | `SHORT` | 1,442,946.06 USD | `359.55` | `4365.03` | `4013.40` | `12759.05` | 126,501.42 USD | `+8.77%` | `10X Cross` |
| `1653` | `0xa41f...d50a` | `LONG` | 1,318,809.06 USD | `328.96` | `4468.89` | `4009.00` | `3833.11` | -151,288.79 USD | `-11.47%` | `15X Cross` |
| `1684` | `0x49e9...e1d0` | `SHORT` | 1,297,173.57 USD | `323.56` | `4025.23` | `4009.00` | `28360.60` | 5,219.13 USD | `+0.40%` | `4X Cross` |
| `1710` | `0xada6...6f88` | `LONG` | 1,280,199.37 USD | `319.28` | `4166.46` | `4009.00` | `1877.24` | -50,051.14 USD | `-3.91%` | `5X Cross` |
| `1719` | `0xbf5a...88ba` | `SHORT` | 1,273,510.26 USD | `317.65` | `4091.80` | `4009.00` | `10472.55` | 26,272.77 USD | `+2.06%` | `20X Cross` |
| `1736` | `0xff31...ff6c` | `SHORT` | 1,243,069.00 USD | `310.00` | `4372.43` | `4009.00` | `4789.11` | 112,386.38 USD | `+9.04%` | `10X Isolated` |
| `1900` | `0x50e2...d770` | `LONG` | 1,083,902.91 USD | `270.37` | `4243.58` | `4009.00` | `2562.02` | -63,423.55 USD | `-5.85%` | `20X Cross` |
| `1916` | `0x4c92...4f17` | `SHORT` | 1,069,282.48 USD | `266.72` | `4260.98` | `4009.00` | `6520.58` | 67,209.75 USD | `+6.29%` | `20X Cross` |
| `1988` | `0xd346...c4f3` | `LONG` | 1,023,017.28 USD | `255.17` | `4188.66` | `4009.00` | `3310.35` | -45,819.23 USD | `-4.48%` | `5X Isolated` |
| `2028` | `0xe47f...758c` | `LONG` | 1,002,500.00 USD | `250.00` | `4020.00` | `4009.00` | `3774.26` | -2,500.00 USD | `-0.25%` | `20X Cross` |
| `2029` | `0x1581...463b` | `LONG` | 1,002,475.00 USD | `250.00` | `4003.77` | `4009.00` | `3504.56` | 1,531.41 USD | `+0.15%` | `15X Cross` |

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
| `7D` | `Long Liquidation` | `3611.20` | 16,490,000.00 USD | 16,490,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.30` | 4,010,000.00 USD | 4,010,000.00 USD | 2,900.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,410,000.00 USD | 16,410,000.00 USD | 107,600.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.50` | 4,000,000.00 USD | 4,000,000.00 USD | 13,270.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,300,000.00 USD | 16,300,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3620.70` | 3,990,000.00 USD | 3,990,000.00 USD | 24,000.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,240,000.00 USD | 16,240,000.00 USD | 105,540.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.90` | 3,960,000.00 USD | 3,960,000.00 USD | 43,990.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,120,000.00 USD | 16,120,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.10` | 3,910,000.00 USD | 3,910,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,920,000.00 USD | 15,920,000.00 USD | 117,280.00 USD | 0.00 USD | 15,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.30` | 3,870,000.00 USD | 3,870,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,790,000.00 USD | 15,790,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.50` | 3,850,000.00 USD | 3,850,000.00 USD | 62,140.00 USD | 0.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,660,000.00 USD | 15,660,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3641.70` | 3,780,000.00 USD | 3,780,000.00 USD | 10,510.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,590,000.00 USD | 15,590,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.90` | 3,760,000.00 USD | 3,760,000.00 USD | 14,480.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,560,000.00 USD | 15,560,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.10` | 3,740,000.00 USD | 3,740,000.00 USD | 34,870.00 USD | 0.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,540,000.00 USD | 15,540,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3654.30` | 3,700,000.00 USD | 3,700,000.00 USD | 11,860.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3658.50` | 3,690,000.00 USD | 3,690,000.00 USD | 13,420.00 USD | 0.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,480,000.00 USD | 15,480,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3662.70` | 3,670,000.00 USD | 3,670,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,470,000.00 USD | 15,470,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,450,000.00 USD | 15,450,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.10` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,440,000.00 USD | 15,440,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 15,020,000.00 USD | 15,020,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,500,000.00 USD | 14,500,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3851.70` | 3,660,000.00 USD | 3,660,000.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,940,000.00 USD | 13,940,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.90` | 3,660,000.00 USD | 3,660,000.00 USD | 35,820.00 USD | 0.00 USD | 6,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,660,000.00 USD | 13,660,000.00 USD | 315,230.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.10` | 3,620,000.00 USD | 3,620,000.00 USD | 50,400.00 USD | 0.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,320,000.00 USD | 13,320,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.30` | 3,560,000.00 USD | 3,560,000.00 USD | 146,200.00 USD | 0.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,130,000.00 USD | 13,130,000.00 USD | 325,660.00 USD | 0.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,400,000.00 USD | 3,400,000.00 USD | 104,800.00 USD | 0.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,740,000.00 USD | 12,740,000.00 USD | 622,200.00 USD | 0.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.70` | 3,270,000.00 USD | 3,270,000.00 USD | 126,980.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,080,000.00 USD | 12,080,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.90` | 3,130,000.00 USD | 3,130,000.00 USD | 105,540.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,700,000.00 USD | 11,700,000.00 USD | 529,730.00 USD | 0.00 USD | 70,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.10` | 3,020,000.00 USD | 3,020,000.00 USD | 145,550.00 USD | 0.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,100,000.00 USD | 11,100,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.30` | 2,840,000.00 USD | 2,840,000.00 USD | 41,920.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,880,000.00 USD | 10,880,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.50` | 2,790,000.00 USD | 2,790,000.00 USD | 36,210.00 USD | 0.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,790,000.00 USD | 10,790,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.70` | 2,740,000.00 USD | 2,740,000.00 USD | 127,420.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,660,000.00 USD | 10,660,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.90` | 2,600,000.00 USD | 2,600,000.00 USD | 41,960.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,540,000.00 USD | 10,540,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.10` | 2,550,000.00 USD | 2,550,000.00 USD | 52,070.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,410,000.00 USD | 10,410,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.30` | 2,490,000.00 USD | 2,490,000.00 USD | 34,240.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,370,000.00 USD | 10,370,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,310,000.00 USD | 10,310,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3914.70` | 2,450,000.00 USD | 2,450,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,290,000.00 USD | 10,290,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,920,000.00 USD | 9,920,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,140,000.00 USD | 9,140,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,100,000.00 USD | 8,100,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 6,990,000.00 USD | 6,990,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3935.70` | 2,440,000.00 USD | 2,440,000.00 USD | 77,270.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,490,000.00 USD | 6,490,000.00 USD | 536,620.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.90` | 2,350,000.00 USD | 2,350,000.00 USD | 46,950.00 USD | 0.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,930,000.00 USD | 5,930,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.10` | 2,290,000.00 USD | 2,290,000.00 USD | 235,600.00 USD | 0.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,470,000.00 USD | 5,470,000.00 USD | 676,110.00 USD | 0.00 USD | 142,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3948.30` | 2,040,000.00 USD | 2,040,000.00 USD | 249,040.00 USD | 0.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,650,000.00 USD | 4,650,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.50` | 1,740,000.00 USD | 1,740,000.00 USD | 295,830.00 USD | 0.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,490,000.00 USD | 3,490,000.00 USD | 803,630.00 USD | 0.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3956.70` | 1,410,000.00 USD | 1,410,000.00 USD | 137,160.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.90` | 1,260,000.00 USD | 1,260,000.00 USD | 378,510.00 USD | 0.00 USD | 47,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.10` | 831,350.00 USD | 831,350.00 USD | 79,800.00 USD | 0.00 USD | 35,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.30` | 715,970.00 USD | 715,970.00 USD | 51,240.00 USD | 0.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.50` | 632,820.00 USD | 632,820.00 USD | 198,130.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3977.70` | 428,090.00 USD | 428,090.00 USD | 133,790.00 USD | 0.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.90` | 279,860.00 USD | 279,860.00 USD | 84,830.00 USD | 0.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.10` | 165,830.00 USD | 165,830.00 USD | 94,080.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `4095.30` | 42,460.00 USD | 42,460.00 USD | 29,600.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,260,000.00 USD | 4,260,000.00 USD | 630,450.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.50` | 143,840.00 USD | 143,840.00 USD | 94,620.00 USD | 0.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,540,000.00 USD | 4,540,000.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4103.70` | 295,540.00 USD | 295,540.00 USD | 138,670.00 USD | 0.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,330,000.00 USD | 5,330,000.00 USD | 678,320.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.90` | 570,030.00 USD | 570,030.00 USD | 234,740.00 USD | 0.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,440,000.00 USD | 6,440,000.00 USD | 1,040,000.00 USD | 0.00 USD | 73,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.10` | 911,360.00 USD | 911,360.00 USD | 303,570.00 USD | 0.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4116.30` | 1,110,000.00 USD | 1,110,000.00 USD | 173,010.00 USD | 0.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,250,000.00 USD | 8,250,000.00 USD | 776,800.00 USD | 0.00 USD | 136,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.50` | 1,420,000.00 USD | 1,420,000.00 USD | 283,380.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,980,000.00 USD | 8,980,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4124.70` | 1,660,000.00 USD | 1,660,000.00 USD | 187,000.00 USD | 0.00 USD | 54,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,220,000.00 USD | 9,220,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4128.90` | 1,780,000.00 USD | 1,780,000.00 USD | 106,820.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,420,000.00 USD | 9,420,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.10` | 1,870,000.00 USD | 1,870,000.00 USD | 57,990.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,660,000.00 USD | 9,660,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.30` | 2,120,000.00 USD | 2,120,000.00 USD | 237,910.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,910,000.00 USD | 9,910,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.50` | 2,220,000.00 USD | 2,220,000.00 USD | 83,910.00 USD | 0.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,080,000.00 USD | 10,080,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.70` | 2,340,000.00 USD | 2,340,000.00 USD | 98,800.00 USD | 0.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,170,000.00 USD | 10,170,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.90` | 2,390,000.00 USD | 2,390,000.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,270,000.00 USD | 10,270,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4154.10` | 2,420,000.00 USD | 2,420,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,640,000.00 USD | 10,640,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.30` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,070,000.00 USD | 11,070,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.50` | 2,440,000.00 USD | 2,440,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,520,000.00 USD | 11,520,000.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,960,000.00 USD | 11,960,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,200,000.00 USD | 12,200,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4175.10` | 2,460,000.00 USD | 2,460,000.00 USD | 14,800.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,460,000.00 USD | 12,460,000.00 USD | 247,350.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4179.30` | 2,500,000.00 USD | 2,500,000.00 USD | 33,170.00 USD | 0.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,630,000.00 USD | 12,630,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.50` | 2,580,000.00 USD | 2,580,000.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 13,020,000.00 USD | 13,020,000.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4187.70` | 2,710,000.00 USD | 2,710,000.00 USD | 122,010.00 USD | 0.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,670,000.00 USD | 13,670,000.00 USD | 607,230.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.90` | 2,870,000.00 USD | 2,870,000.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 14,010,000.00 USD | 14,010,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.10` | 2,980,000.00 USD | 2,980,000.00 USD | 102,820.00 USD | 0.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.30` | 3,090,000.00 USD | 3,090,000.00 USD | 102,180.00 USD | 0.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,540,000.00 USD | 14,540,000.00 USD | 459,220.00 USD | 0.00 USD | 62,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.50` | 3,260,000.00 USD | 3,260,000.00 USD | 139,240.00 USD | 0.00 USD | 26,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,790,000.00 USD | 14,790,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.70` | 3,300,000.00 USD | 3,300,000.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,920,000.00 USD | 14,920,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,360,000.00 USD | 3,360,000.00 USD | 46,160.00 USD | 0.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 15,030,000.00 USD | 15,030,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.10` | 3,450,000.00 USD | 3,450,000.00 USD | 81,500.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,140,000.00 USD | 15,140,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.30` | 3,520,000.00 USD | 3,520,000.00 USD | 63,920.00 USD | 0.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,250,000.00 USD | 15,250,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.50` | 3,580,000.00 USD | 3,580,000.00 USD | 42,420.00 USD | 0.00 USD | 14,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,340,000.00 USD | 15,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.70` | 3,630,000.00 USD | 3,630,000.00 USD | 47,040.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,380,000.00 USD | 15,380,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4233.90` | 3,650,000.00 USD | 3,650,000.00 USD | 20,800.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,430,000.00 USD | 15,430,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,440,000.00 USD | 15,440,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4242.30` | 3,660,000.00 USD | 3,660,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,590,000.00 USD | 15,590,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,720,000.00 USD | 15,720,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,870,000.00 USD | 15,870,000.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,980,000.00 USD | 15,980,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.50` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 16,050,000.00 USD | 16,050,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.70` | 3,680,000.00 USD | 3,680,000.00 USD | 12,430.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,130,000.00 USD | 16,130,000.00 USD | 76,740.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.90` | 3,690,000.00 USD | 3,690,000.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,170,000.00 USD | 16,170,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.10` | 3,730,000.00 USD | 3,730,000.00 USD | 30,000.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,270,000.00 USD | 16,270,000.00 USD | 79,630.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4431.30` | 3,760,000.00 USD | 3,760,000.00 USD | 29,610.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,440,000.00 USD | 16,440,000.00 USD | 157,240.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.70` | 3,780,000.00 USD | 3,780,000.00 USD | 18,430.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,550,000.00 USD | 16,550,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,680,000.00 USD | 16,680,000.00 USD | 102,740.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,760,000.00 USD | 16,760,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,810,000.00 USD | 16,810,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.30` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 2,900.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `3615.50` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 107,600.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.50` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 18,530.00 USD | 0.00 USD | 2,510.00 USD |
| `7D` | `3619.80` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3620.70` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 24,000.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `3624.10` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 105,540.00 USD | 0.00 USD | 21,190.00 USD |
| `1D` | `3624.90` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 43,990.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `3628.40` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.10` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD |
| `7D` | `3632.70` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 117,280.00 USD | 0.00 USD | 15,210.00 USD |
| `1D` | `3633.30` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,790,000.00 USD | 0.00 USD | 15,790,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.50` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 62,140.00 USD | 0.00 USD | 7,500.00 USD |
| `7D` | `3641.30` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3641.70` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 10,510.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `3645.60` | 15,590,000.00 USD | 0.00 USD | 15,590,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3645.90` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 14,480.00 USD | 0.00 USD | 5,020.00 USD |
| `7D` | `3649.90` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 28,880.00 USD | 0.00 USD | 2,300.00 USD |
| `7D` | `3654.20` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3654.30` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 11,860.00 USD | 0.00 USD | 1,900.00 USD |
| `1D` | `3658.50` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 8,050.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `3658.50` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3662.70` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3667.10` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.10` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD |
| `1D` | `3851.70` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3852.00` | 13,940,000.00 USD | 0.00 USD | 13,940,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3855.90` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 48,970.00 USD | 0.00 USD | 6,910.00 USD |
| `7D` | `3856.30` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 315,230.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3860.10` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 50,400.00 USD | 0.00 USD | 6,530.00 USD |
| `7D` | `3860.60` | 13,320,000.00 USD | 0.00 USD | 13,320,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3864.30` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 146,200.00 USD | 0.00 USD | 12,280.00 USD |
| `7D` | `3864.90` | 13,130,000.00 USD | 0.00 USD | 13,130,000.00 USD | 325,660.00 USD | 0.00 USD | 59,280.00 USD |
| `1D` | `3868.50` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 104,800.00 USD | 0.00 USD | 22,340.00 USD |
| `7D` | `3869.20` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 622,200.00 USD | 0.00 USD | 41,850.00 USD |
| `1D` | `3872.70` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 126,980.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3873.50` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3876.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 105,540.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3877.80` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 529,730.00 USD | 0.00 USD | 70,170.00 USD |
| `1D` | `3881.10` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 145,550.00 USD | 0.00 USD | 29,830.00 USD |
| `7D` | `3882.10` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3885.30` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 41,920.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3886.40` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3889.50` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 36,210.00 USD | 0.00 USD | 14,650.00 USD |
| `7D` | `3890.70` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3893.70` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 104,820.00 USD | 0.00 USD | 6,900.00 USD |
| `7D` | `3895.00` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3897.90` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 41,960.00 USD | 0.00 USD | 5,700.00 USD |
| `7D` | `3899.30` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3902.10` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 30,100.00 USD | 0.00 USD | 5,510.00 USD |
| `7D` | `3903.60` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3906.30` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 34,240.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3914.70` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,140,000.00 USD | 0.00 USD | 9,140,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3935.70` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 103,550.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 536,620.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3939.90` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 46,950.00 USD | 0.00 USD | 10,440.00 USD |
| `7D` | `3942.30` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.10` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 235,600.00 USD | 0.00 USD | 12,510.00 USD |
| `7D` | `3946.60` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 676,110.00 USD | 0.00 USD | 142,130.00 USD |
| `1D` | `3948.30` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 249,040.00 USD | 0.00 USD | 51,250.00 USD |
| `7D` | `3950.90` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3952.50` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 295,830.00 USD | 0.00 USD | 36,370.00 USD |
| `7D` | `3955.20` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 803,630.00 USD | 0.00 USD | 73,510.00 USD |
| `1D` | `3956.70` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 137,160.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3960.90` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 378,510.00 USD | 0.00 USD | 47,410.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.10` | 728,170.00 USD | 0.00 USD | 728,170.00 USD | 79,800.00 USD | 0.00 USD | 35,580.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.30` | 612,790.00 USD | 0.00 USD | 612,790.00 USD | 51,240.00 USD | 0.00 USD | 31,900.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.50` | 529,650.00 USD | 0.00 USD | 529,650.00 USD | 182,860.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3977.70` | 340,180.00 USD | 0.00 USD | 340,180.00 USD | 103,850.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3981.90` | 229,120.00 USD | 0.00 USD | 229,120.00 USD | 67,730.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3986.10` | 138,980.00 USD | 0.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3990.30` | 63,870.00 USD | 0.00 USD | 63,870.00 USD | 41,610.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3998.70` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4013.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4015.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4095.30` | 68,750.00 USD | 68,750.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 630,450.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4099.50` | 170,120.00 USD | 170,120.00 USD | 0.00 USD | 94,620.00 USD | 0.00 USD | 6,760.00 USD |
| `7D` | `4101.40` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4103.70` | 321,830.00 USD | 321,830.00 USD | 0.00 USD | 138,670.00 USD | 0.00 USD | 13,030.00 USD |
| `7D` | `4105.70` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 678,320.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4107.90` | 596,320.00 USD | 596,320.00 USD | 0.00 USD | 234,740.00 USD | 0.00 USD | 39,750.00 USD |
| `7D` | `4110.00` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 73,030.00 USD |
| `1D` | `4112.10` | 937,650.00 USD | 937,650.00 USD | 0.00 USD | 303,570.00 USD | 0.00 USD | 37,760.00 USD |
| `7D` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4116.30` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 173,010.00 USD | 0.00 USD | 28,640.00 USD |
| `7D` | `4118.60` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 776,800.00 USD | 0.00 USD | 136,300.00 USD |
| `1D` | `4120.50` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 283,380.00 USD | 0.00 USD | 19,770.00 USD |
| `7D` | `4122.90` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4124.70` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 187,000.00 USD | 0.00 USD | 54,160.00 USD |
| `7D` | `4127.20` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4128.90` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 106,820.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `4131.50` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.10` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 57,990.00 USD | 0.00 USD | 28,740.00 USD |
| `7D` | `4135.80` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.30` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 192,710.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.50` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 83,910.00 USD | 0.00 USD | 11,410.00 USD |
| `7D` | `4144.40` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4145.70` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 54,840.00 USD | 0.00 USD | 11,010.00 USD |
| `7D` | `4148.70` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.90` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4154.10` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.30` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.50` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,520,000.00 USD | 11,520,000.00 USD | 0.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4175.10` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `4178.80` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 247,350.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4179.30` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 33,170.00 USD | 0.00 USD | 5,240.00 USD |
| `7D` | `4183.10` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4183.50` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD |
| `7D` | `4187.40` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD |
| `1D` | `4187.70` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 17,020.00 USD |
| `7D` | `4191.70` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 607,230.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4191.90` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `4196.00` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4196.10` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 102,820.00 USD | 0.00 USD | 15,140.00 USD |
| `1D` | `4200.30` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 102,180.00 USD | 0.00 USD | 8,020.00 USD |
| `7D` | `4200.30` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 459,220.00 USD | 0.00 USD | 62,750.00 USD |
| `1D` | `4204.50` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 139,240.00 USD | 0.00 USD | 26,590.00 USD |
| `7D` | `4204.60` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4208.70` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `4208.90` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4212.90` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 46,160.00 USD | 0.00 USD | 14,650.00 USD |
| `7D` | `4213.20` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4217.10` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 73,870.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4217.50` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4221.30` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 48,960.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4221.80` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4225.50` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 33,860.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `4226.10` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4229.70` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 33,610.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `4230.40` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4233.90` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 20,800.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4234.70` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4242.30` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4389.50` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `1D` | `4414.50` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `4415.30` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4418.70` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 17,690.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4419.60` | 16,130,000.00 USD | 16,130,000.00 USD | 0.00 USD | 76,740.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4422.90` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `4423.90` | 16,170,000.00 USD | 16,170,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4427.10` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `4428.20` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 79,630.00 USD | 0.00 USD | 18,160.00 USD |
| `1D` | `4431.30` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 29,610.00 USD | 0.00 USD | 7,540.00 USD |
| `7D` | `4432.50` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 157,240.00 USD | 0.00 USD | 11,860.00 USD |
| `1D` | `4433.70` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 18,430.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `4436.80` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,680,000.00 USD | 16,680,000.00 USD | 0.00 USD | 102,740.00 USD | 0.00 USD | 27,200.00 USD |
| `7D` | `4445.40` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.03M` | Total OI Tokens: `68,266.5 PAXG`
  * 1h OI Change: `-0.23%` | 4h OI Change: `-0.81%` | 24h OI Change: `+0.02%`
  * Exchange Breakdown: Binance=`106.95M` | Bybit=`19.98M` | OKX=`-` | Hyperliquid=`25.01M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.17K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `61.76%` | `38.24%` | `1.62` | 2,910,000.00 USD |
| `15M` | `Binance` | `58.37%` | `41.63%` | `1.40` | 144,160.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `36.7%` | `63.3%` | `0.58` | 235,140.00 USD |
| `15M` | `KuCoin` | `47.24%` | `52.76%` | `0.90` | 3,690.00 USD |
| `15M` | `Gate` | `63.37%` | `36.63%` | `1.73` | 66,980.00 USD |
| `15M` | `Bitget` | `67.3%` | `32.7%` | `2.06` | 96,670.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `66.53%` | `33.47%` | `1.99` | 1,990,000.00 USD |
| `15M` | `Bitunix` | `78.47%` | `21.53%` | `3.64` | 149,700.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `40.84%` | `59.16%` | `0.69` | 190,570.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.17%` | `99.83%` | `0.00` | 27,920.00 USD |
| `15M` | `HTX` | `13.95%` | `86.05%` | `0.16` | 172.32 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0.45%` | `99.55%` | `0.00` | 8,050.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `58.37%` | `41.63%` | `1.40` | 144,160.00 USD |
| `15M` | `Global Accounts` | `61.76%` | `38.24%` | `1.62` | 2,910,000.00 USD |
| `1H` | `PAXG` | `56.13%` | `43.87%` | `1.28` | 13,970,000.00 USD |
| `1H` | `Binance` | `65.62%` | `34.38%` | `1.91` | 1,210,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `52.88%` | `47.12%` | `1.12` | 1,830,000.00 USD |
| `1H` | `KuCoin` | `12.36%` | `87.64%` | `0.14` | 50,860.00 USD |
| `1H` | `Gate` | `51.26%` | `48.74%` | `1.05` | 462,690.00 USD |
| `1H` | `Bitget` | `43.67%` | `56.33%` | `0.78` | 492,070.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `58.56%` | `41.44%` | `1.41` | 7,840,000.00 USD |
| `1H` | `Bitunix` | `74.51%` | `25.49%` | `2.92` | 675,290.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.15%` | `57.85%` | `0.73` | 1,170,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.74%` | `99.26%` | `0.01` | 167,300.00 USD |
| `1H` | `HTX` | `56.73%` | `43.27%` | `1.31` | 2,770.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.67%` | `55.33%` | `0.81` | 73,420.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `65.62%` | `34.38%` | `1.91` | 1,210,000.00 USD |
| `1H` | `Global Accounts` | `56.13%` | `43.87%` | `1.28` | 13,970,000.00 USD |
| `4H` | `PAXG` | `49.65%` | `50.35%` | `0.99` | 67,730,000.00 USD |
| `4H` | `Binance` | `53.09%` | `46.91%` | `1.13` | 5,260,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `48.84%` | `51.16%` | `0.95` | 5,550,000.00 USD |
| `4H` | `KuCoin` | `46.57%` | `53.43%` | `0.87` | 391,140.00 USD |
| `4H` | `Gate` | `50.86%` | `49.14%` | `1.04` | 1,720,000.00 USD |
| `4H` | `Bitget` | `44.67%` | `55.33%` | `0.81` | 2,080,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `50.17%` | `49.83%` | `1.01` | 44,170,000.00 USD |
| `4H` | `Bitunix` | `59.81%` | `40.19%` | `1.49` | 1,960,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.27%` | `48.73%` | `1.05` | 4,970,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.2%` | `90.8%` | `0.10` | 1,430,000.00 USD |
| `4H` | `HTX` | `92.49%` | `7.51%` | `12.32` | 67,200.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.49%` | `52.51%` | `0.90` | 133,580.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.09%` | `46.91%` | `1.13` | 5,260,000.00 USD |
| `4H` | `Global Accounts` | `49.65%` | `50.35%` | `0.99` | 67,730,000.00 USD |


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
| `5m` | 8,350.00 USD | 32,250.00 USD | **`ACCUMULATION`** |
| `15m` | 24,080.00 USD | 101,350.00 USD | **`ACCUMULATION`** |
| `30m` | -162,380.00 USD | 277,640.00 USD | **`ACCUMULATION`** |
| `1h` | -216,090.00 USD | 465,350.00 USD | **`ACCUMULATION`** |
| `2h` | -407,960.00 USD | 1,040,000.00 USD | **`ACCUMULATION`** |
| `4h` | 299,430.00 USD | 800,330.00 USD | **`ACCUMULATION`** |
| `6h` | 116,890.00 USD | 1,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | -44,450.00 USD | 1,790,000.00 USD | **`ACCUMULATION`** |
| `12h` | -72,790.00 USD | 855,070.00 USD | **`ACCUMULATION`** |
| `24h` | -216,650.00 USD | 1,590,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,690,000.00 USD | -7,340,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,150,000.00 USD | -71,960,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+8.35K` | 15m=`+24.08K` | 1h=`-216.09K` | 24h=`-216.65K`
* Futures Capital Netflows: 5m=`+32.25K` | 15m=`+101.35K` | 1h=`+465.35K` | 24h=`+1.59M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4040.10` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4049.12` (Risk Distance: `9.02` pts)
  * +2.5R Take Profit: `4017.55`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4041.70`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
