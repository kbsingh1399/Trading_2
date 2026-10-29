# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 02:51:55 IST` (`2026-10-29 21:21:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4021.40` | **Live Ask Quote**: `4021.59` | **Mid Price**: `4021.49`
- **Spread Points**: `19.00` | **Spread BPS**: `0.47 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4029.58` | VWAP Z-Score: `-0.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.86` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.06` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.67` | Lower -3.00σ Band: `3994.49`
  * Upper +2.51σ Band: `4058.94` | Lower -2.51σ Band: `4000.22`
  * Upper +2.01σ Band: `4053.09` | Lower -2.01σ Band: `4006.07`
  * Upper +2.00σ Band: `4052.97` | Lower -2.00σ Band: `4006.19`
  * Upper +1.28σ Band: `4044.55` | Lower -1.28σ Band: `4014.61`
  * Upper +1.00σ Band: `4041.28` | Lower -1.00σ Band: `4017.88`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4020.13` | EMA-20=`4019.02` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4023.17` (Slope: `+0.0000`) | EMA-100=`4029.33`
  * Institutional Anchors: EMA-144=`4031.17` | EMA-200=`4031.48` (Slope: `-0.0489`) | EMA-233=`4030.83`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4039.67` (Distance: `-0.45%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.14%`)
  * Value Area Low (VAL) = `4016.67` (Distance: `+0.12%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4005.41` - `4037.58`
  * Optimal Trade Entry (OTE 0.705): `4029.54`
  * Structural Invalidation Anchor (0.786): `4053.67`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4018.34` | `4022.18` | `4018.34` | `4021.33` | `47` | 190,082.35 USD | 61,912.06 USD | `+32.57%` | 1,513,532.06 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4021.33` | `4021.34` | `4020.02` | `4020.96` | `54` | 215,286.29 USD | -25,841.79 USD | `-12.00%` | 1,487,690.28 USD | `-0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4020.96` | `4020.96` | `4020.95` | `4020.96` | `0` | 1,009.26 USD | 615.21 USD | `+60.96%` | 1,488,305.48 USD | `+0.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4024.17` | `4026.05` | `4020.69` | `4021.36` | `303` | 1,217,913.75 USD | -63,332.79 USD | `-5.20%` | 1,510,119.55 USD | `-0.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4021.37` | `4022.18` | `4017.98` | `4020.96` | `230` | 924,323.44 USD | 24,555.35 USD | `+2.66%` | 1,534,674.90 USD | `-0.02` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4020.96` | `4020.96` | `4020.95` | `4020.95` | `0` | 209.09 USD | -184.96 USD | `-88.46%` | 1,534,489.94 USD | `-0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4017.56` | `4025.99` | `4014.71` | `4025.60` | `520` | 2,091,733.78 USD | -652,688.52 USD | `-31.20%` | 1,838,471.59 USD | `-1.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,599,329.68 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4022.18` | `4017.98` | `4020.96` | `230` | 925,332.70 USD | 25,170.56 USD | `+2.72%` | 1,624,500.24 USD | `+0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.98` | `4020.96` | `1,270` | 5,113,053.68 USD | -213,971.35 USD | `-4.18%` | 1,033,175.98 USD | `-0.65` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.98` | `4020.96` | `1,270` | 5,113,053.68 USD | -213,971.35 USD | `-4.18%` | 1,033,175.98 USD | `-0.65` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID` | `4017.40` | `2.8432` | 11,422.27 USD | 214,213.46 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4017.50` | `4.5883` | 18,433.50 USD | 202,791.19 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4017.60` | `7.9762` | 32,045.18 USD | 184,357.69 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4017.70` | `2.6124` | 10,495.84 USD | 152,312.51 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4017.80` | `3.8528` | 15,479.78 USD | 141,816.67 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4017.90` | `1.4084` | 5,658.81 USD | 126,336.89 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4018.00` | `5.5090` | 22,135.16 USD | 120,678.08 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4018.10` | `4.6064` | 18,508.98 USD | 98,542.92 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4018.20` | `1.5329` | 6,159.50 USD | 80,033.94 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4018.40` | `2.9194` | 11,731.32 USD | 73,874.44 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4018.50` | `1.7798` | 7,152.13 USD | 62,143.13 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4018.60` | `0.8126` | 3,265.51 USD | 54,991.00 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4018.70` | `0.1167` | 468.98 USD | 51,725.49 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4018.80` | `1.9863` | 7,982.54 USD | 51,256.50 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4018.90` | `1.0475` | 4,209.80 USD | 43,273.96 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4019.00` | `0.5075` | 2,039.64 USD | 39,064.16 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4019.10` | `0.0547` | 219.84 USD | 37,024.52 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4019.20` | `0.1190` | 478.28 USD | 36,804.68 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4019.40` | `2.4269` | 9,754.68 USD | 36,326.39 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4019.50` | `6.6107` | 26,571.71 USD | 26,571.71 USD | `11 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4019.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,019.55` | `0.00%` | `-` |
| `ASK` | `4019.60` | `0.9863` | 3,964.53 USD | 3,964.53 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `4019.70` | `5.0693` | 20,377.07 USD | 24,341.60 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `4020.00` | `1.2390` | 4,980.78 USD | 29,322.38 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4020.30` | `4.9115` | 19,745.70 USD | 49,068.08 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4020.40` | `2.4827` | 9,981.45 USD | 59,049.53 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4020.50` | `0.9327` | 3,749.92 USD | 62,799.45 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4020.60` | `0.2153` | 865.64 USD | 63,665.08 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4020.70` | `10.0546` | 40,426.53 USD | 104,091.61 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4020.80` | `13.6479` | 54,875.48 USD | 158,967.09 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4020.90` | `10.9409` | 43,992.26 USD | 202,959.35 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4021.00` | `1.9085` | 7,674.08 USD | 210,633.43 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4021.10` | `3.5813` | 14,400.77 USD | 225,034.20 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4021.20` | `3.0364` | 12,209.97 USD | 237,244.17 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4021.30` | `7.7096` | 31,002.61 USD | 268,246.78 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4021.40` | `0.1167` | 469.30 USD | 268,716.08 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4021.50` | `1.1816` | 4,751.80 USD | 273,467.89 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4021.60` | `0.2278` | 916.12 USD | 274,384.01 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4021.70` | `4.8804` | 19,627.50 USD | 294,011.51 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `4021.80` | `6.4073` | 25,768.88 USD | 319,780.39 USD | `3 orders` | `+0.06%` | `-` |
| `ASK` | `4021.90` | `4.7821` | 19,233.13 USD | 339,013.52 USD | `3 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x4692...164f` | `SHORT` | 25,397,227.60 USD | `6,316.62` | `4133.30` | `4020.70` | `13715.26` | 711,312.60 USD | `+2.80%` | `5X Cross` |
| `53` | `0x5b5d...c060` | `SHORT` | 25,218,867.74 USD | `6,272.26` | `4191.43` | `4020.70` | `32771.82` | 1,070,917.77 USD | `+4.25%` | `4X Cross` |
| `69` | `0xb83d...6e36` | `SHORT` | 22,980,291.96 USD | `5,717.06` | `4234.49` | `4020.70` | `30770.12` | 1,228,583.26 USD | `+5.35%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,409,791.28 USD | `4,828.91` | `4157.43` | `4020.70` | `2229.40` | -666,091.03 USD | `-3.43%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,160,322.40 USD | `3,521.86` | `4129.47` | `4020.70` | `387.19` | -383,084.98 USD | `-2.71%` | `3X Cross` |
| `155` | `0x7a6d...f79c` | `SHORT` | 13,140,504.81 USD | `3,268.21` | `4228.94` | `4020.70` | `4395.90` | 680,574.32 USD | `+5.18%` | `25X Cross` |
| `172` | `0xa742...e390` | `SHORT` | 11,660,030.40 USD | `2,900.00` | `4364.92` | `4020.70` | `4235.67` | 998,245.93 USD | `+8.56%` | `20X Cross` |
| `260` | `0x3678...b209` | `LONG` | 8,843,120.00 USD | `2,200.00` | `4176.09` | `4020.70` | `2594.00` | -344,299.30 USD | `-3.89%` | `25X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,843,120.00 USD | `2,200.00` | `4112.20` | `4020.70` | `4331.15` | 203,734.59 USD | `+2.30%` | `20X Cross` |
| `299` | `0xfc66...ca06` | `SHORT` | 7,963,715.48 USD | `1,981.17` | `4032.86` | `4020.70` | `24596.44` | 26,090.74 USD | `+0.33%` | `3X Cross` |
| `302` | `0xacb6...efbd` | `SHORT` | 7,939,996.10 USD | `1,975.37` | `4048.55` | `4020.70` | `6503.97` | 57,395.62 USD | `+0.72%` | `6X Cross` |
| `369` | `0xc26c...b8f4` | `LONG` | 6,350,774.26 USD | `1,579.95` | `4075.62` | `4020.70` | `0.000000` | -88,522.71 USD | `-1.39%` | `1X Cross` |
| `397` | `0x12d2...f97f` | `LONG` | 5,635,109.08 USD | `1,401.94` | `4278.91` | `4020.70` | `3007.52` | -363,681.49 USD | `-6.45%` | `20X Cross` |
| `552` | `0x63da...8add` | `LONG` | 4,019,600.00 USD | `1,000.00` | `4021.46` | `4020.70` | `3564.11` | -1,860.96 USD | `-0.05%` | `25X Cross` |
| `561` | `0x354b...6425` | `LONG` | 3,971,389.33 USD | `987.74` | `4031.85` | `4020.70` | `0.000000` | -11,018.01 USD | `-0.28%` | `10X Cross` |
| `578` | `0x9aa5...58af` | `LONG` | 3,905,515.02 USD | `971.64` | `4279.98` | `4020.70` | `0.000000` | -253,094.07 USD | `-6.48%` | `20X Cross` |
| `605` | `0xf3dc...1672` | `LONG` | 3,741,124.30 USD | `930.74` | `4024.62` | `4020.70` | `3337.59` | -4,768.26 USD | `-0.13%` | `20X Cross` |
| `671` | `0x4a20...3c26` | `LONG` | 3,366,932.97 USD | `837.40` | `4599.73` | `4020.70` | `0.000000` | -484,887.41 USD | `-14.40%` | `20X Cross` |
| `835` | `0x0fac...7a0a` | `LONG` | 2,760,150.24 USD | `686.49` | `4290.34` | `4020.70` | `1367.89` | -185,108.46 USD | `-6.71%` | `25X Cross` |
| `876` | `0xd8c5...99b0` | `SHORT` | 2,582,009.76 USD | `642.35` | `4175.35` | `4020.70` | `32802.83` | 100,051.42 USD | `+3.87%` | `4X Cross` |
| `905` | `0x625e...a354` | `SHORT` | 2,492,152.00 USD | `620.00` | `4122.81` | `4020.70` | `4342.25` | 63,995.03 USD | `+2.57%` | `20X Cross` |
| `935` | `0xeae3...e8ad` | `SHORT` | 2,411,820.00 USD | `600.00` | `4104.77` | `4020.70` | `4325.27` | 51,045.11 USD | `+2.12%` | `20X Cross` |
| `939` | `0xf285...fa82` | `LONG` | 2,404,146.48 USD | `598.11` | `4146.45` | `4020.70` | `3891.24` | -75,873.08 USD | `-3.16%` | `25X Cross` |
| `960` | `0x12f7...8750` | `LONG` | 2,353,920.77 USD | `585.61` | `4082.77` | `4020.70` | `2472.32` | -36,996.21 USD | `-1.57%` | `10X Cross` |
| `1103` | `0x413c...886c` | `LONG` | 2,009,750.00 USD | `500.00` | `4010.43` | `4020.70` | `0.000000` | 4,533.77 USD | `+0.23%` | `2X Cross` |
| `1116` | `0x61ce...a62b` | `SHORT` | 1,999,814.82 USD | `497.50` | `4071.66` | `4020.70` | `4708.15` | 25,853.97 USD | `+1.29%` | `20X Cross` |
| `1121` | `0x0593...40f9` | `LONG` | 1,994,482.69 USD | `496.18` | `4024.57` | `4020.70` | `3701.73` | -2,421.14 USD | `-0.12%` | `10X Isolated` |
| `1201` | `0x2edd...8179` | `LONG` | 1,885,705.14 USD | `468.80` | `4165.33` | `4022.70` | `0.000000` | -67,004.80 USD | `-3.55%` | `10X Cross` |
| `1246` | `0xead5...69f2` | `LONG` | 1,824,029.76 USD | `453.78` | `4220.88` | `4020.70` | `3538.94` | -91,338.29 USD | `-5.01%` | `5X Isolated` |
| `1308` | `0x7a6d...f79c` | `SHORT` | 1,723,111.69 USD | `428.38` | `4136.09` | `4022.70` | `5726.17` | 48,703.32 USD | `+2.83%` | `10X Cross` |
| `1353` | `0x46fc...1195` | `LONG` | 1,654,462.29 USD | `411.59` | `4055.10` | `4020.70` | `2084.58` | -14,572.06 USD | `-0.88%` | `20X Cross` |
| `1392` | `0xee02...309d` | `SHORT` | 1,608,280.00 USD | `400.00` | `4438.84` | `4020.70` | `4226.89` | 167,258.60 USD | `+10.40%` | `25X Isolated` |
| `1393` | `0x6d15...d374` | `LONG` | 1,607,840.00 USD | `400.00` | `4068.25` | `4020.70` | `3841.81` | -19,460.00 USD | `-1.21%` | `25X Cross` |
| `1437` | `0x02a7...fe9f` | `SHORT` | 1,567,644.00 USD | `390.00` | `4055.02` | `4020.70` | `4306.71` | 13,815.25 USD | `+0.88%` | `25X Cross` |
| `1465` | `0x51f6...2b39` | `LONG` | 1,530,200.55 USD | `380.49` | `4234.66` | `4022.70` | `0.000000` | -81,027.52 USD | `-5.30%` | `10X Cross` |
| `1467` | `0x7e77...b8d2` | `SHORT` | 1,527,866.00 USD | `380.00` | `4131.92` | `4020.70` | `4293.51` | 42,263.64 USD | `+2.77%` | `20X Cross` |
| `1487` | `0x72c2...9b37` | `LONG` | 1,499,801.26 USD | `373.13` | `4000.98` | `4020.70` | `3778.04` | 6,907.74 USD | `+0.46%` | `13X Isolated` |
| `1528` | `0xaa44...b844` | `LONG` | 1,447,020.00 USD | `360.00` | `4043.10` | `4020.70` | `2803.26` | -8,497.63 USD | `-0.59%` | `4X Cross` |
| `1532` | `0x781e...96b7` | `SHORT` | 1,445,391.00 USD | `359.55` | `4365.03` | `4022.70` | `13519.27` | 124,056.48 USD | `+8.58%` | `10X Cross` |
| `1636` | `0xa41f...d50a` | `LONG` | 1,322,263.16 USD | `328.96` | `4468.89` | `4020.70` | `3833.19` | -147,834.69 USD | `-11.18%` | `15X Cross` |
| `1658` | `0x49e9...e1d0` | `SHORT` | 1,300,612.82 USD | `323.48` | `4025.23` | `4020.70` | `31031.91` | 1,465.51 USD | `+0.11%` | `4X Cross` |
| `1674` | `0xada6...6f88` | `LONG` | 1,283,711.40 USD | `319.28` | `4166.46` | `4020.70` | `1957.73` | -46,539.11 USD | `-3.63%` | `5X Cross` |
| `1680` | `0xbf5a...88ba` | `SHORT` | 1,276,813.87 USD | `317.65` | `4091.80` | `4020.70` | `9965.67` | 22,969.16 USD | `+1.80%` | `20X Cross` |
| `1715` | `0xff31...ff6c` | `SHORT` | 1,246,076.00 USD | `310.00` | `4372.43` | `4020.70` | `4789.18` | 109,379.38 USD | `+8.78%` | `10X Isolated` |
| `1877` | `0x50e2...d770` | `LONG` | 1,086,768.80 USD | `270.37` | `4243.58` | `4020.70` | `2562.10` | -60,557.66 USD | `-5.57%` | `20X Cross` |
| `1899` | `0x4c92...4f17` | `SHORT` | 1,072,109.72 USD | `266.72` | `4260.98` | `4020.70` | `6519.38` | 64,382.51 USD | `+6.01%` | `20X Cross` |
| `1967` | `0xd346...c4f3` | `LONG` | 1,025,696.61 USD | `255.17` | `4188.66` | `4020.70` | `3310.42` | -43,139.90 USD | `-4.21%` | `5X Isolated` |
| `2001` | `0x1581...463b` | `LONG` | 1,004,925.00 USD | `250.00` | `4003.77` | `4020.70` | `3542.13` | 3,981.41 USD | `+0.40%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.50` (Vol: 281,800.00 USD, Dist: `+2.05%`) | Long MP=`3936.63` (Vol: 356,200.00 USD, Dist: `--2.27%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.74%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.26%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.72%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.25%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.07%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.20` | 16,290,000.00 USD | 16,290,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.60` | 3,850,000.00 USD | 3,850,000.00 USD | 28,900.00 USD | 0.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.80` | 3,820,000.00 USD | 3,820,000.00 USD | 32,930.00 USD | 0.00 USD | 4,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,070,000.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.00` | 3,780,000.00 USD | 3,780,000.00 USD | 60,480.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,010,000.00 USD | 16,010,000.00 USD | 88,630.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.20` | 3,710,000.00 USD | 3,710,000.00 USD | 43,260.00 USD | 0.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 15,900,000.00 USD | 15,900,000.00 USD | 161,350.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.40` | 3,660,000.00 USD | 3,660,000.00 USD | 21,740.00 USD | 0.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,720,000.00 USD | 15,720,000.00 USD | 103,510.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.60` | 3,640,000.00 USD | 3,640,000.00 USD | 47,040.00 USD | 0.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,610,000.00 USD | 15,610,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3640.80` | 3,590,000.00 USD | 3,590,000.00 USD | 15,030.00 USD | 0.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,470,000.00 USD | 15,470,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.00` | 3,560,000.00 USD | 3,560,000.00 USD | 3,610.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3649.20` | 3,560,000.00 USD | 3,560,000.00 USD | 21,830.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,380,000.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3653.40` | 3,530,000.00 USD | 3,530,000.00 USD | 16,880.00 USD | 0.00 USD | 977.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,360,000.00 USD | 15,360,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3657.60` | 3,510,000.00 USD | 3,510,000.00 USD | 5,110.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,300,000.00 USD | 15,300,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3661.80` | 3,510,000.00 USD | 3,510,000.00 USD | 2,940.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,290,000.00 USD | 15,290,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,270,000.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,260,000.00 USD | 15,260,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 14,840,000.00 USD | 14,840,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,320,000.00 USD | 14,320,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,790,000.00 USD | 13,790,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.00` | 3,500,000.00 USD | 3,500,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,500,000.00 USD | 13,500,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.20` | 3,460,000.00 USD | 3,460,000.00 USD | 94,230.00 USD | 0.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,070,000.00 USD | 13,070,000.00 USD | 157,840.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.40` | 3,360,000.00 USD | 3,360,000.00 USD | 110,490.00 USD | 0.00 USD | 13,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 12,890,000.00 USD | 12,890,000.00 USD | 289,880.00 USD | 0.00 USD | 58,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3867.60` | 3,230,000.00 USD | 3,230,000.00 USD | 202,490.00 USD | 0.00 USD | 28,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,540,000.00 USD | 12,540,000.00 USD | 582,900.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3871.80` | 3,000,000.00 USD | 3,000,000.00 USD | 174,900.00 USD | 0.00 USD | 18,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 11,920,000.00 USD | 11,920,000.00 USD | 309,370.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.00` | 2,810,000.00 USD | 2,810,000.00 USD | 67,070.00 USD | 0.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,560,000.00 USD | 11,560,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.20` | 2,730,000.00 USD | 2,730,000.00 USD | 147,450.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 10,980,000.00 USD | 10,980,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.40` | 2,570,000.00 USD | 2,570,000.00 USD | 30,560.00 USD | 0.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,760,000.00 USD | 10,760,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3888.60` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,670,000.00 USD | 10,670,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3892.80` | 2,510,000.00 USD | 2,510,000.00 USD | 78,150.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,540,000.00 USD | 10,540,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.00` | 2,430,000.00 USD | 2,430,000.00 USD | 43,750.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,410,000.00 USD | 10,410,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.20` | 2,380,000.00 USD | 2,380,000.00 USD | 21,270.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,290,000.00 USD | 10,290,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.40` | 2,350,000.00 USD | 2,350,000.00 USD | 15,640.00 USD | 0.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,240,000.00 USD | 10,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,190,000.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,170,000.00 USD | 10,170,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,800,000.00 USD | 9,800,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,020,000.00 USD | 9,020,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,030,000.00 USD | 8,030,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 6,920,000.00 USD | 6,920,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.80` | 2,340,000.00 USD | 2,340,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,420,000.00 USD | 6,420,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.00` | 2,270,000.00 USD | 2,270,000.00 USD | 211,310.00 USD | 0.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,700,000.00 USD | 5,700,000.00 USD | 375,470.00 USD | 0.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.20` | 2,050,000.00 USD | 2,050,000.00 USD | 187,610.00 USD | 0.00 USD | 23,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,260,000.00 USD | 5,260,000.00 USD | 617,970.00 USD | 0.00 USD | 132,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.40` | 1,840,000.00 USD | 1,840,000.00 USD | 418,420.00 USD | 0.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,510,000.00 USD | 4,510,000.00 USD | 1,020,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.60` | 1,370,000.00 USD | 1,370,000.00 USD | 272,600.00 USD | 0.00 USD | 43,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,410,000.00 USD | 3,410,000.00 USD | 734,780.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.80` | 1,050,000.00 USD | 1,050,000.00 USD | 176,910.00 USD | 0.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.00` | 852,170.00 USD | 852,170.00 USD | 284,040.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.20` | 543,320.00 USD | 543,320.00 USD | 95,580.00 USD | 0.00 USD | 40,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3968.40` | 406,780.00 USD | 406,780.00 USD | 30,740.00 USD | 0.00 USD | 19,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3972.60` | 356,250.00 USD | 356,250.00 USD | 127,000.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3976.80` | 221,950.00 USD | 221,950.00 USD | 109,130.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.00` | 104,130.00 USD | 104,130.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3985.20` | 63,050.00 USD | 63,050.00 USD | 54,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3989.40` | 8,420.00 USD | 8,420.00 USD | 0.00 USD | 0.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.40` | 29,250.00 USD | 29,250.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.80` | 439,920.00 USD | 439,920.00 USD | 209,940.00 USD | 0.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,360,000.00 USD | 5,360,000.00 USD | 606,780.00 USD | 0.00 USD | 112,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.00` | 853,620.00 USD | 853,620.00 USD | 372,780.00 USD | 0.00 USD | 40,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,490,000.00 USD | 6,490,000.00 USD | 1,060,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.20` | 1,180,000.00 USD | 1,180,000.00 USD | 288,670.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,250,000.00 USD | 7,250,000.00 USD | 653,860.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.40` | 1,450,000.00 USD | 1,450,000.00 USD | 232,080.00 USD | 0.00 USD | 30,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,130,000.00 USD | 8,130,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.60` | 1,640,000.00 USD | 1,640,000.00 USD | 185,550.00 USD | 0.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,850,000.00 USD | 8,850,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.80` | 1,890,000.00 USD | 1,890,000.00 USD | 210,630.00 USD | 0.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,100,000.00 USD | 9,100,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4128.00` | 1,960,000.00 USD | 1,960,000.00 USD | 45,250.00 USD | 0.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,300,000.00 USD | 9,300,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4132.20` | 2,020,000.00 USD | 2,020,000.00 USD | 41,070.00 USD | 0.00 USD | 17,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,530,000.00 USD | 9,530,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4136.40` | 2,150,000.00 USD | 2,150,000.00 USD | 121,070.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,780,000.00 USD | 9,780,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.60` | 2,240,000.00 USD | 2,240,000.00 USD | 81,660.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.80` | 2,290,000.00 USD | 2,290,000.00 USD | 32,780.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.00` | 2,330,000.00 USD | 2,330,000.00 USD | 41,040.00 USD | 0.00 USD | 6,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.20` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,370,000.00 USD | 11,370,000.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,810,000.00 USD | 11,810,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.20` | 2,350,000.00 USD | 2,350,000.00 USD | 10,060.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,050,000.00 USD | 12,050,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.40` | 2,430,000.00 USD | 2,430,000.00 USD | 74,700.00 USD | 0.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,390,000.00 USD | 12,390,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4182.60` | 2,540,000.00 USD | 2,540,000.00 USD | 104,570.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,570,000.00 USD | 12,570,000.00 USD | 146,480.00 USD | 0.00 USD | 34,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4186.80` | 2,740,000.00 USD | 2,740,000.00 USD | 179,480.00 USD | 0.00 USD | 19,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 12,910,000.00 USD | 12,910,000.00 USD | 292,190.00 USD | 0.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.00` | 2,890,000.00 USD | 2,890,000.00 USD | 129,190.00 USD | 0.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,520,000.00 USD | 13,520,000.00 USD | 567,920.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.20` | 3,040,000.00 USD | 3,040,000.00 USD | 132,410.00 USD | 0.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 13,850,000.00 USD | 13,850,000.00 USD | 286,520.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.40` | 3,130,000.00 USD | 3,130,000.00 USD | 80,330.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,350,000.00 USD | 14,350,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4203.60` | 3,270,000.00 USD | 3,270,000.00 USD | 125,260.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,610,000.00 USD | 14,610,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4207.80` | 3,320,000.00 USD | 3,320,000.00 USD | 30,560.00 USD | 0.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,730,000.00 USD | 14,730,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.00` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 14,840,000.00 USD | 14,840,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4216.20` | 3,400,000.00 USD | 3,400,000.00 USD | 68,400.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 14,960,000.00 USD | 14,960,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4220.40` | 3,450,000.00 USD | 3,450,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,070,000.00 USD | 15,070,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4224.60` | 3,470,000.00 USD | 3,470,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,150,000.00 USD | 15,150,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4228.80` | 3,500,000.00 USD | 3,500,000.00 USD | 27,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,200,000.00 USD | 15,200,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4233.00` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,240,000.00 USD | 15,240,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,260,000.00 USD | 15,260,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,400,000.00 USD | 15,400,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,540,000.00 USD | 15,540,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,670,000.00 USD | 15,670,000.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,790,000.00 USD | 15,790,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 15,850,000.00 USD | 15,850,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4417.80` | 3,530,000.00 USD | 3,530,000.00 USD | 23,120.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 15,960,000.00 USD | 15,960,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.00` | 3,550,000.00 USD | 3,550,000.00 USD | 21,930.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,010,000.00 USD | 16,010,000.00 USD | 35,830.00 USD | 0.00 USD | 8,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.20` | 3,590,000.00 USD | 3,590,000.00 USD | 30,460.00 USD | 0.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,090,000.00 USD | 16,090,000.00 USD | 65,320.00 USD | 0.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.40` | 3,650,000.00 USD | 3,650,000.00 USD | 56,840.00 USD | 0.00 USD | 8,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,250,000.00 USD | 16,250,000.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4434.60` | 3,690,000.00 USD | 3,690,000.00 USD | 33,230.00 USD | 0.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,340,000.00 USD | 16,340,000.00 USD | 76,360.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.70` | 3,720,000.00 USD | 3,720,000.00 USD | 21,740.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,470,000.00 USD | 16,470,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,550,000.00 USD | 16,550,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,590,000.00 USD | 16,590,000.00 USD | 37,880.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3617.40` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 31,840.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `3619.70` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 12,060.00 USD |
| `1D` | `3621.60` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 37,240.00 USD | 0.00 USD | 3,960.00 USD |
| `7D` | `3623.90` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3625.80` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 59,900.00 USD | 0.00 USD | 9,850.00 USD |
| `7D` | `3628.10` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3630.00` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 42,060.00 USD | 0.00 USD | 5,810.00 USD |
| `7D` | `3632.30` | 15,730,000.00 USD | 0.00 USD | 15,730,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3634.20` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 25,700.00 USD | 0.00 USD | 3,570.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3638.40` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 39,820.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `3640.70` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3642.60` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3646.80` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 8,210.00 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `3649.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.00` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 22,380.00 USD | 0.00 USD | 1,570.00 USD |
| `7D` | `3653.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.20` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 9,470.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `3659.40` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 6,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3663.60` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `3665.90` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.60` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `3854.90` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.80` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3861.00` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 104,570.00 USD | 0.00 USD | 14,090.00 USD |
| `7D` | `3863.30` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 204,080.00 USD | 0.00 USD | 53,800.00 USD |
| `1D` | `3865.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 196,130.00 USD | 0.00 USD | 21,950.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3869.40` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 144,340.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3873.60` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 120,620.00 USD | 0.00 USD | 16,830.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3877.80` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 109,560.00 USD | 0.00 USD | 4,670.00 USD |
| `7D` | `3880.10` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3882.00` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 88,130.00 USD | 0.00 USD | 24,810.00 USD |
| `7D` | `3884.30` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3886.20` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 18,450.00 USD | 0.00 USD | 9,220.00 USD |
| `7D` | `3888.50` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3890.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 38,650.00 USD | 0.00 USD | 8,650.00 USD |
| `7D` | `3892.70` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3894.60` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 61,400.00 USD | 0.00 USD | 5,080.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3898.80` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3901.10` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3903.00` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 29,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `3907.20` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3932.40` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 5,620.00 USD | 0.00 USD | 4,300.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3936.60` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 153,970.00 USD | 0.00 USD | 9,520.00 USD |
| `7D` | `3938.90` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3940.80` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 188,670.00 USD | 0.00 USD | 20,380.00 USD |
| `7D` | `3943.10` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 417,530.00 USD | 0.00 USD | 73,100.00 USD |
| `1D` | `3945.00` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 380,160.00 USD | 0.00 USD | 39,170.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD |
| `1D` | `3949.20` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 267,540.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3953.40` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,340.00 USD | 0.00 USD | 36,460.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3957.60` | 904,730.00 USD | 0.00 USD | 904,730.00 USD | 192,270.00 USD | 0.00 USD | 11,660.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3961.80` | 700,800.00 USD | 0.00 USD | 700,800.00 USD | 223,260.00 USD | 0.00 USD | 43,960.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3966.00` | 433,570.00 USD | 0.00 USD | 433,570.00 USD | 45,250.00 USD | 0.00 USD | 23,060.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3970.20` | 365,260.00 USD | 0.00 USD | 365,260.00 USD | 41,070.00 USD | 0.00 USD | 17,850.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3974.40` | 306,340.00 USD | 0.00 USD | 306,340.00 USD | 139,160.00 USD | 0.00 USD | 9,720.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3978.60` | 157,470.00 USD | 0.00 USD | 157,470.00 USD | 63,570.00 USD | 0.00 USD | 4,090.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3982.80` | 89,810.00 USD | 0.00 USD | 89,810.00 USD | 48,240.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `1D` | `3987.00` | 27,350.00 USD | 0.00 USD | 27,350.00 USD | 19,690.00 USD | 0.00 USD | 7,660.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4024.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4024.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4096.20` | 116,420.00 USD | 116,420.00 USD | 0.00 USD | 103,550.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4100.40` | 288,860.00 USD | 288,860.00 USD | 0.00 USD | 163,640.00 USD | 0.00 USD | 8,800.00 USD |
| `7D` | `4102.70` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 69,830.00 USD |
| `1D` | `4104.60` | 530,520.00 USD | 530,520.00 USD | 0.00 USD | 212,750.00 USD | 0.00 USD | 28,910.00 USD |
| `7D` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 547,190.00 USD | 0.00 USD | 101,580.00 USD |
| `1D` | `4108.80` | 980,580.00 USD | 980,580.00 USD | 0.00 USD | 399,060.00 USD | 0.00 USD | 51,000.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4113.00` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 274,150.00 USD | 0.00 USD | 41,550.00 USD |
| `7D` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4117.20` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 169,570.00 USD | 0.00 USD | 20,170.00 USD |
| `7D` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4121.40` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 284,040.00 USD | 0.00 USD | 19,380.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4125.60` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 89,420.00 USD | 0.00 USD | 45,200.00 USD |
| `7D` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4129.80` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 36,900.00 USD | 0.00 USD | 12,430.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4134.00` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 85,540.00 USD | 0.00 USD | 14,840.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4138.20` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 114,570.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4142.40` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4146.60` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `1D` | `4150.80` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 7,660.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.00` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.20` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 94,230.00 USD | 0.00 USD | 4,400.00 USD |
| `7D` | `4182.50` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 24,870.00 USD |
| `1D` | `4184.40` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 93,810.00 USD | 0.00 USD | 12,420.00 USD |
| `7D` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 270,030.00 USD | 0.00 USD | 54,580.00 USD |
| `1D` | `4188.60` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 180,150.00 USD | 0.00 USD | 24,620.00 USD |
| `7D` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.80` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 157,760.00 USD | 0.00 USD | 18,170.00 USD |
| `7D` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4197.00` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 90,920.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4201.20` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 132,280.00 USD | 0.00 USD | 5,890.00 USD |
| `7D` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4205.40` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 59,580.00 USD | 0.00 USD | 23,230.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4209.60` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 18,450.00 USD | 0.00 USD | 9,220.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4213.80` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 26,200.00 USD | 0.00 USD | 8,280.00 USD |
| `7D` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4218.00` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 73,860.00 USD | 0.00 USD | 5,310.00 USD |
| `7D` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4222.20` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 21,840.00 USD | 0.00 USD | 133.60 USD |
| `7D` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4226.40` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 21,270.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4230.60` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4415.40` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 2,900.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4419.60` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 29,730.00 USD | 0.00 USD | 936.99 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4423.80` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 25,070.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 11,470.00 USD |
| `1D` | `4428.00` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 51,570.00 USD | 0.00 USD | 6,840.00 USD |
| `7D` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4432.20` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 34,320.00 USD | 0.00 USD | 5,750.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `4436.40` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 35,600.00 USD | 0.00 USD | 4,860.00 USD |
| `1D` | `4438.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 2,930.00 USD |
| `7D` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.86M` | Total OI Tokens: `68,292.8 PAXG`
  * 1h OI Change: `-0.05%` | 4h OI Change: `-0.24%` | 24h OI Change: `+0.18%`
  * Exchange Breakdown: Binance=`107.20M` | Bybit=`19.94M` | OKX=`-` | Hyperliquid=`24.67M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.35K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
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
| `15M` | `PAXG` | `58.13%` | `41.87%` | `1.39` | 2,370,000.00 USD |
| `15M` | `Binance` | `58.31%` | `41.69%` | `1.40` | 464,220.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `76.17%` | `23.83%` | `3.20` | 605,590.00 USD |
| `15M` | `KuCoin` | `65.41%` | `34.59%` | `1.89` | 19,860.00 USD |
| `15M` | `Gate` | `56.97%` | `43.03%` | `1.32` | 99,820.00 USD |
| `15M` | `Bitget` | `48.21%` | `51.79%` | `0.93` | 43,660.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `37.42%` | `62.58%` | `0.60` | 510,890.00 USD |
| `15M` | `Bitunix` | `40.15%` | `59.85%` | `0.67` | 261,560.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `80.59%` | `19.41%` | `4.15` | 324,400.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 45,160.00 USD |
| `15M` | `HTX` | `60.86%` | `39.14%` | `1.55` | 943.41 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 184.64 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `58.31%` | `41.69%` | `1.40` | 464,220.00 USD |
| `15M` | `Global Accounts` | `58.13%` | `41.87%` | `1.39` | 2,370,000.00 USD |
| `1H` | `PAXG` | `30.16%` | `69.84%` | `0.43` | 21,360,000.00 USD |
| `1H` | `Binance` | `46.12%` | `53.88%` | `0.86` | 2,190,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `49.07%` | `50.93%` | `0.96` | 1,700,000.00 USD |
| `1H` | `KuCoin` | `18.18%` | `81.82%` | `0.22` | 146,630.00 USD |
| `1H` | `Gate` | `37.38%` | `62.62%` | `0.60` | 847,860.00 USD |
| `1H` | `Bitget` | `53.65%` | `46.35%` | `1.16` | 422,040.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `19.35%` | `80.65%` | `0.24` | 12,770,000.00 USD |
| `1H` | `Bitunix` | `41.71%` | `58.29%` | `0.72` | 1,230,000.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `57.53%` | `42.47%` | `1.35` | 1,750,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `10.82%` | `89.18%` | `0.12` | 295,930.00 USD |
| `1H` | `HTX` | `28.53%` | `71.47%` | `0.40` | 5,120.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `37.39%` | `62.61%` | `0.60` | 9,720.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `46.12%` | `53.88%` | `0.86` | 2,190,000.00 USD |
| `1H` | `Global Accounts` | `30.16%` | `69.84%` | `0.43` | 21,360,000.00 USD |
| `4H` | `PAXG` | `45.92%` | `54.08%` | `0.85` | 64,880,000.00 USD |
| `4H` | `Binance` | `54.17%` | `45.83%` | `1.18` | 5,630,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `53.5%` | `46.5%` | `1.15` | 6,200,000.00 USD |
| `4H` | `KuCoin` | `35.96%` | `64.04%` | `0.56` | 378,350.00 USD |
| `4H` | `Gate` | `52.83%` | `47.17%` | `1.12` | 2,610,000.00 USD |
| `4H` | `Bitget` | `52.87%` | `47.13%` | `1.12` | 1,910,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `42.3%` | `57.7%` | `0.73` | 39,090,000.00 USD |
| `4H` | `Bitunix` | `52.16%` | `47.84%` | `1.09` | 2,600,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.58%` | `46.42%` | `1.15` | 5,220,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `13.6%` | `86.4%` | `0.16` | 1,080,000.00 USD |
| `4H` | `HTX` | `54.46%` | `45.54%` | `1.20` | 14,380.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.16%` | `61.84%` | `0.62` | 153,070.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.17%` | `45.83%` | `1.18` | 5,630,000.00 USD |
| `4H` | `Global Accounts` | `45.92%` | `54.08%` | `0.85` | 64,880,000.00 USD |


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
| `5m` | -10,990.00 USD | -28,860.00 USD | **`DISTRIBUTION`** |
| `15m` | -182,630.00 USD | 25,240.00 USD | **`DISTRIBUTION`** |
| `30m` | -174,490.00 USD | -43,930.00 USD | **`DISTRIBUTION`** |
| `1h` | -10,260.00 USD | -425,220.00 USD | **`DISTRIBUTION`** |
| `2h` | -64,550.00 USD | -116,690.00 USD | **`DISTRIBUTION`** |
| `4h` | -680,320.00 USD | -104,010.00 USD | **`DISTRIBUTION`** |
| `6h` | 47,580.00 USD | 678,130.00 USD | **`ACCUMULATION`** |
| `8h` | -111,920.00 USD | 1,050,000.00 USD | **`ACCUMULATION`** |
| `12h` | -317,030.00 USD | 1,270,000.00 USD | **`ACCUMULATION`** |
| `24h` | 76,450.00 USD | 1,540,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,190,000.00 USD | -7,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,920,000.00 USD | -71,370,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-10.99K` | 15m=`-182.63K` | 1h=`-10.26K` | 24h=`+76.45K`
* Futures Capital Netflows: 5m=`-28.86K` | 15m=`+25.24K` | 1h=`-425.22K` | 24h=`+1.54M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `4008.15` (Risk Distance: `8.52` pts)
  * +2.5R Take Profit: `4037.98`
  * Mathematical Lot Sizing: **`1.17 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4039.67` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4048.19` (Risk Distance: `8.52` pts)
  * +2.5R Take Profit: `4018.36`
  * Mathematical Lot Sizing: **`1.17 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4053.67`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
