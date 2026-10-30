# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 11:17:13 IST` (`2026-10-30 05:47:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4003.67` | **Live Ask Quote**: `4003.75` | **Mid Price**: `4003.71`
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
  * Session VWAP: `4002.94` | VWAP Z-Score: `+0.57` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.46` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4020.86` | Lower -3.00σ Band: `3985.02`
  * Upper +2.51σ Band: `4017.93` | Lower -2.51σ Band: `3987.95`
  * Upper +2.01σ Band: `4014.94` | Lower -2.01σ Band: `3990.93`
  * Upper +2.00σ Band: `4014.88` | Lower -2.00σ Band: `3990.99`
  * Upper +1.28σ Band: `4010.58` | Lower -1.28σ Band: `3995.29`
  * Upper +1.00σ Band: `4008.91` | Lower -1.00σ Band: `3996.97`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3998.58` | EMA-20=`4001.24` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4009.10` (Slope: `+0.0000`) | EMA-100=`4017.83`
  * Institutional Anchors: EMA-144=`4022.10` | EMA-200=`4024.68` (Slope: `-0.0884`) | EMA-233=`4026.64`
- **Range Boundaries**: 24H High=`4046.38` | 24H Low=`3987.44` | Weekly High=`4082.75` | Weekly Low=`3987.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.04` (Distance: `-0.25%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.09%`)
  * Value Area Low (VAL) = `3996.99` (Distance: `+0.16%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3996.58`
  * New York Session (13:00-21:00 UTC): High=`4027.73` | Low=`3979.69`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3996.58`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3987.70` - `4019.72`
  * Optimal Trade Entry (OTE 0.705): `4011.72`
  * Structural Invalidation Anchor (0.786): `4035.74`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4013.80` | `4017.75` | `4011.82` | `4012.04` | `115` | 462,669.51 USD | 733.60 USD | `+0.16%` | 72,221.16 USD | `-0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4012.05` | `4014.05` | `4010.55` | `4010.85` | `27` | 108,971.39 USD | -5,429.51 USD | `-4.98%` | 66,791.64 USD | `-0.23` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `4010.81` | `4012.08` | `4009.35` | `4010.71` | `28` | 111,537.15 USD | -11,622.25 USD | `-10.42%` | 55,169.40 USD | `-0.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4002.94` | `4009.65` | `4002.94` | `4007.11` | `318` | 1,272,733.92 USD | 529,845.01 USD | `+41.63%` | 314,069.01 USD | `+1.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4007.11` | `4014.29` | `4006.74` | `4013.79` | `199` | 799,958.77 USD | -242,581.45 USD | `-30.32%` | 71,487.55 USD | `-0.82` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4013.80` | `4017.75` | `4009.35` | `4010.71` | `170` | 683,178.05 USD | -16,318.16 USD | `-2.39%` | 55,169.40 USD | `-0.06` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -446,454.31 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4002.94` | `1,790` | 7,158,366.15 USD | 437,268.83 USD | `+6.11%` | -9,185.48 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4002.94` | `4017.75` | `4002.94` | `4010.71` | `687` | 2,755,870.74 USD | 270,945.40 USD | `+9.83%` | 261,759.92 USD | `+0.51` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3995.14` | `4010.71` | `2,478` | 9,917,485.57 USD | 711,462.91 USD | `+7.17%` | 659,371.37 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3995.14` | `4010.71` | `2,478` | 9,917,485.57 USD | 711,462.91 USD | `+7.17%` | 659,371.37 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `4002.70` | `5.7719` | 23,103.18 USD | 924,830.20 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4002.80` | `11.8705` | 47,515.24 USD | 901,727.02 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4002.90` | `15.0794` | 60,361.33 USD | 854,211.78 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4003.00` | `10.3595` | 41,469.08 USD | 793,850.45 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4003.10` | `49.9602` | 199,995.68 USD | 752,381.37 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4003.20` | `12.8302` | 51,361.86 USD | 552,385.69 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4003.30` | `23.1537` | 92,691.21 USD | 501,023.84 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4003.40` | `9.9874` | 39,983.56 USD | 408,332.63 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4003.50` | `0.0620` | 248.22 USD | 368,349.07 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4003.60` | `2.9943` | 11,987.98 USD | 368,100.86 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4003.70` | `8.0740` | 32,325.87 USD | 356,112.88 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4003.80` | `7.4928` | 29,999.67 USD | 323,787.00 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4003.90` | `25.0967` | 100,484.68 USD | 293,787.33 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4004.00` | `20.6409` | 82,646.16 USD | 193,302.65 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4004.10` | `2.6002` | 10,411.46 USD | 110,656.49 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4004.20` | `4.8891` | 19,576.93 USD | 100,245.03 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4004.30` | `0.4456` | 1,784.32 USD | 80,668.09 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4004.40` | `14.1296` | 56,580.57 USD | 78,883.78 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `4004.50` | `0.1166` | 466.92 USD | 22,303.21 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4004.60` | `5.4528` | 21,836.28 USD | 21,836.28 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4004.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,004.65` | `0.00%` | `-` |
| `ASK` | `4004.70` | `0.1061` | 424.90 USD | 424.90 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `4004.90` | `18.2215` | 72,975.29 USD | 73,400.18 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4005.00` | `6.4519` | 25,839.86 USD | 99,240.04 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4005.10` | `34.7651` | 139,237.70 USD | 238,477.75 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4005.20` | `11.9848` | 48,001.52 USD | 286,479.27 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4005.30` | `57.9498` | 232,106.33 USD | 518,585.60 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4005.40` | `4.2555` | 17,044.98 USD | 535,630.58 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4005.50` | `12.6210` | 50,553.42 USD | 586,184.00 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4005.60` | `4.0036` | 16,036.82 USD | 602,220.82 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4005.70` | `51.8676` | 207,766.05 USD | 809,986.86 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4005.80` | `6.1421` | 24,604.02 USD | 834,590.89 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4005.90` | `9.4659` | 37,919.45 USD | 872,510.33 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4006.00` | `21.4104` | 85,770.06 USD | 958,280.40 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4006.10` | `8.3873` | 33,600.36 USD | 991,880.76 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4006.20` | `11.6853` | 46,813.65 USD | 1,038,694.41 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4006.30` | `85.9615` | 344,387.56 USD | 1,383,081.97 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4006.40` | `7.5867` | 30,395.35 USD | 1,413,477.32 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4006.50` | `19.2887` | 77,280.18 USD | 1,490,757.50 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4006.60` | `9.5106` | 38,105.17 USD | 1,528,862.67 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4006.70` | `18.1250` | 72,621.44 USD | 1,601,484.10 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 25,987,202.24 USD | `6,489.82` | `4185.46` | `4003.60` | `29194.30` | 1,175,748.77 USD | `+4.52%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,297,888.43 USD | `6,317.68` | `4128.93` | `4003.60` | `13970.82` | 787,400.10 USD | `+3.11%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,506,599.14 USD | `5,869.90` | `4228.86` | `4003.60` | `26855.79` | 1,316,422.80 USD | `+5.60%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,335,909.01 USD | `4,828.91` | `4157.43` | `4003.60` | `2265.43` | -739,973.31 USD | `-3.83%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,220,455.41 USD | `3,551.74` | `4127.81` | `4003.60` | `605.92` | -440,481.59 USD | `-3.10%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,085,272.01 USD | `3,268.21` | `4228.94` | `4003.60` | `4375.45` | 735,807.12 USD | `+5.62%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,612,470.40 USD | `2,900.00` | `4364.92` | `4003.60` | `4235.92` | 1,045,805.93 USD | `+9.01%` | `20X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,810,120.00 USD | `2,200.00` | `4112.20` | `4003.60` | `4331.40` | 236,734.59 USD | `+2.69%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,808,360.00 USD | `2,200.00` | `4176.09` | `4003.60` | `2596.68` | -379,059.30 USD | `-4.30%` | `25X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,910,563.10 USD | `1,975.37` | `4048.55` | `4003.60` | `6575.38` | 86,828.62 USD | `+1.10%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,325,811.02 USD | `1,579.95` | `4075.62` | `4003.60` | `0.000000` | -113,485.95 USD | `-1.79%` | `1X Cross` |
| `563` | `0x63da...8add` | `LONG` | 4,003,800.00 USD | `1,000.00` | `4021.46` | `4003.60` | `3564.37` | -17,660.96 USD | `-0.44%` | `25X Cross` |
| `569` | `0xf3dc...1672` | `LONG` | 3,940,626.17 USD | `984.27` | `4018.39` | `4003.60` | `2909.97` | -14,560.52 USD | `-0.37%` | `20X Cross` |
| `584` | `0x9aa5...58af` | `LONG` | 3,890,648.90 USD | `971.64` | `4279.98` | `4003.60` | `0.000000` | -267,960.19 USD | `-6.89%` | `20X Cross` |
| `591` | `0x354b...6425` | `LONG` | 3,839,352.47 USD | `958.81` | `4004.93` | `4003.60` | `0.000000` | -608.75 USD | `-0.02%` | `10X Cross` |
| `673` | `0x4a20...3c26` | `LONG` | 3,352,780.92 USD | `837.40` | `4599.73` | `4003.60` | `0.000000` | -499,039.46 USD | `-14.88%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,748,891.89 USD | `686.49` | `4290.34` | `4003.60` | `1143.91` | -196,366.82 USD | `-7.14%` | `25X Cross` |
| `903` | `0x625e...a354` | `SHORT` | 2,482,852.00 USD | `620.00` | `4122.81` | `4003.60` | `4342.50` | 73,295.03 USD | `+2.95%` | `20X Cross` |
| `909` | `0xd8c5...99b0` | `SHORT` | 2,475,769.35 USD | `618.35` | `4175.35` | `4003.60` | `34175.94` | 106,083.26 USD | `+4.28%` | `4X Cross` |
| `934` | `0xeae3...e8ad` | `SHORT` | 2,402,280.00 USD | `600.00` | `4104.77` | `4003.60` | `4325.52` | 60,585.11 USD | `+2.52%` | `20X Cross` |
| `937` | `0xf285...fa82` | `LONG` | 2,394,995.46 USD | `598.11` | `4146.45` | `4003.60` | `3891.51` | -85,024.10 USD | `-3.55%` | `25X Cross` |
| `951` | `0x12f7...8750` | `LONG` | 2,344,668.12 USD | `585.61` | `4082.77` | `4003.60` | `2582.53` | -46,248.86 USD | `-1.97%` | `10X Cross` |
| `1092` | `0x413c...886c` | `LONG` | 2,001,800.00 USD | `500.00` | `4010.43` | `4003.60` | `0.000000` | -3,416.23 USD | `-0.17%` | `2X Cross` |
| `1099` | `0x9c06...0560` | `LONG` | 1,995,812.39 USD | `498.42` | `4012.76` | `4003.60` | `0.000000` | -4,219.10 USD | `-0.21%` | `25X Cross` |
| `1104` | `0x61ce...a62b` | `SHORT` | 1,991,854.76 USD | `497.50` | `4071.66` | `4003.60` | `4715.52` | 33,814.03 USD | `+1.70%` | `20X Cross` |
| `1175` | `0x2edd...8179` | `LONG` | 1,884,391.85 USD | `469.89` | `4164.68` | `4010.00` | `0.000000` | -72,540.67 USD | `-3.85%` | `10X Cross` |
| `1214` | `0xead5...69f2` | `LONG` | 1,817,223.01 USD | `453.78` | `4220.88` | `4003.60` | `3539.20` | -98,145.05 USD | `-5.40%` | `5X Isolated` |
| `1274` | `0x7a6d...f79c` | `SHORT` | 1,717,917.59 USD | `428.38` | `4136.09` | `4010.00` | `5344.15` | 53,897.41 USD | `+3.14%` | `10X Cross` |
| `1304` | `0x46fc...1195` | `LONG` | 1,661,275.55 USD | `414.87` | `4053.27` | `4003.60` | `2152.77` | -20,317.29 USD | `-1.22%` | `20X Cross` |
| `1347` | `0x6d15...d374` | `LONG` | 1,601,840.00 USD | `400.00` | `4068.25` | `4003.60` | `3842.07` | -25,460.00 USD | `-1.59%` | `25X Cross` |
| `1348` | `0xee02...309d` | `SHORT` | 1,601,720.00 USD | `400.00` | `4438.84` | `4003.60` | `4227.14` | 173,818.60 USD | `+10.85%` | `25X Isolated` |
| `1391` | `0x51f6...2b39` | `LONG` | 1,565,314.60 USD | `390.33` | `4228.91` | `4010.00` | `542.63` | -85,338.49 USD | `-5.45%` | `10X Cross` |
| `1396` | `0x02a7...fe9f` | `SHORT` | 1,561,482.00 USD | `390.00` | `4055.02` | `4003.60` | `4306.96` | 19,977.25 USD | `+1.28%` | `25X Cross` |
| `1432` | `0x7e77...b8d2` | `SHORT` | 1,521,444.00 USD | `380.00` | `4131.92` | `4003.60` | `4293.77` | 48,685.64 USD | `+3.20%` | `20X Cross` |
| `1458` | `0x72c2...9b37` | `LONG` | 1,493,905.79 USD | `373.13` | `4000.98` | `4003.60` | `3778.31` | 1,012.27 USD | `+0.07%` | `13X Isolated` |
| `1496` | `0x781e...96b7` | `SHORT` | 1,449,093.70 USD | `361.37` | `4363.26` | `4010.00` | `12966.72` | 127,656.10 USD | `+8.81%` | `10X Cross` |
| `1507` | `0xaa44...b844` | `LONG` | 1,441,296.00 USD | `360.00` | `4043.10` | `4003.60` | `2819.86` | -14,221.63 USD | `-0.99%` | `4X Cross` |
| `1611` | `0xa41f...d50a` | `LONG` | 1,317,230.04 USD | `328.96` | `4468.89` | `4003.60` | `3802.43` | -152,867.81 USD | `-11.61%` | `15X Cross` |
| `1629` | `0x7fda...17d1` | `SHORT` | 1,299,852.61 USD | `324.62` | `4013.13` | `4003.60` | `30211.94` | 2,899.28 USD | `+0.22%` | `20X Cross` |
| `1661` | `0xbf5a...88ba` | `SHORT` | 1,271,985.52 USD | `317.65` | `4091.80` | `4003.60` | `10010.37` | 27,797.52 USD | `+2.19%` | `20X Cross` |
| `1698` | `0xff31...ff6c` | `SHORT` | 1,241,178.00 USD | `310.00` | `4372.43` | `4003.60` | `4789.43` | 114,277.38 USD | `+9.21%` | `10X Isolated` |
| `1721` | `0xada6...6f88` | `LONG` | 1,215,114.14 USD | `303.50` | `4166.46` | `4003.60` | `1790.47` | -49,398.72 USD | `-4.07%` | `5X Cross` |
| `1886` | `0x50e2...d770` | `LONG` | 1,082,497.00 USD | `270.37` | `4243.58` | `4003.60` | `2562.36` | -64,829.46 USD | `-5.99%` | `20X Cross` |
| `1902` | `0x4c92...4f17` | `SHORT` | 1,067,895.54 USD | `266.72` | `4260.98` | `4003.60` | `6510.11` | 68,596.70 USD | `+6.42%` | `20X Cross` |
| `1977` | `0xd346...c4f3` | `LONG` | 1,021,792.45 USD | `255.17` | `4188.66` | `4003.60` | `3310.69` | -47,044.06 USD | `-4.60%` | `5X Isolated` |

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
| `7D` | `Long Liquidation` | `3596.10` | 16,340,000.00 USD | 16,340,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.40` | 16,310,000.00 USD | 16,310,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3601.80` | 4,900,000.00 USD | 4,900,000.00 USD | 22,150.00 USD | 0.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.70` | 16,140,000.00 USD | 16,140,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.00` | 4,860,000.00 USD | 4,860,000.00 USD | 58,500.00 USD | 0.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.00` | 15,870,000.00 USD | 15,870,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.20` | 4,780,000.00 USD | 4,780,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.30` | 15,680,000.00 USD | 15,680,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.40` | 4,750,000.00 USD | 4,750,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.60` | 15,580,000.00 USD | 15,580,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.60` | 4,700,000.00 USD | 4,700,000.00 USD | 34,170.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.90` | 15,460,000.00 USD | 15,460,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.80` | 4,660,000.00 USD | 4,660,000.00 USD | 73,510.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.20` | 15,380,000.00 USD | 15,380,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.00` | 4,580,000.00 USD | 4,580,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.50` | 15,300,000.00 USD | 15,300,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.20` | 4,530,000.00 USD | 4,530,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.80` | 15,180,000.00 USD | 15,180,000.00 USD | 44,190.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.40` | 4,490,000.00 USD | 4,490,000.00 USD | 14,390.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.10` | 15,130,000.00 USD | 15,130,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.60` | 4,470,000.00 USD | 4,470,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.40` | 15,080,000.00 USD | 15,080,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.70` | 15,020,000.00 USD | 15,020,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.00` | 14,990,000.00 USD | 14,990,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.30` | 14,960,000.00 USD | 14,960,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.60` | 14,920,000.00 USD | 14,920,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3664.90` | 14,900,000.00 USD | 14,900,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 14,890,000.00 USD | 14,890,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.60` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3836.90` | 14,880,000.00 USD | 14,880,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3841.20` | 4,470,000.00 USD | 4,470,000.00 USD | 63,550.00 USD | 0.00 USD | 66,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.20` | 14,670,000.00 USD | 14,670,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3845.40` | 4,340,000.00 USD | 4,340,000.00 USD | 183,730.00 USD | 0.00 USD | 78,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.50` | 14,020,000.00 USD | 14,020,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3849.60` | 4,080,000.00 USD | 4,080,000.00 USD | 35,100.00 USD | 0.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,330,000.00 USD | 13,330,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3853.80` | 4,020,000.00 USD | 4,020,000.00 USD | 115,420.00 USD | 0.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.10` | 12,790,000.00 USD | 12,790,000.00 USD | 249,250.00 USD | 0.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.00` | 3,870,000.00 USD | 3,870,000.00 USD | 96,590.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.40` | 12,470,000.00 USD | 12,470,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.20` | 3,750,000.00 USD | 3,750,000.00 USD | 176,170.00 USD | 0.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.70` | 12,070,000.00 USD | 12,070,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.40` | 3,540,000.00 USD | 3,540,000.00 USD | 199,300.00 USD | 0.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.00` | 11,820,000.00 USD | 11,820,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.60` | 3,310,000.00 USD | 3,310,000.00 USD | 160,940.00 USD | 0.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.30` | 11,540,000.00 USD | 11,540,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3874.80` | 3,130,000.00 USD | 3,130,000.00 USD | 87,740.00 USD | 0.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.60` | 11,210,000.00 USD | 11,210,000.00 USD | 297,370.00 USD | 0.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.00` | 3,030,000.00 USD | 3,030,000.00 USD | 46,050.00 USD | 0.00 USD | 988.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.90` | 10,890,000.00 USD | 10,890,000.00 USD | 235,430.00 USD | 0.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.20` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.20` | 10,620,000.00 USD | 10,620,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,470,000.00 USD | 10,470,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.80` | 10,360,000.00 USD | 10,360,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.10` | 10,230,000.00 USD | 10,230,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.40` | 10,120,000.00 USD | 10,120,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.70` | 10,030,000.00 USD | 10,030,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.00` | 9,960,000.00 USD | 9,960,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.60` | 9,920,000.00 USD | 9,920,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3921.00` | 2,980,000.00 USD | 2,980,000.00 USD | 127,100.00 USD | 0.00 USD | 115,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.90` | 9,010,000.00 USD | 9,010,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3925.20` | 2,740,000.00 USD | 2,740,000.00 USD | 357,750.00 USD | 0.00 USD | 163,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.20` | 7,610,000.00 USD | 7,610,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3929.40` | 2,220,000.00 USD | 2,220,000.00 USD | 79,920.00 USD | 0.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 6,250,000.00 USD | 6,250,000.00 USD | 605,700.00 USD | 0.00 USD | 168,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.60` | 2,080,000.00 USD | 2,080,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.80` | 5,480,000.00 USD | 5,480,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3937.80` | 1,820,000.00 USD | 1,820,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.10` | 4,570,000.00 USD | 4,570,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.00` | 1,580,000.00 USD | 1,580,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.40` | 4,180,000.00 USD | 4,180,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.20` | 1,210,000.00 USD | 1,210,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.70` | 3,630,000.00 USD | 3,630,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.40` | 714,640.00 USD | 714,640.00 USD | 347,740.00 USD | 0.00 USD | 43,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.00` | 2,960,000.00 USD | 2,960,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 323,070.00 USD | 323,070.00 USD | 182,170.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.30` | 2,340,000.00 USD | 2,340,000.00 USD | 478,000.00 USD | 0.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.80` | 108,270.00 USD | 108,270.00 USD | 93,180.00 USD | 0.00 USD | 3,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,820,000.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.00` | 11,170.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.90` | 1,320,000.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.20` | 1,050,000.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.50` | 831,670.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.80` | 579,930.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.10` | 237,060.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.40` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.70` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4080.60` | 227,000.00 USD | 227,000.00 USD | 127,100.00 USD | 0.00 USD | 99,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4084.80` | 750,200.00 USD | 750,200.00 USD | 346,920.00 USD | 0.00 USD | 176,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4089.00` | 859,720.00 USD | 859,720.00 USD | 76,430.00 USD | 0.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.20` | 1,090,000.00 USD | 1,090,000.00 USD | 157,510.00 USD | 0.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 4,820,000.00 USD | 4,820,000.00 USD | 498,510.00 USD | 0.00 USD | 127,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.40` | 1,340,000.00 USD | 1,340,000.00 USD | 197,620.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.20` | 5,570,000.00 USD | 5,570,000.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.60` | 1,690,000.00 USD | 1,690,000.00 USD | 298,260.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 6,060,000.00 USD | 6,060,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4105.80` | 2,170,000.00 USD | 2,170,000.00 USD | 405,090.00 USD | 0.00 USD | 70,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.80` | 6,660,000.00 USD | 6,660,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.00` | 2,480,000.00 USD | 2,480,000.00 USD | 271,030.00 USD | 0.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.10` | 7,130,000.00 USD | 7,130,000.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.20` | 2,810,000.00 USD | 2,810,000.00 USD | 294,970.00 USD | 0.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.40` | 7,750,000.00 USD | 7,750,000.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.40` | 2,940,000.00 USD | 2,940,000.00 USD | 114,320.00 USD | 0.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 8,320,000.00 USD | 8,320,000.00 USD | 534,120.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.60` | 2,980,000.00 USD | 2,980,000.00 USD | 39,940.00 USD | 0.00 USD | 934.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.00` | 8,750,000.00 USD | 8,750,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.30` | 8,930,000.00 USD | 8,930,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.60` | 9,180,000.00 USD | 9,180,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4137.90` | 9,410,000.00 USD | 9,410,000.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 9,690,000.00 USD | 9,690,000.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.50` | 9,750,000.00 USD | 9,750,000.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.80` | 9,880,000.00 USD | 9,880,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.10` | 9,950,000.00 USD | 9,950,000.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.40` | 10,420,000.00 USD | 10,420,000.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.40` | 3,080,000.00 USD | 3,080,000.00 USD | 63,550.00 USD | 0.00 USD | 38,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.70` | 11,170,000.00 USD | 11,170,000.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.60` | 3,330,000.00 USD | 3,330,000.00 USD | 164,700.00 USD | 0.00 USD | 86,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.00` | 11,760,000.00 USD | 11,760,000.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.80` | 3,410,000.00 USD | 3,410,000.00 USD | 46,980.00 USD | 0.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.30` | 12,150,000.00 USD | 12,150,000.00 USD | 302,850.00 USD | 0.00 USD | 82,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.00` | 3,520,000.00 USD | 3,520,000.00 USD | 74,610.00 USD | 0.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.60` | 12,600,000.00 USD | 12,600,000.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.20` | 3,640,000.00 USD | 3,640,000.00 USD | 88,500.00 USD | 0.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.90` | 12,790,000.00 USD | 12,790,000.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.40` | 3,790,000.00 USD | 3,790,000.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.20` | 13,010,000.00 USD | 13,010,000.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.60` | 3,990,000.00 USD | 3,990,000.00 USD | 165,300.00 USD | 0.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.50` | 13,300,000.00 USD | 13,300,000.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.80` | 4,180,000.00 USD | 4,180,000.00 USD | 173,310.00 USD | 0.00 USD | 25,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4193.80` | 13,600,000.00 USD | 13,600,000.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.00` | 4,350,000.00 USD | 4,350,000.00 USD | 148,350.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.10` | 13,860,000.00 USD | 13,860,000.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.20` | 4,430,000.00 USD | 4,430,000.00 USD | 66,440.00 USD | 0.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.40` | 4,470,000.00 USD | 4,470,000.00 USD | 40,910.00 USD | 0.00 USD | 674.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.40` | 14,110,000.00 USD | 14,110,000.00 USD | 222,160.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.60` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.70` | 14,320,000.00 USD | 14,320,000.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,410,000.00 USD | 14,410,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.30` | 14,530,000.00 USD | 14,530,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.60` | 14,650,000.00 USD | 14,650,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.90` | 14,770,000.00 USD | 14,770,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.20` | 14,800,000.00 USD | 14,800,000.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.50` | 14,870,000.00 USD | 14,870,000.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.80` | 14,880,000.00 USD | 14,880,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.90` | 14,950,000.00 USD | 14,950,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4399.80` | 4,490,000.00 USD | 4,490,000.00 USD | 11,760.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.20` | 15,080,000.00 USD | 15,080,000.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.00` | 4,570,000.00 USD | 4,570,000.00 USD | 51,100.00 USD | 0.00 USD | 28,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.50` | 15,300,000.00 USD | 15,300,000.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4408.20` | 4,600,000.00 USD | 4,600,000.00 USD | 23,070.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.80` | 15,480,000.00 USD | 15,480,000.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4412.40` | 4,630,000.00 USD | 4,630,000.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.10` | 15,570,000.00 USD | 15,570,000.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.60` | 4,650,000.00 USD | 4,650,000.00 USD | 19,970.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.40` | 15,670,000.00 USD | 15,670,000.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.80` | 4,690,000.00 USD | 4,690,000.00 USD | 32,630.00 USD | 0.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.70` | 15,760,000.00 USD | 15,760,000.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.80` | 4,700,000.00 USD | 4,700,000.00 USD | 9,110.00 USD | 0.00 USD | 434.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.00` | 15,820,000.00 USD | 15,820,000.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 15,890,000.00 USD | 15,890,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.60` | 15,960,000.00 USD | 15,960,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.90` | 16,040,000.00 USD | 16,040,000.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4440.70` | 16,070,000.00 USD | 16,070,000.00 USD | 23,500.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |

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
| `7D` | `3600.40` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD |
| `1D` | `3601.80` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 22,150.00 USD | 0.00 USD | 24,530.00 USD |
| `7D` | `3604.70` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD |
| `1D` | `3606.00` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 58,500.00 USD | 0.00 USD | 22,800.00 USD |
| `7D` | `3609.00` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD |
| `1D` | `3610.20` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3613.30` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3614.40` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD |
| `7D` | `3617.60` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3618.60` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 34,170.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3621.90` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3622.80` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 73,510.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `3626.20` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.00` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD |
| `7D` | `3630.50` | 15,300,000.00 USD | 0.00 USD | 15,300,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.20` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3634.80` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 44,190.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `3635.40` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 14,390.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3639.10` | 15,130,000.00 USD | 0.00 USD | 15,130,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD |
| `1D` | `3639.60` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.40` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD |
| `7D` | `3647.70` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.00` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.30` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.60` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3664.90` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.60` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3836.90` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `3841.20` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 63,550.00 USD | 0.00 USD | 66,030.00 USD |
| `7D` | `3841.20` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD |
| `1D` | `3845.40` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 183,730.00 USD | 0.00 USD | 78,900.00 USD |
| `7D` | `3845.50` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD |
| `1D` | `3849.60` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 35,100.00 USD | 0.00 USD | 24,620.00 USD |
| `7D` | `3849.80` | 13,330,000.00 USD | 0.00 USD | 13,330,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD |
| `1D` | `3853.80` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 115,420.00 USD | 0.00 USD | 34,820.00 USD |
| `7D` | `3854.10` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 249,250.00 USD | 0.00 USD | 66,410.00 USD |
| `1D` | `3858.00` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 96,590.00 USD | 0.00 USD | 24,610.00 USD |
| `7D` | `3858.40` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD |
| `1D` | `3862.20` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 176,170.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3862.70` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3866.40` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 199,300.00 USD | 0.00 USD | 29,260.00 USD |
| `7D` | `3867.00` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3870.60` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 160,940.00 USD | 0.00 USD | 18,490.00 USD |
| `7D` | `3871.30` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3874.80` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 87,740.00 USD | 0.00 USD | 14,970.00 USD |
| `7D` | `3875.60` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 297,370.00 USD | 0.00 USD | 29,270.00 USD |
| `1D` | `3879.00` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 46,050.00 USD | 0.00 USD | 988.17 USD |
| `7D` | `3879.90` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 235,430.00 USD | 0.00 USD | 27,170.00 USD |
| `1D` | `3883.20` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3884.20` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD |
| `7D` | `3888.50` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3892.80` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.10` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.40` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.70` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.00` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3918.60` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3921.00` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 127,100.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3922.90` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3925.20` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 357,750.00 USD | 0.00 USD | 163,440.00 USD |
| `7D` | `3927.20` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD |
| `1D` | `3929.40` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 79,920.00 USD | 0.00 USD | 59,820.00 USD |
| `7D` | `3931.50` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 605,700.00 USD | 0.00 USD | 168,200.00 USD |
| `1D` | `3933.60` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `3935.80` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD |
| `1D` | `3937.80` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD |
| `7D` | `3940.10` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD |
| `1D` | `3942.00` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD |
| `7D` | `3944.40` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD |
| `1D` | `3946.20` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `3948.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD |
| `1D` | `3950.40` | 714,640.00 USD | 0.00 USD | 714,640.00 USD | 347,740.00 USD | 0.00 USD | 43,820.00 USD |
| `7D` | `3953.00` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD |
| `1D` | `3954.60` | 323,070.00 USD | 0.00 USD | 323,070.00 USD | 182,170.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3957.30` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 478,000.00 USD | 0.00 USD | 49,670.00 USD |
| `1D` | `3958.80` | 108,270.00 USD | 0.00 USD | 108,270.00 USD | 93,180.00 USD | 0.00 USD | 3,920.00 USD |
| `7D` | `3961.60` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3963.00` | 11,170.00 USD | 0.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3965.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD |
| `7D` | `3970.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.50` | 831,670.00 USD | 0.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3978.80` | 579,930.00 USD | 0.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD |
| `7D` | `3983.10` | 237,060.00 USD | 0.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `7D` | `3987.40` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.70` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4012.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4012.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4080.60` | 227,000.00 USD | 227,000.00 USD | 0.00 USD | 127,100.00 USD | 0.00 USD | 99,890.00 USD |
| `7D` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD |
| `1D` | `4084.80` | 750,200.00 USD | 750,200.00 USD | 0.00 USD | 346,920.00 USD | 0.00 USD | 176,290.00 USD |
| `7D` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD |
| `1D` | `4089.00` | 859,720.00 USD | 859,720.00 USD | 0.00 USD | 76,430.00 USD | 0.00 USD | 33,090.00 USD |
| `7D` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4093.20` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 157,510.00 USD | 0.00 USD | 77,320.00 USD |
| `7D` | `4094.90` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 498,510.00 USD | 0.00 USD | 127,890.00 USD |
| `1D` | `4097.40` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 197,620.00 USD | 0.00 USD | 51,660.00 USD |
| `7D` | `4099.20` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4101.60` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 298,260.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4103.50` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4105.80` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 405,090.00 USD | 0.00 USD | 70,840.00 USD |
| `7D` | `4107.80` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4110.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 271,030.00 USD | 0.00 USD | 39,710.00 USD |
| `7D` | `4112.10` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD |
| `1D` | `4114.20` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 294,970.00 USD | 0.00 USD | 37,210.00 USD |
| `7D` | `4116.40` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD |
| `1D` | `4118.40` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 114,320.00 USD | 0.00 USD | 16,410.00 USD |
| `7D` | `4120.70` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 534,120.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4122.60` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 39,940.00 USD | 0.00 USD | 934.06 USD |
| `7D` | `4125.00` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `7D` | `4129.30` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `4133.60` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4137.90` | 9,410,000.00 USD | 9,410,000.00 USD | 0.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.20` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD |
| `7D` | `4146.50` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4150.80` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.10` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.40` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD |
| `1D` | `4160.40` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 63,550.00 USD | 0.00 USD | 38,310.00 USD |
| `7D` | `4163.70` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD |
| `1D` | `4164.60` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 164,700.00 USD | 0.00 USD | 86,180.00 USD |
| `7D` | `4168.00` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4168.80` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 28,700.00 USD |
| `7D` | `4172.30` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 302,850.00 USD | 0.00 USD | 82,190.00 USD |
| `1D` | `4173.00` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 74,610.00 USD | 0.00 USD | 34,000.00 USD |
| `7D` | `4176.60` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD |
| `1D` | `4177.20` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 88,500.00 USD | 0.00 USD | 31,470.00 USD |
| `7D` | `4180.90` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4181.40` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD |
| `7D` | `4185.20` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD |
| `1D` | `4185.60` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 165,300.00 USD | 0.00 USD | 28,810.00 USD |
| `7D` | `4189.50` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD |
| `1D` | `4189.80` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 173,310.00 USD | 0.00 USD | 25,830.00 USD |
| `7D` | `4193.80` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4194.00` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 148,350.00 USD | 0.00 USD | 19,440.00 USD |
| `7D` | `4198.10` | 13,860,000.00 USD | 13,860,000.00 USD | 0.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4198.20` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 66,440.00 USD | 0.00 USD | 10,090.00 USD |
| `1D` | `4202.40` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 40,910.00 USD | 0.00 USD | 674.78 USD |
| `7D` | `4202.40` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 222,160.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4206.60` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4206.70` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD |
| `7D` | `4211.00` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `7D` | `4215.30` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.60` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4223.90` | 14,770,000.00 USD | 14,770,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.20` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `4232.50` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD |
| `7D` | `4236.80` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.90` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `1D` | `4399.80` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 11,760.00 USD | 0.00 USD | 10,970.00 USD |
| `7D` | `4400.20` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4404.00` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 51,100.00 USD | 0.00 USD | 28,620.00 USD |
| `7D` | `4404.50` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD |
| `1D` | `4408.20` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 23,070.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `4408.80` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD |
| `1D` | `4412.40` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `4413.10` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD |
| `1D` | `4416.60` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 19,970.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `4417.40` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD |
| `1D` | `4420.80` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 32,630.00 USD | 0.00 USD | 5,280.00 USD |
| `7D` | `4421.70` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD |
| `1D` | `4421.80` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD | 434.26 USD |
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
  * Total Open Interest: `275.84M` | Total OI Tokens: `68,776.5 PAXG`
  * 1h OI Change: `-0.10%` | 4h OI Change: `+0.19%` | 24h OI Change: `+0.76%`
  * Exchange Breakdown: Binance=`106.91M` | Bybit=`22.24M` | OKX=`-` | Hyperliquid=`24.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.84K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `42.21%` | `57.79%` | `0.73` | 3,910,000.00 USD |
| `15M` | `Binance` | `40.79%` | `59.21%` | `0.69` | 370,190.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `49.75%` | `50.25%` | `0.99` | 303,980.00 USD |
| `15M` | `KuCoin` | `29.86%` | `70.14%` | `0.43` | 13,330.00 USD |
| `15M` | `Gate` | `19.06%` | `80.94%` | `0.24` | 157,510.00 USD |
| `15M` | `Bitget` | `48.51%` | `51.49%` | `0.94` | 298,440.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `43.59%` | `56.41%` | `0.77` | 2,480,000.00 USD |
| `15M` | `Bitunix` | `31.33%` | `68.67%` | `0.46` | 50,400.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.09%` | `50.91%` | `0.96` | 152,390.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.87%` | `99.13%` | `0.01` | 88,630.00 USD |
| `15M` | `HTX` | `14.15%` | `85.85%` | `0.16` | 2,910.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `40.79%` | `59.21%` | `0.69` | 370,190.00 USD |
| `15M` | `Global Accounts` | `42.21%` | `57.79%` | `0.73` | 3,910,000.00 USD |
| `1H` | `PAXG` | `39.65%` | `60.35%` | `0.66` | 19,400,000.00 USD |
| `1H` | `Binance` | `43.38%` | `56.62%` | `0.77` | 7,390,000.00 USD |
| `1H` | `OKX` | `37.35%` | `62.65%` | `0.60` | 4,070,000.00 USD |
| `1H` | `Bybit` | `38.91%` | `61.09%` | `0.64` | 1,810,000.00 USD |
| `1H` | `KuCoin` | `39.69%` | `60.31%` | `0.66` | 92,630.00 USD |
| `1H` | `Gate` | `43.38%` | `56.62%` | `0.77` | 291,120.00 USD |
| `1H` | `Bitget` | `40.37%` | `59.63%` | `0.68` | 1,880,000.00 USD |
| `1H` | `BingX` | `16.69%` | `83.31%` | `0.20` | 1,130,000.00 USD |
| `1H` | `MEXC` | `29.38%` | `70.62%` | `0.42` | 1,230,000.00 USD |
| `1H` | `Bitunix` | `45.56%` | `54.44%` | `0.84` | 344,640.00 USD |
| `1H` | `Hyperliquid` | `49.19%` | `50.81%` | `0.97` | 327,470.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 581,310.00 USD |
| `1H` | `Crypto.com` | `40.65%` | `59.35%` | `0.68` | 5,960.00 USD |
| `1H` | `WhiteBIT` | `77.68%` | `22.32%` | `3.48` | 210,340.00 USD |
| `1H` | `HTX` | `50.3%` | `49.7%` | `1.01` | 2,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `84.95%` | `15.05%` | `5.64` | 4,430.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `38.75%` | `61.25%` | `0.63` | 20,840.00 USD |
| `1H` | `Whale Positions` | `43.38%` | `56.62%` | `0.77` | 7,390,000.00 USD |
| `1H` | `Global Accounts` | `39.65%` | `60.35%` | `0.66` | 19,400,000.00 USD |
| `4H` | `PAXG` | `42.91%` | `57.09%` | `0.75` | 51,060,000.00 USD |
| `4H` | `Binance` | `47.13%` | `52.87%` | `0.89` | 7,850,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `44.43%` | `55.57%` | `0.80` | 3,510,000.00 USD |
| `4H` | `KuCoin` | `61.24%` | `38.76%` | `1.58` | 251,150.00 USD |
| `4H` | `Gate` | `49.24%` | `50.76%` | `0.97` | 1,960,000.00 USD |
| `4H` | `Bitget` | `46.5%` | `53.5%` | `0.87` | 2,840,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `40.31%` | `59.69%` | `0.68` | 28,950,000.00 USD |
| `4H` | `Bitunix` | `48.2%` | `51.8%` | `0.93` | 1,170,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.74%` | `48.26%` | `1.07` | 2,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `23.09%` | `76.91%` | `0.30` | 1,470,000.00 USD |
| `4H` | `HTX` | `83.42%` | `16.58%` | `5.03` | 157,070.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `85.73%` | `14.27%` | `6.01` | 14,370.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `47.13%` | `52.87%` | `0.89` | 7,850,000.00 USD |
| `4H` | `Global Accounts` | `42.91%` | `57.09%` | `0.75` | 51,060,000.00 USD |


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
| `5m` | 17,160.00 USD | -12,970.00 USD | **`ACCUMULATION`** |
| `15m` | 33,330.00 USD | 129,980.00 USD | **`ACCUMULATION`** |
| `30m` | 97,560.00 USD | 88,220.00 USD | **`ACCUMULATION`** |
| `1h` | 1,910,000.00 USD | 1,190,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,910,000.00 USD | 927,690.00 USD | **`ACCUMULATION`** |
| `4h` | 1,710,000.00 USD | 999,740.00 USD | **`ACCUMULATION`** |
| `6h` | 1,880,000.00 USD | 142,580.00 USD | **`ACCUMULATION`** |
| `8h` | 1,850,000.00 USD | -251,460.00 USD | **`ACCUMULATION`** |
| `12h` | 474,950.00 USD | 205,950.00 USD | **`ACCUMULATION`** |
| `24h` | 574,510.00 USD | 504,770.00 USD | **`ACCUMULATION`** |
| `1w` | -7,680,000.00 USD | -8,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -17,930,000.00 USD | -69,540,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+17.16K` | 15m=`+33.33K` | 1h=`+1.91M` | 24h=`+574.51K`
* Futures Capital Netflows: 5m=`-12.97K` | 15m=`+129.98K` | 1h=`+1.19M` | 24h=`+504.77K`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3987.92` (Risk Distance: `9.07` pts)
  * +2.5R Take Profit: `4019.66`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.11` (Risk Distance: `9.07` pts)
  * +2.5R Take Profit: `3990.37`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4035.74`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
