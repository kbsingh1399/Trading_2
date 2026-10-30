# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3988.32` | **Live Ask Quote**: `3988.41` | **Mid Price**: `3988.36`
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
  * Session VWAP: `4002.72` | VWAP Z-Score: `-1.88` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `8.20` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.95` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4020.61` | Lower -3.00σ Band: `3984.84`
  * Upper +2.51σ Band: `4017.68` | Lower -2.51σ Band: `3987.76`
  * Upper +2.01σ Band: `4014.70` | Lower -2.01σ Band: `3990.74`
  * Upper +2.00σ Band: `4014.64` | Lower -2.00σ Band: `3990.80`
  * Upper +1.28σ Band: `4010.35` | Lower -1.28σ Band: `3995.09`
  * Upper +1.00σ Band: `4008.68` | Lower -1.00σ Band: `3996.76`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3997.73` | EMA-20=`4000.39` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4008.15` (Slope: `+0.0000`) | EMA-100=`4017.00`
  * Institutional Anchors: EMA-144=`4021.42` | EMA-200=`4024.24` (Slope: `-0.0884`) | EMA-233=`4026.34`
- **Range Boundaries**: 24H High=`4046.38` | 24H Low=`3987.44` | Weekly High=`4082.75` | Weekly Low=`3987.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.29` (Distance: `-0.64%`)
  * Point of Control (POC) = `4006.91` (Distance: `-0.48%`)
  * Value Area Low (VAL) = `3996.37` (Distance: `-0.22%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4003.61`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3987.36`
  * New York Session (13:00-21:00 UTC): High=`4012.30` | Low=`3964.43`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3972.41` - `4004.32`
  * Optimal Trade Entry (OTE 0.705): `3996.34`
  * Structural Invalidation Anchor (0.786): `4020.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3999.19` | `3999.99` | `3995.95` | `3996.70` | `44` | 174,960.12 USD | -4,158.66 USD | `-2.38%` | 100,496.97 USD | `-0.17` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `3996.70` | `3998.69` | `3995.98` | `3997.54` | `28` | 113,498.42 USD | 15,061.82 USD | `+13.27%` | 115,558.79 USD | `+0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `3997.55` | `3997.93` | `3996.48` | `3996.48` | `11` | 44,739.82 USD | -12,843.19 USD | `-28.71%` | 102,715.60 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4013.80` | `4017.75` | `4009.35` | `4009.60` | `178` | 714,070.12 USD | -22,842.64 USD | `-3.20%` | 127,655.24 USD | `-0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4009.59` | `4010.96` | `3996.68` | `3999.18` | `146` | 583,042.52 USD | -22,999.61 USD | `-3.94%` | 104,655.63 USD | `-0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `3999.19` | `3999.99` | `3995.95` | `3996.62` | `84` | 337,114.77 USD | 521.68 USD | `+0.15%` | 105,177.31 USD | `-0.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4002.94` | `1,790` | 7,158,366.15 USD | 437,268.83 USD | `+6.11%` | -211,673.79 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4002.94` | `4017.75` | `3996.68` | `3999.18` | `841` | 3,369,805.34 USD | 241,421.30 USD | `+7.16%` | 29,747.51 USD | `+0.45` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3999.19` | `3999.99` | `3995.95` | `3996.62` | `84` | 337,114.77 USD | 521.68 USD | `+0.15%` | 30,269.20 USD | `-0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3995.14` | `3996.62` | `2,715` | 10,865,418.15 USD | 679,079.93 USD | `+6.25%` | 626,988.39 USD | `+0.74` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3995.14` | `3996.62` | `2,715` | 10,865,418.15 USD | 679,079.93 USD | `+6.25%` | 626,988.39 USD | `+0.74` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `3988.20` | `6.0279` | 24,040.47 USD | 493,079.60 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3988.30` | `0.3157` | 1,259.11 USD | 469,039.13 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3988.40` | `2.6287` | 10,484.31 USD | 467,780.02 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3988.50` | `15.1081` | 60,258.66 USD | 457,295.71 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3988.60` | `4.2627` | 17,002.21 USD | 397,037.06 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3988.70` | `7.3078` | 29,148.62 USD | 380,034.85 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3988.80` | `24.8166` | 98,988.45 USD | 350,886.23 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3988.90` | `8.0188` | 31,986.19 USD | 251,897.77 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3989.00` | `2.9509` | 11,771.14 USD | 219,911.58 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3989.10` | `4.2631` | 17,005.93 USD | 208,140.44 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3989.20` | `9.6667` | 38,562.40 USD | 191,134.51 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3989.40` | `0.5390` | 2,150.29 USD | 152,572.11 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3989.50` | `0.0720` | 287.24 USD | 150,421.82 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3989.60` | `2.6029` | 10,384.53 USD | 150,134.58 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3989.70` | `6.4867` | 25,879.99 USD | 139,750.05 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3989.80` | `3.7595` | 14,999.65 USD | 113,870.06 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3989.90` | `5.2621` | 20,995.25 USD | 98,870.41 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3990.00` | `8.8285` | 35,225.71 USD | 77,875.16 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3990.10` | `0.4022` | 1,604.82 USD | 42,649.44 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3990.30` | `10.2861` | 41,044.62 USD | 41,044.62 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3990.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,990.35` | `0.00%` | `-` |
| `ASK` | `3990.40` | `107.2128` | 427,821.96 USD | 427,821.96 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `3990.50` | `5.6836` | 22,680.41 USD | 450,502.36 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `3990.70` | `80.6890` | 322,005.59 USD | 772,507.96 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3990.80` | `31.1780` | 124,425.16 USD | 896,933.12 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `3991.00` | `0.0620` | 247.44 USD | 897,180.56 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `3991.10` | `60.8065` | 242,684.82 USD | 1,139,865.38 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3991.20` | `9.2693` | 36,995.63 USD | 1,176,861.01 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3991.30` | `8.8723` | 35,412.01 USD | 1,212,273.02 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3991.40` | `10.9428` | 43,677.09 USD | 1,255,950.11 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3991.50` | `4.7750` | 19,059.41 USD | 1,275,009.53 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3991.60` | `26.1961` | 104,564.35 USD | 1,379,573.88 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `3991.70` | `5.2611` | 21,000.73 USD | 1,400,574.61 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `3991.80` | `23.1172` | 92,279.24 USD | 1,492,853.85 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3991.90` | `14.5031` | 57,894.92 USD | 1,550,748.78 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3992.00` | `3.6353` | 14,512.12 USD | 1,565,260.89 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3992.10` | `10.9067` | 43,540.64 USD | 1,608,801.53 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3992.20` | `5.5761` | 22,260.91 USD | 1,631,062.44 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `3992.40` | `29.2088` | 116,613.21 USD | 1,747,675.65 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `3992.60` | `11.9934` | 47,884.85 USD | 1,795,560.50 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `3992.70` | `5.3759` | 21,464.36 USD | 1,817,024.86 USD | `2 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 25,900,238.60 USD | `6,489.82` | `4185.46` | `3990.80` | `29393.84` | 1,262,712.41 USD | `+4.88%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,259,422.58 USD | `6,329.25` | `4128.54` | `3990.80` | `13998.90` | 871,173.16 USD | `+3.45%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,426,181.52 USD | `5,869.90` | `4228.86` | `3990.80` | `27046.80` | 1,396,840.42 USD | `+5.96%` | `5X Cross` |
| `102` | `0xec0b...b078` | `LONG` | 19,271,684.55 USD | `4,828.91` | `4157.43` | `3990.80` | `2271.65` | -804,197.77 USD | `-4.17%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,164,983.98 USD | `3,549.32` | `4127.81` | `3990.80` | `621.07` | -485,966.19 USD | `-3.43%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,043,112.06 USD | `3,268.21` | `4228.94` | `3990.80` | `4375.02` | 777,967.07 USD | `+5.96%` | `25X Cross` |
| `183` | `0xa742...e390` | `SHORT` | 11,374,069.39 USD | `2,850.00` | `4364.75` | `3990.80` | `4241.57` | 1,065,497.64 USD | `+9.37%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,779,980.00 USD | `2,200.00` | `4176.09` | `3990.80` | `2613.65` | -407,439.30 USD | `-4.64%` | `25X Cross` |
| `265` | `0x41e5...0825` | `SHORT` | 8,779,980.00 USD | `2,200.00` | `4112.20` | `3990.80` | `4331.43` | 266,874.59 USD | `+3.04%` | `20X Cross` |
| `300` | `0xacb6...efbd` | `SHORT` | 7,883,500.54 USD | `1,975.37` | `4048.55` | `3990.80` | `6630.41` | 113,891.17 USD | `+1.44%` | `6X Cross` |
| `369` | `0xc26c...b8f4` | `LONG` | 6,305,429.64 USD | `1,579.95` | `4075.62` | `3990.80` | `0.000000` | -133,867.33 USD | `-2.12%` | `1X Cross` |
| `563` | `0x63da...8add` | `LONG` | 3,990,900.00 USD | `1,000.00` | `4021.46` | `3990.80` | `3564.40` | -30,560.96 USD | `-0.77%` | `25X Cross` |
| `580` | `0xf3dc...1672` | `LONG` | 3,928,224.36 USD | `984.27` | `4018.39` | `3990.80` | `2904.08` | -26,962.33 USD | `-0.69%` | `20X Cross` |
| `588` | `0x9aa5...58af` | `LONG` | 3,877,726.06 USD | `971.64` | `4279.98` | `3990.80` | `0.000000` | -280,883.03 USD | `-7.24%` | `20X Cross` |
| `627` | `0x354b...6425` | `LONG` | 3,597,737.68 USD | `901.49` | `4004.93` | `3990.80` | `0.000000` | -12,652.26 USD | `-0.35%` | `10X Cross` |
| `675` | `0x4a20...3c26` | `LONG` | 3,341,978.46 USD | `837.40` | `4599.73` | `3990.80` | `0.000000` | -509,841.92 USD | `-15.26%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,739,692.99 USD | `686.49` | `4290.34` | `3990.80` | `1182.67` | -205,565.72 USD | `-7.50%` | `25X Cross` |
| `906` | `0x625e...a354` | `SHORT` | 2,474,358.00 USD | `620.00` | `4122.81` | `3990.80` | `4342.53` | 81,789.03 USD | `+3.31%` | `20X Cross` |
| `909` | `0xd8c5...99b0` | `SHORT` | 2,467,792.57 USD | `618.35` | `4175.35` | `3990.80` | `34259.09` | 114,060.03 USD | `+4.62%` | `4X Cross` |
| `930` | `0xeae3...e8ad` | `SHORT` | 2,394,600.00 USD | `600.00` | `4104.77` | `3990.80` | `4325.55` | 68,265.11 USD | `+2.85%` | `20X Cross` |
| `932` | `0xf285...fa82` | `LONG` | 2,386,980.84 USD | `598.11` | `4146.45` | `3990.80` | `3891.53` | -93,038.72 USD | `-3.90%` | `25X Cross` |
| `952` | `0x12f7...8750` | `LONG` | 2,337,113.74 USD | `585.61` | `4082.77` | `3990.80` | `2610.30` | -53,803.24 USD | `-2.30%` | `10X Cross` |
| `1092` | `0x413c...886c` | `LONG` | 1,995,500.00 USD | `500.00` | `4010.43` | `3990.80` | `0.000000` | -9,716.23 USD | `-0.49%` | `2X Cross` |
| `1100` | `0x9c06...0560` | `LONG` | 1,989,133.60 USD | `498.42` | `4012.76` | `3990.80` | `0.000000` | -10,897.90 USD | `-0.55%` | `25X Cross` |
| `1106` | `0x61ce...a62b` | `SHORT` | 1,985,536.47 USD | `497.50` | `4071.66` | `3990.80` | `4716.29` | 40,132.32 USD | `+2.02%` | `20X Cross` |
| `1174` | `0x2edd...8179` | `LONG` | 1,878,287.06 USD | `469.89` | `4164.68` | `3997.80` | `0.000000` | -78,645.46 USD | `-4.19%` | `10X Cross` |
| `1217` | `0xead5...69f2` | `LONG` | 1,811,006.17 USD | `453.78` | `4220.88` | `3990.80` | `3539.23` | -104,361.89 USD | `-5.76%` | `5X Isolated` |
| `1277` | `0x7a6d...f79c` | `SHORT` | 1,712,445.05 USD | `428.38` | `4136.09` | `3997.80` | `5358.25` | 59,369.95 USD | `+3.47%` | `10X Cross` |
| `1310` | `0x46fc...1195` | `LONG` | 1,653,122.17 USD | `414.22` | `4053.27` | `3990.80` | `2160.93` | -25,836.05 USD | `-1.56%` | `20X Cross` |
| `1344` | `0x6d15...d374` | `LONG` | 1,596,360.00 USD | `400.00` | `4068.25` | `3990.80` | `3842.10` | -30,940.00 USD | `-1.94%` | `25X Cross` |
| `1345` | `0xee02...309d` | `SHORT` | 1,596,360.00 USD | `400.00` | `4438.84` | `3990.80` | `4227.17` | 179,178.60 USD | `+11.22%` | `25X Isolated` |
| `1386` | `0x51f6...2b39` | `LONG` | 1,564,902.15 USD | `391.48` | `4228.25` | `3997.80` | `540.43` | -90,373.54 USD | `-5.78%` | `10X Cross` |
| `1389` | `0x02a7...fe9f` | `SHORT` | 1,556,451.00 USD | `390.00` | `4055.02` | `3990.80` | `4306.98` | 25,008.25 USD | `+1.61%` | `25X Cross` |
| `1431` | `0x7e77...b8d2` | `SHORT` | 1,516,542.00 USD | `380.00` | `4131.92` | `3990.80` | `4293.79` | 53,587.64 USD | `+3.53%` | `20X Cross` |
| `1452` | `0x72c2...9b37` | `LONG` | 1,489,167.02 USD | `373.13` | `4000.98` | `3990.80` | `3778.33` | -3,726.50 USD | `-0.25%` | `13X Isolated` |
| `1491` | `0x781e...96b7` | `SHORT` | 1,447,236.04 USD | `361.99` | `4362.63` | `3997.80` | `13035.35` | 131,996.75 USD | `+9.12%` | `10X Cross` |
| `1501` | `0xaa44...b844` | `LONG` | 1,436,760.00 USD | `360.00` | `4043.10` | `3990.80` | `2820.31` | -18,757.63 USD | `-1.31%` | `4X Cross` |
| `1607` | `0xa41f...d50a` | `LONG` | 1,312,854.84 USD | `328.96` | `4468.89` | `3990.80` | `3802.46` | -157,243.01 USD | `-11.98%` | `15X Cross` |
| `1659` | `0xbf5a...88ba` | `SHORT` | 1,267,728.94 USD | `317.65` | `4091.80` | `3990.80` | `10002.07` | 32,054.09 USD | `+2.53%` | `20X Cross` |
| `1693` | `0xff31...ff6c` | `SHORT` | 1,237,179.00 USD | `310.00` | `4372.43` | `3990.80` | `4789.46` | 118,276.38 USD | `+9.56%` | `10X Isolated` |
| `1711` | `0x7fda...17d1` | `SHORT` | 1,213,881.32 USD | `304.16` | `4013.13` | `3990.80` | `31968.25` | 6,761.91 USD | `+0.56%` | `20X Cross` |
| `1715` | `0xada6...6f88` | `LONG` | 1,211,259.72 USD | `303.50` | `4166.46` | `3990.80` | `1794.53` | -53,253.14 USD | `-4.40%` | `5X Cross` |
| `1873` | `0x50e2...d770` | `LONG` | 1,079,009.26 USD | `270.37` | `4243.58` | `3990.80` | `2562.39` | -68,317.20 USD | `-6.33%` | `20X Cross` |
| `1887` | `0x4c92...4f17` | `SHORT` | 1,064,454.84 USD | `266.72` | `4260.98` | `3990.80` | `6505.41` | 72,037.39 USD | `+6.77%` | `20X Cross` |
| `1966` | `0xd346...c4f3` | `LONG` | 1,018,373.12 USD | `255.17` | `4188.66` | `3990.80` | `3310.71` | -50,463.39 USD | `-4.96%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4084.50` (Vol: 319,200.00 USD, Dist: `+1.79%`) | Long MP=`3949.61` (Vol: 346,900.00 USD, Dist: `--1.57%`)
  * 48H Horizon: Short MP=`4097.67` (Vol: 378,100.00 USD, Dist: `+2.12%`) | Long MP=`3936.55` (Vol: 378,100.00 USD, Dist: `--1.89%`)
  * 3D Horizon: Short MP=`4097.67` (Vol: 405,200.00 USD, Dist: `+2.12%`) | Long MP=`3936.55` (Vol: 405,200.00 USD, Dist: `--1.89%`)
  * 7D Horizon: Short MP=`4086.63` (Vol: 910,300.00 USD, Dist: `+1.85%`) | Long MP=`3923.02` (Vol: 1,000,000.00 USD, Dist: `--2.23%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3596.30` | 16,150,000.00 USD | 16,150,000.00 USD | 44,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.60` | 16,110,000.00 USD | 16,110,000.00 USD | 150,420.00 USD | 0.00 USD | 32,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3601.80` | 4,800,000.00 USD | 4,800,000.00 USD | 22,150.00 USD | 0.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.90` | 15,920,000.00 USD | 15,920,000.00 USD | 186,450.00 USD | 0.00 USD | 62,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.00` | 4,750,000.00 USD | 4,750,000.00 USD | 58,500.00 USD | 0.00 USD | 24,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.20` | 15,670,000.00 USD | 15,670,000.00 USD | 140,620.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.20` | 4,670,000.00 USD | 4,670,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.50` | 15,500,000.00 USD | 15,500,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.40` | 4,640,000.00 USD | 4,640,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.80` | 15,390,000.00 USD | 15,390,000.00 USD | 114,410.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.60` | 4,600,000.00 USD | 4,600,000.00 USD | 34,170.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3622.10` | 15,270,000.00 USD | 15,270,000.00 USD | 59,230.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.80` | 4,560,000.00 USD | 4,560,000.00 USD | 73,510.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.40` | 15,190,000.00 USD | 15,190,000.00 USD | 75,590.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.00` | 4,470,000.00 USD | 4,470,000.00 USD | 36,020.00 USD | 0.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.70` | 15,100,000.00 USD | 15,100,000.00 USD | 86,080.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.20` | 4,430,000.00 USD | 4,430,000.00 USD | 28,950.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3635.00` | 15,000,000.00 USD | 15,000,000.00 USD | 44,190.00 USD | 0.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.40` | 4,400,000.00 USD | 4,400,000.00 USD | 12,560.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.30` | 14,950,000.00 USD | 14,950,000.00 USD | 42,820.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.60` | 4,380,000.00 USD | 4,380,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.60` | 14,900,000.00 USD | 14,900,000.00 USD | 22,390.00 USD | 0.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.90` | 14,860,000.00 USD | 14,860,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.20` | 14,830,000.00 USD | 14,830,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.50` | 14,800,000.00 USD | 14,800,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.80` | 14,760,000.00 USD | 14,760,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.10` | 14,740,000.00 USD | 14,740,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.40` | 14,730,000.00 USD | 14,730,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.80` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3837.10` | 14,720,000.00 USD | 14,720,000.00 USD | 212,590.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3841.20` | 4,380,000.00 USD | 4,380,000.00 USD | 63,550.00 USD | 0.00 USD | 74,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.40` | 14,500,000.00 USD | 14,500,000.00 USD | 554,480.00 USD | 0.00 USD | 111,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3845.40` | 4,240,000.00 USD | 4,240,000.00 USD | 190,490.00 USD | 0.00 USD | 82,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.70` | 13,830,000.00 USD | 13,830,000.00 USD | 499,670.00 USD | 0.00 USD | 183,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3849.60` | 3,970,000.00 USD | 3,970,000.00 USD | 35,100.00 USD | 0.00 USD | 26,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.00` | 13,150,000.00 USD | 13,150,000.00 USD | 442,940.00 USD | 0.00 USD | 87,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3853.80` | 3,910,000.00 USD | 3,910,000.00 USD | 115,420.00 USD | 0.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.30` | 12,620,000.00 USD | 12,620,000.00 USD | 311,860.00 USD | 0.00 USD | 67,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.00` | 3,760,000.00 USD | 3,760,000.00 USD | 96,590.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.60` | 12,240,000.00 USD | 12,240,000.00 USD | 322,600.00 USD | 0.00 USD | 19,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.20` | 3,640,000.00 USD | 3,640,000.00 USD | 176,170.00 USD | 0.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.90` | 11,890,000.00 USD | 11,890,000.00 USD | 196,060.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.40` | 3,430,000.00 USD | 3,430,000.00 USD | 199,300.00 USD | 0.00 USD | 28,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.20` | 11,640,000.00 USD | 11,640,000.00 USD | 246,970.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.60` | 3,200,000.00 USD | 3,200,000.00 USD | 131,660.00 USD | 0.00 USD | 17,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.50` | 11,340,000.00 USD | 11,340,000.00 USD | 260,720.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3874.80` | 3,050,000.00 USD | 3,050,000.00 USD | 73,180.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.80` | 11,040,000.00 USD | 11,040,000.00 USD | 297,370.00 USD | 0.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.00` | 2,960,000.00 USD | 2,960,000.00 USD | 43,430.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 10,710,000.00 USD | 10,710,000.00 USD | 186,600.00 USD | 0.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.20` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.40` | 10,500,000.00 USD | 10,500,000.00 USD | 104,420.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.70` | 10,350,000.00 USD | 10,350,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3893.00` | 10,250,000.00 USD | 10,250,000.00 USD | 122,620.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.30` | 10,120,000.00 USD | 10,120,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.60` | 10,010,000.00 USD | 10,010,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.90` | 9,920,000.00 USD | 9,920,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.20` | 9,840,000.00 USD | 9,840,000.00 USD | 23,110.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.80` | 9,810,000.00 USD | 9,810,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3921.00` | 2,920,000.00 USD | 2,920,000.00 USD | 127,100.00 USD | 0.00 USD | 123,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3923.10` | 8,910,000.00 USD | 8,910,000.00 USD | 1,120,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3925.20` | 2,670,000.00 USD | 2,670,000.00 USD | 371,270.00 USD | 0.00 USD | 179,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.40` | 7,430,000.00 USD | 7,430,000.00 USD | 1,030,000.00 USD | 0.00 USD | 280,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3929.40` | 2,120,000.00 USD | 2,120,000.00 USD | 79,920.00 USD | 0.00 USD | 63,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.70` | 6,120,000.00 USD | 6,120,000.00 USD | 605,700.00 USD | 0.00 USD | 170,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.60` | 1,980,000.00 USD | 1,980,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3936.00` | 5,340,000.00 USD | 5,340,000.00 USD | 823,760.00 USD | 0.00 USD | 104,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3937.80` | 1,720,000.00 USD | 1,720,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.30` | 4,420,000.00 USD | 4,420,000.00 USD | 322,520.00 USD | 0.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.00` | 1,480,000.00 USD | 1,480,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.60` | 4,040,000.00 USD | 4,040,000.00 USD | 465,130.00 USD | 0.00 USD | 148,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.20` | 1,110,000.00 USD | 1,110,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.90` | 3,420,000.00 USD | 3,420,000.00 USD | 539,340.00 USD | 0.00 USD | 51,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.40` | 613,170.00 USD | 613,170.00 USD | 295,490.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.20` | 2,830,000.00 USD | 2,830,000.00 USD | 531,020.00 USD | 0.00 USD | 96,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 277,660.00 USD | 277,660.00 USD | 152,490.00 USD | 0.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.50` | 2,200,000.00 USD | 2,200,000.00 USD | 495,980.00 USD | 0.00 USD | 38,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.80` | 96,480.00 USD | 96,480.00 USD | 82,200.00 USD | 0.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.80` | 1,670,000.00 USD | 1,670,000.00 USD | 287,960.00 USD | 0.00 USD | 67,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.00` | 11,170.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3966.10` | 1,310,000.00 USD | 1,310,000.00 USD | 202,410.00 USD | 0.00 USD | 57,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.40` | 1,050,000.00 USD | 1,050,000.00 USD | 199,830.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.70` | 809,000.00 USD | 809,000.00 USD | 243,340.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3979.00` | 540,980.00 USD | 540,980.00 USD | 293,010.00 USD | 0.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.30` | 229,840.00 USD | 229,840.00 USD | 0.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.60` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.90` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.60` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.90` | 733,530.00 USD | 733,530.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4080.60` | 230,960.00 USD | 230,960.00 USD | 127,100.00 USD | 0.00 USD | 103,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.20` | 2,060,000.00 USD | 2,060,000.00 USD | 1,020,000.00 USD | 0.00 USD | 307,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4084.80` | 787,310.00 USD | 787,310.00 USD | 360,440.00 USD | 0.00 USD | 195,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.50` | 3,370,000.00 USD | 3,370,000.00 USD | 1,020,000.00 USD | 0.00 USD | 290,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4089.00` | 900,890.00 USD | 900,890.00 USD | 76,430.00 USD | 0.00 USD | 37,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.80` | 4,230,000.00 USD | 4,230,000.00 USD | 696,130.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.20` | 1,140,000.00 USD | 1,140,000.00 USD | 157,510.00 USD | 0.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4095.10` | 4,920,000.00 USD | 4,920,000.00 USD | 553,040.00 USD | 0.00 USD | 135,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.40` | 1,390,000.00 USD | 1,390,000.00 USD | 197,620.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.40` | 5,610,000.00 USD | 5,610,000.00 USD | 662,770.00 USD | 0.00 USD | 30,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.60` | 1,730,000.00 USD | 1,730,000.00 USD | 298,260.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.70` | 6,100,000.00 USD | 6,100,000.00 USD | 372,480.00 USD | 0.00 USD | 116,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4105.80` | 2,210,000.00 USD | 2,210,000.00 USD | 405,090.00 USD | 0.00 USD | 70,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4108.00` | 6,680,000.00 USD | 6,680,000.00 USD | 454,830.00 USD | 0.00 USD | 123,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.00` | 2,490,000.00 USD | 2,490,000.00 USD | 247,120.00 USD | 0.00 USD | 37,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.30` | 7,280,000.00 USD | 7,280,000.00 USD | 528,700.00 USD | 0.00 USD | 67,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.20` | 2,770,000.00 USD | 2,770,000.00 USD | 246,100.00 USD | 0.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.60` | 7,780,000.00 USD | 7,780,000.00 USD | 448,400.00 USD | 0.00 USD | 51,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.40` | 2,880,000.00 USD | 2,880,000.00 USD | 99,410.00 USD | 0.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.90` | 8,220,000.00 USD | 8,220,000.00 USD | 404,230.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.60` | 2,920,000.00 USD | 2,920,000.00 USD | 34,710.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.20` | 8,650,000.00 USD | 8,650,000.00 USD | 357,280.00 USD | 0.00 USD | 74,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.50` | 8,820,000.00 USD | 8,820,000.00 USD | 123,140.00 USD | 0.00 USD | 50,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.80` | 9,070,000.00 USD | 9,070,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4138.10` | 9,340,000.00 USD | 9,340,000.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.40` | 9,590,000.00 USD | 9,590,000.00 USD | 232,530.00 USD | 0.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.70` | 9,640,000.00 USD | 9,640,000.00 USD | 34,110.00 USD | 0.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4151.00` | 9,770,000.00 USD | 9,770,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.30` | 9,900,000.00 USD | 9,900,000.00 USD | 120,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.60` | 10,320,000.00 USD | 10,320,000.00 USD | 376,160.00 USD | 0.00 USD | 52,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.40` | 3,020,000.00 USD | 3,020,000.00 USD | 63,550.00 USD | 0.00 USD | 40,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.90` | 11,080,000.00 USD | 11,080,000.00 USD | 572,880.00 USD | 0.00 USD | 184,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.60` | 3,290,000.00 USD | 3,290,000.00 USD | 171,460.00 USD | 0.00 USD | 95,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.20` | 11,690,000.00 USD | 11,690,000.00 USD | 511,580.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.80` | 3,370,000.00 USD | 3,370,000.00 USD | 46,980.00 USD | 0.00 USD | 30,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.50` | 12,060,000.00 USD | 12,060,000.00 USD | 285,980.00 USD | 0.00 USD | 85,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.00` | 3,480,000.00 USD | 3,480,000.00 USD | 74,610.00 USD | 0.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.80` | 12,520,000.00 USD | 12,520,000.00 USD | 401,620.00 USD | 0.00 USD | 52,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.20` | 3,600,000.00 USD | 3,600,000.00 USD | 88,500.00 USD | 0.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4181.10` | 12,700,000.00 USD | 12,700,000.00 USD | 161,260.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.40` | 3,750,000.00 USD | 3,750,000.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.40` | 12,950,000.00 USD | 12,950,000.00 USD | 178,140.00 USD | 0.00 USD | 67,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.60` | 3,950,000.00 USD | 3,950,000.00 USD | 165,300.00 USD | 0.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.70` | 13,260,000.00 USD | 13,260,000.00 USD | 278,400.00 USD | 0.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.80` | 4,130,000.00 USD | 4,130,000.00 USD | 161,350.00 USD | 0.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.00` | 4,270,000.00 USD | 4,270,000.00 USD | 123,920.00 USD | 0.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4194.00` | 13,500,000.00 USD | 13,500,000.00 USD | 207,230.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.20` | 4,340,000.00 USD | 4,340,000.00 USD | 58,980.00 USD | 0.00 USD | 9,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.30` | 13,770,000.00 USD | 13,770,000.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.40` | 4,380,000.00 USD | 4,380,000.00 USD | 38,300.00 USD | 0.00 USD | 510.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.60` | 13,970,000.00 USD | 13,970,000.00 USD | 182,330.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.60` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.90` | 14,170,000.00 USD | 14,170,000.00 USD | 153,500.00 USD | 0.00 USD | 43,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.20` | 14,250,000.00 USD | 14,250,000.00 USD | 62,650.00 USD | 0.00 USD | 21,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.50` | 14,400,000.00 USD | 14,400,000.00 USD | 129,360.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.80` | 14,490,000.00 USD | 14,490,000.00 USD | 78,180.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.10` | 14,610,000.00 USD | 14,610,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.40` | 14,660,000.00 USD | 14,660,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.70` | 14,710,000.00 USD | 14,710,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.00` | 14,730,000.00 USD | 14,730,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.80` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.10` | 14,790,000.00 USD | 14,790,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4399.80` | 4,400,000.00 USD | 4,400,000.00 USD | 11,760.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.40` | 14,920,000.00 USD | 14,920,000.00 USD | 114,050.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.00` | 4,490,000.00 USD | 4,490,000.00 USD | 51,100.00 USD | 0.00 USD | 31,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.70` | 15,150,000.00 USD | 15,150,000.00 USD | 168,350.00 USD | 0.00 USD | 55,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4408.20` | 4,520,000.00 USD | 4,520,000.00 USD | 23,070.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.00` | 15,320,000.00 USD | 15,320,000.00 USD | 142,050.00 USD | 0.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4412.40` | 4,540,000.00 USD | 4,540,000.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.30` | 15,420,000.00 USD | 15,420,000.00 USD | 75,090.00 USD | 0.00 USD | 21,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.60` | 4,570,000.00 USD | 4,570,000.00 USD | 19,970.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.60` | 15,560,000.00 USD | 15,560,000.00 USD | 122,390.00 USD | 0.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.80` | 4,610,000.00 USD | 4,610,000.00 USD | 32,630.00 USD | 0.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.80` | 4,610,000.00 USD | 4,610,000.00 USD | 9,110.00 USD | 0.00 USD | 434.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,600,000.00 USD | 15,600,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.20` | 15,660,000.00 USD | 15,660,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.50` | 15,730,000.00 USD | 15,730,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.80` | 15,800,000.00 USD | 15,800,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.50` | 15,880,000.00 USD | 15,880,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |

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
| `7D` | `3596.30` | 16,150,000.00 USD | 0.00 USD | 16,150,000.00 USD | 44,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3600.60` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 150,420.00 USD | 0.00 USD | 32,290.00 USD |
| `1D` | `3601.80` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 22,150.00 USD | 0.00 USD | 26,430.00 USD |
| `7D` | `3604.90` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 186,450.00 USD | 0.00 USD | 62,130.00 USD |
| `1D` | `3606.00` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 58,500.00 USD | 0.00 USD | 24,110.00 USD |
| `7D` | `3609.20` | 15,670,000.00 USD | 0.00 USD | 15,670,000.00 USD | 140,620.00 USD | 0.00 USD | 34,910.00 USD |
| `1D` | `3610.20` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3613.50` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3614.40` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD |
| `7D` | `3617.80` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 114,410.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3618.60` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 34,170.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3622.10` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 59,230.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3622.80` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 73,510.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `3626.40` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 75,590.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.00` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 36,020.00 USD | 0.00 USD | 6,390.00 USD |
| `7D` | `3630.70` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 86,080.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.20` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 28,950.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `3635.00` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 44,190.00 USD | 0.00 USD | 8,410.00 USD |
| `1D` | `3635.40` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 12,560.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3639.30` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 42,820.00 USD | 0.00 USD | 8,110.00 USD |
| `1D` | `3639.60` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.60` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 22,390.00 USD | 0.00 USD | 10,190.00 USD |
| `7D` | `3647.90` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.20` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.50` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.80` | 14,760,000.00 USD | 0.00 USD | 14,760,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3665.10` | 14,740,000.00 USD | 0.00 USD | 14,740,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.40` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.80` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3837.10` | 14,720,000.00 USD | 0.00 USD | 14,720,000.00 USD | 212,590.00 USD | 0.00 USD | 14,220.00 USD |
| `1D` | `3841.20` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 63,550.00 USD | 0.00 USD | 74,550.00 USD |
| `7D` | `3841.40` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 554,480.00 USD | 0.00 USD | 111,970.00 USD |
| `1D` | `3845.40` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 190,490.00 USD | 0.00 USD | 82,180.00 USD |
| `7D` | `3845.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 499,670.00 USD | 0.00 USD | 183,220.00 USD |
| `1D` | `3849.60` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 35,100.00 USD | 0.00 USD | 26,660.00 USD |
| `7D` | `3850.00` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 442,940.00 USD | 0.00 USD | 87,050.00 USD |
| `1D` | `3853.80` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 115,420.00 USD | 0.00 USD | 34,820.00 USD |
| `7D` | `3854.30` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 311,860.00 USD | 0.00 USD | 67,640.00 USD |
| `1D` | `3858.00` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 96,590.00 USD | 0.00 USD | 24,610.00 USD |
| `7D` | `3858.60` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 322,600.00 USD | 0.00 USD | 19,690.00 USD |
| `1D` | `3862.20` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 176,170.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3862.90` | 11,890,000.00 USD | 0.00 USD | 11,890,000.00 USD | 196,060.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3866.40` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 199,300.00 USD | 0.00 USD | 28,280.00 USD |
| `7D` | `3867.20` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 246,970.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3870.60` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 131,660.00 USD | 0.00 USD | 17,250.00 USD |
| `7D` | `3871.50` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 260,720.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3874.80` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 73,180.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `3875.80` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 297,370.00 USD | 0.00 USD | 33,080.00 USD |
| `1D` | `3879.00` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 43,430.00 USD | 0.00 USD | 824.23 USD |
| `7D` | `3880.10` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 186,600.00 USD | 0.00 USD | 25,360.00 USD |
| `1D` | `3883.20` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3884.40` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 104,420.00 USD | 0.00 USD | 41,540.00 USD |
| `7D` | `3888.70` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3893.00` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 122,620.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.30` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.60` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.90` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.20` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 23,110.00 USD | 0.00 USD | 9,190.00 USD |
| `7D` | `3918.80` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3921.00` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 127,100.00 USD | 0.00 USD | 123,380.00 USD |
| `7D` | `3923.10` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 1,120,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3925.20` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 371,270.00 USD | 0.00 USD | 179,490.00 USD |
| `7D` | `3927.40` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 1,030,000.00 USD | 0.00 USD | 280,480.00 USD |
| `1D` | `3929.40` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 79,920.00 USD | 0.00 USD | 63,890.00 USD |
| `7D` | `3931.70` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 605,700.00 USD | 0.00 USD | 170,010.00 USD |
| `1D` | `3933.60` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `3936.00` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 823,760.00 USD | 0.00 USD | 104,250.00 USD |
| `1D` | `3937.80` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD |
| `7D` | `3940.30` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 322,520.00 USD | 0.00 USD | 57,010.00 USD |
| `1D` | `3942.00` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD |
| `7D` | `3944.60` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 465,130.00 USD | 0.00 USD | 148,680.00 USD |
| `1D` | `3946.20` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `3948.90` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 539,340.00 USD | 0.00 USD | 51,360.00 USD |
| `1D` | `3950.40` | 613,170.00 USD | 0.00 USD | 613,170.00 USD | 295,490.00 USD | 0.00 USD | 40,030.00 USD |
| `7D` | `3953.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 531,020.00 USD | 0.00 USD | 96,360.00 USD |
| `1D` | `3954.60` | 277,660.00 USD | 0.00 USD | 277,660.00 USD | 152,490.00 USD | 0.00 USD | 28,700.00 USD |
| `7D` | `3957.50` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 495,980.00 USD | 0.00 USD | 38,880.00 USD |
| `1D` | `3958.80` | 96,480.00 USD | 0.00 USD | 96,480.00 USD | 82,200.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `3961.80` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 287,960.00 USD | 0.00 USD | 67,760.00 USD |
| `1D` | `3963.00` | 11,170.00 USD | 0.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3966.10` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 202,410.00 USD | 0.00 USD | 57,830.00 USD |
| `7D` | `3970.40` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 199,830.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.70` | 809,000.00 USD | 0.00 USD | 809,000.00 USD | 243,340.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3979.00` | 540,980.00 USD | 0.00 USD | 540,980.00 USD | 293,010.00 USD | 0.00 USD | 18,120.00 USD |
| `7D` | `3983.30` | 229,840.00 USD | 0.00 USD | 229,840.00 USD | 0.00 USD | 0.00 USD | 21,420.00 USD |
| `7D` | `3987.60` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.90` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3997.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3998.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.60` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.90` | 733,530.00 USD | 733,530.00 USD | 0.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4080.60` | 230,960.00 USD | 230,960.00 USD | 0.00 USD | 127,100.00 USD | 0.00 USD | 103,850.00 USD |
| `7D` | `4082.20` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 307,920.00 USD |
| `1D` | `4084.80` | 787,310.00 USD | 787,310.00 USD | 0.00 USD | 360,440.00 USD | 0.00 USD | 195,910.00 USD |
| `7D` | `4086.50` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 290,240.00 USD |
| `1D` | `4089.00` | 900,890.00 USD | 900,890.00 USD | 0.00 USD | 76,430.00 USD | 0.00 USD | 37,160.00 USD |
| `7D` | `4090.80` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 696,130.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4093.20` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 157,510.00 USD | 0.00 USD | 77,320.00 USD |
| `7D` | `4095.10` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 553,040.00 USD | 0.00 USD | 135,280.00 USD |
| `1D` | `4097.40` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 197,620.00 USD | 0.00 USD | 51,660.00 USD |
| `7D` | `4099.40` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 662,770.00 USD | 0.00 USD | 30,680.00 USD |
| `1D` | `4101.60` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 298,260.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4103.70` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 372,480.00 USD | 0.00 USD | 116,150.00 USD |
| `1D` | `4105.80` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 405,090.00 USD | 0.00 USD | 70,840.00 USD |
| `7D` | `4108.00` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 454,830.00 USD | 0.00 USD | 123,520.00 USD |
| `1D` | `4110.00` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 247,120.00 USD | 0.00 USD | 37,750.00 USD |
| `7D` | `4112.30` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 528,700.00 USD | 0.00 USD | 67,220.00 USD |
| `1D` | `4114.20` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 246,100.00 USD | 0.00 USD | 31,440.00 USD |
| `7D` | `4116.60` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 448,400.00 USD | 0.00 USD | 51,770.00 USD |
| `1D` | `4118.40` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 99,410.00 USD | 0.00 USD | 15,930.00 USD |
| `7D` | `4120.90` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 404,230.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4122.60` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 34,710.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4125.20` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 74,790.00 USD |
| `7D` | `4129.50` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 50,120.00 USD |
| `7D` | `4133.80` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4138.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.40` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 232,530.00 USD | 0.00 USD | 16,750.00 USD |
| `7D` | `4146.70` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 21,540.00 USD |
| `7D` | `4151.00` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.30` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 120,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.60` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 376,160.00 USD | 0.00 USD | 52,970.00 USD |
| `1D` | `4160.40` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 63,550.00 USD | 0.00 USD | 40,280.00 USD |
| `7D` | `4163.90` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 572,880.00 USD | 0.00 USD | 184,750.00 USD |
| `1D` | `4164.60` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 171,460.00 USD | 0.00 USD | 95,990.00 USD |
| `7D` | `4168.20` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 511,580.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4168.80` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 30,740.00 USD |
| `7D` | `4172.50` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 285,980.00 USD | 0.00 USD | 85,010.00 USD |
| `1D` | `4173.00` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 74,610.00 USD | 0.00 USD | 34,000.00 USD |
| `7D` | `4176.80` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 401,620.00 USD | 0.00 USD | 52,120.00 USD |
| `1D` | `4177.20` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 88,500.00 USD | 0.00 USD | 31,470.00 USD |
| `7D` | `4181.10` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 161,260.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4181.40` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD |
| `7D` | `4185.40` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 178,140.00 USD | 0.00 USD | 67,220.00 USD |
| `1D` | `4185.60` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 165,300.00 USD | 0.00 USD | 28,810.00 USD |
| `7D` | `4189.70` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 278,400.00 USD | 0.00 USD | 38,370.00 USD |
| `1D` | `4189.80` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 161,350.00 USD | 0.00 USD | 24,850.00 USD |
| `1D` | `4194.00` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 123,920.00 USD | 0.00 USD | 17,340.00 USD |
| `7D` | `4194.00` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 207,230.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4198.20` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 58,980.00 USD | 0.00 USD | 9,050.00 USD |
| `7D` | `4198.30` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4202.40` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 38,300.00 USD | 0.00 USD | 510.84 USD |
| `7D` | `4202.60` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 182,330.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4206.60` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4206.90` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 153,500.00 USD | 0.00 USD | 43,720.00 USD |
| `7D` | `4211.20` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 21,770.00 USD |
| `7D` | `4215.50` | 14,400,000.00 USD | 14,400,000.00 USD | 0.00 USD | 129,360.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.80` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 78,180.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4224.10` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.40` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `7D` | `4232.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.00` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.80` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.10` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `1D` | `4399.80` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 11,760.00 USD | 0.00 USD | 10,970.00 USD |
| `7D` | `4400.40` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 114,050.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4404.00` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 51,100.00 USD | 0.00 USD | 31,830.00 USD |
| `7D` | `4404.70` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 168,350.00 USD | 0.00 USD | 55,430.00 USD |
| `1D` | `4408.20` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 23,070.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `4409.00` | 15,320,000.00 USD | 15,320,000.00 USD | 0.00 USD | 142,050.00 USD | 0.00 USD | 31,940.00 USD |
| `1D` | `4412.40` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `4413.30` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 75,090.00 USD | 0.00 USD | 21,250.00 USD |
| `1D` | `4416.60` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 19,970.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `4417.60` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 15,340.00 USD |
| `1D` | `4420.80` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 32,630.00 USD | 0.00 USD | 5,280.00 USD |
| `1D` | `4421.80` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD | 434.26 USD |
| `7D` | `4421.90` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `7D` | `4426.20` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `7D` | `4430.50` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `4434.80` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4438.50` | 15,880,000.00 USD | 15,880,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.25M` | Total OI Tokens: `68,861.5 PAXG`
  * 1h OI Change: `-0.41%` | 4h OI Change: `-0.41%` | 24h OI Change: `+0.26%`
  * Exchange Breakdown: Binance=`106.54M` | Bybit=`22.33M` | OKX=`-` | Hyperliquid=`24.55M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.44K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `51.10%` | `48.90%` | `1.04` | 1,620,000.00 USD |
| `15M` | `Binance` | `51.15%` | `48.85%` | `1.05` | 482,900.00 USD |
| `15M` | `OKX` | `53.2%` | `46.8%` | `1.14` | 88,400.00 USD |
| `15M` | `Bybit` | `40.13%` | `59.87%` | `0.67` | 251,700.00 USD |
| `15M` | `KuCoin` | `51.84%` | `48.16%` | `1.08` | 171,580.00 USD |
| `15M` | `Gate` | `61.61%` | `38.39%` | `1.60` | 47,670.00 USD |
| `15M` | `Bitget` | `54.85%` | `45.15%` | `1.21` | 319,980.00 USD |
| `15M` | `BingX` | `54.53%` | `45.47%` | `1.20` | 72,160.00 USD |
| `15M` | `MEXC` | `72.18%` | `27.82%` | `2.59` | 40,290.00 USD |
| `15M` | `Bitunix` | `52.78%` | `47.22%` | `1.12` | 17,880.00 USD |
| `15M` | `Hyperliquid` | `65.26%` | `34.74%` | `1.88` | 18,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.98%` | `50.02%` | `1.00` | 71,650.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `30.85%` | `69.15%` | `0.45` | 23,950.00 USD |
| `15M` | `HTX` | `99.91%` | `0.09%` | `1110.11` | 201.51 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `43.25%` | `56.75%` | `0.76` | 12,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.25%` | `95.75%` | `0.04` | 235.76 USD |
| `15M` | `Whale Positions` | `51.15%` | `48.85%` | `1.05` | 482,900.00 USD |
| `15M` | `Global Accounts` | `51.10%` | `48.90%` | `1.04` | 1,620,000.00 USD |
| `1H` | `PAXG` | `38.58%` | `61.42%` | `0.63` | 16,380,000.00 USD |
| `1H` | `Binance` | `38.06%` | `61.94%` | `0.61` | 1,450,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `58.41%` | `41.59%` | `1.40` | 1,010,000.00 USD |
| `1H` | `KuCoin` | `54.84%` | `45.16%` | `1.21` | 81,610.00 USD |
| `1H` | `Gate` | `48.31%` | `51.69%` | `0.93` | 532,010.00 USD |
| `1H` | `Bitget` | `32.04%` | `67.96%` | `0.47` | 1,470,000.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `35.58%` | `64.42%` | `0.55` | 10,210,000.00 USD |
| `1H` | `Bitunix` | `67.06%` | `32.94%` | `2.04` | 431,600.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.87%` | `47.13%` | `1.12` | 874,180.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.84%` | `94.16%` | `0.06` | 312,920.00 USD |
| `1H` | `HTX` | `15.36%` | `84.64%` | `0.18` | 6,590.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `38.06%` | `61.94%` | `0.61` | 1,450,000.00 USD |
| `1H` | `Global Accounts` | `38.58%` | `61.42%` | `0.63` | 16,380,000.00 USD |
| `4H` | `PAXG` | `48.42%` | `51.58%` | `0.94` | 20,070,000.00 USD |
| `4H` | `Binance` | `49.93%` | `50.07%` | `1.00` | 6,840,000.00 USD |
| `4H` | `OKX` | `48.88%` | `51.12%` | `0.96` | 2,100,000.00 USD |
| `4H` | `Bybit` | `52.33%` | `47.67%` | `1.10` | 2,000,000.00 USD |
| `4H` | `KuCoin` | `50.08%` | `49.92%` | `1.00` | 1,980,000.00 USD |
| `4H` | `Gate` | `39.94%` | `60.06%` | `0.67` | 407,050.00 USD |
| `4H` | `Bitget` | `49.43%` | `50.57%` | `0.98` | 2,080,000.00 USD |
| `4H` | `BingX` | `37.83%` | `62.17%` | `0.61` | 2,090,000.00 USD |
| `4H` | `MEXC` | `52.83%` | `47.17%` | `1.12` | 823,120.00 USD |
| `4H` | `Bitunix` | `41.55%` | `58.45%` | `0.71` | 281,790.00 USD |
| `4H` | `Hyperliquid` | `64.23%` | `35.77%` | `1.80` | 243,480.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.9%` | `50.1%` | `1.00` | 832,510.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `37.84%` | `62.16%` | `0.61` | 296,610.00 USD |
| `4H` | `HTX` | `39.64%` | `60.36%` | `0.66` | 4,180.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `98.21%` | `1.79%` | `54.87` | 2,340.00 USD |
| `4H` | `Aster` | `20.88%` | `79.12%` | `0.26` | 82,880.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `11.82%` | `88.18%` | `0.13` | 11,610.00 USD |
| `4H` | `Whale Positions` | `49.93%` | `50.07%` | `1.00` | 6,840,000.00 USD |
| `4H` | `Global Accounts` | `48.42%` | `51.58%` | `0.94` | 20,070,000.00 USD |


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
| `5m` | -13,910.00 USD | -14,580.00 USD | **`DISTRIBUTION`** |
| `15m` | -53,130.00 USD | 6,500.00 USD | **`DISTRIBUTION`** |
| `30m` | -196,440.00 USD | -5,910.00 USD | **`DISTRIBUTION`** |
| `1h` | -108,960.00 USD | 79,540.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,770,000.00 USD | 989,060.00 USD | **`ACCUMULATION`** |
| `4h` | 1,550,000.00 USD | 797,440.00 USD | **`ACCUMULATION`** |
| `6h` | 1,930,000.00 USD | 532,310.00 USD | **`ACCUMULATION`** |
| `8h` | 2,050,000.00 USD | 213,090.00 USD | **`ACCUMULATION`** |
| `12h` | 317,890.00 USD | -14,840.00 USD | **`ACCUMULATION`** |
| `24h` | 365,020.00 USD | 652,840.00 USD | **`ACCUMULATION`** |
| `1w` | -6,800,000.00 USD | -9,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -18,100,000.00 USD | -70,700,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-13.91K` | 15m=`-53.13K` | 1h=`-108.96K` | 24h=`+365.02K`
* Futures Capital Netflows: 5m=`-14.58K` | 15m=`+6.50K` | 1h=`+79.54K` | 24h=`+652.84K`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3996.37` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3986.39` (Risk Distance: `9.98` pts)
  * +2.5R Take Profit: `4021.32`
  * Mathematical Lot Sizing: **`1.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.29` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4023.27` (Risk Distance: `9.98` pts)
  * +2.5R Take Profit: `3988.34`
  * Mathematical Lot Sizing: **`1.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4020.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
