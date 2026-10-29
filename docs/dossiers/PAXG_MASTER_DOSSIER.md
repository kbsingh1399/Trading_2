# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 03:04:03 IST` (`2026-10-29 21:34:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `BID` | `4015.80` | `10.0685` | 40,433.08 USD | 658,766.04 USD | `4 orders` | `-0.07%` | `-` |
| `BID` | `4015.90` | `7.6639` | 30,777.46 USD | 618,332.96 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `4016.00` | `25.4737` | 102,302.38 USD | 587,555.50 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `4016.20` | `1.9219` | 7,718.73 USD | 485,253.13 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4016.30` | `2.0493` | 8,230.60 USD | 477,534.39 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4016.40` | `51.5757` | 207,148.64 USD | 469,303.79 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4016.50` | `3.9249` | 15,764.36 USD | 262,155.15 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4016.60` | `0.9336` | 3,749.90 USD | 246,390.78 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4016.70` | `10.1898` | 40,929.37 USD | 242,640.89 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4016.80` | `0.9336` | 3,750.08 USD | 201,711.52 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4016.90` | `1.3885` | 5,577.47 USD | 197,961.43 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4017.00` | `6.0346` | 24,240.99 USD | 192,383.97 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `4017.10` | `4.2207` | 16,954.97 USD | 168,142.98 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4017.20` | `5.8657` | 23,563.69 USD | 151,188.00 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4017.30` | `20.3221` | 81,639.97 USD | 127,624.31 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4017.60` | `0.0859` | 345.11 USD | 45,984.34 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4017.70` | `7.4868` | 30,079.72 USD | 45,639.23 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4017.80` | `0.9878` | 3,968.78 USD | 15,559.51 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4017.90` | `1.4084` | 5,658.81 USD | 11,590.73 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4018.10` | `1.4763` | 5,931.92 USD | 5,931.92 USD | `1 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `4018.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,018.45` | `0.00%` | `-` |
| `ASK` | `4018.80` | `17.8311` | 71,659.62 USD | 71,659.62 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `4018.90` | `2.1744` | 8,738.70 USD | 80,398.32 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4019.00` | `2.4267` | 9,752.91 USD | 90,151.23 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4019.10` | `2.6127` | 10,500.70 USD | 100,651.93 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4019.20` | `3.8808` | 15,597.71 USD | 116,249.64 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4019.40` | `2.9834` | 11,991.48 USD | 128,241.12 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4019.50` | `4.1572` | 16,709.87 USD | 144,950.99 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4019.60` | `7.4020` | 29,753.08 USD | 174,704.06 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4019.70` | `2.1740` | 8,738.83 USD | 183,442.89 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4019.80` | `0.0620` | 249.23 USD | 183,692.12 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4019.90` | `3.5858` | 14,414.56 USD | 198,106.68 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4020.00` | `5.5244` | 22,208.09 USD | 220,314.77 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4020.10` | `3.5452` | 14,252.06 USD | 234,566.82 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4020.30` | `1.0048` | 4,039.60 USD | 238,606.42 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4020.40` | `6.1195` | 24,602.84 USD | 263,209.26 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4020.50` | `14.6160` | 58,763.63 USD | 321,972.89 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4020.60` | `2.1170` | 8,511.61 USD | 330,484.50 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4020.70` | `0.9327` | 3,750.11 USD | 334,234.60 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `4020.80` | `2.6113` | 10,499.52 USD | 344,734.12 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `4020.90` | `3.1932` | 12,839.54 USD | 357,573.66 USD | `3 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `50` | `0x4692...164f` | `SHORT` | 25,377,255.47 USD | `6,315.11` | `4133.25` | `4018.10` | `13786.21` | 724,660.16 USD | `+2.86%` | `5X Cross` |
| `52` | `0x5b5d...c060` | `SHORT` | 25,206,323.22 USD | `6,272.26` | `4191.43` | `4018.10` | `32385.59` | 1,083,462.28 USD | `+4.30%` | `4X Cross` |
| `69` | `0xb83d...6e36` | `SHORT` | 22,979,720.26 USD | `5,717.06` | `4234.49` | `4018.10` | `30064.36` | 1,229,154.97 USD | `+5.35%` | `5X Cross` |
| `95` | `0xec0b...b078` | `LONG` | 19,409,791.28 USD | `4,828.91` | `4157.43` | `4018.10` | `2195.71` | -666,091.03 USD | `-3.43%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,160,589.02 USD | `3,523.59` | `4129.41` | `4018.10` | `409.94` | -389,776.85 USD | `-2.75%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,133,968.39 USD | `3,268.21` | `4228.94` | `4018.10` | `4398.92` | 687,110.74 USD | `+5.23%` | `25X Cross` |
| `173` | `0xa742...e390` | `SHORT` | 11,655,680.40 USD | `2,900.00` | `4364.92` | `4018.10` | `4235.67` | 1,002,595.93 USD | `+8.60%` | `20X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,842,900.00 USD | `2,200.00` | `4112.20` | `4018.10` | `4331.15` | 203,954.59 USD | `+2.31%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,841,360.00 USD | `2,200.00` | `4176.09` | `4018.10` | `2544.09` | -346,059.30 USD | `-3.91%` | `25X Cross` |
| `267` | `0xfc66...ca06` | `SHORT` | 8,768,932.00 USD | `2,182.03` | `4031.64` | `4018.10` | `22728.33` | 28,236.11 USD | `+0.32%` | `3X Cross` |
| `301` | `0xacb6...efbd` | `SHORT` | 7,939,996.10 USD | `1,975.37` | `4048.55` | `4018.10` | `6500.82` | 57,395.62 USD | `+0.72%` | `6X Cross` |
| `369` | `0xc26c...b8f4` | `LONG` | 6,349,352.30 USD | `1,579.95` | `4075.62` | `4018.10` | `0.000000` | -89,944.67 USD | `-1.42%` | `1X Cross` |
| `400` | `0x12d2...f97f` | `LONG` | 5,635,109.08 USD | `1,401.94` | `4278.91` | `4018.10` | `2897.68` | -363,681.49 USD | `-6.45%` | `20X Cross` |
| `556` | `0x63da...8add` | `LONG` | 4,019,300.00 USD | `1,000.00` | `4021.46` | `4018.10` | `3564.11` | -2,160.96 USD | `-0.05%` | `25X Cross` |
| `569` | `0x354b...6425` | `LONG` | 3,969,216.31 USD | `987.74` | `4031.85` | `4018.10` | `0.000000` | -13,191.02 USD | `-0.33%` | `10X Cross` |
| `579` | `0x9aa5...58af` | `LONG` | 3,905,515.02 USD | `971.64` | `4279.98` | `4018.10` | `0.000000` | -253,094.07 USD | `-6.48%` | `20X Cross` |
| `608` | `0xf3dc...1672` | `LONG` | 3,741,496.60 USD | `930.74` | `4024.62` | `4018.10` | `3337.59` | -4,395.96 USD | `-0.12%` | `20X Cross` |
| `674` | `0x4a20...3c26` | `LONG` | 3,365,341.91 USD | `837.40` | `4599.73` | `4018.10` | `0.000000` | -486,478.47 USD | `-14.46%` | `20X Cross` |
| `830` | `0x0fac...7a0a` | `LONG` | 2,758,777.27 USD | `686.49` | `4290.34` | `4018.10` | `1285.77` | -186,481.43 USD | `-6.76%` | `25X Cross` |
| `876` | `0xd8c5...99b0` | `SHORT` | 2,581,495.87 USD | `642.35` | `4175.35` | `4018.10` | `32910.90` | 100,565.31 USD | `+3.90%` | `4X Cross` |
| `911` | `0x625e...a354` | `SHORT` | 2,492,090.00 USD | `620.00` | `4122.81` | `4018.10` | `4342.25` | 64,057.03 USD | `+2.57%` | `20X Cross` |
| `943` | `0xeae3...e8ad` | `SHORT` | 2,411,280.00 USD | `600.00` | `4104.77` | `4018.10` | `4325.27` | 51,585.11 USD | `+2.14%` | `20X Cross` |
| `945` | `0xf285...fa82` | `LONG` | 2,403,608.18 USD | `598.11` | `4146.45` | `4018.10` | `3891.24` | -76,411.37 USD | `-3.18%` | `25X Cross` |
| `961` | `0x12f7...8750` | `LONG` | 2,353,745.09 USD | `585.61` | `4082.77` | `4018.10` | `2446.75` | -37,171.89 USD | `-1.58%` | `10X Cross` |
| `1099` | `0x413c...886c` | `LONG` | 2,009,450.00 USD | `500.00` | `4010.43` | `4018.10` | `0.000000` | 4,233.77 USD | `+0.21%` | `2X Cross` |
| `1108` | `0x61ce...a62b` | `SHORT` | 1,999,615.82 USD | `497.50` | `4071.66` | `4018.10` | `4703.70` | 26,052.97 USD | `+1.30%` | `20X Cross` |
| `1114` | `0x0593...40f9` | `LONG` | 1,994,036.13 USD | `496.18` | `4024.57` | `4018.10` | `3701.73` | -2,867.70 USD | `-0.14%` | `10X Isolated` |
| `1197` | `0x2edd...8179` | `LONG` | 1,885,095.70 USD | `468.80` | `4165.33` | `4020.43` | `0.000000` | -67,614.24 USD | `-3.59%` | `10X Cross` |
| `1239` | `0xead5...69f2` | `LONG` | 1,823,575.98 USD | `453.78` | `4220.88` | `4018.10` | `3538.94` | -91,792.08 USD | `-5.03%` | `5X Isolated` |
| `1307` | `0x7a6d...f79c` | `SHORT` | 1,723,197.37 USD | `428.38` | `4136.09` | `4020.43` | `5653.33` | 48,617.64 USD | `+2.82%` | `10X Cross` |
| `1356` | `0x46fc...1195` | `LONG` | 1,653,903.22 USD | `411.55` | `4055.10` | `4018.10` | `2115.75` | -14,982.32 USD | `-0.91%` | `20X Cross` |
| `1390` | `0x6d15...d374` | `LONG` | 1,607,800.00 USD | `400.00` | `4068.25` | `4018.10` | `3841.81` | -19,500.00 USD | `-1.21%` | `25X Cross` |
| `1391` | `0xee02...309d` | `SHORT` | 1,607,480.00 USD | `400.00` | `4438.84` | `4018.10` | `4226.89` | 168,058.60 USD | `+10.45%` | `25X Isolated` |
| `1432` | `0x02a7...fe9f` | `SHORT` | 1,567,293.00 USD | `390.00` | `4055.02` | `4018.10` | `4306.71` | 14,166.25 USD | `+0.90%` | `25X Cross` |
| `1464` | `0x51f6...2b39` | `LONG` | 1,529,972.25 USD | `380.49` | `4234.66` | `4020.43` | `0.000000` | -81,255.81 USD | `-5.31%` | `10X Cross` |
| `1467` | `0x7e77...b8d2` | `SHORT` | 1,527,144.00 USD | `380.00` | `4131.92` | `4018.10` | `4293.51` | 42,985.64 USD | `+2.81%` | `20X Cross` |
| `1485` | `0x72c2...9b37` | `LONG` | 1,499,726.63 USD | `373.13` | `4000.98` | `4018.10` | `3778.04` | 6,833.12 USD | `+0.46%` | `13X Isolated` |
| `1528` | `0xaa44...b844` | `LONG` | 1,446,948.00 USD | `360.00` | `4043.10` | `4018.10` | `2803.26` | -8,569.63 USD | `-0.59%` | `4X Cross` |
| `1529` | `0x781e...96b7` | `SHORT` | 1,446,361.78 USD | `359.55` | `4365.03` | `4020.43` | `13336.26` | 123,085.70 USD | `+8.51%` | `10X Cross` |
| `1643` | `0xa41f...d50a` | `LONG` | 1,322,263.16 USD | `328.96` | `4468.89` | `4018.10` | `3833.19` | -147,834.69 USD | `-11.18%` | `15X Cross` |
| `1659` | `0x49e9...e1d0` | `SHORT` | 1,299,965.86 USD | `323.48` | `4025.23` | `4018.10` | `31570.20` | 2,112.47 USD | `+0.16%` | `4X Cross` |
| `1677` | `0xada6...6f88` | `LONG` | 1,283,136.71 USD | `319.28` | `4166.46` | `4018.10` | `1978.11` | -47,113.80 USD | `-3.67%` | `5X Cross` |
| `1680` | `0xbf5a...88ba` | `SHORT` | 1,276,718.57 USD | `317.65` | `4091.80` | `4018.10` | `9963.22` | 23,064.46 USD | `+1.81%` | `20X Cross` |
| `1715` | `0xff31...ff6c` | `SHORT` | 1,245,828.00 USD | `310.00` | `4372.43` | `4018.10` | `4789.18` | 109,627.38 USD | `+8.80%` | `10X Isolated` |
| `1884` | `0x50e2...d770` | `LONG` | 1,086,552.51 USD | `270.37` | `4243.58` | `4018.10` | `2562.10` | -60,773.95 USD | `-5.59%` | `20X Cross` |
| `1898` | `0x4c92...4f17` | `SHORT` | 1,071,896.35 USD | `266.72` | `4260.98` | `4018.10` | `6520.66` | 64,595.89 USD | `+6.03%` | `20X Cross` |
| `1967` | `0xd346...c4f3` | `LONG` | 1,025,466.95 USD | `255.17` | `4188.66` | `4018.10` | `3310.42` | -43,369.56 USD | `-4.23%` | `5X Isolated` |
| `2000` | `0x1581...463b` | `LONG` | 1,004,925.00 USD | `250.00` | `4003.77` | `4018.10` | `3529.76` | 3,981.41 USD | `+0.40%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


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
| `7D` | `Long Liquidation` | `3611.30` | 16,280,000.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 3,860,000.00 USD | 3,860,000.00 USD | 31,030.00 USD | 0.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,070,000.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 3,830,000.00 USD | 3,830,000.00 USD | 67,500.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 16,010,000.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 3,760,000.00 USD | 3,760,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,910,000.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 3,710,000.00 USD | 3,710,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,730,000.00 USD | 15,730,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.60` | 3,670,000.00 USD | 3,670,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,610,000.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.80` | 3,630,000.00 USD | 3,630,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,480,000.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3644.00` | 3,600,000.00 USD | 3,600,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3648.20` | 3,590,000.00 USD | 3,590,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,380,000.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3652.40` | 3,580,000.00 USD | 3,580,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,360,000.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3656.60` | 3,550,000.00 USD | 3,550,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,330,000.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.80` | 3,550,000.00 USD | 3,550,000.00 USD | 4,080.00 USD | 0.00 USD | 812.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,290,000.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3665.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 396.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,270,000.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,260,000.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,890,000.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,410,000.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,880,000.00 USD | 13,880,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.00` | 3,540,000.00 USD | 3,540,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,550,000.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.20` | 3,510,000.00 USD | 3,510,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,240,000.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.40` | 3,420,000.00 USD | 3,420,000.00 USD | 129,370.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,960,000.00 USD | 12,960,000.00 USD | 204,080.00 USD | 0.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.60` | 3,280,000.00 USD | 3,280,000.00 USD | 193,320.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,700,000.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.80` | 3,060,000.00 USD | 3,060,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,160,000.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.00` | 2,890,000.00 USD | 2,890,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,740,000.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.20` | 2,780,000.00 USD | 2,780,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,200,000.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.40` | 2,630,000.00 USD | 2,630,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,860,000.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.60` | 2,560,000.00 USD | 2,560,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,720,000.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.80` | 2,530,000.00 USD | 2,530,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,610,000.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3896.00` | 2,460,000.00 USD | 2,460,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,480,000.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3900.20` | 2,410,000.00 USD | 2,410,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,370,000.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3904.40` | 2,390,000.00 USD | 2,390,000.00 USD | 24,370.00 USD | 0.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,280,000.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3908.60` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,190,000.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,170,000.00 USD | 10,170,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,440,000.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,490,000.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,600,000.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.80` | 2,360,000.00 USD | 2,360,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,760,000.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.00` | 2,330,000.00 USD | 2,330,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,300,000.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.20` | 2,150,000.00 USD | 2,150,000.00 USD | 250,380.00 USD | 0.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,640,000.00 USD | 5,640,000.00 USD | 417,530.00 USD | 0.00 USD | 73,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,880,000.00 USD | 1,880,000.00 USD | 360,890.00 USD | 0.00 USD | 45,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.60` | 1,470,000.00 USD | 1,470,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.80` | 1,070,000.00 USD | 1,070,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.00` | 856,730.00 USD | 856,730.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 568,300.00 USD | 568,300.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 409,520.00 USD | 409,520.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.60` | 359,430.00 USD | 359,430.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.80` | 264,840.00 USD | 264,840.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3980.00` | 131,870.00 USD | 131,870.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3984.20` | 64,460.00 USD | 64,460.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3988.40` | 8,150.00 USD | 8,150.00 USD | 2,110.00 USD | 0.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.80` | 382,460.00 USD | 382,460.00 USD | 178,760.00 USD | 0.00 USD | 20,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,830,000.00 USD | 4,830,000.00 USD | 330,140.00 USD | 0.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.00` | 831,930.00 USD | 831,930.00 USD | 408,710.00 USD | 0.00 USD | 40,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 547,190.00 USD | 0.00 USD | 101,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.20` | 1,130,000.00 USD | 1,130,000.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.40` | 1,430,000.00 USD | 1,430,000.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,620,000.00 USD | 1,620,000.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.80` | 1,910,000.00 USD | 1,910,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.00` | 1,990,000.00 USD | 1,990,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.20` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.40` | 2,160,000.00 USD | 2,160,000.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 2,260,000.00 USD | 2,260,000.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 2,310,000.00 USD | 2,310,000.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.00` | 2,360,000.00 USD | 2,360,000.00 USD | 48,740.00 USD | 0.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4152.20` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.20` | 2,370,000.00 USD | 2,370,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.40` | 2,450,000.00 USD | 2,450,000.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.60` | 2,540,000.00 USD | 2,540,000.00 USD | 85,450.00 USD | 0.00 USD | 9,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,540,000.00 USD | 12,540,000.00 USD | 133,800.00 USD | 0.00 USD | 24,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.80` | 2,700,000.00 USD | 2,700,000.00 USD | 142,450.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 270,030.00 USD | 0.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.00` | 2,880,000.00 USD | 2,880,000.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.20` | 3,060,000.00 USD | 3,060,000.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.40` | 3,120,000.00 USD | 3,120,000.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.60` | 3,280,000.00 USD | 3,280,000.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.80` | 3,340,000.00 USD | 3,340,000.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4211.00` | 3,360,000.00 USD | 3,360,000.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4215.20` | 3,420,000.00 USD | 3,420,000.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.40` | 3,470,000.00 USD | 3,470,000.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.60` | 3,510,000.00 USD | 3,510,000.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.80` | 3,540,000.00 USD | 3,540,000.00 USD | 28,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4232.00` | 3,540,000.00 USD | 3,540,000.00 USD | 1,060.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.80` | 3,560,000.00 USD | 3,560,000.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.00` | 3,580,000.00 USD | 3,580,000.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4425.20` | 3,620,000.00 USD | 3,620,000.00 USD | 32,100.00 USD | 0.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 40,010.00 USD | 0.00 USD | 11,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4429.40` | 3,680,000.00 USD | 3,680,000.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.60` | 3,720,000.00 USD | 3,720,000.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4437.80` | 3,750,000.00 USD | 3,750,000.00 USD | 24,810.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.40` | 3,760,000.00 USD | 3,760,000.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,540,000.00 USD | 16,540,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `1D` | `3618.80` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 31,030.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `3619.70` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 12,060.00 USD |
| `1D` | `3623.00` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 67,500.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3623.90` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.20` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `3628.10` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.40` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3632.30` | 15,730,000.00 USD | 0.00 USD | 15,730,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.60` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.80` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD |
| `7D` | `3640.70` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3644.00` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3648.20` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `3649.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3652.40` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD |
| `7D` | `3653.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3656.60` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `3660.80` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 4,080.00 USD | 0.00 USD | 812.11 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3665.00` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 396.25 USD |
| `7D` | `3665.90` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3854.00` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `3854.90` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3858.20` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3862.40` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 129,370.00 USD | 0.00 USD | 13,730.00 USD |
| `7D` | `3863.30` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 204,080.00 USD | 0.00 USD | 53,800.00 USD |
| `1D` | `3866.60` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 193,320.00 USD | 0.00 USD | 25,080.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3870.80` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3875.00` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3879.20` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD |
| `7D` | `3880.10` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3883.40` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD |
| `7D` | `3884.30` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3887.60` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD |
| `7D` | `3888.50` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3891.80` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3892.70` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3896.00` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3900.20` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3901.10` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3904.40` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 24,370.00 USD | 0.00 USD | 1,200.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `3908.60` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3933.80` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.00` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `3938.90` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.20` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 250,380.00 USD | 0.00 USD | 24,730.00 USD |
| `7D` | `3943.10` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 417,530.00 USD | 0.00 USD | 73,100.00 USD |
| `1D` | `3946.40` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 360,890.00 USD | 0.00 USD | 45,790.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD |
| `1D` | `3950.60` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.80` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.00` | 856,730.00 USD | 0.00 USD | 856,730.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.20` | 568,300.00 USD | 0.00 USD | 568,300.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.40` | 409,520.00 USD | 0.00 USD | 409,520.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.60` | 359,430.00 USD | 0.00 USD | 359,430.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.80` | 264,840.00 USD | 0.00 USD | 264,840.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3980.00` | 131,870.00 USD | 0.00 USD | 131,870.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3984.20` | 64,460.00 USD | 0.00 USD | 64,460.00 USD | 56,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `1D` | `3988.40` | 8,150.00 USD | 0.00 USD | 8,150.00 USD | 2,110.00 USD | 0.00 USD | 6,040.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4019.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4019.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 0.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4101.80` | 382,460.00 USD | 382,460.00 USD | 0.00 USD | 178,760.00 USD | 0.00 USD | 20,380.00 USD |
| `7D` | `4102.70` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 69,830.00 USD |
| `1D` | `4106.00` | 831,930.00 USD | 831,930.00 USD | 0.00 USD | 408,710.00 USD | 0.00 USD | 40,760.00 USD |
| `7D` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 547,190.00 USD | 0.00 USD | 101,580.00 USD |
| `1D` | `4110.20` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.40` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD |
| `7D` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD |
| `7D` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.80` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.20` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.40` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.60` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.80` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4148.00` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 48,740.00 USD | 0.00 USD | 1,210.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `1D` | `4152.20` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `1D` | `4173.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4177.40` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4181.60` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 85,450.00 USD | 0.00 USD | 9,390.00 USD |
| `7D` | `4182.50` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 24,870.00 USD |
| `1D` | `4185.80` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 14,290.00 USD |
| `7D` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 270,030.00 USD | 0.00 USD | 54,580.00 USD |
| `1D` | `4190.00` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD |
| `7D` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4194.20` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4198.40` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD |
| `7D` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4202.60` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD |
| `7D` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4206.80` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4211.00` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4215.20` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD |
| `7D` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4219.40` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD |
| `7D` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4223.60` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4227.80` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 28,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4232.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4416.80` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4421.00` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4425.20` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 32,100.00 USD | 0.00 USD | 3,670.00 USD |
| `7D` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 11,470.00 USD |
| `1D` | `4429.40` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.60` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `4437.80` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 24,810.00 USD | 0.00 USD | 5,770.00 USD |
| `1D` | `4438.40` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `274.67M` | Total OI Tokens: `68,311.9 PAXG`
  * 1h OI Change: `-0.10%` | 4h OI Change: `-0.19%` | 24h OI Change: `+0.12%`
  * Exchange Breakdown: Binance=`107.13M` | Bybit=`19.92M` | OKX=`-` | Hyperliquid=`24.64M`
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
| `15M` | `PAXG` | `51.44%` | `48.56%` | `1.06` | 949,020.00 USD |
| `15M` | `Binance` | `45.12%` | `54.88%` | `0.82` | 509,620.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `45.34%` | `54.66%` | `0.83` | 42,960.00 USD |
| `15M` | `KuCoin` | `47.99%` | `52.01%` | `0.92` | 118,130.00 USD |
| `15M` | `Gate` | `63.6%` | `36.4%` | `1.75` | 30,960.00 USD |
| `15M` | `Bitget` | `55.12%` | `44.88%` | `1.23` | 129,350.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `86.67%` | `13.33%` | `6.50` | 8,560.00 USD |
| `15M` | `Bitunix` | `62.45%` | `37.55%` | `1.66` | 13,290.00 USD |
| `15M` | `Hyperliquid` | `79.91%` | `20.09%` | `3.98` | 12,590.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `93.53%` | `6.47%` | `14.46` | 63,540.00 USD |
| `15M` | `HTX` | `94.57%` | `5.43%` | `17.42` | 6,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `2.81%` | `97.19%` | `0.03` | 2,150.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 474.83 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 11,320.00 USD |
| `15M` | `Whale Positions` | `45.12%` | `54.88%` | `0.82` | 509,620.00 USD |
| `15M` | `Global Accounts` | `51.44%` | `48.56%` | `1.06` | 949,020.00 USD |
| `1H` | `PAXG` | `29.97%` | `70.03%` | `0.43` | 21,000,000.00 USD |
| `1H` | `Binance` | `46.65%` | `53.35%` | `0.87` | 2,220,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `49.14%` | `50.86%` | `0.97` | 1,710,000.00 USD |
| `1H` | `KuCoin` | `15.54%` | `84.46%` | `0.18` | 141,690.00 USD |
| `1H` | `Gate` | `36.29%` | `63.71%` | `0.57` | 783,170.00 USD |
| `1H` | `Bitget` | `53.27%` | `46.73%` | `1.14` | 367,610.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `18.56%` | `81.44%` | `0.23` | 12,430,000.00 USD |
| `1H` | `Bitunix` | `39.77%` | `60.23%` | `0.66` | 1,480,000.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `61.94%` | `38.06%` | `1.63` | 1,620,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `3.65%` | `96.35%` | `0.04` | 228,570.00 USD |
| `1H` | `HTX` | `29.66%` | `70.34%` | `0.42` | 4,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `56.64%` | `43.36%` | `1.31` | 13,540.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `46.65%` | `53.35%` | `0.87` | 2,220,000.00 USD |
| `1H` | `Global Accounts` | `29.97%` | `70.03%` | `0.43` | 21,000,000.00 USD |
| `4H` | `PAXG` | `49.10%` | `50.90%` | `0.96` | 19,650,000.00 USD |
| `4H` | `Binance` | `48.95%` | `51.05%` | `0.96` | 10,950,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.41%` | `45.59%` | `1.19` | 569,660.00 USD |
| `4H` | `KuCoin` | `53.33%` | `46.67%` | `1.14` | 1,360,000.00 USD |
| `4H` | `Gate` | `65.62%` | `34.38%` | `1.91` | 299,180.00 USD |
| `4H` | `Bitget` | `53.3%` | `46.7%` | `1.14` | 1,870,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `11.14%` | `88.86%` | `0.13` | 596,920.00 USD |
| `4H` | `Bitunix` | `39.93%` | `60.07%` | `0.66` | 379,250.00 USD |
| `4H` | `Hyperliquid` | `35.23%` | `64.77%` | `0.54` | 2,040,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `75.53%` | `24.47%` | `3.09` | 1,380,000.00 USD |
| `4H` | `HTX` | `63.3%` | `36.7%` | `1.72` | 59,700.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `32.89%` | `67.11%` | `0.49` | 39,150.00 USD |
| `4H` | `Aster` | `40.01%` | `59.99%` | `0.67` | 21,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `25.16%` | `74.84%` | `0.34` | 83,270.00 USD |
| `4H` | `Whale Positions` | `48.95%` | `51.05%` | `0.96` | 10,950,000.00 USD |
| `4H` | `Global Accounts` | `49.10%` | `50.90%` | `0.96` | 19,650,000.00 USD |


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
| `5m` | -93,080.00 USD | -77,580.00 USD | **`DISTRIBUTION`** |
| `15m` | -109,320.00 USD | -62,840.00 USD | **`DISTRIBUTION`** |
| `30m` | -301,100.00 USD | -20,200.00 USD | **`DISTRIBUTION`** |
| `1h` | -253,420.00 USD | -490,080.00 USD | **`DISTRIBUTION`** |
| `2h` | -47,500.00 USD | -201,570.00 USD | **`DISTRIBUTION`** |
| `4h` | -705,510.00 USD | -185,570.00 USD | **`DISTRIBUTION`** |
| `6h` | 134,780.00 USD | 807,560.00 USD | **`ACCUMULATION`** |
| `8h` | -152,170.00 USD | 872,350.00 USD | **`ACCUMULATION`** |
| `12h` | -477,410.00 USD | 1,270,000.00 USD | **`ACCUMULATION`** |
| `24h` | -27,680.00 USD | 1,510,000.00 USD | **`ACCUMULATION`** |
| `1w` | -8,300,000.00 USD | -8,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,970,000.00 USD | -71,410,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-93.08K` | 15m=`-109.32K` | 1h=`-253.42K` | 24h=`-27.68K`
* Futures Capital Netflows: 5m=`-77.58K` | 15m=`-62.84K` | 1h=`-490.08K` | 24h=`+1.51M`
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
  * `2026-10-30 02:53:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:14:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:00:46 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
