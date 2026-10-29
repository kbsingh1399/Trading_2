# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 01:29:57 IST` (`2026-10-29 19:59:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `54` | `0x5b5d...c060` | `SHORT` | 25,631,867.30 USD | `6,372.60` | `4191.43` | `4022.40` | `29309.86` | 1,078,490.95 USD | `+4.21%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,384,304.51 USD | `6,311.05` | `4133.84` | `4022.40` | `13244.58` | 704,608.91 USD | `+2.78%` | `5X Cross` |
| `72` | `0xb83d...6e36` | `SHORT` | 22,995,156.32 USD | `5,717.06` | `4234.49` | `4022.40` | `27660.77` | 1,213,718.91 USD | `+5.28%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,423,795.11 USD | `4,828.91` | `4157.43` | `4022.40` | `2086.14` | -652,087.20 USD | `-3.36%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,153,701.08 USD | `3,518.90` | `4129.56` | `4022.40` | `277.31` | -377,793.50 USD | `-2.67%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,145,407.13 USD | `3,268.21` | `4228.94` | `4022.40` | `4407.00` | 675,672.00 USD | `+5.14%` | `25X Cross` |
| `178` | `0xa742...e390` | `SHORT` | 11,664,090.40 USD | `2,900.00` | `4364.92` | `4022.40` | `4235.62` | 994,185.93 USD | `+8.52%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,849,060.00 USD | `2,200.00` | `4176.09` | `4022.40` | `2503.32` | -338,359.30 USD | `-3.82%` | `25X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,848,840.00 USD | `2,200.00` | `4112.20` | `4022.40` | `4331.10` | 198,014.59 USD | `+2.24%` | `20X Cross` |
| `310` | `0xfc66...ca06` | `SHORT` | 7,991,866.04 USD | `1,986.89` | `4032.86` | `4022.40` | `23995.47` | 21,000.13 USD | `+0.26%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,945,724.67 USD | `1,975.37` | `4048.55` | `4022.40` | `6479.42` | 51,667.05 USD | `+0.65%` | `6X Cross` |
| `381` | `0xc26c...b8f4` | `LONG` | 6,354,882.13 USD | `1,579.95` | `4075.62` | `4022.40` | `0.000000` | -84,414.84 USD | `-1.33%` | `1X Cross` |
| `419` | `0x12d2...f97f` | `LONG` | 5,639,174.72 USD | `1,401.94` | `4278.91` | `4022.40` | `2481.63` | -359,615.86 USD | `-6.38%` | `20X Cross` |
| `575` | `0x63da...8add` | `LONG` | 4,022,200.00 USD | `1,000.00` | `4021.46` | `4022.40` | `3564.06` | 739.04 USD | `+0.02%` | `25X Cross` |
| `596` | `0x9aa5...58af` | `LONG` | 3,908,332.78 USD | `971.64` | `4279.98` | `4022.40` | `0.000000` | -250,276.30 USD | `-6.40%` | `20X Cross` |
| `623` | `0xf3dc...1672` | `LONG` | 3,743,916.53 USD | `930.74` | `4024.62` | `4022.40` | `3337.54` | -1,976.03 USD | `-0.05%` | `20X Cross` |
| `689` | `0x4a20...3c26` | `LONG` | 3,368,272.81 USD | `837.40` | `4599.73` | `4022.40` | `0.000000` | -483,547.57 USD | `-14.36%` | `20X Cross` |
| `704` | `0x354b...6425` | `LONG` | 3,302,281.30 USD | `821.01` | `4033.57` | `4022.40` | `0.000000` | -9,335.08 USD | `-0.28%` | `10X Cross` |
| `842` | `0x0fac...7a0a` | `LONG` | 2,761,111.32 USD | `686.49` | `4290.34` | `4022.40` | `1379.73` | -184,147.38 USD | `-6.67%` | `25X Cross` |
| `884` | `0xd8c5...99b0` | `SHORT` | 2,583,744.11 USD | `642.35` | `4175.35` | `4022.40` | `31946.51` | 98,317.06 USD | `+3.81%` | `4X Cross` |
| `919` | `0x625e...a354` | `SHORT` | 2,493,764.00 USD | `620.00` | `4122.81` | `4022.40` | `4342.20` | 62,383.03 USD | `+2.50%` | `20X Cross` |
| `946` | `0xeae3...e8ad` | `SHORT` | 2,413,500.00 USD | `600.00` | `4104.77` | `4022.40` | `4325.22` | 49,365.11 USD | `+2.05%` | `20X Cross` |
| `947` | `0xf285...fa82` | `LONG` | 2,405,641.74 USD | `598.11` | `4146.45` | `4022.40` | `3891.19` | -74,377.81 USD | `-3.09%` | `25X Cross` |
| `965` | `0x12f7...8750` | `LONG` | 2,355,443.36 USD | `585.61` | `4082.77` | `4022.40` | `2157.27` | -35,473.62 USD | `-1.51%` | `10X Cross` |
| `1123` | `0x413c...886c` | `LONG` | 2,011,250.00 USD | `500.00` | `4010.43` | `4022.40` | `0.000000` | 6,033.77 USD | `+0.30%` | `2X Cross` |
| `1134` | `0x61ce...a62b` | `SHORT` | 2,001,207.83 USD | `497.50` | `4071.66` | `4022.40` | `4692.23` | 24,460.96 USD | `+1.22%` | `20X Cross` |
| `1144` | `0x0593...40f9` | `LONG` | 1,995,772.75 USD | `496.18` | `4024.57` | `4022.40` | `3701.68` | -1,131.08 USD | `-0.06%` | `10X Isolated` |
| `1261` | `0x2edd...8179` | `LONG` | 1,825,267.37 USD | `453.58` | `4169.95` | `4024.77` | `0.000000` | -66,156.74 USD | `-3.62%` | `10X Cross` |
| `1262` | `0xead5...69f2` | `LONG` | 1,825,209.60 USD | `453.78` | `4220.88` | `4022.40` | `3538.89` | -90,158.46 USD | `-4.94%` | `5X Isolated` |
| `1320` | `0x7a6d...f79c` | `SHORT` | 1,723,711.42 USD | `428.38` | `4136.09` | `4024.77` | `5870.76` | 48,103.59 USD | `+2.79%` | `10X Cross` |
| `1388` | `0x46fc...1195` | `LONG` | 1,637,150.03 USD | `407.03` | `4055.53` | `4022.40` | `1958.38` | -13,569.78 USD | `-0.83%` | `20X Cross` |
| `1419` | `0x6d15...d374` | `LONG` | 1,608,880.00 USD | `400.00` | `4068.25` | `4022.40` | `3841.76` | -18,420.00 USD | `-1.14%` | `25X Cross` |
| `1420` | `0xee02...309d` | `SHORT` | 1,608,880.00 USD | `400.00` | `4438.84` | `4022.40` | `4226.84` | 166,658.60 USD | `+10.36%` | `25X Isolated` |
| `1448` | `0x02a7...fe9f` | `SHORT` | 1,568,658.00 USD | `390.00` | `4055.02` | `4022.40` | `4306.66` | 12,801.25 USD | `+0.82%` | `25X Cross` |
| `1482` | `0x51f6...2b39` | `LONG` | 1,531,075.66 USD | `380.49` | `4234.66` | `4024.77` | `0.000000` | -80,152.40 USD | `-5.24%` | `10X Cross` |
| `1484` | `0x7e77...b8d2` | `SHORT` | 1,528,474.00 USD | `380.00` | `4131.92` | `4022.40` | `4293.46` | 41,655.64 USD | `+2.73%` | `20X Cross` |
| `1504` | `0x72c2...9b37` | `LONG` | 1,500,920.65 USD | `373.13` | `4000.98` | `4022.40` | `3777.99` | 8,027.14 USD | `+0.53%` | `13X Isolated` |
| `1543` | `0xaa44...b844` | `LONG` | 1,448,100.00 USD | `360.00` | `4043.10` | `4022.40` | `2803.21` | -7,417.63 USD | `-0.51%` | `4X Cross` |
| `1545` | `0x781e...96b7` | `SHORT` | 1,446,829.20 USD | `359.55` | `4365.03` | `4024.77` | `12764.32` | 122,618.28 USD | `+8.47%` | `10X Cross` |
| `1657` | `0xa41f...d50a` | `LONG` | 1,323,217.15 USD | `328.96` | `4468.89` | `4022.40` | `3833.14` | -146,880.70 USD | `-11.10%` | `15X Cross` |
| `1682` | `0x49e9...e1d0` | `SHORT` | 1,301,412.17 USD | `323.56` | `4025.23` | `4022.40` | `29073.56` | 980.53 USD | `+0.08%` | `4X Cross` |
| `1710` | `0xada6...6f88` | `LONG` | 1,284,286.10 USD | `319.28` | `4166.46` | `4022.40` | `1868.08` | -45,964.41 USD | `-3.58%` | `5X Cross` |
| `1717` | `0xbf5a...88ba` | `SHORT` | 1,277,639.77 USD | `317.65` | `4091.80` | `4022.40` | `10484.49` | 22,143.26 USD | `+1.73%` | `20X Cross` |
| `1740` | `0xff31...ff6c` | `SHORT` | 1,246,913.00 USD | `310.00` | `4372.43` | `4022.40` | `4789.13` | 108,542.38 USD | `+8.70%` | `10X Isolated` |
| `1905` | `0x50e2...d770` | `LONG` | 1,087,498.79 USD | `270.37` | `4243.58` | `4022.40` | `2562.05` | -59,827.67 USD | `-5.50%` | `20X Cross` |
| `1920` | `0x4c92...4f17` | `SHORT` | 1,072,803.20 USD | `266.72` | `4260.98` | `4022.40` | `6513.59` | 63,689.04 USD | `+5.94%` | `20X Cross` |
| `1991` | `0xd346...c4f3` | `LONG` | 1,026,334.54 USD | `255.17` | `4188.66` | `4022.40` | `3310.37` | -42,501.97 USD | `-4.14%` | `5X Isolated` |
| `2029` | `0xe47f...758c` | `LONG` | 1,005,625.00 USD | `250.00` | `4020.00` | `4022.40` | `3774.29` | 625.00 USD | `+0.06%` | `20X Cross` |
| `2030` | `0x1581...463b` | `LONG` | 1,005,575.00 USD | `250.00` | `4003.77` | `4022.40` | `3504.59` | 4,631.41 USD | `+0.46%` | `15X Cross` |

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
| `7D` | `Long Liquidation` | `3611.20` | 16,430,000.00 USD | 16,430,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.60` | 3,590,000.00 USD | 3,590,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,340,000.00 USD | 16,340,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.80` | 3,590,000.00 USD | 3,590,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,200,000.00 USD | 16,200,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.00` | 3,550,000.00 USD | 3,550,000.00 USD | 30,600.00 USD | 0.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,150,000.00 USD | 16,150,000.00 USD | 86,210.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.20` | 3,520,000.00 USD | 3,520,000.00 USD | 45,730.00 USD | 0.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,040,000.00 USD | 16,040,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.40` | 3,470,000.00 USD | 3,470,000.00 USD | 32,220.00 USD | 0.00 USD | 6,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,850,000.00 USD | 15,850,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.60` | 3,430,000.00 USD | 3,430,000.00 USD | 24,570.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,720,000.00 USD | 15,720,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.80` | 3,400,000.00 USD | 3,400,000.00 USD | 45,970.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,590,000.00 USD | 15,590,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3642.00` | 3,350,000.00 USD | 3,350,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,520,000.00 USD | 15,520,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3646.20` | 3,330,000.00 USD | 3,330,000.00 USD | 8,210.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,490,000.00 USD | 15,490,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.40` | 3,320,000.00 USD | 3,320,000.00 USD | 22,380.00 USD | 0.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,470,000.00 USD | 15,470,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3654.60` | 3,300,000.00 USD | 3,300,000.00 USD | 11,860.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,410,000.00 USD | 15,410,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3658.80` | 3,280,000.00 USD | 3,280,000.00 USD | 8,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,400,000.00 USD | 15,400,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3663.00` | 3,270,000.00 USD | 3,270,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,380,000.00 USD | 15,380,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.40` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,370,000.00 USD | 15,370,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 14,950,000.00 USD | 14,950,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,430,000.00 USD | 14,430,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.00` | 3,270,000.00 USD | 3,270,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,900,000.00 USD | 13,900,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.20` | 3,260,000.00 USD | 3,260,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,610,000.00 USD | 13,610,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.40` | 3,180,000.00 USD | 3,180,000.00 USD | 64,240.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,190,000.00 USD | 13,190,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.60` | 3,110,000.00 USD | 3,110,000.00 USD | 150,790.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,010,000.00 USD | 13,010,000.00 USD | 289,880.00 USD | 0.00 USD | 52,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.80` | 2,940,000.00 USD | 2,940,000.00 USD | 104,280.00 USD | 0.00 USD | 20,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,670,000.00 USD | 12,670,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.00` | 2,820,000.00 USD | 2,820,000.00 USD | 126,290.00 USD | 0.00 USD | 18,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,020,000.00 USD | 12,020,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.20` | 2,670,000.00 USD | 2,670,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,640,000.00 USD | 11,640,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.40` | 2,570,000.00 USD | 2,570,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,050,000.00 USD | 11,050,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.60` | 2,440,000.00 USD | 2,440,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,840,000.00 USD | 10,840,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.80` | 2,400,000.00 USD | 2,400,000.00 USD | 26,200.00 USD | 0.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,750,000.00 USD | 10,750,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3894.00` | 2,370,000.00 USD | 2,370,000.00 USD | 73,860.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,610,000.00 USD | 10,610,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.20` | 2,290,000.00 USD | 2,290,000.00 USD | 32,580.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,490,000.00 USD | 10,490,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.40` | 2,250,000.00 USD | 2,250,000.00 USD | 30,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,360,000.00 USD | 10,360,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.60` | 2,220,000.00 USD | 2,220,000.00 USD | 26,240.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,320,000.00 USD | 10,320,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,270,000.00 USD | 10,270,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.00` | 2,190,000.00 USD | 2,190,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,240,000.00 USD | 10,240,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,880,000.00 USD | 9,880,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,090,000.00 USD | 9,090,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,110,000.00 USD | 8,110,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,000,000.00 USD | 7,000,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.00` | 2,180,000.00 USD | 2,180,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,500,000.00 USD | 6,500,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.20` | 2,030,000.00 USD | 2,030,000.00 USD | 94,110.00 USD | 0.00 USD | 11,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,780,000.00 USD | 5,780,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.40` | 1,930,000.00 USD | 1,930,000.00 USD | 285,970.00 USD | 0.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,350,000.00 USD | 5,350,000.00 USD | 605,870.00 USD | 0.00 USD | 123,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3948.60` | 1,620,000.00 USD | 1,620,000.00 USD | 227,310.00 USD | 0.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.80` | 1,350,000.00 USD | 1,350,000.00 USD | 283,970.00 USD | 0.00 USD | 38,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.00` | 1,030,000.00 USD | 1,030,000.00 USD | 171,150.00 USD | 0.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.20` | 838,860.00 USD | 838,860.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.40` | 547,910.00 USD | 547,910.00 USD | 61,120.00 USD | 0.00 USD | 27,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.60` | 458,890.00 USD | 458,890.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.80` | 440,500.00 USD | 440,500.00 USD | 156,290.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3978.00` | 277,610.00 USD | 277,610.00 USD | 106,200.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3982.20` | 164,190.00 USD | 164,190.00 USD | 32,780.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.40` | 112,790.00 USD | 112,790.00 USD | 50,940.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3990.60` | 53,970.00 USD | 53,970.00 USD | 31,710.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3999.00` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4095.60` | 91,610.00 USD | 91,610.00 USD | 78,740.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.80` | 238,120.00 USD | 238,120.00 USD | 137,710.00 USD | 0.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.00` | 419,920.00 USD | 419,920.00 USD | 168,400.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,340,000.00 USD | 5,340,000.00 USD | 606,780.00 USD | 0.00 USD | 90,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.20` | 721,280.00 USD | 721,280.00 USD | 260,190.00 USD | 0.00 USD | 41,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,420,000.00 USD | 6,420,000.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.40` | 1,030,000.00 USD | 1,030,000.00 USD | 272,530.00 USD | 0.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,330,000.00 USD | 7,330,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4116.60` | 1,230,000.00 USD | 1,230,000.00 USD | 166,650.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,210,000.00 USD | 8,210,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.80` | 1,520,000.00 USD | 1,520,000.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,930,000.00 USD | 8,930,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.00` | 1,670,000.00 USD | 1,670,000.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,180,000.00 USD | 9,180,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.20` | 1,720,000.00 USD | 1,720,000.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,380,000.00 USD | 9,380,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.40` | 1,820,000.00 USD | 1,820,000.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,610,000.00 USD | 9,610,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.60` | 1,950,000.00 USD | 1,950,000.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,860,000.00 USD | 9,860,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.80` | 2,030,000.00 USD | 2,030,000.00 USD | 65,150.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,030,000.00 USD | 10,030,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.00` | 2,090,000.00 USD | 2,090,000.00 USD | 60,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,130,000.00 USD | 10,130,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.20` | 2,120,000.00 USD | 2,120,000.00 USD | 20,760.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,220,000.00 USD | 10,220,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4154.40` | 2,160,000.00 USD | 2,160,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,600,000.00 USD | 10,600,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.60` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,030,000.00 USD | 11,030,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.80` | 2,180,000.00 USD | 2,180,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,450,000.00 USD | 11,450,000.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,890,000.00 USD | 11,890,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,120,000.00 USD | 12,120,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4175.40` | 2,210,000.00 USD | 2,210,000.00 USD | 27,940.00 USD | 0.00 USD | 5,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,460,000.00 USD | 12,460,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4179.60` | 2,280,000.00 USD | 2,280,000.00 USD | 66,150.00 USD | 0.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,640,000.00 USD | 12,640,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.80` | 2,370,000.00 USD | 2,370,000.00 USD | 81,330.00 USD | 0.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 12,980,000.00 USD | 12,980,000.00 USD | 292,190.00 USD | 0.00 USD | 46,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.00` | 2,510,000.00 USD | 2,510,000.00 USD | 122,010.00 USD | 0.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,620,000.00 USD | 13,620,000.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.20` | 2,680,000.00 USD | 2,680,000.00 USD | 152,180.00 USD | 0.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 13,960,000.00 USD | 13,960,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.40` | 2,780,000.00 USD | 2,780,000.00 USD | 86,670.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,470,000.00 USD | 14,470,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.60` | 2,890,000.00 USD | 2,890,000.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,720,000.00 USD | 14,720,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.80` | 3,000,000.00 USD | 3,000,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,850,000.00 USD | 14,850,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.00` | 3,040,000.00 USD | 3,040,000.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.20` | 3,070,000.00 USD | 3,070,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 14,960,000.00 USD | 14,960,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.40` | 3,130,000.00 USD | 3,130,000.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,070,000.00 USD | 15,070,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.60` | 3,180,000.00 USD | 3,180,000.00 USD | 50,180.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,180,000.00 USD | 15,180,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.80` | 3,200,000.00 USD | 3,200,000.00 USD | 11,300.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,270,000.00 USD | 15,270,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4230.00` | 3,230,000.00 USD | 3,230,000.00 USD | 25,610.00 USD | 0.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,310,000.00 USD | 15,310,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4234.20` | 3,260,000.00 USD | 3,260,000.00 USD | 20,800.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,360,000.00 USD | 15,360,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,370,000.00 USD | 15,370,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4242.60` | 3,270,000.00 USD | 3,270,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,520,000.00 USD | 15,520,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,650,000.00 USD | 15,650,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,790,000.00 USD | 15,790,000.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,900,000.00 USD | 15,900,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 15,970,000.00 USD | 15,970,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4419.00` | 3,300,000.00 USD | 3,300,000.00 USD | 28,900.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,080,000.00 USD | 16,080,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4423.20` | 3,320,000.00 USD | 3,320,000.00 USD | 20,450.00 USD | 0.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,120,000.00 USD | 16,120,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.40` | 3,360,000.00 USD | 3,360,000.00 USD | 37,230.00 USD | 0.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,200,000.00 USD | 16,200,000.00 USD | 65,320.00 USD | 0.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.00` | 3,370,000.00 USD | 3,370,000.00 USD | 10,120.00 USD | 0.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,360,000.00 USD | 16,360,000.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,480,000.00 USD | 16,480,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,600,000.00 USD | 16,600,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,680,000.00 USD | 16,680,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,730,000.00 USD | 16,730,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.60` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `3615.50` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.80` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 29,730.00 USD | 0.00 USD | 2,100.00 USD |
| `7D` | `3619.80` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3621.00` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 30,600.00 USD | 0.00 USD | 2,360.00 USD |
| `7D` | `3624.10` | 16,150,000.00 USD | 0.00 USD | 16,150,000.00 USD | 86,210.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3625.20` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 45,730.00 USD | 0.00 USD | 7,790.00 USD |
| `7D` | `3628.40` | 16,040,000.00 USD | 0.00 USD | 16,040,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.40` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 32,220.00 USD | 0.00 USD | 6,260.00 USD |
| `7D` | `3632.70` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3633.60` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 24,570.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.80` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 45,970.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3641.30` | 15,590,000.00 USD | 0.00 USD | 15,590,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3642.00` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD |
| `7D` | `3645.60` | 15,520,000.00 USD | 0.00 USD | 15,520,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3646.20` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 8,210.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `3649.90` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.40` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 22,380.00 USD | 0.00 USD | 2,300.00 USD |
| `7D` | `3654.20` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3654.60` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 11,860.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `3658.50` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3658.80` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 8,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3662.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3663.00` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3667.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.40` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD |
| `1D` | `3852.00` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD |
| `7D` | `3852.00` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3856.20` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `3856.30` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3860.40` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 64,240.00 USD | 0.00 USD | 6,850.00 USD |
| `7D` | `3860.60` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3864.60` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 150,790.00 USD | 0.00 USD | 15,790.00 USD |
| `7D` | `3864.90` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 289,880.00 USD | 0.00 USD | 52,180.00 USD |
| `1D` | `3868.80` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 104,280.00 USD | 0.00 USD | 20,070.00 USD |
| `7D` | `3869.20` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 609,640.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3873.00` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 126,290.00 USD | 0.00 USD | 18,930.00 USD |
| `7D` | `3873.50` | 12,020,000.00 USD | 0.00 USD | 12,020,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3877.20` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3877.80` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3881.40` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD |
| `7D` | `3882.10` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3885.60` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `3886.40` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3889.80` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 26,200.00 USD | 0.00 USD | 8,930.00 USD |
| `7D` | `3890.70` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3894.00` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 73,860.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `3895.00` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3898.20` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 32,580.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3899.30` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3902.40` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 30,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3903.60` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3906.60` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 26,240.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3915.00` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3936.00` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3940.20` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 94,110.00 USD | 0.00 USD | 11,080.00 USD |
| `7D` | `3942.30` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.40` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 285,970.00 USD | 0.00 USD | 17,880.00 USD |
| `7D` | `3946.60` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 605,870.00 USD | 0.00 USD | 123,630.00 USD |
| `1D` | `3948.60` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 227,310.00 USD | 0.00 USD | 48,490.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3952.80` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 283,970.00 USD | 0.00 USD | 38,080.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3957.00` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 171,150.00 USD | 0.00 USD | 16,410.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3961.20` | 838,860.00 USD | 0.00 USD | 838,860.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.40` | 547,910.00 USD | 0.00 USD | 547,910.00 USD | 61,120.00 USD | 0.00 USD | 27,900.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.60` | 458,890.00 USD | 0.00 USD | 458,890.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.80` | 440,500.00 USD | 0.00 USD | 440,500.00 USD | 156,290.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3978.00` | 277,610.00 USD | 0.00 USD | 277,610.00 USD | 106,200.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3982.20` | 164,190.00 USD | 0.00 USD | 164,190.00 USD | 32,780.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3986.40` | 112,790.00 USD | 0.00 USD | 112,790.00 USD | 50,940.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3990.60` | 53,970.00 USD | 0.00 USD | 53,970.00 USD | 31,710.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3999.00` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `4025.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4026.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4095.60` | 91,610.00 USD | 91,610.00 USD | 0.00 USD | 78,740.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4099.80` | 238,120.00 USD | 238,120.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 8,800.00 USD |
| `7D` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4104.00` | 419,920.00 USD | 419,920.00 USD | 0.00 USD | 168,400.00 USD | 0.00 USD | 13,400.00 USD |
| `7D` | `4105.70` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 606,780.00 USD | 0.00 USD | 90,730.00 USD |
| `1D` | `4108.20` | 721,280.00 USD | 721,280.00 USD | 0.00 USD | 260,190.00 USD | 0.00 USD | 41,160.00 USD |
| `7D` | `4110.00` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4112.40` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 272,530.00 USD | 0.00 USD | 36,980.00 USD |
| `7D` | `4114.30` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4116.60` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 166,650.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4118.60` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4120.80` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4122.90` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4125.00` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `4127.20` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4129.20` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `4131.50` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.40` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `4135.80` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.60` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.80` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4144.40` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4146.00` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 60,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.70` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4150.20` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 20,760.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4154.40` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.60` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.80` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4175.40` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 27,940.00 USD | 0.00 USD | 5,940.00 USD |
| `7D` | `4178.80` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4179.60` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 66,150.00 USD | 0.00 USD | 4,190.00 USD |
| `7D` | `4183.10` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4183.80` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 81,330.00 USD | 0.00 USD | 5,850.00 USD |
| `7D` | `4187.40` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 292,190.00 USD | 0.00 USD | 46,290.00 USD |
| `1D` | `4188.00` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 18,860.00 USD |
| `7D` | `4191.70` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 594,660.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4192.20` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 152,180.00 USD | 0.00 USD | 19,450.00 USD |
| `7D` | `4196.00` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4196.40` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 86,670.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `4200.30` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4200.60` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4204.60` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4204.80` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `4208.90` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4209.00` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD |
| `1D` | `4213.20` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4213.20` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4217.40` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4217.50` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4221.60` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 50,180.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4221.80` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4225.80` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 11,300.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `4226.10` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4230.00` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 25,610.00 USD | 0.00 USD | 3,120.00 USD |
| `7D` | `4230.40` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4234.20` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 20,800.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `4234.70` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4242.60` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4389.50` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `1D` | `4414.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `4415.30` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4419.00` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4419.60` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4423.20` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 20,450.00 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `4423.90` | 16,120,000.00 USD | 16,120,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4427.40` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 37,230.00 USD | 0.00 USD | 2,530.00 USD |
| `7D` | `4428.20` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 65,320.00 USD | 0.00 USD | 15,320.00 USD |
| `1D` | `4430.00` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 5,090.00 USD |
| `7D` | `4432.50` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 152,220.00 USD | 0.00 USD | 11,860.00 USD |
| `7D` | `4436.80` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,680,000.00 USD | 16,680,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,730,000.00 USD | 16,730,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.63M` | Total OI Tokens: `68,237.7 PAXG`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-0.22%` | 24h OI Change: `-0.15%`
  * Exchange Breakdown: Binance=`107.15M` | Bybit=`20.01M` | OKX=`-` | Hyperliquid=`25.11M`
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
| `15M` | `PAXG` | `45.15%` | `54.85%` | `0.82` | 10,010,000.00 USD |
| `15M` | `Binance` | `52.74%` | `47.26%` | `1.12` | 192,700.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `62.36%` | `37.64%` | `1.66` | 605,240.00 USD |
| `15M` | `KuCoin` | `34.39%` | `65.61%` | `0.52` | 20,290.00 USD |
| `15M` | `Gate` | `51.78%` | `48.22%` | `1.07` | 150,390.00 USD |
| `15M` | `Bitget` | `61.85%` | `38.15%` | `1.62` | 161,060.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `43.54%` | `56.46%` | `0.77` | 8,430,000.00 USD |
| `15M` | `Bitunix` | `53.4%` | `46.6%` | `1.15` | 154,120.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.11%` | `56.89%` | `0.76` | 227,140.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 60,930.00 USD |
| `15M` | `HTX` | `46.42%` | `53.58%` | `0.87` | 224.94 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 3,430.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `52.74%` | `47.26%` | `1.12` | 192,700.00 USD |
| `15M` | `Global Accounts` | `45.15%` | `54.85%` | `0.82` | 10,010,000.00 USD |
| `1H` | `PAXG` | `45.25%` | `54.75%` | `0.83` | 15,010,000.00 USD |
| `1H` | `Binance` | `32.32%` | `67.68%` | `0.48` | 781,120.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `60.39%` | `39.61%` | `1.52` | 1,070,000.00 USD |
| `1H` | `KuCoin` | `47.36%` | `52.64%` | `0.90` | 45,540.00 USD |
| `1H` | `Gate` | `64.73%` | `35.27%` | `1.84` | 447,940.00 USD |
| `1H` | `Bitget` | `61.68%` | `38.32%` | `1.61` | 345,400.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `45.57%` | `54.43%` | `0.84` | 10,990,000.00 USD |
| `1H` | `Bitunix` | `37.48%` | `62.52%` | `0.60` | 405,640.00 USD |
| `1H` | `Hyperliquid` | `96.42%` | `3.58%` | `26.93` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 684,450.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `81.28%` | `18.72%` | `4.34` | 215,310.00 USD |
| `1H` | `HTX` | `69.24%` | `30.76%` | `2.25` | 1,650.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `69.23%` | `30.77%` | `2.25` | 15,060.00 USD |
| `1H` | `Aster` | `100%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `69.16%` | `30.84%` | `2.24` | 0.00 USD |
| `1H` | `Whale Positions` | `32.32%` | `67.68%` | `0.48` | 781,120.00 USD |
| `1H` | `Global Accounts` | `45.25%` | `54.75%` | `0.83` | 15,010,000.00 USD |
| `4H` | `PAXG` | `51.49%` | `48.51%` | `1.06` | 59,430,000.00 USD |
| `4H` | `Binance` | `55.38%` | `44.62%` | `1.24` | 4,490,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `44.29%` | `55.71%` | `0.80` | 5,090,000.00 USD |
| `4H` | `KuCoin` | `47.7%` | `52.3%` | `0.91` | 316,590.00 USD |
| `4H` | `Gate` | `57.36%` | `42.64%` | `1.35` | 1,830,000.00 USD |
| `4H` | `Bitget` | `50.32%` | `49.68%` | `1.01` | 1,780,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `11.49%` | `88.51%` | `0.13` | 38,710,000.00 USD |
| `4H` | `Bitunix` | `54.59%` | `45.41%` | `1.20` | 1,830,000.00 USD |
| `4H` | `Hyperliquid` | `41%` | `59%` | `0.69` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 4,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `60.25%` | `39.75%` | `1.52` | 1,220,000.00 USD |
| `4H` | `HTX` | `54.18%` | `45.82%` | `1.18` | 13,010.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.52%` | `60.48%` | `0.65` | 128,470.00 USD |
| `4H` | `Aster` | `50.42%` | `49.58%` | `1.02` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `15.93%` | `84.07%` | `0.19` | 0.00 USD |
| `4H` | `Whale Positions` | `55.38%` | `44.62%` | `1.24` | 4,490,000.00 USD |
| `4H` | `Global Accounts` | `51.49%` | `48.51%` | `1.06` | 59,430,000.00 USD |


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
| `5m` | -14,270.00 USD | -2,490.00 USD | **`DISTRIBUTION`** |
| `15m` | -30,560.00 USD | -180,910.00 USD | **`DISTRIBUTION`** |
| `30m` | 37,350.00 USD | 668.80 USD | **`ACCUMULATION`** |
| `1h` | -118,670.00 USD | -583,930.00 USD | **`DISTRIBUTION`** |
| `2h` | -326,570.00 USD | 176,860.00 USD | **`DISTRIBUTION`** |
| `4h` | 302,490.00 USD | 972,370.00 USD | **`ACCUMULATION`** |
| `6h` | 181,880.00 USD | 389,150.00 USD | **`ACCUMULATION`** |
| `8h` | -166,030.00 USD | 1,410,000.00 USD | **`ACCUMULATION`** |
| `12h` | -279,510.00 USD | 982,480.00 USD | **`ACCUMULATION`** |
| `24h` | -374,570.00 USD | 1,130,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,260,000.00 USD | -7,630,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,700,000.00 USD | -72,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-14.27K` | 15m=`-30.56K` | 1h=`-118.67K` | 24h=`-374.57K`
* Futures Capital Netflows: 5m=`-2.49K` | 15m=`-180.91K` | 1h=`-583.93K` | 24h=`+1.13M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
