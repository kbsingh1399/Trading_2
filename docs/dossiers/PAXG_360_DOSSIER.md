# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 00:38:22 IST` (`2026-10-29 19:08:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4011.15` | **Live Ask Quote**: `4011.23` | **Mid Price**: `4011.19`
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
  * Session VWAP: `4011.19` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.03` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4039.27` | Lower -3.00σ Band: `3983.11`
  * Upper +2.51σ Band: `4033.25` | Lower -2.51σ Band: `3989.13`
  * Upper +2.01σ Band: `4028.04` | Lower -2.01σ Band: `3994.34`
  * Upper +2.00σ Band: `4027.23` | Lower -2.00σ Band: `3995.15`
  * Upper +1.28σ Band: `4022.42` | Lower -1.28σ Band: `3999.96`
  * Upper +1.00σ Band: `4019.21` | Lower -1.00σ Band: `4003.17`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4011.19` | EMA-20=`4011.19` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4011.19` (Slope: `+0.0000`) | EMA-100=`4011.19`
  * Institutional Anchors: EMA-144=`4011.19` | EMA-200=`4011.19` (Slope: `+0.0000`) | EMA-233=`4011.19`
- **Range Boundaries**: 24H High=`4051.30` | 24H Low=`3971.08` | Weekly High=`4091.41` | Weekly Low=`3930.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.53` (Distance: `-0.71%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.39%`)
  * Value Area Low (VAL) = `4017.10` (Distance: `-0.13%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `3995.15` - `4027.23`
  * Optimal Trade Entry (OTE 0.705): `4019.21`
  * Structural Invalidation Anchor (0.786): `4043.28`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4016.09` | `4017.00` | `4015.57` | `4016.99` | `44` | 178,469.58 USD | 116,525.87 USD | `+65.29%` | 1,755,302.88 USD | `+0.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4017.00` | `4017.97` | `4017.00` | `4017.56` | `19` | 75,112.02 USD | 5,431.03 USD | `+7.23%` | 1,760,733.91 USD | `-0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4017.56` | `4017.56` | `4015.46` | `4015.85` | `125` | 500,912.79 USD | -470,015.51 USD | `-93.83%` | 1,290,718.41 USD | `-2.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4011.89` | `4014.70` | `4011.01` | `4014.55` | `71` | 283,231.27 USD | 115,122.48 USD | `+40.65%` | 1,343,054.52 USD | `+0.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4014.54` | `4017.97` | `4013.57` | `4017.56` | `132` | 528,554.94 USD | 354,179.10 USD | `+67.01%` | 1,697,233.62 USD | `+1.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4017.56` | `4017.56` | `4015.46` | `4015.85` | `125` | 500,912.79 USD | -470,015.51 USD | `-93.83%` | 1,227,218.11 USD | `-2.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4023.30` | `4029.00` | `4011.95` | `4011.96` | `549` | 2,206,317.77 USD | -210,291.82 USD | `-9.53%` | 1,017,172.68 USD | `-0.59` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4017.97` | `4011.01` | `4017.56` | `511` | 2,050,996.96 USD | 1,105,382.66 USD | `+53.89%` | 2,122,555.33 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4017.56` | `4017.56` | `4015.46` | `4015.85` | `125` | 500,912.79 USD | -470,015.51 USD | `-93.83%` | 1,652,539.83 USD | `-1.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4015.85` | `2,135` | 8,581,952.88 USD | 1,275,489.55 USD | `+14.86%` | 1,652,539.83 USD | `+1.61` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4053.44` | `4065.63` | `4036.00` | `4038.03` | `3,568` | 14,441,971.44 USD | 632,777.98 USD | `+4.38%` | 855,497.47 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | 197,313.54 USD | `-1.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -55,062.99 USD | `-0.49` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 377,050.28 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4015.85` | `2,135` | 8,581,952.88 USD | 1,275,489.55 USD | `+14.86%` | 1,652,539.83 USD | `+1.61` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4011.10` | `22.0529` | 88,456.39 USD | 1,636,287.17 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `4011.20` | `1.8126` | 7,270.70 USD | 1,547,830.78 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4011.30` | `12.4546` | 49,959.14 USD | 1,540,560.08 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4011.40` | `101.4699` | 407,036.36 USD | 1,490,600.94 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `4011.50` | `1.8744` | 7,519.16 USD | 1,083,564.58 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4011.60` | `3.9874` | 15,995.85 USD | 1,076,045.43 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4011.70` | `17.8332` | 71,541.45 USD | 1,060,049.57 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4011.80` | `6.9322` | 27,810.60 USD | 988,508.13 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4011.90` | `60.4721` | 242,608.02 USD | 960,697.53 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4012.00` | `53.5772` | 214,951.73 USD | 718,089.51 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4012.10` | `0.1923` | 771.53 USD | 503,137.78 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4012.20` | `22.9005` | 91,881.39 USD | 502,366.25 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4012.30` | `17.8872` | 71,768.81 USD | 410,484.87 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4012.40` | `28.6034` | 114,768.28 USD | 338,716.06 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4012.50` | `3.7374` | 14,996.32 USD | 223,947.77 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4012.60` | `26.3448` | 105,711.14 USD | 208,951.46 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4012.70` | `2.1572` | 8,656.20 USD | 103,240.31 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4012.90` | `9.9058` | 39,750.98 USD | 94,584.11 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4013.00` | `8.8988` | 35,710.88 USD | 54,833.13 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4013.40` | `4.7646` | 19,122.25 USD | 19,122.25 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4013.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,013.45` | `0.00%` | `-` |
| `ASK` | `4013.50` | `2.4065` | 9,658.49 USD | 9,658.49 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `4013.60` | `17.7949` | 71,421.61 USD | 81,080.10 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `4013.70` | `9.4886` | 38,084.39 USD | 119,164.49 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4013.80` | `9.4469` | 37,917.97 USD | 157,082.46 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4013.90` | `6.9613` | 27,941.96 USD | 185,024.42 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4014.00` | `74.1625` | 297,688.27 USD | 482,712.70 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `4014.10` | `8.8905` | 35,687.36 USD | 518,400.05 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4014.20` | `10.4606` | 41,990.94 USD | 560,390.99 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4014.30` | `10.3154` | 41,409.11 USD | 601,800.10 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4014.40` | `65.9176` | 264,619.61 USD | 866,419.72 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `4014.50` | `23.1747` | 93,034.83 USD | 959,454.55 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4014.60` | `52.9919` | 212,741.28 USD | 1,172,195.83 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4014.70` | `25.4684` | 102,247.99 USD | 1,274,443.82 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `4014.80` | `2.1825` | 8,762.30 USD | 1,283,206.12 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4014.90` | `8.5558` | 34,350.68 USD | 1,317,556.80 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4015.00` | `8.0577` | 32,351.67 USD | 1,349,908.47 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4015.10` | `11.2744` | 45,267.84 USD | 1,395,176.31 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4015.20` | `95.2458` | 382,430.94 USD | 1,777,607.24 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `4015.30` | `5.3885` | 21,636.44 USD | 1,799,243.69 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4015.40` | `10.5368` | 42,309.47 USD | 1,841,553.16 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,586,366.51 USD | `6,373.65` | `4191.43` | `4014.50` | `29378.11` | 1,128,382.69 USD | `+4.41%` | `4X Cross` |
| `55` | `0x4692...164f` | `SHORT` | 25,368,885.99 USD | `6,319.47` | `4133.88` | `4014.50` | `13303.29` | 755,101.76 USD | `+2.98%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,950,563.26 USD | `5,717.06` | `4234.49` | `4014.50` | `27707.32` | 1,258,311.97 USD | `+5.48%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,385,163.86 USD | `4,828.91` | `4157.43` | `4014.50` | `2096.91` | -690,718.46 USD | `-3.56%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,117,265.85 USD | `3,516.66` | `4129.63` | `4014.50` | `305.16` | -405,245.02 USD | `-2.87%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,119,915.07 USD | `3,268.21` | `4228.94` | `4014.50` | `4410.02` | 701,164.06 USD | `+5.34%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,641,760.40 USD | `2,900.00` | `4364.92` | `4014.50` | `4235.62` | 1,016,515.93 USD | `+8.73%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,831,680.00 USD | `2,200.00` | `4176.09` | `4014.50` | `2475.86` | -355,739.30 USD | `-4.03%` | `25X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,831,680.00 USD | `2,200.00` | `4112.20` | `4014.50` | `4331.10` | 215,174.59 USD | `+2.44%` | `20X Cross` |
| `308` | `0xfc66...ca06` | `SHORT` | 7,976,169.61 USD | `1,986.89` | `4032.86` | `4014.50` | `25049.11` | 36,696.56 USD | `+0.46%` | `3X Cross` |
| `310` | `0xacb6...efbd` | `SHORT` | 7,929,921.71 USD | `1,975.37` | `4048.55` | `4014.50` | `6500.78` | 67,470.00 USD | `+0.85%` | `6X Cross` |
| `381` | `0xc26c...b8f4` | `LONG` | 6,342,558.51 USD | `1,579.95` | `4075.62` | `4014.50` | `0.000000` | -96,738.46 USD | `-1.53%` | `1X Cross` |
| `420` | `0x12d2...f97f` | `LONG` | 5,627,959.18 USD | `1,401.94` | `4278.91` | `4014.50` | `2536.80` | -370,831.40 USD | `-6.59%` | `20X Cross` |
| `575` | `0x63da...8add` | `LONG` | 4,014,400.00 USD | `1,000.00` | `4021.46` | `4014.50` | `3564.06` | -7,060.96 USD | `-0.18%` | `25X Cross` |
| `596` | `0x9aa5...58af` | `LONG` | 3,900,559.64 USD | `971.64` | `4279.98` | `4014.50` | `0.000000` | -258,049.44 USD | `-6.62%` | `20X Cross` |
| `626` | `0xf3dc...1672` | `LONG` | 3,736,377.51 USD | `930.74` | `4024.62` | `4014.50` | `3337.54` | -9,515.05 USD | `-0.25%` | `20X Cross` |
| `686` | `0x4a20...3c26` | `LONG` | 3,361,657.36 USD | `837.40` | `4599.73` | `4014.50` | `0.000000` | -490,163.03 USD | `-14.58%` | `20X Cross` |
| `767` | `0x354b...6425` | `LONG` | 3,072,270.50 USD | `765.31` | `4035.10` | `4014.50` | `0.000000` | -15,842.48 USD | `-0.52%` | `10X Cross` |
| `847` | `0x0fac...7a0a` | `LONG` | 2,755,825.38 USD | `686.49` | `4290.34` | `4014.50` | `1295.84` | -189,433.32 USD | `-6.87%` | `25X Cross` |
| `886` | `0xd8c5...99b0` | `SHORT` | 2,578,669.51 USD | `642.35` | `4175.35` | `4014.50` | `32027.18` | 103,391.67 USD | `+4.01%` | `4X Cross` |
| `921` | `0x625e...a354` | `SHORT` | 2,488,928.00 USD | `620.00` | `4122.81` | `4014.50` | `4342.20` | 67,219.03 USD | `+2.70%` | `20X Cross` |
| `949` | `0xeae3...e8ad` | `SHORT` | 2,408,640.00 USD | `600.00` | `4104.77` | `4014.50` | `4325.22` | 54,225.11 USD | `+2.25%` | `20X Cross` |
| `953` | `0xf285...fa82` | `LONG` | 2,401,036.33 USD | `598.11` | `4146.45` | `4014.50` | `3891.19` | -78,983.23 USD | `-3.29%` | `25X Cross` |
| `970` | `0x12f7...8750` | `LONG` | 2,350,875.59 USD | `585.61` | `4082.77` | `4014.50` | `2162.29` | -40,041.39 USD | `-1.70%` | `10X Cross` |
| `1133` | `0x413c...886c` | `LONG` | 2,007,200.00 USD | `500.00` | `4010.43` | `4014.50` | `0.000000` | 1,983.77 USD | `+0.10%` | `2X Cross` |
| `1139` | `0x61ce...a62b` | `SHORT` | 1,997,178.05 USD | `497.50` | `4071.66` | `4014.50` | `4692.82` | 28,490.74 USD | `+1.43%` | `20X Cross` |
| `1143` | `0x0593...40f9` | `LONG` | 1,991,852.95 USD | `496.18` | `4024.57` | `4014.50` | `3701.68` | -5,050.88 USD | `-0.25%` | `10X Isolated` |
| `1260` | `0x2edd...8179` | `LONG` | 1,822,681.95 USD | `453.58` | `4169.95` | `4017.80` | `0.000000` | -68,742.17 USD | `-3.77%` | `10X Cross` |
| `1262` | `0xead5...69f2` | `LONG` | 1,821,670.09 USD | `453.78` | `4220.88` | `4014.50` | `3538.89` | -93,697.97 USD | `-5.14%` | `5X Isolated` |
| `1322` | `0x7a6d...f79c` | `SHORT` | 1,721,355.34 USD | `428.38` | `4136.09` | `4017.80` | `5908.45` | 50,459.67 USD | `+2.93%` | `10X Cross` |
| `1385` | `0x46fc...1195` | `LONG` | 1,633,975.21 USD | `407.03` | `4055.53` | `4014.50` | `1929.86` | -16,744.61 USD | `-1.02%` | `20X Cross` |
| `1423` | `0x6d15...d374` | `LONG` | 1,605,760.00 USD | `400.00` | `4068.25` | `4014.50` | `3841.76` | -21,540.00 USD | `-1.34%` | `25X Cross` |
| `1424` | `0xee02...309d` | `SHORT` | 1,605,760.00 USD | `400.00` | `4438.84` | `4014.50` | `4226.84` | 169,778.60 USD | `+10.57%` | `25X Isolated` |
| `1450` | `0x02a7...fe9f` | `SHORT` | 1,565,616.00 USD | `390.00` | `4055.02` | `4014.50` | `4306.66` | 15,843.25 USD | `+1.01%` | `25X Cross` |
| `1485` | `0x51f6...2b39` | `LONG` | 1,527,996.39 USD | `380.49` | `4234.66` | `4017.80` | `0.000000` | -83,231.68 USD | `-5.45%` | `10X Cross` |
| `1486` | `0x7e77...b8d2` | `SHORT` | 1,525,472.00 USD | `380.00` | `4131.92` | `4014.50` | `4293.46` | 44,657.64 USD | `+2.93%` | `20X Cross` |
| `1507` | `0x72c2...9b37` | `LONG` | 1,497,898.29 USD | `373.13` | `4000.98` | `4014.50` | `3777.99` | 5,004.78 USD | `+0.33%` | `13X Isolated` |
| `1545` | `0xaa44...b844` | `LONG` | 1,445,184.00 USD | `360.00` | `4043.10` | `4014.50` | `2803.21` | -10,333.63 USD | `-0.72%` | `9X Cross` |
| `1547` | `0x781e...96b7` | `SHORT` | 1,444,276.40 USD | `359.55` | `4365.03` | `4017.80` | `12746.57` | 125,171.09 USD | `+8.67%` | `10X Cross` |
| `1654` | `0xa41f...d50a` | `LONG` | 1,320,585.45 USD | `328.96` | `4468.89` | `4014.50` | `3833.14` | -149,512.40 USD | `-11.32%` | `15X Cross` |
| `1683` | `0x49e9...e1d0` | `SHORT` | 1,298,888.43 USD | `323.56` | `4025.23` | `4014.50` | `28182.81` | 3,504.27 USD | `+0.27%` | `4X Cross` |
| `1705` | `0xada6...6f88` | `LONG` | 1,281,699.97 USD | `319.28` | `4166.46` | `4014.50` | `1871.75` | -48,550.54 USD | `-3.79%` | `5X Cross` |
| `1715` | `0xbf5a...88ba` | `SHORT` | 1,275,193.83 USD | `317.65` | `4091.80` | `4014.50` | `10484.80` | 24,589.20 USD | `+1.93%` | `20X Cross` |
| `1735` | `0xff31...ff6c` | `SHORT` | 1,244,464.00 USD | `310.00` | `4372.43` | `4014.50` | `4789.13` | 110,991.38 USD | `+8.92%` | `10X Isolated` |
| `1901` | `0x50e2...d770` | `LONG` | 1,085,362.89 USD | `270.37` | `4243.58` | `4014.50` | `2562.05` | -61,963.57 USD | `-5.71%` | `20X Cross` |
| `1916` | `0x4c92...4f17` | `SHORT` | 1,070,722.78 USD | `266.72` | `4260.98` | `4014.50` | `6525.00` | 65,769.46 USD | `+6.14%` | `20X Cross` |
| `1987` | `0xd346...c4f3` | `LONG` | 1,024,369.70 USD | `255.17` | `4188.66` | `4014.50` | `3310.37` | -44,466.81 USD | `-4.34%` | `5X Isolated` |
| `2027` | `0x1581...463b` | `LONG` | 1,003,600.00 USD | `250.00` | `4003.77` | `4014.50` | `3504.59` | 2,656.41 USD | `+0.26%` | `15X Cross` |
| `2028` | `0xe47f...758c` | `LONG` | 1,003,600.00 USD | `250.00` | `4020.00` | `4014.50` | `3774.29` | -1,400.00 USD | `-0.14%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4106.78` (Vol: 227,900.00 USD, Dist: `+2.22%`) | Long MP=`3948.73` (Vol: 250,500.00 USD, Dist: `--1.71%`)
  * 48H Horizon: Short MP=`4121.69` (Vol: 259,800.00 USD, Dist: `+2.59%`) | Long MP=`3948.73` (Vol: 250,500.00 USD, Dist: `--1.71%`)
  * 3D Horizon: Short MP=`4109.24` (Vol: 329,000.00 USD, Dist: `+2.28%`) | Long MP=`3979.55` (Vol: 340,800.00 USD, Dist: `--0.95%`)
  * 7D Horizon: Short MP=`4117.50` (Vol: 1,100,000.00 USD, Dist: `+2.49%`) | Long MP=`3953.89` (Vol: 1,100,000.00 USD, Dist: `--1.58%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.20` | 16,590,000.00 USD | 16,590,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3612.30` | 3,750,000.00 USD | 3,750,000.00 USD | 2,900.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,510,000.00 USD | 16,510,000.00 USD | 121,270.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.50` | 3,750,000.00 USD | 3,750,000.00 USD | 23,950.00 USD | 0.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,380,000.00 USD | 16,380,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3620.70` | 3,720,000.00 USD | 3,720,000.00 USD | 24,000.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,330,000.00 USD | 16,330,000.00 USD | 105,540.00 USD | 0.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.90` | 3,700,000.00 USD | 3,700,000.00 USD | 43,990.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,200,000.00 USD | 16,200,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3629.10` | 3,650,000.00 USD | 3,650,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 16,010,000.00 USD | 16,010,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3633.30` | 3,610,000.00 USD | 3,610,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,880,000.00 USD | 15,880,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.50` | 3,580,000.00 USD | 3,580,000.00 USD | 52,230.00 USD | 0.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,750,000.00 USD | 15,750,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3641.70` | 3,520,000.00 USD | 3,520,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,680,000.00 USD | 15,680,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.90` | 3,500,000.00 USD | 3,500,000.00 USD | 14,480.00 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,650,000.00 USD | 15,650,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3650.10` | 3,490,000.00 USD | 3,490,000.00 USD | 28,880.00 USD | 0.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,630,000.00 USD | 15,630,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3654.30` | 3,460,000.00 USD | 3,460,000.00 USD | 11,860.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3658.50` | 3,440,000.00 USD | 3,440,000.00 USD | 8,050.00 USD | 0.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,570,000.00 USD | 15,570,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3662.70` | 3,430,000.00 USD | 3,430,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,560,000.00 USD | 15,560,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,540,000.00 USD | 15,540,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3671.10` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,530,000.00 USD | 15,530,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 15,110,000.00 USD | 15,110,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,590,000.00 USD | 14,590,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3851.70` | 3,420,000.00 USD | 3,420,000.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 14,030,000.00 USD | 14,030,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.90` | 3,420,000.00 USD | 3,420,000.00 USD | 62,530.00 USD | 0.00 USD | 6,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,750,000.00 USD | 13,750,000.00 USD | 363,410.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.10` | 3,350,000.00 USD | 3,350,000.00 USD | 50,400.00 USD | 0.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,360,000.00 USD | 13,360,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.30` | 3,290,000.00 USD | 3,290,000.00 USD | 146,200.00 USD | 0.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,170,000.00 USD | 13,170,000.00 USD | 325,660.00 USD | 0.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,140,000.00 USD | 3,140,000.00 USD | 104,800.00 USD | 0.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,790,000.00 USD | 12,790,000.00 USD | 622,200.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.70` | 3,010,000.00 USD | 3,010,000.00 USD | 126,980.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,130,000.00 USD | 12,130,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.90` | 2,860,000.00 USD | 2,860,000.00 USD | 105,540.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,740,000.00 USD | 11,740,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.10` | 2,750,000.00 USD | 2,750,000.00 USD | 120,770.00 USD | 0.00 USD | 25,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,160,000.00 USD | 11,160,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.30` | 2,610,000.00 USD | 2,610,000.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,950,000.00 USD | 10,950,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.50` | 2,560,000.00 USD | 2,560,000.00 USD | 36,210.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,850,000.00 USD | 10,850,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.70` | 2,520,000.00 USD | 2,520,000.00 USD | 104,820.00 USD | 0.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,720,000.00 USD | 10,720,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.90` | 2,410,000.00 USD | 2,410,000.00 USD | 32,580.00 USD | 0.00 USD | 5,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,600,000.00 USD | 10,600,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.10` | 2,370,000.00 USD | 2,370,000.00 USD | 30,100.00 USD | 0.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,470,000.00 USD | 10,470,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.30` | 2,330,000.00 USD | 2,330,000.00 USD | 34,240.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,430,000.00 USD | 10,430,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,370,000.00 USD | 10,370,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3914.70` | 2,290,000.00 USD | 2,290,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,350,000.00 USD | 10,350,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,980,000.00 USD | 9,980,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,200,000.00 USD | 9,200,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,160,000.00 USD | 8,160,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,050,000.00 USD | 7,050,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3935.70` | 2,280,000.00 USD | 2,280,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,550,000.00 USD | 6,550,000.00 USD | 632,990.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.90` | 2,140,000.00 USD | 2,140,000.00 USD | 46,950.00 USD | 0.00 USD | 10,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,890,000.00 USD | 5,890,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3944.10` | 2,080,000.00 USD | 2,080,000.00 USD | 235,600.00 USD | 0.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,430,000.00 USD | 5,430,000.00 USD | 676,110.00 USD | 0.00 USD | 137,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3948.30` | 1,830,000.00 USD | 1,830,000.00 USD | 249,040.00 USD | 0.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.50` | 1,530,000.00 USD | 1,530,000.00 USD | 295,830.00 USD | 0.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3956.70` | 1,200,000.00 USD | 1,200,000.00 USD | 137,160.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.90` | 1,050,000.00 USD | 1,050,000.00 USD | 328,950.00 USD | 0.00 USD | 47,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3965.10` | 668,840.00 USD | 668,840.00 USD | 79,800.00 USD | 0.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3969.30` | 562,680.00 USD | 562,680.00 USD | 31,350.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.50` | 510,890.00 USD | 510,890.00 USD | 182,860.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3977.70` | 321,420.00 USD | 321,420.00 USD | 103,850.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.90` | 210,360.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3986.10` | 138,980.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 7,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3990.30` | 63,870.00 USD | 63,870.00 USD | 41,610.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3998.70` | 20,280.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4095.30` | 68,750.00 USD | 68,750.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,350,000.00 USD | 4,350,000.00 USD | 726,830.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.50` | 197,260.00 USD | 197,260.00 USD | 121,750.00 USD | 0.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4103.70` | 348,960.00 USD | 348,960.00 USD | 138,670.00 USD | 0.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,420,000.00 USD | 5,420,000.00 USD | 678,320.00 USD | 0.00 USD | 104,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.90` | 623,450.00 USD | 623,450.00 USD | 234,740.00 USD | 0.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,530,000.00 USD | 6,530,000.00 USD | 1,040,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4112.10` | 964,780.00 USD | 964,780.00 USD | 303,570.00 USD | 0.00 USD | 37,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,430,000.00 USD | 7,430,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4116.30` | 1,170,000.00 USD | 1,170,000.00 USD | 173,010.00 USD | 0.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,310,000.00 USD | 8,310,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.50` | 1,470,000.00 USD | 1,470,000.00 USD | 283,380.00 USD | 0.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 9,040,000.00 USD | 9,040,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4124.70` | 1,650,000.00 USD | 1,650,000.00 USD | 137,440.00 USD | 0.00 USD | 44,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,290,000.00 USD | 9,290,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4128.90` | 1,760,000.00 USD | 1,760,000.00 USD | 86,920.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,490,000.00 USD | 9,490,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4133.10` | 1,830,000.00 USD | 1,830,000.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,720,000.00 USD | 9,720,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4137.30` | 2,040,000.00 USD | 2,040,000.00 USD | 192,710.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,970,000.00 USD | 9,970,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.50` | 2,110,000.00 USD | 2,110,000.00 USD | 65,150.00 USD | 0.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,140,000.00 USD | 10,140,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.70` | 2,180,000.00 USD | 2,180,000.00 USD | 54,840.00 USD | 0.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,240,000.00 USD | 10,240,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.90` | 2,230,000.00 USD | 2,230,000.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,330,000.00 USD | 10,330,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4154.10` | 2,260,000.00 USD | 2,260,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,700,000.00 USD | 10,700,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4158.30` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,140,000.00 USD | 11,140,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4162.50` | 2,280,000.00 USD | 2,280,000.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,580,000.00 USD | 11,580,000.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 12,020,000.00 USD | 12,020,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,260,000.00 USD | 12,260,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4175.10` | 2,310,000.00 USD | 2,310,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,570,000.00 USD | 12,570,000.00 USD | 295,540.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4179.30` | 2,370,000.00 USD | 2,370,000.00 USD | 46,740.00 USD | 0.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,740,000.00 USD | 12,740,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.50` | 2,440,000.00 USD | 2,440,000.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 13,120,000.00 USD | 13,120,000.00 USD | 327,960.00 USD | 0.00 USD | 53,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4187.70` | 2,580,000.00 USD | 2,580,000.00 USD | 122,010.00 USD | 0.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,780,000.00 USD | 13,780,000.00 USD | 607,230.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.90` | 2,730,000.00 USD | 2,730,000.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 14,120,000.00 USD | 14,120,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.10` | 2,850,000.00 USD | 2,850,000.00 USD | 102,820.00 USD | 0.00 USD | 15,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.30` | 2,960,000.00 USD | 2,960,000.00 USD | 102,180.00 USD | 0.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,630,000.00 USD | 14,630,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.50` | 3,100,000.00 USD | 3,100,000.00 USD | 114,460.00 USD | 0.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,880,000.00 USD | 14,880,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.70` | 3,140,000.00 USD | 3,140,000.00 USD | 31,970.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 15,010,000.00 USD | 15,010,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,190,000.00 USD | 3,190,000.00 USD | 36,210.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 15,120,000.00 USD | 15,120,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.10` | 3,270,000.00 USD | 3,270,000.00 USD | 73,870.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,230,000.00 USD | 15,230,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.30` | 3,320,000.00 USD | 3,320,000.00 USD | 48,960.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,340,000.00 USD | 15,340,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.50` | 3,350,000.00 USD | 3,350,000.00 USD | 24,480.00 USD | 0.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,430,000.00 USD | 15,430,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.70` | 3,390,000.00 USD | 3,390,000.00 USD | 33,610.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,470,000.00 USD | 15,470,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4233.90` | 3,410,000.00 USD | 3,410,000.00 USD | 20,800.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,520,000.00 USD | 15,520,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,530,000.00 USD | 15,530,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4242.30` | 3,420,000.00 USD | 3,420,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,680,000.00 USD | 15,680,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,810,000.00 USD | 15,810,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,960,000.00 USD | 15,960,000.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 16,070,000.00 USD | 16,070,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.50` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 16,140,000.00 USD | 16,140,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.70` | 3,450,000.00 USD | 3,450,000.00 USD | 23,120.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,230,000.00 USD | 16,230,000.00 USD | 90,410.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.90` | 3,470,000.00 USD | 3,470,000.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,270,000.00 USD | 16,270,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4427.10` | 3,500,000.00 USD | 3,500,000.00 USD | 30,000.00 USD | 0.00 USD | 1,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,370,000.00 USD | 16,370,000.00 USD | 79,630.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4431.30` | 3,540,000.00 USD | 3,540,000.00 USD | 29,610.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,540,000.00 USD | 16,540,000.00 USD | 157,240.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.70` | 3,560,000.00 USD | 3,560,000.00 USD | 18,430.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,660,000.00 USD | 16,660,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,780,000.00 USD | 16,780,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,860,000.00 USD | 16,860,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,910,000.00 USD | 16,910,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,590,000.00 USD | 0.00 USD | 16,590,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3612.30` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 2,900.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `3615.50` | 16,510,000.00 USD | 0.00 USD | 16,510,000.00 USD | 121,270.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.50` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 23,950.00 USD | 0.00 USD | 2,510.00 USD |
| `7D` | `3619.80` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3620.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 24,000.00 USD | 0.00 USD | 2,070.00 USD |
| `7D` | `3624.10` | 16,330,000.00 USD | 0.00 USD | 16,330,000.00 USD | 105,540.00 USD | 0.00 USD | 21,190.00 USD |
| `1D` | `3624.90` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 43,990.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `3628.40` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3629.10` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 30,630.00 USD | 0.00 USD | 6,930.00 USD |
| `7D` | `3632.70` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3633.30` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 24,680.00 USD | 0.00 USD | 3,680.00 USD |
| `7D` | `3637.00` | 15,880,000.00 USD | 0.00 USD | 15,880,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.50` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 52,230.00 USD | 0.00 USD | 6,210.00 USD |
| `7D` | `3641.30` | 15,750,000.00 USD | 0.00 USD | 15,750,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3641.70` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 10,510.00 USD | 0.00 USD | 4,910.00 USD |
| `7D` | `3645.60` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3645.90` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 14,480.00 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `3649.90` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3650.10` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 28,880.00 USD | 0.00 USD | 2,300.00 USD |
| `7D` | `3654.20` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3654.30` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 11,860.00 USD | 0.00 USD | 1,900.00 USD |
| `1D` | `3658.50` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 8,050.00 USD | 0.00 USD | 2,200.00 USD |
| `7D` | `3658.50` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3662.70` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 6,340.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3667.10` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3671.10` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 994.87 USD |
| `7D` | `3830.50` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 15,110,000.00 USD | 0.00 USD | 15,110,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 497,700.00 USD | 0.00 USD | 59,220.00 USD |
| `1D` | `3851.70` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 2,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3852.00` | 14,030,000.00 USD | 0.00 USD | 14,030,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3855.90` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 62,530.00 USD | 0.00 USD | 6,910.00 USD |
| `7D` | `3856.30` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 363,410.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3860.10` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 50,400.00 USD | 0.00 USD | 6,530.00 USD |
| `7D` | `3860.60` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 167,120.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3864.30` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 146,200.00 USD | 0.00 USD | 12,280.00 USD |
| `7D` | `3864.90` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 325,660.00 USD | 0.00 USD | 59,280.00 USD |
| `1D` | `3868.50` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 104,800.00 USD | 0.00 USD | 22,340.00 USD |
| `7D` | `3869.20` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 622,200.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3872.70` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 126,980.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3873.50` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3876.90` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 96,140.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3877.80` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3881.10` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 111,630.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `3882.10` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3885.30` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 22,630.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3886.40` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3889.50` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 36,210.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3890.70` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3893.70` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 104,820.00 USD | 0.00 USD | 6,900.00 USD |
| `7D` | `3895.00` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3897.90` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 32,580.00 USD | 0.00 USD | 5,700.00 USD |
| `7D` | `3899.30` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3902.10` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 30,100.00 USD | 0.00 USD | 5,510.00 USD |
| `7D` | `3903.60` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3906.30` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 34,240.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `1D` | `3914.70` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `3916.50` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 914,190.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 7,050,000.00 USD | 0.00 USD | 7,050,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3935.70` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 130,690.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 632,990.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3939.90` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 46,950.00 USD | 0.00 USD | 10,440.00 USD |
| `7D` | `3942.30` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 401,910.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3944.10` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 235,600.00 USD | 0.00 USD | 12,510.00 USD |
| `7D` | `3946.60` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 676,110.00 USD | 0.00 USD | 137,820.00 USD |
| `1D` | `3948.30` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 249,040.00 USD | 0.00 USD | 51,250.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3952.50` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 295,830.00 USD | 0.00 USD | 36,370.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3956.70` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 118,360.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3960.90` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 310,670.00 USD | 0.00 USD | 40,930.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3965.10` | 650,160.00 USD | 0.00 USD | 650,160.00 USD | 61,120.00 USD | 0.00 USD | 26,360.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3969.30` | 562,680.00 USD | 0.00 USD | 562,680.00 USD | 31,350.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.50` | 510,890.00 USD | 0.00 USD | 510,890.00 USD | 182,860.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3977.70` | 321,420.00 USD | 0.00 USD | 321,420.00 USD | 103,850.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3981.90` | 210,360.00 USD | 0.00 USD | 210,360.00 USD | 48,970.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3986.10` | 138,980.00 USD | 0.00 USD | 138,980.00 USD | 67,220.00 USD | 0.00 USD | 7,890.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3990.30` | 63,870.00 USD | 0.00 USD | 63,870.00 USD | 41,610.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3998.70` | 20,280.00 USD | 0.00 USD | 20,280.00 USD | 15,300.00 USD | 0.00 USD | 4,970.00 USD |
| `1D` | `4017.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4017.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 986,980.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4095.30` | 68,750.00 USD | 68,750.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `4097.10` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 726,830.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4099.50` | 197,260.00 USD | 197,260.00 USD | 0.00 USD | 121,750.00 USD | 0.00 USD | 6,760.00 USD |
| `7D` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 246,010.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4103.70` | 348,960.00 USD | 348,960.00 USD | 0.00 USD | 138,670.00 USD | 0.00 USD | 13,030.00 USD |
| `7D` | `4105.70` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 678,320.00 USD | 0.00 USD | 104,930.00 USD |
| `1D` | `4107.90` | 623,450.00 USD | 623,450.00 USD | 0.00 USD | 234,740.00 USD | 0.00 USD | 39,750.00 USD |
| `7D` | `4110.00` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4112.10` | 964,780.00 USD | 964,780.00 USD | 0.00 USD | 303,570.00 USD | 0.00 USD | 37,760.00 USD |
| `7D` | `4114.30` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4116.30` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 173,010.00 USD | 0.00 USD | 28,640.00 USD |
| `7D` | `4118.60` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4120.50` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 264,570.00 USD | 0.00 USD | 13,290.00 USD |
| `7D` | `4122.90` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4124.70` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 119,150.00 USD | 0.00 USD | 44,940.00 USD |
| `7D` | `4127.20` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4128.90` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 68,240.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `4131.50` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4133.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `4135.80` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4137.30` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 192,710.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `4140.10` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.50` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 11,410.00 USD |
| `7D` | `4144.40` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4145.70` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 54,840.00 USD | 0.00 USD | 11,010.00 USD |
| `7D` | `4148.70` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.90` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 42,110.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `1D` | `4154.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4157.30` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `1D` | `4158.30` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `4161.60` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `1D` | `4162.50` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 15,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4165.90` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 378,790.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 12,020,000.00 USD | 12,020,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4175.10` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `4178.80` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 295,540.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4179.30` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 46,740.00 USD | 0.00 USD | 5,240.00 USD |
| `7D` | `4183.10` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4183.50` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 72,440.00 USD | 0.00 USD | 5,150.00 USD |
| `7D` | `4187.40` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 327,960.00 USD | 0.00 USD | 53,390.00 USD |
| `1D` | `4187.70` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 17,020.00 USD |
| `7D` | `4191.70` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 607,230.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4191.90` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 131,450.00 USD | 0.00 USD | 20,220.00 USD |
| `7D` | `4196.00` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4196.10` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 102,820.00 USD | 0.00 USD | 15,140.00 USD |
| `1D` | `4200.30` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 92,780.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `4200.30` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4204.50` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 105,320.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `4204.60` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4208.70` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `4208.90` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4212.90` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 36,210.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4213.20` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4217.10` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 73,870.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4217.50` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4221.30` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 48,960.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4221.80` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4225.50` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 24,480.00 USD | 0.00 USD | 11,210.00 USD |
| `7D` | `4226.10` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4229.70` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 33,610.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `4230.40` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4233.90` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 20,800.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4234.70` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4242.30` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 7,650.00 USD | 0.00 USD | 2,490.00 USD |
| `7D` | `4389.50` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,680,000.00 USD | 15,680,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 124,220.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `1D` | `4414.50` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `4415.30` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4418.70` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `4419.60` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 90,410.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4422.90` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 16,900.00 USD | 0.00 USD | 2,330.00 USD |
| `7D` | `4423.90` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4427.10` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | 1,540.00 USD |
| `7D` | `4428.20` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 79,630.00 USD | 0.00 USD | 18,160.00 USD |
| `1D` | `4431.30` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 29,610.00 USD | 0.00 USD | 7,540.00 USD |
| `7D` | `4432.50` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 157,240.00 USD | 0.00 USD | 11,860.00 USD |
| `1D` | `4433.70` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 18,430.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `4436.80` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `7D` | `4441.10` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,910,000.00 USD | 16,910,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.26M` | Total OI Tokens: `68,251.6 PAXG`
  * 1h OI Change: `+0.11%` | 4h OI Change: `-0.60%` | 24h OI Change: `+0.34%`
  * Exchange Breakdown: Binance=`107.00M` | Bybit=`19.99M` | OKX=`-` | Hyperliquid=`25.06M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.35K` | Last 24h: `25.27K` | Last 3d: `95.73K` | Last 7d: `222.33K`
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
| `15M` | `PAXG` | `44.53%` | `55.47%` | `0.80` | 1,250,000.00 USD |
| `15M` | `Binance` | `29.08%` | `70.92%` | `0.41` | 782,160.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `42.88%` | `57.12%` | `0.75` | 13,130.00 USD |
| `15M` | `KuCoin` | `100%` | `0%` | `1.00` | 2,800.00 USD |
| `15M` | `Gate` | `83.91%` | `16.09%` | `5.22` | 21,460.00 USD |
| `15M` | `Bitget` | `64.79%` | `35.21%` | `1.84` | 159,210.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `19.01%` | `80.99%` | `0.23` | 7,610.00 USD |
| `15M` | `Bitunix` | `31.12%` | `68.88%` | `0.45` | 16,580.00 USD |
| `15M` | `Hyperliquid` | `99.66%` | `0.34%` | `293.12` | 112,830.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `60.62%` | `39.38%` | `1.54` | 119,400.00 USD |
| `15M` | `HTX` | `90.23%` | `9.77%` | `9.24` | 1,350.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.5%` | `53.5%` | `0.87` | 5,910.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 52.18 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `63.7%` | `36.3%` | `1.75` | 3,860.00 USD |
| `15M` | `Whale Positions` | `29.08%` | `70.92%` | `0.41` | 782,160.00 USD |
| `15M` | `Global Accounts` | `44.53%` | `55.47%` | `0.80` | 1,250,000.00 USD |
| `1H` | `PAXG` | `59.27%` | `40.73%` | `1.46` | 9,070,000.00 USD |
| `1H` | `Binance` | `68.55%` | `31.45%` | `2.18` | 761,860.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `49.64%` | `50.36%` | `0.99` | 1,060,000.00 USD |
| `1H` | `KuCoin` | `36.44%` | `63.56%` | `0.57` | 17,340.00 USD |
| `1H` | `Gate` | `61.45%` | `38.55%` | `1.59` | 454,450.00 USD |
| `1H` | `Bitget` | `54.85%` | `45.15%` | `1.21` | 376,130.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `62.52%` | `37.48%` | `1.67` | 4,890,000.00 USD |
| `1H` | `Bitunix` | `77%` | `23%` | `3.35` | 388,290.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.98%` | `51.02%` | `0.96` | 843,800.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `18.47%` | `81.53%` | `0.23` | 247,780.00 USD |
| `1H` | `HTX` | `31.41%` | `68.59%` | `0.46` | 1,450.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.15%` | `32.85%` | `2.04` | 28,120.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `68.55%` | `31.45%` | `2.18` | 761,860.00 USD |
| `1H` | `Global Accounts` | `59.27%` | `40.73%` | `1.46` | 9,070,000.00 USD |
| `4H` | `PAXG` | `51.74%` | `48.26%` | `1.07` | 60,680,000.00 USD |
| `4H` | `Binance` | `54.98%` | `45.02%` | `1.22` | 4,960,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `48.86%` | `51.14%` | `0.96` | 5,260,000.00 USD |
| `4H` | `KuCoin` | `49.91%` | `50.09%` | `1.00` | 363,920.00 USD |
| `4H` | `Gate` | `51.22%` | `48.78%` | `1.05` | 1,770,000.00 USD |
| `4H` | `Bitget` | `45.54%` | `54.46%` | `0.84` | 1,860,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `53.02%` | `46.98%` | `1.13` | 38,310,000.00 USD |
| `4H` | `Bitunix` | `61.23%` | `38.77%` | `1.58` | 1,880,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.55%` | `48.45%` | `1.06` | 4,660,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.34%` | `87.66%` | `0.14` | 1,430,000.00 USD |
| `4H` | `HTX` | `92.98%` | `7.02%` | `13.25` | 66,810.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.49%` | `49.51%` | `1.02` | 126,110.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.98%` | `45.02%` | `1.22` | 4,960,000.00 USD |
| `4H` | `Global Accounts` | `51.74%` | `48.26%` | `1.07` | 60,680,000.00 USD |


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
| `5m` | -126,410.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -217,560.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -189,630.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -363,400.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -627,680.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | 137,620.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `6h` | -32,030.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -251,170.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -280,260.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -441,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,490,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,480,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-126.41K` | 15m=`-217.56K` | 1h=`-363.40K` | 24h=`-441.34K`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4017.10` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4004.95` (Risk Distance: `12.15` pts)
  * +2.5R Take Profit: `4047.48`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4052.68` (Risk Distance: `12.15` pts)
  * +2.5R Take Profit: `4010.15`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4043.28`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
