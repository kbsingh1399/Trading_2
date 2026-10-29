# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 01:14:46 IST` (`2026-10-29 19:44:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4018.77` | **Live Ask Quote**: `4018.85` | **Mid Price**: `4018.81`
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
  * Session VWAP: `4029.91` | VWAP Z-Score: `-1.11` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.07` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.59` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4065.70` | Lower -3.00σ Band: `3994.11`
  * Upper +2.51σ Band: `4059.86` | Lower -2.51σ Band: `3999.96`
  * Upper +2.01σ Band: `4053.89` | Lower -2.01σ Band: `4005.92`
  * Upper +2.00σ Band: `4053.77` | Lower -2.00σ Band: `4006.04`
  * Upper +1.28σ Band: `4045.18` | Lower -1.28σ Band: `4014.63`
  * Upper +1.00σ Band: `4041.84` | Lower -1.00σ Band: `4017.97`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4013.01` | EMA-20=`4016.16` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4023.14` (Slope: `+0.0000`) | EMA-100=`4030.00`
  * Institutional Anchors: EMA-144=`4031.71` | EMA-200=`4031.72` (Slope: `-0.0581`) | EMA-233=`4030.88`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.95` (Distance: `-0.54%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.21%`)
  * Value Area Low (VAL) = `4016.67` (Distance: `+0.06%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `4002.73` - `4034.89`
  * Optimal Trade Entry (OTE 0.705): `4026.85`
  * Structural Invalidation Anchor (0.786): `4050.96`

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
| `BID` | `4017.80` | `14.8325` | 59,594.02 USD | 1,623,259.69 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `4017.90` | `1.4084` | 5,658.81 USD | 1,563,665.67 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `4018.00` | `1.5435` | 6,201.78 USD | 1,558,006.86 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4018.10` | `2.0583` | 8,270.46 USD | 1,551,805.07 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `4018.20` | `79.0551` | 317,659.20 USD | 1,543,534.62 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `4018.30` | `83.2221` | 334,411.36 USD | 1,225,875.42 USD | `5 orders` | `-0.05%` | `-` |
| `BID` | `4018.40` | `26.9259` | 108,199.04 USD | 891,464.05 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4018.50` | `15.1072` | 60,708.28 USD | 783,265.02 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4018.60` | `11.7724` | 47,308.57 USD | 722,556.73 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4018.80` | `3.8194` | 15,349.40 USD | 675,248.17 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4018.90` | `12.8841` | 51,779.91 USD | 659,898.76 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4019.00` | `0.3178` | 1,277.24 USD | 608,118.85 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4019.10` | `2.9842` | 11,993.80 USD | 606,841.61 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4019.20` | `65.0272` | 261,357.32 USD | 594,847.81 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `4019.30` | `10.1013` | 40,600.16 USD | 333,490.49 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4019.40` | `28.1305` | 113,067.73 USD | 292,890.34 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4019.60` | `11.0724` | 44,506.62 USD | 179,822.61 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4019.70` | `0.2487` | 999.70 USD | 135,315.99 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4019.80` | `24.8760` | 99,996.54 USD | 134,316.29 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4020.40` | `8.5364` | 34,319.74 USD | 34,319.74 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4020.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,020.45` | `0.00%` | `-` |
| `ASK` | `4020.50` | `14.8075` | 59,533.55 USD | 59,533.55 USD | `12 orders` | `+0.00%` | `-` |
| `ASK` | `4020.60` | `15.6682` | 62,995.56 USD | 122,529.12 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4020.70` | `2.4812` | 9,976.16 USD | 132,505.28 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4020.80` | `16.0837` | 64,669.34 USD | 197,174.62 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4020.90` | `12.3438` | 49,633.19 USD | 246,807.81 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4021.00` | `73.0742` | 293,831.36 USD | 540,639.16 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `4021.10` | `32.1306` | 129,200.36 USD | 669,839.52 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4021.20` | `5.1173` | 20,577.69 USD | 690,417.21 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4021.30` | `10.3400` | 41,580.24 USD | 731,997.45 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4021.40` | `52.5905` | 211,487.44 USD | 943,484.89 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `4021.50` | `7.5669` | 30,430.29 USD | 973,915.17 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4021.60` | `6.1831` | 24,865.95 USD | 998,781.13 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4021.70` | `19.9738` | 80,328.63 USD | 1,079,109.76 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4021.90` | `23.3876` | 94,062.59 USD | 1,173,172.35 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `4022.00` | `52.9416` | 212,931.12 USD | 1,386,103.46 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4022.10` | `12.4881` | 50,228.39 USD | 1,436,331.85 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4022.20` | `4.9341` | 19,845.94 USD | 1,456,177.79 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4022.30` | `10.3591` | 41,667.41 USD | 1,497,845.20 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4022.40` | `13.3607` | 53,742.08 USD | 1,551,587.28 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4022.50` | `2.8739` | 11,560.26 USD | 1,563,147.54 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,606,924.88 USD | `6,373.21` | `4191.43` | `4017.80` | `29294.99` | 1,105,999.37 USD | `+4.32%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,355,616.89 USD | `6,310.66` | `4133.85` | `4017.80` | `13286.73` | 731,774.93 USD | `+2.89%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,967,142.73 USD | `5,717.06` | `4234.49` | `4017.80` | `27625.73` | 1,241,732.50 USD | `+5.41%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,399,167.69 USD | `4,828.91` | `4157.43` | `4017.80` | `2088.49` | -676,714.63 USD | `-3.49%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,138,217.94 USD | `3,518.90` | `4129.56` | `4017.80` | `295.02` | -393,276.64 USD | `-2.78%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,131,026.99 USD | `3,268.21` | `4228.94` | `4017.80` | `4409.10` | 690,052.14 USD | `+5.26%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,651,910.40 USD | `2,900.00` | `4364.92` | `4017.80` | `4235.62` | 1,006,365.93 USD | `+8.64%` | `20X Cross` |
| `276` | `0x3678...b209` | `LONG` | 8,839,160.00 USD | `2,200.00` | `4176.09` | `4017.80` | `2490.23` | -348,259.30 USD | `-3.94%` | `25X Cross` |
| `277` | `0x41e5...0825` | `SHORT` | 8,838,060.00 USD | `2,200.00` | `4112.20` | `4017.80` | `4331.10` | 208,794.59 USD | `+2.36%` | `20X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,983,123.72 USD | `1,986.89` | `4032.86` | `4017.80` | `24965.12` | 29,742.45 USD | `+0.37%` | `3X Cross` |
| `312` | `0xacb6...efbd` | `SHORT` | 7,935,650.29 USD | `1,975.37` | `4048.55` | `4017.80` | `6496.21` | 61,741.43 USD | `+0.78%` | `6X Cross` |
| `382` | `0xc26c...b8f4` | `LONG` | 6,347,930.34 USD | `1,579.95` | `4075.62` | `4017.80` | `0.000000` | -91,366.63 USD | `-1.44%` | `1X Cross` |
| `420` | `0x12d2...f97f` | `LONG` | 5,632,024.81 USD | `1,401.94` | `4278.91` | `4017.80` | `2510.26` | -366,765.77 USD | `-6.51%` | `20X Cross` |
| `574` | `0x63da...8add` | `LONG` | 4,017,800.00 USD | `1,000.00` | `4021.46` | `4017.80` | `3564.06` | -3,660.96 USD | `-0.09%` | `25X Cross` |
| `596` | `0x9aa5...58af` | `LONG` | 3,903,377.41 USD | `971.64` | `4279.98` | `4017.80` | `0.000000` | -255,231.68 USD | `-6.54%` | `20X Cross` |
| `625` | `0xf3dc...1672` | `LONG` | 3,739,355.89 USD | `930.74` | `4024.62` | `4017.80` | `3337.54` | -6,536.67 USD | `-0.17%` | `20X Cross` |
| `687` | `0x4a20...3c26` | `LONG` | 3,364,504.51 USD | `837.40` | `4599.73` | `4017.80` | `0.000000` | -487,315.87 USD | `-14.48%` | `20X Cross` |
| `702` | `0x354b...6425` | `LONG` | 3,298,036.56 USD | `820.84` | `4033.57` | `4017.80` | `0.000000` | -12,865.05 USD | `-0.39%` | `10X Cross` |
| `843` | `0x0fac...7a0a` | `LONG` | 2,758,228.08 USD | `686.49` | `4290.34` | `4017.80` | `1360.30` | -187,030.62 USD | `-6.78%` | `25X Cross` |
| `888` | `0xd8c5...99b0` | `SHORT` | 2,580,853.52 USD | `642.35` | `4175.35` | `4017.80` | `32023.22` | 101,207.66 USD | `+3.92%` | `4X Cross` |
| `922` | `0x625e...a354` | `SHORT` | 2,490,726.00 USD | `620.00` | `4122.81` | `4017.80` | `4342.20` | 65,421.03 USD | `+2.63%` | `20X Cross` |
| `948` | `0xeae3...e8ad` | `SHORT` | 2,410,680.00 USD | `600.00` | `4104.77` | `4017.80` | `4325.22` | 52,185.11 USD | `+2.16%` | `20X Cross` |
| `951` | `0xf285...fa82` | `LONG` | 2,403,129.70 USD | `598.11` | `4146.45` | `4017.80` | `3891.19` | -76,889.86 USD | `-3.20%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,352,866.67 USD | `585.61` | `4082.77` | `4017.80` | `2153.70` | -38,050.31 USD | `-1.62%` | `10X Cross` |
| `1124` | `0x413c...886c` | `LONG` | 2,008,800.00 USD | `500.00` | `4010.43` | `4017.80` | `0.000000` | 3,583.77 USD | `+0.18%` | `2X Cross` |
| `1139` | `0x61ce...a62b` | `SHORT` | 1,998,770.06 USD | `497.50` | `4071.66` | `4017.80` | `4692.26` | 26,898.73 USD | `+1.35%` | `20X Cross` |
| `1146` | `0x0593...40f9` | `LONG` | 1,993,539.95 USD | `496.18` | `4024.57` | `4017.80` | `3701.68` | -3,363.88 USD | `-0.17%` | `10X Isolated` |
| `1262` | `0x2edd...8179` | `LONG` | 1,823,815.91 USD | `453.58` | `4169.95` | `4020.90` | `0.000000` | -67,608.21 USD | `-3.71%` | `10X Cross` |
| `1264` | `0xead5...69f2` | `LONG` | 1,822,986.06 USD | `453.78` | `4220.88` | `4017.80` | `3538.89` | -92,382.00 USD | `-5.07%` | `5X Isolated` |
| `1323` | `0x7a6d...f79c` | `SHORT` | 1,722,236.94 USD | `428.38` | `4136.09` | `4020.90` | `5892.61` | 49,578.07 USD | `+2.88%` | `10X Cross` |
| `1390` | `0x46fc...1195` | `LONG` | 1,635,399.81 USD | `407.03` | `4055.53` | `4017.80` | `1947.08` | -15,320.01 USD | `-0.94%` | `20X Cross` |
| `1426` | `0xee02...309d` | `SHORT` | 1,607,160.00 USD | `400.00` | `4438.84` | `4017.80` | `4226.84` | 168,378.60 USD | `+10.48%` | `25X Isolated` |
| `1427` | `0x6d15...d374` | `LONG` | 1,606,920.00 USD | `400.00` | `4068.25` | `4017.80` | `3841.76` | -20,380.00 USD | `-1.27%` | `25X Cross` |
| `1452` | `0x02a7...fe9f` | `SHORT` | 1,566,942.00 USD | `390.00` | `4055.02` | `4017.80` | `4306.66` | 14,517.25 USD | `+0.93%` | `25X Cross` |
| `1487` | `0x51f6...2b39` | `LONG` | 1,529,858.11 USD | `380.49` | `4234.66` | `4020.90` | `0.000000` | -81,369.96 USD | `-5.32%` | `10X Cross` |
| `1491` | `0x7e77...b8d2` | `SHORT` | 1,526,764.00 USD | `380.00` | `4131.92` | `4017.80` | `4293.46` | 43,365.64 USD | `+2.84%` | `20X Cross` |
| `1509` | `0x72c2...9b37` | `LONG` | 1,499,092.31 USD | `373.13` | `4000.98` | `4017.80` | `3777.99` | 6,198.80 USD | `+0.41%` | `13X Isolated` |
| `1547` | `0xaa44...b844` | `LONG` | 1,446,336.00 USD | `360.00` | `4043.10` | `4017.80` | `2803.21` | -9,181.63 USD | `-0.63%` | `4X Cross` |
| `1548` | `0x781e...96b7` | `SHORT` | 1,445,534.82 USD | `359.55` | `4365.03` | `4020.90` | `12721.02` | 123,912.66 USD | `+8.57%` | `10X Cross` |
| `1658` | `0xa41f...d50a` | `LONG` | 1,321,539.44 USD | `328.96` | `4468.89` | `4017.80` | `3833.14` | -148,558.41 USD | `-11.24%` | `15X Cross` |
| `1683` | `0x49e9...e1d0` | `SHORT` | 1,300,020.88 USD | `323.56` | `4025.23` | `4017.80` | `28790.63` | 2,371.82 USD | `+0.18%` | `4X Cross` |
| `1712` | `0xada6...6f88` | `LONG` | 1,282,721.65 USD | `319.28` | `4166.46` | `4017.80` | `1867.19` | -47,528.86 USD | `-3.71%` | `5X Cross` |
| `1719` | `0xbf5a...88ba` | `SHORT` | 1,276,115.03 USD | `317.65` | `4091.80` | `4017.80` | `10495.54` | 23,668.00 USD | `+1.85%` | `20X Cross` |
| `1740` | `0xff31...ff6c` | `SHORT` | 1,245,518.00 USD | `310.00` | `4372.43` | `4017.80` | `4789.13` | 109,937.38 USD | `+8.83%` | `10X Isolated` |
| `1906` | `0x50e2...d770` | `LONG` | 1,086,282.14 USD | `270.37` | `4243.58` | `4017.80` | `2562.05` | -61,044.32 USD | `-5.62%` | `20X Cross` |
| `1918` | `0x4c92...4f17` | `SHORT` | 1,071,629.62 USD | `266.72` | `4260.98` | `4017.80` | `6523.15` | 64,862.61 USD | `+6.05%` | `20X Cross` |
| `1993` | `0xd346...c4f3` | `LONG` | 1,025,262.81 USD | `255.17` | `4188.66` | `4017.90` | `3310.37` | -43,573.70 USD | `-4.25%` | `5X Isolated` |
| `2033` | `0xe47f...758c` | `LONG` | 1,004,400.00 USD | `250.00` | `4020.00` | `4017.90` | `3774.29` | -600.00 USD | `-0.06%` | `20X Cross` |
| `2034` | `0x1581...463b` | `LONG` | 1,004,325.00 USD | `250.00` | `4003.77` | `4017.90` | `3504.59` | 3,381.41 USD | `+0.34%` | `15X Cross` |

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
| `7D` | `Long Liquidation` | `3611.20` | 16,530,000.00 USD | 16,530,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.80` | 3,650,000.00 USD | 3,650,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,450,000.00 USD | 16,450,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.90` | 3,640,000.00 USD | 3,640,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,310,000.00 USD | 16,310,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.00` | 3,610,000.00 USD | 3,610,000.00 USD | 30,600.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,260,000.00 USD | 16,260,000.00 USD | 86,210.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.10` | 3,580,000.00 USD | 3,580,000.00 USD | 45,730.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,150,000.00 USD | 16,150,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.20` | 3,530,000.00 USD | 3,530,000.00 USD | 27,320.00 USD | 0.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,950,000.00 USD | 15,950,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.30` | 3,490,000.00 USD | 3,490,000.00 USD | 23,210.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,830,000.00 USD | 15,830,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.40` | 3,460,000.00 USD | 3,460,000.00 USD | 49,080.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,690,000.00 USD | 15,690,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3641.50` | 3,410,000.00 USD | 3,410,000.00 USD | 13,660.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.60` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,630,000.00 USD | 15,630,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3649.70` | 3,390,000.00 USD | 3,390,000.00 USD | 23,000.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,600,000.00 USD | 15,600,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3653.80` | 3,360,000.00 USD | 3,360,000.00 USD | 19,450.00 USD | 0.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,580,000.00 USD | 15,580,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3657.90` | 3,340,000.00 USD | 3,340,000.00 USD | 5,110.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,520,000.00 USD | 15,520,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3662.00` | 3,330,000.00 USD | 3,330,000.00 USD | 2,940.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,510,000.00 USD | 15,510,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3666.10` | 3,330,000.00 USD | 3,330,000.00 USD | 6,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,490,000.00 USD | 15,490,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3670.20` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,480,000.00 USD | 15,480,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 15,060,000.00 USD | 15,060,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,540,000.00 USD | 14,540,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,980,000.00 USD | 13,980,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.70` | 3,320,000.00 USD | 3,320,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,690,000.00 USD | 13,690,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.80` | 3,280,000.00 USD | 3,280,000.00 USD | 68,860.00 USD | 0.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,270,000.00 USD | 13,270,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.90` | 3,200,000.00 USD | 3,200,000.00 USD | 92,460.00 USD | 0.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,090,000.00 USD | 13,090,000.00 USD | 289,880.00 USD | 0.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.00` | 3,100,000.00 USD | 3,100,000.00 USD | 150,790.00 USD | 0.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,740,000.00 USD | 12,740,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.10` | 2,930,000.00 USD | 2,930,000.00 USD | 110,970.00 USD | 0.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,090,000.00 USD | 12,090,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.20` | 2,800,000.00 USD | 2,800,000.00 USD | 84,790.00 USD | 0.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,710,000.00 USD | 11,710,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.30` | 2,700,000.00 USD | 2,700,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,120,000.00 USD | 11,120,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.40` | 2,550,000.00 USD | 2,550,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,910,000.00 USD | 10,910,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.50` | 2,480,000.00 USD | 2,480,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,820,000.00 USD | 10,820,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.60` | 2,450,000.00 USD | 2,450,000.00 USD | 63,500.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,690,000.00 USD | 10,690,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3895.70` | 2,390,000.00 USD | 2,390,000.00 USD | 63,600.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,560,000.00 USD | 10,560,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3899.80` | 2,320,000.00 USD | 2,320,000.00 USD | 22,780.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,440,000.00 USD | 10,440,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.90` | 2,290,000.00 USD | 2,290,000.00 USD | 35,310.00 USD | 0.00 USD | 604.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,390,000.00 USD | 10,390,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3908.00` | 2,250,000.00 USD | 2,250,000.00 USD | 20,800.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,340,000.00 USD | 10,340,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3916.20` | 2,220,000.00 USD | 2,220,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,310,000.00 USD | 10,310,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,950,000.00 USD | 9,950,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,160,000.00 USD | 9,160,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,120,000.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3932.60` | 2,210,000.00 USD | 2,210,000.00 USD | 5,620.00 USD | 0.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,010,000.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.70` | 2,200,000.00 USD | 2,200,000.00 USD | 153,970.00 USD | 0.00 USD | 9,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,510,000.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.80` | 2,040,000.00 USD | 2,040,000.00 USD | 128,480.00 USD | 0.00 USD | 13,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,790,000.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.90` | 1,900,000.00 USD | 1,900,000.00 USD | 292,410.00 USD | 0.00 USD | 25,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,360,000.00 USD | 5,360,000.00 USD | 605,870.00 USD | 0.00 USD | 137,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.00` | 1,580,000.00 USD | 1,580,000.00 USD | 202,600.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.10` | 1,330,000.00 USD | 1,330,000.00 USD | 249,450.00 USD | 0.00 USD | 32,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.20` | 1,050,000.00 USD | 1,050,000.00 USD | 160,660.00 USD | 0.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.30` | 875,430.00 USD | 875,430.00 USD | 250,520.00 USD | 0.00 USD | 39,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.40` | 585,280.00 USD | 585,280.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.50` | 496,760.00 USD | 496,760.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.60` | 478,380.00 USD | 478,380.00 USD | 156,290.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3977.70` | 315,480.00 USD | 315,480.00 USD | 97,910.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.80` | 210,360.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3985.90` | 138,980.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3990.00` | 67,140.00 USD | 67,140.00 USD | 41,610.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3998.20` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4092.50` | 5,620.00 USD | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4096.60` | 143,550.00 USD | 143,550.00 USD | 125,060.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,430,000.00 USD | 4,430,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.70` | 240,400.00 USD | 240,400.00 USD | 85,770.00 USD | 0.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,700,000.00 USD | 4,700,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.80` | 444,680.00 USD | 444,680.00 USD | 193,530.00 USD | 0.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,410,000.00 USD | 5,410,000.00 USD | 606,780.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.90` | 784,650.00 USD | 784,650.00 USD | 292,970.00 USD | 0.00 USD | 46,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,500,000.00 USD | 6,500,000.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4113.00` | 1,050,000.00 USD | 1,050,000.00 USD | 221,950.00 USD | 0.00 USD | 41,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,400,000.00 USD | 7,400,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.10` | 1,230,000.00 USD | 1,230,000.00 USD | 159,310.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,280,000.00 USD | 8,280,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.20` | 1,520,000.00 USD | 1,520,000.00 USD | 277,540.00 USD | 0.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 9,000,000.00 USD | 9,000,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.30` | 1,670,000.00 USD | 1,670,000.00 USD | 106,180.00 USD | 0.00 USD | 44,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,250,000.00 USD | 9,250,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.40` | 1,720,000.00 USD | 1,720,000.00 USD | 36,900.00 USD | 0.00 USD | 11,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,450,000.00 USD | 9,450,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.50` | 1,820,000.00 USD | 1,820,000.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,680,000.00 USD | 9,680,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.60` | 1,970,000.00 USD | 1,970,000.00 USD | 140,890.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,930,000.00 USD | 9,930,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.70` | 2,050,000.00 USD | 2,050,000.00 USD | 65,150.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,100,000.00 USD | 10,100,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.80` | 2,110,000.00 USD | 2,110,000.00 USD | 54,840.00 USD | 0.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,200,000.00 USD | 10,200,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.90` | 2,160,000.00 USD | 2,160,000.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,290,000.00 USD | 10,290,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4154.00` | 2,190,000.00 USD | 2,190,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,670,000.00 USD | 10,670,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,100,000.00 USD | 11,100,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.20` | 2,210,000.00 USD | 2,210,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,540,000.00 USD | 11,540,000.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,990,000.00 USD | 11,990,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.50` | 2,230,000.00 USD | 2,230,000.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,220,000.00 USD | 12,220,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.60` | 2,320,000.00 USD | 2,320,000.00 USD | 84,040.00 USD | 0.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,560,000.00 USD | 12,560,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.70` | 2,380,000.00 USD | 2,380,000.00 USD | 60,250.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,740,000.00 USD | 12,740,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.80` | 2,540,000.00 USD | 2,540,000.00 USD | 140,480.00 USD | 0.00 USD | 14,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 13,080,000.00 USD | 13,080,000.00 USD | 292,190.00 USD | 0.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.90` | 2,660,000.00 USD | 2,660,000.00 USD | 100,220.00 USD | 0.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,720,000.00 USD | 13,720,000.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.00` | 2,790,000.00 USD | 2,790,000.00 USD | 115,980.00 USD | 0.00 USD | 15,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 14,070,000.00 USD | 14,070,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.10` | 2,870,000.00 USD | 2,870,000.00 USD | 76,450.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,570,000.00 USD | 14,570,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.20` | 3,020,000.00 USD | 3,020,000.00 USD | 126,510.00 USD | 0.00 USD | 19,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,830,000.00 USD | 14,830,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4207.30` | 3,060,000.00 USD | 3,060,000.00 USD | 27,490.00 USD | 0.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,950,000.00 USD | 14,950,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4211.40` | 3,080,000.00 USD | 3,080,000.00 USD | 10,950.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 15,060,000.00 USD | 15,060,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4215.50` | 3,140,000.00 USD | 3,140,000.00 USD | 57,500.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,180,000.00 USD | 15,180,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.60` | 3,200,000.00 USD | 3,200,000.00 USD | 56,110.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,290,000.00 USD | 15,290,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.70` | 3,240,000.00 USD | 3,240,000.00 USD | 31,440.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,370,000.00 USD | 15,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.80` | 3,280,000.00 USD | 3,280,000.00 USD | 36,150.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,420,000.00 USD | 15,420,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4231.90` | 3,310,000.00 USD | 3,310,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,460,000.00 USD | 15,460,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,480,000.00 USD | 15,480,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4240.10` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4244.20` | 3,320,000.00 USD | 3,320,000.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,620,000.00 USD | 15,620,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,760,000.00 USD | 15,760,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,900,000.00 USD | 15,900,000.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 16,020,000.00 USD | 16,020,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 16,080,000.00 USD | 16,080,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.40` | 3,330,000.00 USD | 3,330,000.00 USD | 8,150.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,190,000.00 USD | 16,190,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.50` | 3,360,000.00 USD | 3,360,000.00 USD | 24,480.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,240,000.00 USD | 16,240,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4424.60` | 3,380,000.00 USD | 3,380,000.00 USD | 23,020.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.50` | 3,400,000.00 USD | 3,400,000.00 USD | 13,230.00 USD | 0.00 USD | 295.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,320,000.00 USD | 16,320,000.00 USD | 65,320.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,480,000.00 USD | 16,480,000.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,600,000.00 USD | 16,600,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,720,000.00 USD | 16,720,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,800,000.00 USD | 16,800,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,850,000.00 USD | 16,850,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,530,000.00 USD | 0.00 USD | 16,530,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.80` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `3615.50` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.90` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD |
| `7D` | `3619.80` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3621.00` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 30,600.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `3624.10` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 86,210.00 USD | 0.00 USD | 21,190.00 USD |
| `1D` | `3625.10` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 45,730.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `3628.40` | 16,150,000.00 USD | 0.00 USD | 16,150,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.20` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 27,320.00 USD | 0.00 USD | 6,930.00 USD |
| `7D` | `3632.70` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3633.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 23,210.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.40` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 49,080.00 USD | 0.00 USD | 6,210.00 USD |
| `7D` | `3641.30` | 15,690,000.00 USD | 0.00 USD | 15,690,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3641.50` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 13,660.00 USD | 0.00 USD | 4,490.00 USD |
| `1D` | `3645.60` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `3645.60` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3649.70` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 23,000.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3649.90` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3653.80` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 19,450.00 USD | 0.00 USD | 1,860.00 USD |
| `7D` | `3654.20` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3657.90` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 5,110.00 USD | 0.00 USD | 3,220.00 USD |
| `7D` | `3658.50` | 15,520,000.00 USD | 0.00 USD | 15,520,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3662.00` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 2,940.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3666.10` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 6,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3667.10` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3670.20` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD |
| `7D` | `3852.00` | 13,980,000.00 USD | 0.00 USD | 13,980,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3854.70` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `3856.30` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3858.80` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 68,860.00 USD | 0.00 USD | 4,400.00 USD |
| `7D` | `3860.60` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3862.90` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 92,460.00 USD | 0.00 USD | 6,510.00 USD |
| `7D` | `3864.90` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 289,880.00 USD | 0.00 USD | 59,280.00 USD |
| `1D` | `3867.00` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 150,790.00 USD | 0.00 USD | 22,530.00 USD |
| `7D` | `3869.20` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3871.10` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 110,970.00 USD | 0.00 USD | 21,730.00 USD |
| `7D` | `3873.50` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3875.20` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 84,790.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3877.80` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3879.30` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD |
| `7D` | `3882.10` | 11,120,000.00 USD | 0.00 USD | 11,120,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3883.40` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD |
| `7D` | `3886.40` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3887.50` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD |
| `7D` | `3890.70` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3891.60` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 63,500.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3895.00` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3895.70` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 63,600.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `3899.30` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3899.80` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 22,780.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `3903.60` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3903.90` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 35,310.00 USD | 0.00 USD | 604.20 USD |
| `7D` | `3907.90` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `1D` | `3908.00` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 20,800.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3912.20` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3916.20` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `1D` | `3932.60` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 5,620.00 USD | 0.00 USD | 4,300.00 USD |
| `7D` | `3933.70` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3936.70` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 153,970.00 USD | 0.00 USD | 9,520.00 USD |
| `7D` | `3938.00` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3940.80` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 128,480.00 USD | 0.00 USD | 13,700.00 USD |
| `7D` | `3942.30` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.90` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 292,410.00 USD | 0.00 USD | 25,950.00 USD |
| `7D` | `3946.60` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 605,870.00 USD | 0.00 USD | 137,820.00 USD |
| `1D` | `3949.00` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 202,600.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3953.10` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 249,450.00 USD | 0.00 USD | 32,150.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3957.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 160,660.00 USD | 0.00 USD | 15,430.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3961.30` | 875,430.00 USD | 0.00 USD | 875,430.00 USD | 250,520.00 USD | 0.00 USD | 39,620.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.40` | 585,280.00 USD | 0.00 USD | 585,280.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.50` | 496,760.00 USD | 0.00 USD | 496,760.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.60` | 478,380.00 USD | 0.00 USD | 478,380.00 USD | 156,290.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3977.70` | 315,480.00 USD | 0.00 USD | 315,480.00 USD | 97,910.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3981.80` | 210,360.00 USD | 0.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3985.90` | 138,980.00 USD | 0.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 4,620.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3990.00` | 67,140.00 USD | 0.00 USD | 67,140.00 USD | 41,610.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3998.20` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `4023.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4023.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD |
| `1D` | `4092.50` | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4096.60` | 143,550.00 USD | 143,550.00 USD | 0.00 USD | 125,060.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4100.70` | 240,400.00 USD | 240,400.00 USD | 0.00 USD | 85,770.00 USD | 0.00 USD | 11,080.00 USD |
| `7D` | `4101.40` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4104.80` | 444,680.00 USD | 444,680.00 USD | 0.00 USD | 193,530.00 USD | 0.00 USD | 10,750.00 USD |
| `7D` | `4105.70` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 606,780.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4108.90` | 784,650.00 USD | 784,650.00 USD | 0.00 USD | 292,970.00 USD | 0.00 USD | 46,990.00 USD |
| `7D` | `4110.00` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4113.00` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 221,950.00 USD | 0.00 USD | 41,550.00 USD |
| `7D` | `4114.30` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4117.10` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 159,310.00 USD | 0.00 USD | 19,550.00 USD |
| `7D` | `4118.60` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4121.20` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 277,540.00 USD | 0.00 USD | 18,910.00 USD |
| `7D` | `4122.90` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4125.30` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 106,180.00 USD | 0.00 USD | 44,780.00 USD |
| `7D` | `4127.20` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4129.40` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 36,900.00 USD | 0.00 USD | 11,040.00 USD |
| `7D` | `4131.50` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.50` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `4135.80` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.60` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 140,890.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.70` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4144.40` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4145.80` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 54,840.00 USD | 0.00 USD | 3,800.00 USD |
| `7D` | `4148.70` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.90` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4154.00` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.20` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `1D` | `4174.50` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `4174.50` | 12,220,000.00 USD | 12,220,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4178.60` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 2,660.00 USD |
| `7D` | `4178.80` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4182.70` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 60,250.00 USD | 0.00 USD | 8,050.00 USD |
| `7D` | `4183.10` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4186.80` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 140,480.00 USD | 0.00 USD | 14,090.00 USD |
| `7D` | `4187.40` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 292,190.00 USD | 0.00 USD | 53,390.00 USD |
| `1D` | `4190.90` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 100,220.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `4191.70` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4195.00` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 115,980.00 USD | 0.00 USD | 15,450.00 USD |
| `7D` | `4196.00` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4199.10` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 76,450.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4200.30` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4203.20` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 126,510.00 USD | 0.00 USD | 19,190.00 USD |
| `7D` | `4204.60` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4207.30` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 27,490.00 USD | 0.00 USD | 13,950.00 USD |
| `7D` | `4208.90` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4211.40` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 10,950.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4213.20` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4215.50` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 57,500.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `4217.50` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4219.60` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 56,110.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `4221.80` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4223.70` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 31,440.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `4226.10` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4227.80` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 36,150.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `4230.40` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4231.90` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4234.70` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4240.10` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD |
| `1D` | `4244.20` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4389.50` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `7D` | `4415.30` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4416.40` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `4419.60` | 16,190,000.00 USD | 16,190,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4420.50` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 24,480.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4423.90` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4424.60` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 23,020.00 USD | 0.00 USD | 2,060.00 USD |
| `1D` | `4426.50` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 13,230.00 USD | 0.00 USD | 295.69 USD |
| `7D` | `4428.20` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 65,320.00 USD | 0.00 USD | 18,160.00 USD |
| `7D` | `4432.50` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD |
| `7D` | `4436.80` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,800,000.00 USD | 16,800,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.64M` | Total OI Tokens: `68,284.5 PAXG`
  * 1h OI Change: `+0.23%` | 4h OI Change: `-0.26%` | 24h OI Change: `+0.08%`
  * Exchange Breakdown: Binance=`107.21M` | Bybit=`20.00M` | OKX=`-` | Hyperliquid=`25.10M`
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
| `15M` | `PAXG` | `73.64%` | `26.36%` | `2.79` | 622,310.00 USD |
| `15M` | `Binance` | `73.6%` | `26.4%` | `2.79` | 351,750.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `84.1%` | `15.9%` | `5.29` | 16,790.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `70.44%` | `29.56%` | `2.38` | 9,970.00 USD |
| `15M` | `Bitget` | `62.48%` | `37.52%` | `1.67` | 108,890.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `79.72%` | `20.28%` | `3.93` | 6,200.00 USD |
| `15M` | `Bitunix` | `37.15%` | `62.85%` | `0.59` | 16,310.00 USD |
| `15M` | `Hyperliquid` | `95.61%` | `4.39%` | `21.78` | 19,610.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `86.33%` | `13.67%` | `6.32` | 86,520.00 USD |
| `15M` | `HTX` | `53.01%` | `46.99%` | `1.13` | 667.08 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 3,380.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 446.17 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `87%` | `13%` | `6.69` | 1,790.00 USD |
| `15M` | `Whale Positions` | `73.6%` | `26.4%` | `2.79` | 351,750.00 USD |
| `15M` | `Global Accounts` | `73.64%` | `26.36%` | `2.79` | 622,310.00 USD |
| `1H` | `PAXG` | `56.40%` | `43.60%` | `1.29` | 3,260,000.00 USD |
| `1H` | `Binance` | `47.89%` | `52.11%` | `0.92` | 2,040,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `63.96%` | `36.04%` | `1.77` | 60,850.00 USD |
| `1H` | `KuCoin` | `48.94%` | `51.06%` | `0.96` | 91,260.00 USD |
| `1H` | `Gate` | `78.31%` | `21.69%` | `3.61` | 50,040.00 USD |
| `1H` | `Bitget` | `60.92%` | `39.08%` | `1.56` | 378,990.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `69.9%` | `30.1%` | `2.32` | 30,960.00 USD |
| `1H` | `Bitunix` | `41.83%` | `58.17%` | `0.72` | 52,910.00 USD |
| `1H` | `Hyperliquid` | `98.16%` | `1.84%` | `53.35` | 177,140.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `76.98%` | `23.02%` | `3.34` | 350,550.00 USD |
| `1H` | `HTX` | `81.88%` | `18.12%` | `4.52` | 7,610.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `68.82%` | `31.18%` | `2.21` | 10,710.00 USD |
| `1H` | `Aster` | `100%` | `0%` | `1.00` | 1,860.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.03%` | `31.97%` | `2.13` | 7,720.00 USD |
| `1H` | `Whale Positions` | `47.89%` | `52.11%` | `0.92` | 2,040,000.00 USD |
| `1H` | `Global Accounts` | `56.40%` | `43.60%` | `1.29` | 3,260,000.00 USD |
| `4H` | `PAXG` | `52.55%` | `47.45%` | `1.11` | 51,570,000.00 USD |
| `4H` | `Binance` | `54.69%` | `45.31%` | `1.21` | 4,520,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.36%` | `50.64%` | `0.97` | 4,800,000.00 USD |
| `4H` | `KuCoin` | `52.26%` | `47.74%` | `1.09` | 303,010.00 USD |
| `4H` | `Gate` | `53.55%` | `46.45%` | `1.15` | 1,730,000.00 USD |
| `4H` | `Bitget` | `44.46%` | `55.54%` | `0.80` | 1,730,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `54.3%` | `45.7%` | `1.19` | 31,190,000.00 USD |
| `4H` | `Bitunix` | `61.33%` | `38.67%` | `1.59` | 1,630,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.37%` | `47.63%` | `1.10` | 4,160,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `13.21%` | `86.79%` | `0.15` | 1,340,000.00 USD |
| `4H` | `HTX` | `93.04%` | `6.96%` | `13.37` | 70,740.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.51%` | `54.49%` | `0.84` | 121,060.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.69%` | `45.31%` | `1.21` | 4,520,000.00 USD |
| `4H` | `Global Accounts` | `52.55%` | `47.45%` | `1.11` | 51,570,000.00 USD |


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
| `5m` | -24,380.00 USD | 98,250.00 USD | **`ACCUMULATION`** |
| `15m` | 2,170.00 USD | 201,220.00 USD | **`ACCUMULATION`** |
| `30m` | 54,270.00 USD | -54,380.00 USD | **`DISTRIBUTION`** |
| `1h` | -152,030.00 USD | -52,020.00 USD | **`DISTRIBUTION`** |
| `2h` | -374,160.00 USD | 248,220.00 USD | **`DISTRIBUTION`** |
| `4h` | 301,140.00 USD | 1,020,000.00 USD | **`ACCUMULATION`** |
| `6h` | 156,690.00 USD | 816,880.00 USD | **`ACCUMULATION`** |
| `8h` | -185,440.00 USD | 1,470,000.00 USD | **`ACCUMULATION`** |
| `12h` | -263,590.00 USD | 1,030,000.00 USD | **`ACCUMULATION`** |
| `24h` | -358,520.00 USD | 1,300,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,220,000.00 USD | -7,450,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,640,000.00 USD | -71,820,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-24.38K` | 15m=`+2.17K` | 1h=`-152.03K` | 24h=`-358.52K`
* Futures Capital Netflows: 5m=`+98.25K` | 15m=`+201.22K` | 1h=`-52.02K` | 24h=`+1.30M`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `4008.06` (Risk Distance: `8.61` pts)
  * +2.5R Take Profit: `4038.19`
  * Mathematical Lot Sizing: **`1.16 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.95` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4049.56` (Risk Distance: `8.61` pts)
  * +2.5R Take Profit: `4019.43`
  * Mathematical Lot Sizing: **`1.16 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4050.96`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
