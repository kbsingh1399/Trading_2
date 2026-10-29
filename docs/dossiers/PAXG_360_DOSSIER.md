# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 23:52:58 IST` (`2026-10-29 18:22:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4011.11` | **Live Ask Quote**: `4011.20` | **Mid Price**: `4011.15`
- **Spread Points**: `9.00` | **Spread BPS**: `0.22 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `4030.79` | VWAP Z-Score: `-1.73` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.78` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.59` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4065.08` | Lower -3.00σ Band: `3996.49`
  * Upper +2.51σ Band: `4059.48` | Lower -2.51σ Band: `4002.10`
  * Upper +2.01σ Band: `4053.76` | Lower -2.01σ Band: `4007.81`
  * Upper +2.00σ Band: `4053.65` | Lower -2.00σ Band: `4007.92`
  * Upper +1.28σ Band: `4045.42` | Lower -1.28σ Band: `4016.15`
  * Upper +1.00σ Band: `4042.22` | Lower -1.00σ Band: `4019.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4015.25` | EMA-20=`4019.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4025.79` (Slope: `+0.0000`) | EMA-100=`4032.03`
  * Institutional Anchors: EMA-144=`4033.22` | EMA-200=`4032.70` (Slope: `-0.0494`) | EMA-233=`4031.72`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4006.70` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4041.12` (Distance: `-0.74%`)
  * Point of Control (POC) = `4027.35` (Distance: `-0.40%`)
  * Value Area Low (VAL) = `4019.01` (Distance: `-0.20%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.72` | Weekly POC=`4015.46` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3995.11` - `4027.20`
  * Optimal Trade Entry (OTE 0.705): `4019.18`
  * Structural Invalidation Anchor (0.786): `4043.24`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4013.92` | `4016.14` | `4013.84` | `4015.27` | `119` | 476,990.00 USD | 423,536.35 USD | `+88.79%` | 974,281.46 USD | `+2.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4015.32` | `4016.65` | `4015.02` | `4016.65` | `25` | 101,951.08 USD | 60,211.51 USD | `+59.06%` | 1,034,492.96 USD | `+0.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4016.60` | `4016.65` | `4016.60` | `4016.65` | `1` | 2,586.72 USD | 1,566.49 USD | `+60.56%` | 1,036,059.46 USD | `-0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4018.05` | `4018.76` | `4011.95` | `4011.96` | `238` | 956,530.83 USD | -295,289.50 USD | `-30.87%` | 401,155.64 USD | `-1.70` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4011.95` | `4016.65` | `4011.95` | `4016.65` | `183` | 735,304.15 USD | 506,416.16 USD | `+68.87%` | 907,571.80 USD | `+2.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4016.60` | `4016.65` | `4016.60` | `4016.65` | `0` | 590.45 USD | -429.78 USD | `-72.79%` | 907,142.02 USD | `-0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 1,062,379.10 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 852,087.28 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4016.65` | `4011.95` | `4016.65` | `184` | 737,890.87 USD | 507,982.65 USD | `+68.84%` | 1,360,069.93 USD | `+0.85` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.95` | `4016.65` | `1,683` | 6,765,937.73 USD | 1,146,108.78 USD | `+16.94%` | 1,523,159.05 USD | `+1.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.95` | `4016.65` | `1,683` | 6,765,937.73 USD | 1,146,108.78 USD | `+16.94%` | 1,523,159.05 USD | `+1.52` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4009.50` | `3.5344` | 14,171.18 USD | 2,032,414.48 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4009.60` | `9.2657` | 37,151.75 USD | 2,018,243.30 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4009.70` | `8.1627` | 32,729.98 USD | 1,981,091.55 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4009.80` | `8.6665` | 34,750.93 USD | 1,948,361.57 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4009.90` | `0.9352` | 3,750.06 USD | 1,913,610.64 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4010.00` | `10.8399` | 43,468.00 USD | 1,909,860.58 USD | `12 orders` | `-0.04%` | `-` |
| `BID` | `4010.10` | `6.1524` | 24,671.74 USD | 1,866,392.58 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4010.20` | `19.6814` | 78,926.35 USD | 1,841,720.84 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `4010.30` | `1.3335` | 5,347.74 USD | 1,762,794.49 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4010.40` | `4.9853` | 19,993.05 USD | 1,757,446.76 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4010.50` | `14.7348` | 59,093.92 USD | 1,737,453.71 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4010.60` | `6.4112` | 25,712.76 USD | 1,678,359.80 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `4010.70` | `24.2982` | 97,452.79 USD | 1,652,647.04 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `4010.80` | `47.6016` | 190,920.50 USD | 1,555,194.25 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4010.90` | `17.1459` | 68,770.49 USD | 1,364,273.75 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4011.00` | `33.3048` | 133,585.55 USD | 1,295,503.26 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4011.10` | `76.9909` | 308,818.20 USD | 1,161,917.71 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4011.20` | `19.4819` | 78,145.80 USD | 853,099.51 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `4011.30` | `46.4430` | 186,296.81 USD | 774,953.71 USD | `11 orders` | `-0.00%` | `-` |
| `BID` | `4011.40` | `146.7460` | 588,656.90 USD | 588,656.90 USD | `27 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4011.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,011.45` | `0.00%` | `-` |
| `ASK` | `4011.50` | `155.6853` | 624,531.58 USD | 624,531.58 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `4012.20` | `4.2937` | 17,227.18 USD | 641,758.76 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4012.30` | `10.6066` | 42,556.86 USD | 684,315.63 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4012.40` | `2.7128` | 10,884.84 USD | 695,200.46 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4012.50` | `1.0000` | 4,012.50 USD | 699,212.96 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4012.60` | `8.4131` | 33,758.41 USD | 732,971.37 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4012.70` | `2.6812` | 10,758.85 USD | 743,730.22 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4012.80` | `2.6118` | 10,480.63 USD | 754,210.85 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4013.10` | `20.8418` | 83,640.23 USD | 837,851.08 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4013.20` | `12.6781` | 50,879.75 USD | 888,730.83 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4013.30` | `1.4344` | 5,756.68 USD | 894,487.51 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4013.40` | `7.4750` | 30,000.17 USD | 924,487.67 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4013.50` | `14.5049` | 58,215.42 USD | 982,703.09 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `4013.60` | `32.3313` | 129,764.91 USD | 1,112,467.99 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4013.70` | `3.0919` | 12,409.96 USD | 1,124,877.95 USD | `3 orders` | `+0.06%` | `-` |
| `ASK` | `4013.80` | `7.4785` | 30,017.20 USD | 1,154,895.16 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `4013.90` | `13.9956` | 56,176.94 USD | 1,211,072.10 USD | `6 orders` | `+0.06%` | `-` |
| `ASK` | `4014.00` | `5.0431` | 20,243.00 USD | 1,231,315.10 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `4014.10` | `9.7052` | 38,957.64 USD | 1,270,272.74 USD | `4 orders` | `+0.07%` | `-` |
| `ASK` | `4014.20` | `17.3764` | 69,752.34 USD | 1,340,025.09 USD | `4 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,558,959.83 USD | `6,373.65` | `4191.43` | `4010.10` | `29022.80` | 1,155,789.37 USD | `+4.52%` | `4X Cross` |
| `57` | `0x4692...164f` | `SHORT` | 25,287,077.86 USD | `6,305.85` | `4134.20` | `4010.10` | `13323.24` | 782,583.64 USD | `+3.09%` | `5X Cross` |
| `72` | `0xb83d...6e36` | `SHORT` | 22,925,979.90 USD | `5,717.06` | `4234.49` | `4010.10` | `27341.66` | 1,282,895.33 USD | `+5.60%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,364,399.56 USD | `4,828.91` | `4157.43` | `4010.10` | `2073.24` | -711,482.76 USD | `-3.67%` | `25X Cross` |
| `149` | `0x645b...87b8` | `LONG` | 14,093,837.31 USD | `3,514.59` | `4129.70` | `4010.10` | `246.29` | -420,367.95 USD | `-2.98%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,105,861.75 USD | `3,268.21` | `4228.94` | `4010.10` | `4408.54` | 715,217.38 USD | `+5.46%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,629,290.40 USD | `2,900.00` | `4364.92` | `4010.10` | `4235.59` | 1,028,985.93 USD | `+8.85%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,822,220.00 USD | `2,200.00` | `4176.09` | `4010.10` | `2459.09` | -365,199.30 USD | `-4.14%` | `25X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,822,220.00 USD | `2,200.00` | `4112.20` | `4010.10` | `4331.08` | 224,634.59 USD | `+2.55%` | `20X Cross` |
| `311` | `0xfc66...ca06` | `SHORT` | 7,967,625.99 USD | `1,986.89` | `4032.86` | `4010.10` | `25108.88` | 45,240.18 USD | `+0.57%` | `3X Cross` |
| `314` | `0xacb6...efbd` | `SHORT` | 7,921,427.63 USD | `1,975.37` | `4048.55` | `4010.10` | `6504.10` | 75,964.09 USD | `+0.96%` | `6X Cross` |
| `380` | `0xc26c...b8f4` | `LONG` | 6,335,764.71 USD | `1,579.95` | `4075.62` | `4010.10` | `0.000000` | -103,532.26 USD | `-1.63%` | `1X Cross` |
| `422` | `0x12d2...f97f` | `LONG` | 5,621,930.82 USD | `1,401.94` | `4278.91` | `4010.10` | `2482.91` | -376,859.76 USD | `-6.70%` | `20X Cross` |
| `576` | `0x63da...8add` | `LONG` | 4,010,100.00 USD | `1,000.00` | `4021.46` | `4010.10` | `3564.03` | -11,360.96 USD | `-0.28%` | `25X Cross` |
| `595` | `0x9aa5...58af` | `LONG` | 3,896,381.58 USD | `971.64` | `4279.98` | `4010.10` | `0.000000` | -262,227.50 USD | `-6.73%` | `20X Cross` |
| `625` | `0xf3dc...1672` | `LONG` | 3,732,375.31 USD | `930.74` | `4024.62` | `4010.10` | `3337.51` | -13,517.25 USD | `-0.36%` | `20X Cross` |
| `685` | `0x4a20...3c26` | `LONG` | 3,358,056.54 USD | `837.40` | `4599.73` | `4010.10` | `0.000000` | -493,763.84 USD | `-14.70%` | `20X Cross` |
| `810` | `0x354b...6425` | `LONG` | 2,868,855.21 USD | `715.41` | `4037.02` | `4010.10` | `0.000000` | -19,260.59 USD | `-0.67%` | `10X Cross` |
| `845` | `0x0fac...7a0a` | `LONG` | 2,752,873.50 USD | `686.49` | `4290.34` | `4010.10` | `1296.73` | -192,385.20 USD | `-6.99%` | `25X Cross` |
| `866` | `0xd8c5...99b0` | `SHORT` | 2,642,450.98 USD | `658.95` | `4175.35` | `4010.10` | `31411.67` | 108,896.07 USD | `+4.12%` | `4X Cross` |
| `917` | `0x625e...a354` | `SHORT` | 2,486,262.00 USD | `620.00` | `4122.81` | `4010.10` | `4342.18` | 69,885.03 USD | `+2.81%` | `20X Cross` |
| `946` | `0xeae3...e8ad` | `SHORT` | 2,406,060.00 USD | `600.00` | `4104.77` | `4010.10` | `4325.20` | 56,805.11 USD | `+2.36%` | `20X Cross` |
| `948` | `0xf285...fa82` | `LONG` | 2,398,464.47 USD | `598.11` | `4146.45` | `4010.10` | `3891.17` | -81,555.08 USD | `-3.40%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,348,357.47 USD | `585.61` | `4082.77` | `4010.10` | `2177.46` | -42,559.51 USD | `-1.81%` | `10X Cross` |
| `1127` | `0x413c...886c` | `LONG` | 2,005,050.00 USD | `500.00` | `4010.43` | `4010.10` | `0.000000` | -166.23 USD | `-0.01%` | `2X Cross` |
| `1134` | `0x61ce...a62b` | `SHORT` | 1,995,038.79 USD | `497.50` | `4071.66` | `4010.10` | `4689.24` | 30,630.01 USD | `+1.54%` | `20X Cross` |
| `1144` | `0x0593...40f9` | `LONG` | 1,989,719.39 USD | `496.18` | `4024.57` | `4010.10` | `3701.65` | -7,184.44 USD | `-0.36%` | `10X Isolated` |
| `1255` | `0x2edd...8179` | `LONG` | 1,825,066.74 USD | `454.70` | `4169.95` | `4013.74` | `0.000000` | -71,031.90 USD | `-3.89%` | `10X Cross` |
| `1259` | `0xead5...69f2` | `LONG` | 1,819,718.82 USD | `453.78` | `4220.88` | `4010.10` | `3538.86` | -95,649.24 USD | `-5.26%` | `5X Isolated` |
| `1318` | `0x7a6d...f79c` | `SHORT` | 1,719,470.47 USD | `428.38` | `4136.09` | `4013.74` | `5856.71` | 52,344.54 USD | `+3.04%` | `10X Cross` |
| `1383` | `0x46fc...1195` | `LONG` | 1,632,224.99 USD | `407.03` | `4055.53` | `4010.10` | `1914.09` | -18,494.83 USD | `-1.13%` | `20X Cross` |
| `1421` | `0x6d15...d374` | `LONG` | 1,604,040.00 USD | `400.00` | `4068.25` | `4010.10` | `3841.73` | -23,260.00 USD | `-1.45%` | `25X Cross` |
| `1422` | `0xee02...309d` | `SHORT` | 1,604,040.00 USD | `400.00` | `4438.84` | `4010.10` | `4226.81` | 171,498.60 USD | `+10.69%` | `25X Isolated` |
| `1451` | `0x02a7...fe9f` | `SHORT` | 1,563,939.00 USD | `390.00` | `4055.02` | `4010.10` | `4306.63` | 17,520.25 USD | `+1.12%` | `25X Cross` |
| `1486` | `0x51f6...2b39` | `LONG` | 1,527,765.44 USD | `380.49` | `4234.66` | `4013.74` | `0.000000` | -83,462.63 USD | `-5.46%` | `10X Cross` |
| `1489` | `0x7e77...b8d2` | `SHORT` | 1,523,838.00 USD | `380.00` | `4131.92` | `4010.10` | `4293.44` | 46,291.64 USD | `+3.04%` | `20X Cross` |
| `1506` | `0x72c2...9b37` | `LONG` | 1,496,293.83 USD | `373.13` | `4000.98` | `4010.10` | `3777.97` | 3,400.31 USD | `+0.23%` | `13X Isolated` |
| `1544` | `0xaa44...b844` | `LONG` | 1,443,636.00 USD | `360.00` | `4043.10` | `4010.10` | `2817.14` | -11,881.63 USD | `-0.82%` | `9X Cross` |
| `1545` | `0x781e...96b7` | `SHORT` | 1,443,139.86 USD | `359.55` | `4365.03` | `4013.74` | `12483.96` | 126,307.62 USD | `+8.75%` | `10X Cross` |
| `1659` | `0xa41f...d50a` | `LONG` | 1,319,170.92 USD | `328.96` | `4468.89` | `4010.10` | `3833.11` | -150,926.93 USD | `-11.44%` | `15X Cross` |
| `1691` | `0x49e9...e1d0` | `SHORT` | 1,297,497.13 USD | `323.56` | `4025.23` | `4010.10` | `29283.96` | 4,895.57 USD | `+0.38%` | `4X Cross` |
| `1710` | `0xada6...6f88` | `LONG` | 1,280,327.08 USD | `319.28` | `4166.46` | `4010.10` | `1865.72` | -49,923.43 USD | `-3.90%` | `5X Cross` |
| `1720` | `0xbf5a...88ba` | `SHORT` | 1,273,827.91 USD | `317.65` | `4091.80` | `4010.10` | `10499.30` | 25,955.12 USD | `+2.04%` | `20X Cross` |
| `1734` | `0xff31...ff6c` | `SHORT` | 1,243,131.00 USD | `310.00` | `4372.43` | `4010.10` | `4789.11` | 112,324.38 USD | `+9.04%` | `10X Isolated` |
| `1896` | `0x50e2...d770` | `LONG` | 1,084,200.31 USD | `270.37` | `4243.58` | `4010.10` | `2562.02` | -63,126.15 USD | `-5.82%` | `20X Cross` |
| `1912` | `0x4c92...4f17` | `SHORT` | 1,069,575.88 USD | `266.72` | `4260.98` | `4010.10` | `6529.01` | 66,916.36 USD | `+6.26%` | `20X Cross` |
| `1987` | `0xd346...c4f3` | `LONG` | 1,023,272.46 USD | `255.17` | `4188.66` | `4010.10` | `3310.35` | -45,564.05 USD | `-4.45%` | `5X Isolated` |
| `2025` | `0x1581...463b` | `LONG` | 1,002,525.00 USD | `250.00` | `4003.77` | `4010.10` | `3504.56` | 1,581.41 USD | `+0.16%` | `15X Cross` |
| `2026` | `0xe47f...758c` | `LONG` | 1,002,525.00 USD | `250.00` | `4020.00` | `4010.10` | `3774.26` | -2,475.00 USD | `-0.25%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.01` (Vol: 250,500.00 USD, Dist: `+2.38%`) | Long MP=`3949.20` (Vol: 281,800.00 USD, Dist: `--1.63%`)
  * 48H Horizon: Short MP=`4110.01` (Vol: 250,500.00 USD, Dist: `+2.38%`) | Long MP=`3949.20` (Vol: 281,800.00 USD, Dist: `--1.63%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.36%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--0.87%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.56%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.51%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3612.10` | 16,490,000.00 USD | 16,490,000.00 USD | 41,480.00 USD | 0.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3613.30` | 4,020,000.00 USD | 4,020,000.00 USD | 2,900.00 USD | 0.00 USD | 789.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3616.40` | 16,440,000.00 USD | 16,440,000.00 USD | 117,220.00 USD | 0.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3617.50` | 4,010,000.00 USD | 4,010,000.00 USD | 17,330.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3620.70` | 16,320,000.00 USD | 16,320,000.00 USD | 63,310.00 USD | 0.00 USD | 10,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.70` | 3,990,000.00 USD | 3,990,000.00 USD | 28,630.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3625.00` | 16,240,000.00 USD | 16,240,000.00 USD | 139,860.00 USD | 0.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.90` | 3,960,000.00 USD | 3,960,000.00 USD | 40,080.00 USD | 0.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3629.30` | 16,080,000.00 USD | 16,080,000.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.10` | 3,910,000.00 USD | 3,910,000.00 USD | 40,930.00 USD | 0.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3633.60` | 15,900,000.00 USD | 15,900,000.00 USD | 108,730.00 USD | 0.00 USD | 27,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.30` | 3,870,000.00 USD | 3,870,000.00 USD | 24,230.00 USD | 0.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.90` | 15,760,000.00 USD | 15,760,000.00 USD | 87,660.00 USD | 0.00 USD | 10,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.50` | 3,840,000.00 USD | 3,840,000.00 USD | 49,740.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3642.20` | 15,660,000.00 USD | 15,660,000.00 USD | 33,140.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3642.70` | 3,780,000.00 USD | 3,780,000.00 USD | 14,550.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3646.50` | 15,620,000.00 USD | 15,620,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3646.90` | 3,760,000.00 USD | 3,760,000.00 USD | 8,210.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3650.80` | 15,590,000.00 USD | 15,590,000.00 USD | 24,210.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.10` | 3,750,000.00 USD | 3,750,000.00 USD | 34,870.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3655.10` | 15,560,000.00 USD | 15,560,000.00 USD | 53,090.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.30` | 3,710,000.00 USD | 3,710,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3659.40` | 15,510,000.00 USD | 15,510,000.00 USD | 11,970.00 USD | 0.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3659.50` | 3,690,000.00 USD | 3,690,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3663.70` | 3,680,000.00 USD | 3,680,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3663.70` | 15,490,000.00 USD | 15,490,000.00 USD | 7,390.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3668.00` | 15,480,000.00 USD | 15,480,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3672.10` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3831.40` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3835.70` | 15,470,000.00 USD | 15,470,000.00 USD | 74,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3840.00` | 15,390,000.00 USD | 15,390,000.00 USD | 358,280.00 USD | 0.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3844.30` | 15,000,000.00 USD | 15,000,000.00 USD | 470,290.00 USD | 0.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3848.60` | 14,460,000.00 USD | 14,460,000.00 USD | 537,650.00 USD | 0.00 USD | 68,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.70` | 3,670,000.00 USD | 3,670,000.00 USD | 2,810.00 USD | 0.00 USD | 935.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.90` | 13,860,000.00 USD | 13,860,000.00 USD | 133,680.00 USD | 0.00 USD | 50,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.90` | 3,670,000.00 USD | 3,670,000.00 USD | 31,080.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3857.20` | 13,670,000.00 USD | 13,670,000.00 USD | 348,540.00 USD | 0.00 USD | 16,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.10` | 3,630,000.00 USD | 3,630,000.00 USD | 60,700.00 USD | 0.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3861.50` | 13,310,000.00 USD | 13,310,000.00 USD | 185,410.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.30` | 3,560,000.00 USD | 3,560,000.00 USD | 143,090.00 USD | 0.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3865.80` | 13,090,000.00 USD | 13,090,000.00 USD | 374,550.00 USD | 0.00 USD | 67,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.50` | 3,400,000.00 USD | 3,400,000.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3870.10` | 12,650,000.00 USD | 12,650,000.00 USD | 541,600.00 USD | 0.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.70` | 3,250,000.00 USD | 3,250,000.00 USD | 107,400.00 USD | 0.00 USD | 16,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3874.40` | 12,070,000.00 USD | 12,070,000.00 USD | 398,220.00 USD | 0.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.90` | 3,130,000.00 USD | 3,130,000.00 USD | 148,870.00 USD | 0.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3878.70` | 11,630,000.00 USD | 11,630,000.00 USD | 451,810.00 USD | 0.00 USD | 65,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3882.10` | 2,970,000.00 USD | 2,970,000.00 USD | 103,740.00 USD | 0.00 USD | 32,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3883.00` | 11,110,000.00 USD | 11,110,000.00 USD | 198,420.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3886.30` | 2,840,000.00 USD | 2,840,000.00 USD | 53,410.00 USD | 0.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3887.30` | 10,870,000.00 USD | 10,870,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3890.50` | 2,780,000.00 USD | 2,780,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3891.60` | 10,790,000.00 USD | 10,790,000.00 USD | 129,360.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3894.70` | 2,710,000.00 USD | 2,710,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.90` | 10,640,000.00 USD | 10,640,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.90` | 2,600,000.00 USD | 2,600,000.00 USD | 53,880.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3900.20` | 10,530,000.00 USD | 10,530,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.10` | 2,540,000.00 USD | 2,540,000.00 USD | 50,640.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3904.50` | 10,420,000.00 USD | 10,420,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.30` | 2,490,000.00 USD | 2,490,000.00 USD | 23,750.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3908.80` | 10,380,000.00 USD | 10,380,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.10` | 10,330,000.00 USD | 10,330,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.70` | 2,460,000.00 USD | 2,460,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.40` | 10,300,000.00 USD | 10,300,000.00 USD | 459,090.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3921.70` | 9,820,000.00 USD | 9,820,000.00 USD | 1,020,000.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.00` | 8,720,000.00 USD | 8,720,000.00 USD | 744,170.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.30` | 7,830,000.00 USD | 7,830,000.00 USD | 809,190.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3932.50` | 2,450,000.00 USD | 2,450,000.00 USD | 5,620.00 USD | 0.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.60` | 6,870,000.00 USD | 6,870,000.00 USD | 445,960.00 USD | 0.00 USD | 49,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3936.70` | 2,440,000.00 USD | 2,440,000.00 USD | 62,160.00 USD | 0.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,380,000.00 USD | 6,380,000.00 USD | 468,890.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.90` | 2,370,000.00 USD | 2,370,000.00 USD | 100,800.00 USD | 0.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.20` | 5,880,000.00 USD | 5,880,000.00 USD | 489,070.00 USD | 0.00 USD | 74,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3945.10` | 2,260,000.00 USD | 2,260,000.00 USD | 301,570.00 USD | 0.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.50` | 5,310,000.00 USD | 5,310,000.00 USD | 859,010.00 USD | 0.00 USD | 114,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.30` | 1,930,000.00 USD | 1,930,000.00 USD | 208,570.00 USD | 0.00 USD | 39,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.80` | 4,340,000.00 USD | 4,340,000.00 USD | 1,000,000.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.50` | 1,680,000.00 USD | 1,680,000.00 USD | 252,570.00 USD | 0.00 USD | 38,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3956.10` | 3,240,000.00 USD | 3,240,000.00 USD | 892,120.00 USD | 0.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.70` | 1,390,000.00 USD | 1,390,000.00 USD | 221,170.00 USD | 0.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3960.40` | 2,250,000.00 USD | 2,250,000.00 USD | 651,020.00 USD | 0.00 USD | 91,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.90` | 1,150,000.00 USD | 1,150,000.00 USD | 297,460.00 USD | 0.00 USD | 53,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.70` | 1,510,000.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.10` | 800,350.00 USD | 800,350.00 USD | 83,830.00 USD | 0.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3969.00` | 1,090,000.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3970.30` | 693,460.00 USD | 693,460.00 USD | 72,410.00 USD | 0.00 USD | 29,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3973.30` | 874,480.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3974.50` | 591,750.00 USD | 591,750.00 USD | 234,950.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3977.60` | 646,890.00 USD | 646,890.00 USD | 241,180.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3978.70` | 345,040.00 USD | 345,040.00 USD | 82,270.00 USD | 0.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.90` | 388,050.00 USD | 388,050.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3982.90` | 249,090.00 USD | 249,090.00 USD | 110,950.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3986.20` | 219,990.00 USD | 219,990.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3987.10` | 113,340.00 USD | 113,340.00 USD | 51,480.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3990.50` | 120,370.00 USD | 120,370.00 USD | 73,770.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3991.30` | 51,990.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3994.80` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3995.50` | 20,280.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3999.70` | 15,300.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4072.20` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4076.50` | 372,250.00 USD | 372,250.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4080.80` | 1,160,000.00 USD | 1,160,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.10` | 2,200,000.00 USD | 2,200,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4089.40` | 3,260,000.00 USD | 3,260,000.00 USD | 936,410.00 USD | 0.00 USD | 122,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4093.70` | 3,600,000.00 USD | 3,600,000.00 USD | 239,740.00 USD | 0.00 USD | 101,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4096.30` | 73,270.00 USD | 73,270.00 USD | 67,780.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.00` | 4,330,000.00 USD | 4,330,000.00 USD | 697,090.00 USD | 0.00 USD | 31,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.50` | 128,390.00 USD | 128,390.00 USD | 46,950.00 USD | 0.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.30` | 4,670,000.00 USD | 4,670,000.00 USD | 292,950.00 USD | 0.00 USD | 55,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.70` | 315,770.00 USD | 315,770.00 USD | 175,760.00 USD | 0.00 USD | 11,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.60` | 5,410,000.00 USD | 5,410,000.00 USD | 625,970.00 USD | 0.00 USD | 104,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.90` | 655,730.00 USD | 655,730.00 USD | 292,970.00 USD | 0.00 USD | 46,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.90` | 6,710,000.00 USD | 6,710,000.00 USD | 1,230,000.00 USD | 0.00 USD | 79,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4113.10` | 919,230.00 USD | 919,230.00 USD | 221,950.00 USD | 0.00 USD | 41,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.20` | 7,440,000.00 USD | 7,440,000.00 USD | 634,940.00 USD | 0.00 USD | 90,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.30` | 1,140,000.00 USD | 1,140,000.00 USD | 199,820.00 USD | 0.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,500,000.00 USD | 8,500,000.00 USD | 935,130.00 USD | 0.00 USD | 125,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.50` | 1,470,000.00 USD | 1,470,000.00 USD | 295,790.00 USD | 0.00 USD | 31,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.80` | 9,010,000.00 USD | 9,010,000.00 USD | 417,860.00 USD | 0.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.70` | 1,670,000.00 USD | 1,670,000.00 USD | 157,260.00 USD | 0.00 USD | 49,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4128.10` | 9,260,000.00 USD | 9,260,000.00 USD | 202,410.00 USD | 0.00 USD | 49,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.90` | 1,790,000.00 USD | 1,790,000.00 USD | 106,820.00 USD | 0.00 USD | 12,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.40` | 9,500,000.00 USD | 9,500,000.00 USD | 199,830.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4134.10` | 1,940,000.00 USD | 1,940,000.00 USD | 118,050.00 USD | 0.00 USD | 26,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.70` | 9,730,000.00 USD | 9,730,000.00 USD | 204,390.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.30` | 2,140,000.00 USD | 2,140,000.00 USD | 186,870.00 USD | 0.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4141.00` | 9,920,000.00 USD | 9,920,000.00 USD | 184,250.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4142.50` | 2,260,000.00 USD | 2,260,000.00 USD | 98,750.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4145.30` | 10,100,000.00 USD | 10,100,000.00 USD | 147,710.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.70` | 2,370,000.00 USD | 2,370,000.00 USD | 99,160.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4149.60` | 10,250,000.00 USD | 10,250,000.00 USD | 110,560.00 USD | 0.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.90` | 2,430,000.00 USD | 2,430,000.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.90` | 10,280,000.00 USD | 10,280,000.00 USD | 36,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4158.20` | 10,710,000.00 USD | 10,710,000.00 USD | 410,790.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.30` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4162.50` | 11,170,000.00 USD | 11,170,000.00 USD | 407,770.00 USD | 0.00 USD | 45,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.50` | 2,450,000.00 USD | 2,450,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4166.80` | 11,630,000.00 USD | 11,630,000.00 USD | 392,410.00 USD | 0.00 USD | 67,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4171.10` | 12,050,000.00 USD | 12,050,000.00 USD | 350,430.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4175.40` | 12,250,000.00 USD | 12,250,000.00 USD | 181,060.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.10` | 2,470,000.00 USD | 2,470,000.00 USD | 21,490.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4179.70` | 12,510,000.00 USD | 12,510,000.00 USD | 243,230.00 USD | 0.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.30` | 2,510,000.00 USD | 2,510,000.00 USD | 35,880.00 USD | 0.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4184.00` | 12,760,000.00 USD | 12,760,000.00 USD | 219,800.00 USD | 0.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.50` | 2,590,000.00 USD | 2,590,000.00 USD | 75,310.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4188.30` | 13,150,000.00 USD | 13,150,000.00 USD | 327,710.00 USD | 0.00 USD | 68,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.70` | 2,740,000.00 USD | 2,740,000.00 USD | 130,100.00 USD | 0.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4192.60` | 13,710,000.00 USD | 13,710,000.00 USD | 524,540.00 USD | 0.00 USD | 32,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.90` | 2,890,000.00 USD | 2,890,000.00 USD | 133,080.00 USD | 0.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.90` | 14,140,000.00 USD | 14,140,000.00 USD | 389,870.00 USD | 0.00 USD | 44,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.10` | 2,990,000.00 USD | 2,990,000.00 USD | 86,510.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4201.20` | 14,670,000.00 USD | 14,670,000.00 USD | 460,170.00 USD | 0.00 USD | 65,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.30` | 3,160,000.00 USD | 3,160,000.00 USD | 153,280.00 USD | 0.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.50` | 3,280,000.00 USD | 3,280,000.00 USD | 93,500.00 USD | 0.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4205.50` | 14,870,000.00 USD | 14,870,000.00 USD | 165,880.00 USD | 0.00 USD | 33,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.70` | 3,340,000.00 USD | 3,340,000.00 USD | 53,410.00 USD | 0.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4209.80` | 14,970,000.00 USD | 14,970,000.00 USD | 74,330.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.90` | 3,380,000.00 USD | 3,380,000.00 USD | 26,200.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4214.10` | 15,080,000.00 USD | 15,080,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4218.10` | 3,510,000.00 USD | 3,510,000.00 USD | 121,750.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4218.40` | 15,210,000.00 USD | 15,210,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4222.30` | 3,550,000.00 USD | 3,550,000.00 USD | 31,190.00 USD | 0.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4222.70` | 15,350,000.00 USD | 15,350,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4226.50` | 3,610,000.00 USD | 3,610,000.00 USD | 52,630.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4227.00` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4230.70` | 3,640,000.00 USD | 3,640,000.00 USD | 28,590.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4231.30` | 15,450,000.00 USD | 15,450,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4234.90` | 3,660,000.00 USD | 3,660,000.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4235.60` | 15,470,000.00 USD | 15,470,000.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4243.30` | 3,670,000.00 USD | 3,670,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4390.40` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4399.00` | 15,620,000.00 USD | 15,620,000.00 USD | 141,850.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4403.30` | 15,780,000.00 USD | 15,780,000.00 USD | 137,570.00 USD | 0.00 USD | 18,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4407.60` | 15,940,000.00 USD | 15,940,000.00 USD | 145,420.00 USD | 0.00 USD | 19,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.90` | 16,010,000.00 USD | 16,010,000.00 USD | 50,960.00 USD | 0.00 USD | 22,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4415.50` | 3,670,000.00 USD | 3,670,000.00 USD | 2,900.00 USD | 0.00 USD | 789.57 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4416.20` | 16,070,000.00 USD | 16,070,000.00 USD | 51,780.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4419.70` | 3,690,000.00 USD | 3,690,000.00 USD | 13,270.00 USD | 0.00 USD | 389.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4420.50` | 16,160,000.00 USD | 16,160,000.00 USD | 85,120.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4423.90` | 3,710,000.00 USD | 3,710,000.00 USD | 17,290.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.80` | 16,210,000.00 USD | 16,210,000.00 USD | 34,880.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4428.10` | 3,750,000.00 USD | 3,750,000.00 USD | 40,670.00 USD | 0.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4429.10` | 16,300,000.00 USD | 16,300,000.00 USD | 77,220.00 USD | 0.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.30` | 3,780,000.00 USD | 3,780,000.00 USD | 21,280.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4433.40` | 16,510,000.00 USD | 16,510,000.00 USD | 201,720.00 USD | 0.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.60` | 3,790,000.00 USD | 3,790,000.00 USD | 11,970.00 USD | 0.00 USD | 1,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4437.70` | 16,610,000.00 USD | 16,610,000.00 USD | 82,170.00 USD | 0.00 USD | 14,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.00` | 16,750,000.00 USD | 16,750,000.00 USD | 114,900.00 USD | 0.00 USD | 23,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.30` | 16,810,000.00 USD | 16,810,000.00 USD | 48,670.00 USD | 0.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.30` | 16,830,000.00 USD | 16,830,000.00 USD | 25,230.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |

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
| `7D` | `3612.10` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 41,480.00 USD | 0.00 USD | 16,020.00 USD |
| `1D` | `3613.30` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 2,900.00 USD | 0.00 USD | 789.57 USD |
| `7D` | `3616.40` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 117,220.00 USD | 0.00 USD | 4,740.00 USD |
| `1D` | `3617.50` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 17,330.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `3620.70` | 16,320,000.00 USD | 0.00 USD | 16,320,000.00 USD | 63,310.00 USD | 0.00 USD | 10,550.00 USD |
| `1D` | `3621.70` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 28,630.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `3625.00` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 139,860.00 USD | 0.00 USD | 23,510.00 USD |
| `1D` | `3625.90` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 40,080.00 USD | 0.00 USD | 9,500.00 USD |
| `7D` | `3629.30` | 16,080,000.00 USD | 0.00 USD | 16,080,000.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3630.10` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 40,930.00 USD | 0.00 USD | 5,370.00 USD |
| `7D` | `3633.60` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 108,730.00 USD | 0.00 USD | 27,200.00 USD |
| `1D` | `3634.30` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 24,230.00 USD | 0.00 USD | 3,060.00 USD |
| `7D` | `3637.90` | 15,760,000.00 USD | 0.00 USD | 15,760,000.00 USD | 87,660.00 USD | 0.00 USD | 10,810.00 USD |
| `1D` | `3638.50` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 49,740.00 USD | 0.00 USD | 10,330.00 USD |
| `7D` | `3642.20` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 33,140.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `3642.70` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 14,550.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3646.50` | 15,620,000.00 USD | 0.00 USD | 15,620,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3646.90` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 8,210.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3650.80` | 15,590,000.00 USD | 0.00 USD | 15,590,000.00 USD | 24,210.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3651.10` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 34,870.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `3655.10` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 53,090.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3655.30` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `3659.40` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 11,970.00 USD | 0.00 USD | 5,410.00 USD |
| `1D` | `3659.50` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD |
| `1D` | `3663.70` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3663.70` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 7,390.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3668.00` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3672.10` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3831.40` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3835.70` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 74,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3840.00` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 358,280.00 USD | 0.00 USD | 33,930.00 USD |
| `7D` | `3844.30` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 470,290.00 USD | 0.00 USD | 66,380.00 USD |
| `7D` | `3848.60` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 537,650.00 USD | 0.00 USD | 68,950.00 USD |
| `1D` | `3852.70` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 2,810.00 USD | 0.00 USD | 935.06 USD |
| `7D` | `3852.90` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 133,680.00 USD | 0.00 USD | 50,970.00 USD |
| `1D` | `3856.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 31,080.00 USD | 0.00 USD | 2,290.00 USD |
| `7D` | `3857.20` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 348,540.00 USD | 0.00 USD | 16,710.00 USD |
| `1D` | `3861.10` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 60,700.00 USD | 0.00 USD | 8,050.00 USD |
| `7D` | `3861.50` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 185,410.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `3865.30` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 143,090.00 USD | 0.00 USD | 17,020.00 USD |
| `7D` | `3865.80` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 374,550.00 USD | 0.00 USD | 67,840.00 USD |
| `1D` | `3869.50` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `3870.10` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 541,600.00 USD | 0.00 USD | 43,240.00 USD |
| `1D` | `3873.70` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 107,400.00 USD | 0.00 USD | 16,830.00 USD |
| `7D` | `3874.40` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 398,220.00 USD | 0.00 USD | 36,760.00 USD |
| `1D` | `3877.90` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 148,870.00 USD | 0.00 USD | 7,910.00 USD |
| `7D` | `3878.70` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 451,810.00 USD | 0.00 USD | 65,180.00 USD |
| `1D` | `3882.10` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 103,740.00 USD | 0.00 USD | 32,050.00 USD |
| `7D` | `3883.00` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 198,420.00 USD | 0.00 USD | 39,990.00 USD |
| `1D` | `3886.30` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 53,410.00 USD | 0.00 USD | 6,590.00 USD |
| `7D` | `3887.30` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `1D` | `3890.50` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD |
| `7D` | `3891.60` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 129,360.00 USD | 0.00 USD | 19,970.00 USD |
| `1D` | `3894.70` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3895.90` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `3898.90` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 53,880.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3900.20` | 10,530,000.00 USD | 0.00 USD | 10,530,000.00 USD | 99,580.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3903.10` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 50,640.00 USD | 0.00 USD | 5,290.00 USD |
| `7D` | `3904.50` | 10,420,000.00 USD | 0.00 USD | 10,420,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `1D` | `3907.30` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 23,750.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3908.80` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `3913.10` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3915.70` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3917.40` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 459,090.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3921.70` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 1,020,000.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `3926.00` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 744,170.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `3930.30` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 809,190.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `3932.50` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 5,620.00 USD | 0.00 USD | 1,870.00 USD |
| `7D` | `3934.60` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 445,960.00 USD | 0.00 USD | 49,590.00 USD |
| `1D` | `3936.70` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 62,160.00 USD | 0.00 USD | 4,580.00 USD |
| `7D` | `3938.90` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 468,890.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3940.90` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 100,800.00 USD | 0.00 USD | 13,070.00 USD |
| `7D` | `3943.20` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 489,070.00 USD | 0.00 USD | 74,120.00 USD |
| `1D` | `3945.10` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 301,570.00 USD | 0.00 USD | 29,800.00 USD |
| `7D` | `3947.50` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 859,010.00 USD | 0.00 USD | 114,580.00 USD |
| `1D` | `3949.30` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 208,570.00 USD | 0.00 USD | 39,430.00 USD |
| `7D` | `3951.80` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 1,000,000.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3953.50` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 252,570.00 USD | 0.00 USD | 38,560.00 USD |
| `7D` | `3956.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 892,120.00 USD | 0.00 USD | 100,750.00 USD |
| `1D` | `3957.70` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 221,170.00 USD | 0.00 USD | 16,030.00 USD |
| `7D` | `3960.40` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 651,020.00 USD | 0.00 USD | 91,830.00 USD |
| `1D` | `3961.90` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 297,460.00 USD | 0.00 USD | 53,190.00 USD |
| `7D` | `3964.70` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD |
| `1D` | `3966.10` | 800,350.00 USD | 0.00 USD | 800,350.00 USD | 83,830.00 USD | 0.00 USD | 23,060.00 USD |
| `7D` | `3969.00` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `1D` | `3970.30` | 693,460.00 USD | 0.00 USD | 693,460.00 USD | 72,410.00 USD | 0.00 USD | 29,300.00 USD |
| `7D` | `3973.30` | 874,480.00 USD | 0.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3974.50` | 591,750.00 USD | 0.00 USD | 591,750.00 USD | 234,950.00 USD | 0.00 USD | 11,770.00 USD |
| `7D` | `3977.60` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 241,180.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3978.70` | 345,040.00 USD | 0.00 USD | 345,040.00 USD | 82,270.00 USD | 0.00 USD | 13,680.00 USD |
| `7D` | `3981.90` | 388,050.00 USD | 0.00 USD | 388,050.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `3982.90` | 249,090.00 USD | 0.00 USD | 249,090.00 USD | 110,950.00 USD | 0.00 USD | 24,800.00 USD |
| `7D` | `3986.20` | 219,990.00 USD | 0.00 USD | 219,990.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `3987.10` | 113,340.00 USD | 0.00 USD | 113,340.00 USD | 51,480.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3990.50` | 120,370.00 USD | 0.00 USD | 120,370.00 USD | 73,770.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3991.30` | 51,990.00 USD | 0.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3994.80` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3995.50` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `3999.70` | 15,300.00 USD | 0.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4014.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4014.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4072.20` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4076.50` | 372,250.00 USD | 372,250.00 USD | 0.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `4080.80` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `4085.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `4089.40` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 936,410.00 USD | 0.00 USD | 122,920.00 USD |
| `7D` | `4093.70` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 239,740.00 USD | 0.00 USD | 101,950.00 USD |
| `1D` | `4096.30` | 73,270.00 USD | 73,270.00 USD | 0.00 USD | 67,780.00 USD | 0.00 USD | 5,490.00 USD |
| `7D` | `4098.00` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 697,090.00 USD | 0.00 USD | 31,660.00 USD |
| `1D` | `4100.50` | 128,390.00 USD | 128,390.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 8,160.00 USD |
| `7D` | `4102.30` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 292,950.00 USD | 0.00 USD | 55,820.00 USD |
| `1D` | `4104.70` | 315,770.00 USD | 315,770.00 USD | 0.00 USD | 175,760.00 USD | 0.00 USD | 11,620.00 USD |
| `7D` | `4106.60` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 625,970.00 USD | 0.00 USD | 104,820.00 USD |
| `1D` | `4108.90` | 655,730.00 USD | 655,730.00 USD | 0.00 USD | 292,970.00 USD | 0.00 USD | 46,990.00 USD |
| `7D` | `4110.90` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 79,390.00 USD |
| `1D` | `4113.10` | 919,230.00 USD | 919,230.00 USD | 0.00 USD | 221,950.00 USD | 0.00 USD | 41,550.00 USD |
| `7D` | `4115.20` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 634,940.00 USD | 0.00 USD | 90,390.00 USD |
| `1D` | `4117.30` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 199,820.00 USD | 0.00 USD | 20,170.00 USD |
| `7D` | `4119.50` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 935,130.00 USD | 0.00 USD | 125,510.00 USD |
| `1D` | `4121.50` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 295,790.00 USD | 0.00 USD | 31,280.00 USD |
| `7D` | `4123.80` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 91,610.00 USD |
| `1D` | `4125.70` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 157,260.00 USD | 0.00 USD | 49,010.00 USD |
| `7D` | `4128.10` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 49,090.00 USD |
| `1D` | `4129.90` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 106,820.00 USD | 0.00 USD | 12,430.00 USD |
| `7D` | `4132.40` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 199,830.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4134.10` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 118,050.00 USD | 0.00 USD | 26,290.00 USD |
| `7D` | `4136.70` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 204,390.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4138.30` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 186,870.00 USD | 0.00 USD | 16,930.00 USD |
| `7D` | `4141.00` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 184,250.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4142.50` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 98,750.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4145.30` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4146.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 99,160.00 USD | 0.00 USD | 10,580.00 USD |
| `7D` | `4149.60` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 110,560.00 USD | 0.00 USD | 32,540.00 USD |
| `1D` | `4150.90` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.90` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 36,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4158.20` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 410,790.00 USD | 0.00 USD | 17,920.00 USD |
| `1D` | `4159.30` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4162.50` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 407,770.00 USD | 0.00 USD | 45,580.00 USD |
| `1D` | `4163.50` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4166.80` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 392,410.00 USD | 0.00 USD | 67,510.00 USD |
| `7D` | `4171.10` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 350,430.00 USD | 0.00 USD | 70,160.00 USD |
| `7D` | `4175.40` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 181,060.00 USD | 0.00 USD | 23,500.00 USD |
| `1D` | `4176.10` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 21,490.00 USD | 0.00 USD | 2,750.00 USD |
| `7D` | `4179.70` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 243,230.00 USD | 0.00 USD | 15,340.00 USD |
| `1D` | `4180.30` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 35,880.00 USD | 0.00 USD | 4,080.00 USD |
| `7D` | `4184.00` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 219,800.00 USD | 0.00 USD | 27,490.00 USD |
| `1D` | `4184.50` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 75,310.00 USD | 0.00 USD | 5,810.00 USD |
| `7D` | `4188.30` | 13,150,000.00 USD | 13,150,000.00 USD | 0.00 USD | 327,710.00 USD | 0.00 USD | 68,830.00 USD |
| `1D` | `4188.70` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 130,100.00 USD | 0.00 USD | 20,580.00 USD |
| `7D` | `4192.60` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 524,540.00 USD | 0.00 USD | 32,190.00 USD |
| `1D` | `4192.90` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 133,080.00 USD | 0.00 USD | 18,490.00 USD |
| `7D` | `4196.90` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 389,870.00 USD | 0.00 USD | 44,580.00 USD |
| `1D` | `4197.10` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 86,510.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4201.20` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 460,170.00 USD | 0.00 USD | 65,180.00 USD |
| `1D` | `4201.30` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 153,280.00 USD | 0.00 USD | 9,890.00 USD |
| `1D` | `4205.50` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 93,500.00 USD | 0.00 USD | 27,080.00 USD |
| `7D` | `4205.50` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 165,880.00 USD | 0.00 USD | 33,520.00 USD |
| `1D` | `4209.70` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 53,410.00 USD | 0.00 USD | 9,220.00 USD |
| `7D` | `4209.80` | 14,970,000.00 USD | 14,970,000.00 USD | 0.00 USD | 74,330.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `4213.90` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 26,200.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4214.10` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `1D` | `4218.10` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 121,750.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `4218.40` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD |
| `1D` | `4222.30` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 31,190.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `4222.70` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `4226.50` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 52,630.00 USD | 0.00 USD | 12,400.00 USD |
| `7D` | `4227.00` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,710.00 USD |
| `1D` | `4230.70` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4231.30` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD |
| `1D` | `4234.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4235.60` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 23,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4243.30` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4390.40` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4399.00` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 141,850.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4403.30` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 137,570.00 USD | 0.00 USD | 18,550.00 USD |
| `7D` | `4407.60` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 145,420.00 USD | 0.00 USD | 19,100.00 USD |
| `7D` | `4411.90` | 16,010,000.00 USD | 16,010,000.00 USD | 0.00 USD | 50,960.00 USD | 0.00 USD | 22,970.00 USD |
| `1D` | `4415.50` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 2,900.00 USD | 0.00 USD | 789.57 USD |
| `7D` | `4416.20` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4419.70` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 13,270.00 USD | 0.00 USD | 389.21 USD |
| `7D` | `4420.50` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 85,120.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4423.90` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 17,290.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `4424.80` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 34,880.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `4428.10` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD | 4,050.00 USD |
| `7D` | `4429.10` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 77,220.00 USD | 0.00 USD | 18,950.00 USD |
| `1D` | `4432.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 21,280.00 USD | 0.00 USD | 5,750.00 USD |
| `7D` | `4433.40` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 201,720.00 USD | 0.00 USD | 10,210.00 USD |
| `1D` | `4433.60` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 11,970.00 USD | 0.00 USD | 1,330.00 USD |
| `7D` | `4437.70` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 82,170.00 USD | 0.00 USD | 14,310.00 USD |
| `7D` | `4442.00` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 114,900.00 USD | 0.00 USD | 23,290.00 USD |
| `7D` | `4446.30` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 48,670.00 USD | 0.00 USD | 9,170.00 USD |
| `7D` | `4448.30` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 25,230.00 USD | 0.00 USD | 1,890.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.24M` | Total OI Tokens: `68,299.5 PAXG`
  * 1h OI Change: `-0.46%` | 4h OI Change: `-0.62%` | 24h OI Change: `+0.34%`
  * Exchange Breakdown: Binance=`106.99M` | Bybit=`19.98M` | OKX=`-` | Hyperliquid=`25.03M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.17K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `79.39%` | `20.61%` | `3.85` | 1,290,000.00 USD |
| `15M` | `Binance` | `86.13%` | `13.87%` | `6.21` | 933,440.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `90.08%` | `9.92%` | `9.08` | 26,000.00 USD |
| `15M` | `KuCoin` | `36.28%` | `63.72%` | `0.57` | 112,070.00 USD |
| `15M` | `Gate` | `65.59%` | `34.41%` | `1.91` | 25,100.00 USD |
| `15M` | `Bitget` | `48.35%` | `51.65%` | `0.94` | 60,930.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `41.29%` | `58.71%` | `0.70` | 2,050.00 USD |
| `15M` | `Bitunix` | `82.73%` | `17.27%` | `4.79` | 22,970.00 USD |
| `15M` | `Hyperliquid` | `72.68%` | `27.32%` | `2.66` | 27,180.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `95.76%` | `4.24%` | `22.58` | 64,180.00 USD |
| `15M` | `HTX` | `52.47%` | `47.53%` | `1.10` | 3,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `84.68%` | `15.32%` | `5.53` | 2,750.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 1,860.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.89%` | `73.11%` | `0.37` | 6,320.00 USD |
| `15M` | `Whale Positions` | `86.13%` | `13.87%` | `6.21` | 933,440.00 USD |
| `15M` | `Global Accounts` | `79.39%` | `20.61%` | `3.85` | 1,290,000.00 USD |
| `1H` | `PAXG` | `44.45%` | `55.55%` | `0.80` | 5,600,000.00 USD |
| `1H` | `Binance` | `54.63%` | `45.37%` | `1.20` | 2,540,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `57.56%` | `42.44%` | `1.36` | 105,520.00 USD |
| `1H` | `KuCoin` | `51.48%` | `48.52%` | `1.06` | 400,600.00 USD |
| `1H` | `Gate` | `78.79%` | `21.21%` | `3.71` | 92,240.00 USD |
| `1H` | `Bitget` | `42.05%` | `57.95%` | `0.73` | 286,120.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `2.32%` | `97.68%` | `0.02` | 496,330.00 USD |
| `1H` | `Bitunix` | `48.74%` | `51.26%` | `0.95` | 77,780.00 USD |
| `1H` | `Hyperliquid` | `27.88%` | `72.12%` | `0.39` | 1,160,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `72.5%` | `27.5%` | `2.64` | 346,960.00 USD |
| `1H` | `HTX` | `51.26%` | `48.74%` | `1.05` | 17,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `11.61%` | `88.39%` | `0.13` | 20,570.00 USD |
| `1H` | `Aster` | `31.38%` | `68.62%` | `0.46` | 7,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `5.81%` | `94.19%` | `0.06` | 44,840.00 USD |
| `1H` | `Whale Positions` | `54.63%` | `45.37%` | `1.20` | 2,540,000.00 USD |
| `1H` | `Global Accounts` | `44.45%` | `55.55%` | `0.80` | 5,600,000.00 USD |
| `4H` | `PAXG` | `49.66%` | `50.34%` | `0.99` | 81,000,000.00 USD |
| `4H` | `Binance` | `53.59%` | `46.41%` | `1.15` | 5,770,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `36.59%` | `63.41%` | `0.58` | 5,680,000.00 USD |
| `4H` | `KuCoin` | `47.54%` | `52.46%` | `0.91` | 462,060.00 USD |
| `4H` | `Gate` | `68.27%` | `31.73%` | `2.15` | 1,920,000.00 USD |
| `4H` | `Bitget` | `49.48%` | `50.52%` | `0.98` | 2,640,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `8.6%` | `91.4%` | `0.09` | 54,540,000.00 USD |
| `4H` | `Bitunix` | `54.43%` | `45.57%` | `1.19` | 2,190,000.00 USD |
| `4H` | `Hyperliquid` | `40.57%` | `59.43%` | `0.68` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 5,840,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `47.38%` | `52.62%` | `0.90` | 1,730,000.00 USD |
| `4H` | `HTX` | `45.55%` | `54.45%` | `0.84` | 67,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.66%` | `70.34%` | `0.42` | 149,650.00 USD |
| `4H` | `Aster` | `83.28%` | `16.72%` | `4.98` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `15.28%` | `84.72%` | `0.18` | 0.00 USD |
| `4H` | `Whale Positions` | `53.59%` | `46.41%` | `1.15` | 5,770,000.00 USD |
| `4H` | `Global Accounts` | `49.66%` | `50.34%` | `0.99` | 81,000,000.00 USD |


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
| `5m` | -35,700.00 USD | 43,620.00 USD | **`ACCUMULATION`** |
| `15m` | -22,390.00 USD | 478,120.00 USD | **`ACCUMULATION`** |
| `30m` | -69,940.00 USD | 187,700.00 USD | **`ACCUMULATION`** |
| `1h` | -247,460.00 USD | 76,820.00 USD | **`DISTRIBUTION`** |
| `2h` | 212,080.00 USD | 869,380.00 USD | **`ACCUMULATION`** |
| `4h` | 564,520.00 USD | 460,490.00 USD | **`ACCUMULATION`** |
| `6h` | 207,350.00 USD | 1,030,000.00 USD | **`ACCUMULATION`** |
| `8h` | 64,800.00 USD | 1,600,000.00 USD | **`ACCUMULATION`** |
| `12h` | 43,550.00 USD | 660,900.00 USD | **`ACCUMULATION`** |
| `24h` | -306,020.00 USD | 923,430.00 USD | **`ACCUMULATION`** |
| `1w` | -8,750,000.00 USD | -7,620,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,140,000.00 USD | -72,240,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-35.70K` | 15m=`-22.39K` | 1h=`-247.46K` | 24h=`-306.02K`
* Futures Capital Netflows: 5m=`+43.62K` | 15m=`+478.12K` | 1h=`+76.82K` | 24h=`+923.43K`
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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4019.01` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.54` (Risk Distance: `9.47` pts)
  * +2.5R Take Profit: `4042.69`
  * Mathematical Lot Sizing: **`1.05 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4041.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4050.59` (Risk Distance: `9.47` pts)
  * +2.5R Take Profit: `4017.44`
  * Mathematical Lot Sizing: **`1.05 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4043.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
