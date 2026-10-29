# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-29 23:07:13 IST` (`2026-10-29 17:37:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4017.85` | **Live Ask Quote**: `4017.94` | **Mid Price**: `4017.89`
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
  * Session VWAP: `4031.46` | VWAP Z-Score: `-1.10` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.92` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.91` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.57` | Lower -3.00σ Band: `3998.34`
  * Upper +2.51σ Band: `4059.17` | Lower -2.51σ Band: `4003.75`
  * Upper +2.01σ Band: `4053.65` | Lower -2.01σ Band: `4009.27`
  * Upper +2.00σ Band: `4053.54` | Lower -2.00σ Band: `4009.38`
  * Upper +1.28σ Band: `4045.59` | Lower -1.28σ Band: `4017.33`
  * Upper +1.00σ Band: `4042.50` | Lower -1.00σ Band: `4020.42`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4019.89` | EMA-20=`4022.33` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4027.74` (Slope: `+0.0000`) | EMA-100=`4033.37`
  * Institutional Anchors: EMA-144=`4034.22` | EMA-200=`4033.35` (Slope: `-0.0370`) | EMA-233=`4032.27`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4010.16` | Weekly High=`4082.75` | Weekly Low=`3988.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.31` (Distance: `-0.55%`)
  * Point of Control (POC) = `4027.30` (Distance: `-0.23%`)
  * Value Area Low (VAL) = `4019.42` (Distance: `-0.04%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.72` | Weekly POC=`4016.16` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4001.82` - `4033.97`
  * Optimal Trade Entry (OTE 0.705): `4025.93`
  * Structural Invalidation Anchor (0.786): `4050.04`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4027.05` | `4029.00` | `4024.77` | `4024.78` | `71` | 284,323.65 USD | 105,615.15 USD | `+37.15%` | 1,264,721.77 USD | `+0.61` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4024.78` | `4027.73` | `4024.78` | `4027.10` | `32` | 127,800.72 USD | 5,321.69 USD | `+4.16%` | 1,270,043.46 USD | `-0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `4027.00` | `4027.00` | `4025.90` | `4026.42` | `17` | 66,926.34 USD | 35,817.90 USD | `+53.52%` | 1,305,861.35 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4021.36` | `4023.30` | `4019.39` | `4023.30` | `201` | 809,848.30 USD | 483,447.28 USD | `+59.70%` | 1,102,826.72 USD | `+2.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4023.30` | `4029.00` | `4022.15` | `4024.78` | `144` | 579,650.94 USD | 173,870.54 USD | `+30.00%` | 1,276,697.27 USD | `+0.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4024.78` | `4027.73` | `4024.78` | `4026.42` | `48` | 194,735.11 USD | 41,147.64 USD | `+21.13%` | 1,317,844.91 USD | `-0.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4029.13` | `4030.46` | `4023.08` | `4026.82` | `526` | 2,116,236.19 USD | -146,951.88 USD | `-6.94%` | -157,920.93 USD | `-0.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4026.82` | `4026.82` | `4016.00` | `4023.30` | `951` | 3,823,725.36 USD | 850,414.22 USD | `+22.24%` | 692,493.29 USD | `+1.66` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4023.30` | `4029.00` | `4022.15` | `4026.42` | `192` | 774,386.05 USD | 215,018.18 USD | `+27.77%` | 907,511.47 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4016.00` | `4026.42` | `1,143` | 4,598,111.40 USD | 1,065,432.40 USD | `+23.17%` | 1,442,482.67 USD | `+1.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4016.00` | `4026.42` | `1,143` | 4,598,111.40 USD | 1,065,432.40 USD | `+23.17%` | 1,442,482.67 USD | `+1.46` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4017.80` | `3.9325` | 15,800.00 USD | 2,202,314.63 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `4017.90` | `10.4158` | 41,849.64 USD | 2,186,514.64 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4018.00` | `2.7428` | 11,020.57 USD | 2,144,664.99 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4018.10` | `48.8446` | 196,262.49 USD | 2,133,644.42 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4018.20` | `32.4933` | 130,564.58 USD | 1,937,381.93 USD | `8 orders` | `-0.05%` | `-` |
| `BID` | `4018.30` | `50.5923` | 203,295.04 USD | 1,806,817.36 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4018.40` | `5.6775` | 22,814.47 USD | 1,603,522.32 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4018.50` | `17.8029` | 71,540.95 USD | 1,580,707.85 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4018.60` | `14.5439` | 58,446.12 USD | 1,509,166.90 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4018.70` | `25.9673` | 104,354.79 USD | 1,450,720.78 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4018.80` | `11.0441` | 44,384.03 USD | 1,346,365.99 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4018.90` | `25.7740` | 103,583.13 USD | 1,301,981.96 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4019.00` | `14.7549` | 59,299.94 USD | 1,198,398.84 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4019.10` | `0.2488` | 999.95 USD | 1,139,098.89 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4019.20` | `2.8889` | 11,611.07 USD | 1,138,098.94 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4019.30` | `19.4088` | 78,009.79 USD | 1,126,487.87 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4019.40` | `7.4625` | 29,994.77 USD | 1,048,478.08 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4019.50` | `1.1007` | 4,424.26 USD | 1,018,483.31 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4019.70` | `0.0766` | 307.91 USD | 1,014,059.05 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4020.00` | `252.1769` | 1,013,751.14 USD | 1,013,751.14 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4020.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,020.05` | `0.00%` | `-` |
| `ASK` | `4020.10` | `49.4972` | 198,983.69 USD | 198,983.69 USD | `17 orders` | `+0.00%` | `-` |
| `ASK` | `4020.20` | `65.4331` | 263,054.15 USD | 462,037.84 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `4020.30` | `33.5711` | 134,965.89 USD | 597,003.74 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4020.40` | `7.6127` | 30,606.10 USD | 627,609.83 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4020.50` | `12.5627` | 50,508.34 USD | 678,118.17 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4020.60` | `10.4682` | 42,088.44 USD | 720,206.62 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4020.70` | `29.5061` | 118,635.18 USD | 838,841.79 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `4020.80` | `3.7926` | 15,249.29 USD | 854,091.08 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4020.90` | `20.2789` | 81,539.43 USD | 935,630.51 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4021.00` | `6.2841` | 25,268.37 USD | 960,898.87 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4021.10` | `79.1858` | 318,414.02 USD | 1,279,312.89 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `4021.20` | `8.8188` | 35,462.16 USD | 1,314,775.05 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4021.30` | `12.2572` | 49,289.88 USD | 1,364,064.93 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4021.40` | `21.0422` | 84,619.10 USD | 1,448,684.03 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `4021.50` | `3.5031` | 14,087.72 USD | 1,462,771.75 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4021.60` | `1.3568` | 5,456.51 USD | 1,468,228.26 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4021.70` | `14.1668` | 56,974.62 USD | 1,525,202.88 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4021.80` | `157.3709` | 632,914.29 USD | 2,158,117.16 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4021.90` | `15.3471` | 61,724.50 USD | 2,219,841.66 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `4022.00` | `24.9770` | 100,457.49 USD | 2,320,299.16 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `55` | `0x5b5d...c060` | `SHORT` | 25,632,306.63 USD | `6,373.66` | `4191.43` | `4021.30` | `28412.38` | 1,082,494.54 USD | `+4.22%` | `4X Cross` |
| `57` | `0x4692...164f` | `SHORT` | 25,258,097.75 USD | `6,281.08` | `4135.01` | `4021.30` | `13246.64` | 714,280.41 USD | `+2.83%` | `5X Cross` |
| `77` | `0xb83d...6e36` | `SHORT` | 22,989,439.26 USD | `5,717.06` | `4234.49` | `4021.30` | `26720.29` | 1,219,435.97 USD | `+5.30%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,418,000.43 USD | `4,828.91` | `4157.43` | `4021.30` | `2046.41` | -657,881.89 USD | `-3.39%` | `25X Cross` |
| `148` | `0x645b...87b8` | `LONG` | 14,143,242.25 USD | `3,517.08` | `4129.71` | `4021.30` | `48.77` | -381,311.49 USD | `-2.70%` | `3X Cross` |
| `161` | `0x7a6d...f79c` | `SHORT` | 13,142,465.74 USD | `3,268.21` | `4228.94` | `4021.30` | `4405.14` | 678,613.39 USD | `+5.16%` | `25X Cross` |
| `184` | `0xa742...e390` | `SHORT` | 11,661,480.40 USD | `2,900.00` | `4364.92` | `4021.30` | `4235.56` | 996,795.93 USD | `+8.55%` | `20X Cross` |
| `277` | `0x3678...b209` | `LONG` | 8,846,860.00 USD | `2,200.00` | `4176.09` | `4021.30` | `2427.78` | -340,559.30 USD | `-3.85%` | `25X Cross` |
| `278` | `0x41e5...0825` | `SHORT` | 8,846,640.00 USD | `2,200.00` | `4112.20` | `4021.30` | `4331.05` | 200,214.59 USD | `+2.26%` | `20X Cross` |
| `313` | `0xfc66...ca06` | `SHORT` | 7,989,879.15 USD | `1,986.89` | `4032.86` | `4021.30` | `24756.95` | 22,987.02 USD | `+0.29%` | `3X Cross` |
| `314` | `0xacb6...efbd` | `SHORT` | 7,943,354.22 USD | `1,975.37` | `4048.55` | `4021.30` | `6478.13` | 54,037.49 USD | `+0.68%` | `6X Cross` |
| `385` | `0xc26c...b8f4` | `LONG` | 6,353,460.17 USD | `1,579.95` | `4075.62` | `4021.30` | `0.000000` | -85,836.80 USD | `-1.35%` | `1X Cross` |
| `427` | `0x12d2...f97f` | `LONG` | 5,637,492.39 USD | `1,401.94` | `4278.91` | `4021.30` | `2403.68` | -361,298.19 USD | `-6.41%` | `20X Cross` |
| `592` | `0x63da...8add` | `LONG` | 4,021,300.00 USD | `1,000.00` | `4021.46` | `4021.30` | `3564.00` | -160.96 USD | `-0.00%` | `25X Cross` |
| `611` | `0x9aa5...58af` | `LONG` | 3,907,166.81 USD | `971.64` | `4279.98` | `4021.30` | `0.000000` | -251,442.27 USD | `-6.44%` | `20X Cross` |
| `635` | `0xf3dc...1672` | `LONG` | 3,742,799.64 USD | `930.74` | `4024.62` | `4021.30` | `3337.48` | -3,092.92 USD | `-0.08%` | `20X Cross` |
| `688` | `0x354b...6425` | `LONG` | 3,430,658.29 USD | `853.12` | `4037.02` | `4021.30` | `0.000000` | -13,413.25 USD | `-0.39%` | `10X Cross` |
| `703` | `0x4a20...3c26` | `LONG` | 3,367,435.41 USD | `837.40` | `4599.73` | `4021.30` | `0.000000` | -484,384.97 USD | `-14.38%` | `20X Cross` |
| `857` | `0x0fac...7a0a` | `LONG` | 2,760,562.13 USD | `686.49` | `4290.34` | `4021.30` | `1294.15` | -184,696.57 USD | `-6.69%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,649,831.21 USD | `658.95` | `4175.35` | `4021.30` | `31147.78` | 101,515.84 USD | `+3.83%` | `4X Cross` |
| `934` | `0x625e...a354` | `SHORT` | 2,493,144.00 USD | `620.00` | `4122.81` | `4021.30` | `4342.14` | 63,003.03 USD | `+2.53%` | `20X Cross` |
| `960` | `0xeae3...e8ad` | `SHORT` | 2,412,780.00 USD | `600.00` | `4104.77` | `4021.30` | `4325.17` | 50,085.11 USD | `+2.08%` | `20X Cross` |
| `965` | `0xf285...fa82` | `LONG` | 2,405,103.45 USD | `598.11` | `4146.45` | `4021.30` | `3891.13` | -74,916.11 USD | `-3.11%` | `25X Cross` |
| `983` | `0x12f7...8750` | `LONG` | 2,354,916.31 USD | `585.61` | `4082.77` | `4021.30` | `2105.54` | -36,000.67 USD | `-1.53%` | `10X Cross` |
| `1138` | `0x413c...886c` | `LONG` | 2,010,650.00 USD | `500.00` | `4010.43` | `4021.30` | `0.000000` | 5,433.77 USD | `+0.27%` | `2X Cross` |
| `1143` | `0x61ce...a62b` | `SHORT` | 2,000,610.82 USD | `497.50` | `4071.66` | `4021.30` | `4685.81` | 25,057.97 USD | `+1.25%` | `20X Cross` |
| `1148` | `0x0593...40f9` | `LONG` | 1,995,276.57 USD | `496.18` | `4024.57` | `4021.30` | `3701.62` | -1,627.26 USD | `-0.08%` | `10X Isolated` |
| `1265` | `0xead5...69f2` | `LONG` | 1,824,755.82 USD | `453.78` | `4220.88` | `4021.30` | `3538.83` | -90,612.24 USD | `-4.97%` | `5X Isolated` |
| `1295` | `0x2edd...8179` | `LONG` | 1,781,621.91 USD | `442.60` | `4174.40` | `4025.50` | `0.000000` | -65,949.24 USD | `-3.70%` | `10X Cross` |
| `1327` | `0x7a6d...f79c` | `SHORT` | 1,724,482.50 USD | `428.38` | `4136.09` | `4025.50` | `5794.49` | 47,332.50 USD | `+2.74%` | `10X Cross` |
| `1395` | `0x46fc...1195` | `LONG` | 1,636,774.06 USD | `407.03` | `4055.53` | `4021.30` | `1885.30` | -13,936.14 USD | `-0.85%` | `20X Cross` |
| `1434` | `0x6d15...d374` | `LONG` | 1,608,480.00 USD | `400.00` | `4068.25` | `4021.30` | `3841.70` | -18,820.00 USD | `-1.17%` | `25X Cross` |
| `1435` | `0xee02...309d` | `SHORT` | 1,608,480.00 USD | `400.00` | `4438.84` | `4021.30` | `4226.78` | 167,058.60 USD | `+10.39%` | `25X Isolated` |
| `1468` | `0x02a7...fe9f` | `SHORT` | 1,568,307.00 USD | `390.00` | `4055.02` | `4021.30` | `4306.60` | 13,152.25 USD | `+0.84%` | `25X Cross` |
| `1501` | `0x7e77...b8d2` | `SHORT` | 1,528,094.00 USD | `380.00` | `4131.92` | `4021.30` | `4293.41` | 42,035.64 USD | `+2.75%` | `20X Cross` |
| `1506` | `0x51f6...2b39` | `LONG` | 1,524,040.59 USD | `378.61` | `4235.75` | `4025.50` | `0.000000` | -79,638.63 USD | `-5.23%` | `10X Cross` |
| `1522` | `0x72c2...9b37` | `LONG` | 1,500,472.90 USD | `373.13` | `4000.98` | `4021.30` | `3777.93` | 7,579.38 USD | `+0.51%` | `13X Isolated` |
| `1567` | `0xaa44...b844` | `LONG` | 1,447,668.00 USD | `360.00` | `4043.10` | `4021.30` | `2818.93` | -7,849.63 USD | `-0.54%` | `9X Cross` |
| `1571` | `0x781e...96b7` | `SHORT` | 1,445,291.69 USD | `359.04` | `4365.52` | `4025.50` | `12209.30` | 122,118.07 USD | `+8.45%` | `10X Cross` |
| `1684` | `0xa41f...d50a` | `LONG` | 1,322,822.40 USD | `328.96` | `4468.89` | `4021.30` | `3833.08` | -147,275.46 USD | `-11.13%` | `15X Cross` |
| `1712` | `0x49e9...e1d0` | `SHORT` | 1,301,120.97 USD | `323.56` | `4025.23` | `4021.30` | `29770.58` | 1,271.73 USD | `+0.10%` | `4X Cross` |
| `1731` | `0xada6...6f88` | `LONG` | 1,283,902.97 USD | `319.28` | `4166.46` | `4021.30` | `1842.78` | -46,347.54 USD | `-3.61%` | `5X Cross` |
| `1737` | `0xbf5a...88ba` | `SHORT` | 1,277,353.88 USD | `317.65` | `4091.80` | `4021.30` | `10536.03` | 22,429.15 USD | `+1.76%` | `20X Cross` |
| `1756` | `0xff31...ff6c` | `SHORT` | 1,246,603.00 USD | `310.00` | `4372.43` | `4021.30` | `4789.07` | 108,852.38 USD | `+8.73%` | `10X Isolated` |
| `1929` | `0x50e2...d770` | `LONG` | 1,087,228.43 USD | `270.37` | `4243.58` | `4021.30` | `2561.99` | -60,098.03 USD | `-5.53%` | `20X Cross` |
| `1955` | `0x4c92...4f17` | `SHORT` | 1,072,563.15 USD | `266.72` | `4260.98` | `4021.30` | `6536.91` | 63,929.09 USD | `+5.96%` | `20X Cross` |
| `2018` | `0xd346...c4f3` | `LONG` | 1,026,104.88 USD | `255.17` | `4188.66` | `4021.30` | `3310.31` | -42,731.62 USD | `-4.16%` | `5X Isolated` |
| `2055` | `0x1581...463b` | `LONG` | 1,005,325.00 USD | `250.00` | `4003.77` | `4021.30` | `3504.53` | 4,381.41 USD | `+0.44%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4111.52` (Vol: 316,800.00 USD, Dist: `+2.17%`) | Long MP=`3951.52` (Vol: 223,500.00 USD, Dist: `--1.81%`)
  * 48H Horizon: Short MP=`4111.52` (Vol: 316,800.00 USD, Dist: `+2.17%`) | Long MP=`3957.44` (Vol: 226,700.00 USD, Dist: `--1.66%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.11%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--1.11%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.32%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3616.10` | 16,280,000.00 USD | 16,280,000.00 USD | 94,440.00 USD | 0.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3617.20` | 4,120,000.00 USD | 4,120,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3620.30` | 16,180,000.00 USD | 16,180,000.00 USD | 52,580.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3621.40` | 4,110,000.00 USD | 4,110,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.50` | 16,110,000.00 USD | 16,110,000.00 USD | 95,620.00 USD | 0.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3625.60` | 4,080,000.00 USD | 4,080,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.70` | 15,990,000.00 USD | 15,990,000.00 USD | 223,360.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.80` | 4,030,000.00 USD | 4,030,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.90` | 15,760,000.00 USD | 15,760,000.00 USD | 90,370.00 USD | 0.00 USD | 16,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.00` | 3,990,000.00 USD | 3,990,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.10` | 15,650,000.00 USD | 15,650,000.00 USD | 93,360.00 USD | 0.00 USD | 15,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.20` | 3,950,000.00 USD | 3,950,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,540,000.00 USD | 15,540,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3642.40` | 3,880,000.00 USD | 3,880,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.50` | 15,480,000.00 USD | 15,480,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3646.60` | 3,860,000.00 USD | 3,860,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.70` | 15,450,000.00 USD | 15,450,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.80` | 3,840,000.00 USD | 3,840,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.90` | 15,430,000.00 USD | 15,430,000.00 USD | 58,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.00` | 3,800,000.00 USD | 3,800,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.10` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3659.20` | 3,790,000.00 USD | 3,790,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.30` | 15,360,000.00 USD | 15,360,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3663.40` | 3,770,000.00 USD | 3,770,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.50` | 15,340,000.00 USD | 15,340,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.80` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.30` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.50` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.70` | 15,330,000.00 USD | 15,330,000.00 USD | 388,830.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.90` | 14,920,000.00 USD | 14,920,000.00 USD | 446,290.00 USD | 0.00 USD | 60,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.10` | 14,410,000.00 USD | 14,410,000.00 USD | 482,900.00 USD | 0.00 USD | 75,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.30` | 13,860,000.00 USD | 13,860,000.00 USD | 256,520.00 USD | 0.00 USD | 54,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.50` | 13,550,000.00 USD | 13,550,000.00 USD | 221,780.00 USD | 0.00 USD | 23,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.70` | 13,300,000.00 USD | 13,300,000.00 USD | 159,510.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.80` | 3,760,000.00 USD | 3,760,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.90` | 13,120,000.00 USD | 13,120,000.00 USD | 260,240.00 USD | 0.00 USD | 43,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.00` | 3,700,000.00 USD | 3,700,000.00 USD | 143,090.00 USD | 0.00 USD | 14,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.10` | 12,820,000.00 USD | 12,820,000.00 USD | 599,530.00 USD | 0.00 USD | 46,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.20` | 3,540,000.00 USD | 3,540,000.00 USD | 127,010.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.30` | 12,170,000.00 USD | 12,170,000.00 USD | 412,260.00 USD | 0.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.40` | 3,390,000.00 USD | 3,390,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3876.50` | 11,710,000.00 USD | 11,710,000.00 USD | 442,350.00 USD | 0.00 USD | 68,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.60` | 3,270,000.00 USD | 3,270,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.70` | 11,200,000.00 USD | 11,200,000.00 USD | 277,230.00 USD | 0.00 USD | 37,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.80` | 3,080,000.00 USD | 3,080,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.90` | 10,880,000.00 USD | 10,880,000.00 USD | 101,210.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3886.00` | 2,920,000.00 USD | 2,920,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3889.10` | 10,750,000.00 USD | 10,750,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3890.20` | 2,840,000.00 USD | 2,840,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3893.30` | 10,640,000.00 USD | 10,640,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3894.40` | 2,770,000.00 USD | 2,770,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.50` | 10,520,000.00 USD | 10,520,000.00 USD | 176,440.00 USD | 0.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3898.60` | 2,670,000.00 USD | 2,670,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.70` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.80` | 2,610,000.00 USD | 2,610,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.90` | 10,330,000.00 USD | 10,330,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.00` | 2,550,000.00 USD | 2,550,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.10` | 10,240,000.00 USD | 10,240,000.00 USD | 23,110.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3915.40` | 2,520,000.00 USD | 2,520,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.50` | 10,210,000.00 USD | 10,210,000.00 USD | 770,170.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.70` | 9,410,000.00 USD | 9,410,000.00 USD | 857,100.00 USD | 0.00 USD | 116,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.90` | 8,430,000.00 USD | 8,430,000.00 USD | 992,370.00 USD | 0.00 USD | 140,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.10` | 7,300,000.00 USD | 7,300,000.00 USD | 455,760.00 USD | 0.00 USD | 122,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.30` | 6,720,000.00 USD | 6,720,000.00 USD | 368,490.00 USD | 0.00 USD | 38,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3939.50` | 6,310,000.00 USD | 6,310,000.00 USD | 456,560.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3940.60` | 2,510,000.00 USD | 2,510,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.70` | 5,830,000.00 USD | 5,830,000.00 USD | 435,580.00 USD | 0.00 USD | 92,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.80` | 2,400,000.00 USD | 2,400,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.90` | 5,310,000.00 USD | 5,310,000.00 USD | 1,030,000.00 USD | 0.00 USD | 99,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.00` | 2,090,000.00 USD | 2,090,000.00 USD | 202,600.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3952.10` | 4,180,000.00 USD | 4,180,000.00 USD | 855,100.00 USD | 0.00 USD | 91,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3953.20` | 1,840,000.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3956.30` | 3,230,000.00 USD | 3,230,000.00 USD | 1,010,000.00 USD | 0.00 USD | 120,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3957.40` | 1,550,000.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3960.50` | 2,100,000.00 USD | 2,100,000.00 USD | 521,420.00 USD | 0.00 USD | 71,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3961.60` | 1,310,000.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.70` | 1,510,000.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.80` | 863,010.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.90` | 1,090,000.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3970.00` | 714,020.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3973.10` | 874,480.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3974.20` | 591,750.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3977.30` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3978.40` | 386,370.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.50` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3982.60` | 253,490.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.70` | 219,990.00 USD | 219,990.00 USD | 59,830.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.80` | 119,030.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.90` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3991.00` | 51,990.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3994.10` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3995.20` | 20,280.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3999.40` | 15,300.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.90` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4078.10` | 733,530.00 USD | 733,530.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.30` | 1,710,000.00 USD | 1,710,000.00 USD | 874,830.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.50` | 2,630,000.00 USD | 2,630,000.00 USD | 784,820.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.70` | 3,440,000.00 USD | 3,440,000.00 USD | 674,970.00 USD | 0.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 3,800,000.00 USD | 3,800,000.00 USD | 320,740.00 USD | 0.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.10` | 4,250,000.00 USD | 4,250,000.00 USD | 422,750.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.30` | 4,710,000.00 USD | 4,710,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.50` | 5,520,000.00 USD | 5,520,000.00 USD | 676,110.00 USD | 0.00 USD | 135,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4108.60` | 563,360.00 USD | 563,360.00 USD | 295,810.00 USD | 0.00 USD | 45,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.70` | 6,650,000.00 USD | 6,650,000.00 USD | 1,060,000.00 USD | 0.00 USD | 69,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.80` | 827,220.00 USD | 827,220.00 USD | 220,390.00 USD | 0.00 USD | 43,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.90` | 7,460,000.00 USD | 7,460,000.00 USD | 728,730.00 USD | 0.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.00` | 1,060,000.00 USD | 1,060,000.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.10` | 8,600,000.00 USD | 8,600,000.00 USD | 1,000,000.00 USD | 0.00 USD | 140,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4121.20` | 1,450,000.00 USD | 1,450,000.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4124.30` | 8,920,000.00 USD | 8,920,000.00 USD | 246,290.00 USD | 0.00 USD | 66,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4125.40` | 1,720,000.00 USD | 1,720,000.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4128.50` | 9,210,000.00 USD | 9,210,000.00 USD | 249,290.00 USD | 0.00 USD | 49,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4129.60` | 1,850,000.00 USD | 1,850,000.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.70` | 9,430,000.00 USD | 9,430,000.00 USD | 170,870.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.80` | 1,990,000.00 USD | 1,990,000.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.90` | 9,680,000.00 USD | 9,680,000.00 USD | 225,430.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.00` | 2,190,000.00 USD | 2,190,000.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4141.10` | 9,980,000.00 USD | 9,980,000.00 USD | 293,010.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4142.20` | 2,300,000.00 USD | 2,300,000.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4145.30` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4146.40` | 2,430,000.00 USD | 2,430,000.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4149.50` | 10,110,000.00 USD | 10,110,000.00 USD | 73,610.00 USD | 0.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4150.60` | 2,490,000.00 USD | 2,490,000.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.70` | 10,190,000.00 USD | 10,190,000.00 USD | 73,770.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.90` | 10,590,000.00 USD | 10,590,000.00 USD | 381,150.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4159.00` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4162.10` | 11,050,000.00 USD | 11,050,000.00 USD | 424,360.00 USD | 0.00 USD | 42,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4163.20` | 2,510,000.00 USD | 2,510,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4166.30` | 11,460,000.00 USD | 11,460,000.00 USD | 338,350.00 USD | 0.00 USD | 68,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.50` | 11,890,000.00 USD | 11,890,000.00 USD | 352,860.00 USD | 0.00 USD | 73,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.70` | 12,120,000.00 USD | 12,120,000.00 USD | 212,100.00 USD | 0.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.90` | 12,320,000.00 USD | 12,320,000.00 USD | 190,420.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.00` | 2,530,000.00 USD | 2,530,000.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,500,000.00 USD | 12,500,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,610,000.00 USD | 2,610,000.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.30` | 12,880,000.00 USD | 12,880,000.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.40` | 2,740,000.00 USD | 2,740,000.00 USD | 117,370.00 USD | 0.00 USD | 18,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.50` | 13,520,000.00 USD | 13,520,000.00 USD | 598,770.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.60` | 2,910,000.00 USD | 2,910,000.00 USD | 151,790.00 USD | 0.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.70` | 13,870,000.00 USD | 13,870,000.00 USD | 304,490.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.80` | 3,010,000.00 USD | 3,010,000.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.90` | 14,420,000.00 USD | 14,420,000.00 USD | 494,670.00 USD | 0.00 USD | 62,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.00` | 3,190,000.00 USD | 3,190,000.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.10` | 14,670,000.00 USD | 14,670,000.00 USD | 208,930.00 USD | 0.00 USD | 37,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.20` | 3,350,000.00 USD | 3,350,000.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.30` | 14,800,000.00 USD | 14,800,000.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.40` | 3,430,000.00 USD | 3,430,000.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.50` | 14,890,000.00 USD | 14,890,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.60` | 3,470,000.00 USD | 3,470,000.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.70` | 15,010,000.00 USD | 15,010,000.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.80` | 3,590,000.00 USD | 3,590,000.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.90` | 15,140,000.00 USD | 15,140,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4222.00` | 3,640,000.00 USD | 3,640,000.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.10` | 15,220,000.00 USD | 15,220,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4226.20` | 3,700,000.00 USD | 3,700,000.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.30` | 15,260,000.00 USD | 15,260,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4230.40` | 3,740,000.00 USD | 3,740,000.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4233.50` | 15,310,000.00 USD | 15,310,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4234.60` | 3,750,000.00 USD | 3,750,000.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.70` | 15,330,000.00 USD | 15,330,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4243.00` | 3,760,000.00 USD | 3,760,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.10` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.30` | 15,460,000.00 USD | 15,460,000.00 USD | 123,180.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.50` | 15,590,000.00 USD | 15,590,000.00 USD | 120,190.00 USD | 0.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.70` | 15,700,000.00 USD | 15,700,000.00 USD | 87,670.00 USD | 0.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.90` | 15,850,000.00 USD | 15,850,000.00 USD | 134,060.00 USD | 0.00 USD | 22,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.10` | 15,890,000.00 USD | 15,890,000.00 USD | 22,000.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4418.30` | 15,980,000.00 USD | 15,980,000.00 USD | 84,830.00 USD | 0.00 USD | 4,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4422.50` | 16,020,000.00 USD | 16,020,000.00 USD | 31,340.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4423.60` | 3,780,000.00 USD | 3,780,000.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.70` | 16,090,000.00 USD | 16,090,000.00 USD | 63,140.00 USD | 0.00 USD | 13,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.80` | 3,830,000.00 USD | 3,830,000.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.90` | 16,230,000.00 USD | 16,230,000.00 USD | 118,300.00 USD | 0.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.00` | 3,860,000.00 USD | 3,860,000.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4434.30` | 3,880,000.00 USD | 3,880,000.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4435.10` | 16,410,000.00 USD | 16,410,000.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4439.30` | 16,480,000.00 USD | 16,480,000.00 USD | 58,000.00 USD | 0.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4443.50` | 16,610,000.00 USD | 16,610,000.00 USD | 115,690.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4447.70` | 16,640,000.00 USD | 16,640,000.00 USD | 22,690.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |

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
| `7D` | `3616.10` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 94,440.00 USD | 0.00 USD | 4,740.00 USD |
| `1D` | `3617.20` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 7,800.00 USD | 0.00 USD | 959.28 USD |
| `7D` | `3620.30` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 52,580.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3621.40` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 26,910.00 USD | 0.00 USD | 1,780.00 USD |
| `7D` | `3624.50` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 95,620.00 USD | 0.00 USD | 23,890.00 USD |
| `1D` | `3625.60` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 41,810.00 USD | 0.00 USD | 8,170.00 USD |
| `7D` | `3628.70` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 223,360.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3629.80` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 39,460.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `3632.90` | 15,760,000.00 USD | 0.00 USD | 15,760,000.00 USD | 90,370.00 USD | 0.00 USD | 16,790.00 USD |
| `1D` | `3634.00` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 31,240.00 USD | 0.00 USD | 4,240.00 USD |
| `7D` | `3637.10` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 93,360.00 USD | 0.00 USD | 15,010.00 USD |
| `1D` | `3638.20` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 56,670.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `3641.30` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3642.40` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 16,710.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `3645.50` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3646.60` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 14,480.00 USD | 0.00 USD | 5,490.00 USD |
| `7D` | `3649.70` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.80` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 34,870.00 USD | 0.00 USD | 3,160.00 USD |
| `7D` | `3653.90` | 15,430,000.00 USD | 0.00 USD | 15,430,000.00 USD | 58,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.00` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 13,210.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `3658.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 5,330.00 USD |
| `1D` | `3659.20` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 12,070.00 USD | 0.00 USD | 2,120.00 USD |
| `7D` | `3662.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3663.40` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3666.50` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.80` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.30` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3834.50` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.70` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 388,830.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3842.90` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 446,290.00 USD | 0.00 USD | 60,030.00 USD |
| `7D` | `3847.10` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 482,900.00 USD | 0.00 USD | 75,710.00 USD |
| `7D` | `3851.30` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 256,520.00 USD | 0.00 USD | 54,050.00 USD |
| `7D` | `3855.50` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 221,780.00 USD | 0.00 USD | 23,450.00 USD |
| `7D` | `3859.70` | 13,300,000.00 USD | 0.00 USD | 13,300,000.00 USD | 159,510.00 USD | 0.00 USD | 18,270.00 USD |
| `1D` | `3860.80` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 56,720.00 USD | 0.00 USD | 7,550.00 USD |
| `7D` | `3863.90` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 260,240.00 USD | 0.00 USD | 43,190.00 USD |
| `1D` | `3865.00` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 143,090.00 USD | 0.00 USD | 14,270.00 USD |
| `7D` | `3868.10` | 12,820,000.00 USD | 0.00 USD | 12,820,000.00 USD | 599,530.00 USD | 0.00 USD | 46,420.00 USD |
| `1D` | `3869.20` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 127,010.00 USD | 0.00 USD | 21,160.00 USD |
| `7D` | `3872.30` | 12,170,000.00 USD | 0.00 USD | 12,170,000.00 USD | 412,260.00 USD | 0.00 USD | 53,490.00 USD |
| `1D` | `3873.40` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 107,260.00 USD | 0.00 USD | 16,210.00 USD |
| `7D` | `3876.50` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 442,350.00 USD | 0.00 USD | 68,150.00 USD |
| `1D` | `3877.60` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 178,670.00 USD | 0.00 USD | 10,980.00 USD |
| `7D` | `3880.70` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 277,230.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `3881.80` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 125,750.00 USD | 0.00 USD | 30,600.00 USD |
| `7D` | `3884.90` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 101,210.00 USD | 0.00 USD | 32,380.00 USD |
| `1D` | `3886.00` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 73,080.00 USD | 0.00 USD | 13,400.00 USD |
| `7D` | `3889.10` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3890.20` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 54,900.00 USD | 0.00 USD | 14,370.00 USD |
| `7D` | `3893.30` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3894.40` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 93,050.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3897.50` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 176,440.00 USD | 0.00 USD | 5,460.00 USD |
| `1D` | `3898.60` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 45,330.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `3901.70` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 14,320.00 USD |
| `1D` | `3902.80` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 58,130.00 USD | 0.00 USD | 5,290.00 USD |
| `7D` | `3905.90` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 67,120.00 USD | 0.00 USD | 13,970.00 USD |
| `1D` | `3907.00` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 24,810.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3910.10` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 23,110.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `1D` | `3915.40` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3918.50` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 770,170.00 USD | 0.00 USD | 35,850.00 USD |
| `7D` | `3922.70` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 857,100.00 USD | 0.00 USD | 116,530.00 USD |
| `7D` | `3926.90` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 992,370.00 USD | 0.00 USD | 140,450.00 USD |
| `7D` | `3931.10` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 455,760.00 USD | 0.00 USD | 122,590.00 USD |
| `7D` | `3935.30` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 368,490.00 USD | 0.00 USD | 38,330.00 USD |
| `7D` | `3939.50` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 456,560.00 USD | 0.00 USD | 23,520.00 USD |
| `1D` | `3940.60` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 92,830.00 USD | 0.00 USD | 12,060.00 USD |
| `7D` | `3943.70` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 435,580.00 USD | 0.00 USD | 92,010.00 USD |
| `1D` | `3944.80` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 292,410.00 USD | 0.00 USD | 23,070.00 USD |
| `7D` | `3947.90` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 1,030,000.00 USD | 0.00 USD | 99,970.00 USD |
| `1D` | `3949.00` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 202,600.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `3952.10` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 855,100.00 USD | 0.00 USD | 91,100.00 USD |
| `1D` | `3953.20` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 260,960.00 USD | 0.00 USD | 35,280.00 USD |
| `7D` | `3956.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 1,010,000.00 USD | 0.00 USD | 120,760.00 USD |
| `1D` | `3957.40` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 222,500.00 USD | 0.00 USD | 16,230.00 USD |
| `7D` | `3960.50` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 521,420.00 USD | 0.00 USD | 71,810.00 USD |
| `1D` | `3961.60` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 385,340.00 USD | 0.00 USD | 58,450.00 USD |
| `7D` | `3964.70` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 307,000.00 USD | 0.00 USD | 105,930.00 USD |
| `1D` | `3965.80` | 863,010.00 USD | 0.00 USD | 863,010.00 USD | 115,290.00 USD | 0.00 USD | 33,700.00 USD |
| `7D` | `3968.90` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `1D` | `3970.00` | 714,020.00 USD | 0.00 USD | 714,020.00 USD | 92,310.00 USD | 0.00 USD | 29,950.00 USD |
| `7D` | `3973.10` | 874,480.00 USD | 0.00 USD | 874,480.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3974.20` | 591,750.00 USD | 0.00 USD | 591,750.00 USD | 198,780.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3977.30` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3978.40` | 386,370.00 USD | 0.00 USD | 386,370.00 USD | 118,440.00 USD | 0.00 USD | 14,450.00 USD |
| `7D` | `3981.50` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `3982.60` | 253,490.00 USD | 0.00 USD | 253,490.00 USD | 105,260.00 USD | 0.00 USD | 29,200.00 USD |
| `7D` | `3985.70` | 219,990.00 USD | 0.00 USD | 219,990.00 USD | 59,830.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `3986.80` | 119,030.00 USD | 0.00 USD | 119,030.00 USD | 57,180.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3989.90` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3991.00` | 51,990.00 USD | 0.00 USD | 51,990.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3994.10` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3995.20` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `3999.40` | 15,300.00 USD | 0.00 USD | 15,300.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4024.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4024.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.90` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4078.10` | 733,530.00 USD | 733,530.00 USD | 0.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4082.30` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 874,830.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `4086.50` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 784,820.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `4090.70` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 674,970.00 USD | 0.00 USD | 137,740.00 USD |
| `7D` | `4094.90` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 320,740.00 USD | 0.00 USD | 40,420.00 USD |
| `7D` | `4099.10` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 422,750.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4100.20` | 45,190.00 USD | 45,190.00 USD | 0.00 USD | 38,980.00 USD | 0.00 USD | 6,200.00 USD |
| `7D` | `4103.30` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `4104.40` | 222,480.00 USD | 222,480.00 USD | 0.00 USD | 167,150.00 USD | 0.00 USD | 10,140.00 USD |
| `7D` | `4107.50` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 676,110.00 USD | 0.00 USD | 135,680.00 USD |
| `1D` | `4108.60` | 563,360.00 USD | 563,360.00 USD | 0.00 USD | 295,810.00 USD | 0.00 USD | 45,070.00 USD |
| `7D` | `4111.70` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 69,590.00 USD |
| `1D` | `4112.80` | 827,220.00 USD | 827,220.00 USD | 0.00 USD | 220,390.00 USD | 0.00 USD | 43,470.00 USD |
| `7D` | `4115.90` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 728,730.00 USD | 0.00 USD | 77,320.00 USD |
| `1D` | `4117.00` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 208,070.00 USD | 0.00 USD | 21,800.00 USD |
| `7D` | `4120.10` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 1,000,000.00 USD | 0.00 USD | 140,330.00 USD |
| `1D` | `4121.20` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 365,180.00 USD | 0.00 USD | 30,190.00 USD |
| `7D` | `4124.30` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 246,290.00 USD | 0.00 USD | 66,200.00 USD |
| `1D` | `4125.40` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 61,290.00 USD |
| `7D` | `4128.50` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 249,290.00 USD | 0.00 USD | 49,090.00 USD |
| `1D` | `4129.60` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 125,190.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4132.70` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 170,870.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.80` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 109,810.00 USD | 0.00 USD | 28,740.00 USD |
| `7D` | `4136.90` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 225,430.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4138.00` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 186,090.00 USD | 0.00 USD | 17,390.00 USD |
| `7D` | `4141.10` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 293,010.00 USD | 0.00 USD | 10,910.00 USD |
| `1D` | `4142.20` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 90,660.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `4145.30` | 10,010,000.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `1D` | `4146.40` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 116,260.00 USD | 0.00 USD | 10,580.00 USD |
| `7D` | `4149.50` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 28,900.00 USD |
| `1D` | `4150.60` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 49,610.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.70` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `4157.90` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 381,150.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4159.00` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4162.10` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 424,360.00 USD | 0.00 USD | 42,940.00 USD |
| `1D` | `4163.20` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4166.30` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 338,350.00 USD | 0.00 USD | 68,260.00 USD |
| `7D` | `4170.50` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 352,860.00 USD | 0.00 USD | 73,620.00 USD |
| `7D` | `4174.70` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 20,210.00 USD |
| `7D` | `4178.90` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 190,420.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4180.00` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 19,490.00 USD | 0.00 USD | 2,400.00 USD |
| `7D` | `4183.10` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4184.20` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 69,340.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `4187.30` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 327,960.00 USD | 0.00 USD | 55,540.00 USD |
| `1D` | `4188.40` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 117,370.00 USD | 0.00 USD | 18,900.00 USD |
| `7D` | `4191.50` | 13,520,000.00 USD | 13,520,000.00 USD | 0.00 USD | 598,770.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4192.60` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 151,790.00 USD | 0.00 USD | 19,500.00 USD |
| `7D` | `4195.70` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 304,490.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4196.80` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 80,680.00 USD | 0.00 USD | 15,800.00 USD |
| `7D` | `4199.90` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 494,670.00 USD | 0.00 USD | 62,750.00 USD |
| `1D` | `4201.00` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 174,090.00 USD | 0.00 USD | 9,230.00 USD |
| `7D` | `4204.10` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4205.20` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 125,750.00 USD | 0.00 USD | 29,170.00 USD |
| `7D` | `4208.30` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `1D` | `4209.40` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 73,080.00 USD | 0.00 USD | 12,740.00 USD |
| `7D` | `4212.50` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4213.60` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 13,200.00 USD |
| `7D` | `4216.70` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `1D` | `4217.80` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 117,470.00 USD | 0.00 USD | 5,880.00 USD |
| `7D` | `4220.90` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `4222.00` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 41,140.00 USD | 0.00 USD | 4,640.00 USD |
| `7D` | `4225.10` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `4226.20` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 52,630.00 USD | 0.00 USD | 14,600.00 USD |
| `7D` | `4229.30` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `1D` | `4230.40` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 3,940.00 USD |
| `7D` | `4233.50` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `1D` | `4234.60` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 15,850.00 USD | 0.00 USD | 990.64 USD |
| `7D` | `4237.70` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4243.00` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4393.10` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4397.30` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 123,180.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4401.50` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 120,190.00 USD | 0.00 USD | 11,600.00 USD |
| `7D` | `4405.70` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 87,670.00 USD | 0.00 USD | 16,730.00 USD |
| `7D` | `4409.90` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 134,060.00 USD | 0.00 USD | 22,490.00 USD |
| `7D` | `4414.10` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 22,000.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `4418.30` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 84,830.00 USD | 0.00 USD | 4,740.00 USD |
| `7D` | `4422.50` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 31,340.00 USD | 0.00 USD | 5,700.00 USD |
| `1D` | `4423.60` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `4426.70` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 63,140.00 USD | 0.00 USD | 13,840.00 USD |
| `1D` | `4427.80` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 44,800.00 USD | 0.00 USD | 4,360.00 USD |
| `7D` | `4430.90` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 118,300.00 USD | 0.00 USD | 14,520.00 USD |
| `1D` | `4432.00` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 18,660.00 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `4434.30` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 22,010.00 USD | 0.00 USD | 1,940.00 USD |
| `7D` | `4435.10` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 168,390.00 USD | 0.00 USD | 14,030.00 USD |
| `7D` | `4439.30` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 58,000.00 USD | 0.00 USD | 9,370.00 USD |
| `7D` | `4443.50` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 115,690.00 USD | 0.00 USD | 22,430.00 USD |
| `7D` | `4447.70` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 7,320.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.21M` | Total OI Tokens: `68,366.7 PAXG`
  * 1h OI Change: `+0.19%` | 4h OI Change: `-0.12%` | 24h OI Change: `+0.64%`
  * Exchange Breakdown: Binance=`106.85M` | Bybit=`20.01M` | OKX=`-` | Hyperliquid=`25.79M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.98K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `42.84%` | `57.16%` | `0.75` | 1,180,000.00 USD |
| `15M` | `Binance` | `38.96%` | `61.04%` | `0.64` | 407,570.00 USD |
| `15M` | `OKX` | `38.94%` | `61.06%` | `0.64` | 154,530.00 USD |
| `15M` | `Bybit` | `51.53%` | `48.47%` | `1.06` | 93,880.00 USD |
| `15M` | `KuCoin` | `55.09%` | `44.91%` | `1.23` | 8,010.00 USD |
| `15M` | `Gate` | `23.01%` | `76.99%` | `0.30` | 4,700.00 USD |
| `15M` | `Bitget` | `50.77%` | `49.23%` | `1.03` | 12,730.00 USD |
| `15M` | `BingX` | `51.95%` | `48.05%` | `1.08` | 48,510.00 USD |
| `15M` | `MEXC` | `45.96%` | `54.04%` | `0.85` | 168,860.00 USD |
| `15M` | `Bitunix` | `45.28%` | `54.72%` | `0.83` | 8,720.00 USD |
| `15M` | `Hyperliquid` | `25.78%` | `74.22%` | `0.35` | 5,310.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.31%` | `64.69%` | `0.55` | 223,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.11 USD |
| `15M` | `WhiteBIT` | `99.24%` | `0.76%` | `130.58` | 38,400.00 USD |
| `15M` | `HTX` | `10.84%` | `89.16%` | `0.12` | 45.81 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `2.91%` | `97.09%` | `0.03` | 1,710.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 113.08 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `13.3%` | `86.7%` | `0.15` | 1,480.00 USD |
| `15M` | `Whale Positions` | `38.96%` | `61.04%` | `0.64` | 407,570.00 USD |
| `15M` | `Global Accounts` | `42.84%` | `57.16%` | `0.75` | 1,180,000.00 USD |
| `1H` | `PAXG` | `46.41%` | `53.59%` | `0.87` | 4,570,000.00 USD |
| `1H` | `Binance` | `41.27%` | `58.73%` | `0.70` | 1,570,000.00 USD |
| `1H` | `OKX` | `45.74%` | `54.26%` | `0.84` | 686,660.00 USD |
| `1H` | `Bybit` | `44.16%` | `55.84%` | `0.79` | 511,610.00 USD |
| `1H` | `KuCoin` | `25.8%` | `74.2%` | `0.35` | 30,180.00 USD |
| `1H` | `Gate` | `31.81%` | `68.19%` | `0.47` | 23,170.00 USD |
| `1H` | `Bitget` | `34.78%` | `65.22%` | `0.53` | 110,610.00 USD |
| `1H` | `BingX` | `59.53%` | `40.47%` | `1.47` | 335,200.00 USD |
| `1H` | `MEXC` | `50.03%` | `49.97%` | `1.00` | 298,730.00 USD |
| `1H` | `Bitunix` | `45.38%` | `54.62%` | `0.83` | 38,960.00 USD |
| `1H` | `Hyperliquid` | `23.95%` | `76.05%` | `0.31` | 14,580.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.91%` | `55.09%` | `0.82` | 790,310.00 USD |
| `1H` | `Crypto.com` | `0%` | `100%` | `0.00` | 0.57 USD |
| `1H` | `WhiteBIT` | `98.28%` | `1.72%` | `57.14` | 158,570.00 USD |
| `1H` | `HTX` | `2.55%` | `97.45%` | `0.03` | 311.34 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `13.78%` | `86.22%` | `0.16` | 4,210.00 USD |
| `1H` | `Aster` | `34.13%` | `65.87%` | `0.52` | 514.48 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `14.16%` | `85.84%` | `0.16` | 2,590.00 USD |
| `1H` | `Whale Positions` | `41.27%` | `58.73%` | `0.70` | 1,570,000.00 USD |
| `1H` | `Global Accounts` | `46.41%` | `53.59%` | `0.87` | 4,570,000.00 USD |
| `4H` | `PAXG` | `51.06%` | `48.94%` | `1.04` | 23,940,000.00 USD |
| `4H` | `Binance` | `50.25%` | `49.75%` | `1.01` | 8,380,000.00 USD |
| `4H` | `OKX` | `52.22%` | `47.78%` | `1.09` | 3,020,000.00 USD |
| `4H` | `Bybit` | `52.38%` | `47.62%` | `1.10` | 2,350,000.00 USD |
| `4H` | `KuCoin` | `30.97%` | `69.03%` | `0.45` | 122,210.00 USD |
| `4H` | `Gate` | `49.56%` | `50.44%` | `0.98` | 287,840.00 USD |
| `4H` | `Bitget` | `53.94%` | `46.06%` | `1.17` | 753,950.00 USD |
| `4H` | `BingX` | `39.12%` | `60.88%` | `0.64` | 2,010,000.00 USD |
| `4H` | `MEXC` | `49.92%` | `50.08%` | `1.00` | 1,690,000.00 USD |
| `4H` | `Bitunix` | `49.49%` | `50.51%` | `0.98` | 260,020.00 USD |
| `4H` | `Hyperliquid` | `81.45%` | `18.55%` | `4.39` | 324,290.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 4,070,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `100%` | `0.00` | 3.04 USD |
| `4H` | `WhiteBIT` | `95.99%` | `4.01%` | `23.94` | 615,930.00 USD |
| `4H` | `HTX` | `53.94%` | `46.06%` | `1.17` | 3,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `31.33%` | `68.67%` | `0.46` | 18,860.00 USD |
| `4H` | `Aster` | `2.5%` | `97.5%` | `0.03` | 9,220.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.64%` | `51.36%` | `0.95` | 25,310.00 USD |
| `4H` | `Whale Positions` | `50.25%` | `49.75%` | `1.01` | 8,380,000.00 USD |
| `4H` | `Global Accounts` | `51.06%` | `48.94%` | `1.04` | 23,940,000.00 USD |


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
| `5m` | -12,400.00 USD | 3,830.00 USD | **`DISTRIBUTION`** |
| `15m` | -41,780.00 USD | 152,060.00 USD | **`ACCUMULATION`** |
| `30m` | -51,460.00 USD | 299,210.00 USD | **`ACCUMULATION`** |
| `1h` | 483,860.00 USD | 658,260.00 USD | **`ACCUMULATION`** |
| `2h` | 834,870.00 USD | 998,350.00 USD | **`ACCUMULATION`** |
| `4h` | 624,600.00 USD | 581,310.00 USD | **`ACCUMULATION`** |
| `6h` | 351,960.00 USD | 1,360,000.00 USD | **`ACCUMULATION`** |
| `8h` | 300,760.00 USD | 973,820.00 USD | **`ACCUMULATION`** |
| `12h` | 263,750.00 USD | 318,860.00 USD | **`ACCUMULATION`** |
| `24h` | 104,200.00 USD | 1,270,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,040,000.00 USD | -8,690,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,750,000.00 USD | -72,370,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.40K` | 15m=`-41.78K` | 1h=`+483.86K` | 24h=`+104.20K`
* Futures Capital Netflows: 5m=`+3.83K` | 15m=`+152.06K` | 1h=`+658.26K` | 24h=`+1.27M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4019.42` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.78` (Risk Distance: `9.64` pts)
  * +2.5R Take Profit: `4043.53`
  * Mathematical Lot Sizing: **`1.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.31` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4049.95` (Risk Distance: `9.64` pts)
  * +2.5R Take Profit: `4016.20`
  * Mathematical Lot Sizing: **`1.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4050.04`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
