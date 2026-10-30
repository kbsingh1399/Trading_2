# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 14:20:35 IST` (`2026-10-30 08:50:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3986.88` | **Live Ask Quote**: `3986.97` | **Mid Price**: `3986.93`
- **Spread Points**: `9.00` | **Spread BPS**: `0.23 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `3986.93` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `9.97` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4014.83` | Lower -3.00σ Band: `3959.02`
  * Upper +2.51σ Band: `4008.85` | Lower -2.51σ Band: `3965.00`
  * Upper +2.01σ Band: `4003.67` | Lower -2.01σ Band: `3970.18`
  * Upper +2.00σ Band: `4002.87` | Lower -2.00σ Band: `3970.98`
  * Upper +1.28σ Band: `3998.09` | Lower -1.28σ Band: `3975.76`
  * Upper +1.00σ Band: `3994.90` | Lower -1.00σ Band: `3978.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3986.93` | EMA-20=`3986.93` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3986.93` (Slope: `+0.0000`) | EMA-100=`3986.93`
  * Institutional Anchors: EMA-144=`3986.93` | EMA-200=`3986.93` (Slope: `+0.0000`) | EMA-233=`3986.93`
- **Range Boundaries**: 24H High=`4026.79` | 24H Low=`3947.06` | Weekly High=`4066.66` | Weekly Low=`3907.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.45` (Distance: `-0.65%`)
  * Point of Control (POC) = `4007.08` (Distance: `-0.50%`)
  * Value Area Low (VAL) = `3988.38` (Distance: `-0.03%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4052.58` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`4010.85` | Low=`3963.00`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3970.98` - `4002.87`
  * Optimal Trade Entry (OTE 0.705): `3994.90`
  * Structural Invalidation Anchor (0.786): `4018.82`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3991.23` | `3993.79` | `3990.46` | `3992.67` | `127` | 506,506.21 USD | 61,654.30 USD | `+12.17%` | -554,375.38 USD | `+0.52` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `3992.67` | `3992.67` | `3990.68` | `3991.08` | `56` | 221,801.97 USD | 3,569.44 USD | `+1.61%` | -550,805.95 USD | `+0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `3991.08` | `3991.08` | `3990.47` | `3990.95` | `10` | 41,886.76 USD | 18,244.54 USD | `+43.56%` | -532,561.41 USD | `+0.30` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3981.68` | `3991.15` | `3979.22` | `3989.06` | `520` | 2,072,644.26 USD | 167,881.86 USD | `+8.10%` | -499,236.63 USD | `+0.57` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `3989.06` | `3994.73` | `3988.88` | `3991.23` | `356` | 1,419,588.63 USD | -116,793.05 USD | `-8.23%` | -616,029.68 USD | `-0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `3991.23` | `3993.79` | `3990.46` | `3990.95` | `193` | 769,975.44 USD | 83,288.68 USD | `+10.82%` | -532,741.00 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3999.19` | `4001.59` | `3987.00` | `3992.27` | `1,465` | 5,850,978.09 USD | -383,638.83 USD | `-6.56%` | 522,438.31 USD | `-0.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3992.27` | `3994.60` | `3973.63` | `3981.69` | `1,798` | 7,168,194.57 USD | -1,074,302.54 USD | `-14.99%` | -551,864.23 USD | `-2.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3981.68` | `3994.73` | `3979.22` | `3990.95` | `1,068` | 4,262,208.33 USD | 134,377.49 USD | `+3.15%` | -417,486.74 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `3994.73` | `3979.22` | `3990.95` | `1,068` | 4,262,208.33 USD | 134,377.49 USD | `+3.15%` | -444,588.74 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `3994.73` | `3979.22` | `3990.95` | `1,068` | 4,262,208.33 USD | 134,377.49 USD | `+3.15%` | -444,588.74 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `BID` | `3987.60` | `9.4978` | 37,873.43 USD | 1,196,638.75 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `3987.70` | `61.1052` | 243,669.21 USD | 1,158,765.32 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3987.80` | `0.4512` | 1,799.30 USD | 915,096.11 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3987.90` | `51.0491` | 203,578.71 USD | 913,296.82 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `3988.00` | `12.4908` | 49,813.31 USD | 709,718.11 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3988.10` | `8.0190` | 31,980.57 USD | 659,904.80 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3988.20` | `28.4329` | 113,396.09 USD | 627,924.23 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3988.30` | `7.6370` | 30,458.65 USD | 514,528.13 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3988.40` | `5.0128` | 19,993.05 USD | 484,069.49 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3988.50` | `7.1919` | 28,684.89 USD | 464,076.44 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3988.60` | `11.2788` | 44,986.62 USD | 435,391.54 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3988.80` | `14.7590` | 58,870.70 USD | 390,404.92 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3988.90` | `1.5946` | 6,360.70 USD | 331,534.22 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3989.00` | `15.0434` | 60,008.12 USD | 325,173.52 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3989.10` | `14.5947` | 58,219.72 USD | 265,165.40 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3989.20` | `7.5192` | 29,995.59 USD | 206,945.68 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3989.40` | `8.1795` | 32,631.30 USD | 176,950.09 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3989.50` | `0.3746` | 1,494.47 USD | 144,318.79 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3989.60` | `13.4954` | 53,841.25 USD | 142,824.32 USD | `4 orders` | `-0.00%` | `-` |
| `BID` | `3989.70` | `22.3032` | 88,983.08 USD | 88,983.08 USD | `10 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3989.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,989.75` | `0.00%` | `-` |
| `ASK` | `3989.80` | `3.9266` | 15,666.35 USD | 15,666.35 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `3990.00` | `25.8256` | 103,044.14 USD | 118,710.49 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3990.10` | `8.0586` | 32,154.62 USD | 150,865.11 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3990.30` | `7.6346` | 30,464.34 USD | 181,329.46 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3990.40` | `7.5192` | 30,004.62 USD | 211,334.07 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `3990.50` | `55.0903` | 219,837.84 USD | 431,171.91 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3990.60` | `1.4676` | 5,856.60 USD | 437,028.52 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3990.70` | `13.2796` | 52,994.90 USD | 490,023.42 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3990.80` | `21.2069` | 84,632.50 USD | 574,655.92 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `3990.90` | `4.7857` | 19,099.25 USD | 593,755.17 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3991.00` | `54.5471` | 217,697.48 USD | 811,452.64 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3991.10` | `93.9997` | 375,162.20 USD | 1,186,614.84 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3991.20` | `4.1820` | 16,691.20 USD | 1,203,306.04 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3991.30` | `13.1500` | 52,485.60 USD | 1,255,791.64 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3991.40` | `31.4248` | 125,428.95 USD | 1,381,220.58 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3991.50` | `20.2758` | 80,930.86 USD | 1,462,151.44 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `3991.70` | `17.0073` | 67,888.04 USD | 1,530,039.48 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `3991.80` | `26.7101` | 106,621.38 USD | 1,636,660.86 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `3991.90` | `0.4697` | 1,875.00 USD | 1,638,535.85 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `3992.00` | `6.7500` | 26,946.00 USD | 1,665,481.85 USD | `5 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `46` | `0x5b5d...c060` | `SHORT` | 25,892,450.81 USD | `6,489.82` | `4185.46` | `3989.70` | `29000.08` | 1,270,500.20 USD | `+4.91%` | `4X Cross` |
| `47` | `0x4692...164f` | `SHORT` | 25,250,432.28 USD | `6,328.90` | `4127.45` | `3989.70` | `14075.18` | 871,832.83 USD | `+3.45%` | `5X Cross` |
| `64` | `0xb83d...6e36` | `SHORT` | 23,419,137.64 USD | `5,869.90` | `4228.86` | `3989.70` | `26600.04` | 1,403,884.30 USD | `+5.99%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,265,889.86 USD | `4,828.91` | `4157.43` | `3989.70` | `2294.12` | -809,992.46 USD | `-4.20%` | `25X Cross` |
| `142` | `0x645b...87b8` | `LONG` | 14,157,872.16 USD | `3,548.61` | `4127.81` | `3989.70` | `640.43` | -490,126.62 USD | `-3.46%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,039,190.20 USD | `3,268.21` | `4228.94` | `3989.70` | `4377.97` | 781,888.93 USD | `+6.00%` | `25X Cross` |
| `183` | `0xa742...e390` | `SHORT` | 11,171,248.57 USD | `2,800.02` | `4364.62` | `3989.70` | `4212.74` | 1,049,795.57 USD | `+9.40%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,777,340.00 USD | `2,200.00` | `4176.09` | `3989.70` | `2685.33` | -410,079.30 USD | `-4.67%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,777,340.00 USD | `2,200.00` | `4112.20` | `3989.70` | `4287.08` | 269,514.59 USD | `+3.07%` | `20X Cross` |
| `303` | `0xacb6...efbd` | `SHORT` | 7,881,130.10 USD | `1,975.37` | `4048.55` | `3989.70` | `6649.71` | 116,261.62 USD | `+1.48%` | `6X Cross` |
| `368` | `0xc26c...b8f4` | `LONG` | 6,303,533.70 USD | `1,579.95` | `4075.62` | `3989.70` | `0.000000` | -135,763.27 USD | `-2.15%` | `1X Cross` |
| `568` | `0x63da...8add` | `LONG` | 3,989,700.00 USD | `1,000.00` | `4021.46` | `3989.70` | `3564.63` | -31,760.96 USD | `-0.80%` | `25X Cross` |
| `583` | `0xf3dc...1672` | `LONG` | 3,926,944.81 USD | `984.27` | `4018.39` | `3989.70` | `2835.97` | -28,241.88 USD | `-0.72%` | `20X Cross` |
| `595` | `0x9aa5...58af` | `LONG` | 3,876,560.09 USD | `971.64` | `4279.98` | `3989.70` | `0.000000` | -282,049.00 USD | `-7.28%` | `20X Cross` |
| `679` | `0x4a20...3c26` | `LONG` | 3,340,973.58 USD | `837.40` | `4599.73` | `3989.70` | `0.000000` | -510,846.80 USD | `-15.29%` | `20X Cross` |
| `795` | `0x9c06...0560` | `LONG` | 2,900,319.60 USD | `726.95` | `4002.36` | `3989.70` | `0.000000` | -9,209.66 USD | `-0.32%` | `25X Cross` |
| `836` | `0x0fac...7a0a` | `LONG` | 2,738,869.20 USD | `686.49` | `4290.34` | `3989.70` | `1415.59` | -206,389.50 USD | `-7.54%` | `25X Cross` |
| `900` | `0x354b...6425` | `LONG` | 2,521,103.40 USD | `631.90` | `4004.93` | `3989.70` | `0.000000` | -9,626.98 USD | `-0.38%` | `10X Cross` |
| `918` | `0x625e...a354` | `SHORT` | 2,473,614.00 USD | `620.00` | `4122.81` | `3989.70` | `4279.49` | 82,533.03 USD | `+3.34%` | `20X Cross` |
| `940` | `0xeae3...e8ad` | `SHORT` | 2,393,820.00 USD | `600.00` | `4104.77` | `3989.70` | `4268.58` | 69,045.11 USD | `+2.88%` | `20X Cross` |
| `942` | `0xf285...fa82` | `LONG` | 2,386,263.11 USD | `598.11` | `4146.45` | `3989.70` | `3891.76` | -93,756.44 USD | `-3.93%` | `25X Cross` |
| `949` | `0xd8c5...99b0` | `SHORT` | 2,371,297.74 USD | `594.35` | `4175.35` | `3989.70` | `35533.03` | 110,346.29 USD | `+4.65%` | `4X Cross` |
| `967` | `0x12f7...8750` | `LONG` | 2,336,411.01 USD | `585.61` | `4082.77` | `3989.70` | `2706.12` | -54,505.97 USD | `-2.33%` | `10X Cross` |
| `1001` | `0x413c...886c` | `LONG` | 2,232,119.05 USD | `559.47` | `4007.05` | `3989.70` | `0.000000` | -9,708.15 USD | `-0.43%` | `2X Cross` |
| `1113` | `0x61ce...a62b` | `SHORT` | 1,984,889.71 USD | `497.50` | `4071.66` | `3989.70` | `4725.06` | 40,779.08 USD | `+2.05%` | `20X Cross` |
| `1186` | `0x2edd...8179` | `LONG` | 1,873,191.12 USD | `469.26` | `4164.68` | `3991.90` | `0.000000` | -81,117.65 USD | `-4.33%` | `10X Cross` |
| `1231` | `0xead5...69f2` | `LONG` | 1,810,461.63 USD | `453.78` | `4220.88` | `3989.70` | `3539.46` | -104,906.43 USD | `-5.79%` | `5X Isolated` |
| `1293` | `0x7a6d...f79c` | `SHORT` | 1,709,746.26 USD | `428.38` | `4136.09` | `3991.90` | `5431.53` | 62,068.74 USD | `+3.63%` | `10X Cross` |
| `1313` | `0x46fc...1195` | `LONG` | 1,667,641.94 USD | `417.99` | `4052.43` | `3989.70` | `2186.57` | -26,223.31 USD | `-1.57%` | `20X Cross` |
| `1356` | `0x6d15...d374` | `LONG` | 1,595,880.00 USD | `400.00` | `4068.25` | `3989.70` | `3842.33` | -31,420.00 USD | `-1.97%` | `25X Cross` |
| `1357` | `0xee02...309d` | `SHORT` | 1,595,880.00 USD | `400.00` | `4438.84` | `3989.70` | `4202.87` | 179,658.60 USD | `+11.26%` | `25X Isolated` |
| `1381` | `0x51f6...2b39` | `LONG` | 1,562,715.74 USD | `391.48` | `4228.25` | `3991.90` | `556.88` | -92,559.95 USD | `-5.92%` | `10X Cross` |
| `1410` | `0x02a7...fe9f` | `SHORT` | 1,555,983.00 USD | `390.00` | `4055.02` | `3989.70` | `4307.20` | 25,476.25 USD | `+1.64%` | `25X Cross` |
| `1445` | `0x7e77...b8d2` | `SHORT` | 1,516,086.00 USD | `380.00` | `4131.92` | `3989.70` | `4294.01` | 54,043.64 USD | `+3.56%` | `20X Cross` |
| `1471` | `0x72c2...9b37` | `LONG` | 1,488,681.95 USD | `373.13` | `4000.98` | `3989.70` | `3778.56` | -4,211.57 USD | `-0.28%` | `13X Isolated` |
| `1487` | `0x781e...96b7` | `SHORT` | 1,458,473.09 USD | `365.37` | `4359.19` | `3991.90` | `12887.91` | 134,229.60 USD | `+9.20%` | `10X Cross` |
| `1505` | `0xaa44...b844` | `LONG` | 1,436,292.00 USD | `360.00` | `4043.10` | `3989.70` | `2817.12` | -19,225.63 USD | `-1.34%` | `4X Cross` |
| `1634` | `0xa41f...d50a` | `LONG` | 1,312,460.09 USD | `328.96` | `4468.89` | `3989.70` | `3802.69` | -157,637.76 USD | `-12.01%` | `15X Cross` |
| `1683` | `0xbf5a...88ba` | `SHORT` | 1,267,347.75 USD | `317.65` | `4091.80` | `3989.70` | `9961.41` | 32,435.28 USD | `+2.56%` | `20X Cross` |
| `1724` | `0xff31...ff6c` | `SHORT` | 1,236,807.00 USD | `310.00` | `4372.43` | `3989.70` | `4789.68` | 118,648.38 USD | `+9.59%` | `10X Isolated` |
| `1749` | `0xada6...6f88` | `LONG` | 1,210,740.30 USD | `303.47` | `4166.46` | `3989.70` | `1788.91` | -53,642.16 USD | `-4.43%` | `5X Cross` |
| `1898` | `0x50e2...d770` | `LONG` | 1,078,684.82 USD | `270.37` | `4243.58` | `3989.70` | `2562.61` | -68,641.64 USD | `-6.36%` | `20X Cross` |
| `1910` | `0x4c92...4f17` | `SHORT` | 1,064,134.78 USD | `266.72` | `4260.98` | `3989.70` | `6494.22` | 72,357.46 USD | `+6.80%` | `20X Cross` |
| `1979` | `0xd346...c4f3` | `LONG` | 1,018,066.91 USD | `255.17` | `4188.66` | `3989.70` | `3310.94` | -50,769.60 USD | `-4.99%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.56%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.42%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+2.94%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.44%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+2.94%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--1.12%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.31%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.67%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `Long Liquidation` | `3582.50` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3583.90` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3586.70` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.30` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3590.90` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3592.70` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3595.10` | 5,510,000.00 USD | 5,510,000.00 USD | 28,070.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.10` | 15,180,000.00 USD | 15,180,000.00 USD | 97,240.00 USD | 0.00 USD | 17,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3599.30` | 5,470,000.00 USD | 5,470,000.00 USD | 16,810.00 USD | 0.00 USD | 13,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.50` | 15,070,000.00 USD | 15,070,000.00 USD | 172,380.00 USD | 0.00 USD | 67,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3603.50` | 5,440,000.00 USD | 5,440,000.00 USD | 63,060.00 USD | 0.00 USD | 45,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3605.90` | 14,830,000.00 USD | 14,830,000.00 USD | 144,650.00 USD | 0.00 USD | 52,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3607.70` | 5,330,000.00 USD | 5,330,000.00 USD | 14,680.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.30` | 14,630,000.00 USD | 14,630,000.00 USD | 83,580.00 USD | 0.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.90` | 5,310,000.00 USD | 5,310,000.00 USD | 25,560.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.70` | 14,520,000.00 USD | 14,520,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.10` | 5,270,000.00 USD | 5,270,000.00 USD | 35,020.00 USD | 0.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.10` | 14,420,000.00 USD | 14,420,000.00 USD | 54,880.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3620.30` | 5,230,000.00 USD | 5,230,000.00 USD | 48,150.00 USD | 0.00 USD | 11,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.50` | 14,350,000.00 USD | 14,350,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.50` | 5,170,000.00 USD | 5,170,000.00 USD | 63,060.00 USD | 0.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.90` | 14,280,000.00 USD | 14,280,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.70` | 5,100,000.00 USD | 5,100,000.00 USD | 28,780.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 14,180,000.00 USD | 14,180,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.90` | 5,070,000.00 USD | 5,070,000.00 USD | 12,880.00 USD | 0.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.70` | 14,110,000.00 USD | 14,110,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.10` | 5,050,000.00 USD | 5,050,000.00 USD | 9,470.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.10` | 14,090,000.00 USD | 14,090,000.00 USD | 55,830.00 USD | 0.00 USD | 13,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.50` | 14,020,000.00 USD | 14,020,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 13,980,000.00 USD | 13,980,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.30` | 13,960,000.00 USD | 13,960,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.70` | 13,900,000.00 USD | 13,900,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3663.10` | 13,890,000.00 USD | 13,890,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.50` | 13,880,000.00 USD | 13,880,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3821.50` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3821.90` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3826.10` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3830.30` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.30` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3834.50` | 4,970,000.00 USD | 4,970,000.00 USD | 81,530.00 USD | 0.00 USD | 37,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.70` | 13,760,000.00 USD | 13,760,000.00 USD | 69,040.00 USD | 0.00 USD | 61,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3838.70` | 4,850,000.00 USD | 4,850,000.00 USD | 34,640.00 USD | 0.00 USD | 43,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 13,630,000.00 USD | 13,630,000.00 USD | 396,580.00 USD | 0.00 USD | 83,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3842.90` | 4,770,000.00 USD | 4,770,000.00 USD | 103,240.00 USD | 0.00 USD | 145,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.50` | 13,150,000.00 USD | 13,150,000.00 USD | 572,270.00 USD | 0.00 USD | 215,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3847.10` | 4,520,000.00 USD | 4,520,000.00 USD | 168,780.00 USD | 0.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.90` | 12,360,000.00 USD | 12,360,000.00 USD | 423,040.00 USD | 0.00 USD | 99,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3851.30` | 4,300,000.00 USD | 4,300,000.00 USD | 46,000.00 USD | 0.00 USD | 35,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.30` | 11,840,000.00 USD | 11,840,000.00 USD | 311,520.00 USD | 0.00 USD | 87,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.50` | 4,220,000.00 USD | 4,220,000.00 USD | 117,110.00 USD | 0.00 USD | 33,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.70` | 11,440,000.00 USD | 11,440,000.00 USD | 233,200.00 USD | 0.00 USD | 37,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.70` | 4,070,000.00 USD | 4,070,000.00 USD | 131,940.00 USD | 0.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3861.10` | 11,170,000.00 USD | 11,170,000.00 USD | 156,400.00 USD | 0.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.90` | 3,920,000.00 USD | 3,920,000.00 USD | 185,770.00 USD | 0.00 USD | 34,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3865.50` | 10,950,000.00 USD | 10,950,000.00 USD | 247,240.00 USD | 0.00 USD | 59,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.10` | 3,700,000.00 USD | 3,700,000.00 USD | 163,490.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.90` | 10,640,000.00 USD | 10,640,000.00 USD | 249,090.00 USD | 0.00 USD | 33,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.30` | 3,510,000.00 USD | 3,510,000.00 USD | 85,880.00 USD | 0.00 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3874.30` | 10,360,000.00 USD | 10,360,000.00 USD | 217,090.00 USD | 0.00 USD | 27,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.50` | 3,410,000.00 USD | 3,410,000.00 USD | 33,490.00 USD | 0.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3878.70` | 10,120,000.00 USD | 10,120,000.00 USD | 129,550.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.70` | 3,380,000.00 USD | 3,380,000.00 USD | 14,120.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3883.10` | 9,970,000.00 USD | 9,970,000.00 USD | 171,360.00 USD | 0.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3887.50` | 9,760,000.00 USD | 9,760,000.00 USD | 72,000.00 USD | 0.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3891.90` | 9,660,000.00 USD | 9,660,000.00 USD | 120,010.00 USD | 0.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.30` | 9,530,000.00 USD | 9,530,000.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3900.70` | 9,400,000.00 USD | 9,400,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.70` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.10` | 9,310,000.00 USD | 9,310,000.00 USD | 36,810.00 USD | 0.00 USD | 73,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.90` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 53,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 9,200,000.00 USD | 9,200,000.00 USD | 36,880.00 USD | 0.00 USD | 169,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3910.10` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 76,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.90` | 9,000,000.00 USD | 9,000,000.00 USD | 154,630.00 USD | 0.00 USD | 40,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3914.30` | 3,210,000.00 USD | 3,210,000.00 USD | 163,060.00 USD | 0.00 USD | 45,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.30` | 8,800,000.00 USD | 8,800,000.00 USD | 601,560.00 USD | 0.00 USD | 127,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3918.50` | 3,000,000.00 USD | 3,000,000.00 USD | 69,290.00 USD | 0.00 USD | 117,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.70` | 2,820,000.00 USD | 2,820,000.00 USD | 206,480.00 USD | 0.00 USD | 279,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.70` | 8,070,000.00 USD | 8,070,000.00 USD | 1,130,000.00 USD | 0.00 USD | 468,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.90` | 2,330,000.00 USD | 2,330,000.00 USD | 337,560.00 USD | 0.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.10` | 6,470,000.00 USD | 6,470,000.00 USD | 995,010.00 USD | 0.00 USD | 255,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3931.10` | 1,880,000.00 USD | 1,880,000.00 USD | 87,700.00 USD | 0.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 5,220,000.00 USD | 5,220,000.00 USD | 605,700.00 USD | 0.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3935.30` | 1,730,000.00 USD | 1,730,000.00 USD | 186,570.00 USD | 0.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.90` | 4,440,000.00 USD | 4,440,000.00 USD | 414,690.00 USD | 0.00 USD | 100,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.50` | 1,470,000.00 USD | 1,470,000.00 USD | 250,650.00 USD | 0.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.30` | 3,920,000.00 USD | 3,920,000.00 USD | 322,520.00 USD | 0.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.70` | 1,190,000.00 USD | 1,190,000.00 USD | 316,200.00 USD | 0.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.70` | 3,540,000.00 USD | 3,540,000.00 USD | 465,130.00 USD | 0.00 USD | 151,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.90` | 807,950.00 USD | 807,950.00 USD | 378,570.00 USD | 0.00 USD | 55,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3949.10` | 2,920,000.00 USD | 2,920,000.00 USD | 570,640.00 USD | 0.00 USD | 48,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.10` | 374,260.00 USD | 374,260.00 USD | 208,360.00 USD | 0.00 USD | 24,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.50` | 2,300,000.00 USD | 2,300,000.00 USD | 442,240.00 USD | 0.00 USD | 87,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3956.30` | 141,490.00 USD | 141,490.00 USD | 66,750.00 USD | 0.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.90` | 1,770,000.00 USD | 1,770,000.00 USD | 264,660.00 USD | 0.00 USD | 38,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.50` | 62,450.00 USD | 62,450.00 USD | 60,830.00 USD | 0.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.30` | 1,470,000.00 USD | 1,470,000.00 USD | 233,850.00 USD | 0.00 USD | 62,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3966.70` | 1,170,000.00 USD | 1,170,000.00 USD | 249,290.00 USD | 0.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.10` | 863,560.00 USD | 863,560.00 USD | 170,870.00 USD | 0.00 USD | 38,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.50` | 653,770.00 USD | 653,770.00 USD | 252,970.00 USD | 0.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3979.90` | 380,310.00 USD | 380,310.00 USD | 265,470.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.30` | 110,560.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3988.70` | 76,450.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4061.30` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4063.50` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4065.50` | 73,370.00 USD | 73,370.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4067.90` | 185,820.00 USD | 185,820.00 USD | 0.00 USD | 0.00 USD | 124,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4069.70` | 150,310.00 USD | 150,310.00 USD | 0.00 USD | 0.00 USD | 76,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4072.30` | 319,810.00 USD | 319,810.00 USD | 57,650.00 USD | 0.00 USD | 76,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4073.90` | 359,250.00 USD | 359,250.00 USD | 163,060.00 USD | 0.00 USD | 45,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4076.70` | 905,580.00 USD | 905,580.00 USD | 470,150.00 USD | 0.00 USD | 115,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.10` | 537,510.00 USD | 537,510.00 USD | 60,920.00 USD | 0.00 USD | 117,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.10` | 2,130,000.00 USD | 2,130,000.00 USD | 958,780.00 USD | 0.00 USD | 269,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4082.30` | 921,480.00 USD | 921,480.00 USD | 165,530.00 USD | 0.00 USD | 218,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.50` | 3,440,000.00 USD | 3,440,000.00 USD | 898,240.00 USD | 0.00 USD | 408,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4086.50` | 1,450,000.00 USD | 1,450,000.00 USD | 360,500.00 USD | 0.00 USD | 169,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4089.90` | 4,380,000.00 USD | 4,380,000.00 USD | 756,080.00 USD | 0.00 USD | 180,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.70` | 1,540,000.00 USD | 1,540,000.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 4,890,000.00 USD | 4,890,000.00 USD | 403,990.00 USD | 0.00 USD | 110,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.90` | 1,840,000.00 USD | 1,840,000.00 USD | 237,090.00 USD | 0.00 USD | 65,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.70` | 5,470,000.00 USD | 5,470,000.00 USD | 528,170.00 USD | 0.00 USD | 51,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.10` | 2,080,000.00 USD | 2,080,000.00 USD | 186,910.00 USD | 0.00 USD | 49,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.10` | 5,920,000.00 USD | 5,920,000.00 USD | 334,780.00 USD | 0.00 USD | 115,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4103.30` | 2,460,000.00 USD | 2,460,000.00 USD | 321,430.00 USD | 0.00 USD | 62,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.50` | 2,890,000.00 USD | 2,890,000.00 USD | 380,110.00 USD | 0.00 USD | 52,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.50` | 6,520,000.00 USD | 6,520,000.00 USD | 475,520.00 USD | 0.00 USD | 124,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.70` | 3,180,000.00 USD | 3,180,000.00 USD | 254,930.00 USD | 0.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.90` | 7,040,000.00 USD | 7,040,000.00 USD | 452,900.00 USD | 0.00 USD | 62,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.90` | 3,280,000.00 USD | 3,280,000.00 USD | 83,840.00 USD | 0.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.30` | 7,490,000.00 USD | 7,490,000.00 USD | 397,960.00 USD | 0.00 USD | 54,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.10` | 3,350,000.00 USD | 3,350,000.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 7,800,000.00 USD | 7,800,000.00 USD | 275,800.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4124.30` | 3,360,000.00 USD | 3,360,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.10` | 8,160,000.00 USD | 8,160,000.00 USD | 303,170.00 USD | 0.00 USD | 61,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.50` | 8,340,000.00 USD | 8,340,000.00 USD | 123,140.00 USD | 0.00 USD | 50,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.90` | 8,600,000.00 USD | 8,600,000.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4138.30` | 8,850,000.00 USD | 8,850,000.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.10` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.70` | 9,130,000.00 USD | 9,130,000.00 USD | 232,530.00 USD | 0.00 USD | 47,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.30` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.10` | 9,270,000.00 USD | 9,270,000.00 USD | 59,830.00 USD | 0.00 USD | 73,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.50` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4151.50` | 9,430,000.00 USD | 9,430,000.00 USD | 87,550.00 USD | 0.00 USD | 75,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.70` | 3,540,000.00 USD | 3,540,000.00 USD | 81,530.00 USD | 0.00 USD | 22,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.90` | 9,700,000.00 USD | 9,700,000.00 USD | 214,420.00 USD | 0.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4157.90` | 3,630,000.00 USD | 3,630,000.00 USD | 30,460.00 USD | 0.00 USD | 58,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.30` | 10,120,000.00 USD | 10,120,000.00 USD | 333,520.00 USD | 0.00 USD | 90,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.10` | 3,810,000.00 USD | 3,810,000.00 USD | 71,840.00 USD | 0.00 USD | 103,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4164.70` | 10,940,000.00 USD | 10,940,000.00 USD | 599,380.00 USD | 0.00 USD | 215,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4166.30` | 4,070,000.00 USD | 4,070,000.00 USD | 176,420.00 USD | 0.00 USD | 90,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.10` | 11,450,000.00 USD | 11,450,000.00 USD | 422,420.00 USD | 0.00 USD | 91,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4170.50` | 4,130,000.00 USD | 4,130,000.00 USD | 35,100.00 USD | 0.00 USD | 21,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.50` | 11,760,000.00 USD | 11,760,000.00 USD | 235,800.00 USD | 0.00 USD | 74,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.70` | 4,260,000.00 USD | 4,260,000.00 USD | 97,530.00 USD | 0.00 USD | 33,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4177.90` | 12,010,000.00 USD | 12,010,000.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.90` | 4,370,000.00 USD | 4,370,000.00 USD | 94,090.00 USD | 0.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.30` | 12,210,000.00 USD | 12,210,000.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.10` | 4,560,000.00 USD | 4,560,000.00 USD | 148,550.00 USD | 0.00 USD | 34,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,480,000.00 USD | 12,480,000.00 USD | 199,210.00 USD | 0.00 USD | 68,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4187.30` | 4,800,000.00 USD | 4,800,000.00 USD | 219,080.00 USD | 0.00 USD | 26,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.10` | 12,790,000.00 USD | 12,790,000.00 USD | 274,560.00 USD | 0.00 USD | 34,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.50` | 4,930,000.00 USD | 4,930,000.00 USD | 115,850.00 USD | 0.00 USD | 14,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.50` | 13,040,000.00 USD | 13,040,000.00 USD | 221,120.00 USD | 0.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.70` | 5,000,000.00 USD | 5,000,000.00 USD | 57,050.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.90` | 5,040,000.00 USD | 5,040,000.00 USD | 33,210.00 USD | 0.00 USD | 2,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.90` | 13,200,000.00 USD | 13,200,000.00 USD | 132,330.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.10` | 5,040,000.00 USD | 5,040,000.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.30` | 13,340,000.00 USD | 13,340,000.00 USD | 116,920.00 USD | 0.00 USD | 24,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.70` | 13,470,000.00 USD | 13,470,000.00 USD | 101,210.00 USD | 0.00 USD | 31,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.10` | 13,580,000.00 USD | 13,580,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 13,700,000.00 USD | 13,700,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.90` | 13,800,000.00 USD | 13,800,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.30` | 13,890,000.00 USD | 13,890,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.70` | 13,940,000.00 USD | 13,940,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4235.10` | 13,980,000.00 USD | 13,980,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.50` | 14,000,000.00 USD | 14,000,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.30` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4380.50` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4384.70` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4388.90` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.10` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4393.10` | 5,100,000.00 USD | 5,100,000.00 USD | 28,070.00 USD | 0.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.50` | 14,060,000.00 USD | 14,060,000.00 USD | 27,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4396.70` | 5,120,000.00 USD | 5,120,000.00 USD | 2,110.00 USD | 0.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.90` | 14,170,000.00 USD | 14,170,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.30` | 14,410,000.00 USD | 14,410,000.00 USD | 173,930.00 USD | 0.00 USD | 69,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 14,560,000.00 USD | 14,560,000.00 USD | 98,540.00 USD | 0.00 USD | 47,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.10` | 14,680,000.00 USD | 14,680,000.00 USD | 100,170.00 USD | 0.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.50` | 14,730,000.00 USD | 14,730,000.00 USD | 36,920.00 USD | 0.00 USD | 12,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.90` | 14,820,000.00 USD | 14,820,000.00 USD | 76,390.00 USD | 0.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.30` | 14,870,000.00 USD | 14,870,000.00 USD | 35,830.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.70` | 14,930,000.00 USD | 14,930,000.00 USD | 45,130.00 USD | 0.00 USD | 15,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4433.10` | 15,020,000.00 USD | 15,020,000.00 USD | 81,850.00 USD | 0.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4437.50` | 15,090,000.00 USD | 15,090,000.00 USD | 61,940.00 USD | 0.00 USD | 9,350.00 USD | `Tier 1 CEX` |

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
| `1D` | `3582.50` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `3583.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `3586.70` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3588.30` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3590.90` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 14,370.00 USD |
| `7D` | `3592.70` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3595.10` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 28,070.00 USD | 0.00 USD | 13,100.00 USD |
| `7D` | `3597.10` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 97,240.00 USD | 0.00 USD | 17,170.00 USD |
| `1D` | `3599.30` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 16,810.00 USD | 0.00 USD | 13,560.00 USD |
| `7D` | `3601.50` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 172,380.00 USD | 0.00 USD | 67,200.00 USD |
| `1D` | `3603.50` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 63,060.00 USD | 0.00 USD | 45,020.00 USD |
| `7D` | `3605.90` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 144,650.00 USD | 0.00 USD | 52,500.00 USD |
| `1D` | `3607.70` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 14,680.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `3610.30` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 83,580.00 USD | 0.00 USD | 27,540.00 USD |
| `1D` | `3611.90` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 25,560.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3614.70` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3616.10` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 35,020.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3619.10` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 54,880.00 USD | 0.00 USD | 10,660.00 USD |
| `1D` | `3620.30` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 48,150.00 USD | 0.00 USD | 11,540.00 USD |
| `7D` | `3623.50` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD |
| `1D` | `3624.50` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 63,060.00 USD | 0.00 USD | 8,760.00 USD |
| `7D` | `3627.90` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3628.70` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 28,780.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `3632.30` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3632.90` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 12,880.00 USD | 0.00 USD | 3,800.00 USD |
| `7D` | `3636.70` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD |
| `1D` | `3637.10` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 9,470.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3641.10` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 55,830.00 USD | 0.00 USD | 13,010.00 USD |
| `7D` | `3645.50` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `7D` | `3649.90` | 13,980,000.00 USD | 0.00 USD | 13,980,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `7D` | `3654.30` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `7D` | `3658.70` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `7D` | `3663.10` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3667.50` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3821.50` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3821.90` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `1D` | `3826.10` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `3830.30` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 38,470.00 USD |
| `7D` | `3830.30` | 13,840,000.00 USD | 0.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3834.50` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 81,530.00 USD | 0.00 USD | 37,630.00 USD |
| `7D` | `3834.70` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 69,040.00 USD | 0.00 USD | 61,760.00 USD |
| `1D` | `3838.70` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 34,640.00 USD | 0.00 USD | 43,980.00 USD |
| `7D` | `3839.10` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 396,580.00 USD | 0.00 USD | 83,550.00 USD |
| `1D` | `3842.90` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 103,240.00 USD | 0.00 USD | 145,060.00 USD |
| `7D` | `3843.50` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 572,270.00 USD | 0.00 USD | 215,940.00 USD |
| `1D` | `3847.10` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 168,780.00 USD | 0.00 USD | 50,200.00 USD |
| `7D` | `3847.90` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 423,040.00 USD | 0.00 USD | 99,480.00 USD |
| `1D` | `3851.30` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 46,000.00 USD | 0.00 USD | 35,430.00 USD |
| `7D` | `3852.30` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 311,520.00 USD | 0.00 USD | 87,820.00 USD |
| `1D` | `3855.50` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 117,110.00 USD | 0.00 USD | 33,380.00 USD |
| `7D` | `3856.70` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 233,200.00 USD | 0.00 USD | 37,330.00 USD |
| `1D` | `3859.70` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 131,940.00 USD | 0.00 USD | 19,430.00 USD |
| `7D` | `3861.10` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 156,400.00 USD | 0.00 USD | 58,780.00 USD |
| `1D` | `3863.90` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 185,770.00 USD | 0.00 USD | 34,460.00 USD |
| `7D` | `3865.50` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 247,240.00 USD | 0.00 USD | 59,830.00 USD |
| `1D` | `3868.10` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 163,490.00 USD | 0.00 USD | 22,020.00 USD |
| `7D` | `3869.90` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 249,090.00 USD | 0.00 USD | 33,900.00 USD |
| `1D` | `3872.30` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 85,880.00 USD | 0.00 USD | 12,570.00 USD |
| `7D` | `3874.30` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 217,090.00 USD | 0.00 USD | 27,780.00 USD |
| `1D` | `3876.50` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 33,490.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `3878.70` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 129,550.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `3880.70` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 14,120.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3883.10` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 171,360.00 USD | 0.00 USD | 33,130.00 USD |
| `7D` | `3887.50` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 72,000.00 USD | 0.00 USD | 27,920.00 USD |
| `7D` | `3891.90` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 120,010.00 USD | 0.00 USD | 17,560.00 USD |
| `7D` | `3896.30` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD |
| `7D` | `3900.70` | 9,400,000.00 USD | 0.00 USD | 9,400,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3901.70` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3905.10` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 36,810.00 USD | 0.00 USD | 73,950.00 USD |
| `1D` | `3905.90` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 53,970.00 USD |
| `7D` | `3909.50` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 36,880.00 USD | 0.00 USD | 169,180.00 USD |
| `1D` | `3910.10` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 76,940.00 USD |
| `7D` | `3913.90` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 154,630.00 USD | 0.00 USD | 40,680.00 USD |
| `1D` | `3914.30` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 163,060.00 USD | 0.00 USD | 45,880.00 USD |
| `7D` | `3918.30` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 601,560.00 USD | 0.00 USD | 127,000.00 USD |
| `1D` | `3918.50` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 69,290.00 USD | 0.00 USD | 117,340.00 USD |
| `1D` | `3922.70` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 206,480.00 USD | 0.00 USD | 279,850.00 USD |
| `7D` | `3922.70` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 1,130,000.00 USD | 0.00 USD | 468,950.00 USD |
| `1D` | `3926.90` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 337,560.00 USD | 0.00 USD | 107,720.00 USD |
| `7D` | `3927.10` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 995,010.00 USD | 0.00 USD | 255,250.00 USD |
| `1D` | `3931.10` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 87,700.00 USD | 0.00 USD | 63,710.00 USD |
| `7D` | `3931.50` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 605,700.00 USD | 0.00 USD | 178,870.00 USD |
| `1D` | `3935.30` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 186,570.00 USD | 0.00 USD | 76,870.00 USD |
| `7D` | `3935.90` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 414,690.00 USD | 0.00 USD | 100,990.00 USD |
| `1D` | `3939.50` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 250,650.00 USD | 0.00 USD | 28,980.00 USD |
| `7D` | `3940.30` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 322,520.00 USD | 0.00 USD | 57,010.00 USD |
| `1D` | `3943.70` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 316,200.00 USD | 0.00 USD | 65,260.00 USD |
| `7D` | `3944.70` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 465,130.00 USD | 0.00 USD | 151,430.00 USD |
| `1D` | `3947.90` | 807,950.00 USD | 0.00 USD | 807,950.00 USD | 378,570.00 USD | 0.00 USD | 55,120.00 USD |
| `7D` | `3949.10` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 570,640.00 USD | 0.00 USD | 48,610.00 USD |
| `1D` | `3952.10` | 374,260.00 USD | 0.00 USD | 374,260.00 USD | 208,360.00 USD | 0.00 USD | 24,410.00 USD |
| `7D` | `3953.50` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 442,240.00 USD | 0.00 USD | 87,240.00 USD |
| `1D` | `3956.30` | 141,490.00 USD | 0.00 USD | 141,490.00 USD | 66,750.00 USD | 0.00 USD | 12,280.00 USD |
| `7D` | `3957.90` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 264,660.00 USD | 0.00 USD | 38,880.00 USD |
| `1D` | `3960.50` | 62,450.00 USD | 0.00 USD | 62,450.00 USD | 60,830.00 USD | 0.00 USD | 1,630.00 USD |
| `7D` | `3962.30` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 233,850.00 USD | 0.00 USD | 62,790.00 USD |
| `7D` | `3966.70` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 249,290.00 USD | 0.00 USD | 61,820.00 USD |
| `7D` | `3971.10` | 863,560.00 USD | 0.00 USD | 863,560.00 USD | 170,870.00 USD | 0.00 USD | 38,920.00 USD |
| `7D` | `3975.50` | 653,770.00 USD | 0.00 USD | 653,770.00 USD | 252,970.00 USD | 0.00 USD | 20,490.00 USD |
| `7D` | `3979.90` | 380,310.00 USD | 0.00 USD | 380,310.00 USD | 265,470.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.30` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3988.70` | 76,450.00 USD | 0.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3992.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3994.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4061.30` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD |
| `7D` | `4063.50` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4065.50` | 73,370.00 USD | 73,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD |
| `7D` | `4067.90` | 185,820.00 USD | 185,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 124,870.00 USD |
| `1D` | `4069.70` | 150,310.00 USD | 150,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76,940.00 USD |
| `7D` | `4072.30` | 319,810.00 USD | 319,810.00 USD | 0.00 USD | 57,650.00 USD | 0.00 USD | 76,340.00 USD |
| `1D` | `4073.90` | 359,250.00 USD | 359,250.00 USD | 0.00 USD | 163,060.00 USD | 0.00 USD | 45,880.00 USD |
| `7D` | `4076.70` | 905,580.00 USD | 905,580.00 USD | 0.00 USD | 470,150.00 USD | 0.00 USD | 115,620.00 USD |
| `1D` | `4078.10` | 537,510.00 USD | 537,510.00 USD | 0.00 USD | 60,920.00 USD | 0.00 USD | 117,340.00 USD |
| `7D` | `4081.10` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 958,780.00 USD | 0.00 USD | 269,470.00 USD |
| `1D` | `4082.30` | 921,480.00 USD | 921,480.00 USD | 0.00 USD | 165,530.00 USD | 0.00 USD | 218,440.00 USD |
| `7D` | `4085.50` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 898,240.00 USD | 0.00 USD | 408,830.00 USD |
| `1D` | `4086.50` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 360,500.00 USD | 0.00 USD | 169,140.00 USD |
| `7D` | `4089.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 756,080.00 USD | 0.00 USD | 180,050.00 USD |
| `1D` | `4090.70` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 40,700.00 USD | 0.00 USD | 46,870.00 USD |
| `7D` | `4094.30` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 403,990.00 USD | 0.00 USD | 110,270.00 USD |
| `1D` | `4094.90` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 237,090.00 USD | 0.00 USD | 65,160.00 USD |
| `7D` | `4098.70` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 528,170.00 USD | 0.00 USD | 51,690.00 USD |
| `1D` | `4099.10` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 186,910.00 USD | 0.00 USD | 49,220.00 USD |
| `7D` | `4103.10` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 334,780.00 USD | 0.00 USD | 115,300.00 USD |
| `1D` | `4103.30` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 321,430.00 USD | 0.00 USD | 62,660.00 USD |
| `1D` | `4107.50` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 380,110.00 USD | 0.00 USD | 52,640.00 USD |
| `7D` | `4107.50` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 475,520.00 USD | 0.00 USD | 124,070.00 USD |
| `1D` | `4111.70` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 254,930.00 USD | 0.00 USD | 28,420.00 USD |
| `7D` | `4111.90` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 452,900.00 USD | 0.00 USD | 62,020.00 USD |
| `1D` | `4115.90` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 83,840.00 USD | 0.00 USD | 21,050.00 USD |
| `7D` | `4116.30` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 397,960.00 USD | 0.00 USD | 54,320.00 USD |
| `1D` | `4120.10` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `4120.70` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 275,800.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4124.30` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4125.10` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 303,170.00 USD | 0.00 USD | 61,080.00 USD |
| `7D` | `4129.50` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 50,120.00 USD |
| `7D` | `4133.90` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4138.30` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD |
| `1D` | `4141.10` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,130.00 USD |
| `7D` | `4142.70` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 232,530.00 USD | 0.00 USD | 47,230.00 USD |
| `1D` | `4145.30` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,560.00 USD |
| `7D` | `4147.10` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 73,280.00 USD |
| `1D` | `4149.50` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38,470.00 USD |
| `7D` | `4151.50` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 87,550.00 USD | 0.00 USD | 75,670.00 USD |
| `1D` | `4153.70` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 81,530.00 USD | 0.00 USD | 22,940.00 USD |
| `7D` | `4155.90` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 214,420.00 USD | 0.00 USD | 56,290.00 USD |
| `1D` | `4157.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 30,460.00 USD | 0.00 USD | 58,670.00 USD |
| `7D` | `4160.30` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 333,520.00 USD | 0.00 USD | 90,670.00 USD |
| `1D` | `4162.10` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 71,840.00 USD | 0.00 USD | 103,110.00 USD |
| `7D` | `4164.70` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 599,380.00 USD | 0.00 USD | 215,070.00 USD |
| `1D` | `4166.30` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 176,420.00 USD | 0.00 USD | 90,670.00 USD |
| `7D` | `4169.10` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 422,420.00 USD | 0.00 USD | 91,590.00 USD |
| `1D` | `4170.50` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 35,100.00 USD | 0.00 USD | 21,200.00 USD |
| `7D` | `4173.50` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 235,800.00 USD | 0.00 USD | 74,580.00 USD |
| `1D` | `4174.70` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 97,530.00 USD | 0.00 USD | 33,200.00 USD |
| `7D` | `4177.90` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD |
| `1D` | `4178.90` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 94,090.00 USD | 0.00 USD | 21,490.00 USD |
| `7D` | `4182.30` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD |
| `1D` | `4183.10` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 148,550.00 USD | 0.00 USD | 34,040.00 USD |
| `7D` | `4186.70` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 199,210.00 USD | 0.00 USD | 68,840.00 USD |
| `1D` | `4187.30` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 219,080.00 USD | 0.00 USD | 26,910.00 USD |
| `7D` | `4191.10` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 274,560.00 USD | 0.00 USD | 34,470.00 USD |
| `1D` | `4191.50` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 115,850.00 USD | 0.00 USD | 14,140.00 USD |
| `7D` | `4195.50` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 221,120.00 USD | 0.00 USD | 33,460.00 USD |
| `1D` | `4195.70` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 57,050.00 USD | 0.00 USD | 10,330.00 USD |
| `1D` | `4199.90` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 33,210.00 USD | 0.00 USD | 2,520.00 USD |
| `7D` | `4199.90` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 132,330.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4204.10` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4204.30` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 24,640.00 USD |
| `7D` | `4208.70` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 31,300.00 USD |
| `7D` | `4213.10` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4217.50` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `4221.90` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `4226.30` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `7D` | `4230.70` | 13,940,000.00 USD | 13,940,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `4235.10` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.50` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4380.30` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4380.50` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,650.00 USD |
| `1D` | `4384.70` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD |
| `1D` | `4388.90` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,350.00 USD |
| `7D` | `4389.10` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,120.00 USD |
| `1D` | `4393.10` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 28,070.00 USD | 0.00 USD | 4,140.00 USD |
| `7D` | `4393.50` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4396.70` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 15,860.00 USD |
| `7D` | `4397.90` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `7D` | `4402.30` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 173,930.00 USD | 0.00 USD | 69,870.00 USD |
| `7D` | `4406.70` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 98,540.00 USD | 0.00 USD | 47,430.00 USD |
| `7D` | `4411.10` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 100,170.00 USD | 0.00 USD | 26,530.00 USD |
| `7D` | `4415.50` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 12,680.00 USD |
| `7D` | `4419.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 76,390.00 USD | 0.00 USD | 6,390.00 USD |
| `7D` | `4424.30` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 18,300.00 USD |
| `7D` | `4428.70` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 45,130.00 USD | 0.00 USD | 15,100.00 USD |
| `7D` | `4433.10` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 81,850.00 USD | 0.00 USD | 9,610.00 USD |
| `7D` | `4437.50` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 61,940.00 USD | 0.00 USD | 9,350.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.92M` | Total OI Tokens: `68,868.2 PAXG`
  * 1h OI Change: `-0.45%` | 4h OI Change: `-0.43%` | 24h OI Change: `-0.01%`
  * Exchange Breakdown: Binance=`105.21M` | Bybit=`24.06M` | OKX=`-` | Hyperliquid=`24.51M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.06K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0009%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0008%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0121%` | **USDT Bitget** | `0.0030%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `55.93%` | `44.07%` | `1.27` | 1,900,000.00 USD |
| `15M` | `Binance` | `46.47%` | `53.53%` | `0.87` | 708,440.00 USD |
| `15M` | `OKX` | `56.07%` | `43.93%` | `1.28` | 343,790.00 USD |
| `15M` | `Bybit` | `70.53%` | `29.47%` | `2.39` | 246,560.00 USD |
| `15M` | `KuCoin` | `50.66%` | `49.34%` | `1.03` | 45,020.00 USD |
| `15M` | `Gate` | `59.38%` | `40.62%` | `1.46` | 38,060.00 USD |
| `15M` | `Bitget` | `79.09%` | `20.91%` | `3.78` | 69,740.00 USD |
| `15M` | `BingX` | `82.77%` | `17.23%` | `4.80` | 81,840.00 USD |
| `15M` | `MEXC` | `44.94%` | `55.06%` | `0.82` | 109,930.00 USD |
| `15M` | `Bitunix` | `40.46%` | `59.54%` | `0.68` | 29,040.00 USD |
| `15M` | `Hyperliquid` | `14.53%` | `85.47%` | `0.17` | 26,190.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50%` | `50%` | `1.00` | 84,260.00 USD |
| `15M` | `Crypto.com` | `95.11%` | `4.89%` | `19.45` | 247.02 USD |
| `15M` | `WhiteBIT` | `79.01%` | `20.99%` | `3.76` | 105,840.00 USD |
| `15M` | `HTX` | `30.61%` | `69.39%` | `0.44` | 549.45 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `74.85%` | `25.15%` | `2.98` | 3,430.00 USD |
| `15M` | `Aster` | `80.95%` | `19.05%` | `4.25` | 1,340.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `80.08%` | `19.92%` | `4.02` | 2,310.00 USD |
| `15M` | `Whale Positions` | `46.47%` | `53.53%` | `0.87` | 708,440.00 USD |
| `15M` | `Global Accounts` | `55.93%` | `44.07%` | `1.27` | 1,900,000.00 USD |
| `1H` | `PAXG` | `44.34%` | `55.66%` | `0.80` | 14,710,000.00 USD |
| `1H` | `Binance` | `48.96%` | `51.04%` | `0.96` | 5,830,000.00 USD |
| `1H` | `OKX` | `46.49%` | `53.51%` | `0.87` | 1,970,000.00 USD |
| `1H` | `Bybit` | `43.31%` | `56.69%` | `0.76` | 1,650,000.00 USD |
| `1H` | `KuCoin` | `31.93%` | `68.07%` | `0.47` | 233,110.00 USD |
| `1H` | `Gate` | `38.72%` | `61.28%` | `0.63` | 517,020.00 USD |
| `1H` | `Bitget` | `43.68%` | `56.32%` | `0.78` | 1,040,000.00 USD |
| `1H` | `BingX` | `22.97%` | `77.03%` | `0.30` | 1,330,000.00 USD |
| `1H` | `MEXC` | `31.24%` | `68.76%` | `0.45` | 840,590.00 USD |
| `1H` | `Bitunix` | `52.83%` | `47.17%` | `1.12` | 188,830.00 USD |
| `1H` | `Hyperliquid` | `55.33%` | `44.67%` | `1.24` | 162,220.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.29%` | `50.71%` | `0.97` | 534,840.00 USD |
| `1H` | `Crypto.com` | `26.71%` | `73.29%` | `0.36` | 8,770.00 USD |
| `1H` | `WhiteBIT` | `72.05%` | `27.95%` | `2.58` | 310,080.00 USD |
| `1H` | `HTX` | `68.55%` | `31.45%` | `2.18` | 8,950.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.57%` | `56.43%` | `0.77` | 14,750.00 USD |
| `1H` | `Aster` | `27.9%` | `72.1%` | `0.39` | 22,010.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `88.53%` | `11.47%` | `7.72` | 48,910.00 USD |
| `1H` | `Whale Positions` | `48.96%` | `51.04%` | `0.96` | 5,830,000.00 USD |
| `1H` | `Global Accounts` | `44.34%` | `55.66%` | `0.80` | 14,710,000.00 USD |
| `4H` | `PAXG` | `43.81%` | `56.19%` | `0.78` | 56,200,000.00 USD |
| `4H` | `Binance` | `47.57%` | `52.43%` | `0.91` | 21,090,000.00 USD |
| `4H` | `OKX` | `41.49%` | `58.51%` | `0.71` | 9,980,000.00 USD |
| `4H` | `Bybit` | `43.8%` | `56.2%` | `0.78` | 6,480,000.00 USD |
| `4H` | `KuCoin` | `40.54%` | `59.46%` | `0.68` | 518,420.00 USD |
| `4H` | `Gate` | `43.81%` | `56.19%` | `0.78` | 1,660,000.00 USD |
| `4H` | `Bitget` | `44.32%` | `55.68%` | `0.80` | 4,420,000.00 USD |
| `4H` | `BingX` | `23.79%` | `76.21%` | `0.31` | 4,120,000.00 USD |
| `4H` | `MEXC` | `34.53%` | `65.47%` | `0.53` | 3,350,000.00 USD |
| `4H` | `Bitunix` | `47.32%` | `52.68%` | `0.90` | 848,810.00 USD |
| `4H` | `Hyperliquid` | `54.62%` | `45.38%` | `1.20` | 716,060.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 1,850,000.00 USD |
| `4H` | `Crypto.com` | `43.42%` | `56.58%` | `0.77` | 28,930.00 USD |
| `4H` | `WhiteBIT` | `76.77%` | `23.23%` | `3.30` | 924,840.00 USD |
| `4H` | `HTX` | `82.08%` | `17.92%` | `4.58` | 30,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.91%` | `58.09%` | `0.72` | 15,340.00 USD |
| `4H` | `Aster` | `56.84%` | `43.16%` | `1.32` | 44,550.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `76.84%` | `23.16%` | `3.32` | 126,530.00 USD |
| `4H` | `Whale Positions` | `47.57%` | `52.43%` | `0.91` | 21,090,000.00 USD |
| `4H` | `Global Accounts` | `43.81%` | `56.19%` | `0.78` | 56,200,000.00 USD |


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
| `5m` | -52,880.00 USD | -745.66 USD | **`DISTRIBUTION`** |
| `15m` | -172,140.00 USD | 96,140.00 USD | **`DISTRIBUTION`** |
| `30m` | -203,490.00 USD | 359,210.00 USD | **`ACCUMULATION`** |
| `1h` | -727,870.00 USD | -96,220.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,140,000.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 487,850.00 USD | -383,050.00 USD | **`ACCUMULATION`** |
| `6h` | 463,180.00 USD | -376,730.00 USD | **`ACCUMULATION`** |
| `8h` | 452,180.00 USD | -1,260,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -688,890.00 USD | -1,280,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -841,800.00 USD | 42,790.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,380,000.00 USD | -9,520,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,870,000.00 USD | -72,150,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-52.88K` | 15m=`-172.14K` | 1h=`-727.87K` | 24h=`-841.80K`
* Futures Capital Netflows: 5m=`-745.66` | 15m=`+96.14K` | 1h=`-96.22K` | 24h=`+42.79K`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3988.38` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3976.28` (Risk Distance: `12.10` pts)
  * +2.5R Take Profit: `4018.62`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.45` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4025.55` (Risk Distance: `12.10` pts)
  * +2.5R Take Profit: `3983.21`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4018.82`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
