# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 04:16:49 IST` (`2026-10-29 22:46:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4021.17` | **Live Ask Quote**: `4021.25` | **Mid Price**: `4021.21`
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
  * Session VWAP: `4029.44` | VWAP Z-Score: `-0.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.66` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.38` | Lower -3.00σ Band: `3994.50`
  * Upper +2.51σ Band: `4058.67` | Lower -2.51σ Band: `4000.21`
  * Upper +2.01σ Band: `4052.85` | Lower -2.01σ Band: `4006.03`
  * Upper +2.00σ Band: `4052.73` | Lower -2.00σ Band: `4006.15`
  * Upper +1.28σ Band: `4044.35` | Lower -1.28σ Band: `4014.53`
  * Upper +1.00σ Band: `4041.09` | Lower -1.00σ Band: `4017.80`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4020.35` | EMA-20=`4019.52` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4022.78` (Slope: `+0.0000`) | EMA-100=`4028.62`
  * Institutional Anchors: EMA-144=`4030.61` | EMA-200=`4031.03` (Slope: `-0.0353`) | EMA-233=`4030.62`
- **Range Boundaries**: 24H High=`4070.97` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4023.03` (Distance: `-0.04%`)
  * Point of Control (POC) = `4020.98` (Distance: `+0.01%`)
  * Value Area Low (VAL) = `4017.81` (Distance: `+0.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4017.62`
  * London Session (08:00-16:00 UTC): High=`4037.29` | Low=`4005.13`
  * New York Session (13:00-21:00 UTC): High=`4045.34` | Low=`3997.08`
  * Initial Balance (First Hour): IB High=`4033.27` | IB Low=`4009.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4005.13` - `4037.29`
  * Optimal Trade Entry (OTE 0.705): `4029.25`
  * Structural Invalidation Anchor (0.786): `4053.38`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4022.02` | `4022.21` | `4021.27` | `4021.48` | `25` | 101,856.61 USD | -26,164.81 USD | `-25.69%` | 2,154,553.93 USD | `-0.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4021.48` | `4021.67` | `4020.87` | `4021.49` | `24` | 98,459.99 USD | -5,125.15 USD | `-5.21%` | 2,149,428.78 USD | `-0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4021.48` | `4024.45` | `4021.28` | `4024.45` | `19` | 78,423.42 USD | 19,975.63 USD | `+25.47%` | 2,169,404.41 USD | `+0.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4018.12` | `4025.28` | `4017.72` | `4022.63` | `250` | 1,005,666.39 USD | 151,466.76 USD | `+15.06%` | 2,074,960.21 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4022.62` | `4023.57` | `4020.87` | `4021.49` | `82` | 330,859.14 USD | 37,421.84 USD | `+11.31%` | 2,112,382.04 USD | `+0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4021.48` | `4024.45` | `4021.28` | `4024.45` | `19` | 78,423.42 USD | 19,975.63 USD | `+25.47%` | 2,132,357.68 USD | `+0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,839,422.95 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,963,502.96 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4025.28` | `4017.72` | `4024.45` | `352` | 1,414,948.95 USD | 208,864.23 USD | `+14.76%` | 2,172,367.19 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4024.45` | `2,004` | 8,062,376.66 USD | 93,814.40 USD | `+1.16%` | 1,340,961.73 USD | `-0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4024.45` | `2,004` | 8,062,376.66 USD | 93,814.40 USD | `+1.16%` | 1,340,961.73 USD | `-0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4021.30` | `13.5174` | 54,357.52 USD | 934,145.01 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `4021.40` | `6.1517` | 24,738.45 USD | 879,787.49 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4021.50` | `9.9395` | 39,971.70 USD | 855,049.04 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4021.60` | `9.5497` | 38,405.07 USD | 815,077.34 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4021.70` | `30.0837` | 120,987.62 USD | 776,672.27 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4021.80` | `7.1943` | 28,934.04 USD | 655,684.65 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4021.90` | `14.2343` | 57,248.93 USD | 626,750.62 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4022.00` | `1.8443` | 7,417.77 USD | 569,501.68 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4022.20` | `17.6495` | 70,989.82 USD | 562,083.91 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4022.30` | `2.7335` | 10,994.96 USD | 491,094.09 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4022.40` | `6.1515` | 24,743.79 USD | 480,099.13 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4022.50` | `28.3760` | 114,142.46 USD | 455,355.34 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4022.60` | `5.8945` | 23,711.22 USD | 341,212.88 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `4022.70` | `15.6659` | 63,019.22 USD | 317,501.66 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4022.80` | `4.6609` | 18,749.87 USD | 254,482.45 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4022.90` | `1.3906` | 5,594.24 USD | 235,732.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4023.10` | `15.5761` | 62,664.21 USD | 230,138.34 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4023.30` | `13.6860` | 55,062.88 USD | 167,474.13 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4023.40` | `1.1587` | 4,661.91 USD | 112,411.24 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4023.50` | `26.7800` | 107,749.33 USD | 107,749.33 USD | `7 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4023.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,023.55` | `0.00%` | `-` |
| `ASK` | `4023.60` | `121.0566` | 487,083.34 USD | 487,083.34 USD | `24 orders` | `+0.00%` | `-` |
| `ASK` | `4023.70` | `7.7667` | 31,250.87 USD | 518,334.21 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4023.80` | `7.4556` | 29,999.84 USD | 548,334.05 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4023.90` | `5.7936` | 23,312.87 USD | 571,646.92 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4024.00` | `18.2650` | 73,498.36 USD | 645,145.28 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4024.10` | `74.5524` | 300,006.31 USD | 945,151.59 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4024.20` | `7.5879` | 30,535.23 USD | 975,686.82 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4024.30` | `3.7769` | 15,199.38 USD | 990,886.20 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4024.40` | `13.3830` | 53,858.55 USD | 1,044,744.74 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `4024.50` | `1.0422` | 4,194.33 USD | 1,048,939.07 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4024.60` | `0.0546` | 219.74 USD | 1,049,158.82 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4024.70` | `16.8885` | 67,971.15 USD | 1,117,129.96 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4024.80` | `7.9491` | 31,993.54 USD | 1,149,123.50 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4024.90` | `51.2863` | 206,422.23 USD | 1,355,545.73 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4025.00` | `6.2214` | 25,041.13 USD | 1,380,586.87 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4025.10` | `25.9773` | 104,561.23 USD | 1,485,148.10 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4025.20` | `10.2468` | 41,245.42 USD | 1,526,393.51 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4025.30` | `4.8463` | 19,507.81 USD | 1,545,901.33 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4025.50` | `24.1636` | 97,270.57 USD | 1,643,171.90 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `4025.70` | `3.9124` | 15,750.15 USD | 1,658,922.05 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x5b5d...c060` | `SHORT` | 25,606,026.19 USD | `6,365.38` | `4188.90` | `4023.70` | `32569.20` | 1,057,945.10 USD | `+4.13%` | `4X Cross` |
| `53` | `0x4692...164f` | `SHORT` | 25,457,305.84 USD | `6,327.94` | `4132.72` | `4023.70` | `13741.14` | 694,364.02 USD | `+2.73%` | `5X Cross` |
| `67` | `0xb83d...6e36` | `SHORT` | 23,612,257.33 USD | `5,869.90` | `4228.86` | `4023.70` | `30326.32` | 1,210,764.61 USD | `+5.13%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,424,760.90 USD | `4,828.91` | `4157.43` | `4023.70` | `2227.53` | -651,121.42 USD | `-3.35%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,215,292.63 USD | `3,533.51` | `4129.10` | `4023.70` | `427.46` | -374,933.82 USD | `-2.64%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,147,041.24 USD | `3,268.21` | `4228.94` | `4023.70` | `4397.09` | 674,037.89 USD | `+5.13%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,665,830.40 USD | `2,900.00` | `4364.92` | `4023.70` | `4235.67` | 992,445.93 USD | `+8.51%` | `20X Cross` |
| `264` | `0xfc66...ca06` | `SHORT` | 8,901,663.83 USD | `2,212.91` | `4031.28` | `4023.70` | `11113.51` | 19,223.55 USD | `+0.22%` | `3X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,851,040.00 USD | `2,200.00` | `4176.09` | `4023.70` | `2643.84` | -336,379.30 USD | `-3.80%` | `25X Cross` |
| `266` | `0x41e5...0825` | `SHORT` | 8,845,980.00 USD | `2,200.00` | `4112.20` | `4023.70` | `4331.15` | 200,874.59 USD | `+2.27%` | `20X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,942,761.61 USD | `1,975.37` | `4048.55` | `4023.70` | `6501.27` | 54,630.10 USD | `+0.69%` | `6X Cross` |
| `370` | `0xc26c...b8f4` | `LONG` | 6,355,672.11 USD | `1,579.95` | `4075.62` | `4023.70` | `0.000000` | -83,624.86 USD | `-1.32%` | `1X Cross` |
| `403` | `0x12d2...f97f` | `LONG` | 5,637,071.80 USD | `1,401.94` | `4278.91` | `4023.70` | `3086.97` | -361,718.78 USD | `-6.42%` | `20X Cross` |
| `551` | `0x63da...8add` | `LONG` | 4,022,700.00 USD | `1,000.00` | `4021.46` | `4023.70` | `3564.11` | 1,239.04 USD | `+0.03%` | `25X Cross` |
| `571` | `0x354b...6425` | `LONG` | 3,950,432.32 USD | `981.96` | `4031.85` | `4023.70` | `0.000000` | -8,694.67 USD | `-0.22%` | `10X Cross` |
| `577` | `0x9aa5...58af` | `LONG` | 3,908,915.77 USD | `971.64` | `4279.98` | `4023.70` | `0.000000` | -249,693.32 USD | `-6.39%` | `20X Cross` |
| `606` | `0xf3dc...1672` | `LONG` | 3,744,568.05 USD | `930.74` | `4024.62` | `4023.70` | `3337.59` | -1,324.51 USD | `-0.04%` | `20X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,369,026.47 USD | `837.40` | `4599.73` | `4023.70` | `0.000000` | -482,793.91 USD | `-14.33%` | `20X Cross` |
| `820` | `0x0fac...7a0a` | `LONG` | 2,761,729.15 USD | `686.49` | `4290.34` | `4023.70` | `1447.16` | -183,529.55 USD | `-6.65%` | `25X Cross` |
| `871` | `0xd8c5...99b0` | `SHORT` | 2,584,322.23 USD | `642.35` | `4175.35` | `4023.70` | `32842.43` | 97,738.94 USD | `+3.78%` | `4X Cross` |
| `898` | `0x625e...a354` | `SHORT` | 2,492,958.00 USD | `620.00` | `4122.81` | `4023.70` | `4342.25` | 63,189.03 USD | `+2.53%` | `20X Cross` |
| `929` | `0xeae3...e8ad` | `SHORT` | 2,413,680.00 USD | `600.00` | `4104.77` | `4023.70` | `4325.27` | 49,185.11 USD | `+2.04%` | `20X Cross` |
| `932` | `0xf285...fa82` | `LONG` | 2,404,924.01 USD | `598.11` | `4146.45` | `4023.70` | `3891.24` | -75,095.54 USD | `-3.12%` | `25X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,355,736.16 USD | `585.61` | `4082.77` | `4023.70` | `2514.21` | -35,180.82 USD | `-1.49%` | `10X Cross` |
| `1095` | `0x413c...886c` | `LONG` | 2,011,300.00 USD | `500.00` | `4010.43` | `4023.70` | `0.000000` | 6,083.77 USD | `+0.30%` | `2X Cross` |
| `1101` | `0x61ce...a62b` | `SHORT` | 2,001,008.83 USD | `497.50` | `4071.66` | `4023.70` | `4711.06` | 24,659.96 USD | `+1.23%` | `20X Cross` |
| `1106` | `0x0593...40f9` | `LONG` | 1,996,020.84 USD | `496.18` | `4024.57` | `4023.70` | `3701.73` | -882.99 USD | `-0.04%` | `10X Isolated` |
| `1180` | `0x2edd...8179` | `LONG` | 1,895,236.46 USD | `470.91` | `4164.68` | `4026.90` | `0.000000` | -65,964.85 USD | `-3.48%` | `10X Cross` |
| `1225` | `0xead5...69f2` | `LONG` | 1,824,619.68 USD | `453.78` | `4220.88` | `4023.70` | `3538.94` | -90,748.38 USD | `-4.97%` | `5X Isolated` |
| `1294` | `0x7a6d...f79c` | `SHORT` | 1,724,182.64 USD | `428.38` | `4136.09` | `4026.90` | `5749.43` | 47,632.37 USD | `+2.76%` | `10X Cross` |
| `1314` | `0x46fc...1195` | `LONG` | 1,675,227.49 USD | `416.39` | `4054.56` | `4023.70` | `2156.15` | -13,058.49 USD | `-0.78%` | `20X Cross` |
| `1379` | `0xee02...309d` | `SHORT` | 1,609,080.00 USD | `400.00` | `4438.84` | `4023.70` | `4226.89` | 166,458.60 USD | `+10.34%` | `25X Isolated` |
| `1380` | `0x6d15...d374` | `LONG` | 1,608,360.00 USD | `400.00` | `4068.25` | `4023.70` | `3841.81` | -18,940.00 USD | `-1.18%` | `25X Cross` |
| `1412` | `0x02a7...fe9f` | `SHORT` | 1,568,853.00 USD | `390.00` | `4055.02` | `4023.70` | `4306.71` | 12,606.25 USD | `+0.80%` | `25X Cross` |
| `1445` | `0x51f6...2b39` | `LONG` | 1,537,100.42 USD | `381.76` | `4233.94` | `4026.90` | `0.000000` | -79,271.22 USD | `-5.16%` | `10X Cross` |
| `1451` | `0x7e77...b8d2` | `SHORT` | 1,528,816.00 USD | `380.00` | `4131.92` | `4023.70` | `4293.51` | 41,313.64 USD | `+2.70%` | `20X Cross` |
| `1469` | `0x72c2...9b37` | `LONG` | 1,500,771.40 USD | `373.13` | `4000.98` | `4023.70` | `3778.05` | 7,877.89 USD | `+0.52%` | `13X Isolated` |
| `1508` | `0x781e...96b7` | `SHORT` | 1,447,873.86 USD | `359.61` | `4364.97` | `4026.90` | `13487.78` | 121,827.06 USD | `+8.41%` | `10X Cross` |
| `1509` | `0xaa44...b844` | `LONG` | 1,447,776.00 USD | `360.00` | `4043.10` | `4023.70` | `2803.27` | -7,741.63 USD | `-0.53%` | `4X Cross` |
| `1629` | `0xa41f...d50a` | `LONG` | 1,322,756.60 USD | `328.96` | `4468.89` | `4023.70` | `3833.19` | -147,341.25 USD | `-11.14%` | `15X Cross` |
| `1664` | `0xbf5a...88ba` | `SHORT` | 1,277,893.90 USD | `317.65` | `4091.80` | `4023.70` | `9924.55` | 21,889.14 USD | `+1.71%` | `20X Cross` |
| `1699` | `0xff31...ff6c` | `SHORT` | 1,247,037.00 USD | `310.00` | `4372.43` | `4023.70` | `4789.18` | 108,418.38 USD | `+8.69%` | `10X Isolated` |
| `1713` | `0xada6...6f88` | `LONG` | 1,239,210.22 USD | `308.10` | `4166.46` | `4023.70` | `1909.75` | -44,478.80 USD | `-3.59%` | `5X Cross` |
| `1878` | `0x50e2...d770` | `LONG` | 1,087,742.12 USD | `270.37` | `4243.58` | `4023.70` | `2562.10` | -59,584.34 USD | `-5.48%` | `20X Cross` |
| `1893` | `0x4c92...4f17` | `SHORT` | 1,072,936.56 USD | `266.72` | `4260.98` | `4023.70` | `6517.76` | 63,555.68 USD | `+5.92%` | `20X Cross` |
| `1953` | `0xd346...c4f3` | `LONG` | 1,026,538.68 USD | `255.17` | `4188.66` | `4023.70` | `3310.43` | -42,297.83 USD | `-4.12%` | `5X Isolated` |
| `2000` | `0x1581...463b` | `LONG` | 1,005,225.00 USD | `250.00` | `4003.77` | `4023.70` | `3554.23` | 4,281.41 USD | `+0.43%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.85` (Vol: 274,500.00 USD, Dist: `+2.19%`) | Long MP=`3937.39` (Vol: 356,200.00 USD, Dist: `--2.10%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.89%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.11%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.87%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.10%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.22%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.46%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,280,000.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.00` | 3,910,000.00 USD | 3,910,000.00 USD | 37,670.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,060,000.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.10` | 3,860,000.00 USD | 3,860,000.00 USD | 67,080.00 USD | 0.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 16,000,000.00 USD | 16,000,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 3,790,000.00 USD | 3,790,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,900,000.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.30` | 3,740,000.00 USD | 3,740,000.00 USD | 31,790.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,720,000.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.40` | 3,710,000.00 USD | 3,710,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,610,000.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.50` | 3,670,000.00 USD | 3,670,000.00 USD | 26,220.00 USD | 0.00 USD | 9,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,470,000.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.60` | 3,640,000.00 USD | 3,640,000.00 USD | 6,610.00 USD | 0.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.70` | 3,630,000.00 USD | 3,630,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,370,000.00 USD | 15,370,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.80` | 3,610,000.00 USD | 3,610,000.00 USD | 18,510.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,350,000.00 USD | 15,350,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.90` | 3,590,000.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,320,000.00 USD | 15,320,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,290,000.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,260,000.00 USD | 15,260,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,250,000.00 USD | 15,250,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,890,000.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,400,000.00 USD | 14,400,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,870,000.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.70` | 3,580,000.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,540,000.00 USD | 13,540,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.80` | 3,580,000.00 USD | 3,580,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,240,000.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.90` | 3,490,000.00 USD | 3,490,000.00 USD | 127,460.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,950,000.00 USD | 12,950,000.00 USD | 183,740.00 USD | 0.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.00` | 3,340,000.00 USD | 3,340,000.00 USD | 220,650.00 USD | 0.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,700,000.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.10` | 3,090,000.00 USD | 3,090,000.00 USD | 142,720.00 USD | 0.00 USD | 20,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,160,000.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.20` | 2,930,000.00 USD | 2,930,000.00 USD | 121,170.00 USD | 0.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,740,000.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.30` | 2,790,000.00 USD | 2,790,000.00 USD | 110,120.00 USD | 0.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,190,000.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.40` | 2,680,000.00 USD | 2,680,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,850,000.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.50` | 2,570,000.00 USD | 2,570,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,710,000.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.60` | 2,530,000.00 USD | 2,530,000.00 USD | 26,200.00 USD | 0.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,600,000.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.70` | 2,500,000.00 USD | 2,500,000.00 USD | 73,860.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,480,000.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.80` | 2,420,000.00 USD | 2,420,000.00 USD | 11,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,360,000.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.90` | 2,410,000.00 USD | 2,410,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,280,000.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,180,000.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,160,000.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,430,000.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,490,000.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,600,000.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.70` | 2,390,000.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,760,000.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.80` | 2,320,000.00 USD | 2,320,000.00 USD | 177,090.00 USD | 0.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,290,000.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.90` | 2,140,000.00 USD | 2,140,000.00 USD | 305,210.00 USD | 0.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,630,000.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.00` | 1,780,000.00 USD | 1,780,000.00 USD | 384,760.00 USD | 0.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 123,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.10` | 1,340,000.00 USD | 1,340,000.00 USD | 315,900.00 USD | 0.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.20` | 986,410.00 USD | 986,410.00 USD | 175,480.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.30` | 781,470.00 USD | 781,470.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.40` | 491,350.00 USD | 491,350.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.50` | 335,720.00 USD | 335,720.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.60` | 285,640.00 USD | 285,640.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.70` | 191,040.00 USD | 191,040.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.80` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.90` | 19,950.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.60` | 65,020.00 USD | 65,020.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.70` | 208,440.00 USD | 208,440.00 USD | 132,300.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.80` | 512,670.00 USD | 512,670.00 USD | 255,730.00 USD | 0.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.90` | 990,060.00 USD | 990,060.00 USD | 428,840.00 USD | 0.00 USD | 48,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 506,510.00 USD | 0.00 USD | 106,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.00` | 1,320,000.00 USD | 1,320,000.00 USD | 288,670.00 USD | 0.00 USD | 38,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.10` | 1,570,000.00 USD | 1,570,000.00 USD | 219,460.00 USD | 0.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.20` | 1,760,000.00 USD | 1,760,000.00 USD | 185,530.00 USD | 0.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.30` | 2,010,000.00 USD | 2,010,000.00 USD | 207,400.00 USD | 0.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.40` | 2,100,000.00 USD | 2,100,000.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.50` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.60` | 2,260,000.00 USD | 2,260,000.00 USD | 140,390.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.70` | 2,360,000.00 USD | 2,360,000.00 USD | 83,630.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.90` | 2,390,000.00 USD | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.60` | 2,460,000.00 USD | 2,460,000.00 USD | 65,340.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.70` | 2,540,000.00 USD | 2,540,000.00 USD | 78,220.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.80` | 2,710,000.00 USD | 2,710,000.00 USD | 139,770.00 USD | 0.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 249,690.00 USD | 0.00 USD | 62,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.90` | 2,930,000.00 USD | 2,930,000.00 USD | 188,760.00 USD | 0.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,470,000.00 USD | 13,470,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.00` | 3,090,000.00 USD | 3,090,000.00 USD | 147,340.00 USD | 0.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,790,000.00 USD | 13,790,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.10` | 3,190,000.00 USD | 3,190,000.00 USD | 87,740.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,230,000.00 USD | 14,230,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.20` | 3,330,000.00 USD | 3,330,000.00 USD | 132,280.00 USD | 0.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,570,000.00 USD | 14,570,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.30` | 3,410,000.00 USD | 3,410,000.00 USD | 55,400.00 USD | 0.00 USD | 23,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.40` | 3,440,000.00 USD | 3,440,000.00 USD | 22,630.00 USD | 0.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.50` | 3,470,000.00 USD | 3,470,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,930,000.00 USD | 14,930,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.60` | 3,540,000.00 USD | 3,540,000.00 USD | 69,580.00 USD | 0.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.70` | 3,570,000.00 USD | 3,570,000.00 USD | 21,900.00 USD | 0.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,140,000.00 USD | 15,140,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.80` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.90` | 3,580,000.00 USD | 3,580,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,600,000.00 USD | 15,600,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,800,000.00 USD | 15,800,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.40` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,930,000.00 USD | 15,930,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.50` | 3,620,000.00 USD | 3,620,000.00 USD | 28,900.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.60` | 3,640,000.00 USD | 3,640,000.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.70` | 3,680,000.00 USD | 3,680,000.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.80` | 3,750,000.00 USD | 3,750,000.00 USD | 59,900.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.30` | 3,760,000.00 USD | 3,760,000.00 USD | 6,460.00 USD | 0.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,530,000.00 USD | 16,530,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
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
| `1D` | `3619.00` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 37,670.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3619.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3623.10` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 67,080.00 USD | 0.00 USD | 10,850.00 USD |
| `7D` | `3623.90` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.20` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `3628.10` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.30` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 31,790.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3632.30` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.40` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.50` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 26,220.00 USD | 0.00 USD | 9,750.00 USD |
| `7D` | `3640.70` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.60` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 6,610.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3649.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.80` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 18,510.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `3653.30` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.90` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.70` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `3854.90` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.80` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3860.90` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 127,460.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3863.30` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 183,740.00 USD | 0.00 USD | 71,710.00 USD |
| `1D` | `3865.00` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 220,650.00 USD | 0.00 USD | 25,260.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3869.10` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 142,720.00 USD | 0.00 USD | 20,100.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3873.20` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 121,170.00 USD | 0.00 USD | 17,270.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3877.30` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 110,120.00 USD | 0.00 USD | 4,940.00 USD |
| `7D` | `3880.10` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3881.40` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `3884.30` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3885.50` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `3888.50` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.60` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 26,200.00 USD | 0.00 USD | 8,930.00 USD |
| `7D` | `3892.70` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.70` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 73,860.00 USD | 0.00 USD | 5,450.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.80` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 11,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3901.10` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.90` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.70` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.80` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 177,090.00 USD | 0.00 USD | 7,390.00 USD |
| `7D` | `3938.90` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.90` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 305,210.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `3943.10` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD |
| `1D` | `3947.00` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 384,760.00 USD | 0.00 USD | 53,660.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 123,890.00 USD |
| `1D` | `3951.10` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 315,900.00 USD | 0.00 USD | 36,980.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3955.20` | 986,410.00 USD | 0.00 USD | 986,410.00 USD | 175,480.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.30` | 781,470.00 USD | 0.00 USD | 781,470.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.40` | 491,350.00 USD | 0.00 USD | 491,350.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.50` | 335,720.00 USD | 0.00 USD | 335,720.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.60` | 285,640.00 USD | 0.00 USD | 285,640.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.70` | 191,040.00 USD | 0.00 USD | 191,040.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.80` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.90` | 19,950.00 USD | 0.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4025.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4025.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4094.60` | 65,020.00 USD | 65,020.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4098.70` | 208,440.00 USD | 208,440.00 USD | 0.00 USD | 132,300.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD |
| `1D` | `4102.80` | 512,670.00 USD | 512,670.00 USD | 0.00 USD | 255,730.00 USD | 0.00 USD | 48,490.00 USD |
| `1D` | `4106.90` | 990,060.00 USD | 990,060.00 USD | 0.00 USD | 428,840.00 USD | 0.00 USD | 48,550.00 USD |
| `7D` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 106,200.00 USD |
| `1D` | `4111.00` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 288,670.00 USD | 0.00 USD | 38,310.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4115.10` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 219,460.00 USD | 0.00 USD | 32,410.00 USD |
| `7D` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4119.20` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 185,530.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4123.30` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 207,400.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.40` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD |
| `7D` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.50` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.60` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 140,390.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.70` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 83,630.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.80` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.90` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.60` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 65,340.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.70` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 78,220.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD |
| `1D` | `4184.80` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 139,770.00 USD | 0.00 USD | 25,770.00 USD |
| `7D` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 62,050.00 USD |
| `1D` | `4188.90` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 188,760.00 USD | 0.00 USD | 26,280.00 USD |
| `7D` | `4190.90` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4193.00` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 147,340.00 USD | 0.00 USD | 18,220.00 USD |
| `7D` | `4195.10` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4197.10` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 87,740.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4199.30` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4201.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 132,280.00 USD | 0.00 USD | 5,890.00 USD |
| `7D` | `4203.50` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4205.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 55,400.00 USD | 0.00 USD | 23,230.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4209.40` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 8,560.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4213.50` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `4216.10` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.60` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 69,580.00 USD | 0.00 USD | 4,860.00 USD |
| `7D` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.70` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 21,900.00 USD | 0.00 USD | 2,050.00 USD |
| `7D` | `4224.50` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.80` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.90` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4414.40` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `4417.70` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4418.50` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.60` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4426.70` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4430.80` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 59,900.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4432.30` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 6,460.00 USD | 0.00 USD | 1,710.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.85M` | Total OI Tokens: `68,253.9 PAXG`
  * 1h OI Change: `+0.03%` | 4h OI Change: `+0.26%` | 24h OI Change: `+0.11%`
  * Exchange Breakdown: Binance=`107.38M` | Bybit=`20.08M` | OKX=`-` | Hyperliquid=`24.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.37K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
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
| `15M` | `PAXG` | `53.02%` | `46.98%` | `1.13` | 1,020,000.00 USD |
| `15M` | `Binance` | `65.09%` | `34.91%` | `1.86` | 241,340.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `50.49%` | `49.51%` | `1.02` | 147,590.00 USD |
| `15M` | `KuCoin` | `95.05%` | `4.95%` | `19.20` | 5,190.00 USD |
| `15M` | `Gate` | `44.35%` | `55.65%` | `0.80` | 138,720.00 USD |
| `15M` | `Bitget` | `48.18%` | `51.82%` | `0.93` | 53,010.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `51.79%` | `48.21%` | `1.07` | 113,290.00 USD |
| `15M` | `Bitunix` | `12.41%` | `87.59%` | `0.14` | 28,320.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `57.35%` | `42.65%` | `1.34` | 185,920.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `45.34%` | `54.66%` | `0.83` | 104,660.00 USD |
| `15M` | `HTX` | `43.62%` | `56.38%` | `0.77` | 1,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 12.04 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `65.09%` | `34.91%` | `1.86` | 241,340.00 USD |
| `15M` | `Global Accounts` | `53.02%` | `46.98%` | `1.13` | 1,020,000.00 USD |
| `1H` | `PAXG` | `50.31%` | `49.69%` | `1.01` | 7,690,000.00 USD |
| `1H` | `Binance` | `55.69%` | `44.31%` | `1.26` | 1,680,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `48.1%` | `51.9%` | `0.93` | 1,040,000.00 USD |
| `1H` | `KuCoin` | `21.67%` | `78.33%` | `0.28` | 71,810.00 USD |
| `1H` | `Gate` | `41.26%` | `58.74%` | `0.70` | 550,200.00 USD |
| `1H` | `Bitget` | `48.35%` | `51.65%` | `0.94` | 646,410.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `56.32%` | `43.68%` | `1.29` | 1,810,000.00 USD |
| `1H` | `Bitunix` | `37.7%` | `62.3%` | `0.61` | 821,740.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `57%` | `43%` | `1.33` | 873,280.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.28%` | `78.72%` | `0.27` | 171,100.00 USD |
| `1H` | `HTX` | `39.19%` | `60.81%` | `0.64` | 2,680.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `64.8%` | `35.2%` | `1.84` | 14,150.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `55.69%` | `44.31%` | `1.26` | 1,680,000.00 USD |
| `1H` | `Global Accounts` | `50.31%` | `49.69%` | `1.01` | 7,690,000.00 USD |
| `4H` | `PAXG` | `45.89%` | `54.11%` | `0.85` | 58,550,000.00 USD |
| `4H` | `Binance` | `53.91%` | `46.09%` | `1.17` | 6,380,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `55.19%` | `44.81%` | `1.23` | 5,670,000.00 USD |
| `4H` | `KuCoin` | `23.98%` | `76.02%` | `0.32` | 308,720.00 USD |
| `4H` | `Gate` | `50.45%` | `49.55%` | `1.02` | 2,700,000.00 USD |
| `4H` | `Bitget` | `56.04%` | `43.96%` | `1.27` | 2,000,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `40.87%` | `59.13%` | `0.69` | 32,080,000.00 USD |
| `4H` | `Bitunix` | `46.11%` | `53.89%` | `0.86` | 3,390,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.37%` | `41.63%` | `1.40` | 4,830,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.88%` | `81.12%` | `0.23` | 1,060,000.00 USD |
| `4H` | `HTX` | `36.19%` | `63.81%` | `0.57` | 11,630.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `37.11%` | `62.89%` | `0.59` | 103,050.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.91%` | `46.09%` | `1.17` | 6,380,000.00 USD |
| `4H` | `Global Accounts` | `45.89%` | `54.11%` | `0.85` | 58,550,000.00 USD |


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
| `5m` | 236,660.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | 220,140.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `30m` | 191,740.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1h` | -47,280.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,200,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,370,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,790,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,030,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,410,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -939,450.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,070,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,850,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+236.66K` | 15m=`+220.14K` | 1h=`-47.28K` | 24h=`-939.45K`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4017.81` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.70` (Risk Distance: `8.11` pts)
  * +2.5R Take Profit: `4038.08`
  * Mathematical Lot Sizing: **`1.23 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4023.03` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4031.14` (Risk Distance: `8.11` pts)
  * +2.5R Take Profit: `4002.76`
  * Mathematical Lot Sizing: **`1.23 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4053.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
