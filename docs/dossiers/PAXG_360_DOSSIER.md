# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 10:59:03 IST` (`2026-10-30 05:29:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3999.89` | **Live Ask Quote**: `3999.97` | **Mid Price**: `3999.93`
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
  * Session VWAP: `4002.92` | VWAP Z-Score: `-0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.39` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.90` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4021.07` | Lower -3.00σ Band: `3984.76`
  * Upper +2.51σ Band: `4018.11` | Lower -2.51σ Band: `3987.72`
  * Upper +2.01σ Band: `4015.08` | Lower -2.01σ Band: `3990.75`
  * Upper +2.00σ Band: `4015.02` | Lower -2.00σ Band: `3990.81`
  * Upper +1.28σ Band: `4010.66` | Lower -1.28σ Band: `3995.17`
  * Upper +1.00σ Band: `4008.97` | Lower -1.00σ Band: `3996.86`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3996.64` | EMA-20=`4000.70` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4009.21` (Slope: `+0.0000`) | EMA-100=`4018.06`
  * Institutional Anchors: EMA-144=`4022.32` | EMA-200=`4024.82` (Slope: `-0.0895`) | EMA-233=`4026.72`
- **Range Boundaries**: 24H High=`4046.38` | 24H Low=`3987.44` | Weekly High=`4082.75` | Weekly Low=`3987.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.04` (Distance: `-0.33%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.18%`)
  * Value Area Low (VAL) = `3996.44` (Distance: `+0.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4001.83` | Low=`3996.58`
  * New York Session (13:00-21:00 UTC): High=`4023.93` | Low=`3975.93`
  * Initial Balance (First Hour): IB High=`4001.83` | IB Low=`3996.58`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3983.93` - `4015.93`
  * Optimal Trade Entry (OTE 0.705): `4007.93`
  * Structural Invalidation Anchor (0.786): `4031.93`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4008.05` | `4009.65` | `4007.11` | `4007.11` | `54` | 215,549.80 USD | -16,800.54 USD | `-7.79%` | 218,405.37 USD | `-0.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4007.11` | `4007.78` | `4006.74` | `4007.78` | `22` | 90,037.83 USD | 24,695.31 USD | `+27.43%` | 243,100.68 USD | `-0.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4007.77` | `4008.31` | `4007.40` | `4008.31` | `19` | 75,452.30 USD | 21,722.52 USD | `+28.79%` | 264,823.20 USD | `-0.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4000.32` | `4003.79` | `3999.97` | `4002.94` | `232` | 930,315.12 USD | 460,670.59 USD | `+49.52%` | -250,973.90 USD | `+1.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4002.94` | `4009.65` | `4002.94` | `4007.11` | `318` | 1,272,733.92 USD | 529,845.01 USD | `+41.63%` | 278,871.10 USD | `+1.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4007.11` | `4008.31` | `4006.74` | `4008.30` | `43` | 170,636.78 USD | 41,271.17 USD | `+24.19%` | 320,142.28 USD | `+0.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -446,454.31 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4002.94` | `1,790` | 7,158,366.15 USD | 437,268.83 USD | `+6.11%` | -9,185.48 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4002.94` | `4009.65` | `4002.94` | `4008.30` | `360` | 1,443,370.71 USD | 571,116.18 USD | `+39.57%` | 561,930.70 USD | `+1.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4009.65` | `3995.14` | `4008.30` | `2,150` | 8,601,736.86 USD | 1,008,385.01 USD | `+11.72%` | 956,293.48 USD | `+1.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4009.65` | `3995.14` | `4008.30` | `2,150` | 8,601,736.86 USD | 1,008,385.01 USD | `+11.72%` | 956,293.48 USD | `+1.03` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `3999.30` | `81.8743` | 327,439.89 USD | 1,140,042.10 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3999.40` | `0.3721` | 1,488.18 USD | 812,602.21 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3999.50` | `2.4363` | 9,743.98 USD | 811,114.03 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3999.60` | `3.7503` | 14,999.70 USD | 801,370.05 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3999.70` | `12.4146` | 49,654.68 USD | 786,370.35 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3999.80` | `17.5225` | 70,086.50 USD | 736,715.68 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3999.90` | `53.5961` | 214,379.04 USD | 666,629.18 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4000.00` | `12.0617` | 48,246.80 USD | 452,250.14 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4000.10` | `5.1759` | 20,704.12 USD | 404,003.34 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4000.20` | `5.6203` | 22,482.32 USD | 383,299.22 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4000.30` | `17.6641` | 70,661.70 USD | 360,816.90 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4000.40` | `3.3756` | 13,503.75 USD | 290,155.20 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4000.50` | `29.2966` | 117,201.05 USD | 276,651.45 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4000.60` | `10.1635` | 40,660.10 USD | 159,450.40 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4000.80` | `1.3381` | 5,353.47 USD | 118,790.30 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4000.90` | `3.7491` | 14,999.77 USD | 113,436.83 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4001.00` | `1.1211` | 4,485.52 USD | 98,437.06 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4001.20` | `3.7488` | 14,999.70 USD | 93,951.54 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4001.30` | `5.8408` | 23,370.79 USD | 78,951.84 USD | `4 orders` | `-0.00%` | `-` |
| `BID` | `4001.40` | `13.8904` | 55,581.05 USD | 55,581.05 USD | `9 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4001.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,001.45` | `0.00%` | `-` |
| `ASK` | `4001.50` | `3.0493` | 12,201.77 USD | 12,201.77 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4001.60` | `9.2649` | 37,074.42 USD | 49,276.20 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4001.70` | `26.2960` | 105,228.70 USD | 154,504.90 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4001.80` | `12.9157` | 51,686.05 USD | 206,190.95 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4001.90` | `14.2444` | 57,004.66 USD | 263,195.61 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4002.00` | `14.9599` | 59,869.52 USD | 323,065.13 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4002.10` | `0.3923` | 1,570.02 USD | 324,635.16 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4002.20` | `9.0581` | 36,252.33 USD | 360,887.49 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4002.30` | `62.8345` | 251,482.52 USD | 612,370.00 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4002.40` | `8.4082` | 33,652.98 USD | 646,022.98 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4002.50` | `13.1471` | 52,621.27 USD | 698,644.25 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4002.60` | `11.9786` | 47,945.54 USD | 746,589.80 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4002.70` | `58.3473` | 233,546.74 USD | 980,136.53 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4002.80` | `4.3849` | 17,551.88 USD | 997,688.41 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4002.90` | `80.5877` | 322,584.50 USD | 1,320,272.92 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4003.00` | `5.7813` | 23,142.54 USD | 1,343,415.46 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4003.10` | `9.4794` | 37,946.99 USD | 1,381,362.45 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4003.20` | `0.4684` | 1,875.10 USD | 1,383,237.54 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4003.30` | `5.8692` | 23,496.17 USD | 1,406,733.71 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4003.40` | `5.9663` | 23,885.49 USD | 1,430,619.20 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:53:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,976,818.52 USD | `6,489.82` | `4185.46` | `4002.70` | `29219.78` | 1,186,132.49 USD | `+4.57%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,255,956.67 USD | `6,309.73` | `4129.12` | `4002.70` | `13947.36` | 797,703.14 USD | `+3.16%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,495,446.33 USD | `5,869.90` | `4228.86` | `4002.70` | `26898.69` | 1,327,575.61 USD | `+5.65%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,328,665.65 USD | `4,828.91` | `4157.43` | `4002.70` | `2262.56` | -747,216.67 USD | `-3.87%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,215,555.83 USD | `3,551.49` | `4127.82` | `4002.70` | `589.91` | -444,386.12 USD | `-3.13%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,081,676.98 USD | `3,268.21` | `4228.94` | `4002.70` | `4373.26` | 739,402.15 USD | `+5.65%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,607,830.40 USD | `2,900.00` | `4364.92` | `4002.70` | `4235.92` | 1,050,445.93 USD | `+9.05%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,805,940.00 USD | `2,200.00` | `4176.09` | `4002.70` | `2591.25` | -381,479.30 USD | `-4.33%` | `25X Cross` |
| `265` | `0x41e5...0825` | `SHORT` | 8,805,940.00 USD | `2,200.00` | `4112.20` | `4002.70` | `4331.40` | 240,914.59 USD | `+2.74%` | `20X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,906,809.90 USD | `1,975.37` | `4048.55` | `4002.70` | `6577.79` | 90,581.82 USD | `+1.15%` | `6X Cross` |
| `366` | `0xc26c...b8f4` | `LONG` | 6,324,073.07 USD | `1,579.95` | `4075.62` | `4002.70` | `0.000000` | -115,223.90 USD | `-1.82%` | `1X Cross` |
| `568` | `0x63da...8add` | `LONG` | 4,002,700.00 USD | `1,000.00` | `4021.46` | `4002.70` | `3564.37` | -18,760.96 USD | `-0.47%` | `25X Cross` |
| `576` | `0xf3dc...1672` | `LONG` | 3,939,740.33 USD | `984.27` | `4018.39` | `4002.70` | `2906.64` | -15,446.36 USD | `-0.39%` | `20X Cross` |
| `590` | `0x9aa5...58af` | `LONG` | 3,889,191.43 USD | `971.64` | `4279.98` | `4002.70` | `0.000000` | -269,417.65 USD | `-6.93%` | `20X Cross` |
| `597` | `0x354b...6425` | `LONG` | 3,837,818.38 USD | `958.81` | `4004.93` | `4002.70` | `0.000000` | -2,142.84 USD | `-0.06%` | `10X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,351,859.78 USD | `837.40` | `4599.73` | `4002.70` | `0.000000` | -499,960.60 USD | `-14.92%` | `20X Cross` |
| `830` | `0x0fac...7a0a` | `LONG` | 2,747,793.51 USD | `686.49` | `4290.34` | `4002.70` | `1173.98` | -197,465.19 USD | `-7.19%` | `25X Cross` |
| `911` | `0x625e...a354` | `SHORT` | 2,481,674.00 USD | `620.00` | `4122.81` | `4002.70` | `4342.50` | 74,473.03 USD | `+3.00%` | `20X Cross` |
| `915` | `0xd8c5...99b0` | `SHORT` | 2,475,089.16 USD | `618.35` | `4175.35` | `4002.70` | `34146.89` | 106,763.45 USD | `+4.31%` | `4X Cross` |
| `941` | `0xeae3...e8ad` | `SHORT` | 2,401,620.00 USD | `600.00` | `4104.77` | `4002.70` | `4325.52` | 61,245.11 USD | `+2.55%` | `20X Cross` |
| `942` | `0xf285...fa82` | `LONG` | 2,394,038.49 USD | `598.11` | `4146.45` | `4002.70` | `3891.51` | -85,981.07 USD | `-3.59%` | `25X Cross` |
| `958` | `0x12f7...8750` | `LONG` | 2,344,023.95 USD | `585.61` | `4082.77` | `4002.70` | `2592.20` | -46,893.03 USD | `-2.00%` | `10X Cross` |
| `1097` | `0x413c...886c` | `LONG` | 2,001,350.00 USD | `500.00` | `4010.43` | `4002.70` | `0.000000` | -3,866.23 USD | `-0.19%` | `2X Cross` |
| `1101` | `0x9c06...0560` | `LONG` | 1,995,014.93 USD | `498.42` | `4012.76` | `4002.70` | `0.000000` | -5,016.57 USD | `-0.25%` | `25X Cross` |
| `1105` | `0x61ce...a62b` | `SHORT` | 1,991,357.26 USD | `497.50` | `4071.66` | `4002.70` | `4715.35` | 34,311.53 USD | `+1.72%` | `20X Cross` |
| `1179` | `0x2edd...8179` | `LONG` | 1,884,062.92 USD | `469.89` | `4164.68` | `4009.60` | `0.000000` | -72,869.59 USD | `-3.87%` | `10X Cross` |
| `1219` | `0xead5...69f2` | `LONG` | 1,816,360.82 USD | `453.78` | `4220.88` | `4002.70` | `3539.20` | -99,007.24 USD | `-5.45%` | `5X Isolated` |
| `1276` | `0x7a6d...f79c` | `SHORT` | 1,717,114.38 USD | `428.38` | `4136.09` | `4009.60` | `5346.93` | 54,700.62 USD | `+3.19%` | `10X Cross` |
| `1290` | `0x46fc...1195` | `LONG` | 1,689,706.18 USD | `422.14` | `4053.27` | `4002.70` | `2158.19` | -21,348.69 USD | `-1.26%` | `20X Cross` |
| `1353` | `0x6d15...d374` | `LONG` | 1,601,080.00 USD | `400.00` | `4068.25` | `4002.70` | `3842.07` | -26,220.00 USD | `-1.64%` | `25X Cross` |
| `1354` | `0xee02...309d` | `SHORT` | 1,601,080.00 USD | `400.00` | `4438.84` | `4002.70` | `4227.14` | 174,458.60 USD | `+10.90%` | `25X Isolated` |
| `1392` | `0x51f6...2b39` | `LONG` | 1,565,012.10 USD | `390.33` | `4228.91` | `4009.60` | `576.33` | -85,640.99 USD | `-5.47%` | `10X Cross` |
| `1398` | `0x02a7...fe9f` | `SHORT` | 1,561,053.00 USD | `390.00` | `4055.02` | `4002.70` | `4306.96` | 20,406.25 USD | `+1.31%` | `25X Cross` |
| `1439` | `0x7e77...b8d2` | `SHORT` | 1,521,026.00 USD | `380.00` | `4131.92` | `4002.70` | `4293.77` | 49,103.64 USD | `+3.23%` | `20X Cross` |
| `1461` | `0x72c2...9b37` | `LONG` | 1,493,532.65 USD | `373.13` | `4000.98` | `4002.70` | `3778.31` | 639.14 USD | `+0.04%` | `13X Isolated` |
| `1503` | `0x781e...96b7` | `SHORT` | 1,448,287.53 USD | `361.21` | `4363.41` | `4009.60` | `12893.46` | 127,836.05 USD | `+8.83%` | `10X Cross` |
| `1509` | `0xaa44...b844` | `LONG` | 1,440,972.00 USD | `360.00` | `4043.10` | `4002.70` | `2819.39` | -14,545.63 USD | `-1.01%` | `4X Cross` |
| `1613` | `0xa41f...d50a` | `LONG` | 1,316,736.60 USD | `328.96` | `4468.89` | `4002.70` | `3802.43` | -153,361.25 USD | `-11.65%` | `15X Cross` |
| `1632` | `0x7fda...17d1` | `SHORT` | 1,301,097.25 USD | `325.05` | `4013.13` | `4002.70` | `30486.81` | 3,390.73 USD | `+0.26%` | `20X Cross` |
| `1667` | `0xbf5a...88ba` | `SHORT` | 1,271,477.27 USD | `317.65` | `4091.80` | `4002.70` | `10006.50` | 28,305.76 USD | `+2.23%` | `20X Cross` |
| `1703` | `0xff31...ff6c` | `SHORT` | 1,240,837.00 USD | `310.00` | `4372.43` | `4002.70` | `4789.43` | 114,618.38 USD | `+9.24%` | `10X Isolated` |
| `1727` | `0xada6...6f88` | `LONG` | 1,214,810.64 USD | `303.50` | `4166.46` | `4002.70` | `1786.50` | -49,702.22 USD | `-4.09%` | `5X Cross` |
| `1892` | `0x50e2...d770` | `LONG` | 1,082,199.59 USD | `270.37` | `4243.58` | `4002.70` | `2562.36` | -65,126.87 USD | `-6.02%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,067,602.15 USD | `266.72` | `4260.98` | `4002.70` | `6518.05` | 68,890.09 USD | `+6.45%` | `20X Cross` |
| `1989` | `0xd346...c4f3` | `LONG` | 1,021,384.17 USD | `255.17` | `4188.66` | `4002.70` | `3310.69` | -47,452.34 USD | `-4.65%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.81` (Vol: 274,500.00 USD, Dist: `+2.67%`) | Long MP=`3936.71` (Vol: 378,100.00 USD, Dist: `--1.65%`)
  * 48H Horizon: Short MP=`4097.67` (Vol: 378,100.00 USD, Dist: `+2.37%`) | Long MP=`3936.55` (Vol: 378,100.00 USD, Dist: `--1.66%`)
  * 3D Horizon: Short MP=`4097.67` (Vol: 405,200.00 USD, Dist: `+2.37%`) | Long MP=`3936.55` (Vol: 405,200.00 USD, Dist: `--1.66%`)
  * 7D Horizon: Short MP=`4086.63` (Vol: 910,300.00 USD, Dist: `+2.09%`) | Long MP=`3923.02` (Vol: 1,000,000.00 USD, Dist: `--2.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3596.10` | 16,690,000.00 USD | 16,690,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.30` | 4,880,000.00 USD | 4,880,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.40` | 16,660,000.00 USD | 16,660,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.40` | 4,870,000.00 USD | 4,870,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.70` | 16,500,000.00 USD | 16,500,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.50` | 4,810,000.00 USD | 4,810,000.00 USD | 55,240.00 USD | 0.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.00` | 16,230,000.00 USD | 16,230,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.60` | 4,740,000.00 USD | 4,740,000.00 USD | 16,140.00 USD | 0.00 USD | 4,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.30` | 16,040,000.00 USD | 16,040,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.70` | 4,720,000.00 USD | 4,720,000.00 USD | 34,930.00 USD | 0.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.60` | 15,940,000.00 USD | 15,940,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 4,680,000.00 USD | 4,680,000.00 USD | 43,270.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.90` | 15,820,000.00 USD | 15,820,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.90` | 4,630,000.00 USD | 4,630,000.00 USD | 64,410.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.20` | 15,740,000.00 USD | 15,740,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.00` | 4,550,000.00 USD | 4,550,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.50` | 15,660,000.00 USD | 15,660,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.10` | 4,510,000.00 USD | 4,510,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.80` | 15,540,000.00 USD | 15,540,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.20` | 4,460,000.00 USD | 4,460,000.00 USD | 14,390.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.10` | 15,450,000.00 USD | 15,450,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.30` | 4,450,000.00 USD | 4,450,000.00 USD | 4,660.00 USD | 0.00 USD | 205.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.40` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 309.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.40` | 15,390,000.00 USD | 15,390,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.70` | 15,340,000.00 USD | 15,340,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.00` | 15,310,000.00 USD | 15,310,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.30` | 15,280,000.00 USD | 15,280,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.60` | 15,230,000.00 USD | 15,230,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3664.90` | 15,220,000.00 USD | 15,220,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 15,210,000.00 USD | 15,210,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3836.90` | 15,190,000.00 USD | 15,190,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.20` | 4,440,000.00 USD | 4,440,000.00 USD | 37,720.00 USD | 0.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.20` | 14,990,000.00 USD | 14,990,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.30` | 4,370,000.00 USD | 4,370,000.00 USD | 190,530.00 USD | 0.00 USD | 102,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.50` | 14,330,000.00 USD | 14,330,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.40` | 4,080,000.00 USD | 4,080,000.00 USD | 46,980.00 USD | 0.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,640,000.00 USD | 13,640,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.50` | 4,010,000.00 USD | 4,010,000.00 USD | 78,750.00 USD | 0.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.10` | 13,100,000.00 USD | 13,100,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.60` | 3,910,000.00 USD | 3,910,000.00 USD | 103,770.00 USD | 0.00 USD | 16,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.40` | 12,800,000.00 USD | 12,800,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.70` | 3,790,000.00 USD | 3,790,000.00 USD | 149,050.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.70` | 12,390,000.00 USD | 12,390,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.80` | 3,610,000.00 USD | 3,610,000.00 USD | 224,310.00 USD | 0.00 USD | 37,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.00` | 12,140,000.00 USD | 12,140,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.90` | 3,350,000.00 USD | 3,350,000.00 USD | 144,700.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.30` | 11,860,000.00 USD | 11,860,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.00` | 3,190,000.00 USD | 3,190,000.00 USD | 126,020.00 USD | 0.00 USD | 18,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.60` | 11,540,000.00 USD | 11,540,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.10` | 3,040,000.00 USD | 3,040,000.00 USD | 54,860.00 USD | 0.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.90` | 11,150,000.00 USD | 11,150,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.20` | 2,980,000.00 USD | 2,980,000.00 USD | 16,620.00 USD | 0.00 USD | 981.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.20` | 10,830,000.00 USD | 10,830,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.30` | 2,960,000.00 USD | 2,960,000.00 USD | 1,930.00 USD | 0.00 USD | 774.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,680,000.00 USD | 10,680,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.80` | 10,570,000.00 USD | 10,570,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.10` | 10,440,000.00 USD | 10,440,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.40` | 10,330,000.00 USD | 10,330,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.70` | 10,240,000.00 USD | 10,240,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.00` | 10,170,000.00 USD | 10,170,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3918.10` | 2,960,000.00 USD | 2,960,000.00 USD | 44,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.60` | 10,120,000.00 USD | 10,120,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.20` | 2,920,000.00 USD | 2,920,000.00 USD | 132,900.00 USD | 0.00 USD | 142,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.90` | 9,220,000.00 USD | 9,220,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.30` | 2,640,000.00 USD | 2,640,000.00 USD | 346,980.00 USD | 0.00 USD | 158,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.20` | 7,820,000.00 USD | 7,820,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.40` | 2,140,000.00 USD | 2,140,000.00 USD | 40,700.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 6,460,000.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.50` | 2,060,000.00 USD | 2,060,000.00 USD | 237,090.00 USD | 0.00 USD | 57,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.80` | 5,710,000.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.60` | 1,770,000.00 USD | 1,770,000.00 USD | 194,880.00 USD | 0.00 USD | 22,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.10` | 4,800,000.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.70` | 1,550,000.00 USD | 1,550,000.00 USD | 351,210.00 USD | 0.00 USD | 64,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.40` | 4,410,000.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.80` | 1,130,000.00 USD | 1,130,000.00 USD | 360,350.00 USD | 0.00 USD | 55,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.70` | 3,860,000.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.90` | 717,630.00 USD | 717,630.00 USD | 346,950.00 USD | 0.00 USD | 39,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.00` | 3,200,000.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.00` | 330,970.00 USD | 330,970.00 USD | 181,840.00 USD | 0.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.30` | 2,580,000.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.10` | 120,490.00 USD | 120,490.00 USD | 92,090.00 USD | 0.00 USD | 3,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,820,000.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 24,480.00 USD | 24,480.00 USD | 17,440.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.90` | 1,320,000.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.30` | 4,580.00 USD | 4,580.00 USD | 3,860.00 USD | 0.00 USD | 719.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.20` | 1,050,000.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.50` | 831,670.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.80` | 579,930.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.10` | 237,060.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.40` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.70` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.00` | 44,190.00 USD | 44,190.00 USD | 44,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4082.10` | 291,510.00 USD | 291,510.00 USD | 111,050.00 USD | 0.00 USD | 136,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4086.20` | 795,350.00 USD | 795,350.00 USD | 339,320.00 USD | 0.00 USD | 164,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.30` | 900,020.00 USD | 900,020.00 USD | 70,210.00 USD | 0.00 USD | 34,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.40` | 1,140,000.00 USD | 1,140,000.00 USD | 195,060.00 USD | 0.00 USD | 49,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 4,800,000.00 USD | 4,800,000.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.50` | 1,350,000.00 USD | 1,350,000.00 USD | 188,180.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.20` | 5,540,000.00 USD | 5,540,000.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.60` | 1,720,000.00 USD | 1,720,000.00 USD | 297,100.00 USD | 0.00 USD | 68,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 6,040,000.00 USD | 6,040,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.70` | 2,220,000.00 USD | 2,220,000.00 USD | 443,380.00 USD | 0.00 USD | 53,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.80` | 6,630,000.00 USD | 6,630,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.80` | 2,520,000.00 USD | 2,520,000.00 USD | 263,130.00 USD | 0.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.10` | 7,110,000.00 USD | 7,110,000.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.90` | 2,800,000.00 USD | 2,800,000.00 USD | 252,040.00 USD | 0.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.40` | 7,730,000.00 USD | 7,730,000.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.00` | 2,900,000.00 USD | 2,900,000.00 USD | 92,040.00 USD | 0.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 8,530,000.00 USD | 8,530,000.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.10` | 2,950,000.00 USD | 2,950,000.00 USD | 46,200.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.00` | 8,960,000.00 USD | 8,960,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.20` | 2,960,000.00 USD | 2,960,000.00 USD | 8,580.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.30` | 9,140,000.00 USD | 9,140,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.60` | 9,380,000.00 USD | 9,380,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4137.90` | 9,620,000.00 USD | 9,620,000.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 9,900,000.00 USD | 9,900,000.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.50` | 9,960,000.00 USD | 9,960,000.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.80` | 10,090,000.00 USD | 10,090,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.10` | 10,160,000.00 USD | 10,160,000.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.40` | 10,630,000.00 USD | 10,630,000.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.00` | 3,030,000.00 USD | 3,030,000.00 USD | 37,720.00 USD | 0.00 USD | 27,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.70` | 11,380,000.00 USD | 11,380,000.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.10` | 3,300,000.00 USD | 3,300,000.00 USD | 184,330.00 USD | 0.00 USD | 88,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.00` | 11,970,000.00 USD | 11,970,000.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.20` | 3,390,000.00 USD | 3,390,000.00 USD | 53,170.00 USD | 0.00 USD | 35,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4172.30` | 3,460,000.00 USD | 3,460,000.00 USD | 46,000.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.30` | 12,340,000.00 USD | 12,340,000.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.40` | 3,590,000.00 USD | 3,590,000.00 USD | 103,540.00 USD | 0.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.60` | 12,800,000.00 USD | 12,800,000.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.50` | 3,710,000.00 USD | 3,710,000.00 USD | 112,920.00 USD | 0.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.90` | 12,990,000.00 USD | 12,990,000.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.60` | 3,880,000.00 USD | 3,880,000.00 USD | 142,270.00 USD | 0.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.20` | 13,210,000.00 USD | 13,210,000.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.70` | 4,100,000.00 USD | 4,100,000.00 USD | 192,900.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.50` | 13,500,000.00 USD | 13,500,000.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.80` | 4,280,000.00 USD | 4,280,000.00 USD | 154,770.00 USD | 0.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4193.80` | 13,790,000.00 USD | 13,790,000.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.90` | 4,380,000.00 USD | 4,380,000.00 USD | 90,920.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.10` | 14,120,000.00 USD | 14,120,000.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.00` | 4,430,000.00 USD | 4,430,000.00 USD | 40,760.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.40` | 14,420,000.00 USD | 14,420,000.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.10` | 4,440,000.00 USD | 4,440,000.00 USD | 14,000.00 USD | 0.00 USD | 817.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.70` | 14,640,000.00 USD | 14,640,000.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.20` | 4,440,000.00 USD | 4,440,000.00 USD | 1,930.00 USD | 0.00 USD | 774.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,720,000.00 USD | 14,720,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.30` | 14,840,000.00 USD | 14,840,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.60` | 14,960,000.00 USD | 14,960,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.90` | 15,080,000.00 USD | 15,080,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.20` | 15,110,000.00 USD | 15,110,000.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.50` | 15,180,000.00 USD | 15,180,000.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.80` | 15,200,000.00 USD | 15,200,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.90` | 15,260,000.00 USD | 15,260,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4397.80` | 4,450,000.00 USD | 4,450,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.20` | 15,390,000.00 USD | 15,390,000.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4401.90` | 4,490,000.00 USD | 4,490,000.00 USD | 14,970.00 USD | 0.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.50` | 15,610,000.00 USD | 15,610,000.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4406.00` | 4,560,000.00 USD | 4,560,000.00 USD | 52,600.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.80` | 15,790,000.00 USD | 15,790,000.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4410.10` | 4,580,000.00 USD | 4,580,000.00 USD | 11,180.00 USD | 0.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4412.10` | 4,590,000.00 USD | 4,590,000.00 USD | 9,760.00 USD | 0.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.10` | 15,880,000.00 USD | 15,880,000.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.40` | 15,980,000.00 USD | 15,980,000.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.70` | 16,070,000.00 USD | 16,070,000.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.00` | 16,130,000.00 USD | 16,130,000.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,200,000.00 USD | 16,200,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.60` | 16,270,000.00 USD | 16,270,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.90` | 16,360,000.00 USD | 16,360,000.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4440.70` | 16,400,000.00 USD | 16,400,000.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |

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
| `7D` | `3596.10` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3598.10` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 4,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3600.40` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD |
| `1D` | `3602.30` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 26,240.00 USD | 0.00 USD | 33,420.00 USD |
| `7D` | `3604.70` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD |
| `1D` | `3606.50` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 55,240.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `3609.00` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD |
| `1D` | `3610.70` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 19,350.00 USD | 0.00 USD | 6,310.00 USD |
| `7D` | `3613.30` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3614.90` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 37,500.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `3617.60` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3619.10` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 41,050.00 USD | 0.00 USD | 7,170.00 USD |
| `7D` | `3621.90` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3623.30` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD |
| `7D` | `3626.20` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.50` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 40,050.00 USD | 0.00 USD | 6,280.00 USD |
| `7D` | `3630.50` | 15,300,000.00 USD | 0.00 USD | 15,300,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.70` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 29,160.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `3634.80` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 44,190.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `3635.90` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 14,670.00 USD | 0.00 USD | 640.43 USD |
| `7D` | `3639.10` | 15,130,000.00 USD | 0.00 USD | 15,130,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD |
| `1D` | `3640.10` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 2,540.00 USD | 0.00 USD | 371.50 USD |
| `7D` | `3643.40` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `3644.30` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 143.82 USD |
| `7D` | `3647.70` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.00` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.30` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.60` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3664.90` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.60` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3836.90` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD |
| `7D` | `3841.20` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD |
| `1D` | `3841.70` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 77,620.00 USD | 0.00 USD | 66,430.00 USD |
| `7D` | `3845.50` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD |
| `1D` | `3845.90` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 169,660.00 USD | 0.00 USD | 83,970.00 USD |
| `7D` | `3849.80` | 13,330,000.00 USD | 0.00 USD | 13,330,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD |
| `1D` | `3850.10` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 35,100.00 USD | 0.00 USD | 21,400.00 USD |
| `7D` | `3854.10` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 249,250.00 USD | 0.00 USD | 66,410.00 USD |
| `1D` | `3854.30` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 118,550.00 USD | 0.00 USD | 36,040.00 USD |
| `7D` | `3858.40` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD |
| `1D` | `3858.50` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 117,680.00 USD | 0.00 USD | 10,760.00 USD |
| `1D` | `3862.70` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 161,340.00 USD | 0.00 USD | 33,490.00 USD |
| `7D` | `3862.70` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3866.90` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 218,970.00 USD | 0.00 USD | 29,970.00 USD |
| `7D` | `3867.00` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3871.10` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 139,970.00 USD | 0.00 USD | 21,730.00 USD |
| `7D` | `3871.30` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3875.30` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 84,790.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3875.60` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 297,370.00 USD | 0.00 USD | 29,270.00 USD |
| `1D` | `3879.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 47,280.00 USD | 0.00 USD | 674.78 USD |
| `7D` | `3879.90` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 235,430.00 USD | 0.00 USD | 27,170.00 USD |
| `1D` | `3883.70` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 2,360.00 USD | 0.00 USD | 1,590.00 USD |
| `7D` | `3884.20` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD |
| `7D` | `3888.50` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3892.80` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.10` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.40` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.70` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.00` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3918.60` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3921.50` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 145,460.00 USD | 0.00 USD | 132,060.00 USD |
| `7D` | `3922.90` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3925.70` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 349,100.00 USD | 0.00 USD | 168,730.00 USD |
| `7D` | `3927.20` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD |
| `1D` | `3929.90` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 70,210.00 USD | 0.00 USD | 38,320.00 USD |
| `7D` | `3931.50` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 605,700.00 USD | 0.00 USD | 168,200.00 USD |
| `1D` | `3934.10` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 230,830.00 USD | 0.00 USD | 69,650.00 USD |
| `7D` | `3935.80` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD |
| `1D` | `3938.30` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 193,170.00 USD | 0.00 USD | 27,550.00 USD |
| `7D` | `3940.10` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD |
| `1D` | `3942.50` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 337,110.00 USD | 0.00 USD | 64,130.00 USD |
| `7D` | `3944.40` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD |
| `1D` | `3946.70` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 369,640.00 USD | 0.00 USD | 54,490.00 USD |
| `7D` | `3948.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD |
| `1D` | `3950.90` | 728,450.00 USD | 0.00 USD | 728,450.00 USD | 359,720.00 USD | 0.00 USD | 41,620.00 USD |
| `7D` | `3953.00` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD |
| `1D` | `3955.10` | 327,110.00 USD | 0.00 USD | 327,110.00 USD | 181,840.00 USD | 0.00 USD | 30,090.00 USD |
| `7D` | `3957.30` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 478,000.00 USD | 0.00 USD | 49,670.00 USD |
| `1D` | `3959.30` | 115,170.00 USD | 0.00 USD | 115,170.00 USD | 92,090.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3961.60` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3963.50` | 20,620.00 USD | 0.00 USD | 20,620.00 USD | 17,440.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3965.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `3967.70` | 719.09 USD | 0.00 USD | 719.09 USD | 0.00 USD | 0.00 USD | 719.09 USD |
| `7D` | `3970.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.50` | 831,670.00 USD | 0.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3978.80` | 579,930.00 USD | 0.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD |
| `7D` | `3983.10` | 237,060.00 USD | 0.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `7D` | `3987.40` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.70` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4012.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4013.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4081.10` | 242,950.00 USD | 242,950.00 USD | 0.00 USD | 127,100.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD |
| `1D` | `4085.30` | 764,140.00 USD | 764,140.00 USD | 0.00 USD | 357,750.00 USD | 0.00 USD | 163,440.00 USD |
| `7D` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD |
| `1D` | `4089.50` | 871,530.00 USD | 871,530.00 USD | 0.00 USD | 65,600.00 USD | 0.00 USD | 41,800.00 USD |
| `7D` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4093.70` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 190,050.00 USD | 0.00 USD | 75,650.00 USD |
| `7D` | `4094.90` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 498,510.00 USD | 0.00 USD | 127,890.00 USD |
| `1D` | `4097.90` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 174,980.00 USD | 0.00 USD | 23,650.00 USD |
| `7D` | `4099.20` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4102.10` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 318,720.00 USD | 0.00 USD | 64,150.00 USD |
| `7D` | `4103.50` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4106.30` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 428,010.00 USD | 0.00 USD | 56,920.00 USD |
| `7D` | `4107.80` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4110.50` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 271,330.00 USD | 0.00 USD | 41,060.00 USD |
| `7D` | `4112.10` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD |
| `1D` | `4114.70` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 263,380.00 USD | 0.00 USD | 36,460.00 USD |
| `7D` | `4116.40` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD |
| `1D` | `4118.90` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 98,780.00 USD | 0.00 USD | 9,800.00 USD |
| `7D` | `4120.70` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 534,120.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4123.10` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 46,200.00 USD | 0.00 USD | 1,960.00 USD |
| `7D` | `4125.00` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `4127.30` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 4,710.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `4129.30` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `4133.60` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4137.90` | 9,410,000.00 USD | 9,410,000.00 USD | 0.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.20` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD |
| `7D` | `4146.50` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4150.80` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.10` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.40` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD |
| `1D` | `4160.90` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 63,550.00 USD | 0.00 USD | 49,950.00 USD |
| `7D` | `4163.70` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD |
| `1D` | `4165.10` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 173,460.00 USD | 0.00 USD | 88,140.00 USD |
| `7D` | `4168.00` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4169.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 38,210.00 USD | 0.00 USD | 17,960.00 USD |
| `7D` | `4172.30` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 302,850.00 USD | 0.00 USD | 82,190.00 USD |
| `1D` | `4173.50` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 78,750.00 USD | 0.00 USD | 37,250.00 USD |
| `7D` | `4176.60` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD |
| `1D` | `4177.70` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 98,810.00 USD | 0.00 USD | 16,900.00 USD |
| `7D` | `4180.90` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4181.90` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 149,130.00 USD | 0.00 USD | 22,110.00 USD |
| `7D` | `4185.20` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD |
| `1D` | `4186.10` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 184,700.00 USD | 0.00 USD | 30,230.00 USD |
| `7D` | `4189.50` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD |
| `1D` | `4190.30` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 143,610.00 USD | 0.00 USD | 24,610.00 USD |
| `7D` | `4193.80` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4194.50` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 153,560.00 USD | 0.00 USD | 17,770.00 USD |
| `7D` | `4198.10` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4198.70` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 39,890.00 USD | 0.00 USD | 8,960.00 USD |
| `7D` | `4202.40` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 222,160.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4202.90` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 47,280.00 USD | 0.00 USD | 977.87 USD |
| `7D` | `4206.70` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD |
| `1D` | `4207.10` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 2,360.00 USD | 0.00 USD | 928.74 USD |
| `7D` | `4211.00` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `1D` | `4211.30` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 359.54 USD |
| `7D` | `4215.30` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.60` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4223.90` | 14,770,000.00 USD | 14,770,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.20` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `4232.50` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD |
| `7D` | `4236.80` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.90` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `7D` | `4400.20` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4400.30` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 14,560.00 USD | 0.00 USD | 14,110.00 USD |
| `1D` | `4404.50` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 56,680.00 USD | 0.00 USD | 27,170.00 USD |
| `7D` | `4404.50` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD |
| `1D` | `4408.70` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 14,680.00 USD | 0.00 USD | 6,060.00 USD |
| `7D` | `4408.80` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD |
| `1D` | `4412.90` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `4413.10` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD |
| `1D` | `4416.00` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 19,970.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4417.40` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD |
| `7D` | `4421.70` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4426.00` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD |
| `7D` | `4430.30` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `4434.60` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4438.90` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD |
| `7D` | `4440.70` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 23,500.00 USD | 0.00 USD | 1,350.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `276.38M` | Total OI Tokens: `68,912.8 PAXG`
  * 1h OI Change: `-0.14%` | 4h OI Change: `+0.26%` | 24h OI Change: `+0.86%`
  * Exchange Breakdown: Binance=`107.28M` | Bybit=`22.18M` | OKX=`-` | Hyperliquid=`24.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.08K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `31.26%` | `68.74%` | `0.45` | 5,200,000.00 USD |
| `15M` | `Binance` | `33.91%` | `66.09%` | `0.51` | 1,630,000.00 USD |
| `15M` | `OKX` | `35.66%` | `64.34%` | `0.55` | 973,500.00 USD |
| `15M` | `Bybit` | `42.07%` | `57.93%` | `0.73` | 439,160.00 USD |
| `15M` | `KuCoin` | `42.7%` | `57.3%` | `0.75` | 19,670.00 USD |
| `15M` | `Gate` | `25.96%` | `74.04%` | `0.35` | 49,010.00 USD |
| `15M` | `Bitget` | `46.64%` | `53.36%` | `0.87` | 595,610.00 USD |
| `15M` | `BingX` | `2.96%` | `97.04%` | `0.03` | 848,080.00 USD |
| `15M` | `MEXC` | `19.84%` | `80.16%` | `0.25` | 340,800.00 USD |
| `15M` | `Bitunix` | `27.51%` | `72.49%` | `0.38` | 87,060.00 USD |
| `15M` | `Hyperliquid` | `61.38%` | `38.62%` | `1.59` | 48,340.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.15%` | `49.85%` | `1.01` | 124,190.00 USD |
| `15M` | `Crypto.com` | `1.84%` | `98.16%` | `0.02` | 494.64 USD |
| `15M` | `WhiteBIT` | `83.32%` | `16.68%` | `5.00` | 31,790.00 USD |
| `15M` | `HTX` | `29.97%` | `70.03%` | `0.43` | 1,110.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `46.73%` | `53.27%` | `0.88` | 176.32 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `88.56%` | `11.44%` | `7.74` | 5,190.00 USD |
| `15M` | `Whale Positions` | `33.91%` | `66.09%` | `0.51` | 1,630,000.00 USD |
| `15M` | `Global Accounts` | `31.26%` | `68.74%` | `0.45` | 5,200,000.00 USD |
| `1H` | `PAXG` | `48.94%` | `51.06%` | `0.96` | 12,380,000.00 USD |
| `1H` | `Binance` | `44.34%` | `55.66%` | `0.80` | 1,630,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `51.89%` | `48.11%` | `1.08` | 731,720.00 USD |
| `1H` | `KuCoin` | `41.62%` | `58.38%` | `0.71` | 36,810.00 USD |
| `1H` | `Gate` | `52.53%` | `47.47%` | `1.11` | 384,060.00 USD |
| `1H` | `Bitget` | `34.13%` | `65.87%` | `0.52` | 387,490.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `51.07%` | `48.93%` | `1.04` | 7,850,000.00 USD |
| `1H` | `Bitunix` | `43.93%` | `56.07%` | `0.78` | 440,290.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `63.07%` | `36.93%` | `1.71` | 592,840.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.41%` | `91.59%` | `0.09` | 309,150.00 USD |
| `1H` | `HTX` | `8.37%` | `91.63%` | `0.09` | 9,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `44.34%` | `55.66%` | `0.80` | 1,630,000.00 USD |
| `1H` | `Global Accounts` | `48.94%` | `51.06%` | `0.96` | 12,380,000.00 USD |
| `4H` | `PAXG` | `41.74%` | `58.26%` | `0.72` | 49,970,000.00 USD |
| `4H` | `Binance` | `46.51%` | `53.49%` | `0.87` | 8,210,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `46.01%` | `53.99%` | `0.85` | 3,770,000.00 USD |
| `4H` | `KuCoin` | `61.79%` | `38.21%` | `1.62` | 259,330.00 USD |
| `4H` | `Gate` | `49.66%` | `50.34%` | `0.99` | 1,750,000.00 USD |
| `4H` | `Bitget` | `46.66%` | `53.34%` | `0.87` | 2,810,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `37.5%` | `62.5%` | `0.60` | 26,890,000.00 USD |
| `4H` | `Bitunix` | `50.1%` | `49.9%` | `1.00` | 1,260,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.61%` | `46.39%` | `1.16` | 3,300,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `22.42%` | `77.58%` | `0.29` | 1,510,000.00 USD |
| `4H` | `HTX` | `84.31%` | `15.69%` | `5.37` | 155,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `15.38%` | `84.62%` | `0.18` | 50,640.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `46.51%` | `53.49%` | `0.87` | 8,210,000.00 USD |
| `4H` | `Global Accounts` | `41.74%` | `58.26%` | `0.72` | 49,970,000.00 USD |


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
| `5m` | 31,100.00 USD | 27,890.00 USD | **`ACCUMULATION`** |
| `15m` | 781,530.00 USD | 288,410.00 USD | **`ACCUMULATION`** |
| `30m` | 1,850,000.00 USD | 1,160,000.00 USD | **`ACCUMULATION`** |
| `1h` | 1,830,000.00 USD | 981,570.00 USD | **`ACCUMULATION`** |
| `2h` | 1,920,000.00 USD | 1,220,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,750,000.00 USD | 913,110.00 USD | **`ACCUMULATION`** |
| `6h` | 1,890,000.00 USD | -37,190.00 USD | **`ACCUMULATION`** |
| `8h` | 932,440.00 USD | 89,560.00 USD | **`ACCUMULATION`** |
| `12h` | 222,580.00 USD | 31,460.00 USD | **`ACCUMULATION`** |
| `24h` | 484,600.00 USD | 343,950.00 USD | **`ACCUMULATION`** |
| `1w` | -7,620,000.00 USD | -8,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -17,880,000.00 USD | -69,580,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+31.10K` | 15m=`+781.53K` | 1h=`+1.83M` | 24h=`+484.60K`
* Futures Capital Netflows: 5m=`+27.89K` | 15m=`+288.41K` | 1h=`+981.57K` | 24h=`+343.95K`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3996.44` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3987.46` (Risk Distance: `8.98` pts)
  * +2.5R Take Profit: `4018.90`
  * Mathematical Lot Sizing: **`1.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.02` (Risk Distance: `8.98` pts)
  * +2.5R Take Profit: `3990.58`
  * Mathematical Lot Sizing: **`1.11 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4031.93`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
