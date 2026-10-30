# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 10:07:34 IST` (`2026-10-30 04:37:34 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3994.27` | **Live Ask Quote**: `3994.35` | **Mid Price**: `3994.31`
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
  * Value Area High (VAH) = `4013.04` (Distance: `-0.47%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.32%`)
  * Value Area Low (VAL) = `3996.99` (Distance: `-0.07%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4010.29` | Low=`3978.33`
  * New York Session (13:00-21:00 UTC): High=`4018.28` | Low=`3970.34`
  * Initial Balance (First Hour): IB High=`4006.29` | IB Low=`3982.33`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3978.33` - `4010.29`
  * Optimal Trade Entry (OTE 0.705): `4002.30`
  * Structural Invalidation Anchor (0.786): `4026.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3999.84` | `4001.99` | `3999.56` | `4000.90` | `57` | 226,581.27 USD | 36,775.57 USD | `+16.23%` | -753,990.46 USD | `+0.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4000.90` | `4003.88` | `4000.90` | `4002.90` | `108` | 433,558.30 USD | 238,104.52 USD | `+54.92%` | -515,885.94 USD | `+1.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4002.91` | `4003.71` | `4002.91` | `4003.71` | `23` | 91,435.51 USD | -63,034.26 USD | `-68.94%` | -578,920.20 USD | `-0.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4000.52` | `4001.18` | `3995.14` | `4001.00` | `693` | 2,769,257.98 USD | 190,834.78 USD | `+6.89%` | -780,388.50 USD | `+1.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4001.01` | `4003.88` | `3999.56` | `4002.90` | `669` | 2,675,288.79 USD | 249,367.20 USD | `+9.32%` | -531,021.31 USD | `+1.21` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4002.91` | `4003.71` | `4002.91` | `4003.71` | `23` | 91,435.51 USD | -63,034.26 USD | `-68.94%` | -594,055.56 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4008.80` | `4014.92` | `4001.35` | `4002.36` | `667` | 2,671,119.24 USD | -91,693.11 USD | `-3.43%` | -823,707.83 USD | `-0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -1,045,509.48 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4003.88` | `3995.14` | `4003.70` | `1,382` | 5,525,488.56 USD | 366,673.99 USD | `+6.64%` | -678,835.49 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4003.88` | `3995.14` | `4003.71` | `1,384` | 5,535,481.82 USD | 376,667.25 USD | `+6.80%` | 324,575.71 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4003.88` | `3995.14` | `4003.71` | `1,384` | 5,535,481.82 USD | 376,667.25 USD | `+6.80%` | 324,575.71 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `3993.80` | `4.1845` | 16,712.06 USD | 935,157.91 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3993.90` | `6.3839` | 25,496.66 USD | 918,445.85 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3994.00` | `7.9694` | 31,829.78 USD | 892,949.19 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3994.10` | `14.5721` | 58,202.42 USD | 861,119.41 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3994.20` | `11.9616` | 47,777.02 USD | 802,916.99 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3994.30` | `53.2440` | 212,672.51 USD | 755,139.96 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3994.50` | `13.6864` | 54,670.32 USD | 542,467.45 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3994.60` | `0.5285` | 2,111.15 USD | 487,797.13 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3994.70` | `9.3832` | 37,483.07 USD | 485,685.98 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3994.80` | `14.8633` | 59,375.91 USD | 448,202.91 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3994.90` | `30.6108` | 122,287.08 USD | 388,827.00 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3995.00` | `0.9745` | 3,893.13 USD | 266,539.92 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3995.10` | `4.3904` | 17,540.09 USD | 262,646.79 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3995.20` | `10.8857` | 43,490.55 USD | 245,106.70 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3995.30` | `7.0092` | 28,003.86 USD | 201,616.15 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `3995.40` | `0.8615` | 3,442.04 USD | 173,612.30 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3995.50` | `4.1845` | 16,719.17 USD | 170,170.26 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3995.60` | `7.5082` | 29,999.76 USD | 153,451.09 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3995.70` | `9.1214` | 36,446.38 USD | 123,451.33 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `3995.80` | `21.7741` | 87,004.95 USD | 87,004.95 USD | `18 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3995.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,995.85` | `0.00%` | `-` |
| `ASK` | `3995.90` | `0.5067` | 2,024.72 USD | 2,024.72 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `3996.00` | `25.0250` | 99,999.90 USD | 102,024.62 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `3996.10` | `0.7021` | 2,805.66 USD | 104,830.28 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3996.20` | `6.7523` | 26,983.54 USD | 131,813.83 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3996.30` | `5.2554` | 21,002.16 USD | 152,815.98 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3996.40` | `0.4692` | 1,875.11 USD | 154,691.09 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3996.50` | `9.0086` | 36,002.87 USD | 190,693.96 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3996.60` | `3.4310` | 13,712.33 USD | 204,406.30 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3996.70` | `55.2983` | 221,010.72 USD | 425,417.01 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3996.80` | `12.9649` | 51,818.11 USD | 477,235.12 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `3996.90` | `5.3921` | 21,551.68 USD | 498,786.81 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3997.00` | `7.3374` | 29,327.59 USD | 528,114.40 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3997.10` | `19.2808` | 77,067.29 USD | 605,181.68 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3997.20` | `68.0068` | 271,836.78 USD | 877,018.46 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3997.30` | `89.7464` | 358,743.28 USD | 1,235,761.75 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3997.40` | `4.6536` | 18,602.30 USD | 1,254,364.05 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3997.50` | `5.5762` | 22,290.86 USD | 1,276,654.91 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3997.60` | `5.7327` | 22,917.04 USD | 1,299,571.95 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3997.70` | `19.1832` | 76,688.68 USD | 1,376,260.63 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `3997.80` | `0.4690` | 1,874.97 USD | 1,378,135.60 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,935,932.63 USD | `6,489.82` | `4185.46` | `3997.10` | `29515.66` | 1,227,018.38 USD | `+4.73%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,161,364.79 USD | `6,295.38` | `4129.49` | `3997.10` | `13941.61` | 835,368.12 USD | `+3.32%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,458,465.96 USD | `5,869.90` | `4228.86` | `3997.10` | `27142.04` | 1,364,555.97 USD | `+5.82%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,298,243.54 USD | `4,828.91` | `4157.43` | `3997.10` | `2277.09` | -777,638.78 USD | `-4.03%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,182,267.02 USD | `3,548.32` | `4127.94` | `3997.10` | `573.65` | -464,983.33 USD | `-3.28%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,061,087.23 USD | `3,268.21` | `4228.94` | `3997.10` | `4394.42` | 759,991.90 USD | `+5.82%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,589,560.40 USD | `2,900.00` | `4364.92` | `3997.10` | `4235.87` | 1,068,715.93 USD | `+9.22%` | `20X Cross` |
| `263` | `0x3678...b209` | `LONG` | 8,793,180.00 USD | `2,200.00` | `4176.09` | `3997.10` | `2636.88` | -394,239.30 USD | `-4.48%` | `25X Cross` |
| `264` | `0x41e5...0825` | `SHORT` | 8,791,200.00 USD | `2,200.00` | `4112.20` | `3997.10` | `4331.35` | 255,654.59 USD | `+2.91%` | `20X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,894,365.07 USD | `1,975.37` | `4048.55` | `3997.10` | `6576.11` | 103,026.64 USD | `+1.31%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,314,119.37 USD | `1,579.95` | `4075.62` | `3997.10` | `0.000000` | -125,177.60 USD | `-1.98%` | `1X Cross` |
| `520` | `0x354b...6425` | `LONG` | 4,280,701.50 USD | `1,071.03` | `4004.93` | `3997.10` | `0.000000` | -8,712.74 USD | `-0.20%` | `10X Cross` |
| `561` | `0x63da...8add` | `LONG` | 3,996,400.00 USD | `1,000.00` | `4021.46` | `3997.10` | `3564.32` | -25,060.96 USD | `-0.63%` | `25X Cross` |
| `574` | `0xf3dc...1672` | `LONG` | 3,933,637.85 USD | `984.27` | `4018.39` | `3997.10` | `2881.09` | -21,548.84 USD | `-0.55%` | `20X Cross` |
| `585` | `0x9aa5...58af` | `LONG` | 3,882,487.10 USD | `971.64` | `4279.98` | `3997.10` | `0.000000` | -276,121.98 USD | `-7.11%` | `20X Cross` |
| `670` | `0x4a20...3c26` | `LONG` | 3,346,919.12 USD | `837.40` | `4599.73` | `3997.10` | `0.000000` | -504,901.26 USD | `-15.09%` | `20X Cross` |
| `823` | `0x0fac...7a0a` | `LONG` | 2,743,811.90 USD | `686.49` | `4290.34` | `3997.10` | `1247.85` | -201,446.81 USD | `-7.34%` | `25X Cross` |
| `912` | `0x625e...a354` | `SHORT` | 2,477,520.00 USD | `620.00` | `4122.81` | `3997.10` | `4342.45` | 78,627.03 USD | `+3.17%` | `20X Cross` |
| `915` | `0xd8c5...99b0` | `SHORT` | 2,471,502.70 USD | `618.35` | `4175.35` | `3997.10` | `34168.47` | 110,349.90 USD | `+4.46%` | `4X Cross` |
| `937` | `0xeae3...e8ad` | `SHORT` | 2,398,140.00 USD | `600.00` | `4104.77` | `3997.10` | `4325.47` | 64,725.11 USD | `+2.70%` | `20X Cross` |
| `939` | `0xf285...fa82` | `LONG` | 2,390,270.42 USD | `598.11` | `4146.45` | `3997.10` | `3891.45` | -89,749.13 USD | `-3.75%` | `25X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,340,334.60 USD | `585.61` | `4082.77` | `3997.10` | `2629.92` | -50,582.38 USD | `-2.16%` | `10X Cross` |
| `1097` | `0x413c...886c` | `LONG` | 1,998,200.00 USD | `500.00` | `4010.43` | `3997.10` | `0.000000` | -7,016.23 USD | `-0.35%` | `2X Cross` |
| `1102` | `0x61ce...a62b` | `SHORT` | 1,988,421.99 USD | `497.50` | `4071.66` | `3997.10` | `4717.73` | 37,246.80 USD | `+1.87%` | `20X Cross` |
| `1176` | `0x2edd...8179` | `LONG` | 1,881,102.63 USD | `469.89` | `4164.68` | `4004.47` | `0.000000` | -75,829.89 USD | `-4.03%` | `10X Cross` |
| `1220` | `0xead5...69f2` | `LONG` | 1,813,229.71 USD | `453.78` | `4220.88` | `3997.10` | `3539.15` | -102,138.35 USD | `-5.63%` | `5X Isolated` |
| `1283` | `0x7a6d...f79c` | `SHORT` | 1,715,062.02 USD | `428.38` | `4136.09` | `4004.47` | `5213.30` | 56,752.99 USD | `+3.31%` | `10X Cross` |
| `1290` | `0x46fc...1195` | `LONG` | 1,694,321.37 USD | `423.95` | `4053.27` | `3997.10` | `2154.81` | -24,068.70 USD | `-1.42%` | `20X Cross` |
| `1360` | `0x6d15...d374` | `LONG` | 1,598,560.00 USD | `400.00` | `4068.25` | `3997.10` | `3842.02` | -28,740.00 USD | `-1.80%` | `25X Cross` |
| `1361` | `0xee02...309d` | `SHORT` | 1,598,560.00 USD | `400.00` | `4438.84` | `3997.10` | `4227.09` | 176,978.60 USD | `+11.07%` | `25X Isolated` |
| `1402` | `0x51f6...2b39` | `LONG` | 1,562,943.37 USD | `390.33` | `4228.91` | `4004.47` | `591.02` | -87,709.72 USD | `-5.61%` | `10X Cross` |
| `1405` | `0x02a7...fe9f` | `SHORT` | 1,558,596.00 USD | `390.00` | `4055.02` | `3997.10` | `4306.91` | 22,863.25 USD | `+1.47%` | `25X Cross` |
| `1448` | `0x7e77...b8d2` | `SHORT` | 1,518,822.00 USD | `380.00` | `4131.92` | `3997.10` | `4293.71` | 51,307.64 USD | `+3.38%` | `20X Cross` |
| `1463` | `0x9c06...0560` | `LONG` | 1,491,699.86 USD | `373.26` | `4018.98` | `3997.10` | `0.000000` | -8,431.94 USD | `-0.57%` | `25X Cross` |
| `1465` | `0x72c2...9b37` | `LONG` | 1,491,219.24 USD | `373.13` | `4000.98` | `3997.10` | `3778.25` | -1,674.28 USD | `-0.11%` | `13X Isolated` |
| `1503` | `0x781e...96b7` | `SHORT` | 1,445,956.66 USD | `361.11` | `4363.51` | `4004.47` | `13202.55` | 129,749.98 USD | `+8.97%` | `10X Cross` |
| `1510` | `0xaa44...b844` | `LONG` | 1,438,560.00 USD | `360.00` | `4043.10` | `3997.10` | `2818.46` | -16,957.63 USD | `-1.18%` | `4X Cross` |
| `1625` | `0xa41f...d50a` | `LONG` | 1,314,664.14 USD | `328.96` | `4468.89` | `3997.10` | `3802.38` | -155,433.72 USD | `-11.82%` | `15X Cross` |
| `1635` | `0x7fda...17d1` | `SHORT` | 1,302,613.69 USD | `325.91` | `4013.13` | `3997.10` | `30408.48` | 5,289.86 USD | `+0.41%` | `20X Cross` |
| `1668` | `0xbf5a...88ba` | `SHORT` | 1,269,476.04 USD | `317.65` | `4091.80` | `3997.10` | `9811.86` | 30,306.99 USD | `+2.39%` | `20X Cross` |
| `1703` | `0xff31...ff6c` | `SHORT` | 1,239,039.00 USD | `310.00` | `4372.43` | `3997.10` | `4789.38` | 116,416.38 USD | `+9.40%` | `10X Isolated` |
| `1732` | `0xada6...6f88` | `LONG` | 1,213,020.01 USD | `303.50` | `4166.46` | `3997.10` | `1784.93` | -51,492.86 USD | `-4.25%` | `5X Cross` |
| `1890` | `0x50e2...d770` | `LONG` | 1,080,631.46 USD | `270.37` | `4243.58` | `3997.10` | `2562.31` | -66,695.00 USD | `-6.17%` | `20X Cross` |
| `1909` | `0x4c92...4f17` | `SHORT` | 1,065,921.81 USD | `266.72` | `4260.98` | `3997.10` | `6513.37` | 70,570.43 USD | `+6.62%` | `20X Cross` |
| `1984` | `0xd346...c4f3` | `LONG` | 1,019,776.57 USD | `255.17` | `4188.66` | `3997.10` | `3310.63` | -49,059.93 USD | `-4.81%` | `5X Isolated` |

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
| `7D` | `Long Liquidation` | `3611.30` | 16,240,000.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,170,000.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.40` | 3,900,000.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,030,000.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.50` | 3,870,000.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 15,960,000.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.60` | 3,790,000.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,870,000.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.70` | 3,740,000.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,680,000.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.80` | 3,700,000.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,570,000.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.90` | 3,670,000.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,440,000.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.00` | 3,630,000.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,370,000.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.10` | 3,610,000.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,330,000.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.20` | 3,600,000.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,310,000.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.30` | 3,590,000.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,280,000.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,250,000.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,220,000.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,210,000.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,850,000.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,360,000.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,830,000.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.10` | 3,580,000.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,510,000.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.20` | 3,580,000.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,200,000.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.30` | 3,490,000.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,910,000.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.40` | 3,350,000.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,650,000.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,120,000.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,110,000.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.60` | 2,940,000.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,710,000.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.70` | 2,780,000.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,170,000.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.80` | 2,700,000.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,830,000.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.90` | 2,550,000.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,690,000.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.00` | 2,510,000.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,580,000.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.10` | 2,480,000.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,450,000.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.20` | 2,440,000.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,340,000.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.30` | 2,400,000.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,250,000.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,210,000.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,160,000.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,140,000.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,410,000.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,460,000.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,570,000.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.10` | 2,390,000.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,730,000.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.20` | 2,320,000.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,270,000.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.30` | 2,150,000.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,600,000.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,790,000.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,110,000.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.50` | 1,360,000.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,140,000.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 955,040.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.70` | 752,230.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.80` | 487,860.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.90` | 298,610.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.00` | 243,280.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.10` | 167,990.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.20` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.30` | 23,310.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 300.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.40` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD |
| `7D` | `3619.70` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3622.50` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD |
| `7D` | `3623.90` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3626.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3628.10` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3630.70` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD |
| `7D` | `3632.30` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3634.80` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD |
| `7D` | `3636.50` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3638.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `3640.70` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.00` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3644.90` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `3649.10` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.20` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `3653.30` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.30` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,850,000.00 USD | 0.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.10` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD |
| `7D` | `3854.90` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.20` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `3859.10` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD |
| `1D` | `3860.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD |
| `7D` | `3863.30` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD |
| `1D` | `3864.40` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD |
| `7D` | `3867.50` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3868.50` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD |
| `7D` | `3871.70` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3872.60` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3875.90` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3876.70` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3880.10` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3880.80` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD |
| `7D` | `3884.30` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3884.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3888.50` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.00` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3892.70` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.10` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `3896.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.20` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `3901.10` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.30` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.10` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD |
| `7D` | `3938.90` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD |
| `1D` | `3942.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD |
| `7D` | `3943.10` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD |
| `1D` | `3946.40` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD |
| `7D` | `3947.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD |
| `1D` | `3950.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD |
| `7D` | `3951.50` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.60` | 955,040.00 USD | 0.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3958.70` | 752,230.00 USD | 0.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3962.80` | 487,860.00 USD | 0.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3966.90` | 298,610.00 USD | 0.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.00` | 243,280.00 USD | 0.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.10` | 167,990.00 USD | 0.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.20` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.30` | 23,310.00 USD | 0.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 0.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 0.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD |
| `7D` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD |
| `1D` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 0.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD |
| `7D` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD |
| `1D` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD |
| `7D` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD |
| `7D` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD |
| `7D` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD |
| `7D` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD |
| `7D` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD |
| `7D` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD |
| `1D` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD |
| `7D` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD |
| `7D` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD |
| `7D` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 300.94 USD |
| `7D` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD |
| `1D` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD |
| `7D` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD |
| `7D` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD |
| `7D` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `276.67M` | Total OI Tokens: `69,088.2 PAXG`
  * 1h OI Change: `+0.45%` | 4h OI Change: `+0.81%` | 24h OI Change: `+1.10%`
  * Exchange Breakdown: Binance=`107.45M` | Bybit=`21.98M` | OKX=`-` | Hyperliquid=`24.72M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.61K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `24.85%` | `75.15%` | `0.33` | 1,970,000.00 USD |
| `15M` | `Binance` | `43.37%` | `56.63%` | `0.77` | 227,980.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `50.26%` | `49.74%` | `1.01` | 204,830.00 USD |
| `15M` | `KuCoin` | `35.86%` | `64.14%` | `0.56` | 8,280.00 USD |
| `15M` | `Gate` | `63.05%` | `36.95%` | `1.71` | 114,110.00 USD |
| `15M` | `Bitget` | `22.99%` | `77.01%` | `0.30` | 92,250.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `7.67%` | `92.33%` | `0.08` | 1,100,000.00 USD |
| `15M` | `Bitunix` | `65.36%` | `34.64%` | `1.89` | 35,230.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.98%` | `43.02%` | `1.32` | 116,960.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `27.1%` | `72.9%` | `0.37` | 62,020.00 USD |
| `15M` | `HTX` | `7.74%` | `92.26%` | `0.08` | 4,440.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `43.37%` | `56.63%` | `0.77` | 227,980.00 USD |
| `15M` | `Global Accounts` | `24.85%` | `75.15%` | `0.33` | 1,970,000.00 USD |
| `1H` | `PAXG` | `28.63%` | `71.37%` | `0.40` | 10,760,000.00 USD |
| `1H` | `Binance` | `39.9%` | `60.1%` | `0.66` | 5,000,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 1,700,000.00 USD |
| `1H` | `Bybit` | `48.9%` | `51.1%` | `0.96` | 1,130,000.00 USD |
| `1H` | `KuCoin` | `66.92%` | `33.08%` | `2.02` | 106,600.00 USD |
| `1H` | `Gate` | `46.65%` | `53.35%` | `0.87` | 423,620.00 USD |
| `1H` | `Bitget` | `42.54%` | `57.46%` | `0.74` | 474,440.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 347,400.00 USD |
| `1H` | `MEXC` | `9.98%` | `90.02%` | `0.11` | 515,000.00 USD |
| `1H` | `Bitunix` | `63.92%` | `36.08%` | `1.77` | 261,690.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 177,220.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.12%` | `47.88%` | `1.09` | 484,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 3,480.00 USD |
| `1H` | `WhiteBIT` | `26.41%` | `73.59%` | `0.36` | 113,840.00 USD |
| `1H` | `HTX` | `93.67%` | `6.33%` | `14.80` | 4,910.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 5,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 9,520.00 USD |
| `1H` | `Whale Positions` | `39.9%` | `60.1%` | `0.66` | 5,000,000.00 USD |
| `1H` | `Global Accounts` | `28.63%` | `71.37%` | `0.40` | 10,760,000.00 USD |
| `4H` | `PAXG` | `40.05%` | `59.95%` | `0.67` | 55,080,000.00 USD |
| `4H` | `Binance` | `48.97%` | `51.03%` | `0.96` | 9,600,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `43.36%` | `56.64%` | `0.77` | 6,340,000.00 USD |
| `4H` | `KuCoin` | `49.37%` | `50.63%` | `0.98` | 386,760.00 USD |
| `4H` | `Gate` | `46.11%` | `53.89%` | `0.86` | 2,220,000.00 USD |
| `4H` | `Bitget` | `48.23%` | `51.77%` | `0.93` | 3,800,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `31.77%` | `68.23%` | `0.47` | 25,130,000.00 USD |
| `4H` | `Bitunix` | `50.59%` | `49.41%` | `1.02` | 1,450,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.65%` | `45.35%` | `1.21` | 4,320,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `19.74%` | `80.26%` | `0.25` | 1,580,000.00 USD |
| `4H` | `HTX` | `85.84%` | `14.16%` | `6.06` | 168,600.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `30.87%` | `69.13%` | `0.45` | 74,000.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `48.97%` | `51.03%` | `0.96` | 9,600,000.00 USD |
| `4H` | `Global Accounts` | `40.05%` | `59.95%` | `0.67` | 55,080,000.00 USD |


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
| `5m` | 17,990.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | 103,330.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `30m` | 66,250.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1h` | 45,840.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `2h` | -115,040.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -126,970.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | 394,640.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `8h` | -1,080,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,640,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,130,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,410,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,720,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+17.99K` | 15m=`+103.33K` | 1h=`+45.84K` | 24h=`-1.13M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3996.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3987.70` (Risk Distance: `9.29` pts)
  * +2.5R Take Profit: `4020.21`
  * Mathematical Lot Sizing: **`1.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.33` (Risk Distance: `9.29` pts)
  * +2.5R Take Profit: `3989.82`
  * Mathematical Lot Sizing: **`1.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4026.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
