# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 10:22:41 IST` (`2026-10-30 04:52:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3991.26` | **Live Ask Quote**: `3991.34` | **Mid Price**: `3991.30`
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
  * Session VWAP: `4003.54` | VWAP Z-Score: `-1.65` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.64` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.55` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4021.10` | Lower -3.00σ Band: `3985.99`
  * Upper +2.51σ Band: `4018.23` | Lower -2.51σ Band: `3988.85`
  * Upper +2.01σ Band: `4015.30` | Lower -2.01σ Band: `3991.78`
  * Upper +2.00σ Band: `4015.24` | Lower -2.00σ Band: `3991.84`
  * Upper +1.28σ Band: `4011.03` | Lower -1.28σ Band: `3996.05`
  * Upper +1.00σ Band: `4009.39` | Lower -1.00σ Band: `3997.69`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3997.07` | EMA-20=`4002.39` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4010.93` (Slope: `+0.0000`) | EMA-100=`4019.45`
  * Institutional Anchors: EMA-144=`4023.44` | EMA-200=`4025.60` (Slope: `-0.0837`) | EMA-233=`4027.32`
- **Range Boundaries**: 24H High=`4046.38` | 24H Low=`3987.44` | Weekly High=`4082.75` | Weekly Low=`3987.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.32` (Distance: `-0.55%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.39%`)
  * Value Area Low (VAL) = `3996.71` (Distance: `-0.14%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4007.27` | Low=`3975.33`
  * New York Session (13:00-21:00 UTC): High=`4015.25` | Low=`3967.35`
  * Initial Balance (First Hour): IB High=`4003.27` | IB Low=`3979.33`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3975.33` - `4007.27`
  * Optimal Trade Entry (OTE 0.705): `3999.28`
  * Structural Invalidation Anchor (0.786): `4023.23`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4002.91` | `4005.00` | `4002.91` | `4003.77` | `64` | 255,344.40 USD | -121,357.76 USD | `-47.53%` | -652,379.07 USD | `-0.77` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4003.78` | `4004.10` | `4000.90` | `4001.35` | `35` | 141,374.77 USD | -58,149.86 USD | `-41.13%` | -710,528.93 USD | `-0.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4001.35` | `4001.35` | `3998.22` | `4000.27` | `94` | 377,160.10 USD | -288,728.47 USD | `-76.55%` | -999,257.40 USD | `-1.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4000.52` | `4001.18` | `3995.14` | `4001.00` | `693` | 2,769,257.98 USD | 190,834.78 USD | `+6.89%` | -780,388.50 USD | `+1.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4001.01` | `4003.88` | `3999.56` | `4002.90` | `669` | 2,675,288.79 USD | 249,367.20 USD | `+9.32%` | -531,021.31 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4002.91` | `4005.00` | `3998.22` | `4000.27` | `193` | 773,879.26 USD | -468,236.09 USD | `-60.51%` | -999,257.40 USD | `-1.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4008.80` | `4014.92` | `4001.35` | `4002.36` | `667` | 2,671,119.24 USD | -91,693.11 USD | `-3.43%` | -823,707.83 USD | `-0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -1,045,509.48 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4000.27` | `1,555` | 6,218,426.04 USD | -28,034.12 USD | `-0.45%` | -1,073,543.61 USD | `-0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4005.00` | `3995.14` | `4000.26` | `1,555` | 6,218,486.05 USD | -28,094.13 USD | `-0.45%` | -80,185.66 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4005.00` | `3995.14` | `4000.26` | `1,555` | 6,218,486.05 USD | -28,094.13 USD | `-0.45%` | -80,185.66 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID` | `3991.30` | `7.8635` | 31,385.59 USD | 739,296.73 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3991.40` | `21.0764` | 84,124.34 USD | 707,911.15 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3991.50` | `6.3794` | 25,463.38 USD | 623,786.80 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3991.60` | `14.4216` | 57,565.26 USD | 598,323.43 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3991.70` | `6.0221` | 24,038.42 USD | 540,758.17 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3991.80` | `25.0567` | 100,021.34 USD | 516,719.75 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3991.90` | `13.6615` | 54,535.34 USD | 416,698.42 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `3992.00` | `5.2592` | 20,994.73 USD | 362,163.08 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3992.10` | `3.5200` | 14,052.19 USD | 341,168.35 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3992.20` | `5.7157` | 22,818.22 USD | 327,116.16 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3992.30` | `10.5461` | 42,103.20 USD | 304,297.94 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3992.40` | `15.3103` | 61,124.84 USD | 262,194.75 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3992.60` | `4.5003` | 17,967.90 USD | 201,069.90 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3992.80` | `0.7194` | 2,872.42 USD | 183,102.01 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3992.90` | `9.8138` | 39,185.52 USD | 180,229.59 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `3993.00` | `12.5736` | 50,206.38 USD | 141,044.06 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `3993.10` | `1.4958` | 5,972.88 USD | 90,837.68 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3993.20` | `6.3411` | 25,321.28 USD | 84,864.80 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3993.30` | `4.7026` | 18,778.89 USD | 59,543.52 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `3993.40` | `10.2080` | 40,764.63 USD | 40,764.63 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3993.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,993.45` | `0.00%` | `-` |
| `ASK` | `3993.50` | `86.1367` | 343,986.91 USD | 343,986.91 USD | `11 orders` | `+0.00%` | `-` |
| `ASK` | `3993.60` | `8.4095` | 33,584.18 USD | 377,571.09 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `3993.70` | `21.5114` | 85,910.08 USD | 463,481.17 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3993.80` | `13.9928` | 55,884.44 USD | 519,365.61 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3993.90` | `5.7271` | 22,873.46 USD | 542,239.08 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3994.00` | `11.7251` | 46,830.05 USD | 589,069.13 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3994.10` | `86.5075` | 345,519.61 USD | 934,588.73 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3994.20` | `4.4009` | 17,578.07 USD | 952,166.81 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3994.30` | `1.4838` | 5,926.74 USD | 958,093.55 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3994.40` | `15.2105` | 60,756.82 USD | 1,018,850.37 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3994.50` | `3.5849` | 14,319.88 USD | 1,033,170.25 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3994.60` | `21.2421` | 84,853.69 USD | 1,118,023.95 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `3994.70` | `3.4142` | 13,638.70 USD | 1,131,662.65 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3994.80` | `68.4246` | 273,342.59 USD | 1,405,005.24 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3994.90` | `11.7923` | 47,109.06 USD | 1,452,114.30 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3995.00` | `10.3678` | 41,419.36 USD | 1,493,533.66 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3995.10` | `4.7240` | 18,872.85 USD | 1,512,406.52 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3995.20` | `5.2567` | 21,001.57 USD | 1,533,408.08 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `3995.40` | `17.7801` | 71,038.61 USD | 1,604,446.70 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `3995.50` | `13.9965` | 55,923.02 USD | 1,660,369.71 USD | `7 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,924,250.95 USD | `6,489.82` | `4185.46` | `3994.60` | `29525.77` | 1,238,700.06 USD | `+4.78%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,196,754.40 USD | `6,307.70` | `4129.22` | `3994.60` | `13924.66` | 849,149.51 USD | `+3.37%` | `5X Cross` |
| `66` | `0xb83d...6e36` | `SHORT` | 23,442,617.23 USD | `5,869.90` | `4228.86` | `3994.60` | `27207.63` | 1,380,404.70 USD | `+5.89%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,283,756.81 USD | `4,828.91` | `4157.43` | `3994.60` | `2275.83` | -792,125.50 USD | `-4.11%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,177,089.86 USD | `3,549.06` | `4127.91` | `3994.60` | `575.47` | -473,145.04 USD | `-3.34%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,055,204.45 USD | `3,268.21` | `4228.94` | `3994.60` | `4393.72` | 765,874.68 USD | `+5.87%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,584,340.40 USD | `2,900.00` | `4364.92` | `3994.60` | `4235.87` | 1,073,935.93 USD | `+9.27%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,788,120.00 USD | `2,200.00` | `4176.09` | `3994.60` | `2648.86` | -399,299.30 USD | `-4.54%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,786,140.00 USD | `2,200.00` | `4112.20` | `3994.60` | `4331.35` | 260,714.59 USD | `+2.97%` | `20X Cross` |
| `301` | `0xacb6...efbd` | `SHORT` | 7,889,031.57 USD | `1,975.37` | `4048.55` | `3994.60` | `6597.76` | 108,360.14 USD | `+1.37%` | `6X Cross` |
| `368` | `0xc26c...b8f4` | `LONG` | 6,311,275.46 USD | `1,579.95` | `4075.62` | `3994.60` | `0.000000` | -128,021.51 USD | `-2.03%` | `1X Cross` |
| `560` | `0x63da...8add` | `LONG` | 3,994,600.00 USD | `1,000.00` | `4021.46` | `3994.60` | `3564.32` | -26,860.96 USD | `-0.67%` | `25X Cross` |
| `572` | `0xf3dc...1672` | `LONG` | 3,930,881.89 USD | `984.27` | `4018.39` | `3994.60` | `2902.06` | -24,304.80 USD | `-0.62%` | `20X Cross` |
| `584` | `0x9aa5...58af` | `LONG` | 3,881,321.13 USD | `971.64` | `4279.98` | `3994.60` | `0.000000` | -277,287.95 USD | `-7.14%` | `20X Cross` |
| `590` | `0x354b...6425` | `LONG` | 3,850,239.55 USD | `963.86` | `4004.93` | `3994.60` | `0.000000` | -9,961.41 USD | `-0.26%` | `10X Cross` |
| `676` | `0x4a20...3c26` | `LONG` | 3,345,076.84 USD | `837.40` | `4599.73` | `3994.60` | `0.000000` | -506,743.54 USD | `-15.15%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,742,232.98 USD | `686.49` | `4290.34` | `3994.60` | `1274.35` | -203,025.72 USD | `-7.40%` | `25X Cross` |
| `914` | `0x625e...a354` | `SHORT` | 2,476,094.00 USD | `620.00` | `4122.81` | `3994.60` | `4342.45` | 80,053.03 USD | `+3.23%` | `20X Cross` |
| `919` | `0xd8c5...99b0` | `SHORT` | 2,470,080.48 USD | `618.35` | `4175.35` | `3994.60` | `34172.83` | 111,772.12 USD | `+4.53%` | `4X Cross` |
| `940` | `0xeae3...e8ad` | `SHORT` | 2,396,760.00 USD | `600.00` | `4104.77` | `3994.60` | `4325.47` | 66,105.11 USD | `+2.76%` | `20X Cross` |
| `943` | `0xf285...fa82` | `LONG` | 2,389,193.83 USD | `598.11` | `4146.45` | `3994.60` | `3891.45` | -90,825.72 USD | `-3.80%` | `25X Cross` |
| `959` | `0x12f7...8750` | `LONG` | 2,339,280.50 USD | `585.61` | `4082.77` | `3994.60` | `2633.79` | -51,636.48 USD | `-2.21%` | `10X Cross` |
| `1100` | `0x413c...886c` | `LONG` | 1,997,300.00 USD | `500.00` | `4010.43` | `3994.60` | `0.000000` | -7,916.23 USD | `-0.40%` | `2X Cross` |
| `1103` | `0x9c06...0560` | `LONG` | 1,990,977.75 USD | `498.42` | `4012.76` | `3994.60` | `0.000000` | -9,053.75 USD | `-0.45%` | `25X Cross` |
| `1107` | `0x61ce...a62b` | `SHORT` | 1,987,327.48 USD | `497.50` | `4071.66` | `3994.60` | `4718.36` | 38,341.31 USD | `+1.93%` | `20X Cross` |
| `1182` | `0x2edd...8179` | `LONG` | 1,879,540.25 USD | `469.89` | `4164.68` | `4001.36` | `0.000000` | -77,392.26 USD | `-4.12%` | `10X Cross` |
| `1222` | `0xead5...69f2` | `LONG` | 1,812,276.76 USD | `453.78` | `4220.88` | `3994.60` | `3539.15` | -103,091.30 USD | `-5.69%` | `5X Isolated` |
| `1285` | `0x7a6d...f79c` | `SHORT` | 1,713,558.84 USD | `428.38` | `4136.09` | `4001.36` | `5201.22` | 58,256.17 USD | `+3.40%` | `10X Cross` |
| `1290` | `0x46fc...1195` | `LONG` | 1,693,515.86 USD | `423.95` | `4053.27` | `3994.60` | `2158.73` | -24,874.21 USD | `-1.47%` | `20X Cross` |
| `1362` | `0xee02...309d` | `SHORT` | 1,597,840.00 USD | `400.00` | `4438.84` | `3994.60` | `4227.09` | 177,698.60 USD | `+11.12%` | `25X Isolated` |
| `1363` | `0x6d15...d374` | `LONG` | 1,597,480.00 USD | `400.00` | `4068.25` | `3994.60` | `3842.02` | -29,820.00 USD | `-1.87%` | `25X Cross` |
| `1406` | `0x51f6...2b39` | `LONG` | 1,561,294.24 USD | `390.33` | `4228.91` | `4001.36` | `589.81` | -89,358.85 USD | `-5.72%` | `10X Cross` |
| `1409` | `0x02a7...fe9f` | `SHORT` | 1,557,894.00 USD | `390.00` | `4055.02` | `3994.60` | `4306.91` | 23,565.25 USD | `+1.51%` | `25X Cross` |
| `1448` | `0x7e77...b8d2` | `SHORT` | 1,517,948.00 USD | `380.00` | `4131.92` | `3994.60` | `4293.71` | 52,181.64 USD | `+3.44%` | `20X Cross` |
| `1466` | `0x72c2...9b37` | `LONG` | 1,490,510.29 USD | `373.13` | `4000.98` | `3994.60` | `3778.25` | -2,383.22 USD | `-0.16%` | `13X Isolated` |
| `1504` | `0x781e...96b7` | `SHORT` | 1,444,476.11 USD | `361.11` | `4363.51` | `4001.36` | `13206.75` | 131,230.53 USD | `+9.08%` | `10X Cross` |
| `1512` | `0xaa44...b844` | `LONG` | 1,438,056.00 USD | `360.00` | `4043.10` | `3994.60` | `2818.36` | -17,461.63 USD | `-1.21%` | `4X Cross` |
| `1619` | `0xa41f...d50a` | `LONG` | 1,313,775.94 USD | `328.96` | `4468.89` | `3994.60` | `3802.38` | -156,321.91 USD | `-11.90%` | `15X Cross` |
| `1632` | `0x7fda...17d1` | `SHORT` | 1,301,729.49 USD | `325.87` | `4013.13` | `3994.60` | `30407.47` | 6,038.82 USD | `+0.46%` | `20X Cross` |
| `1666` | `0xbf5a...88ba` | `SHORT` | 1,268,904.26 USD | `317.65` | `4091.80` | `3994.60` | `9824.22` | 30,878.77 USD | `+2.43%` | `20X Cross` |
| `1702` | `0xff31...ff6c` | `SHORT` | 1,238,047.00 USD | `310.00` | `4372.43` | `3994.60` | `4789.38` | 117,408.38 USD | `+9.48%` | `10X Isolated` |
| `1729` | `0xada6...6f88` | `LONG` | 1,212,079.16 USD | `303.50` | `4166.46` | `3994.60` | `1784.39` | -52,433.70 USD | `-4.33%` | `5X Cross` |
| `1894` | `0x50e2...d770` | `LONG` | 1,080,009.62 USD | `270.37` | `4243.58` | `3994.60` | `2562.31` | -67,316.84 USD | `-6.23%` | `20X Cross` |
| `1912` | `0x4c92...4f17` | `SHORT` | 1,065,441.71 USD | `266.72` | `4260.98` | `3994.60` | `6509.84` | 71,050.53 USD | `+6.67%` | `20X Cross` |
| `1985` | `0xd346...c4f3` | `LONG` | 1,019,317.26 USD | `255.17` | `4188.66` | `3994.60` | `3310.63` | -49,519.25 USD | `-4.86%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.43` (Vol: 350,100.00 USD, Dist: `+2.45%`) | Long MP=`3949.75` (Vol: 346,900.00 USD, Dist: `--1.22%`)
  * 48H Horizon: Short MP=`4110.89` (Vol: 346,900.00 USD, Dist: `+2.81%`) | Long MP=`3950.25` (Vol: 348,600.00 USD, Dist: `--1.21%`)
  * 3D Horizon: Short MP=`4110.89` (Vol: 386,200.00 USD, Dist: `+2.81%`) | Long MP=`3950.25` (Vol: 373,700.00 USD, Dist: `--1.21%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 893,800.00 USD, Dist: `+2.82%`) | Long MP=`3923.02` (Vol: 1,000,000.00 USD, Dist: `--1.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3596.10` | 16,520,000.00 USD | 16,520,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.60` | 4,680,000.00 USD | 4,680,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.40` | 16,490,000.00 USD | 16,490,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.70` | 4,670,000.00 USD | 4,670,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.70` | 16,320,000.00 USD | 16,320,000.00 USD | 183,060.00 USD | 0.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.80` | 4,610,000.00 USD | 4,610,000.00 USD | 30,680.00 USD | 0.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.00` | 16,070,000.00 USD | 16,070,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.90` | 4,570,000.00 USD | 4,570,000.00 USD | 19,350.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.30` | 15,880,000.00 USD | 15,880,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.00` | 4,550,000.00 USD | 4,550,000.00 USD | 37,500.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.60` | 15,770,000.00 USD | 15,770,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.10` | 4,500,000.00 USD | 4,500,000.00 USD | 41,050.00 USD | 0.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.90` | 15,660,000.00 USD | 15,660,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.20` | 4,450,000.00 USD | 4,450,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.20` | 15,580,000.00 USD | 15,580,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.30` | 4,370,000.00 USD | 4,370,000.00 USD | 40,050.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.50` | 15,490,000.00 USD | 15,490,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 4,330,000.00 USD | 4,330,000.00 USD | 29,160.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.80` | 15,380,000.00 USD | 15,380,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.50` | 4,290,000.00 USD | 4,290,000.00 USD | 14,010.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.10` | 15,280,000.00 USD | 15,280,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.60` | 4,280,000.00 USD | 4,280,000.00 USD | 7,770.00 USD | 0.00 USD | 473.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.40` | 15,230,000.00 USD | 15,230,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.70` | 4,270,000.00 USD | 4,270,000.00 USD | 3,000.00 USD | 0.00 USD | 426.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.70` | 15,170,000.00 USD | 15,170,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.00` | 15,150,000.00 USD | 15,150,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.30` | 15,110,000.00 USD | 15,110,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.60` | 15,070,000.00 USD | 15,070,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3664.90` | 15,050,000.00 USD | 15,050,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 15,040,000.00 USD | 15,040,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.60` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3836.90` | 15,030,000.00 USD | 15,030,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.50` | 4,260,000.00 USD | 4,260,000.00 USD | 63,550.00 USD | 0.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.20` | 14,830,000.00 USD | 14,830,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.60` | 4,150,000.00 USD | 4,150,000.00 USD | 104,620.00 USD | 0.00 USD | 88,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.50` | 14,170,000.00 USD | 14,170,000.00 USD | 464,270.00 USD | 0.00 USD | 176,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.70` | 3,960,000.00 USD | 3,960,000.00 USD | 38,210.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,530,000.00 USD | 13,530,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.80` | 3,910,000.00 USD | 3,910,000.00 USD | 91,670.00 USD | 0.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.10` | 12,990,000.00 USD | 12,990,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.90` | 3,790,000.00 USD | 3,790,000.00 USD | 90,850.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.40` | 12,690,000.00 USD | 12,690,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.00` | 3,690,000.00 USD | 3,690,000.00 USD | 159,360.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.70` | 12,280,000.00 USD | 12,280,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.10` | 3,490,000.00 USD | 3,490,000.00 USD | 227,140.00 USD | 0.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.00` | 12,040,000.00 USD | 12,040,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.20` | 3,240,000.00 USD | 3,240,000.00 USD | 147,850.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.30` | 11,750,000.00 USD | 11,750,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.30` | 3,070,000.00 USD | 3,070,000.00 USD | 116,040.00 USD | 0.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.60` | 11,430,000.00 USD | 11,430,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.40` | 2,940,000.00 USD | 2,940,000.00 USD | 53,580.00 USD | 0.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.90` | 11,050,000.00 USD | 11,050,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.50` | 2,880,000.00 USD | 2,880,000.00 USD | 21,640.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.20` | 10,720,000.00 USD | 10,720,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.60` | 2,860,000.00 USD | 2,860,000.00 USD | 13,610.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,570,000.00 USD | 10,570,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.80` | 10,460,000.00 USD | 10,460,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.10` | 10,330,000.00 USD | 10,330,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.40` | 10,220,000.00 USD | 10,220,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.70` | 10,130,000.00 USD | 10,130,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.00` | 10,060,000.00 USD | 10,060,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3918.40` | 2,840,000.00 USD | 2,840,000.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.60` | 10,020,000.00 USD | 10,020,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.50` | 2,790,000.00 USD | 2,790,000.00 USD | 173,860.00 USD | 0.00 USD | 197,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.90` | 9,120,000.00 USD | 9,120,000.00 USD | 1,010,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.60` | 2,420,000.00 USD | 2,420,000.00 USD | 159,980.00 USD | 0.00 USD | 92,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.20` | 7,740,000.00 USD | 7,740,000.00 USD | 1,030,000.00 USD | 0.00 USD | 253,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.70` | 2,170,000.00 USD | 2,170,000.00 USD | 75,170.00 USD | 0.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 6,460,000.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.80` | 2,070,000.00 USD | 2,070,000.00 USD | 202,630.00 USD | 0.00 USD | 52,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.80` | 5,710,000.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.90` | 1,810,000.00 USD | 1,810,000.00 USD | 235,360.00 USD | 0.00 USD | 20,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.10` | 4,800,000.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.00` | 1,550,000.00 USD | 1,550,000.00 USD | 322,690.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.40` | 4,410,000.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.10` | 1,170,000.00 USD | 1,170,000.00 USD | 394,220.00 USD | 0.00 USD | 58,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.70` | 3,860,000.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.20` | 714,120.00 USD | 714,120.00 USD | 307,490.00 USD | 0.00 USD | 36,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.00` | 3,200,000.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.30` | 370,200.00 USD | 370,200.00 USD | 175,480.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.30` | 2,580,000.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.40` | 165,250.00 USD | 165,250.00 USD | 104,950.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,820,000.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.50` | 57,290.00 USD | 57,290.00 USD | 33,020.00 USD | 0.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.90` | 1,320,000.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.60` | 21,300.00 USD | 21,300.00 USD | 18,860.00 USD | 0.00 USD | 2,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.20` | 1,050,000.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.50` | 831,670.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.80` | 579,930.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.10` | 237,060.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.40` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.70` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.30` | 52,560.00 USD | 52,560.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4082.40` | 379,810.00 USD | 379,810.00 USD | 173,860.00 USD | 0.00 USD | 153,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.30` | 3,130,000.00 USD | 3,130,000.00 USD | 837,170.00 USD | 0.00 USD | 319,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4086.50` | 676,260.00 USD | 676,260.00 USD | 159,980.00 USD | 0.00 USD | 136,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.60` | 742,610.00 USD | 742,610.00 USD | 40,700.00 USD | 0.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.60` | 4,090,000.00 USD | 4,090,000.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.70` | 1,020,000.00 USD | 1,020,000.00 USD | 230,830.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 4,690,000.00 USD | 4,690,000.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.80` | 1,220,000.00 USD | 1,220,000.00 USD | 176,660.00 USD | 0.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.20` | 5,440,000.00 USD | 5,440,000.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.90` | 1,560,000.00 USD | 1,560,000.00 USD | 281,430.00 USD | 0.00 USD | 61,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 5,930,000.00 USD | 5,930,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.00` | 2,060,000.00 USD | 2,060,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.80` | 6,530,000.00 USD | 6,530,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.10` | 2,390,000.00 USD | 2,390,000.00 USD | 288,670.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.10` | 7,000,000.00 USD | 7,000,000.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.20` | 2,640,000.00 USD | 2,640,000.00 USD | 219,460.00 USD | 0.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.40` | 7,620,000.00 USD | 7,620,000.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.30` | 2,760,000.00 USD | 2,760,000.00 USD | 109,720.00 USD | 0.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 8,420,000.00 USD | 8,420,000.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.40` | 2,810,000.00 USD | 2,810,000.00 USD | 48,610.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.00` | 8,850,000.00 USD | 8,850,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.50` | 2,840,000.00 USD | 2,840,000.00 USD | 31,940.00 USD | 0.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.30` | 9,030,000.00 USD | 9,030,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.60` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 538.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.60` | 9,280,000.00 USD | 9,280,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4137.90` | 9,510,000.00 USD | 9,510,000.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 9,790,000.00 USD | 9,790,000.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.50` | 9,850,000.00 USD | 9,850,000.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.80` | 9,980,000.00 USD | 9,980,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.10` | 10,050,000.00 USD | 10,050,000.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.40` | 10,530,000.00 USD | 10,530,000.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.30` | 2,920,000.00 USD | 2,920,000.00 USD | 44,720.00 USD | 0.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.70` | 11,220,000.00 USD | 11,220,000.00 USD | 518,390.00 USD | 0.00 USD | 175,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.40` | 3,120,000.00 USD | 3,120,000.00 USD | 108,490.00 USD | 0.00 USD | 85,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.00` | 11,810,000.00 USD | 11,810,000.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.50` | 3,200,000.00 USD | 3,200,000.00 USD | 53,170.00 USD | 0.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.30` | 12,180,000.00 USD | 12,180,000.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4172.60` | 3,270,000.00 USD | 3,270,000.00 USD | 56,270.00 USD | 0.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.60` | 12,630,000.00 USD | 12,630,000.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.70` | 3,400,000.00 USD | 3,400,000.00 USD | 106,840.00 USD | 0.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.80` | 3,510,000.00 USD | 3,510,000.00 USD | 99,350.00 USD | 0.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.90` | 12,820,000.00 USD | 12,820,000.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.90` | 3,690,000.00 USD | 3,690,000.00 USD | 150,530.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.20` | 13,050,000.00 USD | 13,050,000.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.00` | 3,930,000.00 USD | 3,930,000.00 USD | 210,710.00 USD | 0.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.50` | 13,340,000.00 USD | 13,340,000.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.10` | 4,080,000.00 USD | 4,080,000.00 USD | 131,880.00 USD | 0.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4193.80` | 13,630,000.00 USD | 13,630,000.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.20` | 4,180,000.00 USD | 4,180,000.00 USD | 87,740.00 USD | 0.00 USD | 14,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.10` | 13,960,000.00 USD | 13,960,000.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.30` | 4,230,000.00 USD | 4,230,000.00 USD | 47,190.00 USD | 0.00 USD | 1,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.40` | 14,260,000.00 USD | 14,260,000.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.40` | 4,250,000.00 USD | 4,250,000.00 USD | 21,790.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.70` | 14,470,000.00 USD | 14,470,000.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.50` | 4,260,000.00 USD | 4,260,000.00 USD | 9,430.00 USD | 0.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,560,000.00 USD | 14,560,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.30` | 14,680,000.00 USD | 14,680,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.60` | 14,800,000.00 USD | 14,800,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.90` | 14,920,000.00 USD | 14,920,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.20` | 14,950,000.00 USD | 14,950,000.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.50` | 15,020,000.00 USD | 15,020,000.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.80` | 15,040,000.00 USD | 15,040,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.90` | 15,100,000.00 USD | 15,100,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4398.10` | 4,270,000.00 USD | 4,270,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.20` | 15,230,000.00 USD | 15,230,000.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4402.20` | 4,310,000.00 USD | 4,310,000.00 USD | 14,970.00 USD | 0.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.50` | 15,430,000.00 USD | 15,430,000.00 USD | 148,770.00 USD | 0.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4406.30` | 4,360,000.00 USD | 4,360,000.00 USD | 28,040.00 USD | 0.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4408.20` | 4,370,000.00 USD | 4,370,000.00 USD | 11,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.80` | 15,620,000.00 USD | 15,620,000.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.10` | 15,700,000.00 USD | 15,700,000.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.40` | 15,800,000.00 USD | 15,800,000.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.70` | 15,890,000.00 USD | 15,890,000.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.00` | 15,960,000.00 USD | 15,960,000.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,030,000.00 USD | 16,030,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.60` | 16,090,000.00 USD | 16,090,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.90` | 16,180,000.00 USD | 16,180,000.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4440.70` | 16,230,000.00 USD | 16,230,000.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |

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
| `7D` | `3596.10` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3598.60` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3600.40` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD |
| `1D` | `3602.70` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD |
| `7D` | `3604.70` | 16,320,000.00 USD | 0.00 USD | 16,320,000.00 USD | 183,060.00 USD | 0.00 USD | 69,070.00 USD |
| `1D` | `3606.80` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 30,680.00 USD | 0.00 USD | 11,510.00 USD |
| `7D` | `3609.00` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD |
| `1D` | `3610.90` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 19,350.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `3613.30` | 15,880,000.00 USD | 0.00 USD | 15,880,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3615.00` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 37,500.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `3617.60` | 15,770,000.00 USD | 0.00 USD | 15,770,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3619.10` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 41,050.00 USD | 0.00 USD | 7,170.00 USD |
| `7D` | `3621.90` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3623.20` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD |
| `7D` | `3626.20` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.30` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 40,050.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `3630.50` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.40` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 29,160.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3634.80` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `3635.50` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 14,010.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3639.10` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD |
| `1D` | `3639.60` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 7,770.00 USD | 0.00 USD | 473.15 USD |
| `7D` | `3643.40` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `3643.70` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 3,000.00 USD | 0.00 USD | 426.17 USD |
| `7D` | `3647.70` | 15,170,000.00 USD | 0.00 USD | 15,170,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.00` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.30` | 15,110,000.00 USD | 0.00 USD | 15,110,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.60` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3664.90` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.60` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3836.90` | 15,030,000.00 USD | 0.00 USD | 15,030,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `3840.50` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 63,550.00 USD | 0.00 USD | 49,950.00 USD |
| `7D` | `3841.20` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD |
| `1D` | `3844.60` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 104,620.00 USD | 0.00 USD | 88,140.00 USD |
| `7D` | `3845.50` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 464,270.00 USD | 0.00 USD | 176,560.00 USD |
| `1D` | `3848.70` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 38,210.00 USD | 0.00 USD | 12,500.00 USD |
| `7D` | `3849.80` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD |
| `1D` | `3852.80` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 91,670.00 USD | 0.00 USD | 20,560.00 USD |
| `7D` | `3854.10` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD |
| `1D` | `3856.90` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 90,850.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `3858.40` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD |
| `1D` | `3861.00` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 159,360.00 USD | 0.00 USD | 34,910.00 USD |
| `7D` | `3862.70` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3865.10` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 227,140.00 USD | 0.00 USD | 29,260.00 USD |
| `7D` | `3867.00` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3869.20` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 147,850.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `3871.30` | 11,750,000.00 USD | 0.00 USD | 11,750,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3873.30` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 116,040.00 USD | 0.00 USD | 16,210.00 USD |
| `7D` | `3875.60` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD |
| `1D` | `3877.40` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 53,580.00 USD | 0.00 USD | 4,010.00 USD |
| `7D` | `3879.90` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD |
| `1D` | `3881.50` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 21,640.00 USD | 0.00 USD | 1,090.00 USD |
| `7D` | `3884.20` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3885.60` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 13,610.00 USD | 0.00 USD | 1,890.00 USD |
| `7D` | `3888.50` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3892.80` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.10` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.40` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.70` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.00` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `1D` | `3918.40` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3918.60` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3922.50` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 173,860.00 USD | 0.00 USD | 197,850.00 USD |
| `7D` | `3922.90` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 1,010,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3926.60` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 159,980.00 USD | 0.00 USD | 92,020.00 USD |
| `7D` | `3927.20` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 1,030,000.00 USD | 0.00 USD | 253,110.00 USD |
| `1D` | `3930.70` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 75,170.00 USD | 0.00 USD | 25,650.00 USD |
| `7D` | `3931.50` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD |
| `1D` | `3934.80` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 202,630.00 USD | 0.00 USD | 52,410.00 USD |
| `7D` | `3935.80` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD |
| `1D` | `3938.90` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 235,360.00 USD | 0.00 USD | 20,510.00 USD |
| `7D` | `3940.10` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD |
| `1D` | `3943.00` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 322,690.00 USD | 0.00 USD | 64,870.00 USD |
| `7D` | `3944.40` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD |
| `1D` | `3947.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 394,220.00 USD | 0.00 USD | 58,690.00 USD |
| `7D` | `3948.70` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD |
| `1D` | `3951.20` | 714,120.00 USD | 0.00 USD | 714,120.00 USD | 307,490.00 USD | 0.00 USD | 36,430.00 USD |
| `7D` | `3953.00` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD |
| `1D` | `3955.30` | 370,200.00 USD | 0.00 USD | 370,200.00 USD | 175,480.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3957.30` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD |
| `1D` | `3959.40` | 165,250.00 USD | 0.00 USD | 165,250.00 USD | 104,950.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `3961.60` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3963.50` | 57,290.00 USD | 0.00 USD | 57,290.00 USD | 33,020.00 USD | 0.00 USD | 2,970.00 USD |
| `7D` | `3965.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `3967.60` | 21,300.00 USD | 0.00 USD | 21,300.00 USD | 18,860.00 USD | 0.00 USD | 2,440.00 USD |
| `7D` | `3970.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.50` | 831,670.00 USD | 0.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3978.80` | 579,930.00 USD | 0.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD |
| `7D` | `3983.10` | 237,060.00 USD | 0.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `7D` | `3987.40` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.70` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4001.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4001.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4078.30` | 52,560.00 USD | 52,560.00 USD | 0.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD |
| `1D` | `4082.40` | 379,810.00 USD | 379,810.00 USD | 0.00 USD | 173,860.00 USD | 0.00 USD | 153,400.00 USD |
| `7D` | `4086.30` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 837,170.00 USD | 0.00 USD | 319,180.00 USD |
| `1D` | `4086.50` | 676,260.00 USD | 676,260.00 USD | 0.00 USD | 159,980.00 USD | 0.00 USD | 136,470.00 USD |
| `1D` | `4090.60` | 742,610.00 USD | 742,610.00 USD | 0.00 USD | 40,700.00 USD | 0.00 USD | 25,650.00 USD |
| `7D` | `4090.60` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4094.70` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 230,830.00 USD | 0.00 USD | 44,470.00 USD |
| `7D` | `4094.90` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD |
| `1D` | `4098.80` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 176,660.00 USD | 0.00 USD | 26,080.00 USD |
| `7D` | `4099.20` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4102.90` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 281,430.00 USD | 0.00 USD | 61,690.00 USD |
| `7D` | `4103.50` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4107.00` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `4107.80` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4111.10` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 288,670.00 USD | 0.00 USD | 39,930.00 USD |
| `7D` | `4112.10` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD |
| `1D` | `4115.20` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 219,460.00 USD | 0.00 USD | 32,410.00 USD |
| `7D` | `4116.40` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD |
| `1D` | `4119.30` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 109,720.00 USD | 0.00 USD | 7,700.00 USD |
| `7D` | `4120.70` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4123.40` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 48,610.00 USD | 0.00 USD | 2,510.00 USD |
| `7D` | `4125.00` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `4127.50` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 31,940.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `4129.30` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `1D` | `4131.60` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 538.62 USD |
| `7D` | `4133.60` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4137.90` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.20` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD |
| `7D` | `4146.50` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4150.80` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.10` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.40` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD |
| `1D` | `4160.30` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 44,720.00 USD | 0.00 USD | 35,270.00 USD |
| `7D` | `4163.70` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 518,390.00 USD | 0.00 USD | 175,240.00 USD |
| `1D` | `4164.40` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 108,490.00 USD | 0.00 USD | 85,280.00 USD |
| `7D` | `4168.00` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4168.50` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 53,170.00 USD | 0.00 USD | 25,860.00 USD |
| `7D` | `4172.30` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD |
| `1D` | `4172.60` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 56,270.00 USD | 0.00 USD | 14,480.00 USD |
| `7D` | `4176.60` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD |
| `1D` | `4176.70` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 106,840.00 USD | 0.00 USD | 24,450.00 USD |
| `1D` | `4180.80` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 99,350.00 USD | 0.00 USD | 12,590.00 USD |
| `7D` | `4180.90` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4184.90` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 150,530.00 USD | 0.00 USD | 30,600.00 USD |
| `7D` | `4185.20` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD |
| `1D` | `4189.00` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 210,710.00 USD | 0.00 USD | 27,480.00 USD |
| `7D` | `4189.50` | 13,340,000.00 USD | 13,340,000.00 USD | 0.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD |
| `1D` | `4193.10` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 131,880.00 USD | 0.00 USD | 18,220.00 USD |
| `7D` | `4193.80` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4197.20` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 87,740.00 USD | 0.00 USD | 14,730.00 USD |
| `7D` | `4198.10` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4201.30` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 47,190.00 USD | 0.00 USD | 1,230.00 USD |
| `7D` | `4202.40` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4205.40` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 21,790.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4206.70` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD |
| `1D` | `4209.50` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 9,430.00 USD | 0.00 USD | 1,630.00 USD |
| `7D` | `4211.00` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `7D` | `4215.30` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.60` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4223.90` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.20` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `4232.50` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD |
| `7D` | `4236.80` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.90` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `1D` | `4398.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4400.20` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4402.20` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 14,970.00 USD | 0.00 USD | 24,530.00 USD |
| `7D` | `4404.50` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 148,770.00 USD | 0.00 USD | 53,870.00 USD |
| `1D` | `4406.30` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 28,040.00 USD | 0.00 USD | 22,800.00 USD |
| `1D` | `4408.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 11,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4408.80` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD |
| `7D` | `4413.10` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `4417.40` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD |
| `7D` | `4421.70` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4426.00` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD |
| `7D` | `4430.30` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `4434.60` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4438.90` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD |
| `7D` | `4440.70` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `276.18M` | Total OI Tokens: `69,025.6 PAXG`
  * 1h OI Change: `+0.32%` | 4h OI Change: `+0.48%` | 24h OI Change: `+0.82%`
  * Exchange Breakdown: Binance=`107.12M` | Bybit=`21.99M` | OKX=`-` | Hyperliquid=`24.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.20K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `48.49%` | `51.51%` | `0.94` | 5,550,000.00 USD |
| `15M` | `Binance` | `52.62%` | `47.38%` | `1.11` | 312,010.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `31.78%` | `68.22%` | `0.47` | 186,640.00 USD |
| `15M` | `KuCoin` | `18.01%` | `81.99%` | `0.22` | 13,090.00 USD |
| `15M` | `Gate` | `46.32%` | `53.68%` | `0.86` | 114,630.00 USD |
| `15M` | `Bitget` | `34.54%` | `65.46%` | `0.53` | 153,920.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `50.3%` | `49.7%` | `1.01` | 4,510,000.00 USD |
| `15M` | `Bitunix` | `26.66%` | `73.34%` | `0.36` | 93,040.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.49%` | `43.51%` | `1.30` | 118,910.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.73%` | `99.27%` | `0.01` | 48,970.00 USD |
| `15M` | `HTX` | `11.3%` | `88.7%` | `0.13` | 3,740.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `52.62%` | `47.38%` | `1.11` | 312,010.00 USD |
| `15M` | `Global Accounts` | `48.49%` | `51.51%` | `0.94` | 5,550,000.00 USD |
| `1H` | `PAXG` | `41.54%` | `58.46%` | `0.71` | 5,010,000.00 USD |
| `1H` | `Binance` | `56.57%` | `43.43%` | `1.30` | 1,470,000.00 USD |
| `1H` | `OKX` | `49.81%` | `50.19%` | `0.99` | 539,690.00 USD |
| `1H` | `Bybit` | `45.39%` | `54.61%` | `0.83` | 382,730.00 USD |
| `1H` | `KuCoin` | `48.66%` | `51.34%` | `0.95` | 185,250.00 USD |
| `1H` | `Gate` | `56.54%` | `43.46%` | `1.30` | 50,500.00 USD |
| `1H` | `Bitget` | `44.1%` | `55.9%` | `0.79` | 44,250.00 USD |
| `1H` | `BingX` | `5.77%` | `94.23%` | `0.06` | 1,200,000.00 USD |
| `1H` | `MEXC` | `44.47%` | `55.53%` | `0.80` | 226,130.00 USD |
| `1H` | `Bitunix` | `49.32%` | `50.68%` | `0.97` | 32,180.00 USD |
| `1H` | `Hyperliquid` | `77.19%` | `22.81%` | `3.38` | 15,510.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.83%` | `49.17%` | `1.03` | 778,280.00 USD |
| `1H` | `Crypto.com` | `0.07%` | `99.93%` | `0.00` | 689.16 USD |
| `1H` | `WhiteBIT` | `98.45%` | `1.55%` | `63.52` | 44,570.00 USD |
| `1H` | `HTX` | `68.03%` | `31.97%` | `2.13` | 425.46 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `81.19%` | `18.81%` | `4.32` | 52.90 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `77.68%` | `22.32%` | `3.48` | 36,110.00 USD |
| `1H` | `Whale Positions` | `56.57%` | `43.43%` | `1.30` | 1,470,000.00 USD |
| `1H` | `Global Accounts` | `41.54%` | `58.46%` | `0.71` | 5,010,000.00 USD |
| `4H` | `PAXG` | `43.12%` | `56.88%` | `0.76` | 26,120,000.00 USD |
| `4H` | `Binance` | `49.81%` | `50.19%` | `0.99` | 8,590,000.00 USD |
| `4H` | `OKX` | `50.36%` | `49.64%` | `1.01` | 2,370,000.00 USD |
| `4H` | `Bybit` | `51.31%` | `48.69%` | `1.05` | 2,690,000.00 USD |
| `4H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 1,080,000.00 USD |
| `4H` | `Gate` | `57.31%` | `42.69%` | `1.34` | 495,420.00 USD |
| `4H` | `Bitget` | `48.94%` | `51.06%` | `0.96` | 452,510.00 USD |
| `4H` | `BingX` | `9.14%` | `90.86%` | `0.10` | 4,460,000.00 USD |
| `4H` | `MEXC` | `49.16%` | `50.84%` | `0.97` | 913,710.00 USD |
| `4H` | `Bitunix` | `40.36%` | `59.64%` | `0.68` | 260,540.00 USD |
| `4H` | `Hyperliquid` | `49.64%` | `50.36%` | `0.99` | 144,650.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.23%` | `50.77%` | `0.97` | 4,410,000.00 USD |
| `4H` | `Crypto.com` | `19.22%` | `80.78%` | `0.24` | 3,420.00 USD |
| `4H` | `WhiteBIT` | `72.98%` | `27.02%` | `2.70` | 149,990.00 USD |
| `4H` | `HTX` | `54.19%` | `45.81%` | `1.18` | 9,540.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `22.68%` | `77.32%` | `0.29` | 37,580.00 USD |
| `4H` | `Aster` | `59.47%` | `40.53%` | `1.47` | 436.63 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `60.53%` | `39.47%` | `1.53` | 63,350.00 USD |
| `4H` | `Whale Positions` | `49.81%` | `50.19%` | `0.99` | 8,590,000.00 USD |
| `4H` | `Global Accounts` | `43.12%` | `56.88%` | `0.76` | 26,120,000.00 USD |


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
| `5m` | -34,100.00 USD | -301,960.00 USD | **`DISTRIBUTION`** |
| `15m` | -23,670.00 USD | -235,250.00 USD | **`DISTRIBUTION`** |
| `30m` | 49,170.00 USD | -249,020.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,290.00 USD | -267,780.00 USD | **`DISTRIBUTION`** |
| `2h` | -66,260.00 USD | -271,360.00 USD | **`DISTRIBUTION`** |
| `4h` | -76,380.00 USD | -706,260.00 USD | **`DISTRIBUTION`** |
| `6h` | 124,230.00 USD | -1,240,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,120,000.00 USD | -1,150,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,650,000.00 USD | -413,820.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,180,000.00 USD | -987,150.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,420,000.00 USD | -9,460,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,000,000.00 USD | -72,210,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-34.10K` | 15m=`-23.67K` | 1h=`+2.29K` | 24h=`-1.18M`
* Futures Capital Netflows: 5m=`-301.96K` | 15m=`-235.25K` | 1h=`-267.78K` | 24h=`-987.15K`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3996.71` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3987.42` (Risk Distance: `9.29` pts)
  * +2.5R Take Profit: `4019.93`
  * Mathematical Lot Sizing: **`1.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.61` (Risk Distance: `9.29` pts)
  * +2.5R Take Profit: `3990.10`
  * Mathematical Lot Sizing: **`1.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4023.23`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
